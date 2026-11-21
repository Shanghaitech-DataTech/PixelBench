import random

# ---- palette ----
BASE  = "#4a7a34"   # mid green
LIGHT = "#6aa341"   # light green speckle
PALE  = "#86bf55"   # highlight tip
DARK  = "#36612a"   # dark green speckle
DEEP  = "#27491f"   # tuft shadow
DIRT  = "#6d5236"   # bare dirt
DIRTL = "#89693f"   # dirt highlight
YEL   = "#e8cf52"   # flower
YELL  = "#f5e892"   # flower highlight

c = new_canvas(16, 16, background=BASE, name="grass")


def put(x, y, col):
    c.set(x % 16, y % 16, col)


def blade(x, y, col, h=2):
    for i in range(h):
        put(x, y + i, col)


# ---- interleaved speckle field (seeded, wraps by construction) ----
rnd = random.Random(11)
for y in range(16):
    for x in range(16):
        # offset rows so the speckles interleave instead of lining up
        r = rnd.random()
        if r < 0.20:
            put(x, y, LIGHT)
        elif r < 0.38:
            put(x, y, DARK)

# ---- short vertical blades, light over dark, scattered ----
light_blades = [(1, 2), (5, 0), (9, 5), (13, 3), (3, 9), (7, 12), (11, 10), (15, 13)]
for x, y in light_blades:
    blade(x, y, LIGHT, 2)
    put(x, y, PALE)

dark_blades = [(2, 6), (6, 4), (10, 1), (14, 7), (4, 13), (8, 8), (12, 14), (0, 11)]
for x, y in dark_blades:
    blade(x, y, DARK, 2)

# ---- darker grass tufts (small clumps, wrap across edges) ----
tufts = [(3, 3), (11, 7), (6, 14), (15, 1)]
for tx, ty in tufts:
    put(tx, ty, DEEP)
    put(tx + 1, ty, DARK)
    put(tx, ty + 1, DARK)
    put(tx - 1, ty + 1, DEEP)
    put(tx + 1, ty + 2, DEEP)

# ---- sparse bare-dirt patches ----
dirt_patches = [(8, 2), (2, 11), (13, 11)]
for dx, dy in dirt_patches:
    put(dx, dy, DIRT)
    put(dx + 1, dy, DIRTL)
    put(dx, dy + 1, DIRTL)
    put(dx + 1, dy + 1, DIRT)
put(9, 3, DIRT)
put(1, 12, DIRT)

# ---- tiny yellow flowers ----
flowers = [(5, 7), (12, 4), (7, 15)]
for fx, fy in flowers:
    put(fx, fy, YEL)
    put(fx + 1, fy, YELL)
    put(fx, fy - 1, PALE)

view(c)

# tiling check on a working canvas (not submitted)
tile = new_canvas(32, 32, name="tilecheck")
for oy in (0, 16):
    for ox in (0, 16):
        tile.blit(c, ox, oy)
view(tile)

result = c
finish(result)
