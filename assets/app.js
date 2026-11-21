/* PixelBench project page — PixelSkill case-study player, results, editing examples, gallery.
   Data globals: window.PIXELBENCH_SCORES, window.PIXELBENCH_SESSION (see data/*.js). */
(() => {
'use strict';

const SCORES = window.PIXELBENCH_SCORES;
const SESSION = window.PIXELBENCH_SESSION;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

let LANG = document.documentElement.dataset.lang || 'en';
const pick = (en, zh) => (LANG === 'zh' ? zh : en);
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/* ───────────────────────────── language ───────────────────────────── */
function setLang(lang) {
  LANG = lang;
  document.documentElement.dataset.lang = lang;
  document.documentElement.lang = lang === 'zh' ? 'zh-Hans' : 'en';
  $('#langToggle').textContent = lang === 'zh' ? 'EN' : '中文';
  try { localStorage.setItem('pb-lang', lang); } catch (e) { /* ignore */ }
  renderCaseStatic();
  renderAll();
}

/* ───────────────────────── case study player ───────────────────────── */
/* the case task's number in the benchmark's task order */
function caseTaskIdx(m) {
  const t = (SCORES ? SCORES.tasks : []).find((x) => x.id === m.task_id);
  return t ? `#${t.idx}` : m.task_id;
}

const S = SESSION;
const frameCount = S ? S.frames.length : 0;
const layerByName = new Map((S?.layers || []).map((l) => [l.name, l]));

const player = {
  i: 0, playing: false, speed: 1, timer: null, mergeBusy: false, lastOutput: '',
  stmtKey: null, compressedFrames: 0, acc: 0, lastTs: null,
};

/* ── frame images ─────────────────────────────────────────────────
   The stage is a <canvas>, not an <img>: at the compressed loop pace frames
   are 5–20 ms apart, and re-assigning <img src> that fast aborts each decode
   before it paints, so the picture freezes.  Drawing pre-decoded images onto a
   canvas is synchronous, so the stage always shows the newest frame we set.
   All frames come from one sprite sheet and the layer snapshots from another
   (tools/build_case_sheets.py): cell k sits at column k % cols, row k / cols,
   one canvas-sized cell each, so one request replaces hundreds. */
const CELL_W = S ? S.meta.width : 0;
const CELL_H = S ? S.meta.height : 0;
const frameSheet = new Image();
let framesReady = 0;
let lastDrawn = -1;
let preloadStarted = false;

const sheetReady = (im) => im.complete && im.naturalWidth > 0;

/* copy cell k of a sheet onto a canvas, scaled to the canvas size */
function drawCell(cv, sheet, k) {
  const cols = Math.floor(sheet.naturalWidth / CELL_W);
  const ctx = cv.getContext('2d');
  ctx.imageSmoothingEnabled = false;
  ctx.clearRect(0, 0, cv.width, cv.height);
  ctx.drawImage(sheet, (k % cols) * CELL_W, Math.floor(k / cols) * CELL_H, CELL_W, CELL_H,
    0, 0, cv.width, cv.height);
}

/* one file carries every image, so a failed request is retried twice before giving up */
function loadSheet(im, src, onload, onfail) {
  let tries = 0;
  im.onload = onload;
  im.onerror = () => {
    tries++;
    if (tries < 3) setTimeout(() => { im.src = `${src}?retry=${tries}`; }, 1500 * tries);
    else if (onfail) onfail();
  };
  im.src = src;
}

function preloadFrames() {
  if (!S || preloadStarted) return;   /* language switches re-render, not re-download */
  preloadStarted = true;
  frameSheet.decoding = 'sync';
  loadSheet(frameSheet, 'case/frames.png', () => {
    framesReady = frameCount;
    updateLoadBadge();
    drawStage(player.i, true);
  }, () => { framesReady = frameCount; updateLoadBadge(); });
  updateLoadBadge();
}

function updateLoadBadge() {
  const el = $('#stageLoad');
  if (!el) return;
  el.textContent = framesReady >= frameCount ? '' : `${framesReady}/${frameCount}`;
}

function drawStage(i, force) {
  const cv = $('#stageCanvas');
  if (!cv || !sheetReady(frameSheet)) return;   /* not decoded yet: its onload draws */
  if (!force && i === lastDrawn) return;
  drawCell(cv, frameSheet, i);
  lastDrawn = i;
}

/* per-layer frame lists: [{frame, img}] in order */
const layerFrames = new Map();
if (S) {
  for (const l of S.layers) layerFrames.set(l.name, []);
  for (const f of S.frames) {
    for (const [name, img] of Object.entries(f.layers || {})) {
      if (!layerFrames.has(name)) layerFrames.set(name, []);
      layerFrames.get(name).push({ frame: f.i, img });
    }
  }
}
function layerAt(name, frame) {
  const list = layerFrames.get(name) || [];
  let cur = null;
  for (const e of list) { if (e.frame <= frame) cur = e.img; else break; }
  return cur;
}

/* layer snapshot -> its cell in the layer sheet: order of first appearance, the
   order tools/build_case_sheets.py packs them in */
const layerCell = new Map();
if (S) {
  for (const f of S.frames) {
    for (const img of Object.values(f.layers || {})) if (!layerCell.has(img)) layerCell.set(img, layerCell.size);
  }
}
const layerSheet = new Image();
function drawLayerThumb(box) {
  const cv = $('canvas', box);
  const k = layerCell.get(box.dataset.src);
  if (cv && k != null && sheetReady(layerSheet)) drawCell(cv, layerSheet, k);
}
function loadLayerSheet() {   /* first needed when a layer appears */
  if (layerSheet.src) return;
  loadSheet(layerSheet, 'case/layers.png', () => $$('.lyr-thumb[data-src]', $('#layerStrip')).forEach(drawLayerThumb));
}

/* flat-code index helpers */
const lineIndex = new Map();     // "step:line" -> index in code list
const stmtRanges = [];           // {first,last,frame_start,frame_end,step,layer,output,text}
function buildStmtRanges() {
  if (!S) return;
  stmtRanges.length = 0;
  S.statements.forEach((st, k) => {
    stmtRanges.push({ ...st, key: k });
  });
}
function stmtForFrame(i) {
  let best = null;
  for (const st of stmtRanges) {
    if (i >= st.frame_start && i <= st.frame_end) best = st;
    if (st.frame_start > i) break;
  }
  return best || stmtRanges[stmtRanges.length - 1] || null;
}

function renderCaseStatic() {
  if (!S) return;
  const m = S.meta;
  /* meta strip */
  const meta = $('#caseMeta');
  const rows = [
    [pick('Task', '题目'), caseTaskIdx(m), pick(m.title_en, m.title_zh)],
    [pick('Model', '模型'), m.model_label, 'PixelSkill'],
    [pick('Canvas', '画布'), `${m.width}×${m.height}`, `${m.colors} ${pick('colors', '种颜色')}`],
    [pick('Layers', '图层'), String(m.layers), `${m.merges} ${pick('merges', '次合并')}`],
    [pick('Code lines', '代码行'), String(m.total_statements), pick('statements', '个语句')],
    [pick('Draw calls', '绘图调用'), String(m.total_draw_calls), `${m.total_frames} ${pick('frames', '帧')}`],
  ];
  meta.innerHTML = rows.map(([dt, dd, sub]) =>
    `<div><dt>${esc(dt)}</dt><dd>${esc(dd)}${sub ? ` <small>${esc(sub)}</small>` : ''}</dd></div>`).join('');
  $('#casePrompt').textContent = pick(m.prompt_en, m.prompt_zh);
  const nCode = S.lines.filter((l) => l.kind !== 'sep').length;
  ['#fig1Lines', '#fig1LinesZh'].forEach((sel) => { const e = $(sel); if (e) e.textContent = String(nCode); });
  ['#fig1Frames', '#fig1FramesZh'].forEach((sel) => { const e = $(sel); if (e) e.textContent = String(m.total_frames); });

  /* code listing */
  const code = $('#codeList');
  code.innerHTML = '';
  lineIndex.clear();
  S.lines.forEach((ln, k) => {
    if (ln.kind === 'sep') {
      const li = document.createElement('li');
      li.className = 'sep';
      code.appendChild(li);
      return;
    }
    const li = document.createElement('li');
    li.className = 'k-' + ln.kind;
    li.dataset.step = ln.step;
    li.dataset.line = ln.line;
    li.innerHTML = `<span class="ln">${ln.line}</span><span class="src">${esc(ln.text)}</span>`;
    code.appendChild(li);
    lineIndex.set(`${ln.step}:${ln.line}`, k);
  });

  /* timeline marks */
  const tl = $('#timeline');
  $$('.tl-mark', tl).forEach((n) => n.remove());
  const track = $('.tl-track', tl);
  if (!$('.tl-fill', tl)) {
    const fill = document.createElement('div');
    fill.className = 'tl-fill';
    tl.insertBefore(fill, track.nextSibling);
  }
  const total = Math.max(1, frameCount - 1);
  const marks = [];
  S.layers.forEach((l) => marks.push({ f: l.created_frame, label: `${pick('new layer', '新建图层')} · ${l.name}`, merge: false }));
  S.merges.forEach((mg) => marks.push({ f: mg.frame, label: `${pick('flatten', '合并')} → ${mg.name}`, merge: true }));
  marks.forEach((mk) => {
    if (mk.f == null) return;
    const d = document.createElement('div');
    d.className = 'tl-mark' + (mk.merge ? ' merge' : '');
    d.style.left = (mk.f / total * 100) + '%';
    d.innerHTML = `<span>${esc(mk.label)}</span>`;
    d.addEventListener('click', () => setFrame(mk.f, true));
    tl.appendChild(d);
  });

  /* layer strip */
  const strip = $('#layerStrip');
  strip.innerHTML = '';
  S.layers.forEach((l) => {
    const d = document.createElement('div');
    d.className = 'lyr pending';
    d.dataset.layer = l.name;
    d.innerHTML = `
      <div class="lyr-thumb"><span class="ph">—</span></div>
      <div class="lyr-name" title="${esc(l.name)}">${esc(l.name)}</div>
      <div class="lyr-stat"><span class="lyr-calls">0</span> calls · <span class="lyr-colors">0</span>c</div>
      <span class="lyr-badge" hidden>${esc(pick('merged', '已合并'))}</span>`;
    d.addEventListener('click', () => l.created_frame != null && setFrame(l.created_frame, true));
    strip.appendChild(d);
  });
  $('#layerCount').textContent = '0';


  preloadFrames();
  buildStmtRanges();
  const compressed = buildDurations();
  player.compressedFrames = compressed;
  $('#scrub').max = String(Math.max(0, frameCount - 1));
  $('#roTotal').textContent = String(frameCount);
  setFrame(Math.min(player.i, frameCount - 1), false);
}

/* ── frame rendering ── */
function setFrame(i, userAction) {
  if (!S) return;
  player.i = Math.max(0, Math.min(frameCount - 1, i));
  const f = S.frames[player.i];

  drawStage(player.i);
  $('#roFrame').textContent = String(player.i);
  $('#roLine').textContent = String(f.line ?? '—');
  $('#roOps').textContent = String(f.ops);
  $('#scrub').value = String(player.i);
  $('.tl-fill').style.width = (frameCount > 1 ? player.i / (frameCount - 1) * 100 : 0) + '%';

  const st = stmtForFrame(player.i);
  const stChanged = player.stmtKey !== (st ? `${st.step}:${st.first}` : null);
  player.stmtKey = st ? `${st.step}:${st.first}` : null;
  const stepLabel = (S.steps.find((s) => s.n === f.step) || {}).label || `Step ${f.step}`;
  $('#codeStepLabel').textContent = LANG === 'zh'
    ? stepLabel.replace(/^Step (\d) — (.*)$/, '第 $1 步 · $2') : stepLabel;
  $('#stageLayerLabel').textContent = i === frameCount - 1 ? pick('complete', '完成')
    : f.active ? pick('drawing to ', '正在绘制：') + f.active : pick('idle', '空闲');

  /* code highlight */
  const code = $('#codeList');
  $$('.active, .stmt', code).forEach((n) => n.classList.remove('active', 'stmt'));
  if (st) {
    for (let line = st.first; line <= st.last; line++) {
      const k = lineIndex.get(`${st.step}:${line}`);
      if (k == null) continue;
      const li = code.children[k];
      if (!li) continue;
      li.classList.add('stmt');
      if (line === f.line) li.classList.add('active');
    }
  }
  const curKey = lineIndex.get(`${f.step}:${f.line}`);
  if (curKey != null && code.children[curKey]) code.children[curKey].classList.add('active');

  /* the bar above the listing always names the line being executed, even when the
     listing itself is scrolled or the line is a wide loop header */
  const curLine = (S.lines.filter((l) => l.step === f.step && l.line === f.line)[0] || {}).text
    || (st ? st.text.split('\n')[0] : '—');
  $('#nowLine').textContent = 'L' + (f.line ?? '—');
  $('#nowCode').textContent = curLine.trim();
  $('#nowCode').title = curLine;
  const layerName = f.active || (st && st.layer) || '';
  $('#nowLayer').textContent = layerName && layerName !== '—' ? '→ ' + layerName : '';

  scrollCodeIntoView(stChanged);

  /* layer strip */
  let created = 0;
  const mergedNames = new Set();
  S.merges.forEach((mg) => { if (mg.frame != null && player.i >= mg.frame) mg.inputs.forEach((n) => mergedNames.add(n)); });
  S.layers.forEach((l) => {
    const el = $(`.lyr[data-layer="${CSS.escape(l.name)}"]`, $('#layerStrip'));
    if (!el) return;
    const born = l.created_frame != null && player.i >= l.created_frame;
    if (born) created++;
    el.classList.toggle('pending', !born);
    el.classList.toggle('active', born && f.active === l.name);
    el.classList.toggle('merged', born && mergedNames.has(l.name));
    $('.lyr-badge', el).hidden = !(born && mergedNames.has(l.name));
    if (born) {
      const src = layerAt(l.name, player.i);
      const box = $('.lyr-thumb', el);
      if (src && box.dataset.src !== src) {
        box.dataset.src = src;
        if (!$('canvas', box)) {
          box.innerHTML = `<canvas width="${CELL_W}" height="${CELL_H}" role="img" aria-label="${esc(l.name)}"></canvas>`;
        }
        loadLayerSheet();
        drawLayerThumb(box);
      }
      /* approximate live progress: scale total calls by how far this layer's own
         frames have progressed */
      const list = layerFrames.get(l.name) || [];
      const done = list.filter((e) => e.frame <= player.i).length;
      const frac = list.length ? done / list.length : 0;
      $('.lyr-calls', el).textContent = String(Math.round(l.draw_calls * frac));
      $('.lyr-colors', el).textContent = String(Math.max(0, Math.round(l.colors * frac)));
    } else {
      $('.lyr-calls', el).textContent = '0';
      $('.lyr-colors', el).textContent = '0';
    }
  });
  $('#layerCount').textContent = String(created);

  /* REPL output (latest non-empty output at or before the playhead) */
  let out = null;
  for (const s2 of stmtRanges) {
    if (s2.frame_start <= player.i && s2.output) out = s2;
    if (s2.frame_start > player.i) break;
  }
  if (out && player.lastOutput !== out.output) {
    player.lastOutput = out.output;
    const box = $('#outBox');
    box.innerHTML = `<span class="out-tag">step ${out.step} · line ${out.first}  ▸ </span>` + esc(out.output);
  } else if (!out && player.i < (stmtRanges[0]?.frame_start ?? 0)) {
    $('#outBox').innerHTML = '<span class="out-idle">—</span>';
  }
}

function scrollCodeIntoView(force) {
  const code = $('#codeList');
  const el = $('.active', code);
  if (!el) return;
  /* offsets measured against the scroll box itself: offsetTop would be relative to
     the page, which pinned the panel to the bottom and hid the active line. */
  const cr = code.getBoundingClientRect();
  const er = el.getBoundingClientRect();
  const relTop = er.top - cr.top;
  const pad = 56;
  if (relTop < pad || relTop + er.height > code.clientHeight - pad) {
    code.scrollTop += relTop - Math.round(code.clientHeight * 0.42);
  }
  /* long lines scroll horizontally; keep the start of the statement in view */
  if (force && code.scrollLeft !== 0) code.scrollLeft = 0;
}

/* ── merge animation beat ── */
function playMerge(mg, done) {
  const ov = $('#mergeOverlay');
  const inner = $('.mo-inner', ov);
  const ins = mg.inputs.filter((n) => layerByName.has(n));
  inner.innerHTML = ins.map((n, k) => {
    const angle = (k / ins.length) * Math.PI * 2 - Math.PI / 2;
    const tx = Math.round(Math.cos(angle) * 96), ty = Math.round(Math.sin(angle) * 74);
    return `<img src="${layerByName.get(n).final}" alt="${esc(n)}"
      style="--tx:${tx}px;--ty:${ty}px;transform:translate(${tx}px, ${ty}px)">`;
  }).join('');
  $('#moCode').textContent = `flatten([${mg.inputs.join(', ')}])`;
  ov.classList.remove('collapse');
  ov.classList.add('on');
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      $$('.mo-inner img', ov).forEach((img) => { img.style.transform = 'translate(0,0)'; });
      setTimeout(() => {
        ov.classList.add('collapse');
        setTimeout(() => { ov.classList.remove('on', 'collapse'); done && done(); }, 620);
      }, 620);
    });
  });
}

