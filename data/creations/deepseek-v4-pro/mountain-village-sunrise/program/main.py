# Mountain village at sunrise - 128x128 pixel art

# ---- palette constants (tuples, reused so the palette stays small) ----
SKY_TOP = (18, 16, 44)
SKY_MID = (60, 38, 82)
SKY_LOW = (150, 72, 96)
SKY_HOR = (238, 150, 88)
SKY_SUN = (252, 208, 120)

SUN_1 = (250, 170, 110)
SUN_2 = (252, 196, 126)
SUN_3 = (255, 220, 150)
SUN_4 = (255, 238, 178)
SUN_5 = (255, 250, 214)
SUN_6 = (255, 255, 238)

FAR_MT = (204, 164, 178)
MID_MT = (138, 111, 158)
NEAR_HILL = (82, 112, 74)

GROUND_TOP = (142, 152, 102)
GROUND_MID = (92, 116, 64)
GROUND_BOT = (48, 72, 44)

PATH_STONE = (170, 158, 140)
PATH_DARK = (108, 102, 90)

TREE_LIGHT = (56, 100, 60)
TREE_DARK = (32, 60, 38)
TREE_MID = (47, 88, 54)

WALL = (176, 122, 74)
WALL_DARK = (128, 84, 50)
ROOF = (140, 66, 46)
DOOR = (74, 48, 26)
WIN = (255, 214, 96)
WIN_FRAME = (58, 40, 26)
CHIMNEY = (88, 78, 74)
SMOKE = (200, 200, 208)
BIRD = (70, 60, 70)


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def sample(stops, t):
    for i in range(len(stops) - 1):
        c0, p0 = stops[i]
        c1, p1 = stops[i + 1]
        if p0 <= t <= p1:
            tt = 0 if p1 == p0 else (t - p0) / (p1 - p0)
            return lerp(c0, c1, tt)
    return stops[-1][0]


def grad_band(c, x, y, w, h, stops, K):
    """Draw a vertical gradient quantised to K bands (K distinct colours)."""
    for i in range(K):
        t0 = i / K
        t1 = (i + 1) / K
        col = sample(stops, (t0 + t1) / 2)
        y0 = y + int(round(h * t0))
        y1 = y + int(round(h * t1))
        if y1 > y0:
            c.rect(x, y0, w, y1 - y0, col)


