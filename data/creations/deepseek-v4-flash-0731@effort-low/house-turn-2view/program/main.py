from pixelbench_api import *

c = input_canvas
f1 = c.copy(name="f1")

W, H = 112, 157
f2 = new_canvas(W, H)

# ---- Frame 2: 90-degree rotation, only the right-hand wall (with window) visible.
# The input is an elevated-isometric corner view.  The right-hand wall occupies
# columns roughly [62..103].  To render the "90 degree" one-wall view (house yawed
# so the right wall faces the fixed elevated camera) we take that right strip and
# shear each column vertically so the strip top becomes a straight horizontal
# line -> an upright single-face render at the same 45-degree high camera pitch.
x0, x1 = 62, 103
cols = []
for x in range(x0, x1 + 1):
    ts = [y for y in range(H) if c.get(x, y) is not None]
    if ts:
        cols.append((x, min(ts), max(ts)))

top_ref = max(t for (_, t, _) in cols)
dest_w = x1 - x0 + 1
dx = (W - dest_w) // 2 - x0

for (x, t, b) in cols:
    o = top_ref - t          # shear so the top edge flattens to row `top_ref`
    for y in range(t, b + 1):
        idx = c.get(x, y)
        if idx is not None:
            f2.set(x + dx, y + o, idx)

# Center vertically inside the canvas so nothing clips.
bbox = f2.stats()['bbox']
if bbox is not None:
    sv = max(8, (H - (bbox[3] - bbox[1])) // 2 - bbox[1])
    f2.shift(0, sv)

print("F1:", f1.stats_text())
print("F2:", f2.stats_text())
print(f2.matrix_text())
print("SUBMITTING 2 frames: f1 (45d front+right), f2 (90d right wall only)")
finish([f1, f2])