/* ── playback timing ──────────────────────────────────────────────
   Three statements — the sparkle loop, the 128-step shore sweep and the sand
   speckle loop — account for 211 of the 293 frames, so a uniform delay spends
   most of the animation watching texture being dotted in.  Frames inside a long
   statement are therefore played on a compressed schedule: the first few stay
   readable, then the rest fast-forward until that statement's budget is used up.
   Scrub granularity and ← / → stepping stay one frame at a time either way. */
const BASE_MS = 130;
const LOOP_MIN_FRAMES = 12;    // a statement shorter than this plays at BASE_MS
const LOOP_BUDGET_MS = 2200;   // wall-clock budget for one long statement
const LOOP_FLOOR_MS = 22;      // never faster than this per frame
const LOOP_RAMP = 4;           // frames at BASE_MS before the fast-forward starts
let durations = [];
let fastLoops = true;

function buildDurations() {
  durations = new Array(frameCount).fill(BASE_MS);
  let compressed = 0;
  stmtRanges.forEach((st) => {
    const n = st.frame_end - st.frame_start;
    if (n < LOOP_MIN_FRAMES) return;
    const d = Math.max(LOOP_FLOOR_MS, Math.round(LOOP_BUDGET_MS / n));
    for (let i = st.frame_start + 1; i <= st.frame_end; i++) {
      durations[i] = (i - st.frame_start <= LOOP_RAMP) ? BASE_MS : d;
      compressed++;
    }
  });
  /* let a new layer card and a merge register before the playhead moves on */
  S.layers.forEach((l) => {
    if (l.created_frame != null) durations[l.created_frame] = Math.max(durations[l.created_frame], 300);
  });
  S.merges.forEach((mg) => {
    if (mg.frame != null) durations[mg.frame] = Math.max(durations[mg.frame], 220);
  });
  return compressed;
}

