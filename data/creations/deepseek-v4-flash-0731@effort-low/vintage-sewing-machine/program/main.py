from pixelbench_api import *

c = new_canvas(48, 48)

OUT   = (22, 22, 26)
BODY  = (34, 36, 40)
BODYL = (58, 62, 68)
BODLH = (92, 98, 106)
DARK  = (16, 16, 18)
SILV  = (172, 180, 190)
SILVD = (122, 130, 140)
GOLD  = (216, 182, 86)
GOLDD = (162, 130, 52)
RED   = (212, 56, 48)
REDL  = (240, 128, 116)
FD    = (138, 34, 36)

# ---- base ----
c.rect(4, 40, 40, 1, BODYL)      # top surface
c.rect(4, 41, 40, 3, OUT)       # front face
c.rect(4, 43, 40, 1, DARK)      # bottom shade

# ---- machine body ----
# arm
c.rect(8, 16, 24, 8, BODY)      # x8..31 y16..23
c.rect(8, 16, 24, 1, BODLH)     # arm top highlight
c.rect(8, 16, 2, 8, BODYL)      # head front edge
# pillar (right upright)
c.rect(30, 16, 8, 24, BODY)     # x30..37 y16..39
c.rect(30, 16, 8, 1, BODLH)
# head (left)
c.rect(8, 18, 8, 9, BODY)       # x8..15 y18..26
c.rect(8, 18, 8, 1, BODLH)
# gold filigree on arm
c.line(11, 20, 28, 20, GOLD)
c.line(11, 21, 28, 21, GOLDD)
# gold badge on head
c.circle(11, 23, 2, GOLD)

# ---- handwheel (right end) ----
cx, cy = 37, 14
c.circle(cx, cy, 6, OUT)
c.circle(cx, cy, 5, SILVD)
c.circle(cx, cy, 4, SILV)
c.circle(cx, cy, 2, OUT)
c.line(cx-4, cy, cx+4, cy, GOLD)
c.line(cx, cy-4, cx, cy+4, GOLD)
c.line(cx-3, cy-3, cx+3, cy+3, GOLD)
c.line(cx-3, cy+3, cx+3, cy-3, GOLD)

# ---- needle bar from head down ----
c.rect(13, 27, 2, 6, SILV)      # needle bar y27..32
c.rect(12, 30, 4, 2, BODY)      # clamp block
c.rect(13, 32, 1, 6, SILVD)     # needle to y37

# ---- red fabric (over base, draped) ----
c.poly([(4,47),(4,36),(14,35),(25,36),(36,37),(42,38),(43,46),(33,47),(26,47),(16,47),(8,47)], RED)
# top edge highlight
c.line(5,36,36,37, REDL)
# folds
for x in (9, 15, 21, 28, 35):
    c.line(x, 37, x, 47, FD)
    c.line(x+1, 37, x+1, 46, RED)
    c.line(x-1, 38, x-1, 20, REDL) if False else None
# curl shadows between folds
c.line(12,36,12,47, FD if False else REDL)
c.line(25,36,25,47, FD)
c.line(31,37,31,47, REDL)

# ---- presser foot (over fabric) ----
c.rect(9, 34, 4, 7, SILVD)      # foot stem
c.rect(8, 36, 7, 2, SILV)       # foot body
c.rect(8, 38, 7, 2, OUT)        # sole

# ---- throat plate on base near left ----
c.rect(8, 39, 6, 2, SILVD)

# needle tip into fabric
c.rect(13, 36, 1, 4, OUT)

print(c.stats_text())
finish(c)
