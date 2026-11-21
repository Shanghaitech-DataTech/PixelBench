from pixelbench_api import *

# 64x64 neighborhood laundromat, built from a small cool industrial palette.
c = new_canvas(64, 64, background="#111b25", name="neighborhood_laundromat")

# Palette
ink = "#111b25"
ink2 = "#1b2934"
wall = "#344852"
tile = "#49616a"
tile_hi = "#617981"
metal = "#aabcc0"
metal_hi = "#d3e1df"
metal_shadow = "#71878d"
steel_dark = "#526a72"
blackglass = "#172934"
glass = "#315765"
glass_hi = "#6da0a4"
blue = "#7fc4c5"
white = "#e4f0ec"
yellow = "#e5d58b"
red = "#c96e6b"
orange = "#d49462"
floor = "#293d48"
floor_hi = "#405963"
wood = "#806e5e"
wood_hi = "#b39b7c"
basket = "#b77f54"
basket_hi = "#d0a06b"

# Back wall and tiled structure
c.rect(3, 3, 58, 43, wall)
c.rect(3, 3, 58, 3, tile_hi)
c.rect(3, 6, 58, 1, tile)
# tile seams, kept soft behind the machinery
for x in (15, 27, 39, 51):
    c.rect(x, 7, 1, 39, tile)
for y in (12, 23, 34, 45):
    c.rect(3, y, 58, 1, tile)
# cool light cast on upper wall
c.rect(4, 7, 56, 2, "#7f9899")
c.rect(4, 9, 56, 1, "#607b80")

# Ceiling light fixtures
for x in (10, 32, 54):
    c.rect(x-4, 4, 8, 1, ink2)
    c.rect(x-3, 5, 6, 1, white)
    c.rect(x-2, 6, 4, 1, "#b9d9d6")

# Wall clock, centered at top
c.rect(28, 7, 8, 1, ink)
c.rect(27, 8, 10, 7, ink)
c.rect(28, 8, 8, 7, metal_shadow)
c.rect(29, 9, 6, 5, "#c5d9d4")
c.rect(30, 10, 4, 3, "#20343d")
c.rect(32, 10, 1, 2, white)
c.rect(31, 12, 2, 1, ink)
c.rect(28, 14, 8, 1, ink)

# A tiny service sign and vent
c.rect(5, 8, 9, 3, ink2)
c.rect(6, 9, 7, 1, blue)
c.rect(7, 10, 5, 1, "#90adae")
c.rect(54, 8, 5, 5, ink2)
for yy in (9, 11):
    c.rect(55, yy, 3, 1, tile_hi)

# Reusable front-loading machine, each outlined and separated by wall gaps.
def machine(x, y, w=10, h=15, lower=False):
    # dark footprint and outer shell
    c.rect(x+1, y+1, w, h, ink)
    c.rect(x, y, w, h, metal_shadow)
    c.rect(x+1, y, w-2, 1, metal_hi)
    c.rect(x+1, y+1, w-2, 2, metal)
    # control panel
    c.rect(x+1, y+3, w-2, 2, steel_dark)
    c.rect(x+2, y+3, 3, 1, metal_hi)
    c.rect(x+6, y+3, 1, 1, blue)
    c.rect(x+7, y+3, 1, 1, yellow)
    # lower cabinet and loading door
    cx = x + w//2
    cy = y + 10 if not lower else y + 9
    rr = 4 if w >= 10 else 3
    c.rect(x+1, y+5, w-2, h-6, metal)
    c.circle(cx, cy, rr+1, ink)
    c.circle(cx, cy, rr, blackglass)
    c.circle(cx, cy, rr-1, glass)
    # square glint across glass, pixel sharp
    c.rect(cx-rr+1, cy-rr+1, 2, 1, glass_hi)
    c.rect(cx-rr+1, cy-rr+2, 1, 1, blue)
    # door rim highlight and latch
    c.line(cx-rr-1, cy+rr-1, cx-rr, cy+rr, metal_hi)
    c.rect(x+w-3, y+6, 1, 2, ink2)
    c.rect(x+2, y+h-2, w-4, 1, metal_shadow)

# Upper bank: five compact machines, with one-pixel gaps and bold dark divisions.
for x in (5, 17, 29, 41, 53):
    machine(x, 15, 10, 15, False)

# Labels beneath top row give the appliance wall a lived-in retail feel.
for x in (6, 18, 30, 42, 54):
    c.rect(x, 29, 2, 1, ink2)
    c.rect(x+3, 29, 1, 1, red)

# Lower bank, slightly bigger machines with a strong counter edge.
c.rect(4, 31, 56, 2, ink)
for x in (5, 17, 29, 41, 53):
    machine(x, 33, 10, 16, True)

# Make lower door placement varied but consistent enough to feel hand-built.
for x in (5, 17, 29, 41, 53):
    c.rect(x+2, 47, 6, 1, metal_hi)
    c.rect(x+4, 48, 2, 1, ink2)

# Floor plane
c.rect(3, 49, 58, 12, floor)
c.rect(3, 49, 58, 2, floor_hi)
c.rect(3, 51, 58, 1, ink2)
# floor tile perspective seams
for x in (15, 27, 39, 51):
    c.line(x, 52, x-3, 60, floor_hi)
for y in (55, 59):
    c.line(3, y, 61, y, floor_hi)
c.rect(3, 60, 58, 1, ink)

# Folding table in foreground left: top, legs, and folded towels.
c.rect(7, 48, 23, 2, ink)
c.rect(8, 47, 21, 2, wood)
c.rect(9, 46, 19, 1, wood_hi)
c.rect(10, 47, 17, 1, wood_hi)
c.rect(10, 49, 2, 10, ink2)
c.rect(25, 49, 2, 10, ink2)
c.rect(9, 58, 4, 1, ink)
c.rect(24, 58, 4, 1, ink)
# folded laundry stack
c.rect(13, 43, 10, 1, ink)
c.rect(12, 44, 11, 2, white)
c.rect(13, 43, 9, 1, "#aac9c3")
c.rect(14, 42, 8, 1, blue)
c.rect(15, 41, 6, 1, white)
c.rect(15, 45, 8, 1, "#b9d7d1")

# Laundry basket at lower right, with visible weave and handles.
c.rect(43, 52, 13, 2, ink)
c.rect(44, 53, 11, 8, ink)
c.poly([(44,53),(55,53),(53,61),(46,61)], basket)
c.rect(45, 54, 9, 1, basket_hi)
c.rect(45, 56, 8, 1, basket_hi)
c.rect(46, 58, 7, 1, basket_hi)
c.rect(47, 60, 5, 1, basket_hi)
c.line(46, 53, 47, 60, basket_hi)
c.line(52, 53, 51, 60, basket_hi)
# handles and a pale towel peeking out
c.line(46, 53, 47, 50, ink)
c.line(47, 50, 52, 50, ink)
c.line(52, 50, 53, 53, ink)
c.rect(46, 51, 7, 2, white)
c.rect(48, 50, 4, 1, blue)

# Small wall notice tucked between rows
c.rect(34, 28, 7, 3, ink)
c.rect(35, 29, 5, 1, white)
c.rect(35, 30, 3, 1, yellow)

# Crisp edge accents and a few floor reflections
c.rect(4, 62, 56, 1, ink2)
c.rect(16, 52, 5, 1, "#54727a")
c.rect(31, 52, 5, 1, "#54727a")
c.rect(56, 53, 3, 1, "#54727a")

print(c.stats_text())
view(c)
finish(c)
