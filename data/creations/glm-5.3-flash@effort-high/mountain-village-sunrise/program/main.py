# Mountain Village at Sunrise — 128x128 pixel art
c = new_canvas(128, 128, background="#221d40", name="village")

HORIZON = 80

# ---------- SKY GRADIENT ----------
bands = [
    (0,  "#221d40"),
    (12, "#322a52"),
    (24, "#4a3260"),
    (34, "#6b3a62"),
    (44, "#93475e"),
    (54, "#bd5e54"),
    (62, "#dc7d55"),
    (70, "#efa25e"),
    (76, "#f6c276"),
]
ys = [b[0] for b in bands] + [HORIZON]
for i, (y0, hexv) in enumerate(bands):
    c.rect(0, y0, 128, ys[i + 1] - y0, hexv)
for i in range(len(bands) - 1):
    yb = ys[i + 1]
    c.dither(0, yb - 2, 128, 4, [bands[i][1], bands[i + 1][1]])

# ---------- SUN (focal point, rising in the mountain notch) ----------
SX, SY = 64, 66
c.circle(SX, SY, 14, "#d98a5f")
c.circle(SX, SY, 10, "#efa96a")
c.circle(SX, SY, 7,  "#f9cd82")
c.circle(SX, SY, 5,  "#ffe9ad")
c.circle(SX, SY, 3,  "#fff6d6")

# ---------- BIRDS ----------
for bx, by in [(26, 26), (34, 31), (90, 22), (98, 27)]:
    c.line(bx - 2, by - 1, bx, by, "#2a2444")
    c.line(bx, by, bx + 2, by - 1, "#2a2444")

# ---------- DISTANT MOUNTAINS (hazy, lightest) ----------
far = [(0, 58), (14, 44), (28, 56), (44, 46), (58, 60), (64, 72), (70, 60),
       (84, 48), (100, 58), (114, 46), (127, 56), (127, HORIZON), (0, HORIZON)]
c.poly(far, "#8a6a8e")
# sun-facing slope highlights
c.line(44, 46, 58, 60, "#a585a6")
c.line(84, 48, 70, 60, "#a585a6")

# ---------- MID MOUNTAINS (darker, closer) ----------
mid = [(0, 68), (18, 56), (36, 66), (52, 58), (64, 76), (76, 60), (94, 66),
       (110, 56), (127, 66), (127, HORIZON), (0, HORIZON)]
c.poly(mid, "#5c4470")
c.line(52, 58, 64, 76, "#74588a")
c.line(76, 60, 64, 76, "#74588a")

