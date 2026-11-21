from pixelbench_api import *

src = input_canvas
W, H = src.stats()['size']
TOP = 4
OUT_H = H + 8

def make_shear(amp):
    """Vertical per-column ramp: dy grows from 0 at the mast side to amp at the fly end."""
    out = new_canvas(W, OUT_H)
    for x in range(W):
        dy = int(round(amp * x / (W - 1)))
        for y in range(H):
            idx = src.get(x, y)
            if idx != 0:
                out.set(x, y + TOP + dy, idx)
    return out

# Frame 1: original picture content preserved, on the enlarged canvas.
f1 = new_canvas(W, OUT_H)
f1.blit(src, 0, TOP)

# Frame 2: fly end at its highest point (right side swung up).
f2 = make_shear(-4)

# Frame 3: fly end at its lowest point (right side swung down).
f3 = make_shear(+4)

finish([f1, f2, f3])
