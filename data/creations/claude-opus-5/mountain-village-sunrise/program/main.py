import math
import random

rng = random.Random(7)
c = new_canvas(128, 128, name="output")

# ---------------- palette ----------------
SKY = [
    (0, 7, "#241f44"),
    (7, 15, "#322a55"),
    (15, 23, "#443166"),
    (23, 31, "#5a3a70"),
    (31, 39, "#754776"),
    (39, 46, "#915574"),
    (46, 52, "#b06a6c"),
    (52, 58, "#c9825f"),
    (58, 64, "#dd9a5c"),
    (64, 72, "#eeb366"),
    (72, 86, "#f7c878"),
]

FAR = "#6e6291"
FAR_LIT = "#e9a98a"
FAR_SNOW = "#cdc4dd"
MID = "#4f4a74"
MID_LIT = "#c9866e"
HILL = "#3c4a58"
HILL_LIT = "#6a6479"
TREELINE = "#2b3a38"

G1 = "#55683f"
G2 = "#48593a"
G3 = "#3c4d31"
GLIT = "#75814a"

TRUNK = "#3a2a1e"
PINE_D = "#27402f"
PINE_M = "#2f4a35"
PINE_L = "#5c7a4a"
PINE_FG = "#1b2a22"

WALL = "#8c5f3a"
PLANK = "#744c2e"
WALL_SH = "#63402a"
ROOF = "#52302a"
ROOF_LIT = "#d08a52"
ROOF_MID = "#6d4030"
BRICK = "#6b4336"
BRICK_LIT = "#8d5c46"
GLOW = "#ffce73"
GLOW_W = "#fff0c2"
FRAME = "#36211a"
DOOR = "#4b2f21"

SMOKE_A = "#ded7d9"
SMOKE_B = "#c3bac0"
SMOKE_C = "#a79ea8"

STONE = "#918d87"
STONE_L = "#aba6a0"
STONE_D = "#5d5a56"
DIRT = "#6b665f"


