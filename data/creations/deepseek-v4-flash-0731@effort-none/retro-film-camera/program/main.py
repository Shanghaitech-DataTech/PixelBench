from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, background=None, name="camera")

# Palette
OUTLINE = "#0d0d0d"
DARK_LEATHER = "#38281e"
LEATHER = "#4a3626"
LEATHER_LIGHT = "#5a4430"
LEATHER_HI = "#6e5236"
DARK_METAL = "#454545"
METAL = "#666666"
METAL_LIGHT = "#8a8a8a"
METAL_HI = "#b8b8b8"
GLASS = "#22303c"
GLASS_DARK = "#18222c"
GLASS_MID = "#3a5268"
GLASS_HI = "#a0c8e8"
SHUTTER = "#b03020"
SHUTTER_DARK = "#7a1e12"
HOTSHOE = "#808080"

# ===========================================
# CAMERA BODY
# ===========================================
# Body dark outline
c.rect(3, 8, 26, 21, OUTLINE, fill=True)
# Leather body
c.rect(4, 9, 24, 19, DARK_LEATHER, fill=True)

# Light source top-left: left face lighter
for y in range(10, 27):
    c.set(4, y, LEATHER)
    c.set(5, y, LEATHER_LIGHT)
    c.set(6, y, LEATHER)

# Leather texture pattern
texture_hi = [
    (10,11),(14,11),(18,11),(22,11),
    (10,13),(14,13),(19,13),(23,13),
    (11,15),(16,15),(21,15),
    (10,17),(15,17),(20,17),(24,17),
    (11,19),(16,19),(21,19),
    (10,21),(15,21),(20,21),(24,21),
    (11,23),(16,23),(21,23),
    (10,25),(14,25),(18,25),(22,25),
]
for (x,y) in texture_hi:
    c.set(x, y, LEATHER_HI)

texture_mid = [
    (12,12),(16,12),(20,12),(24,12),
    (11,14),(15,14),(20,14),(24,14),
    (12,16),(17,16),(22,16),
    (11,18),(16,18),(21,18),
    (12,20),(17,20),(22,20),
    (11,22),(16,22),(21,22),
    (12,24),(17,24),(22,24),
    (11,26),(15,26),(19,26),(23,26),
]
for (x,y) in texture_mid:
    c.set(x, y, LEATHER)

# ===========================================
# TOP PLATE
# ===========================================
# Top metal plate extends beyond body
c.rect(3, 6, 27, 4, OUTLINE, fill=True)
# plate metal top
c.rect(4, 7, 25, 3, DARK_METAL, fill=True)
c.rect(5, 7, 22, 1, METAL, fill=True)
# top-left shine on plate
c.set(5, 7, METAL_HI)
c.set(6, 7, METAL_LIGHT)

# Under-plate leather exposed on left edge
c.set(3, 6, OUTLINE)
c.set(3, 7, OUTLINE)

# ===========================================
# PRISM HUMP (top center)
# ===========================================
# Raised center top - classic vintage look
c.rect(8, 4, 8, 3, OUTLINE, fill=True)
c.rect(9, 5, 6, 1, METAL, fill=True)
c.set(10, 5, METAL_LIGHT)
c.set(11, 5, METAL_LIGHT)

# ===========================================
# VIEWFINDER (top left on hump)
# ===========================================
c.rect(9, 6, 6, 2, OUTLINE, fill=True)
c.rect(10, 6, 4, 2, GLASS_DARK, fill=True)
c.rect(10, 6, 3, 1, GLASS, fill=True)
c.set(11, 6, GLASS_HI)

# ===========================================
# HOT SHOE (right of hump)
# ===========================================
c.rect(19, 4, 5, 3, OUTLINE, fill=True)
c.rect(20, 4, 3, 2, HOTSHOE, fill=True)
c.set(20, 4, METAL)
c.set(21, 4, METAL_HI)

# ===========================================
# SHUTTER BUTTON (far right) - the classic metal + red-style
# ===========================================
# button base
c.rect(26, 3, 4, 4, OUTLINE, fill=True)
c.rect(26, 4, 4, 2, DARK_METAL, fill=True)
# knurled metal shutter top
c.set(26, 4, METAL)
c.set(28, 4, METAL)
c.set(27, 4, SHUTTER)
c.set(29, 4, OUTLINE)
c.set(27, 5, SHUTTER_DARK)
c.set(28, 5, SHUTTER)
c.set(28, 6, METAL)
# under-shadow
c.set(27, 6, OUTLINE)

# ===========================================
# LENS
# ===========================================
lcx, lcy = 17, 19
# Barrel extends outward from body
# Outer ring (very dark)
c.circle(lcx, lcy, 11, OUTLINE, fill=True)
c.circle(lcx, lcy, 10, DARK_METAL, fill=True)
# Main barrel ring
c.circle(lcx, lcy, 9, METAL, fill=True)
# Second ring (groove darker)
c.circle(lcx, lcy, 8, DARK_METAL, fill=True)
# Third ring brighter
c.circle(lcx, lcy, 7, METAL_LIGHT, fill=True)
# Outer glass bezel
c.circle(lcx, lcy, 6, DARK_METAL, fill=True)
# Glass
c.circle(lcx, lcy, 5, GLASS_DARK, fill=True)
c.circle(lcx, lcy, 5, GLASS, fill=True)
c.circle(lcx, lcy, 4, GLASS_DARK, fill=True)

