"""Public transportation icon set - 64x64, 2x2 grid.

    bus (TL)      subway (TR)
    bicycle (BL)  pedestrian (BR)

Shared design language
  * one dark navy ground, one warm-white ink -> 2 colours total
  * every icon is drawn in a 24x24 field centred in its 32x32 cell, so the
    gutter between icons is identical horizontally and vertically
  * every stroke is exactly 2px: horizontal, vertical and diagonal alike
  * discs use hand-made symmetric half-width tables (the engine circle() is
    lopsided and spiky at these radii)
  * silhouettes get a 1px corner clip where a hard corner would read as a
    bare rectangle edge
  * natural aspect per icon: wide bus, square badge, wide-low bicycle,
    tall-narrow pedestrian, all on a common optical centre
"""

BG = "#151F2B"
FG = "#F2EFE6"

c = new_canvas(64, 64, background=BG, name="icons")
WHITE = c.color(FG)

# ------------------------------------------------------------- span tables
D5 = [1, 2, 2, 2, 1]                                             # 5px disc
D9 = [1, 2, 3, 4, 4, 4, 3, 2, 1]                                 # 9px disc
D15 = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 6, 5, 4, 3, 2, 1]        # 15px disc
D19 = [1, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 1]  # 19px disc


# ---------------------------------------------------------------- primitives
def stroke(x0, y0, x1, y1, col=FG):
    """Exactly 2px-wide straight stroke, stepped along the dominant axis."""
    dx, dy = x1 - x0, y1 - y0
    if abs(dx) >= abs(dy):
        n = abs(dx)
        step = 1 if dx > 0 else -1
        for i in range(n + 1):
            x = x0 + step * i
            y = y0 + int(round(dy * i / float(n))) if n else y0
            c.rect(x, y, 1, 2, col)
    else:
        n = abs(dy)
        step = 1 if dy > 0 else -1
        for i in range(n + 1):
            y = y0 + step * i
            x = x0 + int(round(dx * i / float(n))) if n else x0
            c.rect(x, y, 2, 1, col)


def disc(cx, cy, hbs, col=FG):
    """Symmetric filled disc from a half-width table (dy = index - R)."""
    R = (len(hbs) - 1) // 2
    for i, hb in enumerate(hbs):
        c.rect(cx - hb, cy + i - R, 2 * hb + 1, 1, col)


def ring(cx, cy, outer, inner):
    disc(cx, cy, outer, FG)
    disc(cx, cy, inner, BG)


def frame(x, y, w, h, t=2, col=FG):
    c.rect(x, y, w, t, col)
    c.rect(x, y + h - t, w, t, col)
    c.rect(x, y, t, h, col)
    c.rect(x + w - t, y, t, h, col)


def ease(x, y, w, h, col=BG):
    """Clip the four corners of a box for a softened silhouette."""
    for px, py in ((x, y), (x + w - 1, y), (x, y + h - 1), (x + w - 1, y + h - 1)):
        c.set(px, py, col)


# --------------------------------------------------------------------- icons
def draw_bus(ox, oy):
    """Side view: slab body, three glazed panes, two wheels."""
    c.rect(ox + 2, oy + 3, 20, 12, FG)          # body  x2..21 y3..14
    c.rect(ox + 4, oy + 6, 16, 5, BG)           # glazing y6..10
    c.rect(ox + 8, oy + 6, 2, 5, FG)            # pillar 1
    c.rect(ox + 14, oy + 6, 2, 5, FG)           # pillar 2
    disc(ox + 7, oy + 18, D5, FG)               # wheels y16..20
    disc(ox + 17, oy + 18, D5, FG)
    ease(ox + 2, oy + 3, 20, 12)


def draw_subway(ox, oy):
    """Metro badge: square roundel carrying the letter M."""
    frame(ox + 2, oy + 2, 20, 20)               # badge x2..21 y2..21
    ease(ox + 2, oy + 2, 20, 20)
    c.rect(ox + 6, oy + 6, 2, 11, FG)           # left stem
    c.rect(ox + 16, oy + 6, 2, 11, FG)          # right stem
    for i in range(11):                         # V of the M
        yy = oy + 6 + i
        left = 7 + int(round(4.0 * i / 10.0))
        c.rect(ox + left, yy, 2, 1, FG)
        c.rect(ox + 22 - left, yy, 2, 1, FG)


def draw_bike(ox, oy):
    """Side view: wheels, step-through frame, saddle, handlebar."""
    ring(ox + 5, oy + 15, D9, D5)
    ring(ox + 18, oy + 15, D9, D5)
    stroke(ox + 5, oy + 15, ox + 11, oy + 15)   # chainstay
    stroke(ox + 11, oy + 15, ox + 8, oy + 7)    # seat tube
    stroke(ox + 8, oy + 7, ox + 15, oy + 7)     # top tube
    stroke(ox + 11, oy + 15, ox + 15, oy + 7)   # down tube
    stroke(ox + 15, oy + 7, ox + 18, oy + 15)   # fork
    c.rect(ox + 6, oy + 5, 5, 2, FG)            # saddle
    c.rect(ox + 14, oy + 5, 5, 2, FG)           # handlebar


def draw_ped(ox, oy):
    """Walking pedestrian: head, torso, counter-swinging arms, striding legs."""
    disc(ox + 12, oy + 5, D5, FG)               # head y3..7
    c.rect(ox + 11, oy + 8, 3, 7, FG)           # torso x11..13 y8..14
    stroke(ox + 11, oy + 10, ox + 8, oy + 14)   # back arm
    stroke(ox + 13, oy + 10, ox + 16, oy + 13)  # front arm
    stroke(ox + 12, oy + 14, ox + 9, oy + 20)   # back leg
    stroke(ox + 12, oy + 14, ox + 15, oy + 17)  # front thigh
    stroke(ox + 15, oy + 17, ox + 15, oy + 20)  # front shin
    c.rect(ox + 7, oy + 20, 4, 2, FG)           # back shoe
    c.rect(ox + 14, oy + 20, 4, 2, FG)          # front shoe


draw_bus(4, 4)
draw_subway(36, 4)
draw_bike(4, 36)
draw_ped(36, 36)

print(c.stats_text())
save("transport-icons", c)
finish(c)
