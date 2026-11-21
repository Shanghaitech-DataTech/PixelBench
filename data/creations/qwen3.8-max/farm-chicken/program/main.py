from pixelbench_api import *

W = H = 32
c = new_canvas(W, H, name="chicken")

# ---------------- warm muted palette ----------------
DARK     = "#4b3a2e"   # soft warm outline
CREAM    = "#f3e5cb"   # body base
CREAM_HI = "#fdf7ea"   # rim light
CREAM_SH = "#ddc6a2"   # belly shadow
CREAM_DK = "#c2a880"   # deep shadow
TAIL     = "#e9d8b8"   # tail feathers
WING     = "#e7d5b2"   # wing base
WING_SH  = "#cdb289"   # wing feather lines
RED      = "#c9584b"   # comb / wattle
RED_DK   = "#a5403a"
AMBER    = "#e3a551"   # beak / legs
AMBER_DK = "#bf7f36"
EYE      = "#3a2a21"
GLINT    = "#fffaf0"

# ---------------- helpers ----------------
def dpoly(pts, colour):
    """1px dilation of a polygon -> dark outline under the fill."""
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            c.poly([(x + dx, y + dy) for (x, y) in pts], colour, fill=True)

def dell(cx, cy, rx, ry, colour):
    c.ellipse(cx, cy, rx + 1, ry + 1, colour, fill=True)

def dcirc(cx, cy, r, colour):
    c.circle(cx, cy, r + 1, colour, fill=True)

def runs(xs):
    """group a sorted list of ints into contiguous runs"""
    out = []
    for v in xs:
        if out and v == out[-1][-1] + 1:
            out[-1].append(v)
        else:
            out.append([v])
    return out

# ---------------- geometry ----------------
BX, BY, BRX, BRY = 14, 20, 9, 7          # body
NX, NY, NRX, NRY = 19, 15, 5, 4          # neck bridge
HX, HY, HR      = 22, 11, 5              # head

F1 = [(9, 15), (6, 12), (3, 9), (1, 10), (2, 13), (5, 17), (8, 19)]   # top tail feather
F2 = [(9, 18), (5, 15), (2, 13), (1, 15), (3, 18), (6, 21), (9, 22)]  # mid
F3 = [(9, 21), (5, 20), (2, 19), (1, 21), (3, 24), (7, 25), (9, 24)]  # low

BEAK = [(27, 10), (30, 11), (30, 12), (27, 13)]

WINGP = [(8, 19), (10, 18), (13, 18), (16, 19), (18, 21), (17, 23),
         (15, 25), (12, 25), (9, 24), (8, 22)]

COMB_PX = [(x, 5) for x in range(19, 27)] + \
          [(19, 4), (20, 4), (22, 4), (23, 4), (25, 4), (26, 4),
           (22, 3), (23, 3)] + \
          [(x, 6) for x in range(20, 26)] + \
          [(x, 7) for x in range(21, 25)]
WATTLE_PX = [(26, 15), (27, 15), (26, 16), (27, 16)]

LEGS = [(12, AMBER_DK), (17, AMBER)]     # (x, colour) back leg darker

# ================= PHASE 1 : dark silhouette =================
dpoly(F1, DARK); dpoly(F2, DARK); dpoly(F3, DARK)
dell(BX, BY, BRX, BRY, DARK)
dell(NX, NY, NRX, NRY, DARK)
dcirc(HX, HY, HR, DARK)
for (px, py) in COMB_PX:
    c.rect(px - 1, py - 1, 3, 3, DARK, fill=True)
for (px, py) in WATTLE_PX:
    c.rect(px - 1, py - 1, 3, 3, DARK, fill=True)
dpoly(BEAK, DARK)

# ================= PHASE 2 : flat fills =================
c.poly(F3, TAIL, fill=True)
c.poly(F2, TAIL, fill=True)
c.poly(F1, TAIL, fill=True)

c.ellipse(BX, BY, BRX, BRY, CREAM, fill=True)
c.ellipse(NX, NY, NRX, NRY, CREAM, fill=True)
c.circle(HX, HY, HR, CREAM, fill=True)

cream_i = c.color(CREAM)
head_mask = set((x, y) for x in range(W) for y in range(H) if c.get(x, y) == cream_i)

# comb
for (px, py) in COMB_PX:
    c.set(px, py, RED)
# wattle
for (px, py) in WATTLE_PX:
    c.set(px, py, RED)
# beak
c.poly(BEAK, AMBER, fill=True)

red_i = c.color(RED)
# dark-red seam where comb meets head
for x in range(W):
    seam = [y for y in range(H) if (x, y) in head_mask and c.get(x, y) == red_i]
    if seam:
        c.set(x, max(seam), RED_DK)

# beak detail
c.set(27, 12, AMBER_DK); c.set(28, 12, AMBER_DK); c.set(29, 12, AMBER_DK)
c.set(27, 13, AMBER_DK)
# wattle shading
c.set(26, 16, RED_DK); c.set(27, 16, RED_DK)

# ================= PHASE 3 : body shading =================
sh_runs = lambda mask_idx: None
for x in range(W):
    col = [y for y in range(H) if c.get(x, y) == cream_i]
    for run in runs(col):
        n = len(run)
        if n >= 1:
            c.set(x, run[0], CREAM_HI)                 # rim light on top
        if n >= 2:
            c.set(x, run[-1], CREAM_SH)                # belly shadow
        if n >= 3:
            c.set(x, run[-2], CREAM_SH)
        if n >= 6:
            c.set(x, run[-3], CREAM_SH)

# right-edge rim shadow (light comes from the left)
for y in range(H):
    row = [x for x in range(W) if c.get(x, y) == cream_i]
    for run in runs(row):
        if len(run) >= 4:
            c.set(run[-1], y, CREAM_SH)

# ================= PHASE 4 : tail over body, then wing =================
for P in (F1, F2, F3):
    dpoly(P, DARK)
c.poly(F3, TAIL, fill=True)
c.poly(F2, TAIL, fill=True)
c.poly(F1, TAIL, fill=True)
c.line(2, 12, 8, 18, DARK)
c.line(2, 15, 8, 21, DARK)

dpoly(WINGP, DARK)
c.poly(WINGP, WING, fill=True)
c.line(10, 21, 11, 23, WING_SH)
c.line(13, 21, 14, 24, WING_SH)
c.line(16, 21, 16, 23, WING_SH)
c.line(9, 20, 12, 19, CREAM_HI)

# ================= PHASE 5 : legs & feet =================
for (lx, lcol) in LEGS:
    leg_px = [(lx, y) for y in range(26, 30)] + \
             [(lx - 1, 30), (lx, 30), (lx + 1, 30), (lx + 2, 30)]
    for (px, py) in leg_px:
        c.rect(px - 1, py - 1, 3, 3, DARK, fill=True)
    for (px, py) in leg_px:
        c.set(px, py, lcol)
    c.set(lx + 2, 30, AMBER_DK)

# ================= PHASE 6 : face =================
c.set(23, 9, EYE); c.set(24, 9, EYE)
c.set(23, 10, EYE); c.set(24, 10, EYE)
c.set(23, 9, GLINT)
# cheek blush
c.set(23, 13, CREAM_SH)

# tail feather separation lines
c.line(2, 12, 8, 18, DARK)
c.line(2, 15, 8, 21, DARK)

save("chicken", c, indexed=True)
print(c.stats_text())
print(view(c, scale=16))
finish(c)
