from pixelbench_api import *

out = input_canvas.copy(name='output')

def recolor(src_hex, dst_hex):
    src = out.color(src_hex)
    dst = out.color(dst_hex)
    w, h = out.stats()['size']
    for y in range(h):
        for x in range(w):
            if out.get(x, y) == src:
                out.set(x, y, dst)

# --- turn the water (and label) blue family into a purple magic potion ---
recolor("#2f7598", "#5e2ba8")   # deep liquid violet
recolor("#74b8cf", "#8f4fd3")   # medium purple (label/body)
recolor("#77b7ce", "#a263da")   # light purple
recolor("#76b7d1", "#b678e6")   # lighter purple
recolor("#7bb5cb", "#a567e0")   # highlight purple
recolor("#31121d", "#30105c")   # emblem -> deep violet

# --- bubbles ---
lav  = out.color("#e9d5ff")   # bubble rim
glow = out.color("#f8eeff")   # bubble highlight

bubbles = [
    (40, 28, 1), (30, 29, 2), (20, 32, 3), (36, 33, 1), (10, 35, 2),
    (15, 37, 2), (38, 38, 2), (28, 40, 1), (8, 42, 2),  (46, 42, 1),
    (24, 43, 3), (12, 45, 2), (34, 45, 2), (44, 45, 1),
]
for (cx, cy, r) in bubbles:
    out.circle(cx, cy, r, lav, fill=False)
    if r >= 2:
        out.set(cx - 1, cy - 1, glow)

print(out.stats_text())

finish(out)

