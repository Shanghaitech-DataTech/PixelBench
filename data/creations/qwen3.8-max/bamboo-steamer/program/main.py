import math

try:
    from pixelbench_api import new_canvas, view, save, finish
except Exception:
    pass

# ---------------- palette ----------------
OUT     = "#4A3320"   # dumpling outline / deep shadow
DOU_L   = "#FBF2DA"   # wrapper light
DOU_M   = "#E9D3A6"   # wrapper mid / pleats
DOU_S   = "#CDAE7C"   # wrapper shadow base
PINK    = "#E79C7E"   # filling dot
BAM_L   = "#D9B36A"   # bamboo light
BAM_M   = "#B98F4E"   # bamboo mid
BAM_D   = "#7A5628"   # bamboo dark
INTER   = "#5E4224"   # basket interior
STEAM   = "#EAF4F6"   # steam
STEAM2  = "#C2D8DC"   # steam shade

COLS = {'o': OUT, 'L': DOU_L, 'm': DOU_M, 'S': DOU_S, 'p': PINK, '.': None}

# ---------------- dumpling sprites ----------------
D1 = [  # round pleated dome 9x7
    "..ooooo..",
    ".oLLLLLo.",
    "oLmLLmLLo",
    "oLmLLmLLo",
    "oSSSSSSSo",
    ".oSSSSSo.",
    "..ooooo..",
]
D2 = [  # har-gow crescent with pleat bumps 9x5
    "..o.o.o..",
    ".oLLLLLo.",
    "oLmLLmLLo",
    "oSSSSSSSo",
    ".ooooooo.",
]
D3 = [  # open-top siu mai 8x5, filling band on top
    ".oooooo.",
    "oppgpppo",
    "oLLLLLLo",
    "oSSSSSSo",
    ".oooooo.",
]


def draw_map(cv, m, x0, y0):
    for j, row in enumerate(m):
        for i, ch in enumerate(row):
            col = COLS.get(ch)
            if col:
                cv.set(x0 + i, y0 + j, col)


def rot_ellipse(cv, cx, cy, rx, ry, ang_deg, colour):
    a = math.radians(ang_deg)
    ca, sa = math.cos(a), math.sin(a)
    x0 = int(math.floor(cx - rx - ry - 1))
    x1 = int(math.ceil(cx + rx + ry + 1))
    y0 = int(math.floor(cy - rx - ry - 1))
    y1 = int(math.ceil(cy + rx + ry + 1))
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            dx, dy = x - cx, y - cy
            ux = ca * dx + sa * dy
            uy = -sa * dx + ca * dy
            if (ux * ux) / (rx * rx) + (uy * uy) / (ry * ry) <= 1.0:
                cv.set(x, y, colour)


result = new_canvas(32, 32, background=None, name="bamboo_steamer")

# ---------------- steam (drawn first, behind nothing important) ----------------
w1 = [(6, 9), (5, 8), (5, 7), (6, 6), (6, 5), (5, 4)]
w2 = [(11, 8), (10, 7), (10, 6), (11, 5), (11, 4), (10, 3), (10, 2)]
w3 = [(16, 7), (15, 6), (15, 5), (16, 4), (16, 3)]
for px, py in w1 + w2 + w3:
    result.set(px, py, STEAM)
result.set(5, 3, STEAM2)
result.set(10, 8, STEAM2)
result.set(15, 7, STEAM2)

# ---------------- tilted lid, propped open at the right ----------------
ANG = 14
rot_ellipse(result, 22, 11.2, 9.6, 4.4, ANG, BAM_D)    # silhouette / edge
rot_ellipse(result, 22, 10.6, 9.0, 3.8, ANG, BAM_M)    # side rim thickness
rot_ellipse(result, 22, 9.6, 9.0, 3.6, ANG, BAM_L)     # top face
rot_ellipse(result, 22, 9.6, 6.2, 2.3, ANG, BAM_M)     # woven ring
rot_ellipse(result, 22, 9.6, 3.4, 1.2, ANG, BAM_L)     # inner ring
rot_ellipse(result, 22, 5.8, 1.8, 1.2, ANG, BAM_D)     # knob base bump
rot_ellipse(result, 22, 5.5, 1.1, 0.7, ANG, BAM_M)     # knob top

# ---------------- basket interior + back rim ----------------
result.rect(3, 12, 26, 1, BAM_M)
result.rect(3, 13, 26, 1, BAM_D)
result.rect(3, 14, 26, 5, INTER)

# ---------------- dumplings ----------------
draw_map(result, D2, 12, 12)   # back middle
draw_map(result, D1, 3, 13)    # front left
draw_map(result, D3, 21, 14)   # front right

# ---------------- basket front rim ----------------
result.rect(2, 18, 28, 1, BAM_L)
result.rect(1, 19, 30, 1, BAM_M)
result.rect(1, 20, 30, 1, BAM_D)

# ---------------- basket body with weave ----------------
result.rect(2, 21, 28, 6, BAM_M)
result.rect(2, 21, 1, 6, BAM_D)
result.rect(29, 21, 1, 6, BAM_D)
result.rect(2, 23, 28, 1, BAM_D)
result.rect(2, 25, 28, 1, BAM_D)
for x in (7, 15, 23):
    result.rect(x, 21, 1, 2, BAM_D)
for x in (4, 11, 18, 25):
    result.rect(x, 24, 1, 1, BAM_D)
for x in (7, 15, 23):
    result.rect(x, 26, 1, 1, BAM_D)
# light weave dashes
for x in (3, 9, 17, 25):
    result.rect(x, 22, 2, 1, BAM_L)
for x in (6, 13, 20, 27):
    result.rect(x, 24, 2, 1, BAM_L)

# ---------------- base ----------------
result.rect(3, 27, 26, 1, BAM_D)
result.rect(5, 28, 22, 1, BAM_D)

print(result.stats_text())
view(result, scale=12)
view(result)
save("bamboo_steamer", result)
finish(result)