def pine(c, x, y, h, col, dark):
    """Simple layered pine tree with a dark back edge and lighter front."""
    w_top = max(2, h // 6)
    w_mid = max(3, h // 4)
    w_bot = max(4, h // 3)
    # dark back layer
    c.poly([(x, y - h), (x - w_top, y - h * 2 // 3), (x + w_top, y - h * 2 // 3)], dark)
    c.poly([(x, y - h * 3 // 4), (x - w_mid, y - h // 3), (x + w_mid, y - h // 3)], dark)
    c.poly([(x, y - h // 3), (x - w_bot, y), (x + w_bot, y)], dark)
    # lighter front layer
    c.poly([(x + 1, y - h + 1), (x + 1 - w_top, y - h * 2 // 3), (x + 1 + w_top, y - h * 2 // 3)], col)
    c.poly([(x + 1, y - h * 3 // 4 + 1), (x + 1 - w_mid, y - h // 3), (x + 1 + w_mid, y - h // 3)], col)
    c.poly([(x + 1, y - h // 3 + 1), (x + 1 - w_bot, y), (x + 1 + w_bot, y)], col)


def house(c, x, y, w, h, wall=WALL, roof=ROOF, apex_off=None, chimney=True):
    """Wooden house. y is the top of the wall; roof rises above it."""
    apex = y - int(w * 0.55) if apex_off is None else y - apex_off
    # roof
    c.poly([(x - 4, y), (x + w // 2, apex), (x + w + 4, y)], roof)
    # chimney on the ridge
    if chimney:
        c.rect(x + w // 2 + 1, apex - 1, 4, 7, CHIMNEY)
    # walls
    c.rect(x, y, w, h, wall)
    c.rect(x, y, 2, h, WALL_DARK)
    c.rect(x + w - 2, y, 2, h, WALL_DARK)
    # door
    dw = max(5, w // 4)
    dh = max(6, h // 2)
    c.rect(x + w // 2 - dw // 2, y + h - dh, dw, dh, DOOR)
    # windows (lit)
    ww = max(4, w // 5)
    wh = ww
    c.rect(x + 4, y + 5, ww, wh, WIN_FRAME)
    c.rect(x + 5, y + 6, ww - 2, wh - 2, WIN)
    c.rect(x + w - 4 - ww, y + 5, ww, wh, WIN_FRAME)
    c.rect(x + w - 3 - ww, y + 6, ww - 2, wh - 2, WIN)


def smoke(c, cx, cy, col):
    """Curling smoke puffs rising from a chimney top."""
    pts = [(cx, cy - 4), (cx + 1, cy - 9), (cx - 2, cy - 14),
           (cx + 2, cy - 19), (cx - 1, cy - 24), (cx + 3, cy - 29)]
    for i, (px, py) in enumerate(pts):
        r = 2 + (i % 2)
        c.circle(px, py, r, col)


# ---------------- canvas ----------------
c = new_canvas(128, 128, name="mountain-village-sunrise")

# sky (horizon at y=80)
sky_stops = [
    (SKY_TOP, 0.0),
    (SKY_MID, 0.30),
    (SKY_LOW, 0.55),
    (SKY_HOR, 0.78),
    (SKY_SUN, 1.0),
]
grad_band(c, 0, 0, 128, 80, sky_stops, 26)

# sunrise glow and sun disc (behind the mountains)
c.circle(64, 62, 22, SUN_1)
c.circle(64, 62, 18, SUN_2)
c.circle(64, 62, 14, SUN_3)
c.circle(64, 62, 11, SUN_4)
c.circle(64, 62, 8, SUN_5)
c.circle(64, 62, 6, SUN_6)

# far mountains (hazy, central valley reveals the sun)
c.poly([
    (0, 80), (12, 64), (26, 74), (38, 56), (50, 72), (56, 64),
    (64, 80), (76, 60), (88, 74), (102, 56), (114, 72), (124, 64),
    (127, 74), (127, 80)
], FAR_MT)

# middle mountains (cooler purple)
c.poly([
    (0, 88), (14, 72), (28, 82), (42, 64), (52, 80), (58, 70),
    (66, 82), (78, 64), (92, 80), (104, 68), (116, 82), (126, 72),
    (127, 80), (127, 88)
], MID_MT)

# ground (meadow gradient)
ground_stops = [
    (GROUND_TOP, 0.0),
    (GROUND_MID, 0.5),
    (GROUND_BOT, 1.0),
]
grad_band(c, 0, 80, 128, 48, ground_stops, 10)

# near hills (dark green, sit on the meadow)
c.poly([
    (0, 98), (22, 84), (44, 94), (62, 80), (74, 94),
    (92, 80), (108, 92), (120, 84), (127, 94), (127, 98)
], NEAR_HILL)

# stone path winding to the centre house
for px, py in [(62, 124), (66, 121), (58, 115), (68, 109), (60, 103), (70, 97), (64, 110)]:
    c.ellipse(px, py, 5, 3, PATH_STONE)
for px, py in [(62, 124), (58, 118), (66, 112), (60, 106), (68, 99), (63, 94), (66, 120)]:
    c.ellipse(px, py, 2, 2, PATH_DARK)

# pine trees (behind the houses, framing the scene)
pine(c, 10, 96, 30, TREE_LIGHT, TREE_DARK)
pine(c, 22, 90, 24, TREE_MID, TREE_DARK)
pine(c, 34, 104, 20, TREE_LIGHT, TREE_DARK)
pine(c, 94, 102, 20, TREE_LIGHT, TREE_DARK)
pine(c, 106, 90, 24, TREE_MID, TREE_DARK)
pine(c, 116, 96, 30, TREE_LIGHT, TREE_DARK)

# three wooden houses (centre house is the focal point)
house(c, 28, 92, 20, 16, apex_off=12)      # left
house(c, 52, 88, 28, 22, apex_off=14)      # centre
house(c, 86, 90, 20, 18, apex_off=12)      # right

# chimney smoke
smoke(c, 68, 72, SMOKE)   # centre chimney
smoke(c, 40, 79, SMOKE)   # left chimney
smoke(c, 97, 77, SMOKE)   # right chimney

# a few distant birds
for bx, by in [(30, 22), (96, 18), (86, 30)]:
    c.line(bx - 3, by - 2, bx, by, BIRD)
    c.line(bx, by, bx + 3, by - 2, BIRD)

print(c.stats_text())
print("palette entries:", len(c.palette()))

finish(c)
