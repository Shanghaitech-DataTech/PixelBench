import math
import random

# Exact editable copy of input canvas
output = input_canvas.copy(name='output')

# ==============================================================================
# 1. LAYER OF CLIMBING VINES COVERING PART OF THE TOWER'S WALLS
# ==============================================================================

# Harmonious dark/medium forest greens matching the scene's gothic nighttime palette
c_stem_dark  = output.color('#0c1b15', 'v_stem_d')
c_stem_mid   = output.color('#183024', 'v_stem_m')
c_stem_hi    = output.color('#274836', 'v_stem_h')

c_leaf_shadow = output.color('#0d1e16', 'v_leaf_shadow')
c_leaf_dark   = output.color('#163324', 'v_leaf_dark')
c_leaf_mid1   = output.color('#214a34', 'v_leaf_mid1')
c_leaf_mid2   = output.color('#2f6345', 'v_leaf_mid2')
c_leaf_bright = output.color('#417f58', 'v_leaf_bright')
c_leaf_hi     = output.color('#589e6f', 'v_leaf_hi')
c_leaf_tip    = output.color('#75bd8d', 'v_leaf_tip')

# Main creeper vine runners climbing the tower walls
vines_runners = [
    # Trunk 1: lower right wall climbing up across corbel ledge into upper tower
    [(86, 202), (85, 192), (87, 182), (84, 172), (85, 162), (82, 154), (81, 146), (79, 138), (75, 130), (73, 120), (72, 110), (74, 100), (72, 90), (75, 80)],
    # Branch 1A: climbing left of window
    [(79, 138), (74, 134), (70, 128), (68, 120), (66, 112), (67, 102), (66, 92), (69, 84)],
    # Branch 1B: climbing right of window
    [(82, 154), (87, 148), (90, 140), (92, 130), (90, 120), (91, 110), (89, 100), (87, 90), (84, 82)],
    # Branch 1C: spreading across corbel ledge
    [(82, 154), (76, 152), (70, 151), (65, 152), (61, 153)],
    [(82, 154), (88, 152), (93, 153)],
    # Branch 1D: lower wall spread
    [(84, 172), (78, 174), (74, 180), (76, 190), (78, 198)],
    [(87, 182), (90, 178), (92, 170), (91, 160)],
    # Trunk 2: left base of tower wall framing archway
    [(32, 198), (34, 188), (33, 178), (35, 170), (34, 162), (37, 156), (36, 148)],
    [(33, 178), (38, 174), (40, 168), (39, 160)],
]

# Draw woody stems
for runner in vines_runners:
    for i in range(len(runner) - 1):
        x0, y0 = runner[i]
        x1, y1 = runner[i+1]
        output.line(x0, y0, x1, y1, c_stem_dark)
        output.line(x0 + 1, y0, x1 + 1, y1, c_stem_mid)

# Hanging runner tendrils dangling from corbels and sills
dangling_tendrils = [
    (62, 154, 9), (66, 154, 13), (71, 153, 11), (75, 153, 15),
    (80, 154, 12), (85, 154, 16), (89, 153, 10), (92, 153, 8),
    (77, 140, 8), (83, 140, 11), # slit window sill
    (74, 182, 7), (77, 192, 9),  # lower wall
]
rng = random.Random(2024)
for dx, dy, length in dangling_tendrils:
    for step in range(length):
        ox = 1 if (step % 5 == 0) else (-1 if (step % 5 == 2) else 0)
        output.set(dx + ox, dy + step, c_stem_dark)
        if rng.random() < 0.5:
            output.set(dx + ox + rng.choice([-1, 1]), dy + step, c_leaf_dark)
    output.set(dx, dy + length, c_leaf_mid2)
    output.set(dx, dy + length + 1, c_leaf_hi)

