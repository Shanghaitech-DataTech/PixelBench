"""Harness-side observation artifacts: per-episode HTML process viewer.

After a benchmark episode finishes, the runner / report writer calls
:func:`write_process_viewer` to render a self-contained ``process.html``
next to the episode's ``record.json``.  The page embeds the agent
transcript, the kernel-side observation logs (turns + tool calls) and
the OpenAI Agents SDK trace (when present) as JSON, and references the
frame / diff PNGs written by the kernel observer, so it works over
``file://`` with no server and no external dependencies.

The same SDK-trace tree renderer powers :data:`TRACES_PAGE`, a live
trace dashboard served by ``python -m pixelbench serve-traces`` (it
polls ``/manifest.json`` and re-renders trace trees as a benchmark run
writes ``sdk_trace.jsonl`` files).

Episode observation layout (written live by the kernel during the run)::

    <episode>/observations/
        calls.jsonl      one line per drawing tool call
        turns.jsonl      one line per executed code block (+ initial)
        frames/turn_NNNN.png      canvas state after each block
        diffs/call_NNNNNN.png     before|after diff per mutating call
        sdk_trace.jsonl  native OpenAI Agents SDK trace lines (SDK agent)
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

OBS_DIRNAME = "observations"


def observation_dir(episode_dir: Path) -> Path:
    return Path(episode_dir) / OBS_DIRNAME


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    """Tolerantly read a JSONL file (skips corrupt lines)."""
    out: List[Dict[str, Any]] = []
    try:
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:  # pragma: no cover
                    continue
                if isinstance(obj, dict):
                    out.append(obj)
    except FileNotFoundError:
        pass
    return out


def collect_observation_stats(episode_dir: Path) -> Dict[str, Any]:
    """Counts for record.json's ``observations`` field.

    Returns an empty dict when nothing was observed (e.g. direct
    agents that never touch a kernel).
    """
    odir = observation_dir(episode_dir)
    calls = read_jsonl(odir / "calls.jsonl")
    turns = read_jsonl(odir / "turns.jsonl")
    sdk_path = odir / "sdk_trace.jsonl"
    frames = [p for p in (odir / "frames").glob("*.png")] if (odir / "frames").is_dir() else []
    if not calls and not turns and not frames and not sdk_path.is_file():
        return {}
    return {
        "dir": OBS_DIRNAME,
        "viewer": "process.html",
        "calls": len(calls),
        "turns": len(turns),
        "diff_images": sum(1 for c in calls if c.get("diff")),
        "frames": len(frames),
        "sdk_trace": sdk_path.is_file(),
    }


# ----------------------------------------------------------------------
# shared page CSS + SDK trace tree renderer (used by both pages)
# ----------------------------------------------------------------------
_PAGE_CSS = """
 body { background:#1c1c22; color:#d9d9e3; font-family:system-ui,-apple-system,sans-serif; margin:0; padding:24px; }
 h1 { font-size:20px; margin:0 0 4px; } h2 { font-size:15px; color:#9ab; margin:28px 0 8px; }
 .muted { color:#889; font-size:12px; } .tag { color:#7bd; }
 .cards { display:flex; flex-wrap:wrap; gap:14px; margin:12px 0; }
 .card { background:#26262e; border-radius:10px; padding:12px 14px; min-width:200px; }
 .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:14px; }
 .imgs { display:flex; flex-wrap:wrap; gap:14px; }
 figure { margin:0; } figcaption { font-size:11px; color:#889; margin-top:4px; text-align:center; }
 img { image-rendering:pixelated; background:repeating-conic-gradient(#3a3a44 0% 25%, #2a2a32 0% 50%) 0 0/16px 16px; border-radius:6px; border:1px solid #444; max-width:100%; }
 .tl { border-left:2px solid #333; margin-left:8px; padding-left:18px; }
 .item { margin:14px 0; background:#23232b; border:1px solid #333; border-radius:10px; padding:12px 14px; }
 .item h3 { margin:0 0 6px; font-size:14px; }
 .item .meta { font-size:12px; color:#889; margin-bottom:8px; }
 pre { background:#16161c; border:1px solid #2c2c36; border-radius:8px; padding:10px; overflow-x:auto; font-size:12px; line-height:1.45; margin:6px 0; }
 details { margin:6px 0; } summary { cursor:pointer; color:#9db8d2; font-size:12px; }
 .call { margin:8px 0 0 8px; padding:8px 10px; background:#1e1e26; border-left:3px solid #556; border-radius:6px; }
 .call .op { font-weight:600; color:#7bd; } .call .chg { color:#f79; }
 .opstats { margin:8px 0 0; display:flex; flex-wrap:wrap; gap:5px; align-items:center; }
 .opchip { background:#20283a; border:1px solid #334; border-radius:20px; padding:1px 9px; font-size:11px; color:#9db8d2; font-family:ui-monospace,monospace; }
 .frame img { max-width:340px; max-height:340px; width:auto; height:auto; }
 .badge { display:inline-block; background:#2b3a4a; border-radius:4px; padding:1px 7px; font-size:11px; color:#9db8d2; margin-right:6px; }
 .badge.finish { background:#4a2b2b; color:#f9a; } .badge.err { background:#4a2b2b; color:#f77; }
 .kv { display:grid; grid-template-columns:max-content 1fr; gap:2px 14px; font-size:12px; }
 .kv b { color:#9ab; font-weight:600; }
 .sdk { margin:6px 0; padding:8px 10px; background:#1e1e26; border-left:3px solid #5a5; border-radius:6px; font-size:12px; }
 .sdk .kind { color:#9d8; }
 .sdk .tok { color:#a9d; }
 .frame { margin-top:8px; }
 a.img { display:inline-block; }
 a { color:#7bd; }
"""

_SDK_TREE_JS = """
function renderSdkTraceTrees(sdk, H) {
  if (!sdk.length) return;
  H.push(`<h2>OpenAI Agents SDK trace <span class="muted">(native trace · local copy · ${sdk.length} events)</span></h2>`);
  const ends = {};
  sdk.forEach(l => { if (l.kind === 'span_end') ends[l.span_id] = l; });
  const traces = sdk.filter(l => l.kind === 'trace_start');
  const dur = (a, b) => {
    if (!a || !b) return '';
    const ms = Date.parse(b) - Date.parse(a);
    if (isNaN(ms)) return '';
    return ms >= 1000 ? (ms / 1000).toFixed(1) + 's' : ms + 'ms';
  };
  const sLabel = sp => {
    const sd = sp.span_data || {};
    if (sd.type === 'function') return sd.name || 'function';
    if (sd.type === 'generation') return sd.model || 'generation';
    if (sd.type === 'agent') return sd.name || 'agent';
    return sp.name || sd.type || 'span';
  };
  const sKind = sp => (sp.span_data && sp.span_data.type) || sp.name || 'span';
  const sTokens = sp => {
    const u = (sp.span_data || {}).usage;
    if (!u) return '';
    return ` <span class="tok">${u.input_tokens || 0}→${u.output_tokens || 0} tok</span>`;
  };
  const sIO = sp => {
    const sd = sp.span_data || {};
    const inp = sd.input != null ? short(fmt(sd.input), 600) : '';
    const out = sd.output != null ? short(fmt(sd.output), 600) : '';
    let h = '';
    if (inp) h += `<details><summary>input</summary><pre>${esc(inp)}</pre></details>`;
    if (out) h += `<details><summary>output</summary><pre>${esc(out)}</pre></details>`;
    return h;
  };
  traces.forEach(tr => {
    const meta = tr.metadata || {};
    H.push(`<div class="sdk trace"><b>trace</b> <span class="kind">${esc(tr.workflow_name || '')}</span>` +
      ` <span class="muted">${esc(tr.trace_id || '')}</span>` +
      (meta.task_id ? ` <span class="badge">${esc(meta.task_id)}</span>` : '') +
      (meta.task_type ? ` <span class="badge">${esc(meta.task_type)}</span>` : '') +
      (meta.agent ? ` <span class="badge">${esc(meta.agent)}</span>` : '') +
      `</div>`);
    const spans = Object.values(ends).filter(l => l.trace_id === tr.trace_id);
    const byParent = {};
    spans.forEach(s => { const k = s.parent_id || tr.trace_id; (byParent[k] = byParent[k] || []).push(s); });
    Object.keys(byParent).forEach(k =>
      byParent[k].sort((a, b) => String(a.started_at || '').localeCompare(String(b.started_at || ''))));
    const walk = (id, depth) => {
      (byParent[id] || []).forEach(sp => {
        H.push(`<div class="sdk" style="margin-left:${depth * 18}px">` +
          `<span class="kind">[${esc(sKind(sp))}]</span> <b>${esc(sLabel(sp))}</b>` +
          (sp.error ? ` <span class="badge err">error</span>` : '') +
          ` <span class="muted">${dur(sp.started_at, sp.ended_at)}</span>${sTokens(sp)}` +
          sIO(sp) + `</div>`);
        walk(sp.span_id, depth + 1);
      });
    };
    walk(tr.trace_id, 1);
  });
}
"""


# ----------------------------------------------------------------------
# per-episode process viewer
# ----------------------------------------------------------------------
_VIEWER_HEADER = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>PixelBench episode — __TITLE__</title>
<style>""" + _PAGE_CSS + """</style></head><body>
"""

_VIEWER_FOOTER = """<p class="muted" style="margin-top:32px">PixelBench process viewer — data from
 <code>observations/turns.jsonl</code> (the canvas frame after each executed code block),
 <code>observations/calls.jsonl</code> (the before|after diff of each drawing function call),
 <code>trace.jsonl</code> (agent transcript) and <code>observations/sdk_trace.jsonl</code> (native OpenAI Agents SDK trace).
 This observer never injects diffs or frames into the model context; it is purely for recording.</p>
<script>
const DATA = __DATA__;
const rec = DATA.record || {}, trace = DATA.trace || [], turns = DATA.turns || [],
      calls = DATA.calls || [], sdk = DATA.sdk || [];
const callStats = DATA.call_stats || {}, callCount = DATA.call_count ?? calls.length, diffCount = DATA.diff_count ?? calls.filter(c=>c.diff).length;
const OBS = DATA.obs_dir + '/';
const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt = v => { if (v == null) return ''; if (typeof v === 'object') { try { return JSON.stringify(v); } catch(e) { return String(v); } } return String(v); };
const short = (s, n) => { s = String(s == null ? '' : s); return s.length > n ? s.slice(0, n) + ' …' : s; };
const app = document.getElementById('app');
const H = [];
H.push(`<h1>${esc(rec.task_id || 'episode')} <span class="tag">${esc(rec.agent || '')}</span></h1>`);
H.push(`<p class="muted">${esc(rec.task_type || '')} · ${rec.ok ? 'ok' : 'FAIL'} · steps=${rec.steps ?? '?'} · ` +
  `turns=${turns.length} · tool calls=${callCount} · diff images=${diffCount}</p>`);
if (rec.error) H.push(`<pre class="err">${esc(rec.error)}</pre>`);
// images
const imgNames = ['reference','corrupted','final','final_1x'];
const imgs = imgNames.filter(n => (DATA.images || []).includes(n));
if (imgs.length) {
  H.push(`<h2>Images</h2><div class="imgs">` + imgs.map(n =>
    `<figure><img src="${n}.png"><figcaption>${n}.png</figcaption></figure>`).join('') + `</div>`);
}
// metrics
const flat = {};
(function walk(o, p){ if (o && typeof o === 'object') { for (const k in o) { const v = o[k];
  if (v && typeof v === 'object') walk(v, p + k + '.'); else flat[p + k] = v; } } })(rec.metrics || {}, '');
const jd = (rec.judge && rec.judge.dims) || {};
const jkeys = Object.keys(jd);
if (Object.keys(flat).length || jkeys.length) {
  H.push(`<h2>Evaluation</h2><div class="cards">`);
  if (Object.keys(flat).length) H.push(`<div class="card"><div class="kv">` +
    Object.entries(flat).map(([k,v]) => `<b>${esc(k)}</b><span>${esc(v)}</span>`).join('') + `</div></div>`);
  if (jkeys.length) H.push(`<div class="card"><h3>LLM judge ${rec.judge && rec.judge.overall != null ? '(' + rec.judge.overall + ')' : ''}</h3><div class="kv">` +
    jkeys.map(k => `<b>${esc(k)}</b><span>${esc(jd[k].score)}</span>`).join('') + `</div></div>`);
  H.push(`</div>`);
}
// ---- timeline ----
const sortedTurns = turns.slice().sort((a,b)=>a.turn-b.turn);
const codeEntries = trace.filter(e => e.kind === 'code');
const finishByStep = {};
trace.forEach(e => { if (e.kind === 'finish') finishByStep[e.step] = true; });
// pair turn index t (>=1) with code entry t-1 (execute order)
const items = [];
sortedTurns.forEach((t, idx) => {
  items.push({ turn: t, initial: idx === 0, ce: idx === 0 ? null : codeEntries[idx-1] });
});
codeEntries.forEach((e, i) => { if (!sortedTurns[i+1]) items.push({ turn: null, ce: e }); });
const callsByTurn = {};
calls.forEach(c => { (callsByTurn[c.turn] = callsByTurn[c.turn] || []).push(c); });
if (items.length) {
  H.push(`<h2>Painting process</h2><div class="tl">`);
  items.forEach(it => {
    const t = it.turn, ce = it.ce;
    const header = it.initial ? 'Initial canvas' : (t ? `Turn ${t.turn}` : 'Code (no canvas record)');
    H.push(`<div class="item"><h3>${header} ${ce && ce.step != null ? `<span class="badge">step ${ce.step}</span>` : ''}` +
      (it.initial ? '' : (t ? `<span class="badge">v${t.version}</span>` : '')) +
      (ce && finishByStep[ce.step] ? `<span class="badge finish">finish()</span>` : '') +
      (t ? `<span class="muted">calls ${t.calls_start}-${t.calls_end}</span>` : '') + `</h3>`);
    if (ce) {
      if (ce.code) H.push(`<details open><summary>code</summary><pre>${esc(ce.code)}</pre></details>`);
      const o = ce.output || {};
      const outText = [o.stdout, o.stderr ? 'STDERR:\\n' + o.stderr : '', (o.errors||[]).map(e=>`${e.ename}: ${e.evalue}`).join('\\n')].filter(Boolean).join('\\n');
      if (outText) H.push(`<details><summary>output</summary><pre>${esc(short(outText, 4000))}</pre></details>`);
      if (o && o.n_images) H.push(`<span class="badge">rendered ${o.n_images} image(s)</span>`);
      if (ce.kind === 'max_steps') H.push(`<span class="badge err">max steps</span>`);
    }
    if (t && t.frame) H.push(`<div class="frame"><a class="img" href="${OBS}${t.frame}" target="_blank"><img src="${OBS}${t.frame}"></a></div>`);
    const tCalls = t ? (callsByTurn[t.turn] || []) : [];
    const tStat = t ? (callStats[t.turn] || null) : null;
    if (tStat && Object.keys(tStat.ops || {}).length) {
      const ops = Object.entries(tStat.ops).map(([op, cnt]) =>
        `<span class="opchip">${esc(op)} × ${cnt}</span>`).join('');
      H.push(`<div class="opstats">${ops}` +
        (tStat.changed ? `<span class="chg">+${tStat.changed}px changed</span>` : '') + `</div>`);
    }
    if (tCalls.length) {
      // cap DOM nodes even for the embedded sample
      const shown = tCalls.slice(0, 60);
      const hidden = tCalls.length - shown.length;
      H.push(`<div class="calls">` + shown.map(c => {
        const args = c.args ? short(fmt(c.args), 400) : '';
        return `<div class="call"><span class="op">${esc(c.op)}</span>` +
          (c.changed > 0 ? ` <span class="chg">+${c.changed}px</span>` : ` <span class="muted">0px</span>`) +
          (c.diff ? ` <a href="${OBS}${c.diff}" target="_blank">diff</a>` : '') +
          (args ? `<details><summary>args</summary><pre>${esc(args)}</pre></details>` : '') +
          (c.diff ? `<div class="frame"><a class="img" href="${OBS}${c.diff}" target="_blank"><img src="${OBS}${c.diff}"></a></div>` : '') +
          `</div>`;
      }).join('') +
      (hidden > 0 ? `<div class="call muted">… and ${hidden} more calls this turn (see op histogram above)</div>` : '') +
      `</div>`);
    }
    H.push(`</div>`);
  });
  H.push(`</div>`);
}
renderSdkTraceTrees(sdk, H);
app.innerHTML = H.join('');
</script>
</body></html>
"""


def write_process_viewer(episode_dir: Path) -> Optional[Path]:
    """Generate ``process.html`` for one episode directory.

    Returns the written path, or ``None`` when the episode has no
    observation data (e.g. direct-generation agents without a kernel).
    """
    episode_dir = Path(episode_dir)
    odir = observation_dir(episode_dir)
    record_path = episode_dir / "record.json"
    if not record_path.exists():
        return None
    try:
        record = json.loads(record_path.read_text(encoding="utf-8"))
    except Exception:  # pragma: no cover
        record = {}

    data: Dict[str, Any] = {
        "record": record,
        "trace": read_jsonl(episode_dir / "trace.jsonl"),
        "turns": read_jsonl(odir / "turns.jsonl"),
        "sdk": read_jsonl(odir / "sdk_trace.jsonl"),
        "obs_dir": OBS_DIRNAME,
        "images": [p.name for p in episode_dir.glob("*.png")],
    }
    calls = read_jsonl(odir / "calls.jsonl")
    # compact per-turn call statistics (op histogram + changed pixels),
    # so the viewer never needs to render one DOM node per set_pixel.
    call_stats: Dict[int, Dict[str, Any]] = {}
    for c in calls:
        t = int(c.get("turn", 0))
        st = call_stats.setdefault(t, {"ops": {}, "changed": 0})
        op = str(c.get("op", "?"))
        st["ops"][op] = st["ops"].get(op, 0) + 1
        st["changed"] += int(c.get("changed", 0))
    # cap embedded per-call detail: keep every diff-carrying call (they
    # have before|after images) plus an evenly sampled subset of the rest.
    with_diff = [c for c in calls if c.get("diff")]
    no_diff = [c for c in calls if not c.get("diff")]
    max_plain = 1200
    if len(no_diff) > max_plain:
        step = len(no_diff) / max_plain
        no_diff = [no_diff[int(i * step)] for i in range(max_plain)]
    call_sample = sorted(with_diff + no_diff, key=lambda c: c.get("call", 0))
    data["calls"] = call_sample
    data["call_stats"] = {str(k): v for k, v in call_stats.items()}
    data["call_count"] = len(calls)
    data["diff_count"] = len(with_diff)
    if not data["turns"] and not calls and not data["sdk"]:
        return None  # nothing was observed (e.g. direct agent, no kernel)
    title = f"{record.get('task_id', 'episode')} · {record.get('agent', '')}".strip(" ·")
    json_data = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = _VIEWER_HEADER.replace("__TITLE__", esc_attr(title))
    html += '<div id="app"></div>'
    html += _VIEWER_FOOTER.replace("__DATA__", json_data)
    target = episode_dir / "process.html"
    target.write_text(html, encoding="utf-8")
    return target


def esc_attr(s: str) -> str:
    return str(s).replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


# ----------------------------------------------------------------------
# live trace dashboard (python -m pixelbench serve-traces)
# ----------------------------------------------------------------------
_TRACES_HEADER = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>PixelBench Agent Trace</title>
<style>""" + _PAGE_CSS + """
 .status { color:#9d8; font-size:12px; }
</style></head><body>
<div id="app"></div>
<script>
"""

_TRACES_SCRIPT = """
const app = document.getElementById('app');
const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt = v => { if (v == null) return ''; if (typeof v === 'object') { try { return JSON.stringify(v); } catch(e) { return String(v); } } return String(v); };
const short = (s, n) => { s = String(s == null ? '' : s); return s.length > n ? s.slice(0, n) + ' …' : s; };
let cache = {};
let lastRefresh = 0;
async function refresh() {
  let m;
  try { m = await (await fetch('/manifest.json', {cache: 'no-store'})).json(); } catch (e) { return; }
  const entries = m.traces || [];
  const H = [];
  H.push(`<h1>PixelBench Agent Trace <span class="muted">(${entries.length} trace files · auto-refresh every 3s)</span></h1>`);
  H.push(`<p class="muted">Native openai-agents traces are written to <code>episodes/&lt;ep&gt;/observations/sdk_trace.jsonl</code> and rendered here live. ` +
    `If there are no trace files yet, run an evaluation with the <code>sdk-repl</code> agent, or first generate a sample with <code>python -m pixelbench sample-sdk-trace</code>.</p>`);
  if (!entries.length) {
    H.push(`<p class="status">⌛ Waiting for trace files… (they appear automatically once a running evaluation writes them)</p>`);
  }
  for (const e of entries) {
    const key = `${e.episode}|${e.mtime}|${e.size}`;
    if (cache[key]) { H.push(cache[key]); continue; }
    let text = null;
    try { text = await (await fetch(e.url, {cache: 'no-store'})).text(); } catch (err) {}
    if (text == null) continue;
    const lines = text.split('\\n').filter(Boolean).map(l => { try { return JSON.parse(l); } catch (err) { return null; } }).filter(Boolean);
    const eh = [];
    eh.push(`<h2>${esc(e.episode)} <span class="muted">${lines.length} events</span>` +
      (e.viewer ? ` <a href="${e.viewer}" target="_blank">painting process</a>` : '') + `</h2>`);
    renderSdkTraceTrees(lines, eh);
    const html = eh.join('');
    cache[key] = html;
    H.push(html);
  }
  app.innerHTML = H.join('');
  lastRefresh = Date.now();
}
setInterval(refresh, 3000);
refresh();
</script>
</body></html>
"""

TRACES_PAGE: str = _TRACES_HEADER + _SDK_TREE_JS + _TRACES_SCRIPT


def build_trace_manifest(out_dir: Path) -> Dict[str, Any]:
    """List every ``sdk_trace.jsonl`` under a run directory.

    Supports both the standard layout (``episodes/<ep>/observations/``)
    and a single-episode directory at the root (``observations/``).
    """
    out = Path(out_dir)
    entries: List[Dict[str, Any]] = []

    def add(episode: str, url: str, f: Path, viewer: bool) -> None:
        st = f.stat()
        entries.append(
            {"episode": episode, "url": url, "mtime": st.st_mtime, "size": st.st_size, "viewer": viewer}
        )

    for d in sorted(out.glob("episodes/*")):
        f = d / OBS_DIRNAME / "sdk_trace.jsonl"
        if f.is_file():
            viewer = f"episodes/{d.name}/process.html" if (d / "process.html").is_file() else None
            add(d.name, f"episodes/{d.name}/{OBS_DIRNAME}/sdk_trace.jsonl", f, viewer)
    f = out / OBS_DIRNAME / "sdk_trace.jsonl"
    if f.is_file():
        viewer = "process.html" if (out / "process.html").is_file() else None
        add(out.name, f"{OBS_DIRNAME}/sdk_trace.jsonl", f, viewer)
    return {"traces": entries}


def make_traces_handler(out_dir: Path):
    """HTTP handler for the live trace dashboard.

    - ``/`` and ``/traces.html`` → the dashboard page (embedded JS polls
      ``/manifest.json`` and re-renders trace trees as files grow).
    - ``/manifest.json`` → current list of trace files (no-store).
    - everything else → static files from ``out_dir`` (so the page can
      fetch the JSONL files themselves).
    """
    from http.server import SimpleHTTPRequestHandler

    out = str(Path(out_dir))
    page = TRACES_PAGE

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=out, **kw)

        def do_GET(self):
            if self.path in ("/", "/traces.html"):
                body = page.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if self.path == "/manifest.json":
                payload = json.dumps(build_trace_manifest(out_dir), ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
                return
            return super().do_GET()

        def log_message(self, *a):  # quieter logs
            pass

    return Handler
