from pixelbench_api import *

c = new_canvas(64, 64)

OUTLINE = (18, 18, 32)
STEEL = (198, 208, 220)
STEEL_D = (120, 132, 150)
GOLD = (233, 190, 96)
GOLD_D = (176, 136, 44)
WOOD = (150, 104, 58)
WOOD_D = (104, 68, 34)
RED = (198, 58, 52)
RED_D = (138, 36, 32)
BLUE = (82, 128, 214)
WHITE = (240, 240, 244)


def push(pts, d):
    pk = list(pts)
    cx = sum(p[0] for p in pk) / len(pk)
    cy = sum(p[1] for p in pk) / len(pk)
    out = []
    for x, y in pk:
        dx = x - cx
        dy = y - cy
        n = (dx * dx + dy * dy) ** 0.5
        if n < 1e-6:
            out.append((x, y))
        else:
            out.append((x + dx / n * d, y + dy / n * d))
    return out


def ol_poly(pts, col):
    c.poly(push(pts, 1.5), OUTLINE)
    c.poly(pts, col)


def ol_rect(x, y, w, h, col):
    c.rect(x - 1, y - 1, w + 2, h + 2, OUTLINE)
    c.rect(x, y, w, h, col)


# ---------- SWORD (top-left, quadrant 0,0) ----------
ol_poly([(16, 5), (13, 16), (19, 16)], STEEL)
c.rect(15, 16, 2, 1, STEEL_D)          # ricasso
c.line(15, 8, 15, 13, STEEL_D)         # fuller
ol_rect(10, 16, 12, 3, GOLD)           # cross guard
c.rect(11, 17, 10, 1, GOLD_D)
ol_rect(14, 19, 4, 5, WOOD_D)          # grip
ol_rect(13, 24, 6, 3, GOLD)            # pommel
c.ellipse(16, 25, 2, 1, BLUE)          # pommel gem

# ---------- BOW (top-right, quadrant 32,0) ----------
ox, oy = 32, 0
c.path("M%d %d A10 13 0 0 1 %d %d A4 9 0 0 0 %d %d Z" % (ox+16, oy+3, ox+16, oy+29, ox+16, oy+3), OUTLINE)
c.path("M%d %d A9 12 0 0 1 %d %d A5 10 0 0 0 %d %d Z" % (ox+16, oy+4, ox+16, oy+28, ox+16, oy+4), WOOD)
c.circle(ox+16, oy+3, 1, GOLD)          # tip cap
c.circle(ox+16, oy+28, 1, GOLD)         # tip cap
c.line(ox+14, oy+6, ox+14, oy+26, WHITE)  # string
c.rect(ox+20, oy+14, 3, 5, WOOD_D)      # grip wrap

# ---------- SHIELD (bottom-left, quadrant 0,32) ----------
ox, oy = 0, 32
PTS = [(ox+7, oy+13), (ox+9, oy+8), (ox+13, oy+5), (ox+16, oy+4), (ox+19, oy+5),
       (ox+23, oy+8), (ox+25, oy+13), (ox+25, oy+20), (ox+21, oy+25),
       (ox+16, oy+28), (ox+11, oy+25), (ox+7, oy+20)]
c.poly(push(PTS, 2), OUTLINE)
c.poly(PTS, GOLD)
c.poly(push(PTS, -4), RED)
c.rect(ox+15, oy+9, 2, 10, BLUE)
c.rect(ox+11, oy+14, 10, 2, BLUE)
c.rect(ox+20, oy+13, 3, 1, GOLD_D)
c.circle(ox+16, oy+4, 1, GOLD)

# ---------- BATTLE AXE (bottom-right, quadrant 32,32) ----------
ox, oy = 32, 32
ol_rect(ox+15, oy+7, 5, 22, WOOD)
head = [(ox+17, oy+7), (ox+28, oy+8), (ox+30, oy+16), (ox+27, oy+22), (ox+17, oy+20)]
ol_poly(head, STEEL)
c.line(ox+27, oy+9, ox+25, oy+20, STEEL_D)
c.line(ox+18, oy+9, ox+26, oy+10, STEEL_D)
c.rect(ox+16, oy+24, 3, 2, STEEL_D)
c.rect(ox+16, oy+26, 3, 2, WOOD_D)

print(c.stats_text())
finish(c)