# ---------- GROUND ----------
c.rect(0, HORIZON, 128, 128 - HORIZON, "#39412e")
c.rect(0, HORIZON, 128, 3, "#575a38")  # lit grass at horizon
for y in range(84, 128):
    for x in range(128):
        v = (x * 7 + y * 13 + (x // 4) * (y // 5)) % 17
        if v == 0:
            c.set(x, y, "#2f3627")
        elif v == 8:
            c.set(x, y, "#454d31")
# warm light spilling through the notch onto the ground
c.ellipse(64, 88, 20, 4, "#4d5434")
c.ellipse(64, 87, 12, 2, "#5c5c38")

# ---------- NEAR DARK RIDGE (tree line behind village) ----------
near = [(0, 80), (20, 72), (40, 79), (56, 73), (64, 80), (74, 74), (92, 80),
        (110, 73), (127, 79), (127, 88), (0, 88)]
c.poly(near, "#2c2a3c")

# distant silhouette pines on the ridge
def silhouette_pine(cx, base, h):
    top = base - h
    tiers = 3
    step = (h - 2) // tiers
    for i in range(tiers):
        ay = top + i * step
        by = top + (i + 1) * step + (1 if i < tiers - 1 else 0)
        hw = 1 + i
        c.poly([(cx, ay), (cx + hw, by), (cx - hw, by)], "#222b30")

for px, pb, ph in [(30, 82, 10), (46, 84, 9), (84, 84, 9), (100, 82, 10)]:
    silhouette_pine(px, pb, ph)

# ---------- STONE PATH (converges on the centre house = focal point) ----------
c.poly([(60, 100), (68, 100), (77, 127), (51, 127)], "#867c6f")
c.line(60, 100, 51, 127, "#9c9284")  # lit edge
# spur paths to the side houses
c.line(34, 94, 58, 100, "#6b6257")
c.line(94, 94, 70, 100, "#6b6257")
# stones
for sx, sy, sw, sh in [(62, 104, 2, 1), (66, 108, 2, 1), (60, 112, 2, 2),
                       (68, 114, 2, 1), (63, 118, 2, 2), (58, 122, 2, 1),
                       (70, 122, 2, 2), (64, 125, 3, 2)]:
    c.rect(sx, sy, sw, sh, "#6b6257")
for sx, sy, sw, sh in [(65, 103, 2, 1), (61, 110, 1, 1), (67, 118, 2, 1),
                       (60, 120, 2, 1)]:
    c.rect(sx, sy, sw, sh, "#a89e8f")

# ---------- HOUSES ----------
BODY, SHADE = "#5a4030", "#463125"
ROOF, ROOF_HI = "#38281f", "#7a563c"
DOOR, WIN = "#2e2018", "#ffd27a"

def house(cx, base, w, h, roof_h, chimney_x, lit):
    x0 = cx - w // 2
    top = base - h
    c.rect(chimney_x, top - (roof_h - 4), 3, roof_h + 1, "#4a352a")  # chimney behind roof
    c.rect(x0, top, w, h, BODY)
    c.rect(x0 + w - 3, top, 3, h, SHADE)
    c.rect(x0, base - 1, w, 1, "#2a2418")  # grounding shadow
    c.poly([(x0 - 2, top), (cx, top - roof_h), (x0 + w + 1, top)], ROOF)
    if lit in ("both", "left"):
        c.line(cx, top - roof_h, x0 + w + 1, top, ROOF_HI)
    if lit in ("both", "right"):
        c.line(x0 - 2, top, cx, top - roof_h, ROOF_HI)
    return x0, top

# left house
x0, top = house(32, 94, 16, 9, 7, 36, "right")
c.rect(30, 89, 4, 5, DOOR)
c.rect(26, 88, 3, 3, WIN)
c.rect(36, 88, 3, 3, WIN)

# right house
x0, top = house(96, 94, 16, 9, 7, 90, "left")
c.rect(94, 89, 4, 5, DOOR)
c.rect(89, 88, 3, 3, WIN)
c.rect(100, 88, 3, 3, WIN)

# centre house (main focal building)
x0, top = house(64, 100, 24, 13, 11, 70, "both")
c.rect(61, 94, 6, 6, DOOR)
c.rect(55, 91, 4, 4, WIN)
c.rect(69, 91, 4, 4, WIN)
c.line(57, 91, 57, 95, BODY)   # window frames
c.line(55, 93, 59, 93, BODY)
c.line(71, 91, 71, 95, BODY)
c.line(69, 93, 73, 93, BODY)

# ---------- PINE TREES (foreground frame) ----------
def pine(cx, base, h, lit_right):
    c.rect(cx - 1, base - 3, 2, 3, "#3a2a1e")
    top = base - h
    tiers = 3
    step = (h - 3) // tiers
    for i in range(tiers):
        ay = top + i * step
        by = top + (i + 1) * step + (1 if i < tiers - 1 else 0)
        hw = 2 + i * 2
        c.poly([(cx, ay), (cx + hw, by), (cx - hw, by)], "#24382a")
        hx = cx + hw if lit_right else cx - hw
        c.line(cx, ay, hx, by, "#3d5c3e")

pine(10, 112, 30, True)
pine(22, 108, 22, True)
pine(4, 102, 16, True)
pine(118, 112, 30, False)
pine(106, 108, 22, False)
pine(121, 102, 16, False)

# ---------- CHIMNEY SMOKE ----------
SMOKE = ["#d8d1c5", "#cbc4b9", "#bfb8ae"]
def smoke(puffs):
    for i, (px, py, pr) in enumerate(puffs):
        c.circle(px, py, pr, SMOKE[min(i // 2, 2)])

smoke([(71, 74, 2), (73, 70, 2), (75, 66, 3), (78, 61, 3),
       (81, 56, 2), (84, 52, 2), (86, 48, 1)])
smoke([(37, 74, 1), (39, 70, 2), (42, 65, 2), (45, 60, 1)])
smoke([(91, 74, 1), (93, 70, 2), (96, 65, 2), (99, 60, 1)])

# ---------- FOREGROUND GRASS ----------
c.ellipse(10, 124, 9, 3, "#2a3526")
c.ellipse(118, 124, 9, 3, "#2a3526")
for gx in [3, 9, 15, 20, 108, 114, 120, 125]:
    c.rect(gx, 126, 1, 2, "#31402c")

print(c.stats_text())
finish(c)
