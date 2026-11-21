from pixelbench_api import *

# Create 128x128 canvas for poolcore liminal space
c = new_canvas(128, 128, name="poolcore")

# Define color palette - staying under 86 visible colors
# Water colors (pale blues with variations for depth and ripples)
water_light = c.color("#b8e0f0", "water_light")
water_mid = c.color("#88c8e0", "water_mid")
water_dark = c.color("#60a8c8", "water_dark")
water_ripple = c.color("#d0e8f5", "water_ripple")
water_deep = c.color("#5090b0", "water_deep")
water_highlight = c.color("#e0f0f8", "water_highlight")

# Tile colors (pale blue and white grid mosaic)
tile_white = c.color("#f8fbff", "tile_white")
tile_white_shadow = c.color("#e0e8f0", "tile_white_shadow")
tile_blue = c.color("#c0d8e8", "tile_blue")
tile_blue_dark = c.color("#a0c0d8", "tile_blue_dark")
tile_grout = c.color("#90b0c8", "tile_grout")

# Water slide (white with shading)
slide_white = c.color("#ffffff", "slide_white")
slide_mid = c.color("#f0f0f5", "slide_mid")
slide_shadow = c.color("#d8d8e0", "slide_shadow")
slide_dark = c.color("#c0c0c8", "slide_dark")

# Ceiling lights (bright fluorescent)
light_bright = c.color("#fff8e8", "light_bright")
light_glow = c.color("#f0f0e0", "light_glow")
ceiling = c.color("#e8f0f5", "ceiling")

# Girl colors
skin_light = c.color("#f8d8c8", "skin_light")
skin_mid = c.color("#e8c0b0", "skin_mid")
skin_shadow = c.color("#d8a898", "skin_shadow")
hair_dark = c.color("#2a1810", "hair_dark")
hair_mid = c.color("#4a2820", "hair_mid")

# Swim ring (yellow)
ring_yellow = c.color("#ffd850", "ring_yellow")
ring_shadow = c.color("#e8c040", "ring_shadow")
ring_highlight = c.color("#fff080", "ring_highlight")

# Background/atmosphere (liminal cool tones)
bg_wall_far = c.color("#a8c8d8", "bg_wall_far")
bg_wall_mid = c.color("#c0d8e8", "bg_wall_mid")
bg_shadow = c.color("#7090a8", "bg_shadow")

# Draw background walls and ceiling
# Ceiling (top portion)
c.rect(0, 0, 128, 20, ceiling)

# Back wall (far end of pool)
c.rect(20, 20, 88, 40, bg_wall_far)

# Side walls
c.rect(0, 20, 20, 88, bg_wall_mid)
c.rect(108, 20, 20, 88, bg_wall_mid)

