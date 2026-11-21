from pixelbench_api import *

# ---------------------------------------------------------------
#  Fantasy RPG title screen - 128x128
#  Castle on a seaside cliff, sunset, two towers with flags,
#  large orange sun, layered clouds, dark rocks foreground.
# ---------------------------------------------------------------

c = new_canvas(128, 128, name="title")

# ---- palette ---------------------------------------------------
SKY = [
    (42, 20, 64),    # sky1 deep indigo
    (74, 31, 110),   # sky2 purple
    (122, 42, 120),  # sky3 magenta
    (176, 58, 98),   # sky4 pink-red
    (217, 90, 67),   # sky5 red-orange
    (239, 138, 50),  # sky6 orange
    (248, 185, 62),  # sky7 yellow-orange
    (251, 214, 122), # sky8 pale horizon
]

CLOUD_FAR  = (26, 13, 46)
CLOUD_MID  = (58, 28, 90)
CLOUD_NEAR = (32, 16, 54)
CLOUD_DARK = (16, 8, 30)

SUN_EDGE = (224, 96, 40)
SUN1     = (255, 154, 42)
SUN2     = (255, 210, 62)
SUN_CORE = (255, 246, 192)

SEA_MID  = (60, 47, 94)
SEA_DEEP = (28, 28, 58)
SEA_DARK = (20, 20, 44)

ROCK_DARK  = (20, 16, 32)
ROCK_DEEP  = (12, 10, 22)
ROCK_LIGHT = (64, 46, 88)
CASTLE     = (16, 12, 26)
ROOF       = (44, 32, 66)
FLAG_RED   = (217, 70, 60)
RIM        = (190, 110, 80)
CLIFF_RIM  = (160, 90, 80)

for i, v in enumerate(SKY):
    c.color(v, name=f"sky{i+1}")
c.color(CLOUD_FAR, "cloud_far")
c.color(CLOUD_MID, "cloud_mid")
c.color(CLOUD_NEAR, "cloud_near")
c.color(CLOUD_DARK, "cloud_dark")
c.color(SUN_EDGE, "sun_edge")
c.color(SUN1, "sun1")
c.color(SUN2, "sun2")
c.color(SUN_CORE, "sun_core")
c.color(SEA_MID, "sea_mid")
c.color(SEA_DEEP, "sea_deep")
c.color(SEA_DARK, "sea_dark")
c.color(ROCK_DARK, "rock_dark")
c.color(ROCK_DEEP, "rock_deep")
c.color(ROCK_LIGHT, "rock_light")
c.color(CASTLE, "castle")
c.color(ROOF, "roof")
c.color(FLAG_RED, "flag_red")
c.color(RIM, "rim")
c.color(CLIFF_RIM, "cliff_rim")

# ---- 4x4 ordered dithering -------------------------------------
BAYER4 = [
    [0, 8, 2, 10],
    [12, 4, 14, 6],
    [3, 11, 1, 9],
    [15, 7, 13, 5],
]

def bayer(x, y):
    return (BAYER4[y & 3][x & 3] + 0.5) / 16.0

def stops_to_idx(stops):
    return [(y, c.color(col)) for y, col in stops]

def grad_idx(idx_stops, x, y):
    if y <= idx_stops[0][0]:
        return idx_stops[0][1]
    if y >= idx_stops[-1][0]:
        return idx_stops[-1][1]
    for i in range(len(idx_stops) - 1):
        ya, ia = idx_stops[i]
        yb, ib = idx_stops[i + 1]
        if ya <= y <= yb:
            if ya == yb:
                return ib
            t = (y - ya) / (yb - ya)
            return ib if bayer(x, y) < t else ia
    return idx_stops[-1][1]

def vgrad(x0, y0, x1, y1, idx_stops):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            c.set(x, y, grad_idx(idx_stops, x, y))

# ---- sky -------------------------------------------------------
sky_stops = stops_to_idx([
    (0, SKY[0]),
    (10, SKY[1]),
    (22, SKY[2]),
    (34, SKY[3]),
    (46, SKY[4]),
    (58, SKY[5]),
    (68, SKY[6]),
    (79, SKY[7]),
])
vgrad(0, 0, 127, 79, sky_stops)

# ---- far / mid / near clouds -----------------------------------
def cloud(y_base, x0, x1, color, puffs):
    c.rect(x0, y_base - 4, x1 - x0 + 1, 5, color)
    for (cx, cy, rx, ry) in puffs:
        c.ellipse(cx, cy, rx, ry, color, fill=True)

# behind the sun
cloud(18, 8, 120, CLOUD_FAR, [
    (18, 15, 10, 3), (38, 14, 16, 4), (62, 15, 13, 4),
    (86, 14, 15, 4), (108, 15, 10, 3),
])
cloud(28, 15, 112, CLOUD_MID, [
    (30, 24, 10, 3), (52, 23, 15, 4), (78, 24, 13, 4), (102, 24, 11, 3),
])
cloud(40, 5, 122, CLOUD_NEAR, [
    (18, 36, 11, 3), (46, 35, 15, 4), (72, 36, 13, 4),
    (98, 35, 15, 4), (118, 36, 9, 3),
])

# ---- large orange sun ------------------------------------------
sun_stops = stops_to_idx([
    (34, SUN_EDGE),
    (46, SUN1),
    (58, SUN2),
    (72, SUN_CORE),
    (82, SUN2),
])

def sun_disc(cx, cy, r, idx_stops):
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            dx = x - cx
            dy = y - cy
            if dx * dx + dy * dy <= r * r:
                c.set(x, y, grad_idx(idx_stops, x, y))