function frameMs(i) { return fastLoops ? (durations[i] ?? BASE_MS) : BASE_MS; }

function totalMs() {
  let t = 0;
  for (let i = 1; i < frameCount; i++) t += frameMs(i);
  return t;
}

/* Playback is driven by elapsed wall-clock time inside requestAnimationFrame, and
   the stage is painted once per animation frame.  A frame-by-frame setTimeout chain
   falls behind as soon as rendering costs more than the frame interval (which is
   exactly what the compressed loop pace does), and on top of that it renders every
   intermediate step; advancing the playhead by time and drawing only the resulting
   frame keeps the motion continuous at any speed. */
function playLoop(ts) {
  if (!player.playing) return;
  if (player.lastTs == null) player.lastTs = ts;
  /* a background tab or a long task must not fast-forward the whole animation */
  const dt = Math.min(Math.max(0, ts - player.lastTs), 250);
  player.lastTs = ts;
  player.acc += dt * player.speed;

  let target = player.i;
  let guard = 0;
  while (target < frameCount - 1 && player.acc >= frameMs(target + 1) && guard++ < 4000) {
    player.acc -= frameMs(target + 1);
    target++;
    const mg = S.merges.find((x) => x.frame === target);
    if (mg) {
      /* merges are set pieces: stop on them, animate, then carry on */
      setFrame(target, false);
      player.acc = 0;
      player.mergeBusy = true;
      playMerge(mg, () => {
        player.mergeBusy = false;
        if (player.playing) { player.lastTs = null; player.timer = requestAnimationFrame(playLoop); }
      });
      return;
    }
  }
  if (target !== player.i) setFrame(target, false);
  if (target >= frameCount - 1) { pause(); return; }
  player.timer = requestAnimationFrame(playLoop);
}

function play() {
  if (player.i >= frameCount - 1) setFrame(0, true);
  player.playing = true;
  player.acc = 0;
  player.lastTs = null;
  $('#playGlyph').textContent = '❚❚';
  $('#playLabel').textContent = pick('Pause', '暂停');
  $('#playLabelZh').textContent = '暂停';
  player.timer = requestAnimationFrame(playLoop);
}
function pause() {
  player.playing = false;
  if (player.timer != null) cancelAnimationFrame(player.timer);
  player.timer = null;
  $('#playGlyph').textContent = '▶';
  $('#playLabel').textContent = pick('Play', '播放');
  $('#playLabelZh').textContent = '播放';
}

function initPlayer() {
  if (!S) return;
  $('#btnPlay').addEventListener('click', () => (player.playing ? pause() : play()));
  $('#btnRestart').addEventListener('click', () => {
    pause();
    const mg = $('#mergeOverlay'); mg.classList.remove('on', 'collapse');
    setFrame(0, true);
  });
  $$('.chip[data-speed]').forEach((c) => c.addEventListener('click', () => {
    $$('.chip[data-speed]').forEach((x) => x.classList.remove('is-on'));
    c.classList.add('is-on');
    player.speed = Number(c.dataset.speed);
  }));
  const loopBtn = $('#loopFast');
  loopBtn.addEventListener('click', () => {
    fastLoops = !fastLoops;
    loopBtn.classList.toggle('is-on', fastLoops);
  });
  /* clicking a line jumps to the first frame of the statement it belongs to */
  $('#codeList').addEventListener('click', (e) => {
    const li = e.target.closest('li');
    if (!li || li.classList.contains('sep')) return;
    const step = Number(li.dataset.step), line = Number(li.dataset.line);
    const st = stmtRanges.find((x) => x.step === step && line >= x.first && line <= x.last);
    if (!st) return;
    pause();
    $('#mergeOverlay').classList.remove('on', 'collapse');
    setFrame(st.frame_start, true);
  });
  $('#scrub').addEventListener('input', (e) => {
    pause();
    $('#mergeOverlay').classList.remove('on', 'collapse');
    setFrame(Number(e.target.value), true);
  });
  document.addEventListener('keydown', (e) => {
    if (e.target.matches('input, select, textarea')) return;
    if (!document.getElementById('lightbox').hidden) return;
    if (e.key === 'ArrowRight') { pause(); setFrame(player.i + 1, true); }
    if (e.key === 'ArrowLeft') { pause(); setFrame(player.i - 1, true); }
    if (e.key === ' ') { e.preventDefault(); player.playing ? pause() : play(); }
  });
}

/* ───────────────────────────── data ───────────────────────────── */
const D = SCORES;
const META = D ? D.meta : {};
const CONFIGS = D ? D.configs : [];          /* sorted by the all-task score, best first */
const CFG = new Map(CONFIGS.map((c) => [c.id, c]));
const TASKS = D ? D.tasks : [];
const TASK = new Map(TASKS.map((t) => [t.id, t]));
const GROUPS = META.groups || [];
const GROUP = new Map(GROUPS.map((g) => [g.key, g]));
/* categorical slots 1-3 (validated all-pairs on the white card surface) and the
   sequential blue ramp, steps 100-700 */
const SERIES = ['#2a78d6', '#eb6834', '#1baf7a'];
const RAMP = ['#cde2fb', '#b7d3f6', '#9ec5f4', '#86b6ef', '#6da7ec', '#5598e7', '#3987e5',
  '#2a78d6', '#256abf', '#1c5cab', '#184f95', '#104281', '#0d366b'];
const EDIT_EXAMPLES = ['melting-icecream', 'fist-swing', 'char-turn-3view', 'big-170-170'];

