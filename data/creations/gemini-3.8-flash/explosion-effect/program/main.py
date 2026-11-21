import numpy as np

c = new_canvas(64, 64, name="explosion")

# 12-color cohesive retro arcade explosion palette
PAL = [
    (0, None),                # 0: transparent
    (1, "#180200"),           # 1: Charcoal soot outline
    (2, "#3d0400"),           # 2: Dark charred red
    (3, "#740800"),           # 3: Deep crimson
    (4, "#b01000"),           # 4: Saturated flame red
    (5, "#e02e00"),           # 5: Fiery orange-red
    (6, "#f85c00"),           # 6: Vibrant fire orange
    (7, "#ffa000"),           # 7: Golden amber
    (8, "#ffd000"),           # 8: Golden yellow
    (9, "#ffe400"),           # 9: Blazing bright yellow
    (10, "#fff8b4"),          # 10: Cream hot yellow
    (11, "#ffffff"),          # 11: Pure white hot
]

for idx, hex_val in PAL:
    if hex_val:
        c.color(hex_val)

grid = np.zeros((64, 64), dtype=int)

# =============================================================================
# FRAME 1: Bright Yellow Fireball at center (15.5, 32)
# =============================================================================
f1_plumes = [
    # (x, y, radius, heat)
    (15.5, 32.0, 8.5, 1.4),    # Main hot core
    (12.0, 28.0, 6.0, 1.1),    # Top-left lobe
    (19.0, 27.0, 6.5, 1.1),    # Top-right lobe
    (11.0, 35.5, 6.0, 1.05),   # Bottom-left lobe
    (19.5, 36.0, 6.5, 1.1),    # Bottom-right lobe
    (15.5, 23.0, 4.5, 0.95),   # Top plume lick
    (15.5, 41.0, 4.5, 0.95),   # Bottom plume lick
    (7.5, 32.0, 4.2, 0.95),    # Left flare lick
    (23.5, 32.0, 4.2, 0.95),   # Right flare lick
    (9.0, 24.5, 3.5, 0.85),    # Diagonal flare
    (22.0, 23.5, 3.5, 0.85),   # Diagonal flare
    (9.0, 39.5, 3.5, 0.85),    # Diagonal flare
    (22.0, 40.5, 3.5, 0.85),   # Diagonal flare
]

for y in range(64):
    for x in range(30):
        density = 0.0
        heat = 0.0
        total_w = 0.0
        for px, py, pr, ph in f1_plumes:
            d2 = (x - px)**2 + (y - py)**2
            if d2 < (pr * 1.5)**2:
                norm_d = np.sqrt(d2) / pr
                if norm_d < 1.0:
                    val = (1.0 - norm_d**2)**2
                    density += val
                    heat += val * ph
                    total_w += val
                elif norm_d < 1.3:
                    val = (1.0 - ((norm_d - 1.0) / 0.3)**2) * 0.1
                    density += val
        
        if density > 0.05:
            avg_heat = (heat / max(0.001, total_w)) * density
            d_center = np.hypot(x - 15.5, y - 32)
            # Frame 1: DOMINANT BRIGHT YELLOW FIREBALL
            if avg_heat > 1.3 and d_center < 3.2:
                grid[y, x] = 11  # White core
            elif avg_heat > 1.0 and d_center < 5.8:
                grid[y, x] = 10  # Cream yellow
            elif density > 0.38:
                grid[y, x] = 9   # Blazing bright yellow (DOMINANT!)
            elif density > 0.28:
                grid[y, x] = 8   # Golden yellow
            elif density > 0.20:
                grid[y, x] = 7   # Golden amber
            elif density > 0.14:
                grid[y, x] = 6   # Vibrant fire orange
            elif density > 0.09:
                grid[y, x] = 5   # Fiery orange-red
            elif density > 0.05:
                grid[y, x] = 4   # Flame red
            else:
                grid[y, x] = 3   # Crimson outline

# Frame 1 sparks & flame tips
f1_sparks = [
    (3, 21, 9), (4, 22, 7),
    (26, 20, 9), (25, 21, 7),
    (2, 39, 8), (3, 40, 6),
    (26, 42, 8), (25, 41, 6),
    (15, 17, 9), (15, 18, 7),
    (15, 46, 9), (15, 45, 7),
    (3, 32, 9), (4, 32, 7),
    (27, 32, 9), (26, 32, 7),
]
for sx, sy, sc in f1_sparks:
    if 0 <= sx < 30 and 0 <= sy < 64:
        grid[sy, sx] = sc


# =============================================================================
# FRAME 2: Expanding Orange-Red Blast with Sparks (Centered at x=49.5, y=32)
# =============================================================================
f2_plumes = [
    # (x, y, radius, heat)
    (49.5, 32.0, 5.5, 1.4),    # Central core
    (49.0, 18.0, 7.0, 0.85),   # Top plume
    (56.5, 21.5, 8.2, 0.90),   # Upper-right mega billow
    (58.5, 32.0, 7.5, 0.85),   # Right lateral plume
    (55.5, 42.0, 7.8, 0.85),   # Lower-right plume
    (48.5, 46.5, 7.2, 0.85),   # Bottom plume
    (42.5, 41.0, 6.8, 0.85),   # Lower-left plume
    (40.0, 32.0, 6.2, 0.85),   # Left plume
    (42.5, 22.5, 6.8, 0.85),   # Upper-left plume
    # Secondary billow swellings
    (38.5, 27.0, 4.0, 0.75),
    (60.0, 26.5, 4.8, 0.80),
    (38.5, 37.0, 4.0, 0.75),
    (59.5, 38.0, 4.8, 0.80),
    (44.5, 15.5, 4.0, 0.75),
    (53.0, 15.5, 4.2, 0.75),
    (44.5, 48.5, 4.0, 0.75),
    (53.5, 48.0, 4.2, 0.75),
]

