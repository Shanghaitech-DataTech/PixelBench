from pixelbench_api import new_canvas, view, finish

# 48x48 vintage mechanical sewing machine on transparency.
c = new_canvas(48, 48, background=None, name="vintage-sewing-machine")

# Palette: restrained enamel, steel, brass, wood and cloth tones.
outline = "#17181b"
deep = "#202629"
black = "#292d2d"
mid = "#3b4442"
light = "#66706a"
glint = "#9aa39a"
brass_dark = "#765121"
brass = "#b88432"
gold = "#d9aa52"
pale_gold = "#f0cf7a"
steel_dark = "#525b5e"
steel = "#a9b0ad"
steel_hi = "#e2dfcf"
wood_dark = "#49281d"
wood = "#75442c"
wood_hi = "#a8653b"
red_dark = "#7e1f25"
red = "#bd3033"
red_hi = "#e7554f"

# Ground/contact shadow, sparse and pixel-clean.
c.rect(7, 43, 35, 2, "#17181b66")
c.rect(12, 45, 25, 1, "#17181b33")

# Wooden plinth in slight three-quarter perspective.
c.poly([(4, 36), (37, 35), (44, 39), (11, 42)], outline)
c.poly([(6, 36), (36, 36), (41, 38), (10, 40)], wood_hi)
c.poly([(10, 40), (41, 38), (41, 42), (11, 45), (5, 41), (5, 37)], wood_dark)
c.poly([(8, 38), (39, 37), (41, 39), (10, 42), (6, 40)], wood)
c.line(11, 42, 40, 39, "#a76a3e")
c.rect(9, 42, 4, 2, outline)
c.rect(36, 40, 4, 3, outline)
c.set(10, 42, brass)
c.set(37, 40, brass)

# Iron bed plate above the plinth.
c.poly([(8, 33), (35, 32), (40, 35), (12, 38), (7, 36)], outline)
c.poly([(9, 33), (34, 33), (37, 35), (12, 37), (8, 35)], mid)
c.line(12, 36, 36, 34, light)
c.rect(17, 33, 12, 2, steel_dark)
c.line(18, 33, 28, 33, steel)
c.set(29, 34, glint)

# Main pillar at right: broad, weighty vintage casting.
c.poly([(31, 13), (37, 14), (39, 18), (38, 31), (35, 34), (29, 33),
        (31, 29), (32, 20)], outline)
c.poly([(32, 15), (35, 15), (37, 18), (36, 29), (34, 32), (30, 32),
        (33, 28), (33, 19)], deep)
c.poly([(35, 16), (37, 18), (36, 28), (34, 30), (35, 20)], mid)
c.line(36, 19, 35, 27, light)
c.set(35, 18, glint)

# Upper arm, subtly receding toward the pillar.
c.poly([(10, 10), (31, 11), (36, 14), (34, 19), (17, 18), (15, 22),
        (10, 21), (8, 17)], outline)
c.poly([(11, 11), (30, 12), (34, 14), (33, 17), (16, 16), (14, 20),
        (10, 19), (9, 16)], deep)
c.poly([(12, 12), (29, 13), (32, 14), (31, 15), (14, 14)], mid)
c.line(13, 12, 27, 13, light)
c.set(11, 13, glint)
c.set(30, 14, glint)

# Rounded front head and face plate.
c.poly([(8, 15), (14, 15), (17, 18), (16, 27), (14, 30), (9, 29),
        (7, 26), (7, 18)], outline)
c.poly([(9, 16), (13, 16), (15, 18), (14, 26), (13, 28), (9, 27),
        (8, 25), (8, 18)], black)
c.rect(9, 18, 2, 7, mid)
c.line(9, 18, 9, 24, light)
c.set(10, 17, glint)
c.rect(13, 19, 2, 7, brass_dark)
c.line(14, 20, 14, 24, gold)

# Gold filigree and maker medallion on the arm.
c.line(17, 15, 28, 16, brass_dark)
c.set(18, 15, gold); c.set(21, 16, gold); c.set(26, 16, gold)
c.line(22, 13, 25, 13, brass)
c.rect(23, 15, 3, 3, brass_dark)
c.set(24, 15, pale_gold); c.set(24, 16, gold)
c.set(17, 17, brass); c.set(28, 17, brass)
# Decorative curl on pillar.
c.line(32, 22, 35, 21, brass_dark)
c.line(32, 23, 34, 25, brass)
c.set(33, 24, gold); c.set(35, 20, gold)

# Large handwheel behind/right of pillar.
c.circle(39, 18, 7, outline, fill=True)
c.circle(39, 18, 5, brass_dark, fill=True)
c.circle(39, 18, 4, deep, fill=True)
# spokes and hub
c.line(39, 14, 39, 22, brass)
c.line(35, 18, 43, 18, brass)
c.line(36, 15, 42, 21, brass_dark)
c.line(42, 15, 36, 21, brass_dark)
c.circle(39, 18, 2, gold, fill=True)
c.set(39, 18, pale_gold)
c.set(44, 15, outline); c.set(45, 14, brass); c.set(45, 15, gold)

# Reassert pillar edge where it overlaps wheel.
c.line(36, 17, 36, 29, outline)
c.line(35, 18, 35, 27, light)

# Needle bar and fittings.
c.rect(11, 27, 4, 2, outline)
c.rect(12, 27, 2, 7, steel_dark)
c.rect(13, 28, 1, 6, steel)
c.set(13, 30, steel_hi)
c.line(13, 33, 13, 37, steel_hi)
c.set(13, 36, outline)
# Presser foot.
c.rect(11, 35, 3, 1, steel)
c.line(11, 36, 15, 36, outline)
c.set(15, 35, steel_hi)

# Tension dial and thread guide details.
c.circle(8, 22, 2, brass_dark, fill=True)
c.set(8, 21, gold); c.set(9, 22, pale_gold)
c.line(8, 13, 8, 10, steel)
c.line(8, 10, 12, 10, steel_dark)
c.set(8, 9, steel_hi)
c.line(9, 10, 12, 15, "#d7d2b8")

# Red fabric flowing under presser foot and off the front-left edge.
c.poly([(10, 34), (24, 34), (27, 36), (20, 38), (8, 39), (5, 37)], red_dark)
c.poly([(11, 34), (23, 34), (25, 36), (18, 37), (7, 38), (6, 36)], red)
c.line(8, 36, 22, 35, red_hi)
c.set(9, 37, red_hi); c.set(18, 36, "#f06a5f")
# Stitches immediately behind the foot.
c.set(15, 35, pale_gold); c.set(17, 35, pale_gold); c.set(19, 35, pale_gold)

# Small highlights and casting bolts.
c.set(31, 30, glint); c.set(34, 31, brass)
c.set(30, 32, outline); c.set(37, 32, outline)
c.set(10, 28, light); c.set(15, 25, glint)

view(c, scale=10, margin=0)
finish(c)
