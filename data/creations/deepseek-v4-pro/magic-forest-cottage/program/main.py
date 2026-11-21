from pixelbench_api import *

W, H = 128, 128

# ---------------------------------------------------------------------------
# Base background layer and shared palette
# ---------------------------------------------------------------------------
bg = new_canvas(W, H, name="bg")

# ---- Palette ---------------------------------------------------------------
sky_top = bg.color("#120826", "sky_top")
sky1 = bg.color("#1e1038", "sky1")
sky2 = bg.color("#2e1a4e", "sky2")
sky3 = bg.color("#402664", "sky3")
sky4 = bg.color("#543478", "sky4")
star = bg.color("#d8d0ea", "star")

moon_glow_out = bg.color("#6f5a92", "moon_glow_out")
moon_glow_in = bg.color("#a08cbe", "moon_glow_in")
moon = bg.color("#f6e7b2", "moon")
moon_hi = bg.color("#fffbe0", "moon_hi")

ground_dark = bg.color("#16221c", "ground_dark")
ground_mid = bg.color("#243a2c", "ground_mid")
ground_light = bg.color("#3a5238", "ground_light")
moss = bg.color("#4a6634", "moss")

dist1 = bg.color("#1c142e", "dist1")
dist2 = bg.color("#2a1e42", "dist2")

mist_back = bg.color((150, 140, 186, 95), "mist_back")
mist_front = bg.color((172, 162, 200, 70), "mist_front")

stone_wall = bg.color("#685a52", "stone_wall")
stone_wall_dark = bg.color("#4e433c", "stone_wall_dark")
plaster = bg.color("#7c6c5e", "plaster")
timber = bg.color("#3a261a", "timber")

roof_dark = bg.color("#202a20", "roof_dark")
roof_mid = bg.color("#3a4c34", "roof_mid")
roof_light = bg.color("#587048", "roof_light")

window_glow = bg.color("#ff9a3c", "window_glow")
window_hi = bg.color("#ffc878", "window_hi")
window_frame = bg.color("#2c1e14", "window_frame")

door_wood = bg.color("#8a5a32", "door_wood")
door_dark = bg.color("#523018", "door_dark")

chimney_stone = bg.color("#7a6a5c", "chimney_stone")
chimney_dark = bg.color("#52463c", "chimney_dark")
smoke = bg.color((120, 110, 140, 120), "smoke")
warm_glow = bg.color((255, 150, 60, 60), "warm_glow")
warm_glow_soft = bg.color((255, 150, 60, 28), "warm_glow_soft")

well_stone = bg.color("#6e6258", "well_stone")
well_stone_dark = bg.color("#52483e", "well_stone_dark")
well_wood = bg.color("#5a3a24", "well_wood")
well_wood_dark = bg.color("#3a2414", "well_wood_dark")
well_dark = bg.color("#1e1820", "well_dark")

path1 = bg.color("#746e6a", "path1")
path2 = bg.color("#58504e", "path2")
path3 = bg.color("#3e3838", "path3")

tree_trunk = bg.color("#3a2418", "tree_trunk")
tree_trunk_dark = bg.color("#241410", "tree_trunk_dark")
leaf_red = bg.color("#8a2434", "leaf_red")
leaf_brown = bg.color("#6e3a22", "leaf_brown")
leaf_purple = bg.color("#4a2050", "leaf_purple")
leaf_dark = bg.color("#2e1828", "leaf_dark")


# ---------------------------------------------------------------------------
# Sky, ground, stars
# ---------------------------------------------------------------------------
def draw_sky():
    bands = [
        (0, 18, sky_top),
        (18, 36, sky1),
        (36, 54, sky2),
        (54, 72, sky3),
        (72, 88, sky4),
    ]
    for y0, y1, c in bands:
        bg.rect(0, y0, W, y1 - y0, c)
    # Soften the band boundaries with checker dithering.
    for yb, c1, c2 in [(18, sky_top, sky1), (36, sky1, sky2),
                       (54, sky2, sky3), (72, sky3, sky4)]:
        bg.dither(0, yb - 2, W, 4, [c1, c2], "checker")


def draw_ground():
    bg.rect(0, 88, W, 40, ground_dark)
    bg.dither(0, 88, W, 5, [ground_mid, ground_dark], "checker")
    bg.dither(0, 100, W, 9, [ground_mid, ground_dark], "checker")
    bg.dither(0, 116, W, 12, [ground_mid, ground_dark], "checker")
    # Mossy ground patches
    bg.ellipse(18, 110, 14, 4, moss)
    bg.ellipse(106, 116, 16, 5, moss)
    bg.ellipse(62, 120, 22, 5, moss)
    bg.ellipse(96, 102, 10, 3, ground_light)