# Organic ivy foliage clusters across the wall
# Clusters are defined by center, radii, and leaf density
foliage_masses = [
    # Upper tower wall:
    (74, 84, 6, 4, 0.75),
    (83, 83, 7, 4, 0.75),
    (70, 92, 6, 5, 0.8),
    (76, 91, 7, 5, 0.85),
    (84, 91, 7, 5, 0.85),
    (89, 93, 5, 4, 0.75),
    (67, 100, 6, 5, 0.8),
    (74, 100, 7, 5, 0.85),
    (86, 100, 7, 5, 0.85),
    (67, 110, 6, 5, 0.8),
    (73, 109, 6, 5, 0.85),
    (88, 109, 7, 5, 0.85),
    (68, 118, 6, 5, 0.8),
    (74, 118, 6, 5, 0.85),
    (88, 118, 7, 5, 0.85),
    (69, 127, 6, 5, 0.8),
    (75, 127, 7, 5, 0.85),
    (87, 127, 7, 5, 0.85),
    (91, 126, 5, 5, 0.75),
    (71, 136, 7, 5, 0.85),
    (77, 136, 7, 5, 0.85),
    (85, 136, 7, 5, 0.85),
    (73, 144, 7, 5, 0.85),
    (81, 144, 8, 5, 0.85),
    (88, 144, 7, 5, 0.85),
    
    # Corbel ledge band:
    (64, 151, 6, 4, 0.8),
    (72, 151, 7, 4, 0.85),
    (80, 151, 8, 4, 0.85),
    (87, 151, 7, 4, 0.85),
    (92, 150, 5, 4, 0.75),
    
    # Lower tower wall:
    (75, 160, 6, 5, 0.85),
    (83, 160, 7, 5, 0.85),
    (89, 159, 5, 5, 0.75),
    (76, 169, 7, 5, 0.85),
    (84, 169, 7, 5, 0.85),
    (77, 178, 6, 5, 0.85),
    (85, 178, 7, 5, 0.85),
    (79, 187, 6, 5, 0.8),
    (86, 187, 7, 5, 0.85),
    (83, 195, 7, 5, 0.8),
    
    # Left base of tower beside archway:
    (33, 166, 5, 5, 0.8),
    (37, 173, 5, 5, 0.8),
    (34, 182, 6, 5, 0.85),
    (36, 191, 6, 5, 0.85),
]

for cx, cy, rx, ry, dens in foliage_masses:
    for dy in range(-ry, ry + 1):
        for dx in range(-rx, rx + 1):
            if (dx/rx)**2 + (dy/ry)**2 <= 1.0:
                if rng.random() < dens:
                    px = cx + dx
                    py = cy + dy
                    # Keep slit window aperture open
                    if 79 <= px <= 82 and 112 <= py <= 136:
                        continue
                    
                    # Vertical shading: top catches light, bottom in shadow
                    v_factor = dy / ry
                    r_val = rng.random()
                    if v_factor < -0.3:
                        c = c_leaf_hi if r_val < 0.4 else c_leaf_bright
                    elif v_factor < 0.2:
                        c = c_leaf_bright if r_val < 0.4 else c_leaf_mid2
                    elif v_factor < 0.6:
                        c = c_leaf_mid2 if r_val < 0.4 else c_leaf_mid1
                    else:
                        c = c_leaf_mid1 if r_val < 0.4 else c_leaf_dark
                    output.set(px, py, c)

# Fine leaf highlights and single sprouting leaves along edges
edge_leaves = [
    # Upper wall top perimeter
    (72, 80), (75, 79), (78, 78), (81, 78), (84, 79), (87, 80), (89, 82),
    (67, 85), (65, 90), (64, 96), (63, 104), (64, 112), (65, 120), (66, 126),
    (93, 86), (94, 92), (95, 98), (95, 106), (95, 114), (94, 122), (93, 130),
    # Lower wall edges
    (71, 158), (70, 166), (71, 174), (72, 182), (74, 190), (76, 197),
    (91, 166), (92, 174), (91, 182), (90, 190),
    # Left base edges
    (29, 168), (30, 176), (29, 184), (30, 192),
    (40, 164), (41, 172), (39, 180), (39, 188),
]
for lx, ly in edge_leaves:
    output.set(lx, ly, c_leaf_hi if rng.random() < 0.5 else c_leaf_tip)
    if rng.random() < 0.4:
        output.set(lx + rng.choice([-1, 1]), ly, c_leaf_mid2)


