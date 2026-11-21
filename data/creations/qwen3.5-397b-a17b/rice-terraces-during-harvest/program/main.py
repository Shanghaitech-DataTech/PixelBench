from pixelbench_api import *

# Create 64x64 canvas
c = new_canvas(64, 64, name="rice_terraces")

# Define palette - earth tones, golden rice colors, water, farmers, houses
# Background/mountain colors (darker for depth)
c.color("#2d3a2a", "mountain_dark")      # 0 - deepest shadow
c.color("#3d4a3a", "mountain_mid")       # 1 - mid shadow
c.color("#4d5a4a", "mountain_light")     # 2 - lighter mountain
c.color("#5a6a5a", "hill_base")          # 3 - hill base

# Terrace colors - golden rice harvest tones (layered by depth)
c.color("#8b7355", "terrace_deep")       # 4 - deepest terrace (darker)
c.color("#a08060", "terrace_mid_dark")   # 5 - mid-dark terrace
c.color("#b89060", "terrace_mid")        # 6 - mid terrace
c.color("#d4a050", "terrice_gold")       # 7 - golden rice
c.color("#e8b850", "rice_bright")        # 8 - bright harvest gold
c.color("#f0c860", "rice_highlight")     # 9 - highlight

# Water in terraces
c.color("#4a6080", "water_dark")         # 10 - deep water
c.color("#6080a0", "water_mid")          # 11 - mid water
c.color("#7090b0", "water_light")        # 12 - light water reflection

# Ridge/border colors
c.color("#6b5343", "ridge_dark")         # 13 - terrace edge shadow
c.color("#8b6b53", "ridge_mid")          # 14 - terrace edge
c.color("#ab8b6b", "ridge_light")        # 15 - terrace edge highlight

# Farmer colors
c.color("#8b4513", "farmer_skin")        # 16 - skin tone
c.color("#5c4033", "farmer_hair")        # 17 - dark hair
c.color("#6b8e23", "farmer_shirt1")      # 18 - farmer 1 shirt (green)
c.color("#8b6b43", "farmer_pants1")      # 19 - farmer 1 pants
c.color("#cd853f", "farmer_shirt2")      # 20 - farmer 2 shirt (orange)
c.color("#556b2f", "farmer_pants2")      # 21 - farmer 2 pants
c.color("#3d2818", "farmer_shadow")      # 22 - farmer shadow

# Village house colors (distant, muted)
c.color("#8b7355", "house_wall")         # 23 - house walls (muted brown)
c.color("#6b5343", "house_shadow")       # 24 - house shadow
c.color("#5c4033", "house_roof")         # 25 - roof (dark thatch)
c.color("#706050", "house_roof_light")   # 26 - roof highlight
c.color("#4a3828", "house_door")         # 27 - doorway

# Sky/horizon (very top, minimal)
c.color("#a8c8d8", "sky_light")          # 28 - distant sky
c.color("#b8d8e8", "sky_bright")         # 29 - brighter sky

# Additional depth tones
c.color("#3a4a3a", "depth_1")            # 30
c.color("#4a5a4a", "depth_2")            # 31
c.color("#5a6a5a", "depth_3")            # 32
c.color("#6a7a6a", "depth_4")            # 33
c.color("#7a8a7a", "depth_5")            # 34
c.color("#8a9a8a", "depth_6")            # 35

# More rice variations
c.color("#c09050", "rice_1")             # 36
c.color("#d0a055", "rice_2")             # 37
c.color("#e0b055", "rice_3")             # 38
c.color("#e8c060", "rice_4")             # 39
c.color("#f0d065", "rice_5")             # 40

# More water variations
c.color("#507090", "water_1")            # 41
c.color("#587898", "water_2")            # 42
c.color("#6080a0", "water_3")            # 43
c.color("#6888a8", "water_4")            # 44

# More ridge variations
c.color("#7a5a40", "ridge_1")            # 45
c.color("#8a6a50", "ridge_2")            # 46
c.color("#9a7a60", "ridge_3")            # 47
c.color("#aa8a70", "ridge_4")            # 48

# Path colors
c.color("#6b5848", "path_dark")          # 49
c.color("#8b7868", "path_mid")           # 50
c.color("#ab9888", "path_light")         # 51

# Vegetation accents
c.color("#5a7a5a", "veg_dark")           # 52
c.color("#6a8a6a", "veg_mid")            # 53
c.color("#7a9a7a", "veg_light")          # 54

# Shadow tones for depth
c.color("#2a3025", "shadow_deep")        # 55
c.color("#354035", "shadow_mid")         # 56
c.color("#405040", "shadow_light")       # 57

# Harvest details
c.color("#b88040", "harvest_1")          # 58
c.color("#c89045", "harvest_2")          # 59
c.color("#d8a045", "harvest_3")          # 60

# Farmer tools
c.color("#a08060", "tool_wood")          # 61
c.color("#707070", "tool_metal")         # 62

# More house details
c.color("#7a6858", "house_wall_light")   # 63
c.color("#5a4838", "house_wall_dark")    # 64

