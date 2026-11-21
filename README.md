# PixelBench: Evaluating Language Models for Pixel-Art Creation

<p align="center">
  <a href="https://arxiv.org/abs/2611.20628">Paper</a> &nbsp;·&nbsp;
  <a href="https://www.datatech.club/PixelBench/">Project page</a> &nbsp;·&nbsp;
  <a href="https://github.com/Shanghaitech-DataTech/PixelSkill">PixelSkill</a>
</p>

<p align="center">
  Mutian Hong<sup>1,3</sup>, Jianxuan Yao<sup>2,*</sup>, Mingkun Yue<sup>2,*</sup>, Changkai Li<sup>1</sup>, Hower Yang, Haibin Ling<sup>1</sup><br>
  <sup>1</sup>Westlake University &nbsp; <sup>2</sup>ShanghaiTech University &nbsp; <sup>3</sup>Mind Lab &nbsp; <sup>*</sup>Equal contribution
</p>

<p align="center"><img src="docs/teaser.png" alt="Pixel artworks created by GPT-6 Astra on PixelBench tasks" width="100%"></p>

PixelBench evaluates language models as pixel-art creators. Each of its 100 tasks asks for a native pixel artwork
under a specified canvas size and color ceiling: 75 text-to-image tasks across seven subjects on canvases from 16×16
to 256×256, and 25 editing tasks that start from an existing artwork (13 instruction edits, 10 animations and 2
multiview turnarounds). Models create in an agentic environment: they write Python programs against a pixel-art
drawing API, run them in a sandbox and look at the result. Ten raters with professional art backgrounds ranked all
1,200 artworks of the twelve main configurations, and a calibrated multimodal judge, GPT-6 Astra at reasoning effort
xhigh, scores every artwork from 0 to 100.

