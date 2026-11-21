import random

W = H = 64

# ---------------- background scene ----------------
bg = new_canvas(W, H, background=None, name="bg")

SKY_TOP  = bg.color("#7fc4e8", "sky_top")
SKY_LOW  = bg.color("#a9dcf0", "sky_low")
CLOUD    = bg.color("#ffffff")
CLOUD_SH = bg.color("#d7ebf7", "cloud_shade")
SUN      = bg.color("#ffe9a8", "sun")
SUN_CORE = bg.color("#ffd76e", "sun_core")
BIRD     = bg.color("#4a4a52", "bird")
HILL     = bg.color("#7fb069", "hill")
TREE_D   = bg.color("#3f7d3c", "tree_dark")
TREE_L   = bg.color("#5b9c4a", "tree_light")
GRASS    = bg.color("#6aa84f", "grass")
GRASS_D  = bg.color("#4e8c3a", "grass_dark")
GRASS_L  = bg.color("#8cc46a", "grass_light")
DIRT     = bg.color("#9a8a5f", "dirt")
FENCE    = bg.color("#8b5e34", "fence")
FENCE_D  = bg.color("#6e4a28", "fence_dark")
TRUNK    = bg.color("#7a5230", "trunk")
ROAD     = bg.color("#6e6e74", "road")
ROAD_D   = bg.color("#5a5a61", "road_dark")
ROAD_L   = bg.color("#7e7e86", "road_light")
LINE     = bg.color("#e8e4d8", "road_line")
SHADOW   = bg.color("#57575e", "bike_shadow")
FLW_R    = bg.color("#d94f4f", "flower_red")
FLW_Y    = bg.color("#e8c84f", "flower_yellow")

# --- sky ---
bg.rect(0, 0, 64, 20, SKY_TOP)
bg.rect(0, 20, 64, 8, SKY_LOW)

# sun
bg.circle(57, 6, 4, SUN)
bg.circle(57, 6, 2, SUN_CORE)

# clouds
def big_cloud(cx, cy):
    bg.ellipse(cx, cy, 5, 2, CLOUD)
    bg.ellipse(cx - 4, cy + 1, 3, 2, CLOUD)
    bg.ellipse(cx + 4, cy + 1, 3, 2, CLOUD)
    bg.rect(cx - 6, cy + 2, 13, 1, CLOUD_SH)

def small_cloud(cx, cy):
    bg.ellipse(cx, cy, 3, 1, CLOUD)
    bg.ellipse(cx - 2, cy + 1, 2, 1, CLOUD)
    bg.ellipse(cx + 2, cy + 1, 2, 1, CLOUD)
    bg.rect(cx - 4, cy + 1, 9, 1, CLOUD_SH)

big_cloud(12, 7)
small_cloud(32, 13)
small_cloud(46, 5)

# birds
for (bx, by) in [(22, 15), (28, 12)]:
    bg.set(bx, by, BIRD)
    bg.set(bx + 1, by + 1, BIRD)
    bg.set(bx + 2, by, BIRD)

# --- horizon: hills and distant treeline ---
bg.ellipse(14, 30, 22, 6, HILL)
bg.ellipse(47, 31, 22, 6, HILL)
for cx in [3, 10, 21, 31, 42, 53, 61]:
    bg.circle(cx, 25, 2, TREE_D)

# --- fields ---
bg.rect(0, 27, 64, 16, GRASS)          # y27..42
rng = random.Random(11)
for _ in range(110):
    bg.set(rng.randrange(64), rng.randrange(28, 43), GRASS_D)
for _ in range(55):
    bg.set(rng.randrange(64), rng.randrange(28, 43), GRASS_L)

# fence along the far verge
for px in [1, 15, 57]:
    bg.rect(px, 30, 1, 9, FENCE)
    bg.set(px, 30, FENCE_D)
bg.rect(0, 32, 64, 1, FENCE)
bg.rect(0, 36, 64, 1, FENCE)

# trees
bg.rect(3, 32, 2, 8, TRUNK)
bg.circle(4, 29, 4, TREE_D)
bg.circle(2, 27, 2, TREE_L)
bg.circle(6, 27, 2, TREE_L)
bg.rect(60, 31, 2, 6, TRUNK)
bg.circle(61, 28, 3, TREE_D)
bg.set(60, 26, TREE_L)
bg.set(62, 29, TREE_L)

# flowers in the far field
for (fx, fy, fc) in [(2, 35, FLW_R), (5, 41, FLW_Y), (59, 34, FLW_R),
                     (62, 40, FLW_Y), (1, 29, FLW_Y), (58, 42, FLW_R)]:
    bg.set(fx, fy, fc)

# --- road ---
bg.rect(0, 43, 64, 1, DIRT)            # gravel shoulder
bg.rect(0, 44, 64, 15, ROAD)           # y44..58
bg.rect(0, 44, 64, 1, ROAD_L)
bg.rect(0, 58, 64, 1, ROAD_D)
for _ in range(70):
    bg.set(rng.randrange(64), rng.randrange(45, 58), ROAD_D)
for _ in range(40):
    bg.set(rng.randrange(64), rng.randrange(45, 58), ROAD_L)
for x0 in range(0, 64, 12):            # dashed centre line
    bg.rect(x0, 52, 6, 2, LINE)

# shadow under the motorcycle
bg.ellipse(32, 49, 24, 1, SHADOW)
bg.rect(11, 48, 6, 1, ROAD_D)
bg.rect(49, 48, 6, 1, ROAD_D)

# --- near verge ---
bg.rect(0, 59, 64, 5, GRASS_D)
for _ in range(40):
    bg.set(rng.randrange(64), rng.randrange(59, 64), GRASS)
for _ in range(18):
    bg.set(rng.randrange(64), rng.randrange(59, 64), GRASS_L)
for (fx, fy, fc) in [(9, 61, FLW_Y), (26, 62, FLW_R), (47, 61, FLW_Y), (57, 62, FLW_R)]:
    bg.set(fx, fy, fc)

# ---------------- motorcycle layer ----------------
moto = input_canvas.copy(name="moto")
WHITE = moto.color("#ffffff")
for y in range(H):
    for x in range(W):
        if moto.get(x, y) == WHITE:
            moto.set(x, y, None)

# ---------------- composite ----------------
result = flatten([bg, moto], name="output")
print(result.stats_text())
print(result.matrix_text(region=(0, 42, 63, 55)))

finish(result)
print(result.stats_text())
