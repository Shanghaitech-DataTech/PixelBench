c = new_canvas(64, 64)

OUTLINE = (30, 30, 38)
INNER   = (238, 238, 238)
GREEN   = (70, 210, 90)
YELLOW  = (246, 205, 58)
RED     = (232, 66, 46)
AMBER   = (255, 168, 44)
BOLT    = (40, 40, 52)

def battery(bx, by, frac, color, label, bolt=False):
    # terminal nub on top
    c.rect(bx + 4, by - 4, 4, 4, OUTLINE)
    # body outline
    c.rect(bx, by, 12, 24, OUTLINE)
    # light interior
    c.rect(bx + 1, by + 1, 10, 22, INNER)
    # fill level from the bottom
    fh = round(22 * frac)
    if fh > 0:
        c.rect(bx + 1, by + 1 + 22 - fh, 10, fh, color)
    if bolt:
        ix, iy = bx + 1, by + 1
        pts = [
            (ix + 6, iy + 1),
            (ix + 2, iy + 12),
            (ix + 4, iy + 12),
            (ix + 2, iy + 21),
            (ix + 8, iy + 10),
            (ix + 6, iy + 10),
        ]
        c.poly(pts, BOLT)
    # label under the battery
    txt_w = len(label) * 5 + (len(label) - 1)
    c.text(bx + 6 - txt_w // 2, by + 28, label, color)

battery(2,  22, 1.0, GREEN,  "100")
battery(18, 22, 0.6, YELLOW, "60")
battery(34, 22, 0.2, RED,    "20")
battery(49, 22, 0.6, AMBER,  "CHG", bolt=True)

print(c.stats_text())
finish(c)
