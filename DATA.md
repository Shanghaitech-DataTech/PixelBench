# Data formats

All data come from the evaluation round reported in the paper. Configuration ids are those of `data/configs.json`:
the twelve main configurations (e.g. `gpt-6-astra`) and their variants, written `<base>@<variant>`
(`@run2`, `@run3`, `@effort-<level>`, `@no-vision`, `@direct`).

## `tasks/`

- `tasks/index.json`: one entry per task in the order of the paper's gallery: `id`, `family` (`text2image`, `edit`,
  `animation`, `multiview`), `subject` (text-to-image), `title`, `canvas`, `max_colors`, `frames`, `reference`
  (`gpt-image-2` or `source frames`), `first_frame_is_original`, `development_subset`, and for one task the canvas
  string the judge prompt carries verbatim (`judge_size`).
- `tasks/<family>/<id>/task.json`: the task statement the model receives, its canvas and constraints, and the write
  budget (`tool_budget.max_steps`).
- `initial.pixel.json` (and `base.pixel.json` for editing): the starting canvas as palette plus index matrix.
- `reference.png`: the task's reference image as the judge receives it (512 pixels on the longer side, with the
  protocol's margin).
- Editing tasks also have `original.png` (the input artwork), `frames/` (the source's own target frames, never shown
  to the model), `metadata.json`, and `source.json` (see `SOURCES.md`).

## `data/creations/<config>/<task>/`

- `frame_000.png`, `frame_001.png`, ...: the submitted artwork at native resolution, one PNG per frame.
- `program/`: every source file of the submitted run (the entry file is `submission.path` in the record).
- `answer.json.xz` (direct answers only): the model's answer text, parsed into the frames.
- `record.json`:
  - outcome: `ok`, `error` (exception class and HTTP status only), `termination` (`submitted`, `max_steps`,
    `long_request_cut`, ...), and `submission` (source `explicit` or `recovered`, frame counts, the run that was
    submitted and the SHA-256 of its source files);
  - effort: `writes` (source writes), `model_rounds`, `llm_calls`, `retries`, `colors`;
  - tokens: `prompt_tokens`, `cached_tokens`, `completion_tokens`, `reasoning_tokens`, and `calls_usage`, one
    `[prompt, cached, output including reasoning, reasoning]` entry per model call;
  - time: `seconds` (wall clock for the task), `llm_seconds`, `tool_seconds`;
  - `reasoning_effort`, only where a task ran at a different reasoning effort than its configuration.
- `transcript.json.xz` (the twelve main configurations): the episode as a list of entries: `llm_response` (the model's
  text, its reasoning where the endpoint returned it, tool calls, token usage, latency), `tool_call`, `code` (each
  tool execution and its output), and the final `submission`.

Release processing, applied uniformly: paths of the evaluation machine (absolute, or relative to its working
directories) inside programs and transcripts are replaced by `/workspace` (the run directory), `/env` (the Python environment) or `/host` (anything else), and
`record.json` lists any program file changed this way (`paths_neutralized`); transcripts omit request metadata,
response headers, opaque reasoning payloads and timestamps, keeping latencies; errors keep the exception class and
HTTP status. Images sent to the model are referenced by their SHA-256 (`image_sha256`).

## `data/judge/`

- `final_protocol.jsonl`: the final protocol (`e3_reference`) on every artwork: `task`, `config`, `score`, `raw` (the
  judge's reply), `message` (the prompt text), `images` (SHA-256 of each PNG sent: `candidate`, `reference`,
  `original` for editing), `image_pixels` (SHA-256 of the decoded pixels, independent of the PNG encoder), and
  `attempts`. Direct answers without a valid answer have no row and score 0.
- `protocol_versions.jsonl`: the versions `e0_base`, `e1_margin` and `e2_rubric` on the artworks of the main table.
- `repeat_passes.jsonl`: three further passes of the final protocol over 144 artworks of 12 tasks (`pass` 1-3,
  `first_pass_score`).
- `other_judges.jsonl`: Claude Opus 5 (reasoning effort low) and DeepSeek V4.1 Flash (high) as judges under the
  final protocol, on the artworks of the main table. Claude Opus 5 returned no score for two artworks of
  `fist-swing` (`score` null).

## `data/human/`

`R01.json` ... `R10.json`, one per rater: `reference_mode` (`with_reference` or `without_reference`) and, per task,
the `ranking` (configuration ids from best to worst), the `initial_order` of the cards, and the `seconds` spent.

## `data/cost/prices.json`, `data/configs.json`

List prices in USD per million tokens with the pricing rules of the paper's cost table, and the list of
configurations with their roles.
