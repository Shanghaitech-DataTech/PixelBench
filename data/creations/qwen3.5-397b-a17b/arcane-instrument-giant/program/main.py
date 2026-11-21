from pixelbench_api import *

# Create the canvas
c = new_canvas(256, 256, background=None, name="arcane_instrument")

# Define color palette - brass, dark hall, glowing elements
# Keep under 140 visible colors

# Dark background colors (hall)
bg_dark = c.color("#0a0a0f", "bg_dark")
bg_mid = c.color("#151520", "bg_mid")
bg_light = c.color("#1f1f2a", "bg_light")

# Stone pedestal colors
stone_dark = c.color("#2a2a35", "stone_dark")
stone_mid = c.color("#3d3d4a", "stone_mid")
stone_light = c.color("#5a5a6a", "stone_light")
stone_highlight = c.color("#7a7a8a", "stone_highlight")

# Brass colors (main instrument)
brass_dark = c.color("#4a3a1a", "brass_dark")
brass_mid = c.color("#6b5424", "brass_mid")
brass_light = c.color("#8f7230", "brass_light")
brass_highlight = c.color("#b89a4a", "brass_highlight")
brass_shine = c.color("#e0c060", "brass_shine")

# Crystal sphere colors
crystal_dark = c.color("#2a3a5a", "crystal_dark")
crystal_mid = c.color("#4a6a9a", "crystal_mid")
crystal_light = c.color("#7a9ac0", "crystal_light")
crystal_highlight = c.color("#aaccff", "crystal_highlight")

# Glowing rune colors
glow_core = c.color("#ffaa00", "glow_core")
glow_mid = c.color("#ffcc44", "glow_mid")
glow_outer = c.color("#ffee88", "glow_outer")
glow_white = c.color("#ffffff", "glow_white")

# Gear/mechanical colors
gear_dark = c.color("#3a3a4a", "gear_dark")
gear_mid = c.color("#5a5a6a", "gear_mid")
gear_light = c.color("#7a7a8a", "gear_light")

# Shadow colors
shadow_soft = c.color((0, 0, 0, 64), "shadow_soft")
shadow_hard = c.color((0, 0, 0, 128), "shadow_hard")

# Dark outline
outline = c.color("#1a1a1a", "outline")

# === BACKGROUND - Dark Hall ===
# Fill with gradient-like dark background
c.rect(0, 0, 256, 256, bg_dark)

# Add some wall texture/depth
for i in range(0, 256, 16):
    c.rect(i, 0, 2, 256, bg_mid)
for i in range(0, 256, 32):
    c.rect(0, i, 256, 2, bg_light)

# Vignette effect - darker corners
for corner_dist in range(4, 60, 4):
    alpha_val = min(255, corner_dist * 4)
    corner_color = c.color((0, 0, 0, alpha_val))
    # Draw corner darkening
    c.rect(corner_dist, 0, 4, corner_dist, corner_color)
    c.rect(252-corner_dist, 0, 4, corner_dist, corner_color)
    c.rect(corner_dist, 252-corner_dist, 4, corner_dist, corner_color)
    c.rect(252-corner_dist, 252-corner_dist, 4, corner_dist, corner_color)

# === STONE PEDESTAL ===
pedestal_y = 180
pedestal_top_y = 190

# Main pedestal body
c.rect(80, pedestal_y, 96, 66, stone_dark)
c.rect(84, pedestal_y+4, 88, 58, stone_mid)
c.rect(90, pedestal_y+10, 76, 46, stone_light)

# Pedestal top platform
c.rect(70, pedestal_top_y, 116, 12, stone_mid)
c.rect(74, pedestal_top_y+2, 108, 8, stone_light)
c.rect(80, pedestal_top_y+4, 96, 4, stone_highlight)

# Pedestal engravings
for i in range(0, 96, 12):
    c.line(80+i, pedestal_y+15, 80+i, pedestal_y+55, stone_dark)
    c.line(82+i, pedestal_y+15, 82+i, pedestal_y+55, stone_light)

# Pedestal base decorations
c.rect(76, pedestal_y+60, 104, 6, stone_dark)
c.rect(80, pedestal_y+62, 96, 3, stone_light)

# === CENTRAL ASTROLABE CORE ===
center_x, center_y = 128, 110