# ==============================================================================
# 2. CLOAKED MAGE HOLDING A GLOWING STAFF AT THE ARCHWAY ENTRANCE
#    HE IS WALKING INTO THE TOWER (FACING AWAY FROM VIEWER, HEADING THROUGH ARCHWAY)
# ==============================================================================

# Palette for the mage
c_m_hood_peak   = output.color('#624d8a', 'm_hood_peak')
c_m_hood_hi     = output.color('#4e3b72', 'm_hood_hi')
c_m_hood_mid    = output.color('#372754', 'm_hood_mid')
c_m_hood_dark   = output.color('#221638', 'm_hood_dark')
c_m_hood_shadow = output.color('#130b22', 'm_hood_shadow')

c_m_cloak_hi    = output.color('#584282', 'm_cloak_hi')
c_m_cloak_mid2  = output.color('#402e64', 'm_cloak_mid2')
c_m_cloak_mid1  = output.color('#2d1f48', 'm_cloak_mid1')
c_m_cloak_dark  = output.color('#1b122c', 'm_cloak_dark')
c_m_cloak_deep  = output.color('#0f091a', 'm_cloak_deep')

c_m_boot_mid    = output.color('#28201a', 'm_boot_mid')
c_m_boot_dark   = output.color('#16120e', 'm_boot_dark')
c_m_boot_sole   = output.color('#0a0806', 'm_boot_sole')

# Staff
c_st_core       = output.color('#1a120a', 'm_staff_core')
c_st_wood       = output.color('#362416', 'm_staff_wood')
c_st_hi         = output.color('#543d2a', 'm_staff_hi')
c_st_metal      = output.color('#6e604e', 'm_staff_metal')
c_glove         = output.color('#2e241c', 'm_glove')

# Magical glowing orb & cyan lighting
c_glow_white    = output.color('#ffffff', 'm_glow_white')
c_glow_core     = output.color('#c8ffff', 'm_glow_core')
c_glow_bright   = output.color('#4af0ff', 'm_glow_bright')
c_glow_cyan     = output.color('#00c8e8', 'm_glow_cyan')
c_glow_blue     = output.color('#0088b8', 'm_glow_blue')
c_glow_deep     = output.color('#005070', 'm_glow_deep')

c_rim_bright    = output.color('#5ed4e8', 'm_rim_bright')
c_rim_mid       = output.color('#3490a4', 'm_rim_mid')
c_rim_dark      = output.color('#1c5464', 'm_rim_dark')

# Grounded mage coordinates:
# Archway ground threshold is at y=214..218.
# Head top: y=182.
# Shoulders: y=190.
# Hem: y=212..215.
# Feet: left boot stepping inside archway at y=213..215, right boot trailing on threshold at y=215..217.

# 1. Hood (y=182..189, back view):
# Peak of hood
output.set(53, 182, c_m_hood_peak)
output.set(54, 182, c_m_hood_hi)

output.set(52, 183, c_m_hood_mid)
output.set(53, 183, c_m_hood_hi)
output.set(54, 183, c_m_hood_peak)
output.set(55, 183, c_rim_mid)

output.set(51, 184, c_m_hood_dark)
output.set(52, 184, c_m_hood_mid)
output.set(53, 184, c_m_hood_hi)
output.set(54, 184, c_m_hood_hi)
output.set(55, 184, c_m_hood_mid)
output.set(56, 184, c_rim_bright)

