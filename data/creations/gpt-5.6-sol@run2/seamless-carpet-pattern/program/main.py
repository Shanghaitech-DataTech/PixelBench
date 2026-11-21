from pixelbench_api import new_canvas, view, finish

# 32x32 periodic woven carpet tile
c = new_canvas(32, 32, background="#5a1f2a", name="carpet_tile")

# Warm woven ground and inset field
c.rect(2, 2, 28, 28, "#8f3f35")
c.rect(4, 4, 24, 24, "#b85c3f")

# Subtle woven checker texture, clipped to the field
for y in range(4, 28, 2):
    for x in range(4, 28, 2):
        if ((x // 2 + y // 2) % 2) == 0:
            c.rect(x, y, 1, 1, "#c56a47")
        else:
            c.rect(x + 1, y + 1, 1, 1, "#9e493b")

# Repeating dark/gold stepped border; all coordinates wrap naturally at 32.
border_dark = "#6b2630"
border_gold = "#e6a24b"
for x in range(0, 32, 8):
    c.rect(x, 0, 4, 1, border_dark)
    c.rect(x + 4, 0, 4, 1, border_gold)
    c.rect(x, 31, 4, 1, border_dark)
    c.rect(x + 4, 31, 4, 1, border_gold)
for y in range(0, 32, 8):
    c.rect(0, y, 1, 4, border_dark)
    c.rect(0, y + 4, 1, 4, border_gold)
    c.rect(31, y, 1, 4, border_dark)
    c.rect(31, y + 4, 1, 4, border_gold)

# Inner floral border: four-petal rosettes repeat every 8 pixels.
petal = "#f0c15b"
petal_shadow = "#d47b3e"
center = "#702631"
for cy in (3, 11, 19, 27):
    for cx in (3, 11, 19, 27):
        c.set(cx, cy, center)
        c.set(cx - 1, cy, petal)
        c.set(cx + 1, cy, petal)
        c.set(cx, cy - 1, petal)
        c.set(cx, cy + 1, petal)
        c.set(cx - 1, cy - 1, petal_shadow)
        c.set(cx + 1, cy + 1, petal_shadow)

# Four large interlocking diamonds, centered on a 16px lattice.
def diamond(cx, cy):
    outline = "#672631"
    mid = "#d98343"
    light = "#f0b34f"
    deep = "#8d3335"
    c.poly([(cx, cy-6), (cx+6, cy), (cx, cy+6), (cx-6, cy)], outline)
    c.poly([(cx, cy-5), (cx+5, cy), (cx, cy+5), (cx-5, cy)], mid)
    c.poly([(cx, cy-3), (cx+3, cy), (cx, cy+3), (cx-3, cy)], light)
    c.poly([(cx, cy-1), (cx+1, cy), (cx, cy+1), (cx-1, cy)], deep)
    # tiny cardinal woven accents
    c.set(cx, cy-7, light)
    c.set(cx, cy+7, light)
    c.set(cx-7, cy, light)
    c.set(cx+7, cy, light)

for cy in (8, 24):
    for cx in (8, 24):
        diamond(cx, cy)

# Small vine diamonds between the larger medallions.
vine = "#e6a24b"
vine_dark = "#7b2b31"
for cx, cy in ((16, 8), (8, 16), (24, 16), (16, 24)):
    c.poly([(cx, cy-3), (cx+3, cy), (cx, cy+3), (cx-3, cy)], vine_dark)
    c.poly([(cx, cy-2), (cx+2, cy), (cx, cy+2), (cx-2, cy)], vine)
    c.set(cx, cy, "#f4c65d")

# Corner/edge running-stitch marks, periodic on every side.
stitch = "#f1bd58"
for p in (6, 14, 22, 30):
    c.set(p, 2, stitch); c.set(p, 29, stitch)
    c.set(2, p, stitch); c.set(29, p, stitch)

# A few dark joints make the woven structure read crisply at 32px.
for p in (7, 15, 23, 31):
    c.set(p, 1, border_dark); c.set(p, 30, border_dark)
    c.set(1, p, border_dark); c.set(30, p, border_dark)

# Clear four-petal flowers on the inner perimeter, repeating across tile edges.
for cx in (7, 15, 23):
    for cy in (3, 28):
        c.set(cx, cy, center)
        c.set(cx-1, cy, petal); c.set(cx+1, cy, petal)
        c.set(cx, cy-1, petal); c.set(cx, cy+1, petal)
for cy in (7, 15, 23, 31):
    for cx in (3, 28):
        c.set(cx, cy, center)
        c.set(cx-1, cy, petal); c.set(cx+1, cy, petal)
        c.set(cx, cy-1, petal); c.set(cx, cy+1, petal)

view(c, scale=16, margin=0)
finish(c)