const fmt = (v, d = 2) => (v == null || Number.isNaN(v) ? '—' : Number(v).toFixed(d));
const effortText = (e) => (e === 'thinking budget' ? pick('thinking budget', '思考预算') : e);
const cfgLabel = (c) => (c.effort === 'thinking budget' ? c.model : `${c.model} (${c.effort})`);
const effortTag = (c) => `<span class="eff${c.main ? ' is-main' : ''}">${esc(effortText(c.effort))}</span>`;
const groupLabel = (key) => { const g = GROUP.get(key); return g ? pick(g.en, g.zh) : key; };
const taskTitle = (t) => pick(t.title_en, t.title_zh || t.title_en);
const sizeText = (t) => `${t.canvas[0]}×${t.canvas[1]}`;
const visibleConfigs = (set) => (set === 'main' ? CONFIGS.filter((c) => c.main) : CONFIGS);
const svgEl = (tag, attrs) => {
  const n = document.createElementNS('http://www.w3.org/2000/svg', tag);
  Object.entries(attrs || {}).forEach(([k, v]) => n.setAttribute(k, String(v)));
  return n;
};
const ticksBy = (lo, hi, step) => {
  const out = [];
  for (let v = Math.ceil(lo / step - 1e-9) * step; v <= hi + 1e-9; v += step) out.push(Math.round(v * 1e6) / 1e6);
  return out;
};

/* ── shared tooltip: values lead, labels follow; text goes in through textContent ── */
function showTip(pos, lines) {
  const el = $('#vizTip');
  el.replaceChildren();
  lines.forEach((ln) => {
    const row = document.createElement('div');
    row.className = 'tip-row';
    if (ln.color) {
      const key = document.createElement('i');
      key.className = 'tip-key';
      key.style.background = ln.color;
      row.appendChild(key);
    }
    if (ln.value != null) {
      const b = document.createElement('strong');
      b.textContent = ln.value;
      row.appendChild(b);
    }
    if (ln.text) {
      const s = document.createElement('span');
      s.textContent = ln.text;
      row.appendChild(s);
    }
    el.appendChild(row);
  });
  el.hidden = false;
  moveTip(pos);
}
function moveTip(pos) {
  const el = $('#vizTip');
  const pad = 14;
  const r = el.getBoundingClientRect();
  let x = pos.clientX + pad, y = pos.clientY + pad;
  if (x + r.width > window.innerWidth - 8) x = pos.clientX - r.width - pad;
  if (y + r.height > window.innerHeight - 8) y = pos.clientY - r.height - pad;
  el.style.left = `${Math.max(4, x)}px`;
  el.style.top = `${Math.max(4, y)}px`;
}
function hideTip() { $('#vizTip').hidden = true; }
function bindTip(node, linesFn) {
  node.addEventListener('pointerenter', (e) => showTip(e, linesFn()));
  node.addEventListener('pointermove', moveTip);
  node.addEventListener('pointerleave', hideTip);
  node.addEventListener('focus', () => {
    const r = node.getBoundingClientRect();
    showTip({ clientX: r.right, clientY: r.top }, linesFn());
  });
  node.addEventListener('blur', hideTip);
}

/* ───────────────────────────── results ───────────────────────────── */
const res = { set: 'all', sort: 'all' };

function renderCatChips() {
  $('#catChips').innerHTML = GROUPS.map((g) => `<span>${esc(pick(g.en, g.zh))} ${g.n}</span>`).join('');
}

function renderStatBand() {
  const best = CONFIGS[0];
  const ag = META.agreement, jl = META.judge_loo, rl = META.rater_loo;
  const tiles = [
    [pick('Top score', '最高分'), fmt(best.score.all), cfgLabel(best)],
    [pick('Judge–human agreement', 'Judge 与人类一致性'), fmt(ag.mean, 3),
      pick(`Kendall τ per task, 95% CI [${fmt(ag.ci[0], 3)}, ${fmt(ag.ci[1], 3)}]`,
        `逐题 Kendall τ，95% 置信区间 [${fmt(ag.ci[0], 3)}, ${fmt(ag.ci[1], 3)}]`)],
    [pick('Raters under leave-one-out', '留一法下的评分者'), `${fmt(rl.range[0], 3)}–${fmt(rl.range[1], 3)}`,
      pick(`judge ${fmt(jl.mean, 3)}, above ${META.raters_below_judge} of the ${META.n_raters} raters`,
        `Judge 为 ${fmt(jl.mean, 3)}，高于其中 ${META.raters_below_judge} 位评分者`)],
    [pick('Leaderboard correlation', '榜单相关'), fmt(META.rho_judge_human, 3),
      pick('Spearman ρ between the judge and human leaderboards', 'Judge 榜单与人类榜单的 Spearman ρ')],
  ];
  $('#statBand').innerHTML = tiles.map(([dt, dd, sub]) =>
    `<div><dt>${esc(dt)}</dt><dd class="v">${esc(dd)}</dd><dd class="sub">${esc(sub)}</dd></div>`).join('');
}

function renderLeaderboard() {
  const key = res.sort;
  const val = (c) => (key === 'human' ? (c.human ? c.human.all : null) : c.score[key]);
  const rows = visibleConfigs(res.set).slice().sort((a, b) => {
    const va = val(a), vb = val(b);
    if (va == null || vb == null) return (va == null) - (vb == null) || b.score.all - a.score.all;
    return key === 'human' ? va - vb : vb - va;
  });
  $('#lbTable tbody').innerHTML = rows.map((c, k) => `
    <tr class="${c.main ? 'is-main' : 'is-extra'}${k === 0 ? ' top' : ''}">
      <td class="num rk">${val(c) == null ? '' : k + 1}</td>
      <td class="cfg"><span class="m">${esc(c.model)}</span>${effortTag(c)}</td>
      <td class="num judge"><div class="metric"><div class="bar" aria-hidden="true"><i style="width:${c.score.all.toFixed(2)}%"></i></div><b>${fmt(c.score.all)}</b></div></td>
      <td class="num">${fmt(c.score.gen)}</td>
      <td class="num">${fmt(c.score.edit)}</td>
      <td class="num">${c.human ? fmt(c.human.all) : '<span class="na">—</span>'}</td>
    </tr>`).join('');
  $$('#lbTable th.sortable').forEach((th) => th.classList.toggle('on', th.dataset.sort === key));
}

/* ── Figure 1: judge score vs. human rank, twelve main-table configurations ── */
function placeLabels(items, bounds, obstacles) {
  /* greedy: each label takes the first candidate offset that overlaps nothing placed so far */
  const placed = [];
  const hit = (a, b) => !(a.x + a.w <= b.x || b.x + b.w <= a.x || a.y + a.h <= b.y || b.y + b.h <= a.y);
  const area = (a, b) => Math.max(0, Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x))
    * Math.max(0, Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y));
  return items.map((it) => {
    const { px, py, w, h } = it;
    const cands = [
      { x: px + 9, y: py - h / 2, anchor: 'start' }, { x: px - 9 - w, y: py - h / 2, anchor: 'end' },
      { x: px - w / 2, y: py - 9 - h, anchor: 'middle' }, { x: px - w / 2, y: py + 9, anchor: 'middle' },
      { x: px + 7, y: py - 7 - h, anchor: 'start' }, { x: px + 7, y: py + 7, anchor: 'start' },
      { x: px - 7 - w, y: py - 7 - h, anchor: 'end' }, { x: px - 7 - w, y: py + 7, anchor: 'end' },
      { x: px + 9, y: py - h / 2 - 13, anchor: 'start', lead: true }, { x: px + 9, y: py - h / 2 + 13, anchor: 'start', lead: true },
      { x: px - 9 - w, y: py - h / 2 - 13, anchor: 'end', lead: true }, { x: px - 9 - w, y: py - h / 2 + 13, anchor: 'end', lead: true },
    ];
    let best = null;
    cands.forEach((c, k) => {
      const box = { x: c.x, y: c.y, w, h };
      let cost = 0;
      if (box.x < bounds.x0 || box.x + w > bounds.x1 || box.y < bounds.y0 || box.y + h > bounds.y1) cost += 1e6;
      placed.concat(obstacles).forEach((o) => { if (hit(box, o)) cost += area(box, o) + 50; });
      cost += k * 0.5;
      if (!best || cost < best.cost) best = { ...c, cost, box };
    });
    placed.push(best.box);
    return best;
  });
}

