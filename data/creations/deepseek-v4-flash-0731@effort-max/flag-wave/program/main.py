from pixelbench_api import *

src = input_canvas
w, h = 48, 56
pal = src.palette()
A = 10.0  # maximum droop of the fly end


def is_vis(idx):
    return pal[idx]['rgba'][3] > 0


def wave(swing, name):
    """Flag panel (columns 20..47, rows 0..35) sags about its attachment:
    each column is shifted straight down by dy that ramps from 0 at the
    pole to A*swing at the fly end.  Frame 1 is the untouched highest
    position; later frames sweep the fly end down to its lowest point."""
    f = new_canvas(w, h, name=name)
    for x in range(w):
        if x < 20:                       # pole / figure: fixed
            for y in range(h):
                idx = src.get(x, y)
                if is_vis(idx):
                    f.set(x, y, idx)
        else:                            # flag panel: sags toward the fly
            dy = round(A * ((x - 20) / 27.0) ** 1.4 * swing)
            for y in range(36):
                idx = src.get(x, y)
                if is_vis(idx):
                    f.set(x, y + dy, idx)
    return f


f1 = src.copy(name="f1")
f2 = wave(0.5, "f2")
f3 = wave(1.0, "f3")

# verification: fly-end (x=47) top pixel row per frame and overall stats
for name, f in (("f1", f1), ("f2", f2), ("f3", f3)):
    tops = []
    for x in (20, 27, 33, 39, 43, 47):
        t = None
        for y in range(h):
            if is_vis(f.get(x, y)):
                t = y
                break
        tops.append(t)
    print(name, "top rows at x=20,27,33,39,43,47:", tops, f.stats()['size'])

finish([f1, f2, f3])