| Directory | Contents |
|---|---|
| `pixelbench/` | The creation environment: canvas and drawing API, the file workspace in which a model writes and runs programs, the sandbox every program runs in, the agent loop, and the judge protocol. |
| `pixelbench/protocol.py` | The creation protocol: write budgets, time limits, and the rerun rule. |
| `scripts/` | `run_benchmark.py` (agentic creation), `run_direct.py` (direct-answer baseline), `run_judge.py` (judge scoring and verification), `reproduce_paper.py` and `cost.py` (the paper's numbers from the released data). |
| `configs/` | The model configurations of the paper (`configs/models/`) and the judge settings (`configs/judge.json`). |
| `tasks/` | The 100 tasks: 75 text-to-image tasks and 25 editing tasks (13 instruction edits, 10 animations, 2 multiviews), with the reference image of each task exactly as the judge receives it. |
| `data/` | The complete evaluation round: all artworks with their programs and run records, the transcripts of the twelve main configurations, every judge response, the ten raters' complete rankings, and the price table. |

[PROTOCOL.md](PROTOCOL.md) describes the protocol, [DATA.md](DATA.md) the data formats, and
[SOURCES.md](SOURCES.md) the sources of the editing inputs.

## Leaderboard

Twenty configurations on all 100 tasks: the twelve models of the paper's main table (bold), each at the reasoning
effort listed there, and the further reasoning-effort levels of GPT-6 Astra, DeepSeek V4 Flash and GLM-5.3 Flash.
Scores are mean judge scores from 0 to 100 over the tasks of each column. Human rank is the mean within-task rank
among the twelve main-table configurations over the ten raters (1 is best); the other effort levels are scored by
the judge only. The two Qwen models take a thinking budget instead of an effort level.

| # | Model | Reasoning effort | All (100) | Generation (75) | Editing (25) | Human rank |
|---:|---|---|---:|---:|---:|---:|
| 1 | GPT-6 Astra | xhigh | 84.68 | 83.61 | 87.88 | – |
| 2 | **GPT-6 Astra** | **high** | 83.76 | 82.35 | 88.00 | 3.34 |
| 3 | GPT-6 Astra | medium | 82.44 | 80.80 | 87.36 | – |
| 4 | GPT-6 Astra | low | 81.83 | 80.51 | 85.80 | – |
| 5 | **Claude Opus 5** | **low** | 78.49 | 77.64 | 81.04 | 4.88 |
| 6 | **Qwen3.8 Max** | **thinking budget** | 78.04 | 77.35 | 80.12 | 5.13 |
| 7 | **Gemini 3.8 Flash** | **high** | 77.35 | 77.87 | 75.80 | 4.27 |
| 8 | **GPT-5.6 Sol** | **medium** | 76.92 | 76.29 | 78.80 | 5.91 |
| 9 | **DeepSeek V4.1 Flash** | **high** | 75.70 | 76.27 | 74.00 | 6.45 |
| 10 | **GLM-5.3 Flash** | **max** | 74.98 | 75.44 | 73.60 | 6.53 |
| 11 | **Kimi K3** | **max** | 74.45 | 74.23 | 75.12 | 6.42 |
| 12 | GLM-5.3 Flash | high | 69.84 | 72.20 | 62.76 | – |
| 13 | **Gemini 3.1 Pro Preview** | **high** | 69.51 | 68.13 | 73.64 | 6.78 |
| 14 | **DeepSeek V4 Pro** | **high** | 67.41 | 67.73 | 66.44 | 8.74 |
| 15 | DeepSeek V4 Flash | max | 66.12 | 68.00 | 60.48 | – |
| 16 | **DeepSeek V4 Flash** | **high** | 65.52 | 66.88 | 61.44 | 9.08 |
| 17 | GLM-5.3 Flash | low | 62.63 | 65.13 | 55.12 | – |
| 18 | DeepSeek V4 Flash | none | 62.35 | 64.87 | 54.80 | – |
| 19 | DeepSeek V4 Flash | low | 60.97 | 62.91 | 55.16 | – |
| 20 | **Qwen3.5-397B-A17B** | **thinking budget** | 55.60 | 57.89 | 48.72 | 10.47 |

Per task, the judge's scores agree with the consensus order of the ten raters at Kendall τ = 0.557
[0.520, 0.593]; under leave-one-out the judge reaches 0.554 and the held-out
raters 0.465 to 0.649. Every artwork, with its judge score, is on the
[project page](https://www.datatech.club/PixelBench/).

## Setup

Python 3.12 on Linux (x86-64, kernel 5.13 or later for the sandbox):

```bash
pip install -c constraints-py312.txt -e .
```

## Reproduce the paper's numbers (no model calls)

```bash
python scripts/reproduce_paper.py      # leaderboards, judge-human agreement, protocol versions, repeat scoring,
                                       # other judges, raters, repeated creation, reasoning effort, direct answers
python scripts/cost.py                 # tokens, time and cost per task
python scripts/run_judge.py --verify   # rebuild every judge input (prompt and images) and compare with the records
```

`run_judge.py --verify` rebuilds all 6,450 judge calls of the evaluation (the final protocol on every artwork and
the three earlier protocol versions on the main artworks) from the released tasks and artworks, and checks the
prompt text and the decoded pixels of every image against the released judge records.

## Evaluate a model

Any OpenAI-compatible endpoint works. Copy `.env.example` to `.env` or export the variables:

```bash
export PIXELBENCH_BASE_URL=https://your-endpoint/v1
export PIXELBENCH_API_KEY=...
python scripts/run_benchmark.py --config configs/models/gpt-6-astra.json --out runs/gpt-6-astra
```

A new configuration is a JSON file in the format of `configs/models/` (model name, request format, vision, and
any request fields). Every program the model writes runs in the sandbox; `--unsafe-no-sandbox` exists only for
platforms without Landlock, and its results are not comparable. The output directory has the layout of
`data/creations/<config>/`, so the judge reads it directly:

```bash
export PIXELBENCH_JUDGE_BASE_URL=https://your-judge-endpoint/v1
export PIXELBENCH_JUDGE_API_KEY=...
python scripts/run_judge.py --creations runs/gpt-6-astra --config-id my-run --out runs/gpt-6-astra.judge.jsonl
```

The mean judge score over the 100 tasks places a new configuration on the leaderboard of the paper.

## PixelSkill

The creation environment also ships as [PixelSkill](https://github.com/Shanghaitech-DataTech/PixelSkill), an agent
skill that brings the same canvas and drawing primitives to general-purpose coding agents.

## Licenses

The code is released under the MIT license (`LICENSE`). Task statements, artworks produced by the evaluated
models, human rankings and judge responses are released for research use. The editing inputs come from the works
listed in [SOURCES.md](SOURCES.md) and remain under their original terms.

## Citation

```bibtex
@misc{hong2026pixelbench,
  title         = {PixelBench: Evaluating Language Models for Pixel-Art Creation},
  author        = {Mutian Hong and Jianxuan Yao and Mingkun Yue and Changkai Li and Hower Yang and Haibin Ling},
  year          = {2026},
  eprint        = {2611.20628},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url           = {https://arxiv.org/abs/2611.20628}
}
```