# Radiant core glow (behind everything)
for r in range(25, 0, -2):
    glow_alpha = int(200 * (r / 25))
    glow_c = c.color((255, 170, 0, glow_alpha))
    c.circle(center_x, center_y, r, glow_c)

# Central core - bright
c.circle(center_x, center_y, 8, glow_white)
c.circle(center_x, center_y, 6, glow_core)
c.circle(center_x, center_y, 4, glow_mid)
c.circle(center_x, center_y, 2, glow_white)

# === CONCENTRIC RINGS ===
# Multiple brass rings with engravings

# Outer ring (largest)
outer_r = 95
c.circle(center_x, center_y, outer_r, brass_dark, fill=False)
c.circle(center_x, center_y, outer_r-2, brass_mid, fill=False)
c.circle(center_x, center_y, outer_r-4, brass_light, fill=False)

# Ring engravings - outer
for angle in range(0, 360, 15):
    import math
    rad = math.radians(angle)
    x1 = int(center_x + (outer_r-6) * math.cos(rad))
    y1 = int(center_y + (outer_r-6) * math.sin(rad))
    x2 = int(center_x + (outer_r-3) * math.cos(rad))
    y2 = int(center_y + (outer_r-3) * math.sin(rad))
    c.line(x1, y1, x2, y2, brass_highlight)

# Second ring
ring2_r = 75
c.circle(center_x, center_y, ring2_r, brass_dark, fill=False)
c.circle(center_x, center_y, ring2_r-2, brass_mid, fill=False)
c.circle(center_x, center_y, ring2_r-4, brass_light, fill=False)

# Ring engravings - second
for angle in range(0, 360, 20):
    rad = math.radians(angle)
    x1 = int(center_x + (ring2_r-6) * math.cos(rad))
    y1 = int(center_y + (ring2_r-6) * math.sin(rad))
    x2 = int(center_x + (ring2_r-3) * math.cos(rad))
    y2 = int(center_y + (ring2_r-3) * math.sin(rad))
    c.line(x1, y1, x2, y2, brass_highlight)

# Third ring
ring3_r = 55
c.circle(center_x, center_y, ring3_r, brass_dark, fill=False)
c.circle(center_x, center_y, ring3_r-2, brass_mid, fill=False)
c.circle(center_x, center_y, ring3_r-4, brass_light, fill=False)

# Glowing runes on third ring
for angle in range(0, 360, 30):
    rad = math.radians(angle)
    rx = int(center_x + ring3_r * math.cos(rad))
    ry = int(center_y + ring3_r * math.sin(rad))
    # Small rune marks
    c.rect(rx-2, ry-2, 4, 4, glow_mid)
    c.rect(rx-1, ry-1, 2, 2, glow_outer)

# Inner ring
ring4_r = 35
c.circle(center_x, center_y, ring4_r, brass_dark, fill=False)
c.circle(center_x, center_y, ring4_r-2, brass_mid, fill=False)

# === CRYSTAL SPHERES (orbiting) ===
# Place several crystal spheres on different orbital paths

sphere_positions = [
    (center_x + 65, center_y),
    (center_x - 65, center_y),
    (center_x, center_y + 65),
    (center_x, center_y - 65),
    (center_x + 45, center_y + 45),
    (center_x - 45, center_y - 45),
    (center_x + 45, center_y - 45),
    (center_x - 45, center_y + 45),
]

for sx, sy in sphere_positions:
    # Crystal sphere with gradient
    c.circle(sx, sy, 10, crystal_dark)
    c.circle(sx, sy, 8, crystal_mid)
    c.circle(sx, sy, 6, crystal_light)
    c.circle(sx-2, sy-2, 3, crystal_highlight)
    c.circle(sx-3, sy-3, 1, glow_white)

# === GEARS AND MECHANICAL DETAILS ===
# Add gears around the instrument

def draw_gear(gx, gy, size, color_main, color_dark):
    """Draw a mechanical gear"""
    # Gear body
    c.circle(gx, gy, size, color_main)
    c.circle(gx, gy, size-2, color_dark)
    # Gear teeth
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        tx = int(gx + (size+3) * math.cos(rad))
        ty = int(gy + (size+3) * math.sin(rad))
        c.rect(tx-2, ty-2, 4, 4, color_main)
    # Center hole
    c.circle(gx, gy, 4, color_dark)
    c.circle(gx, gy, 2, brass_highlight)

