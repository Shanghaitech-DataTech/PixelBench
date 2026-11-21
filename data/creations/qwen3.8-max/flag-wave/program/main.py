import math
from pixelbench_api import *

# ---- flag-wave animation, 3 frames (48x64, original padded with 8px head-room) ----
W, H = 48, 64
PAD = 8           # head-room above the original so the fly end can swing up
ATTACH = 20       # columns left of this (pole + hoist bands) stay fixed
SPAN = 27.0

src = input_canvas
trans = {p['index'] for p in src.palette() if p['rgba'][3] == 0}


def make_frame(dy_fn):
    c = new_canvas(W, H)
    for x in range(W):
        if x < ATTACH:
            dy = 0
        else:
            dy = dy_fn((x - ATTACH) / SPAN)
        for y in range(56):
            idx = src.get(x, y)
            if idx in trans:
                continue
            c.set(x, y + PAD + dy, idx)
    return c


# frame 1: original picture, unchanged, on the taller canvas
f1 = new_canvas(W, H)
f1.blit(src, 0, PAD)

# frame 2: fly end at its highest (whole cloth lifts, curved)
f2 = make_frame(lambda t: -int(round(6 * t + 1.0 * math.sin(math.pi * t))))

# frame 3: fly end at its lowest (slight lift near hoist, deep sag at fly)
f3 = make_frame(lambda t: int(round(9 * t * t - 2.0 * math.sin(math.pi * t))))

print(view(f1))
print(view(f2))
print(view(f3))

finish([f1, f2, f3])