sun_disc(64, 58, 24, sun_stops)

# foreground cloud crossing the lower sun
cloud(68, 0, 127, CLOUD_DARK, [
    (16, 64, 12, 4), (40, 63, 17, 5), (64, 64, 14, 5),
    (88, 63, 17, 5), (112, 64, 12, 4),
])

# ---- sea --------------------------------------------------------
sea_stops = stops_to_idx([
    (80, SKY[7]),
    (84, SKY[4]),
    (90, SKY[2]),
    (96, SEA_MID),
    (103, SEA_DEEP),
    (108, SEA_DARK),
])
vgrad(0, 80, 127, 108, sea_stops)

# glowing horizon line
c.line(0, 80, 127, 80, SUN_CORE)

# sun reflection shimmer on the water
for y in range(81, 100):
    w = max(1, int(20 - (y - 80) * 1.25))
    col = SUN2 if (y // 2) % 2 == 0 else SUN_CORE
    x0 = 64 - w // 2
    x1 = 64 + w // 2
    if (y // 3) % 2 == 0:
        c.line(x0, y, x1, y, col)
    else:
        c.line(x0, y, x0 + max(1, w // 2), y, col)
        c.line(64 + 1, y, x1, y, col)

# ---- seaside cliff ----------------------------------------------
cliff_pts = [
    (74, 100), (78, 86), (82, 74), (86, 62), (90, 54), (94, 52),
    (104, 50), (114, 50), (120, 52), (125, 56), (127, 62), (127, 100),
]
c.poly(cliff_pts, ROCK_DARK, fill=True)

# warm rim light on the sun-facing left edge and plateau
cliff_rim_pts = [
    (74, 100), (78, 86), (82, 74), (86, 62), (90, 54), (94, 52),
    (104, 50), (114, 50), (120, 52), (125, 56),
]
for i in range(len(cliff_rim_pts) - 1):
    c.line(cliff_rim_pts[i][0], cliff_rim_pts[i][1],
           cliff_rim_pts[i + 1][0], cliff_rim_pts[i + 1][1], CLIFF_RIM)

# subtle cliff cracks / texture
c.line(92, 58, 98, 52, ROCK_DEEP)
c.line(100, 54, 108, 50, ROCK_DEEP)
c.line(116, 52, 124, 58, ROCK_DEEP)
c.line(82, 78, 88, 68, ROCK_DEEP)

# ---- castle ------------------------------------------------------
# left tower
c.rect(92, 36, 12, 2, CASTLE)          # crenellation behind roof
c.rect(92, 38, 12, 14, CASTLE)         # body
c.poly([(90, 38), (98, 26), (106, 38)], ROOF, fill=True)

# right tower
c.rect(112, 36, 12, 2, CASTLE)
c.rect(112, 38, 12, 14, CASTLE)
c.poly([(110, 38), (118, 26), (126, 38)], ROOF, fill=True)

# connecting wall with battlements
c.rect(104, 44, 8, 8, CASTLE)
for x in (104, 106, 108, 110):
    c.rect(x, 42, 1, 2, CASTLE)

# warm windows / gate
c.rect(96, 42, 2, 3, SUN2)
c.rect(100, 46, 2, 2, SUN2)
c.rect(116, 42, 2, 3, SUN2)
c.rect(120, 46, 2, 2, SUN2)
c.rect(106, 48, 3, 4, SUN2)

# flags flying toward the sunset
c.line(98, 26, 98, 16, CASTLE)
c.poly([(98, 16), (88, 17), (98, 18)], FLAG_RED, fill=True)
c.line(118, 26, 118, 16, CASTLE)
c.poly([(118, 16), (108, 17), (118, 18)], SKY[6], fill=True)

# subtle warm rim on castle edges facing the sun
c.line(92, 52, 92, 36, RIM)
c.line(112, 52, 112, 36, RIM)
c.line(104, 52, 104, 44, RIM)

# ---- birds -------------------------------------------------------
def bird(x, y):
    c.set(x, y, CLOUD_FAR)
    c.set(x + 2, y, CLOUD_FAR)
    c.set(x + 1, y - 1, CLOUD_FAR)

bird(26, 30)
bird(36, 26)
bird(48, 32)
bird(96, 24)
bird(106, 30)

# ---- foreground rocks --------------------------------------------
back_top = [
    (0, 110), (8, 104), (16, 108), (24, 102), (32, 107), (40, 101),
    (50, 106), (58, 100), (66, 105), (74, 109), (82, 103), (90, 108),
    (98, 102), (106, 107), (114, 101), (122, 106), (127, 103),
]
front_top = [
    (0, 122), (10, 114), (20, 118), (30, 112), (40, 117), (50, 111),
    (60, 116), (70, 110), (80, 115), (90, 111), (100, 117), (110, 113),
    (120, 119), (127, 116),
]

back_poly = back_top + [(127, 128), (0, 128)]
front_poly = front_top + [(127, 128), (0, 128)]
c.poly(back_poly, ROCK_DARK, fill=True)
c.poly(front_poly, ROCK_DEEP, fill=True)

for i in range(len(back_top) - 1):
    c.line(back_top[i][0], back_top[i][1],
           back_top[i + 1][0], back_top[i + 1][1], ROCK_LIGHT)
for i in range(len(front_top) - 1):
    c.line(front_top[i][0], front_top[i][1],
           front_top[i + 1][0], front_top[i + 1][1], RIM)

# ---- report ------------------------------------------------------
print(c.stats_text())
print(c.matrix_text(region=(36, 30, 92, 84)))
print(c.matrix_text(region=(40, 78, 90, 102)))

finish(c)