# Floor tiles (bottom portion, perspective)
# Draw tiled floor pattern
for y in range(70, 128, 4):
    for x in range(0, 128, 4):
        # Checkerboard pattern with perspective
        if ((x // 4) + (y // 4)) % 2 == 0:
            c.rect(x, y, 4, 4, tile_white)
        else:
            c.rect(x, y, 4, 4, tile_blue)

# Draw pool water area (middle section)
# Main water body
c.rect(15, 55, 98, 50, water_mid)

# Water gradient (darker at edges, lighter in center)
c.rect(20, 58, 88, 44, water_light)
c.rect(30, 62, 68, 35, water_ripple)

# Water ripples (horizontal lines for gentle movement)
for y in range(60, 100, 6):
    for x in range(20, 115, 8):
        c.set(x, y, water_ripple)
        c.set(x+1, y, water_highlight)
        c.set(x+2, y, water_light)

# Reflection effects on water
for i in range(5):
    x = 40 + i * 12
    c.rect(x, 65, 2, 15, water_highlight)

# Draw water slide (curving from upper left into water)
# Slide starts from ceiling area, curves down
# Main slide body - curved path
slide_points = [
    (10, 15), (15, 18), (22, 22), (30, 28), (38, 36),
    (45, 46), (50, 56), (53, 65), (55, 72), (56, 78)
]

# Draw slide as thick curved line
for i in range(len(slide_points) - 1):
    x0, y0 = slide_points[i]
    x1, y1 = slide_points[i + 1]
    # Draw slide width
    for w in range(-4, 5):
        px = (x0 + x1) // 2 + w
        py = (y0 + y1) // 2
        if 0 <= px < 128 and 0 <= py < 128:
            c.set(px, py, slide_white)

# Slide shading
c.path("M 12 16 Q 30 30 50 60 L 54 62 Q 32 32 14 18 Z", slide_shadow, fill=True)

# Slide interior (visible part)
c.path("M 16 18 Q 32 32 52 62 L 50 64 Q 30 34 14 20 Z", slide_mid, fill=True)

# Slide edge highlight
c.path("M 14 17 Q 30 30 48 58", slide_white, fill=False)

# Draw columns (tiled, supporting ceiling)
# Left column
c.rect(18, 20, 6, 50, tile_white)
for y in range(22, 68, 6):
    c.rect(18, y, 6, 5, tile_blue)
    c.rect(18, y+5, 6, 1, tile_grout)

# Right column
c.rect(104, 20, 6, 50, tile_white)
for y in range(22, 68, 6):
    c.rect(104, y, 6, 5, tile_blue)
    c.rect(104, y+5, 6, 1, tile_grout)

# Middle columns (perspective, smaller)
c.rect(45, 25, 4, 40, tile_white_shadow)
for y in range(27, 63, 5):
    c.rect(45, y, 4, 4, tile_blue_dark)

c.rect(79, 25, 4, 40, tile_white_shadow)
for y in range(27, 63, 5):
    c.rect(79, y, 4, 4, tile_blue_dark)

# Ceiling lights (fluorescent strips)
c.rect(25, 2, 20, 4, light_bright)
c.rect(54, 2, 20, 4, light_bright)
c.rect(83, 2, 20, 4, light_bright)

# Light glow effect
c.rect(23, 6, 24, 3, light_glow)
c.rect(52, 6, 24, 3, light_glow)
c.rect(81, 6, 24, 3, light_glow)

# Draw girl in yellow swim ring (center of pool, seen from behind)
girl_x, girl_y = 64, 78

# Swim ring (oval, yellow)
# Outer ring
c.ellipse(girl_x, girl_y, 14, 10, ring_yellow, fill=True)
# Inner hole (water shows through)
c.ellipse(girl_x, girl_y, 8, 6, water_light, fill=True)
# Ring highlight
c.ellipse(girl_x - 3, girl_y - 4, 6, 3, ring_highlight, fill=True)
# Ring shadow
c.ellipse(girl_x + 2, girl_y + 3, 8, 4, ring_shadow, fill=False)

# Girl's body (seen from behind, floating)
# Head
c.circle(girl_x, girl_y - 3, 5, skin_light, fill=True)
# Hair (dark, shoulder length)
c.circle(girl_x, girl_y - 5, 5, hair_dark, fill=True)
c.rect(girl_x - 4, girl_y - 2, 8, 6, hair_dark)
# Hair highlight
c.set(girl_x - 2, girl_y - 6, hair_mid)
c.set(girl_x, girl_y - 6, hair_mid)

# Shoulders (partially in water)
c.ellipse(girl_x, girl_y + 2, 7, 4, skin_mid, fill=True)

# Arms (relaxed, on ring)
c.ellipse(girl_x - 8, girl_y, 3, 2, skin_light, fill=True)
c.ellipse(girl_x + 8, girl_y, 3, 2, skin_light, fill=True)

# Water displacement around girl
import math
for i in range(8):
    angle = i * 45
    rx = int(girl_x + 16 * math.cos(math.radians(angle)))
    ry = int(girl_y + 10 * math.sin(math.radians(angle)))
    if 0 <= rx < 128 and 0 <= ry < 128:
        c.set(rx, ry, water_ripple)

# Add atmospheric depth (vignette effect for liminal feel)
# Darker corners
for i in range(10):
    c.rect(i, 118-i, 3, 3+i//2, bg_shadow)
    c.rect(125-i, 118-i, 3, 3+i//2, bg_shadow)

# Wall tile details (grid pattern on side walls)
for y in range(25, 105, 8):
    for x in range(2, 18, 8):
        c.set(x, y, tile_grout)
    for x in range(110, 126, 8):
        c.set(x, y, tile_grout)

# Pool edge tiles
c.rect(12, 53, 104, 3, tile_white)
c.rect(14, 53, 100, 2, tile_blue)

# Water surface highlights (from ceiling lights)
c.rect(30, 56, 8, 2, water_highlight)
c.rect(60, 56, 8, 2, water_highlight)
c.rect(90, 56, 8, 2, water_highlight)

# Slide support structure (subtle)
c.rect(8, 25, 4, 30, slide_dark)

# Final atmosphere - subtle mist/haze at water level
for y in range(54, 60):
    for x in range(0, 128, 4):
        if (x + y) % 7 == 0:
            c.set(x, y, water_highlight)

# Check color count
stats = c.stats()
print(f"Colors used: {stats['colors_used']}")
print(f"Visible pixels: {stats['visible_pixels']}")
print(c.stats_text())

# Submit the canvas
finish(c)