def draw_stars():
    import random
    random.seed(7)
    for _ in range(30):
        x = random.randint(0, 127)
        y = random.randint(0, 66)
        if (x - 98) ** 2 + (y - 30) ** 2 < 19 ** 2:
            continue
        bg.set(x, y, star)
        if random.random() < 0.28:
            bg.set(x + 1, y, star)


draw_sky()
draw_ground()
draw_stars()


# ---------------------------------------------------------------------------
# Moon layer
# ---------------------------------------------------------------------------
moon_layer = new_canvas(W, H, name="moon")
moon_layer.circle(98, 30, 16, moon_glow_out)
moon_layer.circle(98, 30, 13, moon_glow_in)
moon_layer.circle(98, 30, 10, moon)
moon_layer.circle(95, 27, 4, moon_hi)
moon_layer.circle(102, 34, 2, moon_glow_in)
moon_layer.circle(94, 35, 1, moon_glow_in)
moon_layer.circle(101, 26, 1, moon_glow_in)


# ---------------------------------------------------------------------------
# Distant tree silhouettes
# ---------------------------------------------------------------------------
dist = new_canvas(W, H, name="dist")
for i, (x, c) in enumerate([(10, dist1), (26, dist2), (42, dist1),
                            (70, dist2), (84, dist1), (104, dist2),
                            (118, dist1)]):
    dist.poly([(x - 7, 88), (x, 70), (x + 7, 88)], c)


# ---------------------------------------------------------------------------
# Cottage layer
# ---------------------------------------------------------------------------
cottage = new_canvas(W, H, name="cottage")

# Walls (wood-and-stone)
cottage.rect(40, 80, 48, 28, stone_wall)
for (sx, sy) in [(42, 84), (50, 88), (58, 82), (66, 90), (74, 86),
                 (82, 92), (44, 98), (70, 100), (78, 96)]:
    cottage.rect(sx, sy, 4, 3, stone_wall_dark)
for (sx, sy) in [(46, 90), (60, 96), (72, 84), (84, 86)]:
    cottage.rect(sx, sy, 3, 2, plaster)

# Timber frame
for y in [80, 94, 106]:
    cottage.rect(40, y, 48, 2, timber)
for x in [40, 56, 72, 88]:
    cottage.rect(x, 80, 2, 28, timber)

# Warm glowing windows
for wx in [44, 76]:
    cottage.rect(wx, 86, 8, 8, window_glow)
    cottage.rect(wx - 1, 85, 10, 10, window_frame, fill=False)
    cottage.rect(wx + 3, 86, 2, 8, window_frame)
    cottage.rect(wx, 89, 8, 2, window_frame)
    cottage.rect(wx + 3, 87, 2, 2, window_hi)

# Arched wooden door
cottage.circle(64, 94, 6, door_wood)
cottage.rect(58, 94, 12, 14, door_wood)
for px in [61, 64, 67]:
    cottage.line(px, 94, px, 107, door_dark)
cottage.circle(64, 94, 7, window_frame, fill=False)
cottage.rect(63, 98, 3, 4, window_glow)

# Steep mossy roof (left slope in shadow, right slope moonlit)
cottage.poly([(30, 86), (64, 36), (64, 86)], roof_dark)
cottage.poly([(64, 36), (98, 86), (64, 86)], roof_mid)
cottage.rect(28, 84, 72, 3, roof_dark)

for (mx, my) in [(36, 80), (44, 74), (54, 66), (66, 60), (76, 56),
                 (86, 62), (92, 70), (34, 84), (96, 84)]:
    cottage.circle(mx, my, 3, moss)
cottage.line(64, 36, 98, 86, roof_light)
cottage.line(65, 37, 96, 84, roof_light)
cottage.line(30, 86, 64, 36, roof_light)

# Chimney and smoke
cottage.rect(48, 30, 10, 26, chimney_stone)
cottage.rect(46, 28, 14, 3, chimney_dark)
for yy in [34, 40, 46, 52]:
    cottage.line(48, yy, 57, yy, chimney_dark)
cottage.circle(53, 24, 2, smoke)
cottage.circle(56, 20, 3, smoke)
cottage.circle(60, 16, 3, smoke)


# ---------------------------------------------------------------------------
# Stone well with wooden winch
# ---------------------------------------------------------------------------
well = new_canvas(W, H, name="well")
well.rect(14, 72, 3, 30, well_wood)
well.rect(35, 72, 3, 30, well_wood)
well.rect(12, 86, 28, 3, well_wood)
well.rect(12, 86, 28, 1, well_wood_dark)
well.line(40, 86, 46, 80, well_wood)
well.circle(46, 80, 2, well_wood)
well.poly([(12, 74), (26, 62), (40, 74)], well_wood_dark)
well.rect(12, 72, 28, 2, well_wood)

