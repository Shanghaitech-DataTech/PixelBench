from pixelbench_api import *
import math

# Create the canvas
c = new_canvas(128, 128, background=None, name="village")

# ============================================================
# SUNRISE SKY
# ============================================================
sky_colors = [
    (18, 28, 65),    # dark blue top
    (35, 45, 95),    # deeper blue  
    (72, 65, 125),   # purple-blue
    (130, 85, 135),  # purple-pink
    (195, 105, 105), # pink-orange
    (235, 145, 75),  # orange
    (255, 185, 75),  # light orange
    (255, 215, 130), # warm yellow near horizon
]
band_h = 16
for i, col in enumerate(sky_colors):
    for y in range(i * band_h, min((i + 1) * band_h, 128)):
        c.line(0, y, 127, y, col)

# ============================================================
# SUN with glow
# ============================================================
sun_cx, sun_cy = 64, 70
# Outer glow rings
c.circle(sun_cx, sun_cy, 15, (255, 165, 90), fill=False)
c.circle(sun_cx, sun_cy, 12, (255, 190, 85), fill=False)
# Sun disc
c.circle(sun_cx, sun_cy, 9, (255, 225, 115))
# Sun inner bright
c.circle(sun_cx, sun_cy, 5, (255, 245, 185))

# Soft rays
for angle in range(0, 360, 30):
    rx = int(sun_cx + 13 * math.cos(math.radians(angle)))
    ry = int(sun_cy + 13 * math.sin(math.radians(angle)))
    rx2 = int(sun_cx + 18 * math.cos(math.radians(angle)))
    ry2 = int(sun_cy + 18 * math.sin(math.radians(angle)))
    c.line(rx, ry, rx2, ry2, (255, 200, 100))

# ============================================================
# CLOUDS
# ============================================================
clouds = [
    (8, 18, (255, 235, 215)),
    (25, 14, (255, 225, 200)),
    (95, 16, (255, 220, 195)),
    (40, 26, (240, 200, 180)),
    (105, 28, (250, 210, 190)),
    (14, 33, (235, 195, 175)),
    (70, 22, (245, 205, 185)),
]
for cx, cy, cc in clouds:
    c.circle(cx, cy, 3, cc)
    c.circle(cx + 4, cy, 3, cc)
    c.circle(cx + 2, cy - 1, 3, cc)
    c.circle(cx + 5, cy - 1, 2, cc)
    c.circle(cx + 2, cy + 1, 2, cc)

# ============================================================
# DISTANT MOUNTAINS (layer 1 - haziest, lightest)
# ============================================================
far_mtn = (95, 85, 115)
c.path("M0,82 L18,55 L32,72 L48,50 L65,75 L82,58 L100,75 L115,62 L127,78 L127,100 L0,100 Z",
       far_mtn)
# Snow caps on distant peaks
c.path("M48,50 L55,58 L41,58 Z", (230, 215, 220))
c.path("M18,55 L27,66 L12,67 Z", (225, 210, 215))
c.path("M82,58 L91,68 L75,68 Z", (218, 203, 208))
c.path("M115,62 L121,70 L109,71 Z", (212, 197, 202))
# Mountain texture - subtle shadows
c.line(32, 72, 48, 50, (80, 72, 100))
c.line(65, 75, 82, 58, (82, 74, 102))

# ============================================================
# MID-DISTANCE MOUNTAINS (layer 2 - darker)
# ============================================================
mid_mtn = (58, 54, 78)
c.path("M0,92 L14,72 L28,86 L44,67 L58,84 L74,70 L92,88 L108,75 L127,90 L127,104 L0,104 Z",
       mid_mtn)
# Warm rim light where sun hits ridge lines
c.line(14, 72, 28, 86, (130, 100, 118))
c.line(44, 67, 58, 84, (140, 108, 122))
c.line(74, 70, 92, 88, (135, 102, 118))
c.line(108, 75, 127, 90, (125, 95, 112))
# Mountain shadow slopes
c.line(28, 86, 44, 67, (75, 70, 92))
c.line(58, 84, 74, 70, (75, 70, 92))

