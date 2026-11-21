from pixelbench_api import new_canvas, view, finish

# 16x16 seamless RPG wooden plank material.
c = new_canvas(16, 16, background="#8b512b", name="rpg_wooden_planks")

# Palette: deep grooves, four board bodies, end-grain shades, and restrained grain accents.
groove = "#3a2118"
dark = "#684025"
mid = "#8b512b"
light = "#a96736"
honey = "#bd7a40"
shadow = "#542f20"
hi = "#d08b49"
ink = "#47271a"

# Plank bodies. Grooves sit at x=3,7,11,15 and continue across the tile edge.
c.rect(0, 0, 3, 16, mid)
c.rect(4, 0, 3, 16, light)
c.rect(8, 0, 3, 16, dark)
c.rect(12, 0, 3, 16, honey)
for x in (3, 7, 11, 15):
    c.rect(x, 0, 1, 16, groove)

# Alternating end-grain strips at the repeating top/bottom boundary.
for x, col in [(0, shadow), (1, light), (2, dark), (4, honey), (5, dark), (6, light),
               (8, shadow), (9, mid), (10, light), (12, dark), (13, hi), (14, mid)]:
    c.set(x, 0, col)
    c.set(x, 15, col)
# A few darker end pixels deepen the board ends without making a solid border.
for x in (1, 5, 9, 13):
    c.set(x, 1, shadow)
    c.set(x, 14, shadow)

# Vertical wood-grain runs, broken into pixel-sized segments for a hand-placed look.
for x, ys in [(0, (3,4,5,9,10,11,13)), (2, (2,3,7,8,12,13)),
              (4, (3,4,8,9,10,13)), (6, (2,5,6,11,12)),
              (8, (3,4,7,8,12,13)), (10, (2,3,5,9,10,14)),
              (12, (2,5,6,9,10,13)), (14, (3,4,7,8,11,12))]:
    for y in ys:
        c.set(x, y, hi if x in (1, 5, 9, 13) else honey)

# Shadow-side grain marks give the boards depth.
for x, ys in [(1, (5,6,10,11,12)), (5, (2,7,8,12,13)),
              (9, (4,5,6,10,11)), (13, (3,4,7,8,11,12))]:
    for y in ys:
        c.set(x, y, dark if x != 9 else shadow)

# Small angular knots, each kept inside its plank and surrounded by dark grain.
# Knot 1 on board 1.
c.set(1, 6, ink); c.set(2, 6, ink); c.set(1, 7, dark); c.set(1, 8, ink); c.set(0, 7, shadow)
# Knot 2 on board 3.
c.set(9, 9, ink); c.set(10, 9, ink); c.set(9, 10, shadow); c.set(9, 11, ink); c.set(8, 10, dark)
# Tiny knot on board 4.
c.set(13, 5, ink); c.set(14, 5, shadow); c.set(13, 6, dark); c.set(12, 5, dark)

# Restore the continuous grooves over incidental grain at plank boundaries.
for x in (3, 7, 11, 15):
    c.rect(x, 0, 1, 16, groove)

# Broken horizontal grain accents. Their short stair-steps suggest growth rings
# without creating a visible horizontal tile seam at the top or bottom.
for x, y, seq in [
    (0, 3, [honey, honey, hi]), (4, 5, [hi, honey, honey]),
    (8, 2, [mid, honey, honey]), (12, 8, [hi, honey, honey]),
    (0, 12, [shadow, honey, honey]), (4, 10, [hi, honey]),
    (8, 13, [shadow, honey, honey]), (12, 3, [hi, honey])]:
    for i, col in enumerate(seq):
        if x + i < 15:
            c.set(x + i, y, col)

# Knot highlights and dark cores, deliberately asymmetrical like natural wood.
c.set(0, 7, honey); c.set(1, 6, ink); c.set(2, 6, honey)
c.set(0, 8, shadow); c.set(1, 7, hi); c.set(1, 8, ink); c.set(2, 7, dark)
c.set(8, 10, honey); c.set(9, 9, ink); c.set(10, 9, hi)
c.set(8, 11, shadow); c.set(9, 10, hi); c.set(9, 11, ink); c.set(10, 10, dark)
c.set(12, 5, dark); c.set(13, 5, ink); c.set(14, 5, hi); c.set(13, 6, ink)

# Reassert grooves after all cross-grain accents.
for x in (3, 7, 11, 15):
    c.rect(x, 0, 1, 16, groove)

view(c, scale=24, margin=1)
finish(c)