for y in range(64):
    for x in range(33, 64):
        density = 0.0
        heat = 0.0
        total_w = 0.0
        for px, py, pr, ph in f2_plumes:
            d2 = (x - px)**2 + (y - py)**2
            if d2 < (pr * 1.5)**2:
                norm_d = np.sqrt(d2) / pr
                if norm_d < 1.0:
                    val = (1.0 - norm_d**2)**2
                    density += val
                    heat += val * ph
                    total_w += val
                elif norm_d < 1.3:
                    val = (1.0 - ((norm_d - 1.0) / 0.3)**2) * 0.1
                    density += val
        
        d_center = np.hypot(x - 49.5, y - 32)
        if d_center < 9.0 or density > 0.04:
            # FRAME 2: DOMINATED BY ORANGE AND RED!
            if d_center < 2.0:
                grid[y, x] = 11  # White hot core
            elif d_center < 3.2:
                grid[y, x] = 10  # Cream yellow
            elif d_center < 4.8:
                grid[y, x] = 9   # Bright yellow
            elif d_center < 6.8:
                grid[y, x] = 8   # Golden yellow
            elif d_center < 9.0:
                grid[y, x] = 7   # Golden amber
            elif density > 0.30:
                grid[y, x] = 6   # Vibrant fire orange (DOMINANT!)
            elif density > 0.15:
                grid[y, x] = 5   # Fiery orange-red (DOMINANT!)
            elif density > 0.08:
                grid[y, x] = 4   # Saturated flame red
            elif density > 0.04:
                grid[y, x] = 3   # Deep crimson
            elif density > 0.02:
                grid[y, x] = 2   # Dark charred red
            else:
                grid[y, x] = 1   # Charcoal soot outline

# Warm billow crest highlights in Frame 2
billow_highlights = [
    # Upper-right mega billow
    (55, 19, 7), (56, 19, 7), (57, 20, 7), (56, 20, 8),
    # Top plume
    (48, 16, 7), (49, 16, 7), (48, 17, 7),
    # Upper-left plume
    (42, 21, 7), (43, 21, 7),
    # Right lateral plume
    (58, 30, 7), (58, 31, 7), (59, 31, 7),
    # Lower-right plume
    (55, 43, 7), (56, 43, 7), (55, 44, 7),
    # Bottom plume
    (48, 47, 7), (49, 47, 7),
    # Lower-left plume
    (42, 42, 7), (43, 42, 7),
    # Left lateral plume
    (39, 31, 7), (39, 32, 7),
]
for hx, hy, hcol in billow_highlights:
    if 33 <= hx < 64 and 0 <= hy < 64 and grid[hy, hx] == 6:
        grid[hy, hx] = hcol

# Natural crevices between billows on the outer perimeter ONLY
f2_crevices = [
    # Top crevices
    (46, 18, 3), (47, 18, 3),
    (52, 18, 3), (53, 19, 3),
    # Lateral crevices
    (38, 27, 3), (59, 26, 3),
    (38, 36, 3), (59, 36, 3),
    # Bottom crevices
    (45, 47, 3), (46, 46, 3),
    (52, 46, 3), (53, 47, 3),
]
for cx, cy, col in f2_crevices:
    if 33 <= cx < 64 and 0 <= cy < 64 and grid[cy, cx] in [4, 5]:
        grid[cy, cx] = col

# SPARKS FOR FRAME 2:
# High-velocity explosive embers radiating outward!
f2_sparks = [
    # High-altitude sparks (flying top-right)
    (58, 3, 11), (59, 4, 9), (60, 5, 7),
    (52, 4, 11), (51, 5, 8),
    (47, 3, 9),
    (41, 5, 10), (40, 6, 8),
    (36, 8, 9), (35, 9, 7),

    # Mid-high lateral sparks
    (63, 13, 11), (62, 14, 8),
    (63, 20, 10), (62, 21, 7),
    (34, 14, 8), (33, 19, 9),

    # Far-right high-speed sparks
    (63, 28, 11), (62, 28, 8),
    (63, 35, 10), (63, 36, 7),
    (63, 42, 11), (62, 43, 8),

    # Far-left sparks (keeping x >= 33!)
    (33, 25, 10), (34, 26, 7),
    (33, 32, 11), (34, 32, 8),
    (33, 39, 10), (34, 40, 7),

    # Low-altitude sparks (flying bottom-right & bottom-left)
    (62, 49, 9), (61, 50, 7),
    (58, 55, 11), (59, 56, 8),
    (53, 59, 10), (52, 58, 7),
    (48, 62, 11), (48, 61, 9), (48, 60, 6),
    (43, 59, 10), (42, 58, 7),
    (37, 54, 9), (36, 53, 7),
    (34, 47, 8),
    # Floating embers
    (61, 9, 8), (37, 12, 8), (44, 9, 8), (55, 8, 8),
    (60, 53, 7), (40, 57, 7), (47, 57, 8),
]

for sx, sy, sc in f2_sparks:
    if 33 <= sx < 64 and 0 <= sy < 64:
        grid[sy, sx] = sc

# Ensure columns 30, 31, 32 are strictly transparent for a clean gap
grid[:, 30] = 0
grid[:, 31] = 0
grid[:, 32] = 0

# Render to canvas
for y in range(64):
    for x in range(64):
        idx = grid[y, x]
        if idx > 0 and PAL[idx][1]:
            c.set(x, y, PAL[idx][1])

view(c)
finish(c)
