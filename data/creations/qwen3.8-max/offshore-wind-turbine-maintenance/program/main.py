"""Offshore wind turbine maintenance platform - 64x64 pixel art.

Scale reference: technician = 12 px = 1.8 m  ->  1 px ~ 0.15 m
  railing 7 px  ~ 1.05 m   (correct guard-rail height)
  tower  19 px  ~ 2.9 m    (transition piece diameter)
  deck   20 px above the waterline ~ 3 m freeboard
Horizon at y=30 = camera eye level; distant turbines stand on it.
"""
import math

W = H = 64
c = new_canvas(W, H, name="offshore_wind")

# ------------------------------------------------------------------ palette --
SKY = ["#1e3d5c", "#2c5578", "#3e6f92", "#568ca9", "#7dadc3", "#a4c9da"]
CL_L, CL_M, CL_D = "#eaf2f6", "#c3d7e1", "#93b1c2"
GULL = "#d8e7ee"

SEA = ["#4a86a4", "#3a7595", "#2e6685", "#245876", "#1c4a67", "#153d57", "#0f3248"]
WMID, WLT, FOAM = "#6ba0b6", "#9ac8d8", "#e2f2f7"
HORIZON = "#b6d3df"

DST_A, DST_AD = "#8fb0c1", "#7396ab"
DST_B, DST_BD = "#7fa2b5", "#66899e"

ST = ("#2e3c46", "#eff5f7", "#c9d6db", "#a0aeb5", "#75828a", "#4f5c64")   # steel
YL = ("#6b4c0d", "#ffeda6", "#f7cd55", "#d9a82f", "#ac801d", "#8a6514")   # transition
SP = ("#0c141a", "#4a5961", "#38454c", "#29343a", "#1d262b", "#111a20")   # splash zone

DECK_T, DECK_E, DECK_U, DECK_S = "#c9d4d8", "#93a1a8", "#5e6b72", "#3b464c"
SAFETY = "#e3b53e"
RAIL_L, RAIL_M, RAIL_D = "#dbe4e8", "#a8b5bb", "#717e85"
BR_L, BR_D = "#8d9aa1", "#5a676e"
GLASS = "#7fa8bb"
LAMP = "#e8564a"
OUT = "#0e1a24"

P = {
    "h": "#e8a92a", "H": "#ffd766",          # hard hat
    "F": "#cf9a72",                          # face
    "V": "#f2682a", "v": "#c94f1c", "R": "#eef4f6",  # hi-vis vest + tape
    "A": "#dd5a24",                          # sleeves
    "B": "#2b343b",                          # harness
    "T": "#3d5570", "t": "#2b3c52",          # trousers
    "O": "#171d23",                          # boots
    "G": "#d8dfe2",                          # gloves
}


# ------------------------------------------------------------------ helpers --
def hsh(x, y, s):
    v = (x * 73856093) ^ (y * 19349663) ^ (s * 83492791)
    v = (v * 2654435761) & 0xFFFFFFFF
    v ^= v >> 15
    v = (v * 2246822519) & 0xFFFFFFFF
    v ^= v >> 13
    return (v & 0xFFFFFF) / 16777215.0


def band(y0, y1, col, x0=0, x1=W - 1):
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, col)


def checker(y, ca, cb, x0=0, x1=W - 1):
    for x in range(x0, x1 + 1):
        c.set(x, y, ca if x % 2 == 0 else cb)


def tL(y):
    return int(round(38 - 4 * (y - 17) / 37.0))


def tR(y):
    return int(round(52 + 4 * (y - 17) / 37.0))


def steel(y, pal, L, R):
    w = R - L + 1
    e, hi, ml, md, sh, dk = pal
    for i in range(w):
        x = L + i
        if not 0 <= x < W:
            continue
        f = i / float(w - 1) if w > 1 else 0.0
        if i == 0 or i == w - 1:
            col = e
        elif f < 0.17:
            col = hi
        elif f < 0.45:
            col = ml
        elif f < 0.71:
            col = md
        elif f < 0.90:
            col = sh
        else:
            col = dk
        c.set(x, y, col)


