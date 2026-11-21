from pixelbench_api import *
import math

# Main 64x64 output canvas, transparent background.
c = new_canvas(64, 64, background=None, name="weapons")

# ---- palette (one coherent set for all four weapons) ----
OUTLINE = c.color("#1c1824", name="outline")
STEEL_HI = c.color("#e8eef4", name="steel_hi")
STEEL = c.color("#b8c4d4", name="steel")
STEEL_LO = c.color("#7c8ca0", name="steel_lo")
GOLD = c.color("#e8b84c", name="gold")
GOLD_LO = c.color("#c89430", name="gold_lo")
BROWN = c.color("#9c6234", name="brown")
BROWN_LO = c.color("#6e4220", name="brown_lo")
BLUE = c.color("#4a6cac", name="blue")
BLUE_LO = c.color("#38507f", name="blue_lo")

# ----------------------------------------------------------------------
# SWORD  (top-left cell)
# ----------------------------------------------------------------------
sword = new_canvas(32, 32, name="sword")

# blade
sword.poly([(15, 2), (16, 2), (19, 6), (19, 19), (12, 19), (12, 6)], STEEL)
# symmetric shading: dark edges, bright fuller, mid steel between them
sword.rect(13, 6, 1, 13, STEEL_LO)
sword.rect(18, 6, 1, 13, STEEL_LO)
sword.rect(15, 6, 2, 13, STEEL_HI)
# crossguard
sword.rect(9, 19, 14, 3, GOLD)
sword.rect(9, 19, 14, 1, GOLD_LO)
# grip
sword.rect(14, 22, 4, 4, BROWN)
# pommel
sword.circle(15, 28, 2, GOLD)

sword.outline(OUTLINE)

# ----------------------------------------------------------------------
# BOW  (top-right cell)
# ----------------------------------------------------------------------
bow = new_canvas(32, 32, name="bow")

# string (drawn first; the outline pass keeps it dark)
bow.line(9, 4, 9, 28, STEEL)

# bow stave: a crescent band, filled row by row for exact thickness.
cx, cy, ry = 9, 16, 12
rx_outer, rx_inner = 14, 10
for y in range(4, 29):
    dy = y - cy
    ratio = dy / ry
    if abs(ratio) > 1.0:
        continue
    t = math.sqrt(max(0.0, 1.0 - ratio * ratio))
    xo = cx + rx_outer * t
    xi = cx + rx_inner * t
    x0 = int(round(xi))
    x1 = int(round(xo))
    for x in range(x0, x1 + 1):
        bow.set(x, y, STEEL)

# grip wrap at the middle of the stave
bow.rect(20, 14, 3, 4, BROWN)

bow.outline(OUTLINE)

# ----------------------------------------------------------------------
# SHIELD  (bottom-left cell)
# ----------------------------------------------------------------------
shield = new_canvas(32, 32, name="shield")

# symmetric heater-shield rows: (y, left_x, right_x), centred on x=15.5
shield_rows = [
    (5, 8, 23), (6, 8, 23), (7, 8, 23),
    (8, 9, 22), (9, 9, 22),
    (10, 10, 21), (11, 10, 21),
    (12, 11, 20), (13, 11, 20),
    (14, 12, 19), (15, 12, 19),
    (16, 13, 18), (17, 13, 18),
    (18, 14, 17), (19, 14, 17),
    (20, 15, 16), (21, 15, 16), (22, 15, 16), (23, 15, 16),
]
for y, x0, x1 in shield_rows:
    # gold rim
    shield.rect(x0, y, x1 - x0 + 1, 1, GOLD)
    # blue field, inset by 2 px so a symmetric gold rim survives the outline
    ix0, ix1 = x0 + 2, x1 - 2
    if ix0 <= ix1:
        shield.rect(ix0, y, ix1 - ix0 + 1, 1, BLUE)
        shield.rect(ix0, y, 1, 1, BLUE_LO)

# boss (diamond, centred on the same axis as the shield)
shield.poly([(15, 11), (16, 11), (18, 14), (16, 17), (15, 17), (13, 14)], GOLD)
shield.poly([(15, 12), (16, 12), (17, 14), (16, 16), (15, 16), (14, 14)], GOLD_LO)

shield.outline(OUTLINE)

# ----------------------------------------------------------------------
# BATTLE AXE  (bottom-right cell)
# ----------------------------------------------------------------------
axe = new_canvas(32, 32, name="axe")

# head
axe.poly([(9, 4), (24, 4), (23, 7), (21, 10), (16, 13), (10, 14), (5, 10), (7, 6)], STEEL)
# top highlight
axe.line(9, 4, 24, 4, STEEL_HI)
# shade under the top-right poll
axe.rect(21, 5, 3, 4, STEEL_LO)
# inner highlight along the cutting edge
axe.line(6, 10, 8, 6, STEEL_HI)
axe.line(8, 6, 10, 4, STEEL_HI)

# handle
axe.rect(13, 13, 5, 16, BROWN)
# end cap
axe.rect(12, 29, 7, 2, BROWN_LO)

axe.outline(OUTLINE)

# ----------------------------------------------------------------------
# composite the 2x2 grid
# ----------------------------------------------------------------------
c.blit(sword, 0, 0)
c.blit(bow, 32, 0)
c.blit(shield, 0, 32)
c.blit(axe, 32, 32)

print(c.stats_text())
print("SWORD")
print(sword.matrix_text(indices=False))
print("BOW")
print(bow.matrix_text(indices=False))
print("SHIELD")
print(shield.matrix_text(indices=False))
print("AXE")
print(axe.matrix_text(indices=False))

finish(c)
