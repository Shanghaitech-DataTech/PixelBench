import math
from pixelbench_api import *

c = new_canvas(64, 64, None, "void-eye")

# ---------------- palette (22 colours) ----------------
OUTLINE  = c.color("#100616", "outline")
FLESH    = c.color("#4d2058", "flesh")
FLESH_D  = c.color("#2e1138", "flesh_dark")
FLESH_L  = c.color("#7a3589", "flesh_light")
SCLERA   = c.color("#e6def4", "sclera")
SCLERA_M = c.color("#c8bbdf", "sclera_mid")
SCLERA_D = c.color("#a896c7", "sclera_deep")
VEIN     = c.color("#b34a66", "vein")
IRIS1 = c.color("#1d0c38", "iris_rim")
IRIS2 = c.color("#2a1458", "iris_2")
IRIS3 = c.color("#3a1c7a", "iris_3")
IRIS4 = c.color("#4c269e", "iris_4")
IRIS5 = c.color("#6031c2", "iris_5")
PUPIL  = c.color("#0a0414", "pupil")
PGLOW1 = c.color("#2c1a60", "pupil_glow_dim")
PGLOW2 = c.color("#8257e0", "pupil_glow")
PGLOW3 = c.color("#d8c8ff", "pupil_core")
GLINT  = c.color("#f7f2ff", "glint")
SH1 = c.color("#0a051238", "shadow_far")
SH2 = c.color("#0a051266", "shadow_mid")
SH3 = c.color("#0a0512a0", "shadow_near")

BX, BY = 32, 24            # body sphere
BR2, BO2 = 361, 400
EX, EY = 32, 27            # eyeball
ER2, EO2 = 196, 225
IX, IY = 32, 29            # iris / pupil


def rnd(v):
    return int(math.floor(v + 0.5))


def put(x, y, col):
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, col)


def disc(cx, cy, r2, col, lo2=None, a0=None, a1=None):
    r = int(math.sqrt(r2)) + 1
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            d2 = (x - cx) ** 2 + (y - cy) ** 2
            if d2 > r2 or (lo2 is not None and d2 <= lo2):
                continue
            if a0 is not None:
                a = math.degrees(math.atan2(y - cy, x - cx)) % 360.0
                if a < a0:
                    a += 360.0
                hi = a1 if a1 >= a0 else a1 + 360.0
                if not (a0 <= a <= hi):
                    continue
            put(x, y, col)


def line(x0, y0, x1, y1, col, clip=None):
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        if 0 <= x < 64 and 0 <= y < 64 and (clip is None or clip(x, y)):
            c.set(x, y, col)
        if x == x1 and y == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


def lid_y(x):
    return 23 - abs(x - 32) * 0.5


# ============ 1. soft hovering shadow ============
c.ellipse(32, 59, 17, 1, SH1)
c.ellipse(32, 59, 12, 1, SH2)
c.ellipse(32, 59, 6, 1, SH3)

# ============ 2. short tentacles (clean tapered runs) ============
def tent_rows(ctrl):
    rows = {}
    for i in range(len(ctrl) - 1):
        y0, c0, w0 = ctrl[i]
        y1, c1, w1 = ctrl[i + 1]
        n = y1 - y0
        for j in range(n + 1):
            t = j / float(n)
            rows[y0 + j] = (c0 + (c1 - c0) * t, w0 + (w1 - w0) * t)
    return rows


TENTS = [
    [(33, 20, 8), (37, 17, 7), (41, 15, 6), (45, 13, 5), (48, 12, 4), (50, 11, 3)],
    [(40, 26, 6), (44, 24, 5), (47, 23, 4), (50, 22, 3), (52, 21, 2)],
    [(42, 32, 6), (45, 32, 5), (48, 33, 4), (50, 33, 3), (52, 33, 2)],
    [(40, 38, 6), (44, 40, 5), (47, 41, 4), (50, 42, 3), (52, 43, 2)],
    [(33, 44, 8), (37, 47, 7), (41, 49, 6), (45, 51, 5), (48, 52, 4), (50, 53, 3)],
]
TROWS = [tent_rows(t) for t in TENTS]
for rows in TROWS:
    for y in sorted(rows):
        cx, w = rows[y]
        wi = max(2, int(math.floor(w + 0.5)))
        xL = rnd(cx - wi / 2.0)
        put(xL - 1, y, OUTLINE)
        put(xL + wi, y, OUTLINE)
        for x in range(xL, xL + wi):
            put(x, y, FLESH)
        if wi >= 4:
            put(xL, y, FLESH_L)
            put(xL + wi - 1, y, FLESH_D)
        elif wi == 3:
            put(xL, y, FLESH_L)
        elif wi == 2:
            put(xL + 1, y, FLESH_D)
