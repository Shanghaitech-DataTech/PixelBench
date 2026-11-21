from pixelbench_api import *

src = input_canvas
W, H = 48, 56
CH = 70          # tall enough to fit the full downward swing with the pole fixed

ANCHOR = 4       # pole / hoist; cloth beyond it waves
FLY = 47

def make(phase):
    c = new_canvas(W, CH)
    for x in range(W):
        w = 0.0 if x <= ANCHOR else (x - ANCHOR) / (FLY - ANCHOR)
        down = round(phase * w * w)     # curved droop, strongest at the fly end
        for y in range(H):
            col = src.get(x, y)
            if col:
                c.set(x, y + down, col)
    return c

# Frame 1 keeps the original picture content: fly end at its highest point.
f1 = new_canvas(W, CH); f1.blit(src, 0, 0)

# Frames 2 and 3 continue the looping flag-wave: the fly end swings downward
# from its highest point (frame 1) through mid (frame 2) to its lowest (frame 3).
f2 = make(6)
f3 = make(12)

finish([f1, f2, f3])
print("submitted")