# ---------------- helpers ----------------
def pine(cv, x, base, h, dark, light=None, side=1, trunk=TRUNK):
    top = base - h
    body = max(3, h - 2)
    w = max(2, int(round(h * 0.34)))
    tierh = max(3, body // 3)
    tw = max(1, h // 9)
    cv.rect(x - tw // 2, base - max(2, h // 7), max(1, tw), max(2, h // 7) + 1, trunk)
    for y in range(top, base - 1):
        f = (y - top) / max(1, body - 1)
        m = ((y - top) % tierh) / tierh
        hw = int(round(f * w * (0.70 + 0.40 * m)))
        cv.line(x - hw, y, x + hw, y, dark)
        if light is not None and hw > 0 and (y - top) % 2 == 0:
            cv.set(x + side * hw, y, light)


def smoke(cv, x, y, h, drift, phase=0.0):
    """A soft rising plume: mostly vertical, widening and dissolving upward."""
    for k in range(h):
        cy = y - k
        t = k / float(h - 1)
        cx = x + drift * (t ** 1.8) * h * 0.30 + 1.9 * math.sin(phase + t * 3.4)
        cx = int(round(cx))
        wid = 1 if t < 0.18 else (2 if t < 0.38 else
                                  (3 if t < 0.58 else (4 if t < 0.8 else 5)))
        col = SMOKE_A if t < 0.28 else (SMOKE_B if t < 0.58 else SMOKE_C)
        x0 = cx - wid // 2
        if t < 0.58:
            cv.line(x0, cy, x0 + wid - 1, cy, col)
        else:
            # dissolve: skip pixels in a 2x2-ish pattern, more as it rises
            keep = 3 if t < 0.72 else (2 if t < 0.88 else 1)
            for i in range(wid):
                if (i + k) % 4 < keep:
                    cv.set(x0 + i, cy, col)


def heights(pts, w=128):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    out = []
    for x in range(w):
        if x <= xs[0]:
            out.append(ys[0])
            continue
        if x >= xs[-1]:
            out.append(ys[-1])
            continue
        for i in range(len(xs) - 1):
            if xs[i] <= x <= xs[i + 1]:
                f = (x - xs[i]) / (xs[i + 1] - xs[i])
                out.append(int(round(ys[i] + f * (ys[i + 1] - ys[i]))))
                break
    return out


def ridge(cv, pts, body, lit=None, snow=None, snow_depth=0, ybase=128,
          sun_x=64, w=128):
    """Mountain range drawn as a column heightfield, so valleys stay valleys."""
    top = heights(pts, w)
    for x in range(w):
        cv.line(x, top[x], x, ybase, body)
    if lit is not None:
        for x in range(w):
            prev = top[max(0, x - 1)]
            nxt = top[min(w - 1, x + 1)]
            if prev == nxt:
                continue
            facing = (nxt > prev) if x < sun_x else (nxt < prev)
            if facing:
                cv.line(x, top[x], x, top[x] + 1, lit)
    if snow is not None and snow_depth > 0:
        for x in range(w):
            lo, hi = max(0, x - 5), min(w, x + 6)
            if top[x] <= min(top[lo:hi]):
                peak = top[x]
                for xx in range(max(0, x - 8), min(w, x + 9)):
                    d = snow_depth - (top[xx] - peak)
                    if d > 0:
                        cv.line(xx, top[xx], xx, top[xx] + min(d, 3), snow)
    return top


# ---------------- sky ----------------
for y0, y1, col in SKY:
    c.rect(0, y0, 128, y1 - y0, col)
for i in range(len(SKY) - 1):
    yb = SKY[i][1]
    c.dither(0, yb - 2, 128, 4, [SKY[i][2], SKY[i + 1][2]], pattern="bayer4")

# sun
HALO = "#f3b277"
for yy in range(40, 77):
    for xx in range(46, 83):
        d2 = (xx - 64) ** 2 + (yy - 58) ** 2
        if 196 < d2 <= 324 and (xx + yy) % 2 == 0:
            c.set(xx, yy, HALO)
        elif 169 < d2 <= 196 and (xx * 3 + yy) % 3 != 0:
            c.set(xx, yy, HALO)
c.circle(64, 58, 13, "#f6bd7c")
c.circle(64, 58, 10, "#ffe9a8")
c.circle(64, 58, 6, "#fff6d8")

# birds
for bx, by in ((26, 28), (34, 24), (100, 33)):
    c.line(bx, by, bx + 1, by - 1, "#3b2f4e")
    c.line(bx + 2, by - 1, bx + 3, by, "#3b2f4e")

# ---------------- far mountains ----------------
far = [(0, 60), (7, 52), (14, 57), (22, 44), (27, 38), (36, 50), (45, 58),
       (54, 63), (64, 67), (74, 60), (84, 50), (93, 41), (101, 50), (109, 58),
       (116, 52), (122, 57), (127, 54)]
ridge(c, far, FAR, FAR_LIT, FAR_SNOW, 7, ybase=92)
c.set(27, 38, "#f1ddea")
c.set(93, 41, "#f1ddea")

# ---------------- mid mountains ----------------
mid = [(0, 75), (9, 68), (18, 74), (29, 65), (39, 59), (49, 69), (57, 74),
       (64, 76), (71, 74), (79, 68), (88, 61), (97, 70), (107, 76), (117, 70),
       (127, 74)]
ridge(c, mid, MID, MID_LIT, "#b8aed0", 5, ybase=96)

# valley mist between the mid range and the near hills, for depth
c.dither(0, 73, 128, 2, ["#73679a", MID], pattern="bayer4")
c.dither(0, 75, 128, 4, ["#8478a6", HILL], pattern="bayer4")

# ---------------- near hills ----------------
c.path("M 0 100 L 0 82 Q 16 75 32 80 Q 48 85 64 81 Q 82 75 100 80 "
       "Q 114 84 127 79 L 127 100 Z", HILL)
c.dither(0, 79, 128, 3, [HILL, HILL_LIT], pattern="bayer4")

# distant tree line on the ridge
for i in range(34):
    tx = 2 + i * 4 + rng.randint(-1, 1)
    base = 92 + rng.randint(-1, 1)
    h = rng.randint(9, 15)
    pine(c, tx, base, h, TREELINE, None, 1, TREELINE)

# ---------------- ground ----------------
c.path("M 0 128 L 0 90 Q 18 85 38 88 Q 52 90 64 87 Q 84 83 102 88 "
       "Q 116 91 127 87 L 127 128 Z", G1)
c.rect(0, 103, 128, 12, G2)
c.rect(0, 115, 128, 13, G3)
c.dither(0, 101, 128, 4, [G1, G2], pattern="bayer4")
c.dither(0, 113, 128, 4, [G2, G3], pattern="bayer4")
# warm rim along the meadow crest
c.path("M 3 89 Q 18 85 38 88 Q 52 90 64 87 Q 84 83 102 88 Q 114 91 124 88",
       GLIT, fill=False)

# ---------------- stone path ----------------
path_pts = [(61, 100), (68, 100), (75, 112), (86, 127), (44, 127), (55, 112)]
c.poly(path_pts, DIRT)
dirt_i = c.color(DIRT)
for _ in range(430):
    x = rng.randint(40, 90)
    y = rng.randint(100, 127)
    if 0 <= x < 128 and c.get(x, y) == dirt_i:
        w = rng.choice((2, 2, 3))
        h = rng.choice((1, 2))
        col = rng.choice((STONE, STONE, STONE_L, STONE_D))
        c.rect(x, y, w, h, col)

# ---------------- mid trees ----------------
for tx, base, h, side in ((12, 104, 24, 1), (24, 100, 17, 1), (44, 98, 15, 1),
                          (82, 99, 16, -1), (116, 104, 23, -1), (104, 99, 14, -1),
                          (36, 96, 12, 1), (92, 96, 12, -1)):
    pine(c, tx, base, h, PINE_M, PINE_L, side)


# ---------------- houses ----------------
def house(cv, x0, x1, wtop, wbot, apex_y, eave_x0, eave_x1, eave_y,
          chim_x, chim_y0, chim_y1, win, door=None):
    cx = (x0 + x1) // 2
    cv.rect(x0, wtop, x1 - x0 + 1, wbot - wtop + 1, WALL)
    for y in range(wtop + 2, wbot, 4):
        cv.line(x0, y, x1, y, PLANK)
    cv.rect(x0, wtop, 2, wbot - wtop + 1, WALL_SH)
    cv.rect(x1 - 1, wtop, 2, wbot - wtop + 1, WALL_SH)
    cv.line(x0, wbot, x1, wbot, "#3b2a1e")
    # roof
    cv.poly([(cx, apex_y), (eave_x1, eave_y), (eave_x0, eave_y)], ROOF)
    cv.line(cx, apex_y + 1, eave_x0 + 2, eave_y - 1, ROOF_MID)
    cv.line(cx, apex_y + 1, eave_x1 - 2, eave_y - 1, ROOF_MID)
    cv.line(cx, apex_y, eave_x0, eave_y, ROOF_LIT)
    cv.line(cx, apex_y, eave_x1, eave_y, ROOF_LIT)
    cv.line(eave_x0, eave_y, eave_x1, eave_y, ROOF_MID)
    # chimney
    cv.rect(chim_x, chim_y0, 4, chim_y1 - chim_y0 + 1, BRICK)
    cv.rect(chim_x, chim_y0, 4, 2, BRICK_LIT)
    # windows
    for (wx, wy, ww, wh) in win:
        cv.rect(wx - 1, wy - 1, ww + 2, wh + 2, FRAME)
        cv.rect(wx, wy, ww, wh, GLOW)
        cv.rect(wx + 1, wy + 1, max(1, ww - 2), max(1, wh - 2), GLOW_W)
        cv.line(wx, wy + wh // 2, wx + ww - 1, wy + wh // 2, FRAME)
    if door:
        dx, dy, dw, dh = door
        cv.rect(dx - 1, dy - 1, dw + 2, dh + 1, FRAME)
        cv.rect(dx, dy, dw, dh, DOOR)
        cv.line(dx, dy, dx + dw - 1, dy, GLOW)


# left house
house(c, 20, 40, 92, 105, 82, 16, 44, 94, 24, 83, 90,
      [(25, 97, 4, 4), (34, 97, 3, 4)])
# right house
house(c, 88, 108, 90, 103, 80, 84, 112, 92, 103, 81, 88,
      [(92, 95, 3, 4), (101, 95, 4, 4)])
# centre house (focal point)
house(c, 50, 78, 86, 104, 70, 45, 83, 88, 70, 72, 82,
      [(54, 92, 5, 5), (70, 92, 5, 5)], door=(62, 95, 5, 9))
# warm light spill from the centre door onto the path
c.dither(60, 104, 9, 4, [GLOW, DIRT], pattern="bayer4")
c.dither(58, 107, 13, 3, [STONE_L, DIRT], pattern="bayer4")

SHADOW = "#2f3a2b"
# ground shadows just below each structure
c.dither(17, 106, 28, 3, [SHADOW, G2], pattern="bayer4")
c.dither(85, 104, 28, 3, [SHADOW, G2], pattern="bayer4")
c.dither(46, 105, 36, 3, [SHADOW, G2], pattern="bayer4")
for tx, base in ((12, 104), (24, 100), (44, 98), (82, 99), (116, 104),
                 (104, 99), (36, 96), (92, 96)):
    c.dither(tx - 4, base + 1, 9, 2, [SHADOW, G2], pattern="checker")

# ---------------- chimney smoke ----------------
smoke(c, 71, 69, 30, 0.55, 0.0)
smoke(c, 25, 80, 22, 0.75, 1.3)
smoke(c, 104, 78, 24, -0.7, 2.4)

# ---------------- foreground framing ----------------
pine(c, 4, 128, 34, PINE_FG, None, 1, "#1a241d")
pine(c, 122, 126, 31, PINE_FG, None, 1, "#1a241d")
pine(c, 112, 128, 22, PINE_D, None, -1, "#20302a")
pine(c, 16, 127, 20, PINE_D, None, 1, "#20302a")

# grass tufts / rocks in the foreground
for _ in range(60):
    x = rng.randint(0, 127)
    y = rng.randint(112, 127)
    if 42 < x < 88 and y > 110:
        continue
    c.set(x, y, rng.choice(("#334228", "#46583a", "#2c3a24")))
for rx, ry in ((34, 118), (96, 115), (24, 112), (108, 122)):
    c.rect(rx, ry, 3, 2, "#55544e")
    c.set(rx, ry, "#6e6b62")

view(c)
print(c.stats_text())
result = c
save("mountain-village-sunrise", result)
finish(result)
