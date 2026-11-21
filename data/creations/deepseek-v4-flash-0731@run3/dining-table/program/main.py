from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

# Palette
OUT = (46, 30, 20, 255)      # dark outline
W_D = (94, 60, 32, 255)      # dark wood
WG = (112, 72, 40, 255)      # wood grain
W_M = (130, 86, 48, 255)     # mid wood
W_L = (168, 114, 64, 255)    # light wood
W_HL = (202, 148, 98, 255)   # wood highlight
CUSH = (200, 110, 76, 255)   # warm cushion
PLATE = (246, 238, 216, 255)
PLATE_D = (212, 200, 172, 255)
BOWL = (208, 100, 68, 255)
APPLE = (210, 64, 48, 255)
ORANGE = (246, 146, 46, 255)
BANANA = (252, 206, 86, 255)
LEAF = (108, 152, 68, 255)
LEAF_D = (80, 120, 50, 255)
RUG = (222, 194, 160, 255)
RUG_B = (166, 116, 90, 255)

def rrect(x, y, w, h, r, col):
    r = min(r, (w - 1) // 2, (h - 1) // 2)
    if r > 0:
        c.rect(x + r, y, w - 2 * r, h, col)
        c.rect(x, y + r, w, h - 2 * r, col)
        c.circle(x + r, y + r, r, col)
        c.circle(x + w - 1 - r, y + r, r, col)
        c.circle(x + r, y + h - 1 - r, r, col)
        c.circle(x + w - 1 - r, y + h - 1 - r, r, col)
    else:
        c.rect(x, y, w, h, col)

def chair(back, seat):
    bx, by, bw, bh = back
    rrect(bx, by, bw, bh, 2, OUT)
    rrect(bx + 1, by + 1, bw - 2, bh - 2, 1, W_L)
    sx, sy, sw, sh = seat
    rrect(sx, sy, sw, sh, 2, OUT)
    rrect(sx + 1, sy + 1, sw - 2, sh - 2, 1, CUSH)

# ---- cozy rug under the table ----
rrect(13, 19, 38, 26, 6, RUG_B)
rrect(15, 21, 34, 22, 5, RUG)
c.rect(17, 23, 30, 1, RUG_B)
c.rect(17, 39, 30, 1, RUG_B)
c.rect(17, 22, 1, 20, RUG_B)
c.rect(46, 22, 1, 20, RUG_B)

# ---- four chairs (drawn first so the table tucks neatly between them) ----
chair((28, 3, 8, 11), (26, 13, 12, 8))    # top chair
chair((28, 51, 8, 11), (26, 43, 12, 8))   # bottom chair
chair((1, 26, 8, 12), (9, 25, 8, 14))     # left chair
chair((55, 26, 8, 12), (47, 25, 8, 14))    # right chair
# backrest slats
c.rect(31, 6, 2, 5, W_D)
c.rect(31, 54, 2, 5, W_D)
c.rect(3, 31, 4, 2, W_D)
c.rect(57, 31, 4, 2, W_D)

# ---- wooden table ----
rrect(15, 22, 34, 20, 6, OUT)
rrect(16, 23, 32, 18, 5, W_D)
rrect(17, 24, 30, 16, 4, W_M)
rrect(18, 25, 28, 14, 3, W_L)
# wood grain
c.rect(20, 27, 22, 1, WG)
c.rect(21, 30, 22, 1, WG)
c.rect(20, 33, 22, 1, WG)
c.rect(21, 36, 22, 1, WG)
c.rect(20, 25, 14, 1, W_HL)

# ---- place settings (one in front of each chair) ----
for (px, py) in [(31, 27), (31, 36), (20, 32), (43, 32)]:
    c.circle(px, py, 2, PLATE_D)
    c.circle(px, py, 1, PLATE)

# ---- fruit bowl ----
c.ellipse(32, 31, 3, 2, OUT)
c.ellipse(32, 31, 2, 1, BOWL)
rrect(30, 29, 5, 2, 1, BANANA)
c.circle(31, 31, 1, APPLE)
c.circle(33, 30, 1, ORANGE)
c.circle(33, 32, 1, LEAF)
c.circle(32, 28, 1, LEAF)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=True))
finish(c)