def blade(cx, cy, ang, L, wr, col, hi):
    a = math.radians(ang)
    dx, dy = math.sin(a), -math.cos(a)
    px, py = math.cos(a), math.sin(a)
    tx, ty = cx + dx * L, cy + dy * L
    q = [(cx + px * wr, cy + py * wr),
         (tx + px * 0.25, ty + py * 0.25),
         (tx - px * 0.25, ty - py * 0.25),
         (cx - px * wr, cy - py * wr)]
    c.poly([(int(round(u)), int(round(v))) for u, v in q], col)
    mx, my = cx + dx * L * 0.5, cy + dy * L * 0.5
    c.line(cx, cy, int(round(mx)), int(round(my)), hi)


# ---------------------------------------------------------------------- sky --
band(0, 3, SKY[0]);  checker(4, SKY[0], SKY[1])
band(5, 9, SKY[1]);  checker(10, SKY[1], SKY[2])
band(11, 15, SKY[2]); checker(16, SKY[2], SKY[3])
band(17, 21, SKY[3]); checker(22, SKY[3], SKY[4])
band(23, 27, SKY[4]); checker(28, SKY[4], SKY[5])
band(29, 29, SKY[5])


def cloud(x0, y0, rows):
    for dx, dy, w in rows:
        c.rect(x0 + dx, y0 + dy, w, 1, CL_L)
    for i, (dx, dy, w) in enumerate(rows):
        if i == len(rows) - 1:
            c.rect(x0 + dx + 1, y0 + dy, max(1, w - 2), 1, CL_M)


cloud(0, 3, [(3, 0, 5), (1, 1, 9), (0, 2, 12)])
c.rect(1, 5, 10, 1, CL_D)
cloud(21, 1, [(2, 0, 4), (0, 1, 9), (0, 2, 7)])
c.rect(22, 3, 6, 1, CL_D)
cloud(26, 16, [(2, 0, 6), (0, 1, 10), (0, 2, 8)])
c.rect(27, 18, 7, 1, CL_D)
cloud(2, 19, [(2, 0, 5), (0, 1, 9), (0, 2, 7)])
c.rect(3, 21, 6, 1, CL_D)
cloud(52, 21, [(1, 0, 5), (0, 1, 8), (0, 2, 6)])
c.rect(53, 23, 5, 1, CL_D)
cloud(14, 8, [(1, 0, 4), (0, 1, 7)])

for gx, gy in [(24, 7), (28, 10)]:
    c.set(gx, gy, GULL); c.set(gx + 1, gy - 1, GULL)
    c.set(gx + 2, gy, GULL); c.set(gx + 3, gy - 1, GULL)

# --------------------------------------------------------- distant turbines --
def dist_turbine(cx, hub_y, L, col, cold, th):
    for y in range(hub_y, 31):
        c.set(cx, y, col)
        if y > hub_y + 4:
            c.set(cx - 1, y, col)
    c.rect(cx - 1, hub_y - 1, 3, 2, col)
    c.set(cx + 2, hub_y - 1, cold)
    for k in range(3):
        a = math.radians(th + 120 * k)
        c.line(cx, hub_y, int(round(cx + L * math.sin(a))),
               int(round(hub_y - L * math.cos(a))), col)
    c.set(cx, hub_y, cold)


dist_turbine(7, 20, 6, DST_A, DST_AD, 0)
dist_turbine(59, 23, 5, DST_B, DST_BD, 0)

# --------------------------------------------------------------------- sea --
band(30, 30, HORIZON)
band(31, 31, SEA[0]); checker(32, SEA[0], SEA[1])
band(33, 36, SEA[1]); checker(37, SEA[1], SEA[2])
band(38, 42, SEA[2]); checker(43, SEA[2], SEA[3])
band(44, 48, SEA[3]); checker(49, SEA[3], SEA[4])
band(50, 54, SEA[4]); checker(55, SEA[4], SEA[5])
band(56, 59, SEA[5]); checker(60, SEA[5], SEA[6])
band(61, 63, SEA[6])


