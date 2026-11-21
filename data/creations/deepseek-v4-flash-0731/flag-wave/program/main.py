from pixelbench_api import input_canvas, new_canvas, finish

SRC = input_canvas
AMP = 6                 # max swing of the fly end (pixels)
W, H = 48, 72
OFF = 8                 # vertical placement of the original so the highest swing fits
PIVOT = 24              # anchor x: flag pixels farther right swing more
SPAN = 47 - PIVOT        # 23

def is_flag(x, y):
    # flag region of the source sprite
    if y <= 15:
        return x >= 28
    if y <= 35:
        return x >= 20
    return False

def swing(direction):
    # direction -1: fly end rises to its highest point; +1: drops to its lowest
    w, h, rgba = SRC.to_rgba()
    c = new_canvas(W, H)
    for y in range(h):
        for x in range(w):
            i = (y * w + x) * 4
            r, g, b, a = rgba[i], rgba[i + 1], rgba[i + 2], rgba[i + 3]
            if a == 0:
                continue
            if is_flag(x, y):
                dy = direction * round(AMP * max(0, x - PIVOT) / SPAN)
            else:
                dy = 0
            c.set(x, y + OFF + dy, (r, g, b, a))
    return c

f1 = new_canvas(W, H)
f1.blit(SRC, 0, OFF)
f2 = swing(-1)   # fly end at its HIGHEST
f3 = swing(+1)   # fly end at its LOWEST

finish([f1, f2, f3])