for rows in TROWS:                      # close each tip
    ys = sorted(rows)
    cx, w = rows[ys[-1]]
    wi = max(2, int(math.floor(w + 0.5)))
    xL = rnd(cx - wi / 2.0)
    for x in range(xL - 1, xL + wi + 1):
        put(x, ys[-1] + 1, OUTLINE)

# ============ 3. body sphere ============
disc(BX, BY, BO2, OUTLINE, lo2=BR2)
disc(BX, BY, BR2, FLESH)
disc(BX, BY, BR2, FLESH_L, lo2=1, a0=160, a1=275)   # lit upper-left
disc(BX, BY, BR2, FLESH_D, lo2=1, a0=340, a1=115)   # shadowed right/bottom
if c.get(32, 44) == OUTLINE and c.get(32, 45) is not None:
    c.set(32, 44, FLESH)                # body tip must not hole the tentacle

# ============ 4. eyeball ============
disc(EX, EY, EO2, OUTLINE, lo2=ER2)
disc(EX, EY, ER2, SCLERA)
disc(EX, EY, ER2, SCLERA_M, lo2=121, a0=15, a1=165)
disc(EX, EY, ER2, SCLERA_D, lo2=169, a0=40, a1=140)

line(19, 26, 20, 29, VEIN)
line(19, 31, 20, 34, VEIN)
line(45, 26, 44, 29, VEIN)
line(45, 31, 44, 34, VEIN)
line(29, 40, 33, 40, VEIN)

# ============ 5. deep purple iris ============
disc(IX, IY, 100, IRIS1)
disc(IX, IY, 81, IRIS2)
disc(IX, IY, 64, IRIS3)
disc(IX, IY, 49, IRIS4)
disc(IX, IY, 36, IRIS5)
for k in range(12):                     # radial striations
    a = math.radians(15 + k * 30)
    ca, sa = math.cos(a), math.sin(a)
    line(rnd(IX + 6.5 * ca), rnd(IY + 6.5 * sa),
         rnd(IX + 9.8 * ca), rnd(IY + 9.8 * sa), IRIS1,
         clip=lambda px, py: (px - IX) ** 2 + (py - IY) ** 2 <= 100)

# ============ 6. faintly glowing pupil ============
disc(IX, IY, 32, PUPIL)
disc(IX, IY, 15, PGLOW1)
disc(IX, IY, 4, PGLOW2)
put(IX, IY, PGLOW3)
put(27, 25, GLINT)
put(28, 25, GLINT)

# ============ 7. heavy hooded lid (angry V) ============
for y in range(64):
    for x in range(64):
        d2 = (x - BX) ** 2 + (y - BY) ** 2
        if d2 > BR2:
            continue
        yv = rnd(lid_y(x))
        if y > yv:
            continue
        if y == yv:
            col = OUTLINE                    # crease
        elif y >= yv - 2:
            col = FLESH_L                    # margin lit by the eye
        elif y >= yv - 5:
            col = FLESH_D                    # fold
        else:
            a = math.degrees(math.atan2(y - BY, x - BX)) % 360.0
            if 160 <= a <= 275:
                col = FLESH_L
            elif a >= 340 or a <= 115:
                col = FLESH_D
            else:
                col = FLESH
        put(x, y, col)

# shadow the lid casts onto the sclera
for x in range(64):
    yv = rnd(lid_y(x))
    for dy in (1, 2):
        i = c.get(x, yv + dy)
        if i in (SCLERA, SCLERA_M):
            c.set(x, yv + dy, SCLERA_D)

# ---------------- inspection ----------------
_LET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


print(c.stats_text())


def dump(x0, y0, x1, y1, title=""):
    idxs = [p["index"] for p in c.palette() if p["index"] != 0]
    m = {i: _LET[k] for k, i in enumerate(idxs)}
    print(f"--- {title} x{x0}-{x1} y{y0}-{y1} ---")
    print("     " + "".join(str(x // 10 % 10) if x % 5 == 0 else " " for x in range(x0, x1 + 1)))
    print("     " + "".join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = ""
        for x in range(x0, x1 + 1):
            i = c.get(x, y)
            row += "." if i is None or i < 0 else m.get(i, "?")
        print(f"{y:3d}  {row}")
    print("  " + ", ".join(f"{_LET[k]}={c.color_name(i)}" for k, i in enumerate(idxs)))


dump(0, 0, 63, 63, "FULL")

print("\n-- bottom-centre junction, named colours --")
for y in range(40, 48):
    print(f"y{y:02d}: " + "  ".join(
        f"x{x}:{(c.color_name(c.get(x, y)) or 'trans')[:10]}"
        for x in range(28, 38)))




finish(c)
