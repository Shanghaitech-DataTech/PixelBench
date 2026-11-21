from pixelbench_api import new_canvas, finish
import random

W = H = 16
c = new_canvas(W, H, name="minecraft_stone")

rng = random.Random(20240613)

# Palette (8 visible colors, <= 10 allowed)
BASE   = c.color("#7e7e7e")
DARK   = c.color("#6e6e6e")
DARKER = c.color("#5e5e5e")
LIGHT  = c.color("#8b8b8b")
BRIGHT = c.color("#979797")
DIM    = c.color("#4f4f4f")
CRACK  = c.color("#3a3a3a")
CORE   = c.color("#242424")

c.rect(0, 0, W, H, BASE)

# Seamless value noise: random 8x8 lattice, bilinear-interpolated with
# period 16 so columns 0 and 15 / rows 0 and 15 wrap smoothly.
grid = [[rng.random() for _ in range(8)] for _ in range(8)]

def smooth_value(x, y):
    gx = (x % 16) / 16.0 * 8
    gy = (y % 16) / 16.0 * 8
    x0 = int(gx) % 8
    y0 = int(gy) % 8
    fx = gx - int(gx)
    fy = gy - int(gy)
    x1 = (x0 + 1) % 8
    y1 = (y0 + 1) % 8
    return (grid[y0][x0] * (1 - fx) * (1 - fy) +
            grid[y0][x1] * fx * (1 - fy) +
            grid[y1][x0] * (1 - fx) * fy +
            grid[y1][x1] * fx * fy)

for y in range(H):
    for x in range(W):
        v = smooth_value(x, y) + (rng.random() - 0.5) * 0.30
        if v < 0.24:
            ci = DARKER
        elif v < 0.40:
            ci = DARK
        elif v < 0.62:
            ci = BASE
        elif v < 0.80:
            ci = LIGHT
        else:
            ci = BRIGHT
        c.set(x, y, ci)

# Fine grain speckles (Minecraft-style mottling)
for _ in range(10):
    c.set(rng.randrange(16), rng.randrange(16), DIM)
for _ in range(6):
    c.set(rng.randrange(16), rng.randrange(16), BRIGHT)

# Wrapped crack rendering: draw each segment plus its copies shifted by
# multiples of 16 so cracks crossing a tile edge continue on the opposite
# side -> seamless tiling.
def wrapped_line(p0, p1, color):
    for sx in (-16, 0, 16):
        for sy in (-16, 0, 16):
            c.line(p0[0] + sx, p0[1] + sy, p1[0] + sx, p1[1] + sy, color)

cracks = [
    [(2, 0), (3, 1), (3, 4), (6, 7), (6, 10), (10, 14), (10, 16)],
    [(16, 6), (13, 7), (12, 8), (12, 11), (9, 14), (8, 15)],
    [(6, 7), (7, 6), (10, 5), (12, 5), (13, 4)],
    [(3, 4), (5, 3), (5, 1)],
]

for poly in cracks:
    for i in range(len(poly) - 1):
        wrapped_line(poly[i], poly[i + 1], CRACK)

# Darken alternating crack points for depth
for poly in cracks:
    for i in range(1, len(poly) - 1, 2):
        px, py = poly[i]
        c.set((px + 16) % 16, (py + 16) % 16, CORE)

print(c.stats_text())

# Tiled 2x2 preview to check seamless edges
import pixelbench_api as api
tile = new_canvas(32, 32, name="tile_check")
for ty in range(2):
    for tx in range(2):
        tile.blit(c, tx * 16, ty * 16)
pal = {i: p["rgba"] for i, p in enumerate(tile.palette())}

# Compact luminance preview of the tiled texture
def ch(i):
    lum = pal[i][0] + pal[i][1] + pal[i][2]
    if lum < 200:   return "#"
    if lum < 320:   return "+"
    if lum < 420:   return "."
    if lum < 490:   return ","
    return " "
for yy in range(32):
    print("".join(ch(tile.get(xx, yy)) for xx in range(32)))
finish(c)
