from pixelbench_api import *
import math

W, H = 128, 128
c = new_canvas(W, H, name="result")

# Palette
tire   = c.color((18, 18, 20), "tire")
black  = c.color((28, 28, 31), "black")
dark   = c.color((58, 58, 64), "darkgray")
mid    = c.color((104, 104, 110), "midgray")
silver = c.color((190, 190, 194), "silver")
silv_d = c.color((142, 142, 148), "silverdark")
hub    = c.color((162, 162, 168), "hubgray")
white  = c.color((242, 242, 242), "white")
red    = c.color((214, 44, 44), "red")

def thick_line(x0, y0, x1, y1, w, col):
    dx = x1 - x0
    dy = y1 - y0
    L = math.hypot(dx, dy) or 1.0
    px = -dy / L * w / 2.0
    py = dx / L * w / 2.0
    pts = [(x0 + px, y0 + py), (x1 + px, y1 + py),
           (x1 - px, y1 - py), (x0 - px, y0 - py)]
    c.poly(pts, col, fill=True)

# ---------------- Wheels ----------------
for cx in (30, 98):
    c.circle(cx, 104, 20, tire, fill=True)
    # spokes
    for k in range(8):
        a = k * math.pi / 4 + math.pi / 8
        c.line(cx, 104, int(round(cx + 13 * math.cos(a))),
               int(round(104 + 13 * math.sin(a))), white)
    # hub
    c.circle(cx, 104, 7, hub, fill=True)
    c.circle(cx, 104, 3, silv_d, fill=True)

# ---------------- Frame (silver tubular) ----------------
thick_line(92, 78, 66, 86, 4, silver)     # main spar
thick_line(66, 86, 58, 90, 4, silver)     # to swingarm pivot
thick_line(92, 80, 78, 96, 3, silv_d)     # down tube
thick_line(58, 88, 46, 60, 3, silv_d)     # subframe upper
thick_line(52, 90, 40, 56, 3, silv_d)     # subframe lower
thick_line(58, 92, 30, 102, 5, silver)    # swingarm

# ---------------- Exhaust ----------------
thick_line(56, 94, 42, 86, 4, silv_d)
c.ellipse(28, 80, 11, 5, silver, fill=True)

# ---------------- Engine cover ----------------
c.circle(66, 90, 12, silver, fill=True)
c.circle(66, 90, 7, silv_d, fill=True)
c.circle(66, 90, 2, mid, fill=True)

# ---------------- Main body: fairing + tank ----------------
fairing = [
    (120, 83), (113, 66), (104, 57), (92, 54), (70, 56),
    (58, 60), (58, 74), (70, 84), (104, 90), (112, 86),
]
c.poly(fairing, dark, fill=True)

# Belly pan (lower fairing)
belly = [(66, 88), (104, 92), (110, 100), (86, 104), (70, 102)]
c.poly(belly, dark, fill=True)

# ---------------- Seat / upswept tail (black) ----------------
tail = [
    (68, 62), (52, 58), (40, 50), (34, 46), (38, 56),
    (52, 66), (64, 66),
]
c.poly(tail, black, fill=True)

# Red tail light at the rearmost tip
c.poly([(36, 46), (29, 50), (34, 53)], red, fill=True)

# ---------------- Front fender ----------------
fender = [(82, 88), (88, 77), (106, 77), (114, 88), (112, 92), (84, 92)]
c.poly(fender, dark, fill=True)

# ---------------- Front fork ----------------
thick_line(97, 104, 91, 74, 4, silver)
thick_line(99, 104, 93, 76, 2, silv_d)

# ---------------- Windscreen (small black, tilted) ----------------
c.poly([(108, 60), (100, 48), (92, 51), (96, 62)], black, fill=True)

# ---------------- Red accent stripe on fairing ----------------
thick_line(112, 64, 90, 54, 2, red)

# ---------------- Finish ----------------
print(c.stats_text())
finish(c)