well.rect(14, 98, 24, 12, well_stone)
well.rect(12, 95, 28, 4, well_stone)
well.rect(12, 95, 28, 1, well_stone_dark)
well.ellipse(26, 97, 9, 3, well_dark)
well.rect(16, 102, 5, 3, well_stone_dark)
well.rect(28, 104, 6, 3, well_stone_dark)


# ---------------------------------------------------------------------------
# Stone-slab path
# ---------------------------------------------------------------------------
path = new_canvas(W, H, name="path")
path.poly([(58, 108), (70, 108), (73, 114), (61, 115)], path1)
path.poly([(63, 115), (77, 114), (82, 122), (67, 124)], path2)
path.poly([(66, 124), (82, 123), (88, 127), (74, 127)], path3)
path.poly([(74, 126), (88, 125), (92, 127), (78, 127)], path1)
path.line(60, 110, 71, 111, path2)


# ---------------------------------------------------------------------------
# Twisted ancient trees with dark red / brown / purple leaves
# ---------------------------------------------------------------------------
trees = new_canvas(W, H, name="trees")

# Left tree
trees.poly([(4, 124), (16, 124), (18, 100), (13, 86), (17, 66), (11, 54),
            (8, 66), (7, 86), (10, 100)], tree_trunk)
trees.poly([(12, 88), (4, 74), (7, 90)], tree_trunk)
trees.poly([(13, 80), (22, 66), (16, 82)], tree_trunk)
trees.poly([(11, 60), (4, 52), (8, 64)], tree_trunk)
trees.poly([(15, 58), (24, 48), (18, 62)], tree_trunk)
for (cx, cy, r, c) in [(6, 52, 7, leaf_dark), (15, 44, 8, leaf_purple),
                       (24, 54, 6, leaf_red), (5, 70, 6, leaf_brown),
                       (12, 68, 5, leaf_dark), (15, 38, 6, leaf_red),
                       (24, 42, 4, leaf_brown), (9, 62, 5, leaf_dark)]:
    trees.circle(cx, cy, r, c)
for (cx, cy, r) in [(15, 40, 3), (22, 50, 3), (14, 64, 2)]:
    trees.circle(cx, cy, r, leaf_red)

# Right tree
trees.poly([(112, 124), (124, 124), (126, 100), (121, 86), (125, 66),
            (119, 54), (116, 66), (115, 86), (118, 100)], tree_trunk)
trees.poly([(116, 88), (124, 74), (120, 90)], tree_trunk)
trees.poly([(115, 80), (106, 66), (111, 82)], tree_trunk)
trees.poly([(119, 60), (126, 52), (122, 64)], tree_trunk)
trees.poly([(113, 58), (104, 48), (109, 62)], tree_trunk)
for (cx, cy, r, c) in [(120, 56, 8, leaf_dark), (108, 48, 9, leaf_purple),
                       (98, 58, 8, leaf_red), (122, 72, 6, leaf_brown),
                       (102, 72, 6, leaf_dark), (110, 40, 7, leaf_red),
                       (98, 44, 5, leaf_brown), (116, 64, 5, leaf_dark)]:
    trees.circle(cx, cy, r, c)
for (cx, cy, r) in [(110, 42, 3), (100, 54, 3), (106, 66, 2)]:
    trees.circle(cx, cy, r, leaf_red)


# ---------------------------------------------------------------------------
# Warm window glow spill
# ---------------------------------------------------------------------------
glow_wall = new_canvas(W, H, name="glow_wall")
glow_wall.ellipse(48, 90, 8, 7, warm_glow)
glow_wall.ellipse(80, 90, 8, 7, warm_glow)
glow_wall.ellipse(64, 101, 9, 7, warm_glow)

glow_ground = new_canvas(W, H, name="glow_ground")
glow_ground.ellipse(64, 115, 14, 8, warm_glow_soft)


# ---------------------------------------------------------------------------
# Mist (drawn as translucent bands, composited later)
# ---------------------------------------------------------------------------
mist_b = new_canvas(W, H, name="mist_b")
mist_b.ellipse(64, 84, 70, 9, mist_back)
mist_b.ellipse(12, 76, 22, 6, mist_back)
mist_b.ellipse(104, 78, 40, 7, mist_back)
mist_b.ellipse(64, 92, 80, 6, mist_back)

mist_f = new_canvas(W, H, name="mist_f")
mist_f.ellipse(64, 114, 70, 7, mist_front)
mist_f.ellipse(20, 112, 30, 5, mist_front)
mist_f.ellipse(104, 110, 36, 5, mist_front)


# ---------------------------------------------------------------------------
# Composite and inspect
# ---------------------------------------------------------------------------
layers = [bg, moon_layer, dist, mist_b, cottage, glow_wall, well, path,
          trees, glow_ground, mist_f]
result = flatten(layers, name="result")

print(result.stats_text())

finish(result)