function renderScatter() {
  const host = $('#scatter');
  const pts = CONFIGS.filter((c) => c.main);
  const W = 540, H = 340, m = { l: 46, r: 12, t: 12, b: 44 };
  const xs = pts.map((c) => c.score.all), ys = pts.map((c) => c.human.all);
  const x0 = Math.floor(Math.min(...xs) - 2), x1 = Math.ceil(Math.max(...xs) + 2);
  const y0 = Math.floor(Math.min(...ys)) - 0.6, y1 = Math.ceil(Math.max(...ys)) + 0.6;
  const X = (v) => m.l + (v - x0) / (x1 - x0) * (W - m.l - m.r);
  const Y = (v) => m.t + (v - y0) / (y1 - y0) * (H - m.t - m.b);   /* rank 1 at the top */
  const svg = svgEl('svg', { viewBox: `0 0 ${W} ${H}`, role: 'img',
    'aria-label': pick('Mean judge score against mean human rank for the twelve main-table configurations',
      '主表 12 个配置的 Judge 平均分与人类平均名次') });
  ticksBy(y0, y1, 1).filter((v) => v % 2 === 1).forEach((v) => {
    svg.appendChild(svgEl('line', { class: 'grid', x1: m.l, x2: W - m.r, y1: Y(v), y2: Y(v) }));
    const t = svgEl('text', { class: 'tick', x: m.l - 8, y: Y(v) + 3.5, 'text-anchor': 'end' });
    t.textContent = String(v);
    svg.appendChild(t);
  });
  ticksBy(x0, x1, 5).forEach((v) => {
    svg.appendChild(svgEl('line', { class: 'grid', x1: X(v), x2: X(v), y1: m.t, y2: H - m.b }));
    const t = svgEl('text', { class: 'tick', x: X(v), y: H - m.b + 16, 'text-anchor': 'middle' });
    t.textContent = String(v);
    svg.appendChild(t);
  });
  svg.appendChild(svgEl('line', { class: 'axis', x1: m.l, x2: W - m.r, y1: H - m.b, y2: H - m.b }));
  const xl = svgEl('text', { class: 'axis-label', x: (m.l + W - m.r) / 2, y: H - 8, 'text-anchor': 'middle' });
  xl.textContent = pick('mean judge score →', 'Judge 平均分 →');
  svg.appendChild(xl);
  const yl = svgEl('text', { class: 'axis-label', transform: `translate(13 ${(m.t + H - m.b) / 2}) rotate(-90)`, 'text-anchor': 'middle' });
  yl.textContent = pick('mean human rank (1 = best)', '人类平均名次（1 为最好）');
  svg.appendChild(yl);

  const gLabels = svgEl('g', { class: 'labels' });
  const gPts = svgEl('g', {});
  svg.appendChild(gLabels);
  svg.appendChild(gPts);
  pts.forEach((c) => {
    gPts.appendChild(svgEl('circle', { class: 'pt', cx: X(c.score.all), cy: Y(c.human.all), r: 5 }));
  });
  host.replaceChildren(svg);

  /* labels: measure, then place greedily around their points */
  const order = pts.slice().sort((a, b) => b.score.all - a.score.all);
  const texts = order.map((c) => {
    const t = svgEl('text', { class: 'pt-label', x: 0, y: 0 });
    t.textContent = c.short;
    gLabels.appendChild(t);
    const bb = t.getBBox();
    return { c, t, w: bb.width || c.short.length * 5.8, h: 11 };
  });
  const obstacles = pts.map((c) => ({ x: X(c.score.all) - 7, y: Y(c.human.all) - 7, w: 14, h: 14 }));
  const spots = placeLabels(texts.map((o) => ({ px: X(o.c.score.all), py: Y(o.c.human.all), w: o.w, h: o.h })),
    { x0: m.l + 2, x1: W - m.r, y0: m.t, y1: H - m.b - 2 }, obstacles);
  texts.forEach((o, k) => {
    const s = spots[k];
    const x = s.anchor === 'start' ? s.x : s.anchor === 'end' ? s.x + o.w : s.x + o.w / 2;
    o.t.setAttribute('x', x.toFixed(1));
    o.t.setAttribute('y', (s.y + o.h - 2).toFixed(1));
    o.t.setAttribute('text-anchor', s.anchor);
    if (s.lead) {
      const px = X(o.c.score.all), py = Y(o.c.human.all);
      const lx = s.anchor === 'start' ? s.x - 2 : s.x + o.w + 2;
      gLabels.appendChild(svgEl('line', { class: 'leader', x1: px, y1: py, x2: lx, y2: s.y + o.h / 2 }));
    }
  });
  /* hit targets bigger than the marks */
  pts.forEach((c) => {
    const hitC = svgEl('circle', { class: 'hit', cx: X(c.score.all), cy: Y(c.human.all), r: 12, tabindex: 0 });
    bindTip(hitC, () => [
      { text: cfgLabel(c) },
      { value: fmt(c.score.all), text: pick('mean judge score', 'Judge 平均分') },
      { value: fmt(c.human.all), text: pick('mean human rank', '人类平均名次') },
    ]);
    svg.appendChild(hitC);
  });
}

/* ── Figure 2: reasoning effort ── */
function renderEffort() {
  const host = $('#effortChart');
  const study = D.effort_study;
  const order = META.effort_order;
  const used = order.filter((e) => study.some((s) => s.levels.some((l) => l.effort === e)));
  const W = 540, H = 316, m = { l: 46, r: 110, t: 14, b: 40 };
  const all = study.flatMap((s) => s.levels.map((l) => l.score));
  const y0 = Math.floor((Math.min(...all) - 2) / 5) * 5, y1 = Math.ceil((Math.max(...all) + 2) / 5) * 5;
  const band = (W - m.l - m.r) / used.length;
  const X = (e) => m.l + (used.indexOf(e) + 0.5) * band;
  const Y = (v) => m.t + (y1 - v) / (y1 - y0) * (H - m.t - m.b);

  const legend = document.createElement('div');
  legend.className = 'chart-legend';
  study.forEach((s, k) => {
    const item = document.createElement('span');
    const key = document.createElement('i');
    key.className = 'line-key';
    key.style.background = SERIES[k];
    item.appendChild(key);
    item.appendChild(document.createTextNode(s.model));
    legend.appendChild(item);
  });
  const ring = document.createElement('span');
  ring.className = 'ring-key-item';
  const rk = document.createElement('i');
  rk.className = 'ring-key';
  ring.appendChild(rk);
  ring.appendChild(document.createTextNode(pick('main-table level', '主表档位')));
  legend.appendChild(ring);

  const svg = svgEl('svg', { viewBox: `0 0 ${W} ${H}`, role: 'img',
    'aria-label': pick('Mean judge score by reasoning effort for three models', '三个模型在各思考强度下的 Judge 平均分') });
  ticksBy(y0, y1, 5).forEach((v) => {
    svg.appendChild(svgEl('line', { class: 'grid', x1: m.l, x2: W - m.r, y1: Y(v), y2: Y(v) }));
    const t = svgEl('text', { class: 'tick', x: m.l - 8, y: Y(v) + 3.5, 'text-anchor': 'end' });
    t.textContent = String(v);
    svg.appendChild(t);
  });
  svg.appendChild(svgEl('line', { class: 'axis', x1: m.l, x2: W - m.r, y1: H - m.b, y2: H - m.b }));
  used.forEach((e) => {
    const t = svgEl('text', { class: 'tick', x: X(e), y: H - m.b + 16, 'text-anchor': 'middle' });
    t.textContent = e;
    svg.appendChild(t);
  });
  const xl = svgEl('text', { class: 'axis-label', x: (m.l + W - m.r) / 2, y: H - 6, 'text-anchor': 'middle' });
  xl.textContent = pick('reasoning effort', '思考强度');
  svg.appendChild(xl);
  const yl = svgEl('text', { class: 'axis-label', transform: `translate(13 ${(m.t + H - m.b) / 2}) rotate(-90)`, 'text-anchor': 'middle' });
  yl.textContent = pick('mean judge score', 'Judge 平均分');
  svg.appendChild(yl);

  const ends = [];
  study.forEach((s, k) => {
    const col = SERIES[k];
    const d = s.levels.map((l, i) => `${i ? 'L' : 'M'}${X(l.effort).toFixed(1)} ${Y(l.score).toFixed(1)}`).join(' ');
    svg.appendChild(svgEl('path', { class: 'series', d, stroke: col }));
    s.levels.forEach((l) => {
      if (l.main) {
        svg.appendChild(svgEl('circle', { class: 'ring', cx: X(l.effort), cy: Y(l.score), r: 7.5, stroke: col }));
      }
      svg.appendChild(svgEl('circle', { class: 'dot', cx: X(l.effort), cy: Y(l.score), r: 4, fill: col }));
    });
    const last = s.levels[s.levels.length - 1];
    ends.push({ s, k, x: X(last.effort) + 12, y: Y(last.score) + 4 });
  });
  /* end labels: keep them at least 13px apart */
  ends.sort((a, b) => a.y - b.y);
  for (let i = 1; i < ends.length; i++) if (ends[i].y - ends[i - 1].y < 13) ends[i].y = ends[i - 1].y + 13;
  ends.forEach((e) => {
    const t = svgEl('text', { class: 'end-label', x: e.x, y: e.y });
    t.textContent = e.s.model;
    svg.appendChild(t);
  });
  study.forEach((s, k) => s.levels.forEach((l) => {
    const hitC = svgEl('circle', { class: 'hit', cx: X(l.effort), cy: Y(l.score), r: 12, tabindex: 0 });
    bindTip(hitC, () => [
      { color: SERIES[k], text: `${s.model} (${l.effort})` },
      { value: fmt(l.score), text: pick('mean judge score', 'Judge 平均分') },
      ...(l.main ? [{ text: pick('level of the main table', '主表档位') }] : []),
    ]);
    svg.appendChild(hitC);
  }));
  host.replaceChildren(legend, svg);
}