# ============================================================
# NEAR HILLS (layer 3 - flanking the valley, center open)
# ============================================================
near_hill = (40, 55, 60)
# Left hill
c.path("M0,98 L8,86 L20,91 L34,86 L46,93 L52,99 L52,108 L0,108 Z", near_hill)
# Right hill
c.path("M127,97 L116,88 L106,93 L92,88 L80,95 L76,100 L76,108 L127,108 Z", near_hill)
# Forest texture dots on hills
for fx, fy in [(3, 92), (10, 89), (18, 93), (28, 90), (38, 90)]:
    c.set(fx, fy, (30, 42, 50))
    c.set(fx + 4, fy + 1, (48, 60, 65))
for fx, fy in [(122, 93), (112, 91), (100, 90), (88, 92), (78, 98)]:
    c.set(fx, fy, (30, 42, 50))
    c.set(fx + 3, fy + 1, (48, 60, 65))

# ============================================================
# ATMOSPHERIC HAZE
# ============================================================
c.rect(0, 92, 128, 6, (210, 165, 130))
c.rect(0, 97, 128, 3, (225, 185, 145))

# ============================================================
# VALLEY GROUND
# ============================================================
c.rect(0, 98, 128, 30, (75, 110, 72))

# Sunlit valley floor
c.ellipse(64, 108, 48, 17, (115, 150, 90))
c.ellipse(64, 110, 36, 13, (140, 168, 105))
c.ellipse(64, 99, 28, 9, (160, 180, 115))
# Warm sunlight washing over the valley
c.ellipse(64, 102, 22, 7, (175, 190, 125))

# ============================================================
# STONE PATH - meandering from front to houses
# ============================================================
stone_a = (158, 153, 148)
stone_b = (135, 130, 125)
stone_c = (175, 170, 165)

# Bottom wide section
c.poly([(88, 128), (112, 128), (104, 118), (80, 118)], stone_a)
c.poly([(80, 118), (104, 118), (94, 109), (72, 109)], stone_b)
c.poly([(72, 109), (94, 109), (84, 102), (64, 102)], stone_a)
c.poly([(64, 102), (84, 102), (70, 95), (54, 95)], stone_b)
# Top narrow section connecting to village
c.poly([(54, 95), (70, 95), (60, 92), (50, 92)], stone_a)

# Stone texture
for sx, sy in [(90, 122), (100, 124), (85, 114), (94, 112), (75, 106), (83, 104),
               (65, 99), (58, 97), (52, 93)]:
    c.set(sx, sy, (120, 115, 110))
    c.set(sx + 3, sy + 1, stone_c)
    c.set(sx + 5, sy, (110, 105, 100))

# More detailed stones - individual pavers (reusing stone colors)
for px, py, pw, ph in [
    (92, 121, 6, 3), (100, 124, 7, 3), (84, 115, 5, 3), (93, 113, 6, 3),
    (74, 107, 6, 3), (82, 106, 5, 3), (65, 101, 5, 3), (56, 98, 4, 3),
]: 
    c.rect(px, py, pw, ph, stone_a)

# ============================================================
# HOUSES - center focal point
# ============================================================
wood = (145, 100, 60)
wood_light = (165, 120, 75)
roof = (110, 52, 38)
roof_dark = (76, 40, 30)
timber = (60, 38, 30)
glow = (255, 215, 130)

