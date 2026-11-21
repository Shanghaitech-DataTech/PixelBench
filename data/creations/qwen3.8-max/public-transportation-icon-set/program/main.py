# Public transportation icon set - 64x64, consistent 2x2 grid
# bus (TL) | subway (TR) | bicycle (BL) | pedestrian (BR)

INK    = "#22303C"   # shared line work / outlines (2px weight)
PAPER  = "#EEF3F9"   # tile background
BORDER = "#C9D8E6"   # tile hairline
GLASS  = "#FFFFFF"   # windows / glass
GREY   = "#A7B6C4"   # metal details
AMBER  = "#F2B33D"   # shared secondary accent
BLUE   = "#2F80ED"   # bus body
RED    = "#E2574C"   # subway body
GREEN  = "#22A45D"   # bicycle frame

c = new_canvas(64, 64, name="transit_icons")


# ---------- helpers -------------------------------------------------------
def rrect(x0, y0, x1, y1, r, col, fill=True):
    """Rounded rectangle from inclusive corner (x0,y0) to (x1,y1)."""
    d = ("M %d %d H %d A %d %d 0 0 1 %d %d V %d A %d %d 0 0 1 %d %d H %d "
         "A %d %d 0 0 1 %d %d V %d A %d %d 0 0 1 %d %d Z") % (
             x0 + r, y0, x1 - r, r, r, x1, y0 + r, y1 - r, r, r, x1 - r, y1,
             x0 + r, r, r, x0, y1 - r, y0 + r, r, r, x0 + r, y0)
    c.path(d, col, fill=fill)


def tline(x0, y0, x1, y1, col, w=2):
    """Bresenham line thickened to w pixels, offset across its minor axis."""
    if abs(x1 - x0) >= abs(y1 - y0):
        offs = [(0, i) for i in range(w)]
    else:
        offs = [(i, 0) for i in range(w)]
    for dx, dy in offs:
        c.line(x0 + dx, y0 + dy, x1 + dx, y1 + dy, col)


def tile(ox, oy):
    rrect(ox + 1, oy + 1, ox + 30, oy + 30, 4, PAPER, fill=True)
    rrect(ox + 1, oy + 1, ox + 30, oy + 30, 4, BORDER, fill=False)


# ---------- 1. bus (side view) -------------------------------------------
def bus(ox, oy):
    # wheels behind-ish, drawn first so the body skirt overlaps them
    for wx in (10, 21):
        c.circle(ox + wx, oy + 23, 3, INK)
        c.circle(ox + wx, oy + 23, 1, GREY)
    # body: 2px ink shell + coloured interior
    rrect(ox + 4, oy + 6, ox + 27, oy + 20, 3, INK, fill=True)
    rrect(ox + 6, oy + 8, ox + 25, oy + 18, 2, BLUE, fill=True)
    # window band with 2px mullions
    c.rect(ox + 7, oy + 9, 18, 5, GLASS)
    c.rect(ox + 12, oy + 9, 2, 5, INK)
    c.rect(ox + 18, oy + 9, 2, 5, INK)
    # amber skirt stripe + headlight
    c.rect(ox + 6, oy + 17, 17, 2, AMBER)
    c.rect(ox + 23, oy + 15, 2, 2, GLASS)
    # roof marker
    c.rect(ox + 13, oy + 4, 6, 2, INK)


# ---------- 2. subway / metro (front view) --------------------------------
def subway(ox, oy):
    rrect(ox + 7, oy + 6, ox + 24, oy + 26, 6, INK, fill=True)
    rrect(ox + 9, oy + 8, ox + 22, oy + 24, 4, RED, fill=True)
    # roof unit
    c.rect(ox + 13, oy + 4, 6, 2, INK)
    # route sign
    c.rect(ox + 12, oy + 9, 8, 2, GLASS)
    # windscreen
    rrect(ox + 11, oy + 12, ox + 20, oy + 18, 2, GLASS, fill=True)
    # headlights
    c.rect(ox + 11, oy + 20, 3, 2, AMBER)
    c.rect(ox + 18, oy + 20, 3, 2, AMBER)
    # bumper / skirt
    c.rect(ox + 9, oy + 23, 14, 2, INK)


# ---------- 3. bicycle ----------------------------------------------------
def bicycle(ox, oy):
    # wheels: 2px ink tyres, paper bores
    for wx in (10, 22):
        c.circle(ox + wx, oy + 20, 5, INK)
        c.circle(ox + wx, oy + 20, 3, PAPER)
    A = (10, 20)   # rear hub
    B = (22, 20)   # front hub
    C = (15, 21)   # bottom bracket
    D = (12, 10)   # seat cluster
    E = (20, 10)   # head tube top
    for p, q in ((A, C), (A, D), (C, D), (D, E), (C, E), (E, B)):
        tline(ox + p[0], oy + p[1], ox + q[0], oy + q[1], GREEN, 2)
    # bottom bracket
    c.circle(ox + 15, oy + 21, 1, INK)
    # saddle (amber accent) + handlebar
    c.rect(ox + 9, oy + 8, 6, 2, AMBER)
    tline(ox + 12, oy + 9, ox + 12, oy + 11, GREEN, 2)
    c.rect(ox + 18, oy + 7, 6, 2, INK)
    tline(ox + 20, oy + 8, ox + 20, oy + 11, GREEN, 2)


# ---------- 4. pedestrian -------------------------------------------------
def pedestrian(ox, oy):
    # torso (amber accent)
    c.poly([(ox + 14, oy + 12), (ox + 20, oy + 12),
            (ox + 19, oy + 19), (ox + 15, oy + 19)], AMBER)
    # head
    c.circle(ox + 17, oy + 8, 3, INK)
    # arms
    tline(ox + 18, oy + 13, ox + 23, oy + 16, INK, 2)
    tline(ox + 15, oy + 13, ox + 10, oy + 15, INK, 2)
    # front leg
    tline(ox + 17, oy + 18, ox + 20, oy + 21, INK, 2)
    tline(ox + 20, oy + 21, ox + 21, oy + 25, INK, 2)
    tline(ox + 21, oy + 25, ox + 24, oy + 25, INK, 2)
    # rear leg
    tline(ox + 15, oy + 18, ox + 12, oy + 21, INK, 2)
    tline(ox + 12, oy + 21, ox + 11, oy + 25, INK, 2)
    tline(ox + 11, oy + 25, ox + 8, oy + 25, INK, 2)


# ---------- assemble the grid ---------------------------------------------
tile(0, 0)
tile(32, 0)
tile(0, 32)
tile(32, 32)

bus(0, 0)
subway(32, 0)
bicycle(0, 32)
pedestrian(32, 32)

print(c.stats_text())
save("transit_icons", c)
print(view(c, scale=8, margin=0))
finish(c)