output.set(50, 185, c_m_hood_dark)
output.set(51, 185, c_m_hood_mid)
output.set(52, 185, c_m_hood_mid)
output.set(53, 185, c_m_hood_hi)
output.set(54, 185, c_m_hood_mid)
output.set(55, 185, c_m_hood_mid)
output.set(56, 185, c_rim_bright)

output.set(50, 186, c_m_hood_shadow)
output.set(51, 186, c_m_hood_dark)
output.set(52, 186, c_m_hood_mid)
output.set(53, 186, c_m_hood_hi)
output.set(54, 186, c_m_hood_mid)
output.set(55, 186, c_m_hood_dark)
output.set(56, 186, c_rim_bright)

output.set(50, 187, c_m_hood_shadow)
output.set(51, 187, c_m_hood_dark)
output.set(52, 187, c_m_hood_mid)
output.set(53, 187, c_m_hood_hi)
output.set(54, 187, c_m_hood_mid)
output.set(55, 187, c_m_hood_dark)
output.set(56, 187, c_rim_bright)
output.set(57, 187, c_rim_mid)

output.set(49, 188, c_m_hood_shadow)
output.set(50, 188, c_m_hood_dark)
output.set(51, 188, c_m_hood_dark)
output.set(52, 188, c_m_hood_mid)
output.set(53, 188, c_m_hood_hi)
output.set(54, 188, c_m_hood_mid)
output.set(55, 188, c_m_hood_dark)
output.set(56, 188, c_rim_bright)
output.set(57, 188, c_rim_dark)

# Neck & Cowl fold
output.set(49, 189, c_m_cloak_deep)
output.set(50, 189, c_m_cloak_dark)
output.set(51, 189, c_m_hood_dark)
output.set(52, 189, c_m_hood_mid)
output.set(53, 189, c_m_hood_mid)
output.set(54, 189, c_m_hood_mid)
output.set(55, 189, c_m_hood_dark)
output.set(56, 189, c_rim_bright)
output.set(57, 189, c_rim_mid)

# 2. Shoulders & Mantle (y=190..194)
for y in range(190, 195):
    lx = 48 - (y - 190) // 2
    rx = 57 + (y - 190) // 2
    for x in range(lx, rx + 1):
        output.set(x, y, c_m_cloak_dark)
    output.set(lx, y, c_m_cloak_deep)
    output.set(51, y, c_m_cloak_mid1)
    output.set(53, y, c_m_cloak_hi if y < 193 else c_m_cloak_mid2)
    output.set(54, y, c_m_cloak_mid2)
    output.set(rx, y, c_rim_bright)
    output.set(rx - 1, y, c_rim_mid)

# Scalloped mantle hemline at y=194
mantle_hem = [
    (47, 194, c_m_cloak_deep), (48, 194, c_m_cloak_mid1), (49, 194, c_m_cloak_dark),
    (50, 194, c_m_cloak_deep), (51, 194, c_m_cloak_mid2), (52, 194, c_m_cloak_mid1),
    (53, 194, c_m_cloak_hi),   (54, 194, c_m_cloak_mid2), (55, 194, c_m_cloak_dark),
    (56, 194, c_m_cloak_mid1), (57, 194, c_m_cloak_mid2), (58, 194, c_rim_bright),
    (59, 194, c_rim_mid),
]
for hx, hy, hc in mantle_hem:
    output.set(hx, hy, hc)

