"""Benchmark runner: tasks x agents -> episodes -> metrics -> judge -> report."""
from __future__ import annotations

import json
import shutil
import traceback
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from pixelbench.agents.base import Agent, AgentResult, Budget
from pixelbench.eval.judge import EpisodeView, Judge
from pixelbench.eval.metrics import compute_metrics
from pixelbench.eval.report import EpisodeRecord, RunReport, save_episode
from pixelbench.repl.file_session import FileSession as KernelSession
from pixelbench.repl.prelude import build_prelude
from pixelbench.tasks.specs import TaskSpec


class BenchmarkRunner:
    def __init__(
        self,
        tasks: List[TaskSpec],
        agents: List[Agent],
        judge: Optional[Judge] = None,
        out_dir: str = "outputs",
        seed: int = 0,
        max_tasks: Optional[int] = None,
        observe: bool = True,
    ) -> None:
        self.tasks = tasks[:max_tasks] if max_tasks else list(tasks)
        self.agents = agents
        # judge may be None ("judge": {"type": "none"}): episodes are then scored with
        # deterministic hard metrics only and no LLM is called. Task types that have ground
        # truth and can be evaluated deterministically, such as restore, need no judge.
        self.judge = judge
        self.out_dir = Path(out_dir)
        self.seed = seed
        self.observe = bool(observe)

    def run(self) -> RunReport:
        from pixelbench import tracing

        # optional: mirror OpenAI Agents SDK traces to Arize Phoenix
        # (PIXELBENCH_TRACE_BACKEND=phoenix)
        tracing.maybe_enable_phoenix_from_env()
        run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        records: List[EpisodeRecord] = []
        total = len(self.tasks) * len(self.agents)
        i = 0
        for task in self.tasks:
            for agent in self.agents:
                i += 1
                print(f"[pixelbench] episode {i}/{total}: {task.id} x {agent.name} ...", flush=True)
                rec = self._run_episode(task, agent)
                records.append(rec)
                status = "ok" if rec.ok else f"FAIL ({rec.error})"
                print(f"  -> {status}  steps={rec.steps}", flush=True)
        report = RunReport(run_id, records, config={"seed": self.seed})
        report.save(self.out_dir)
        return report

    def _run_episode(self, task: TaskSpec, agent: Agent) -> EpisodeRecord:
        session: Optional[KernelSession] = None
        episode_dir = self.out_dir / "episodes" / f"{task.id}__{agent.name}"
        # wipe any previous run's episode directory: the observer appends to
        # calls.jsonl / turns.jsonl and writes per-turn frames, so reusing a
        # stale directory would mix observations from different runs (and
        # inflate the record's observation stats)
        if episode_dir.exists():
            shutil.rmtree(episode_dir)
        obs_dir = episode_dir / "observations"
        if self.observe and agent.requires_repl:
            obs_dir.mkdir(parents=True, exist_ok=True)
        try:
            from pixelbench import tracing

            # point the OpenAI Agents SDK trace sink (and any other
            # per-episode loggers) at this episode's directory
            tracing.set_current_episode_dir(str(episode_dir) if self.observe else None)
            if agent.requires_repl:
                session = KernelSession(root=episode_dir)
                session.start(timeout=90)
                frames_state = None
                if task.task_type == "animation" and task.frames_visible and task.frames:
                    from pixelbench.core.serialization import to_pixel_json

                    frames_state = [
                        to_pixel_json(f, id_=f"{task.id}_ref_frame_{i}")
                        for i, f in enumerate(task.frames)
                    ]
                prelude = build_prelude(
                    task=task.public_task(),
                    initial_state=task.initial_state(),
                    reference_state=task.reference_state() if task.reference_visible else None,
                    mask_state=task.mask_state(),
                    frames_state=frames_state,
                    seed=self.seed,
                    observer_dir=str(obs_dir) if self.observe else None,
                    surface=getattr(agent, "prelude_surface", "full"),
                )
                session.execute_checked(prelude, timeout=60, what="prelude")

            budget = Budget.from_task(task)
            result = agent.run(task, session, budget)
            final_frames = list(result.final_frames or ([result.final_canvas] if result.final_canvas is not None else []))
            if not final_frames and session is not None:
                try:
                    final_frames, result.submission = session.extract_submission()
                except Exception:
                    pass
            final = final_frames[-1] if final_frames else None
            result.final_canvas = final
            result.final_frames = final_frames
            # agentic tool-use statistics come from the painting-process
            # observer's call log (records every model call incl. palette
            # registration, and survives canvas serialization)
            obs_calls: Optional[List[dict]] = None
            calls_path = Path(obs_dir) / "calls.jsonl"
            if calls_path.exists():
                obs_calls = [json.loads(l) for l in calls_path.read_text().splitlines() if l.strip()]
            metrics = (
                compute_metrics(task, final, result, obs_calls=obs_calls)
                if final is not None
                else {}
            )
            judge_scores = None
            judge_view = None
            if final is not None:
                corrupted = None
                if task.task_type == "restoration" and task.reference is not None:
                    corrupted = task.reference.copy()
                    corrupted.matrix[task.mask] = corrupted.transparent_id
                visible_ref = task.reference if (task.reference_visible or task.task_type == "restoration") else None
                judge_view = EpisodeView(
                    task=task,
                    agent_name=agent.name,
                    final_canvas=final,
                    final_frames=final_frames,
                    reference=visible_ref,
                    corrupted=corrupted,
                    mask=task.mask,
                    original=task.base if task.task_type == "edit" else None,
                    metrics=metrics,
                )
                # judge_view is assembled even without a judge ("type": "none"): it also carries
                # the reference / corrupted renders used by the report; only the LLM call is skipped.
                if self.judge is not None:
                    try:
                        judge_scores = self.judge.score(judge_view)
                    except Exception as e:  # judge failures should not sink the episode
                        judge_scores = {"error": f"{type(e).__name__}: {e}"}

            images = {}
            if final is not None:
                images["final"] = final.render_png_bytes(scale=8)
                images["final_1x"] = final.render_png_bytes(scale=1)
            if judge_view is not None and judge_view.reference is not None:
                images["reference"] = judge_view.reference.render_png_bytes(scale=8)
            if judge_view is not None and judge_view.original is not None:
                images["original"] = judge_view.original.render_png_bytes(scale=8)
            if judge_view is not None and judge_view.corrupted is not None:
                images["corrupted"] = judge_view.corrupted.render_png_bytes(scale=8)
            if final_frames:
                for i, f in enumerate(final_frames):
                    images[f"frame_{i:03d}"] = f.render_png_bytes(scale=8)

            record = EpisodeRecord(
                task_id=task.id,
                task_type=task.task_type,
                agent=agent.name,
                ok=result.ok and final is not None,
                steps=result.steps_used,
                error=result.error,
                metrics=metrics,
                judge=judge_scores,
                images=images,
                transcript=result.transcript,
                submission=result.submission,
                episode_dir=str(episode_dir) if self.observe else None,
            )
            if session is not None and session.checkpoint_path.is_file():
                episode_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(session.checkpoint_path, episode_dir / 'workspace.json')
            # persist this episode immediately so an interrupted run keeps it
            try:
                save_episode(self.out_dir, record)
            except Exception:  # noqa: BLE001 - never sink the episode
                pass
            return record
        except Exception as e:  # noqa: BLE001 - keep the benchmark running
            return EpisodeRecord(
                task_id=task.id,
                task_type=task.task_type,
                agent=agent.name,
                ok=False,
                error=f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=3)}",
                episode_dir=str(episode_dir) if self.observe else None,
            )
        finally:
            from pixelbench import tracing

            tracing.set_current_episode_dir(None)
            if session is not None:
                session.shutdown()
