from pixelbench_api import new_canvas, finish

BG  = "#F4F0E8"
TILE = "#FFFFFF"
INK = "#33302C"
BUS = "#3F7CC9"
SUB = "#E34E3A"
BIK = "#3FA55B"
PED = "#E8A33D"


def rrect(ox, oy, x0, y0, x1, y1, r):
    return (
        f"M {ox+x0+r},{oy+y0} H {ox+x1-r} Q {ox+x1},{oy+y0} {ox+x1},{oy+y0+r} "
        f"V {oy+y1-r} Q {ox+x1},{oy+y1} {ox+x1-r},{oy+y1} H {ox+x0+r} "
        f"Q {ox+x0},{oy+y1} {ox+x0},{oy+y1-r} V {oy+y0+r} Q {ox+x0},{oy+y0} {ox+x0+r},{oy+y0} Z"
    )


c = new_canvas(64, 64)
c.rect(0, 0, 64, 64, BG)

# consistent tiles: 24x24 rounded tiles inset 4px in each 32x32 cell
for ox, oy in ((0, 0), (32, 0), (0, 32), (32, 32)):
    c.path(rrect(ox, oy, 4, 4, 27, 27, 3), TILE)

# ---- bus (top-left) ----
c.path(rrect(0, 0, 8, 9, 23, 19, 2), BUS)
c.path(rrect(0, 0, 8, 9, 23, 19, 2), INK, fill=False)
for wx in (9, 13, 17):
    c.rect(wx, 11, 3, 4, TILE)
c.circle(11, 21, 2, INK)
c.circle(21, 21, 2, INK)

# ---- subway (top-right) ----
c.path(rrect(32, 0, 8, 9, 23, 18, 3), SUB)
c.path(rrect(32, 0, 8, 9, 23, 18, 3), INK, fill=False)
c.rect(42, 11, 12, 3, INK)          # dark windshield
c.rect(41, 15, 3, 2, TILE)          # headlight
c.rect(52, 15, 3, 2, TILE)          # headlight

# ---- bicycle (bottom-left) ----
c.circle(10, 22, 3, INK, fill=False)
c.circle(22, 22, 3, INK, fill=False)
for (x0, y0, x1, y1) in (
    (10, 22, 16, 20),   # chainstay
    (16, 20, 22, 22),   # down tube to front
    (13, 14, 16, 20),   # seat tube
    (13, 14, 19, 13),   # top tube
    (19, 13, 22, 22),   # fork
):
    c.line(x0, 32 + y0, x1, 32 + y1, BIK)
c.line(11, 32 + 13, 14, 32 + 13, INK)   # seat
c.line(17, 32 + 12, 20, 32 + 12, INK)   # handlebar
c.line(19, 32 + 12, 19, 32 + 13, INK)   # stem

# ---- pedestrian (bottom-right) ----
c.circle(32 + 16, 32 + 12, 2, PED)      # head
c.rect(32 + 15, 32 + 15, 3, 5, PED)     # torso
c.poly([(32 + 15, 32 + 15), (32 + 17, 32 + 15),
       (32 + 17, 32 + 19), (32 + 15, 32 + 19)], INK, fill=False)
c.line(32 + 15, 32 + 16, 32 + 12, 32 + 17, INK)  # back arm
c.line(32 + 17, 32 + 16, 32 + 20, 32 + 18, INK)  # front arm
c.line(32 + 15, 32 + 19, 32 + 12, 32 + 22, INK)  # back leg
c.line(32 + 16, 32 + 19, 32 + 19, 32 + 23, INK)  # front leg
c.line(32 + 11, 32 + 22, 32 + 13, 32 + 22, INK)  # back foot
c.line(32 + 18, 32 + 23, 32 + 21, 32 + 23, INK)  # front foot

print(c.stats_text())
finish(c)