# 3. Main Cloak Body (y=195..212)
# Walking motion: moving forward into the tower archway
for y in range(195, 213):
    prog = (y - 195) / 17.0
    lx = int(47 - prog * 2)
    rx = int(59 + prog * 2)
    
    for x in range(lx, rx + 1):
        output.set(x, y, c_m_cloak_dark)
    output.set(lx, y, c_m_cloak_deep)
    
    # Left drape folds
    output.set(lx + 2, y, c_m_cloak_mid1)
    output.set(lx + 3, y, c_m_cloak_mid2)
    output.set(lx + 4, y, c_m_cloak_deep)
    
    # Central spine fold
    cx = 53 + int(prog * 1.5)
    output.set(cx - 1, y, c_m_cloak_deep)
    output.set(cx, y, c_m_cloak_mid2)
    output.set(cx + 1, y, c_m_cloak_hi if y < 206 else c_m_cloak_mid2)
    
    # Right fold
    rf = rx - 3
    if rf > cx + 1:
        output.set(rf - 1, y, c_m_cloak_deep)
        output.set(rf, y, c_m_cloak_mid2)
        output.set(rf + 1, y, c_m_cloak_mid1)
    
    # Staff rim lighting on right edge
    output.set(rx, y, c_rim_bright if y < 204 else c_rim_mid)
    output.set(rx - 1, y, c_rim_mid if y < 204 else c_rim_dark)

# 4. Right Arm holding the staff (y=194..199)
output.set(59, 195, c_m_cloak_mid2)
output.set(60, 195, c_rim_bright)

output.set(59, 196, c_m_cloak_mid1)
output.set(60, 196, c_rim_bright)
output.set(61, 196, c_rim_mid)

output.set(60, 197, c_m_cloak_mid2)
output.set(61, 197, c_rim_bright)

# Gloved hand gripping staff at (61, 198) and (61, 199)
output.set(60, 198, c_glove)
output.set(61, 198, c_st_metal)
output.set(62, 198, c_rim_bright)

output.set(60, 199, c_glove)
output.set(61, 199, c_st_metal)
output.set(62, 199, c_rim_bright)

# 5. Stride, Hem, and Boots firmly grounded on the threshold (y=212..217)
# Left foot is stepping forward into the doorway opening:
output.set(48, 212, c_m_cloak_deep)
output.set(49, 212, c_boot_dark)
output.set(50, 212, c_boot_mid)
output.set(48, 213, c_boot_dark)
output.set(49, 213, c_boot_mid)
output.set(50, 213, c_boot_sole)
output.set(49, 214, c_boot_sole)
output.set(50, 214, c_boot_sole)

# Trailing right foot/boot on the threshold step (x=56..58, y=214..217):
output.set(56, 213, c_m_cloak_deep)
output.set(57, 213, c_boot_dark)
output.set(58, 213, c_rim_dark)

output.set(56, 214, c_boot_mid)
output.set(57, 214, c_boot_dark)
output.set(58, 214, c_boot_sole)

output.set(56, 215, c_boot_sole)
output.set(57, 215, c_boot_sole)
output.set(58, 215, c_boot_sole)

# Trailing cloak hem folds waving at y=212..214:
hem_details = [
    (45, 212, c_m_cloak_deep), (46, 212, c_m_cloak_dark), (47, 212, c_m_cloak_mid1),
    (51, 212, c_m_cloak_deep), (52, 212, c_m_cloak_mid1), (53, 212, c_m_cloak_mid2),
    (54, 212, c_m_cloak_dark), (55, 212, c_m_cloak_deep),
    (59, 212, c_m_cloak_mid1), (60, 212, c_rim_mid),      (61, 212, c_rim_dark),
    # y=213 dips
    (45, 213, c_m_cloak_deep), (46, 213, c_m_cloak_dark),
    (52, 213, c_m_cloak_deep), (53, 213, c_m_cloak_dark), (54, 213, c_m_cloak_deep),
    (60, 213, c_rim_dark),
]
for hx, hy, hc in hem_details:
    output.set(hx, hy, hc)

# 6. Glowing Staff:
# Staff stave runs from the floor step at (62, 216) up to staff head at (61, 177)
for sy in range(178, 217):
    if sy not in (198, 199):
        output.set(62, sy, c_st_core)
        output.set(61, sy, c_st_wood if sy > 199 else c_st_hi)
        output.set(63, sy, c_rim_bright if sy < 194 else c_rim_mid)

