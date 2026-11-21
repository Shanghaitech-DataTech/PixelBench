try:
    from pixelbench_api import new_canvas, view, save, finish
except Exception:
    pass

OUT = "#4A3320"
DOU_L = "#FBF2DA"
DOU_M = "#E9D3A6"
DOU_S = "#CDAE7C"
PINK = "#E79C7E"
GREEN = "#8FA95C"

COLS = {'o': OUT, 'L': DOU_L, 'm': DOU_M, 'S': DOU_S, 'p': PINK, 'g': GREEN, '.': None}

# F: round dome, vertical pleat ridges
F = [
    "..ooooo..",
    ".oLLLLLLo",
    "oLmLLmLLo",
    "oLmLLmLLo",
    "oSSSSSSSo",
    ".oSSSSSo.",
    "..ooooo..",
]
# G: har-gow crescent, pleats on top edge
G = [
    ".oooooo..",
    "oLmLmLmLo",
    "oLLLLLLLo",
    "oSSSSSSSo",
    ".ooooooo.",
]
# H: siu mai open-top cup
H = [
    ".oooooo.",
    "oLpLLpLo",
    "oLLLLLLo",
    "oSSSSSSo",
    "oooooooo",
]
# I: wide dome, pleat bumps + side shading + base shadow
I = [
    ".oo.oo.oo.",
    "oLLLLLLLLo",
    "oLmLLmLLmo",
    "oLLLLLLLLo",
    "oSSSSSSSSo",
    ".oooooooo.",
]
# J: round dome with highlight + pleat dots + shaded base
J = [
    "..ooooo..",
    ".oLLLLLo.",
    "oLLmLmLLo",
    "oLLLLLLSo",
    "oSSSSSSSo",
    ".ooooooo.",
]


def draw_map(cv, m, x0, y0):
    for j, row in enumerate(m):
        for i, ch in enumerate(row):
            col = COLS.get(ch)
            if col:
                cv.set(x0 + i, y0 + j, col)


t = new_canvas(32, 20, background="#3A4A5A", name="dumptest2")
draw_map(t, F, 0, 0)
draw_map(t, G, 10, 0)
draw_map(t, H, 21, 0)
draw_map(t, I, 0, 9)
draw_map(t, J, 12, 9)
print(t.stats_text())
p = view(t, scale=16)
print(p)