def waves(y0, y1):
    for y in range(y0, y1 + 1):
        d = (y - 30) / 33.0
        dl = 1 + int(d * 7)
        per = 3 + int(d * 9)
        x = -per + int(hsh(0, y, 3) * per)
        while x < W + per:
            if hsh(x, y, 5) > 0.40:
                ln = max(1, int(dl * (0.4 + hsh(x, y, 9))))
                r = hsh(x, y, 13)
                col = FOAM if r > 0.93 else (WLT if r > 0.66 else WMID)
                for i in range(ln):
                    xx = x + i
                    if 0 <= xx < W:
                        c.set(xx, y, col)
            x += per


waves(31, 42)

# ------------------------------------------------------------- main turbine --
# nacelle
c.rect(38, 10, 15, 7, ST[4])
c.rect(38, 10, 15, 1, ST[2])
c.rect(38, 11, 15, 1, ST[3])
c.rect(38, 15, 15, 2, ST[5])
c.rect(38, 10, 1, 7, ST[0])
c.rect(52, 10, 1, 7, ST[5])
c.rect(41, 12, 3, 2, GLASS)
c.rect(47, 7, 1, 3, ST[4])
c.set(47, 6, LAMP)

# rotor (light blades read against the darker nacelle)
blade(45, 13, 120, 11, 1.3, ST[5], ST[4])
blade(45, 13, 240, 11, 1.3, ST[5], ST[4])
blade(45, 13, 0, 11, 1.3, ST[2], ST[1])
c.circle(45, 13, 1, ST[1])
c.set(45, 13, ST[4])

# tower / transition piece / splash zone
for y in range(17, 55):
    L, R = tL(y), tR(y)
    if y <= 35:
        steel(y, ST, L, R)
    elif y <= 48:
        steel(y, YL, L - 1, R + 1)
    else:
        steel(y, SP, L - 1, R + 1)

# transition-piece top lip
L, R = tL(36), tR(36)
c.line(L - 2, 36, R + 2, 36, YL[4])
c.line(L - 2, 37, R + 2, 37, YL[1])
c.line(L - 1, 38, R + 1, 38, YL[3])

# flange rings on the steel tower
for fy in (22, 29):
    L, R = tL(fy), tR(fy)
    for x in range(L + 1, R):
        c.set(x, fy, ST[4])
        c.set(x, fy + 1, ST[1])
    for x in range(L + 2, R, 4):
        c.set(x, fy, ST[5])

# tower door ~ person height (scale cue) + hazard stripe + internal ladder
L = tL(24)
dx = L + 2
for i, x in enumerate(range(dx, dx + 7)):
    c.set(x, 22, SAFETY if i % 2 == 0 else ST[0])
c.rect(dx, 23, 7, 12, "#2c3941")
c.rect(dx, 23, 7, 1, RAIL_M)
c.line(dx, 23, dx, 34, RAIL_M)
c.line(dx + 6, 23, dx + 6, 34, ST[5])
c.rect(dx + 2, 25, 2, 2, GLASS)
c.set(dx + 5, 30, RAIL_L)
c.line(dx + 1, 34, dx + 5, 34, "#202c34")

# J-tube cable down the transition piece
for y in range(39, 49):
    c.set(tL(y), y, YL[5])
    c.set(tL(y) + 1, y, SP[2])

# ---------------------------------------------------------------- platform --
# under-deck bracing (right of the ladder, tying the deck to the tower)
c.line(28, 37, 40, 49, BR_D)
c.line(29, 37, 41, 49, BR_L)
c.line(35, 37, 45, 45, BR_D)
c.line(36, 37, 46, 45, BR_L)
c.line(28, 37, 28, 44, BR_D)
c.line(29, 37, 29, 44, BR_L)
c.line(28, 44, 42, 44, BR_D)
c.line(28, 43, 42, 43, BR_L)

# deck slab
band(33, 33, DECK_T, 14, 42)
for x in range(14, 43, 2):
    c.set(x, 33, "#e6ecef")
band(34, 34, DECK_E, 14, 42)
for x in range(14, 43, 4):
    c.set(x, 34, SAFETY)
band(35, 35, DECK_U, 14, 42)
band(36, 36, DECK_S, 15, 41)