# Glass inner with a clean window-arch reflection
# Upper-left bright crescent (light from upper-left)
glass_hi = [(14,16),(15,16),(16,16),(16,17),(15,15),(14,17),(15,17)]
for (x,y) in glass_hi:
    c.set(x, y, GLASS_HI)
# mid tone around the highlight
for (x,y) in [(17,16),(17,17),(18,16),(16,15),(13,16)]:
    c.set(x, y, GLASS_MID)
# glass base dark bottom
# catch a thin bright glint on the bottom-right of inner glass
c.set(19,20, GLASS_MID)
c.set(18,21, GLASS_MID)
c.set(19,21, GLASS_DARK)
c.set(20,20, GLASS_DARK)
# deepest lens center - subtle aperture depth of the glass
c.set(18,19, GLASS_MID)
c.set(19,19, GLASS_MID)

# Ring highlights top-left
c.set(10,11, METAL_HI)
c.set(11,10, METAL_HI)
c.set(12,9, METAL_HI)
c.set(13,9, METAL_LIGHT)
c.set(9,12, METAL_LIGHT)
c.set(8,13, METAL_LIGHT)
c.set(8,14, METAL_LIGHT)
c.set(8,15, METAL)
# Ring shadows bottom-right
c.set(26,24, METAL)
c.set(25,25, DARK_METAL)
c.set(24,26, DARK_METAL)
c.set(23,27, DARK_METAL)

# Side definition - vertical seam line for leather wrap on right
for y in range(10, 26):
    c.set(25, y, LEATHER)

# left side strap lug on the top corner (small metal tab)
c.set(3, 8, METAL)
c.set(3, 9, METAL)

# ===========================================
# LENS BARREL - extended below body
# ===========================================
# Make the barrel protrusion below the body read as a solid cylinder
# The lens outer ring (y up to 29-30) provides the curve; add shading
for y in range(27, 30):
    for x in range(6, 28):
        pass
# barrel bottom arc shading
c.set(9, 28, DARK_METAL)
c.set(10, 29, DARK_METAL)
c.set(11, 29, DARK_METAL)
c.set(12, 29, DARK_METAL)
c.set(13, 29, DARK_METAL)
c.set(14, 29, METAL)
c.set(17, 29, METAL)
c.set(18, 29, METAL)
c.set(19, 29, METAL)
c.set(20, 29, METAL)
c.set(21, 29, METAL)
c.set(22, 28, DARK_METAL)
c.set(23, 28, DARK_METAL)

# ===========================================
# REWIND KNOB (TOP LEFT)
# ===========================================
c.rect(4, 4, 3, 3, OUTLINE, fill=True)
c.rect(5, 5, 1, 1, METAL, fill=True)
c.set(5, 5, METAL_HI)

# ===========================================
# SMALL DIAL behind hump (film speed dial)
# ===========================================
c.rect(5, 5, 2, 2, OUTLINE, fill=True)
c.rect(6, 6, 1, 1, METAL, fill=True)

# ===========================================
# BOTTOM DETAIL
# ===========================================
# bottom leather shadow
c.rect(5, 25, 22, 1, LEATHER, fill=True)
# bottom edge dark
c.rect(5, 26, 22, 1, DARK_LEATHER, fill=True)

# ===========================================
# CLEAN LENS BARREL BOTTOM (below the body)
# ===========================================
# Solid cylinder bottom arc so the barrel reads clean below the body
barrel_bottom = [
    # y=28
    (8,28),(9,28),(10,28),(11,28),(12,28),(13,28),(14,28),(15,28),
    (16,28),(17,28),(18,28),(19,28),(20,28),(21,28),(22,28),(23,28),(24,28),
    # y=29
    (10,29),(11,29),(12,29),(13,29),(14,29),(15,29),(16,29),(17,29),
    (18,29),(19,29),(20,29),(21,29),(22,29),
    # y=30 lone pixel
    (16,30),(17,30),(18,30),
]
for (x,y) in barrel_bottom:
    c.set(x, y, DARK_METAL)
# shade the bottom: darker at the very bottom, lighter sides
for (x,y) in [(11,29),(12,29),(19,29),(20,29),(21,29),(22,29),(17,30)]:
    c.set(x, y, METAL)
# bottom rim line
for (x,y) in [(13,30),(14,30),(15,30),(16,30),(18,30)]:
    c.set(x, y, METAL)
# left and right barrel foot shading
for x in range(8, 11):
    c.set(x, 28, OUTLINE)
for x in range(22, 25):
    c.set(x, 28, OUTLINE)

# ===========================================
# REFINEMENTS & EDGE CLEANUP
# ===========================================
# Right edge of body - slight bevel feel
for y in range(10, 26):
    if c.get(27, y) is not None and c.get(27,y) == c.color(DARK_LEATHER):
        c.set(27, y, LEATHER)
    else:
        c.set(27, y, DARK_LEATHER)

# Red accent dot on front plate (brand)
c.set(9, 8, SHUTTER)

# Ensue body bottom edge has outline
for x in range(4, 28):
    c.set(x, 27, OUTLINE)

finish(c)
