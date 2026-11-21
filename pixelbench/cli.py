"""Command line interface: ``python -m pixelbench ...``."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from pixelbench.agents import build_agent
from pixelbench.config import BenchmarkConfig
from pixelbench.eval.judge import build_judge
from pixelbench.runner import BenchmarkRunner


def cmd_demo(args: argparse.Namespace) -> int:
    cfg = BenchmarkConfig(
        tasks="smoke",
        agents=[
            {"type": "mock-direct", "name": "mock-direct"},
            {"type": "mock-repl", "name": "mock-repl"},
        ],
        judge={"type": "mock"},
        out_dir=args.out,
        seed=7,
    )
    print(f"[pixelbench] demo run -> {cfg.out_dir} (mock agents, no LLM)")
    report = _run(cfg)
    _print_summary(report)
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    cfg_path = Path(args.config)
    if not cfg_path.is_file():
        print(f"run: config file not found: {cfg_path}", file=sys.stderr)
        print("  example: python -m pixelbench run --config examples/config.sdk.json", file=sys.stderr)
        return 1
    cfg = BenchmarkConfig.from_json(str(cfg_path))
    if args.out:
        cfg.out_dir = args.out
    print(f"[pixelbench] running benchmark from {cfg_path}")
    report = _run(cfg)
    _print_summary(report)
    return 0


def cmd_gen_tasks(args: argparse.Namespace) -> int:
    from pixelbench.tasks.smoke import smoke_tasks
    from pixelbench.tasks.specs import save_task_dir

    out = Path(args.out)
    for spec in smoke_tasks():
        save_task_dir(spec, out / spec.task_type / spec.id)
    print(f"[pixelbench] wrote {len(smoke_tasks())} smoke task dirs to {out}")
    return 0


def cmd_check_repl(args: argparse.Namespace) -> int:
    from pixelbench.repl.kernel import KernelSession

    print("[pixelbench] starting a test kernel...")
    s = KernelSession()
    try:
        s.start(timeout=60)
        r = s.execute("import pixelbench; print('kernel ok', pixelbench.__version__)", timeout=30)
        print(r.combined())
        ok = r.ok
    finally:
        s.shutdown()
    return 0 if ok else 1


def cmd_sample_sdk_trace(args: argparse.Namespace) -> int:
    """Generate a sample OpenAI Agents SDK trace + process viewer for
    previewing the local trace viewer without an API key."""
    from pixelbench.tracing import write_sample_sdk_trace

    target = write_sample_sdk_trace(str(args.out))
    print(f"[pixelbench] sample SDK trace written; open in a browser:\n  {target}")
    return 0


def cmd_serve_phoenix(args: argparse.Namespace) -> int:
    """Run the Arize Phoenix trace-viewer server (open-source, local).

    Phoenix collects OpenAI Agents SDK traces (via OpenInference OTLP
    instrumentation) and serves a proper trace-tree UI.  Traces are
    stored in a SQLite database under ``--data`` so they survive
    restarts.  Ctrl-C to stop.
    """
    import os
    import shutil
    import subprocess

    data = Path(args.data)
    data.mkdir(parents=True, exist_ok=True)
    if shutil.which("phoenix") is None:  # pragma: no cover
        print("serve-phoenix: 'phoenix' CLI not found; run: pip install arize-phoenix", file=sys.stderr)
        return 1
    # run phoenix inside a python -c wrapper so the starlette-compat patch
    # applies in the same process that serves the UI
    wrapper = (
        "import starlette.templating as _st\n"
        "_orig = _st.Jinja2Templates.TemplateResponse\n"
        "def _compat(self, *a, **kw):\n"
        "    # phoenix 13.6.0: TemplateResponse('index.html', context={...})\n"
        "    # starlette>=1.x:  TemplateResponse(request, name, context)\n"
        "    if a and isinstance(a[0], str) and 'context' in kw:\n"
        "        _ctx = kw['context']\n"
        "        _req = _ctx.get('request')\n"
        "        return _orig(self, _req, a[0], context=_ctx)\n"
        "    return _orig(self, *a, **kw)\n"
        "_st.Jinja2Templates.TemplateResponse = _compat\n"
        "import sys\n"
        "sys.argv = ['phoenix', 'serve']\n"
        "from phoenix.server.main import main\n"
        "main()\n"
    )
    env = dict(os.environ, PHOENIX_PORT=str(args.port))
    print(f"[pixelbench] Arize Phoenix trace viewer: http://{args.host}:{args.port} (Ctrl-C to stop)")
    print(f"[pixelbench] data dir: {data}  (set PIXELBENCH_TRACE_BACKEND=phoenix to send SDK traces here)")
    try:
        return subprocess.call([sys.executable, "-c", wrapper], cwd=data, env=env)
    except KeyboardInterrupt:
        print("\n[pixelbench] stopped")
        return 0


def cmd_serve_traces(args: argparse.Namespace) -> int:
    """Serve the live Agent Trace dashboard over HTTP.

    The page polls ``/manifest.json`` and re-renders every
    ``observations/sdk_trace.jsonl`` under the directory as a trace
    tree, so traces appear live while a benchmark runs.  Ctrl-C to stop.
    """
    from http.server import ThreadingHTTPServer

    from pixelbench.observe import make_traces_handler

    out = Path(args.out).resolve()
    if not out.is_dir():
        print(f"serve-traces: no such directory: {out}", file=sys.stderr)
        return 1
    handler = make_traces_handler(out)
    host, port = args.host, int(args.port)
    httpd = ThreadingHTTPServer((host, port), handler)
    url = f"http://{host}:{port}/"
    print(f"[pixelbench] Agent Trace viewer: {url} (Ctrl-C to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[pixelbench] stopped")
    return 0


def cmd_phoenix_replay(args: argparse.Namespace) -> int:
    """Replay finished episodes (observations + trace.jsonl) into a running
    local Arize Phoenix as OpenInference spans with inline pixel-art images."""
    from pixelbench.phoenix_pixel import replay_run_to_phoenix

    n = replay_run_to_phoenix(args.run, project=args.project)
    return 0 if n else 1


def cmd_serve(args: argparse.Namespace) -> int:
    """Serve a benchmark output directory over HTTP for browsing.

    Generates an index page linking every episode's process viewer
    (``process.html``), gallery and records, then serves the directory
    with ``http.server`` (threaded).  Ctrl-C to stop.
    """
    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

    out = Path(args.out).resolve()
    if not out.is_dir():
        print(f"serve: no such directory: {out}", file=sys.stderr)
        return 1
    _write_run_index(out)

    handler = _make_index_handler(out)
    host, port = args.host, int(args.port)
    httpd = ThreadingHTTPServer((host, port), handler)
    url = f"http://{host}:{port}/"
    print(f"[pixelbench] serving {out} at {url} (Ctrl-C to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[pixelbench] stopped")
    return 0


def cmd_serve_web(args: argparse.Namespace) -> int:
    """Serve the interactive PixelBench Agent Test Console (the web UI).

    Starts the FastAPI backend in ``webapp/server.py`` which drives the
    REPL harness live: pick a task, start an episode (mock or real LLM),
    and watch the agent paint round by round — every executed code block
    pushes a canvas snapshot to the browser whether or not the model
    itself asked to see it.  Ctrl-C to stop.
    """
    import sys

    import pixelbench

    repo_root = Path(pixelbench.__file__).resolve().parent.parent
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

    import uvicorn

    from webapp.server import app

    host, port = args.host, int(args.port)
    url = f"http://{host}:{port}/"
    print(f"[pixelbench] PixelBench Agent Test Console: {url} (Ctrl-C to stop)")
    print(f"[pixelbench] mock LLM works out of the box; real models: set PIXELBENCH_API_KEY (and PIXELBENCH_BASE_URL) in .env, or pass llm.api_key in the request")
    try:
        uvicorn.run(app, host=host, port=port, log_level="warning")
    except KeyboardInterrupt:
        print("\n[pixelbench] stopped")
    return 0


def _write_run_index(out: Path) -> None:
    """Write a friendly index.html for the served run directory
    (final-image thumbnails + links to viewers / records)."""
    episodes = sorted(out.glob("episodes/*"))
    cards = []
    for d in episodes:
        rec_path = d / "record.json"
        meta = {}
        if rec_path.exists():
            try:
                meta = json.loads(rec_path.read_text(encoding="utf-8"))
            except Exception:
                meta = {}
        obs = meta.get("observations")
        links = []
        if (d / "process.html").exists():
            links.append(f'<a href="episodes/{d.name}/process.html">process viewer</a>')
        if (d / "record.json").exists():
            links.append(f'<a href="episodes/{d.name}/record.json">record.json</a>')
        thumbs = []
        for n in ("reference", "corrupted", "final", "final_1x"):
            if (d / f"{n}.png").is_file():
                thumbs.append(f'<a href="episodes/{d.name}/{n}.png"><img src="episodes/{d.name}/{n}.png" alt="{n}"></a>')
        if thumbs or links:
            tag = "ok" if meta.get("ok") else "FAIL"
            info = ""
            if obs:
                info = (f'<span class="muted">turns={obs.get("turns")} calls={obs.get("calls")} '
                        f'diffs={obs.get("diff_images")}</span>')
            cards.append(
                f'<div class="card"><h3>{d.name} <span class="tag">{tag}</span></h3>'
                f'<p class="muted">{meta.get("task_type", "")} · steps={meta.get("steps", "?")} {info}</p>'
                f'{"".join(thumbs) or ""}'
                f'<p>{" · ".join(links)}</p></div>'
            )
    index = (
        "<!DOCTYPE html><html lang=\"zh\"><head><meta charset=\"utf-8\">"
        "<title>PixelBench run — model outputs</title><style>"
        "body{background:#1c1c22;color:#ddd;font-family:system-ui,sans-serif;margin:24px}"
        "h1{font-size:20px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px}"
        ".card{background:#26262e;border-radius:10px;padding:12px 16px}"
        "h3{margin:0 0 6px;font-size:14px}.tag{color:#7bd}.muted{color:#889;font-size:12px}"
        "a{color:#7bd;text-decoration:none}p{margin:6px 0}"
        "img{image-rendering:pixelated;height:56px;border-radius:4px;border:1px solid #444;margin:2px 4px 2px 0;"
        "background:repeating-conic-gradient(#3a3a44 0% 25%,#2a2a32 0% 50%) 0 0/16px 16px}"
        "</style></head><body>"
        f"<h1>PixelBench run — {out.name} (images produced by the models)</h1>"
        f'<p class="muted"><a href="gallery.html">gallery.html</a> · '
        f'<a href="contact_sheet.png">contact_sheet.png</a> · '
        f'<a href="summary.json">summary.json</a> · <a href="summary.md">summary.md</a> · '
        f'<a href="traces.html">trace viewer</a> (requires serve-traces)</p>'
        f'<div class="grid">{"".join(cards) or "<p>no episodes found</p>"}</div>'
        "</body></html>"
    )
    (out / "index.html").write_text(index, encoding="utf-8")


def _make_index_handler(out: Path):
    """http.server handler that serves ``index.html`` by default."""
    from http.server import SimpleHTTPRequestHandler

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(out), **kw)

        def do_GET(self):
            if self.path in ("/", ""):
                self.path = "/index.html"
            return super().do_GET()

        def log_message(self, *a):  # quieter logs
            pass

    return Handler


def _run(cfg: BenchmarkConfig):
    tasks = cfg.load_tasks()
    agents = [build_agent(a) for a in cfg.agents]
    judge = build_judge(cfg.judge)
    runner = BenchmarkRunner(
        tasks, agents, judge, out_dir=cfg.out_dir, seed=cfg.seed, max_tasks=cfg.max_tasks, observe=cfg.observe
    )
    return runner.run()


def _print_summary(report) -> None:
    print(f"\n[pixelbench] run {report.run_id} saved to {report.out_dir}")
    summary = report.summary()
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="python -m pixelbench", description="PixelBench agentic pixel-art benchmark harness")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("demo", help="run the smoke tasks with mock agents (no LLM, offline)")
    p.add_argument("--out", default="outputs/demo")
    p.set_defaults(func=cmd_demo)

    p = sub.add_parser("run", help="run a benchmark from a config JSON")
    p.add_argument("--config", required=True)
    p.add_argument("--out")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("gen-tasks", help="materialize the smoke task set as task dirs")
    p.add_argument("--out", default="tasks/smoke")
    p.set_defaults(func=cmd_gen_tasks)

    p = sub.add_parser("check-repl", help="verify the ipykernel sandbox works")
    p.set_defaults(func=cmd_check_repl)

    p = sub.add_parser("sample-sdk-trace", help="write a sample OpenAI Agents SDK trace + viewer (preview without an API key)")
    p.add_argument("--out", default="outputs/sample_sdk_trace")
    p.set_defaults(func=cmd_sample_sdk_trace)

    p = sub.add_parser("serve", help="serve a benchmark output directory over HTTP (browse images / process viewers)")
    p.add_argument("--out", default="outputs/demo")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", default="8000")
    p.set_defaults(func=cmd_serve)

    p = sub.add_parser("serve-web", help="serve the interactive PixelBench Agent Test Console (live web UI for watching an agent paint)")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", default="8090")
    p.set_defaults(func=cmd_serve_web)

    p = sub.add_parser("serve-traces", help="serve the live Agent Trace dashboard (auto-refreshing trace trees)")
    p.add_argument("--out", default="outputs/demo")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", default="8001")
    p.set_defaults(func=cmd_serve_traces)

    p = sub.add_parser("serve-phoenix", help="run the Arize Phoenix trace viewer (open-source, local, proper trace UI)")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", default="6006")
    p.add_argument("--data", default="outputs/phoenix_data")
    p.set_defaults(func=cmd_serve_phoenix)

    p = sub.add_parser(
        "phoenix-replay",
        help="replay finished episodes into a running local Phoenix as OpenInference spans "
             "(model steps + tools + inline pixel-art frames); requires phoenix on :6006",
    )
    p.add_argument("--run", default="outputs/showcase_128")
    p.add_argument("--project", default="pixelbench-showcase")
    p.set_defaults(func=cmd_phoenix_replay)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
