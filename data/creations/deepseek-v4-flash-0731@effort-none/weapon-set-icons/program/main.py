from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="weapon_set")

OUTLINE = "#1a1410"
GRAY = "#b8b8c8"
GRAY_LIGHT = "#e8e8f0"
GOLD = "#d4a83c"
GOLD_LIGHT = "#f0d070"
BROWN = "#8b5a2b"
BROWN_DARK = "#5a3a1a"
RED = "#b02420"
RED_LIGHT = "#e05048"
SILVER = "#c8c8d8"
DARKMETAL = "#5a5a68"
LEATHER = "#7a4a28"
STEEL = "#9a9aaa"
BOW_HI = "#a06b34"

# ============================================================
# SWORD  (0,0)-(31,31)  vertical, blade up
# ============================================================
# blade steel body
c.rect(13, 3, 6, 13, GRAY)
# tip
c.rect(14, 2, 4, 1, GRAY)
c.rect(15, 1, 2, 1, GRAY)
c.rect(14, 1, 1, 1, GRAY)
c.rect(17, 1, 1, 1, GRAY)
# blade highlight (left lighter, right shading)
c.rect(14, 3, 2, 11, SILVER)
c.rect(17, 3, 1, 10, DARKMETAL)
c.rect(14, 2, 1, 1, GRAY_LIGHT)
# blade outline
c.line(13, 3, 13, 15, OUTLINE)
c.line(18, 3, 18, 15, OUTLINE)
c.line(14, 1, 14, 2, OUTLINE)
c.line(17, 1, 17, 2, OUTLINE)
c.line(15, 0, 16, 0, OUTLINE)
c.line(13, 15, 13, 15, OUTLINE)
c.line(18, 15, 18, 15, OUTLINE)
# cross guard
c.rect(8, 16, 16, 3, GOLD)
c.rect(8, 16, 16, 1, GOLD_LIGHT)
c.rect(8, 16, 1, 3, OUTLINE)
c.rect(23, 16, 1, 3, OUTLINE)
c.line(8, 18, 23, 18, OUTLINE)
# grip
c.rect(14, 19, 4, 7, BROWN)
c.rect(14, 19, 1, 7, BROWN_DARK)
c.rect(17, 20, 1, 5, LEATHER)
c.line(14, 19, 17, 19, OUTLINE)
c.line(14, 25, 17, 25, OUTLINE)
# pommel
c.rect(13, 26, 6, 3, GOLD)
c.rect(13, 26, 6, 1, GOLD_LIGHT)
c.rect(13, 26, 1, 3, OUTLINE)
c.rect(18, 26, 1, 3, OUTLINE)
c.line(13, 28, 18, 28, OUTLINE)

# ============================================================
# BOW  (32,0)-(63,31)  vertical bow
# ============================================================
# Center line x=47.5; limbs curve outward.
# Left limb silhouette rows
left_rows = {
    2: [36,37,38],
    3: [35,36,37,38],
    4: [34,35,36,37,39],
    5: [34,35,36,37,39],
    6: [34,35,36,37,38,40],
    7: [34,35,36,37,38,41],
    8: [35,36,37,38,43],
    9: [36,37,38,44],
    10:[37,38,45],
    11:[38,46],
    12:[39,47],
}
# Right limb = mirror of left about x=47.5: x_r = 95-x
# String between inner tips at bottom center.
# Build both limbs
def MR(x):
    return 95 - x

# Fill bow limbs
for y, xs in left_rows.items():
    for x in xs:
        if x < 48:
            c.set(x, y, BROWN)
            c.set(MR(x), y, BROWN)
    # highlight inner face (both limbs for symmetry)
for y, xs in left_rows.items():
    for x in xs[1:-1]:
        c.set(x, y, BOW_HI)
        c.set(MR(x), y, BOW_HI)
# outline each limb outer+inner edges
for y, xs in left_rows.items():
    c.set(min(xs), y, OUTLINE)
    c.set(max(xs), y, OUTLINE)
    c.set(MR(min(xs)), y, OUTLINE)
    c.set(MR(max(xs)), y, OUTLINE)
# tip caps
c.set(36,1,OUTLINE); c.set(37,1,OUTLINE); c.set(38,1,OUTLINE)
c.set(MR(38),1,OUTLINE); c.set(MR(37),1,OUTLINE); c.set(MR(36),1,OUTLINE)
# Bow string: slight inward curve from top-left tip across to top-right tip
# string goes from inner top to inner top
for y in range(2, 13):
    # string slightly curved: s_x moves inward as it descends
    s_x = 38 + (y-2)
    c.set(s_x, y, SILVER)
    c.set(MR(s_x), y, SILVER)