function renderAgreement() {
  const ag = META.agreement, jl = META.judge_loo, rl = META.rater_loo, oj = META.other_judges;
  const ci = `[${fmt(ag.ci[0], 3)}, ${fmt(ag.ci[1], 3)}]`;
  $('#agreeEn').innerHTML = `Per task, the judge's twelve scores agree with the consensus order of the ten raters at
    Kendall τ = <strong>${fmt(ag.mean, 3)}</strong> ${ci}. Holding out one rater at a time, the judge reaches
    <strong>${fmt(jl.mean, 3)}</strong> against the other nine, and the held-out raters reach
    ${fmt(rl.range[0], 3)} to ${fmt(rl.range[1], 3)}: the judge sits inside the range of the raters, above
    ${META.raters_below_judge} of them. Under the same protocol, Claude Opus 5 and DeepSeek V4.1 Flash as judges agree
    less with the raters, at ${fmt(oj['claude-opus-5'], 3)} and ${fmt(oj['deepseek-v4.1-flash'], 3)}.`;
  $('#agreeZh').innerHTML = `逐题来看，Judge 对 12 件作品的打分与十位人类评分者共识排序的一致性为 Kendall τ = <strong>${fmt(ag.mean, 3)}</strong> ${ci}。每次留出一位评分者时，Judge 与其余九人共识的一致性为 <strong>${fmt(jl.mean, 3)}</strong>，留出的评分者为 ${fmt(rl.range[0], 3)} 至 ${fmt(rl.range[1], 3)}：Judge 落在评分者的范围之内，高于其中 ${META.raters_below_judge} 位。在同一协议下，以 Claude Opus 5 和 DeepSeek V4.1 Flash 作为评审时，与评分者的一致性更低，分别为 ${fmt(oj['claude-opus-5'], 3)} 和 ${fmt(oj['deepseek-v4.1-flash'], 3)}。`;
  $$('[data-num="rho"]').forEach((n) => { n.textContent = fmt(META.rho_judge_human, 3); });
  $$('[data-num="rhoRef"]').forEach((n) => { n.textContent = fmt(META.rho_reference_split, 3); });
}

/* ── Table 2: score by subject and editing type (sequential, one hue) ── */
function rampColor(v, lo, hi) {
  const t = Math.max(0, Math.min(1, (v - lo) / (hi - lo)));
  const i = Math.round(t * (RAMP.length - 1));
  return { bg: RAMP[i], ink: i >= 7 ? '#ffffff' : '#14141a' };
}
function renderHeat() {
  const rows = visibleConfigs(res.set);
  /* colour domain from the 5th to the 95th percentile, so a few slices with very few
     tasks (multiview has two) do not flatten the contrast of every other cell */
  const vals = rows.flatMap((c) => GROUPS.map((g) => c.groups[g.key])).sort((a, b) => a - b);
  const q = (f) => vals[Math.round(f * (vals.length - 1))];
  const lo = Math.floor(q(0.05) / 5) * 5, hi = Math.ceil(q(0.95) / 5) * 5;
  const nGen = GROUPS.filter((g) => !['edit', 'animation', 'multiview'].includes(g.key)).length;
  const head = `<thead>
    <tr class="grp"><th></th><th colspan="${nGen}">${esc(pick('Generation', '生成'))}</th>
      <th colspan="${GROUPS.length - nGen}">${esc(pick('Editing', '编辑'))}</th></tr>
    <tr><th>${esc(pick('Configuration', '配置'))}</th>${GROUPS.map((g, k) =>
      `<th class="${k === nGen ? 'split' : ''}">${esc(pick(g.en, g.zh))}<span class="n">${g.n}</span></th>`).join('')}</tr>
  </thead>`;
  const body = rows.map((c) => `<tr><th><span class="m">${esc(c.model)}</span>${effortTag(c)}</th>${GROUPS.map((g, k) => {
    const v = c.groups[g.key];
    const col = rampColor(v, lo, hi);
    return `<td class="${k === nGen ? 'split' : ''}" style="background:${col.bg};color:${col.ink}" data-cfg="${esc(c.id)}" data-g="${g.key}">${fmt(v, 1)}</td>`;
  }).join('')}</tr>`).join('');
  $('#heatTable').innerHTML = head + `<tbody>${body}</tbody>`;
  const stops = RAMP.map((h, k) => `${h} ${(k / (RAMP.length - 1) * 100).toFixed(0)}%`).join(', ');
  $('#heatLegend').innerHTML = `<span>${esc(pick('Mean judge score', 'Judge 平均分'))}</span>
    <span class="scale"><b>≤${lo}</b><i style="background:linear-gradient(90deg, ${stops})"></i><b>≥${hi}</b></span>`;
}
function initHeatTips() {
  const table = $('#heatTable');
  table.addEventListener('pointerover', (e) => {
    const td = e.target.closest('td[data-cfg]');
    if (!td) return;
    const c = CFG.get(td.dataset.cfg), g = GROUP.get(td.dataset.g);
    showTip(e, [{ text: cfgLabel(c) }, { value: fmt(c.groups[g.key], 2), text: `${pick(g.en, g.zh)} · ${g.n} ${pick('tasks', '题')}` }]);
  });
  table.addEventListener('pointermove', (e) => { if (e.target.closest('td[data-cfg]')) moveTip(e); });
  table.addEventListener('pointerout', (e) => { if (!e.relatedTarget || !table.contains(e.relatedTarget)) hideTip(); });
}

/* ── editing examples ── */
function thumbHTML(srcs, alt, extraClass = '') {
  const multi = srcs.length > 1;
  return `<div class="thumb${multi ? ' anim' : ''}${extraClass}"${multi ? ` data-n="${srcs.length}" data-f="0"` : ''}>${
    srcs.map((s, k) => `<img src="${s}" alt="${k ? '' : esc(alt)}" loading="lazy" decoding="async">`).join('')}</div>`;
}
function renderEditExamples() {
  const c = CFG.get('gpt-6-astra');
  $('#editExamples').innerHTML = EDIT_EXAMPLES.map((id) => {
    const t = TASK.get(id);
    if (!t || !c) return '';
    const fr = t.img[c.id];
    return `<figure class="edit-card" data-task="${esc(id)}" tabindex="0">
      <div class="edit-pair">
        <div class="ep">${thumbHTML([t.original], `${t.title_en}, original`, ' big')}<span>${esc(pick('Original', '原图'))}</span></div>
        <span class="ep-arrow" aria-hidden="true">→</span>
        <div class="ep">${thumbHTML(fr, `${t.title_en}, GPT-6 Astra`, ' big')}<span>GPT-6 Astra · <b>${fmt(t.judge[c.id], 0)}</b></span></div>
      </div>
      <figcaption><span class="ec-title">${esc(taskTitle(t))}</span><span class="rh-chip cat">${esc(groupLabel(t.group))}</span>
        <span class="ec-prompt">${esc(LANG === 'zh' && t.prompt_zh ? t.prompt_zh : t.prompt_en)}</span></figcaption>
    </figure>`;
  }).join('');
  $$('#editExamples .edit-card').forEach((card) => {
    const open = () => openLightbox(TASK.get(card.dataset.task), c);
    card.addEventListener('click', open);
    card.addEventListener('keydown', (e) => { if (e.key === 'Enter') open(); });
  });
}

/* ───────────────────────────── gallery ───────────────────────────── */
const gal = { set: 'all', cat: '', sort: 'idx', metric: 'judge', q: '', best: true, zoom: false, rows: new Map(), built: '' };
const galConfigs = () => visibleConfigs(gal.set);
const rowMean = (t) => { const cs = galConfigs(); return cs.reduce((a, c) => a + t.judge[c.id], 0) / cs.length; };

