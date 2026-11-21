# 32x32 seamless warm carpet tile
result = new_canvas(32, 32, background="#35151b", name="seamless_carpet")

# Compact wool palette.
base = "#35151b"
base2 = "#421b20"
base3 = "#512126"
ink = "#241014"
red = "#7a2f2b"
red_hi = "#a94735"
terracotta = "#c5653d"
gold = "#d99345"
gold_hi = "#efb95d"
cream = "#f1d18a"
olive = "#6f6531"
olive_hi = "#9a853d"

# Periodic woven ground: tiny alternating warp/weft flecks.
for y in range(32):
    for x in range(32):
        if (x + 2*y) % 8 == 0:
            result.set(x, y, base3)
        elif (x - y) % 8 == 4:
            result.set(x, y, base2)

# Broken horizontal yarn ribs, all phase-periodic at 32px.
for y in (1, 8, 23, 30):
    for x in range(0, 32, 4):
        result.rect(x, y, 2, 1, red)
for y in (2, 29):
    for x in range(2, 32, 4):
        result.set(x, y, gold)

# Wrapped pixel helper for motifs crossing the tile boundary.
def p(x, y, colour):
    result.set(x % 32, y % 32, colour)

def wrapped_flower(cx, cy):
    # Dark shadow, four warm petals, gold heart, olive diagonal leaves.
    for dx, dy in ((0,-2),(-2,0),(2,0),(0,2)):
        p(cx+dx, cy+dy, ink)
    for dx, dy in ((0,-1),(-1,0),(1,0),(0,1)):
        p(cx+dx, cy+dy, terracotta)
    for dx, dy in ((-2,-2),(2,-2),(-2,2),(2,2)):
        p(cx+dx, cy+dy, olive)
    p(cx, cy, gold_hi)

# Floral border ornaments repeat cleanly over every edge and corner.
for cx in (0, 8, 24):
    wrapped_flower(cx, 0)
    wrapped_flower(cx, 32)
for cy in (8, 24):
    wrapped_flower(0, cy)
    wrapped_flower(32, cy)

# Paired border vines and inward-facing leaves.
for x in range(4, 32, 8):
    p(x, 3, olive_hi); p(x+1, 4, olive)
    p(x, 28, olive_hi); p(x-1, 27, olive)
for y in range(4, 32, 8):
    p(3, y, olive_hi); p(4, y+1, olive)
    p(28, y, olive_hi); p(27, y-1, olive)

# Central stepped diamond medallion: dark selvedge, red field, golden bands.
result.poly([(16,4),(28,16),(16,28),(4,16)], ink)
result.poly([(16,5),(27,16),(16,27),(5,16)], red)
# Pixel stair highlights along the four sloped edges.
for i in range(1, 10, 2):
    p(16-i, 5+i, red_hi); p(16+i, 5+i, terracotta)
    p(16-i, 27-i, terracotta); p(16+i, 27-i, red_hi)
result.poly([(16,8),(24,16),(16,24),(8,16)], gold)
result.poly([(16,10),(22,16),(16,22),(10,16)], base3)
result.poly([(16,12),(20,16),(16,20),(12,16)], cream)
result.poly([(16,13),(19,16),(16,19),(13,16)], terracotta)

# Floral rosette at the heart, with leaf tips aligned to the diamond axes.
for dx, dy in ((0,-2),(-2,0),(2,0),(0,2)):
    p(16+dx, 16+dy, gold_hi)
for dx, dy in ((-1,-1),(1,-1),(-1,1),(1,1)):
    p(16+dx, 16+dy, red_hi)
p(16,16,cream)

# Small knotted accents in the red corners of the medallion.
for cx, cy in ((16,7),(25,16),(16,25),(7,16)):
    p(cx,cy,cream)
    if cx == 16:
        p(cx-1,cy,olive_hi); p(cx+1,cy,olive_hi)
    else:
        p(cx,cy-1,olive_hi); p(cx,cy+1,olive_hi)

# Single-pixel loom glints keep the surfaces visibly woven, not flat.
for x, y in ((11,9),(20,9),(9,11),(22,11),(9,20),(22,20),(11,22),(20,22)):
    p(x,y,gold_hi)

finish(result)