# grip wrap near center
c.rect(40, 13, 15, 4, LEATHER)
c.rect(40, 13, 15, 1, OUTLINE)
c.rect(40, 16, 15, 1, OUTLINE)

# ============================================================
# SHIELD  (0,32)-(31,63)
# ============================================================
# main shield body
c.poly([(7,34),(24,34),(24,50),(16,59),(7,50)], SILVER)
# left shading band
c.line(8,35,8,49,GRAY)
# top rim
c.line(7,34,24,34,OUTLINE)
c.line(7,35,24,35,GRAY)
# outline around body
c.line(7,34,7,50,OUTLINE)
c.line(24,34,24,50,OUTLINE)
c.line(7,50,16,59,OUTLINE)
c.line(24,50,16,59,OUTLINE)
# gold band inner
c.line(9,37,9,48,GOLD)
c.line(22,37,22,48,GOLD)
c.line(9,37,16,41,GOLD)
c.line(22,37,16,41,GOLD)
# bottom gold
c.line(9,48,13,52,GOLD)
c.line(22,48,18,52,GOLD)
# boss
c.circle(16,43,5,GOLD,fill=True)
c.circle(16,43,5,OUTLINE,fill=True)
c.circle(16,43,3,GOLD,fill=False)
c.circle(16,43,2,GOLD_LIGHT,fill=True)
# boss detail notch
c.set(14,43,OUTLINE); c.set(15,43,OUTLINE); c.set(17,43,OUTLINE); c.set(18,43,OUTLINE)
c.set(16,41,OUTLINE); c.set(16,44,OUTLINE)
# rivets
for (rx,ry) in [(8,36),(23,36)]:
    c.set(rx,ry,GOLD_LIGHT)

# ============================================================
# BATTLE AXE  (32,32)-(63,63)  handle right, blade left
# ============================================================
# Handle (vertical, right side)
c.rect(49, 32, 3, 27, BROWN)
c.rect(49, 32, 1, 27, BROWN_DARK)
c.rect(51, 34, 1, 23, LEATHER)
c.rect(49, 32, 3, 1, OUTLINE)
c.rect(49, 58, 3, 1, OUTLINE)
c.rect(49, 32, 1, 28, OUTLINE)
c.rect(51, 33, 1, 27, OUTLINE)
# pommel cap
c.rect(49, 59, 3, 1, GOLD)
c.rect(49, 60, 3, 1, OUTLINE)
# Axe head: steel crescent blade, handle at right x=49-51.
# Blade columns by row (x from left edge to 48, handle inner edge)
blade_rows = {
    35:(41,48), 36:(38,48), 37:(36,48), 38:(35,48), 39:(35,48),
    40:(35,48), 41:(35,48), 42:(35,48), 43:(36,48), 44:(37,48),
    45:(38,48), 46:(40,48), 47:(42,48), 48:(44,48),
}
for y,(x0,x1) in blade_rows.items():
    for x in range(x0, x1+1):
        c.set(x, y, STEEL)
# gleaming curved cutting edge (left swept edge)
c.line(35,38,35,42,GRAY_LIGHT)
c.line(36,36,36,44,SILVER)
# swooping lower edge outline
swoop = [(36,40),(37,41),(38,42),(38,43),(39,44),(40,45),(40,46),(42,47),(44,48)]
for (x,y) in swoop:
    c.set(x,y,OUTLINE)
# top edge outline (arc of head)
for y,(x0,x1) in blade_rows.items():
    if y>=35:
        c.set(x0 if x0>35 else 35, y, OUTLINE)  # will refine below
# precise left edge outline per row
sweep = {38:(34,35),39:(34,35),40:(34,35),41:(34,35),42:(34,35),
         43:(35,36),44:(36,37),45:(37,38),46:(39,40),47:(41,42),48:(43,44)}
for y,(xa,xb) in sweep.items():
    c.set(xa,y,OUTLINE)
    c.set(xb,y,OUTLINE)
# top of head outline
c.line(41,34,49,35,OUTLINE)
for x in range(36,42):
    c.set(x,35,STEEL)
# separation line handle/blade
c.line(49,36,49,47,OUTLINE)
# head shine spot
c.set(40,40,GRAY_LIGHT); c.set(41,40,GRAY_LIGHT)

print(c.stats_text())
finish(c)