function cellBadge(t, c) {
  if (gal.metric === 'judge') return fmt(t.judge[c.id], 0);
  if (gal.metric === 'human') return c.main ? fmt(t.human[c.id], 1) : '';
  return '';
}

function buildGallery() {
  const cs = galConfigs();
  $('#galHead').innerHTML = `<th class="corner">${esc(pick('Task ↓ · configuration →', '题目 ↓ · 配置 →'))}</th>` + cs.map((c) => `
    <th class="sortable" data-cfg="${esc(c.id)}" title="${esc(pick('sort rows by this configuration', '按该配置的分数排序'))}">
      <span class="m-name">${esc(c.short)}</span>${effortTag(c)}<span class="m-sub">${fmt(c.score.all, 1)}</span>
    </th>`).join('');
  $$('#galHead th.sortable').forEach((th) => th.addEventListener('click', () => {
    const id = th.dataset.cfg;
    gal.sort = gal.sort === `cfg:${id}` ? `cfg-asc:${id}` : `cfg:${id}`;
    applyGallery();
  }));
  const body = $('#galBody');
  body.innerHTML = '';
  gal.rows.clear();
  TASKS.forEach((t) => {
    const tr = document.createElement('tr');
    tr.dataset.id = t.id;
    const frames = t.frames > 1 ? `<span class="rh-chip">${t.frames} ${esc(pick('frames', '帧'))}</span>` : '';
    const orig = t.original ? `<div class="rh-orig" title="${esc(pick('the input artwork', '输入的原图'))}">${
      thumbHTML([t.original], `${t.title_en}, original`)}<span>${esc(pick('original', '原图'))}</span></div>` : '';
    tr.innerHTML = `<td class="rowhead"><div class="rh-wrap"><div class="rh-text">
        <span class="rh-idx">#${t.idx}</span><span class="rh-title">${esc(taskTitle(t))}</span>
        <div class="rh-meta"><span class="rh-chip size">${sizeText(t)}</span><span class="rh-chip cat">${esc(groupLabel(t.group))}</span>${frames}</div>
        <div class="rh-best"></div></div>${orig}</div></td>` +
      cs.map((c) => `<td class="cell" data-cfg="${esc(c.id)}">${thumbHTML(t.img[c.id], `${t.title_en}, ${cfgLabel(c)}`)
        .replace(/<\/div>$/, '<span class="score"></span></div>')}</td>`).join('');
    tr.addEventListener('click', (e) => {
      if (e.target.closest('.rh-orig')) { openLightbox(t, null); return; }
      const td = e.target.closest('td.cell');
      if (td) openLightbox(t, CFG.get(td.dataset.cfg));
    });
    body.appendChild(tr);
    gal.rows.set(t.id, tr);
  });
  gal.built = gal.set;
}

function taskMatches(t) {
  const q = gal.q.trim().toLowerCase();
  const catOk = !gal.cat || (gal.cat === 'gen' ? t.family === 'text2image'
    : gal.cat === 'editall' ? t.family !== 'text2image' : t.group === gal.cat);
  if (!catOk) return false;
  if (!q) return true;
  const g = GROUP.get(t.group) || {};
  return [t.id, t.title_en, t.title_zh, t.prompt_en, t.prompt_zh, g.en, g.zh, sizeText(t)]
    .join(' ').toLowerCase().includes(q);
}

function applyGallery() {
  if (gal.built !== gal.set) buildGallery();
  const cs = galConfigs();
  let visible = 0;
  TASKS.forEach((t) => {
    const tr = gal.rows.get(t.id);
    const ok = taskMatches(t);
    tr.hidden = !ok;
    if (!ok) return;
    visible++;
    const top = Math.max(...cs.map((c) => t.judge[c.id]));
    const winners = cs.filter((c) => t.judge[c.id] === top);
    $('.rh-best', tr).textContent = `${pick('best', '最高')}: ${winners.map((c) => cfgLabel(c)).join(', ')} · ${fmt(top, 0)}`;
    $$('td.cell[data-cfg]', tr).forEach((td) => {
      const c = CFG.get(td.dataset.cfg);
      const badge = $('.score', td);
      const text = cellBadge(t, c);
      badge.textContent = text;
      badge.hidden = !text;
      td.classList.toggle('best', gal.best && t.judge[c.id] === top);
    });
  });
  const order = TASKS.slice();
  const area = (t) => t.canvas[0] * t.canvas[1];
  if (gal.sort === 'size') order.sort((a, b) => area(b) - area(a) || a.idx - b.idx);
  else if (gal.sort === 'easy') order.sort((a, b) => rowMean(b) - rowMean(a));
  else if (gal.sort === 'hard') order.sort((a, b) => rowMean(a) - rowMean(b));
  else if (gal.sort === 'raters') order.sort((a, b) => a.rater_tau - b.rater_tau);
  else if (gal.sort.startsWith('cfg')) {
    const id = gal.sort.split(':')[1];
    const asc = gal.sort.startsWith('cfg-asc');
    order.sort((a, b) => (asc ? a.judge[id] - b.judge[id] : b.judge[id] - a.judge[id]) || a.idx - b.idx);
  } else order.sort((a, b) => a.idx - b.idx);
  const body = $('#galBody');
  order.forEach((t) => body.appendChild(gal.rows.get(t.id)));
  $$('#galHead th.sortable').forEach((th) => th.classList.toggle('on', gal.sort.endsWith(`:${th.dataset.cfg}`)));
  if (!gal.sort.startsWith('cfg')) $('#sortSel').value = gal.sort;
  $('#galCount').textContent = pick(
    `${visible} of ${TASKS.length} tasks · ${(visible * cs.length).toLocaleString('en-US')} artworks · ${cs.length} configurations`,
    `显示 ${visible}/${TASKS.length} 道题 · ${(visible * cs.length).toLocaleString('en-US')} 件作品 · ${cs.length} 个配置`);
  renderGalleryLegend();
}

function renderGalleryLegend() {
  const parts = gal.metric === 'judge'
    ? [pick('Badge: judge score, 0–100', '角标：Judge 分数（0–100）')]
    : gal.metric === 'human'
      ? [pick('Badge: mean rank among the twelve main-table configurations over the ten raters (1 = best)',
        '角标：十位人类评分者在主表 12 个配置中的平均名次（1 为最好）')]
      : [];
  parts.push(pick('outline: highest judge score in the row', '外框：该行 Judge 最高分'),
    pick('multi-frame results loop', '多帧结果循环播放'),
    pick('click for full size', '点击查看大图'));
  $('#legend').innerHTML = parts.map((p) => `<span>${esc(p)}</span>`).join('');
}

function refreshGalleryControls() {
  const setSel = $('#galCfgSel');
  setSel.innerHTML = `<option value="all">${esc(pick('All 20', '全部 20 个'))}</option>
    <option value="main">${esc(pick('Main table (12)', '论文主表（12 个）'))}</option>`;
  setSel.value = gal.set;
  const catSel = $('#catSel');
  const nGen = TASKS.filter((t) => t.family === 'text2image').length;
  catSel.innerHTML = [
    `<option value="">${esc(pick(`All tasks (${TASKS.length})`, `全部题目（${TASKS.length}）`))}</option>`,
    `<option value="gen">${esc(pick(`Generation (${nGen})`, `生成（${nGen}）`))}</option>`,
    `<option value="editall">${esc(pick(`Editing (${TASKS.length - nGen})`, `编辑（${TASKS.length - nGen}）`))}</option>`,
    ...GROUPS.map((g) => `<option value="${g.key}">· ${esc(pick(g.en, g.zh))} (${g.n})</option>`),
  ].join('');
  catSel.value = gal.cat;
  const sortSel = $('#sortSel');
  sortSel.innerHTML = [
    ['idx', pick('Task order', '题目顺序')], ['size', pick('Canvas size', '画幅大小')],
    ['easy', pick('Highest row mean first', '行平均分从高到低')], ['hard', pick('Lowest row mean first', '行平均分从低到高')],
    ['raters', pick('Rater disagreement first', '评分者分歧大的优先')],
  ].map(([v, l]) => `<option value="${v}">${esc(l)}</option>`).join('');
  sortSel.value = gal.sort.startsWith('cfg') ? 'idx' : gal.sort;
  const metricSel = $('#metricSel');
  metricSel.innerHTML = [
    ['judge', pick('Judge score', 'Judge 分数')], ['human', pick('Human rank (main table)', '人类名次（主表）')],
    ['none', pick('None', '不显示')],
  ].map(([v, l]) => `<option value="${v}">${esc(l)}</option>`).join('');
  metricSel.value = gal.metric;
  $('#searchBox').placeholder = pick('dragon, 64×64, animation…', '龙、64×64、动画……');
}

