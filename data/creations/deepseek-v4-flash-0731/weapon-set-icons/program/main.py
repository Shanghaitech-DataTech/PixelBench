import math
from pixelbench_api import new_canvas, finish

OUT    = "#17191e"
STEEL  = "#b7c2cd"
STEEL_L = "#e4ebf1"
STEEL_D = "#7c8a97"
GOLD  = "#e9b84d"
WOOD  = "#8c5a32"
WOOD_D = "#5b3a1e"
LEA   = "#7a4230"
LEA_D = "#4c2a1c"
BLU   = "#3c68b6"
BLU_D = "#26477a"

c = new_canvas(64, 64)

def out_poly(ox, oy, pts, fill):
    p = [(ox + x, oy + y) for (x, y) in pts]
    c.poly(p, fill, fill=True)
    c.poly(p, OUT, fill=False)

def out_rect(ox, oy, x, y, w, h, fill):
    c.rect(ox + x, oy + y, w, h, fill)
    c.rect(ox + x, oy + y, w, h, OUT, fill=False)

def out_circ(ox, oy, x, y, r, fill):
    c.circle(ox + x, oy + y, r, fill)
    c.circle(ox + x, oy + y, r, OUT, fill=False)

def arc_pts(cx, cy, r, a0, a1, n=12):
    pts = []
    for i in range(n + 1):
        t = a0 + (a1 - a0) * i / n
        pts.append((round(cx + r * math.cos(t)), round(cy + r * math.sin(t))))
    return pts

# ================= SWORD  (top-left) =================
out_poly(0, 0, [(16,4),(18,13),(18,17),(14,17),(14,13)], STEEL)
c.line(16, 6, 16, 13, STEEL_L)
c.line(15, 14, 15, 16, STEEL_D)
c.line(17, 14, 17, 16, STEEL_D)
out_rect(0, 0, 10, 18, 12, 3, GOLD)
out_rect(0, 0, 14, 21, 4, 5, WOOD)
c.line(14, 23, 17, 23, WOOD_D)
c.line(14, 25, 17, 25, WOOD_D)
out_circ(0, 0, 16, 27, 2, GOLD)

# ================= BOW  (top-right) =================
o  = 32
bow_bot = arc_pts(16, 16, 10, math.radians(90), math.radians(270), 14)   # bottom->left->top
bow_top = list(reversed(arc_pts(16, 16, 7, math.radians(90), math.radians(270), 14)))
limb = [(o + x, y) for x, y in (bow_bot + bow_top)]
c.poly(limb, WOOD, fill=True)
c.poly(limb, OUT, fill=False)
c.line(o + 17, 5, o + 17, 27, OUT)              # string
out_rect(o, 0, 14, 14, 5, 5, LEA)               # leather grip
c.line(o + 15, 15, o + 15, 17, LEA_D)
# arrow pointing left, nocked
c.line(o + 3, 16, o + 16, 16, STEEL)
tri = [(o + 1, 16), (o + 6, 13), (o + 6, 19)]
c.poly(tri, STEEL)
c.poly(tri, OUT, fill=False)

# ================= SHIELD  (bottom-left) =================
c.poly([(8,38),(23,38),(26,44),(26,48),(16,61),(5,48),(5,44)], OUT)
c.poly([(9,40),(22,40),(24,45),(24,47),(16,59),(7,47),(7,45)], BLU)
c.poly([(11,42),(20,42),(22,45),(22,46),(16,57),(9,46),(9,45)], BLU_D)
out_circ(0, 0, 16, 49, 2, GOLD)

# ================= AXE  (bottom-right) =================
o  = 32
oy = 32
out_rect(o, oy, 15, 13, 3, 16, WOOD)
c.line(o + 15, oy + 22, o + 17, oy + 22, WOOD_D)
c.line(o + 15, oy + 25, o + 17, oy + 25, WOOD_D)
out_circ(o, oy, 16, 29, 2, GOLD)
head = [(7,7),(24,7),(26,11),(22,13),(16,11),(15,11),(9,13),(5,11)]
c.poly([(o + x, oy + y) for x, y in head], STEEL)
c.poly([(o + x, oy + y) for x, y in head], OUT, fill=False)
c.line(o + 8, oy + 8, o + 23, oy + 8, STEEL_L)

print(c.stats_text())
for label, reg in [("SWORD", (0, 0, 31, 31)),
                 ("BOW", (32, 0, 63, 31)),
                 ("SHIELD", (0, 32, 31, 63)),
                 ("AXE", (32, 32, 63, 63))]:
    print("=====", label, "=====")
    print(c.matrix_text(region=reg, indices=False))

finish(c)