# Position gears around the astrolabe
gear_positions = [
    (128, 40, 12),
    (60, 80, 10),
    (196, 80, 10),
    (50, 130, 8),
    (206, 130, 8),
    (80, 170, 10),
    (176, 170, 10),
]

for gx, gy, gsize in gear_positions:
    draw_gear(gx, gy, gsize, gear_mid, gear_dark)

# === SUPPORT ARMS ===
# Brass arms holding the rings

# Left support arm
c.poly([
    (70, 190), (85, 160), (90, 140), (85, 120),
    (80, 120), (85, 140), (80, 160), (65, 190)
], brass_mid, fill=True)
c.line(70, 190, 85, 160, brass_dark)
c.line(85, 160, 90, 140, brass_dark)

# Right support arm
c.poly([
    (186, 190), (171, 160), (166, 140), (171, 120),
    (176, 120), (171, 140), (176, 160), (191, 190)
], brass_mid, fill=True)
c.line(186, 190, 171, 160, brass_dark)
c.line(171, 160, 166, 140, brass_dark)

# Top support arch
c.path("M 90 100 Q 128 70 166 100", brass_light, fill=False)
c.path("M 95 105 Q 128 80 161 105", brass_mid, fill=False)

# === ALCHEMICAL DIALS ===
# Small circular dials with symbols

def draw_dial(dx, dy, size):
    """Draw an alchemical dial"""
    c.circle(dx, dy, size, brass_dark)
    c.circle(dx, dy, size-2, brass_mid)
    c.circle(dx, dy, size-4, brass_light)
    # Dial markings
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        mx = int(dx + (size-3) * math.cos(rad))
        my = int(dy + (size-3) * math.sin(rad))
        c.set(mx, my, brass_highlight)
    # Center pointer
    c.line(dx, dy, dx, dy-size+6, glow_mid)

dial_positions = [(100, 150, 15), (156, 150, 15), (128, 135, 10)]
for dx, dy, dsize in dial_positions:
    draw_dial(dx, dy, dsize)

# === DECORATIVE CHAINS/ORNAMENTS ===
# Hanging chains from the top
for chain_x in [100, 128, 156]:
    for cy in range(20, 80, 8):
        c.rect(chain_x-2, cy, 4, 6, brass_mid)
        c.rect(chain_x-1, cy+2, 2, 2, brass_dark)

# === DRAMATIC LIGHTING ===
# Add light rays from the core
for angle in range(0, 360, 12):
    rad = math.radians(angle)
    # Light ray
    for dist in range(20, 60, 4):
        lx = int(center_x + dist * math.cos(rad))
        ly = int(center_y + dist * math.sin(rad))
        ray_alpha = int(100 * (1 - dist/60))
        if ray_alpha > 0:
            ray_c = c.color((255, 200, 100, ray_alpha))
            c.set(lx, ly, ray_c)

# Shadow under the instrument (on pedestal)
c.rect(90, 185, 76, 8, shadow_soft)
c.rect(100, 187, 56, 4, shadow_hard)

# === DARK OUTLINE ===
# Add outline around major elements for definition

# Outline around outer ring
c.circle(center_x, center_y, outer_r+1, outline, fill=False)

# Outline around core
c.circle(center_x, center_y, 10, outline, fill=False)

# Outline around pedestal
c.rect(78, pedestal_y-1, 100, 68, outline, fill=False)

# === FINAL DETAILS ===
# Add some sparkles/stars in the background
import random
random.seed(42)
for _ in range(30):
    sx = random.randint(10, 246)
    sy = random.randint(10, 170)
    sparkle = random.choice([glow_outer, glow_mid, brass_highlight])
    c.set(sx, sy, sparkle)
    if random.random() > 0.5:
        c.set(sx+1, sy, sparkle)
        c.set(sx, sy+1, sparkle)

# Additional rune symbols on rings
for angle in range(0, 360, 45):
    rad = math.radians(angle)
    rx = int(center_x + (ring2_r + 8) * math.cos(rad))
    ry = int(center_y + (ring2_r + 8) * math.sin(rad))
    c.set(rx, ry, glow_core)

# Check stats
print(c.stats_text())

# Submit
finish(c)