function refreshGalleryLang() {
  if (!gal.rows.size) return;
  refreshGalleryControls();
  buildGallery();
  applyGallery();
}

function initGallery() {
  refreshGalleryControls();
  buildGallery();
  $('#galCfgSel').addEventListener('change', (e) => { gal.set = e.target.value; applyGallery(); });
  $('#catSel').addEventListener('change', (e) => { gal.cat = e.target.value; applyGallery(); });
  $('#sortSel').addEventListener('change', (e) => { gal.sort = e.target.value; applyGallery(); });
  $('#metricSel').addEventListener('change', (e) => { gal.metric = e.target.value; applyGallery(); });
  $('#searchBox').addEventListener('input', (e) => { gal.q = e.target.value; applyGallery(); });
  $('#bestToggle').addEventListener('change', (e) => { gal.best = e.target.checked; applyGallery(); });
  $('#zoomToggle').addEventListener('change', (e) => {
    gal.zoom = e.target.checked;
    $('#galleryTable').classList.toggle('zoom', gal.zoom);
  });
  applyGallery();
}

/* multi-frame thumbnails: one timer flips only the animated cells (a live collection) */
function startFrameTicker() {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const anim = document.getElementsByClassName('anim');
  let tick = 0;
  setInterval(() => {
    tick++;
    for (const el of anim) el.dataset.f = String(tick % Number(el.dataset.n || 1));
  }, 650);
}

/* ───────────────────────────── lightbox ───────────────────────────── */
const lb = { task: null, cfg: null };
function openLightbox(t, c) {
  if (!t) return;
  lb.task = t;
  lb.cfg = c;
  const items = [];
  if (t.original) items.push({ src: t.original, cap: pick('Original', '原图') });
  if (c) {
    const fr = t.img[c.id];
    fr.forEach((s, k) => items.push({ src: s, cap: fr.length > 1 ? pick(`Frame ${k + 1}`, `第 ${k + 1} 帧`) : cfgLabel(c) }));
  }
  const box = $('#lbFrames');
  box.innerHTML = items.map((it) => `<figure class="lbf"><img src="${it.src}" alt=""><figcaption>${esc(it.cap)}</figcaption></figure>`).join('');
  /* one integer scale for every image in the row, so the original and the frames keep their true sizes */
  const maxW = Math.min(window.innerWidth * 0.9, 1180) / items.length - 18;
  const maxH = window.innerHeight * 0.56;
  const imgs = $$('img', box);
  Promise.all(imgs.map((im) => (im.complete && im.naturalWidth ? Promise.resolve()
    : new Promise((ok) => { im.addEventListener('load', ok, { once: true }); im.addEventListener('error', ok, { once: true }); }))))
    .then(() => {
      const s = Math.min(...imgs.map((im) => Math.min(maxW / (im.naturalWidth || 1), maxH / (im.naturalHeight || 1))));
      const k = s >= 1 ? Math.floor(s) : s;
      imgs.forEach((im) => {
        im.style.width = `${Math.round(im.naturalWidth * k)}px`;
        im.style.height = `${Math.round(im.naturalHeight * k)}px`;
      });
    });
  const facts = [];
  if (c) {
    facts.push(`${esc(cfgLabel(c))}: ${esc(pick('judge score', 'Judge 分数'))} <strong>${fmt(t.judge[c.id], 0)}</strong>`);
    if (c.main) facts.push(`${esc(pick('mean human rank', '人类平均名次'))} <strong>${fmt(t.human[c.id], 1)}</strong> / 12`);
  }
  facts.push(`${esc(groupLabel(t.group))} · ${t.original ? esc(pick('input ', '原图 ')) : ''}${sizeText(t)}${t.frames > 1 ? ` · ${t.frames} ${esc(pick('frames', '帧'))}` : ''}`);
  const zh = LANG === 'zh' && t.prompt_zh ? `<span class="lb-prompt zh">${esc(t.prompt_zh)}</span>` : '';
  $('#lbCap').innerHTML = `
    <span class="lb-title">#${t.idx} ${esc(t.title_en)}${t.title_zh ? ` · ${esc(t.title_zh)}` : ''}</span>
    <span class="lb-metrics">${facts.join(' &nbsp;·&nbsp; ')}</span>
    <span class="lb-prompt-label">${esc(pick('Task statement, as given to the model', '题目陈述（模型收到的原文）'))}</span>
    <span class="lb-prompt">${esc(t.prompt_en)}</span>${zh}
    ${c ? `<span class="lb-hint">${esc(pick('← → other configurations · Esc closes', '← → 切换配置 · Esc 关闭'))}</span>` : ''}`;
  $('#lightbox').hidden = false;
}
function stepLightbox(dir) {
  if (!lb.task || !lb.cfg) return;
  const cs = galConfigs().some((c) => c.id === lb.cfg.id) ? galConfigs() : CONFIGS;
  const k = cs.findIndex((c) => c.id === lb.cfg.id);
  openLightbox(lb.task, cs[(k + dir + cs.length) % cs.length]);
}
function initLightbox() {
  const close = () => { $('#lightbox').hidden = true; };
  $('#lbClose').addEventListener('click', close);
  $('#lightbox').addEventListener('click', (e) => { if (e.target.id === 'lightbox') close(); });
  document.addEventListener('keydown', (e) => {
    if ($('#lightbox').hidden) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowRight') stepLightbox(1);
    if (e.key === 'ArrowLeft') stepLightbox(-1);
  });
}

/* ───────────────────────────── wiring ───────────────────────────── */
function renderAll() {
  renderCatChips();
  renderStatBand();
  renderLeaderboard();
  renderScatter();
  renderEffort();
  renderAgreement();
  renderHeat();
  renderEditExamples();
  refreshGalleryLang();
}

function initResults() {
  $$('#cfgSeg button').forEach((b) => b.addEventListener('click', () => {
    res.set = b.dataset.set;
    $$('#cfgSeg button').forEach((x) => x.classList.toggle('is-on', x === b));
    renderLeaderboard();
    renderHeat();
  }));
  $$('#lbTable th.sortable').forEach((th) => th.addEventListener('click', () => {
    res.sort = th.dataset.sort;
    renderLeaderboard();
  }));
  initHeatTips();
  $('#copyBib').addEventListener('click', () => {
    const text = $('#bibtex').textContent;
    const done = () => { $('#copyBib').classList.add('done'); setTimeout(() => $('#copyBib').classList.remove('done'), 1400); };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, () => {});
  });
}

/* ───────────────────────────── boot ───────────────────────────── */
function boot() {
  if (!SCORES || !SESSION) {
    document.body.insertAdjacentHTML('afterbegin',
      '<p style="padding:16px;background:#ffe8e8;font:14px sans-serif">' +
      'Page data missing: expected <code>data/scores.js</code> and <code>case/data/session.js</code>.</p>');
    return;
  }
  let saved = null;
  try { saved = localStorage.getItem('pb-lang'); } catch (e) { /* ignore */ }
  const lang = saved || ((navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en');
  $('#langToggle').addEventListener('click', () => setLang(LANG === 'zh' ? 'en' : 'zh'));
  initPlayer();
  /* inspection hook: lets tools/check_site.py verify the playback schedule */
  window.PixelBenchPlayer = {
    frameMs: (i) => frameMs(i),
    totalMs: () => totalMs(),
    durations: () => durations.slice(),
    fastLoops: () => fastLoops,
    state: () => ({ frame: player.i, playing: player.playing, stmtKey: player.stmtKey,
                    compressedFrames: player.compressedFrames }),
    loaded: () => ({ ready: framesReady, total: frameCount, drawn: lastDrawn }),
    stageSignature: () => { const cv = document.querySelector('#stageCanvas');
      const d = cv.getContext('2d').getImageData(0, 0, cv.width, cv.height).data;
      let h = 2166136261; for (let i = 0; i < d.length; i += 4) {
        h ^= d[i] + d[i + 1] * 3 + d[i + 2] * 7 + d[i + 3] * 11; h = Math.imul(h, 16777619);
      } return h >>> 0; },
  };
  initResults();
  initGallery();
  initLightbox();
  startFrameTicker();
  setLang(lang);
}
document.addEventListener('DOMContentLoaded', boot);
})();