# ----- MAIN HOUSE (center) -----
h1x, h1y = 49, 80
c.rect(h1x, h1y, 30, 17, wood)
# Timber framework
c.line(h1x + 9, h1y, h1x + 9, h1y + 16, timber)
c.line(h1x + 19, h1y, h1x + 19, h1y + 16, timber)
c.line(h1x, h1y + 8, h1x + 29, h1y + 8, timber)
# Plank lines
c.line(h1x, h1y + 3, h1x + 29, h1y + 3, (135, 92, 55))
c.line(h1x, h1y + 11, h1x + 29, h1y + 11, (135, 92, 55))
# Roof
c.poly([(h1x - 5, h1y), (h1x + 15, h1y - 11), (h1x + 35, h1y)], roof)
c.line(h1x - 3, h1y - 2, h1x + 15, h1y - 9, roof_dark)
c.line(h1x + 33, h1y - 2, h1x + 15, h1y - 9, roof_dark)
# Ridge with sunrise light
c.line(h1x + 13, h1y - 11, h1x + 17, h1y - 11, (200, 95, 55))
# Windows (warm glow)
c.rect(h1x + 3, h1y + 3, 6, 5, glow)
c.rect(h1x + 21, h1y + 3, 6, 5, glow)
# Window cross-frames
c.line(h1x + 5, h1y + 3, h1x + 5, h1y + 7, timber)
c.line(h1x + 23, h1y + 3, h1x + 23, h1y + 7, timber)
# Door with steps
c.rect(h1x + 11, h1y + 10, 7, 7, timber)
c.rect(h1x + 10, h1y + 15, 9, 2, (120, 100, 80))
c.set(h1x + 14, h1y + 12, glow)
c.set(h1x + 15, h1y + 12, glow)
# Chimney
c.rect(h1x + 23, h1y - 4, 4, 7, roof_dark)
c.line(h1x + 23, h1y - 4, h1x + 26, h1y - 4, (100, 55, 40))
# Smoke - wispy rising
c.circle(h1x + 24, h1y - 8, 3, (235, 228, 225))
c.circle(h1x + 23, h1y - 12, 4, (245, 240, 238))
c.circle(h1x + 24, h1y - 16, 3, (250, 248, 246))
c.circle(h1x + 23, h1y - 19, 2, (252, 250, 249))
c.circle(h1x + 24, h1y - 22, 2, (253, 251, 250))

# ----- LEFT HOUSE -----
h2x, h2y = 22, 86
c.rect(h2x, h2y, 21, 14, wood_light)
c.line(h2x + 10, h2y, h2x + 10, h2y + 13, timber)
c.line(h2x, h2y + 7, h2x + 20, h2y + 7, timber)
# Roof
c.poly([(h2x - 3, h2y), (h2x + 10, h2y - 8), (h2x + 24, h2y)], roof)
c.line(h2x + 8, h2y - 8, h2x + 12, h2y - 8, (200, 95, 55))
c.line(h2x - 1, h2y - 3, h2x + 10, h2y - 6, roof_dark)
c.line(h2x + 21, h2y - 3, h2x + 10, h2y - 6, roof_dark)
# Windows
c.rect(h2x + 2, h2y + 3, 5, 4, glow)
c.rect(h2x + 14, h2y + 3, 5, 4, glow)
c.line(h2x + 4, h2y + 3, h2x + 4, h2y + 6, timber)
c.line(h2x + 16, h2y + 3, h2x + 16, h2y + 6, timber)
# Door
c.rect(h2x + 8, h2y + 9, 5, 5, timber)
# Chimney
c.rect(h2x + 17, h2y - 3, 3, 6, roof_dark)
# Smoke
c.circle(h2x + 18, h2y - 7, 3, (240, 235, 232))
c.circle(h2x + 17, h2y - 11, 4, (248, 245, 243))

