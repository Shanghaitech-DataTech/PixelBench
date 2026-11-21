from pixelbench_api import *

W, H = 32, 32
c = new_canvas(W, H, name="leather-spellbook")

# ---- palette: 8 colours ----
outline = "#1a1220"   # dark outline
dark    = "#3f1f2b"   # dark leather / spine shadow
leather = "#7a3743"   # main leather cover
leath2  = "#a85358"   # lit leather
pages   = "#efe2bd"   # page block / metal shine
page2   = "#cdb98a"   # page shadow lines
metal   = "#c3c8d4"   # silver corner brackets
gold    = "#e2b04a"   # gilded medallion, spine bands

# ---- silhouette + 1px dark outline ----
c.rect(3, 3, 26, 26, outline)
c.rect(4, 4, 24, 24, leather)

# ---- spine on the left: dark band, rounded highlight, gold bands ----
c.rect(4, 4, 5, 24, dark)
c.rect(6, 4, 1, 24, leather)
c.rect(4, 8, 5, 1, gold)
c.rect(4, 23, 5, 1, gold)

# ---- fore-edge page block on the right ----
c.rect(25, 4, 3, 1, leather)      # top board
c.rect(25, 27, 3, 1, leather)     # bottom board
c.rect(25, 5, 3, 22, pages)
for y in (8, 12, 16, 20, 24):
    c.rect(25, y, 3, 1, page2)

# ---- cover shading ----
c.rect(9, 5, 16, 1, leath2)       # lit top edge
c.rect(24, 5, 1, 22, dark)        # board edge beside the pages
c.rect(13, 26, 8, 1, dark)        # soft bottom shade

# ---- metal corner brackets ----
def bracket(x, y, sx, sy):
    for i in range(4):
        for t in range(2):
            c.set(x + sx * i, y + sy * t, metal)
            c.set(x + sx * t, y + sy * i, metal)

bracket(9, 5, 1, 1)
bracket(24, 5, -1, 1)
bracket(9, 26, 1, -1)
bracket(24, 26, -1, -1)

# ---- gilded diamond medallion ----
def diamond(cx, cy, r, colour):
    for dy in range(-r, r + 1):
        span = r - abs(dy)
        c.rect(cx - span, cy + dy, 2 * span + 1, 1, colour)

diamond(16, 15, 5, outline)
diamond(16, 15, 4, gold)
for (x, y) in ((16, 11), (15, 12), (14, 13), (13, 14), (12, 15)):
    c.set(x, y, pages)            # upper-left bevel shine

print(c.stats_text())
print(c.matrix_text())
save("leather-spellbook", c, indexed=True)
finish(c)
