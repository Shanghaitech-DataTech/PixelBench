from pixelbench_api import *

src = input_canvas
W, H = 48, 72
pal = src.palette()
idx_alpha = {p['index']: p['rgba'][3] for p in pal}

def build(dy, amp):
    """Rebuild the flag on a 48x72 canvas. Each column is shifted vertically by
    amp*(x-6)/35, so the pole (x ~ 0..7) stays anchored while the fly end
    (x ~ 47) swings up (amp negative) or down (amp positive)."""
    out = new_canvas(W, H)
    for y in range(56):
        for x in range(48):
            i = src.get(x, y)
            if i is not None and i in idx_alpha and idx_alpha[i] > 0:
                yy = round(y + dy + amp * (x - 6) / 35.0)
                out.set(x, yy, i)
    return out

# Frame 1: original picture content (kept as-is, just positioned on the canvas).
f1 = build(8, 0.0)
# Frame 2: fly end at its highest point (flag lifted).
f2 = build(8, -6.0)
# Frame 3: fly end at its lowest point (flag drooped).
f3 = build(8, +6.0)

print(f1.stats_text())
print(f2.stats_text())
print(f3.stats_text())

finish([f1, f2, f3])