# Extra depth layers
c.color("#354535", "layer_1")            # 65
c.color("#455545", "layer_2")            # 66
c.color("#556555", "layer_3")            # 67
c.color("#657565", "layer_4")            # 68
c.color("#758575", "layer_5")            # 69
c.color("#859585", "layer_6")            # 70

# Rice sheaves
c.color("#d8b050", "sheaf_1")            # 71
c.color("#e8c055", "sheaf_2")            # 72
c.color("#f8d055", "sheaf_3")            # 73

# Mist/atmosphere
c.color("#90a0a0", "mist_1")             # 74
c.color("#a0b0b0", "mist_2")             # 75

# Ground/soil
c.color("#5a4a3a", "soil_1")             # 76
c.color("#6a5a4a", "soil_2")             # 77
c.color("#7a6a5a", "soil_3")             # 78

# Final accents
c.color("#908070", "accent_1")           # 79
c.color("#a09080", "accent_2")           # 80
c.color("#b0a090", "accent_3")           # 81
c.color("#c0b0a0", "accent_4")           # 82
c.color("#d0c0b0", "accent_5")           # 83
c.color("#e0d0c0", "accent_6")           # 84
c.color("#f0e0d0", "accent_7")           # 85

print(f"Colors registered: {len(c.palette())}")

# Draw the terraces from back (top of canvas) to front (bottom)
# Top-down view: y=0 is distant (top of mountain), y=63 is foreground

# Draw background sky at very top (first few rows)
c.rect(0, 0, 64, 4, "sky_light", fill=True)
c.rect(0, 3, 64, 2, "sky_bright", fill=True)

# Mountain contours - draw curved terrace levels
# Each terrace is a curved band following mountain shape

# Distant terraces (top of canvas, smaller, darker values)
# Terrace 1 (furthest)
for x in range(64):
    y_base = 8 + int(3 * ((x - 32) / 32) ** 2)
    c.set(x, y_base, "layer_1")
    c.set(x, y_base + 1, "layer_1")
    c.set(x, y_base + 2, "terrace_deep")

# Terrace 2
for x in range(64):
    y_base = 12 + int(4 * ((x - 32) / 32) ** 2)
    for dy in range(4):
        c.set(x, y_base + dy, "depth_2" if dy < 2 else "terrace_mid_dark")

# Terrace 3
for x in range(64):
    y_base = 17 + int(5 * ((x - 32) / 32) ** 2)
    for dy in range(5):
        c.set(x, y_base + dy, "depth_3" if dy < 2 else "terrace_mid")

# Terrace 4
for x in range(64):
    y_base = 23 + int(5 * ((x - 32) / 32) ** 2)
    for dy in range(5):
        c.set(x, y_base + dy, "depth_4" if dy < 2 else "rice_1" if dy == 2 else "rice_2")

# Terrace 5
for x in range(64):
    y_base = 29 + int(6 * ((x - 32) / 32) ** 2)
    for dy in range(6):
        c.set(x, y_base + dy, "depth_5" if dy < 2 else "rice_3" if dy < 4 else "ridge_1")

# Terrace 6
for x in range(64):
    y_base = 36 + int(6 * ((x - 32) / 32) ** 2)
    for dy in range(6):
        c.set(x, y_base + dy, "depth_6" if dy < 2 else "rice_4" if dy < 4 else "ridge_2")

# Terrace 7 (middle ground)
for x in range(64):
    y_base = 43 + int(5 * ((x - 32) / 32) ** 2)
    for dy in range(5):
        c.set(x, y_base + dy, "layer_5" if dy < 1 else "rice_5" if dy < 4 else "ridge_3")

# Terrace 8
for x in range(64):
    y_base = 49 + int(4 * ((x - 32) / 32) ** 2)
    for dy in range(5):
        c.set(x, y_base + dy, "layer_4" if dy < 1 else "harvest_2" if dy < 4 else "ridge_4")

# Terrace 9 (foreground)
for x in range(64):
    y_base = 54 + int(3 * ((x - 32) / 32) ** 2)
    for dy in range(8):
        if y_base + dy < 64:
            c.set(x, y_base + dy, "rice_bright" if dy < 5 else "ridge_light")

# Add water reflections in some terraces
# Water in terrace 3
for x in range(20, 45):
    y_base = 17 + int(5 * ((x - 32) / 32) ** 2)
    for dy in range(2):
        c.set(x, y_base + 2 + dy, "water_1")

# Water in terrace 5
for x in range(15, 50):
    y_base = 29 + int(6 * ((x - 32) / 32) ** 2)
    for dy in range(2):
        c.set(x, y_base + 2 + dy, "water_2")

# Water in terrace 7
for x in range(25, 40):
    y_base = 43 + int(5 * ((x - 32) / 32) ** 2)
    for dy in range(1):
        c.set(x, y_base + 1 + dy, "water_3")