# Staff contact with threshold step
output.set(62, 217, c_boot_sole)

# Staff Head (carved prongs gripping the glowing orb):
staff_head_pts = [
    (61, 178, c_st_metal), (62, 178, c_st_metal),
    (61, 177, c_st_metal), (62, 177, c_st_hi),
    (60, 176, c_st_metal), (59, 175, c_st_hi), (59, 174, c_st_hi), (60, 173, c_st_metal),
    (63, 176, c_st_metal), (64, 175, c_st_hi), (64, 174, c_st_hi), (63, 173, c_st_metal),
    (61, 171, c_st_metal), (62, 171, c_st_metal), (61, 170, c_st_hi),
]
for sx, sy, sc in staff_head_pts:
    output.set(sx, sy, sc)

# Glowing magical crystal/orb centered at (61.5, 174)
# Radiant white core
output.set(61, 174, c_glow_white)
output.set(62, 174, c_glow_white)
output.set(61, 173, c_glow_core)
output.set(62, 173, c_glow_core)
output.set(61, 175, c_glow_core)
output.set(62, 175, c_glow_core)
output.set(60, 174, c_glow_core)
output.set(63, 174, c_glow_core)

# Bright cyan aura ring
aura_ring = [
    (60, 173), (63, 173), (60, 175), (63, 175),
    (61, 172), (62, 172), (61, 176), (62, 176),
    (59, 174), (64, 174),
]
for gx, gy in aura_ring:
    output.set(gx, gy, c_glow_bright)

# Outer radiant glow
outer_glow = [
    (59, 173, c_glow_cyan), (64, 173, c_glow_cyan),
    (59, 175, c_glow_cyan), (64, 175, c_glow_cyan),
    (60, 172, c_glow_cyan), (63, 172, c_glow_cyan),
    (60, 176, c_glow_cyan), (63, 176, c_glow_cyan),
    (61, 171, c_glow_cyan), (62, 171, c_glow_cyan),
    (61, 177, c_glow_cyan), (62, 177, c_glow_cyan),
    # Soft translucent outer falloff
    (58, 174, c_glow_blue), (65, 174, c_glow_blue),
    (58, 173, c_glow_deep), (65, 173, c_glow_deep),
    (58, 175, c_glow_deep), (65, 175, c_glow_deep),
    (61, 170, c_glow_blue), (62, 170, c_glow_blue),
    (61, 178, c_glow_blue), (62, 178, c_glow_blue),
    (59, 172, c_glow_deep), (64, 172, c_glow_deep),
    (59, 176, c_glow_deep), (64, 176, c_glow_deep),
]
for gx, gy, gc in outer_glow:
    output.set(gx, gy, gc)

# Floating magical embers/sparks around orb
magical_sparks = [
    (57, 171, c_glow_bright),
    (58, 168, c_glow_core),
    (63, 168, c_glow_bright),
    (65, 170, c_glow_core),
    (66, 176, c_glow_cyan),
    (57, 177, c_glow_cyan),
    (64, 166, c_glow_blue),
    (59, 166, c_glow_bright),
    (61, 165, c_glow_core),
]
for sx, sy, sc in magical_sparks:
    output.set(sx, sy, sc)

# Light cast on the archway stone wall right behind the staff:
archway_wall_light = [
    (65, 175, c_rim_bright), (66, 175, c_rim_mid),
    (65, 176, c_rim_mid),    (66, 176, c_rim_dark),
    (65, 174, c_rim_bright), (66, 174, c_rim_mid),
    (65, 173, c_rim_mid),    (66, 173, c_rim_dark),
    (65, 177, c_rim_dark),   (64, 178, c_rim_dark),
]
for ax, ay, ac in archway_wall_light:
    output.set(ax, ay, ac)

# Submit finished artwork
finish(output)