# ----- RIGHT HOUSE -----
h3x, h3y = 84, 85
c.rect(h3x, h3y, 20, 13, wood)
c.line(h3x + 10, h3y, h3x + 10, h3y + 12, timber)
# Roof
c.poly([(h3x - 3, h3y), (h3x + 10, h3y - 8), (h3x + 23, h3y)], roof)
c.line(h3x + 8, h3y - 8, h3x + 12, h3y - 8, (200, 95, 55))
c.line(h3x - 1, h3y - 3, h3x + 10, h3y - 6, roof_dark)
c.line(h3x + 21, h3y - 3, h3x + 10, h3y - 6, roof_dark)
# Windows
c.rect(h3x + 2, h3y + 3, 5, 4, glow)
c.rect(h3x + 12, h3y + 3, 5, 4, glow)
c.line(h3x + 4, h3y + 3, h3x + 4, h3y + 6, timber)
c.line(h3x + 14, h3y + 3, h3x + 14, h3y + 6, timber)
# Door
c.rect(h3x + 7, h3y + 8, 5, 5, timber)
# Chimney
c.rect(h3x + 17, h3y - 3, 3, 5, roof_dark)
# Smoke
c.circle(h3x + 18, h3y - 7, 3, (240, 235, 232))
c.circle(h3x + 17, h3y - 11, 4, (250, 247, 245))

# ============================================================
# PINE TREES
# ============================================================
def pine(tx, ty, th, col):
    """Layered pine tree."""
    tier = th // 3
    # Bottom tier
    c.poly([(max(0, tx - tier - 2), ty), (min(127, tx + tier + 2), ty), (tx, ty + tier * 2 + 2)], col)
    # Middle tier overlap
    c.poly([(max(0, tx - tier), ty - tier + 1), (min(127, tx + tier), ty - tier + 1), (tx, ty + tier * 3 // 2)], col)
    # Top tier  
    c.poly([(max(0, tx - tier + 1), ty - tier * 2 + 2), (min(127, tx + tier - 1), ty - tier * 2 + 2), (tx, ty + tier // 2)], col)
    # Trunk
    c.rect(max(0, tx - 1), ty + tier * 2, 2, 3, (65, 48, 35))

# Mid-distance pines
pine(10, 92, 11, (25, 55, 38))
pine(118, 93, 10, (25, 55, 38))
pine(15, 98, 8, (35, 70, 45))
pine(112, 97, 8, (35, 70, 45))
pine(44, 96, 7, (45, 80, 48))
pine(84, 97, 6, (45, 80, 48))

# Foreground pines (large and dark)
pine(8, 106, 15, (16, 38, 28))
pine(123, 105, 14, (18, 42, 30))

# Small pine cluster between houses for depth
pine(38, 98, 5, (40, 75, 45))
pine(90, 99, 5, (40, 75, 45))

# ============================================================
# FOREGROUND detail
# ============================================================
c.rect(0, 119, 128, 4, (50, 75, 46))
c.rect(0, 123, 128, 5, (30, 55, 36))

# Small flowers by path (using existing warm colors)
flower = (170, 120, 80)
for fx, fy in [(58, 110), (52, 116), (70, 115), (44, 120), (76, 112),
               (30, 112), (100, 110), (86, 118), (36, 117), (94, 120)]:
    c.set(fx, fy, flower)

# Grass blade highlights (using existing forest green tones)
for gx in range(2, 125, 8):
    c.set(gx, 121, (50, 75, 46))
    c.set(gx + 2, 122, (30, 55, 36))

# ============================================================
# FENCE
# ============================================================
fence = (85, 65, 45)
for fx in range(32, 100, 5):
    c.rect(fx, 101, 2, 6, fence)
c.line(30, 102, 102, 102, fence)

# ============================================================
# BIRDS
# ============================================================
bird = (55, 55, 70)
for bx, by in [(92, 26), (99, 31), (74, 40), (28, 44), (85, 50)]:
    c.set(bx, by, bird)
    c.set(bx + 1, by - 1, bird)
    c.set(bx + 2, by, bird)
    c.set(bx + 3, by - 1, bird)

# ============================================================
# FOCAL WARM GLOW around the village
# ============================================================
c.ellipse(64, 96, 28, 10, (255, 210, 135), fill=False)
c.ellipse(64, 99, 18, 7, (255, 225, 155), fill=False)

# Sunrise sparkle on path
for px in range(60, 100, 8):
    c.set(px, 99, stone_c)

# ============================================================
print(c.stats_text())

finish(c)