# Add ridge borders between terraces
for x in range(64):
    # Ridge lines
    y1 = 11 + int(4 * ((x - 32) / 32) ** 2)
    c.set(x, y1, "ridge_dark")
    
    y2 = 16 + int(5 * ((x - 32) / 32) ** 2)
    c.set(x, y2, "ridge_mid")
    
    y3 = 22 + int(5 * ((x - 32) / 32) ** 2)
    c.set(x, y3, "ridge_1")
    
    y4 = 28 + int(6 * ((x - 32) / 32) ** 2)
    c.set(x, y4, "ridge_2")
    
    y5 = 35 + int(6 * ((x - 32) / 32) ** 2)
    c.set(x, y5, "ridge_3")
    
    y6 = 42 + int(5 * ((x - 32) / 32) ** 2)
    c.set(x, y6, "ridge_4")
    
    y7 = 48 + int(4 * ((x - 32) / 32) ** 2)
    c.set(x, y7, "ridge_light")

# Draw village houses in distance (top area, y=5-10)
# House 1
hx1, hy1 = 10, 5
c.rect(hx1, hy1, 6, 4, "house_wall", fill=True)
c.rect(hx1, hy1, 6, 1, "house_roof", fill=True)  # roof top
c.set(hx1 + 3, hy1 + 2, "house_door")
c.set(hx1 + 3, hy1 + 3, "house_door")

# House 2
hx2, hy2 = 20, 6
c.rect(hx2, hy2, 5, 4, "house_wall_light", fill=True)
c.rect(hx2, hy2, 5, 1, "house_roof", fill=True)
c.set(hx2 + 2, hy2 + 2, "house_door")

# House 3
hx3, hy3 = 45, 5
c.rect(hx3, hy3, 6, 5, "house_wall", fill=True)
c.rect(hx3, hy3, 6, 1, "house_roof_light", fill=True)
c.set(hx3 + 3, hy3 + 3, "house_door")
c.set(hx3 + 3, hy3 + 4, "house_door")

# House 4 (smaller, further)
hx4, hy4 = 52, 7
c.rect(hx4, hy4, 4, 3, "house_wall_dark", fill=True)
c.rect(hx4, hy4, 4, 1, "house_roof", fill=True)

# Draw two farmers on ridges
# Farmer 1 - on ridge at y~28, x~20
fx1, fy1 = 20, 27
# Body (2x3 pixels)
c.set(fx1, fy1, "farmer_hair")
c.set(fx1 + 1, fy1, "farmer_hair")
c.set(fx1, fy1 + 1, "farmer_shirt1")
c.set(fx1 + 1, fy1 + 1, "farmer_shirt1")
c.set(fx1, fy1 + 2, "farmer_pants1")
c.set(fx1 + 1, fy1 + 2, "farmer_pants1")
# Tool
c.set(fx1 + 2, fy1 + 1, "tool_wood")
c.set(fx1 + 2, fy1 + 2, "tool_wood")

# Farmer 2 - on ridge at y~42, x~45
fx2, fy2 = 45, 41
c.set(fx2, fy2, "farmer_hair")
c.set(fx2 + 1, fy2, "farmer_hair")
c.set(fx2, fy2 + 1, "farmer_shirt2")
c.set(fx2 + 1, fy2 + 1, "farmer_shirt2")
c.set(fx2, fy2 + 2, "farmer_pants2")
c.set(fx2 + 1, fy2 + 2, "farmer_pants2")
# Basket
c.set(fx2 + 2, fy2 + 1, "sheaf_1")
c.set(fx2 + 2, fy2 + 2, "sheaf_2")

# Add some harvested rice sheaves on terraces
# Sheaf group 1
sx1, sy1 = 30, 35
c.set(sx1, sy1, "sheaf_1")
c.set(sx1 + 1, sy1, "sheaf_2")
c.set(sx1, sy1 + 1, "sheaf_3")

# Sheaf group 2
sx2, sy2 = 50, 50
c.set(sx2, sy2, "sheaf_2")
c.set(sx2 + 1, sy2, "sheaf_1")
c.set(sx2 + 1, sy2 + 1, "sheaf_3")

# Sheaf group 3
sx3, sy3 = 12, 22
c.set(sx3, sy3, "sheaf_3")
c.set(sx3 + 1, sy3, "sheaf_2")

# Add path winding through terraces
for i in range(10):
    px = 55 + int(2 * ((i - 5) / 5) ** 2)
    py = 15 + i * 4
    if py < 60:
        c.set(px, py, "path_mid")
        c.set(px - 1, py, "path_light")
        c.set(px, py + 1, "path_mid")

# Add some vegetation accents on terrace edges
for x in [5, 15, 25, 35, 45, 55]:
    for y in [20, 30, 40, 50]:
        if c.get(x, y) not in [0, 1, 2]:  # Not on house area
            c.set(x, y, "veg_mid")
            c.set(x + 1, y, "veg_light")

# Add mist/atmosphere in distant areas
for x in range(10, 55):
    for y in range(6, 12):
        if c.get(x, y) in [28, 29]:  # Sky area
            if (x + y) % 7 == 0:
                c.set(x, y, "mist_1")

print(f"Stats: {c.stats_text()}")

# Submit
finish(c)