# deck equipment: tool crate + cable reel (behind the railing)
c.rect(31, 28, 6, 5, "#7e8b92")
c.rect(31, 28, 6, 1, "#aab6bc")
c.rect(31, 32, 6, 1, DECK_U)
c.rect(33, 29, 2, 3, SAFETY)
c.rect(39, 29, 3, 4, "#6d7a81")
c.rect(39, 29, 3, 1, BR_L)

# railings (right of the ladder opening)
band(26, 26, RAIL_L, 28, 42)
band(27, 27, RAIL_M, 28, 42)
band(30, 30, RAIL_M, 28, 42)
band(32, 32, RAIL_D, 28, 42)
for px in (28, 33, 38, 42):
    c.line(px, 27, px, 32, RAIL_M)
    c.set(px, 26, RAIL_L)
    c.set(px, 27, RAIL_L)

# grab rails flanking the ladder opening
c.line(15, 25, 15, 33, RAIL_L)
c.line(27, 25, 27, 33, RAIL_L)
c.set(15, 25, RAIL_D); c.set(27, 25, RAIL_D)
c.line(15, 25, 27, 25, RAIL_M)

# --------------------------------------------------- boat-landing ladder ----
c.line(16, 32, 16, 53, RAIL_L)
c.line(26, 32, 26, 53, RAIL_D)
for ry in range(34, 54, 3):
    c.line(17, ry, 25, ry, RAIL_M)
    c.set(17, ry, "#d3dce0")
    c.set(25, ry, RAIL_D)
c.line(16, 33, 26, 33, BR_L)

# --------------------------------------------------------------- technician --
SPR = [
    "G.........G",
    ".A.hHHHh.A.",
    ".AAhhhhhAA.",
    "..AFFFFFA..",
    "..AVVVVvA..",
    "..ARRRRRA..",
    "...VVVvv...",
    "...BBBBB...",
    "...TTTTT...",
    "...OO.TT...",
    "......TT...",
    "......tt...",
    "......OO...",
]
X0, Y0 = 16, 37
solid = set()
for j, row in enumerate(SPR):
    for i, ch in enumerate(row):
        if ch != ".":
            solid.add((X0 + i, Y0 + j))
for (x, y) in sorted(solid):
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1),
                   (-1, -1), (1, -1), (-1, 1), (1, 1)):
        if (x + dx, y + dy) not in solid:
            c.set(x + dx, y + dy, OUT)
for j, row in enumerate(SPR):
    for i, ch in enumerate(row):
        if ch != ".":
            c.set(X0 + i, Y0 + j, P[ch])
# lanyard from the harness to a fall-arrest slider on the ladder rail
c.line(24, 44, 26, 43, "#2b343b")
c.set(26, 42, "#98a4aa")
c.set(26, 43, SAFETY)

# ------------------------------------- base foam, reflection, near waves ----
Lb, Rb = tL(53), tR(53)
for x in range(Lb - 5, min(W, Rb + 5)):
    if 0 <= x < W:
        c.set(x, 53, FOAM)
for x in range(Lb - 4, min(W, Rb + 4)):
    if 0 <= x < W and hsh(x, 2, 17) > 0.28:
        c.set(x, 54, WLT)
for x in range(Lb - 6, Lb):
    if 0 <= x < W:
        c.set(x, 52, FOAM)
for x in range(Rb, min(W, Rb + 5)):
    if 0 <= x < W:
        c.set(x, 52, WLT)

for y in range(55, 62):
    for x in range(34, 58):
        if 0 <= x < W:
            r = hsh(x, y, 19)
            if r > 0.74:
                c.set(x, y, SEA[6])
            elif r > 0.62:
                c.set(x, y, "#1d4763")

for x in range(14, 29):
    if hsh(x, 1, 29) > 0.38:
        c.set(x, 52, FOAM)
        c.set(x, 53, WLT)
c.line(15, 54, 27, 54, WMID)

waves(43, 63)

for x, y in [(3, 50), (11, 57), (24, 47), (32, 61), (47, 55), (56, 60),
             (7, 45), (29, 44), (0, 63), (38, 51), (18, 58), (53, 48), (1, 41)]:
    c.line(x, y, x + 3, y, FOAM)

print(c.stats_text())
view(c)
save("offshore_wind", c, indexed=True)
finish(c)
