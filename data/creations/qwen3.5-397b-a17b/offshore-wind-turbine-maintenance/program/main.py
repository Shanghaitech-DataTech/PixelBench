from pixelbench_api import *

# Create 64x64 canvas for offshore wind turbine maintenance scene
c = new_canvas(64, 64, name="offshore_wind")

# Define color palette
# Sky colors
sky_light = c.color("#87CEEB", "sky_light")      # Light blue
sky_mid = c.color("#5BA3D0", "sky_mid")          # Medium blue
sky_dark = c.color("#4A90B8", "sky_dark")        # Darker blue

# Ocean colors
ocean_dark = c.color("#1E5B7C", "ocean_dark")    # Deep ocean
ocean_mid = c.color("#2E7A9E", "ocean_mid")      # Mid ocean
ocean_light = c.color("#4FA3C7", "ocean_light")  # Wave highlights
ocean_foam = c.color("#A8D8EA", "ocean_foam")    # Foam

# Turbine structure (steel)
steel_dark = c.color("#5A6B7C", "steel_dark")    # Shadow steel
steel_mid = c.color("#7A8B9C", "steel_mid")      # Mid steel
steel_light = c.color("#9AABBC", "steel_light")  # Highlight steel
steel_white = c.color("#C0D0E0", "steel_white")  # Bright steel

# Technician colors
helmet_yellow = c.color("#FFD700", "helmet_yellow")  # Safety helmet
vest_orange = c.color("#FF6B35", "vest_orange")      # Safety vest
vest_dark = c.color("#CC5522", "vest_dark")          # Vest shadow
pants_dark = c.color("#2C3E50", "pants_dark")        # Dark pants
boots_black = c.color("#1A1A1A", "boots_black")      # Boots
skin_tone = c.color("#D4A574", "skin_tone")          # Skin
gloves_white = c.color("#E8E8E8", "gloves_white")    # Gloves

# Platform colors
platform_rust = c.color("#8B4513", "platform_rust")  # Rust accents
platform_gray = c.color("#6B7B8B", "platform_gray")  # Platform deck

# Distant turbine colors
distant_gray = c.color("#8A9AAF", "distant_gray")    # Faded turbine
distant_light = c.color("#B0C4DE", "distant_light")  # Highlight

# === SKY (top ~24 pixels) ===
# Gradient sky from top to horizon
for y in range(0, 24):
    if y < 8:
        sky_col = sky_light
    elif y < 16:
        sky_col = sky_mid
    else:
        sky_col = sky_dark
    c.rect(0, y, 64, 1, sky_col)

# === OCEAN (bottom ~28 pixels, from y=36 to 63) ===
# Base ocean
c.rect(0, 36, 64, 28, ocean_dark)

# Ocean gradient layers
for y in range(36, 50):
    c.rect(0, y, 64, 1, ocean_mid)
for y in range(50, 58):
    c.rect(0, y, 64, 1, ocean_light)

# Wave patterns (simple sine-like waves)
# Wave crests
wave_y = 48
for x in range(0, 64, 8):
    offset = (x // 8) % 2
    c.rect(x, wave_y - offset, 6, 2, ocean_light)
    if x + 6 < 64:
        c.set(x + 3, wave_y - offset - 1, ocean_foam)

# More wave details - scattered foam
for x in range(4, 64, 12):
    c.rect(x, 52, 4, 1, ocean_foam)
for x in range(10, 64, 10):
    c.set(x, 54, ocean_foam)
    c.set(x + 1, 54, ocean_foam)

# Additional wave highlights
for x in range(2, 64, 7):
    c.set(x, 50, ocean_foam)
for x in range(15, 64, 15):
    c.set(x, 55, ocean_foam)
    c.set(x + 1, 55, ocean_foam)

# === MAIN TURBINE (foreground, left-center) ===
# Tower base in water
tower_x = 18
tower_base_y = 36
tower_width = 8

# Tower structure (tapering slightly)
for y in range(10, 40):
    taper = (40 - y) // 15
    tw = tower_width - taper
    tx = tower_x + taper
    if y < 36:
        c.rect(tx, y, tw, 1, steel_mid)
    else:
        # Base in water
        c.rect(tx, y, tw, 1, steel_dark)

# Tower highlights
for y in range(12, 38, 3):
    taper = (40 - y) // 15
    tx = tower_x + taper
    c.set(tx + 1, y, steel_light)

# === NACELLE (top of turbine) ===
nacelle_y = 6
nacelle_x = tower_x - 2
c.rect(nacelle_x, nacelle_y, 12, 5, steel_white)
c.rect(nacelle_x + 1, nacelle_y + 1, 10, 3, steel_light)

# === ROTOR BLADES ===
# Center hub
hub_x = tower_x + 4
hub_y = nacelle_y + 2
c.circle(hub_x, hub_y, 2, steel_dark, fill=True)

# Blade 1 (pointing up-right)
for i in range(3, 18):
    bx = hub_x + int(i * 0.5)
    by = hub_y - int(i * 0.85)
    if 0 <= bx < 64 and 0 <= by < 64:
        c.set(bx, by, steel_white)
        if i > 5:
            c.set(bx + 1, by, steel_light)

# Blade 2 (pointing down-left)
for i in range(3, 16):
    bx = hub_x - int(i * 0.6)
    by = hub_y + int(i * 0.8)
    if 0 <= bx < 64 and 0 <= by < 64:
        c.set(bx, by, steel_white)
        if i > 5:
            c.set(bx - 1, by, steel_light)

# Blade 3 (pointing right)
for i in range(3, 17):
    bx = hub_x + int(i * 0.9)
    by = hub_y + int(i * 0.3)
    if 0 <= bx < 64 and 0 <= by < 64:
        c.set(bx, by, steel_white)
        if i > 5:
            c.set(bx, by + 1, steel_light)

# === MAINTENANCE PLATFORM ===
platform_y = 22
platform_x = tower_x + tower_width
platform_w = 14
platform_h = 6

# Platform deck
c.rect(platform_x, platform_y, platform_w, 2, platform_gray)
c.rect(platform_x + 1, platform_y + 1, platform_w - 2, 1, steel_mid)

# Platform railings
for x in range(platform_x, platform_x + platform_w, 2):
    c.set(x, platform_y - 1, steel_dark)
    c.set(x, platform_y - 2, steel_light)

# Support brackets
c.rect(platform_x - 1, platform_y + 2, 2, 4, steel_dark)
c.rect(platform_x + platform_w - 1, platform_y + 2, 2, 4, steel_dark)

# === LADDER ===
ladder_x = tower_x + tower_width + 2
ladder_top = platform_y
ladder_bottom = 35

# Ladder sides
for y in range(ladder_top, ladder_bottom + 1):
    c.set(ladder_x, y, steel_dark)
    c.set(ladder_x + 3, y, steel_dark)

# Ladder rungs
for y in range(ladder_top + 2, ladder_bottom, 3):
    c.rect(ladder_x + 1, y, 2, 1, steel_mid)

# === TECHNICIAN CLIMBING ===
tech_x = ladder_x + 1
tech_y = ladder_top + 6  # Mid-climb position

# Legs (climbing pose) - more visible
c.set(tech_x, tech_y + 5, pants_dark)  # Left foot on rung
c.set(tech_x + 1, tech_y + 5, pants_dark)
c.set(tech_x + 2, tech_y + 3, pants_dark)  # Right foot higher
c.set(tech_x + 3, tech_y + 3, pants_dark)
c.set(tech_x, tech_y + 4, pants_dark)
c.set(tech_x + 2, tech_y + 2, pants_dark)

# Boots - more prominent
c.set(tech_x, tech_y + 6, boots_black)
c.set(tech_x + 1, tech_y + 6, boots_black)
c.set(tech_x + 2, tech_y + 4, boots_black)
c.set(tech_x + 3, tech_y + 4, boots_black)

# Torso with safety vest - larger and more visible
c.set(tech_x, tech_y - 3, vest_orange)
c.set(tech_x + 1, tech_y - 3, vest_orange)
c.set(tech_x + 2, tech_y - 3, vest_orange)
c.set(tech_x, tech_y - 2, vest_dark)
c.set(tech_x + 1, tech_y - 2, vest_orange)
c.set(tech_x + 2, tech_y - 2, vest_dark)
c.set(tech_x, tech_y - 1, vest_orange)
c.set(tech_x + 1, tech_y - 1, vest_orange)
c.set(tech_x + 2, tech_y - 1, vest_dark)
c.set(tech_x, tech_y, vest_dark)
c.set(tech_x + 1, tech_y, vest_dark)
c.set(tech_x + 2, tech_y, vest_orange)

# Arms (holding ladder) - more visible
c.set(tech_x - 1, tech_y - 2, skin_tone)  # Left arm
c.set(tech_x - 1, tech_y - 1, skin_tone)
c.set(tech_x - 1, tech_y, gloves_white)   # Left hand on ladder
c.set(tech_x - 1, tech_y + 1, gloves_white)
c.set(tech_x + 3, tech_y - 3, skin_tone)  # Right arm
c.set(tech_x + 3, tech_y - 2, skin_tone)
c.set(tech_x + 3, tech_y - 1, gloves_white)  # Right hand
c.set(tech_x + 3, tech_y, gloves_white)

# Head with helmet - larger and more visible
c.set(tech_x, tech_y - 5, skin_tone)
c.set(tech_x + 1, tech_y - 5, skin_tone)
c.set(tech_x + 2, tech_y - 5, skin_tone)
c.set(tech_x, tech_y - 6, helmet_yellow)
c.set(tech_x + 1, tech_y - 6, helmet_yellow)
c.set(tech_x + 2, tech_y - 6, helmet_yellow)
c.set(tech_x + 1, tech_y - 7, helmet_yellow)  # Helmet top
c.set(tech_x, tech_y - 7, helmet_yellow)
c.set(tech_x + 2, tech_y - 7, helmet_yellow)

# Safety harness straps
c.set(tech_x + 1, tech_y - 4, pants_dark)
c.set(tech_x + 1, tech_y - 3, vest_dark)

# === DISTANT TURBINES (background, right side) ===
# Turbine 1 (medium distance) - more visible
dt1_x = 46
dt1_base = 38

# Tower - thicker
for y in range(16, dt1_base):
    c.set(dt1_x, y, distant_gray)
    c.set(dt1_x + 1, y, distant_gray)
    c.set(dt1_x + 2, y, distant_light)

# Nacelle
c.rect(dt1_x - 1, 14, 5, 4, distant_light)
c.set(dt1_x + 1, 15, distant_gray)

# Blades (more defined)
c.set(dt1_x + 1, 13, distant_gray)  # Hub
# Up blade
c.set(dt1_x + 1, 11, distant_light)
c.set(dt1_x + 1, 12, distant_light)
c.set(dt1_x + 2, 10, distant_light)
# Down-left blade
c.set(dt1_x - 1, 16, distant_gray)
c.set(dt1_x - 2, 17, distant_gray)
c.set(dt1_x - 2, 18, distant_light)
# Down-right blade  
c.set(dt1_x + 3, 16, distant_gray)
c.set(dt1_x + 4, 17, distant_gray)
c.set(dt1_x + 4, 18, distant_light)

# Turbine 2 (far distance) - smaller but visible
dt2_x = 56
dt2_base = 42

# Smaller tower
for y in range(22, dt2_base):
    c.set(dt2_x, y, distant_gray)
    c.set(dt2_x + 1, y, distant_light)

# Nacelle
c.set(dt2_x - 1, 20, distant_light)
c.set(dt2_x, 20, distant_light)
c.set(dt2_x + 1, 20, distant_light)
c.set(dt2_x + 2, 20, distant_light)

# Blades (minimal but clear)
c.set(dt2_x + 1, 19, distant_gray)  # Hub
c.set(dt2_x + 1, 17, distant_light)  # Up
c.set(dt2_x + 1, 18, distant_light)
c.set(dt2_x - 1, 21, distant_gray)  # Left
c.set(dt2_x + 3, 21, distant_gray)  # Right
c.set(dt2_x - 1, 22, distant_light)
c.set(dt2_x + 3, 22, distant_light)

# === ADDITIONAL DETAILS ===
# Water splashes at tower base
for x in range(tower_x - 2, tower_x + tower_width + 2):
    if x % 3 == 0:
        c.set(x, 37, ocean_foam)
        if x % 5 == 0:
            c.set(x, 38, ocean_foam)

# Platform equipment box
c.rect(platform_x + 4, platform_y - 1, 4, 2, steel_dark)
c.set(platform_x + 5, platform_y, steel_light)

# Warning stripes on tower base
for y in range(32, 38, 2):
    c.set(tower_x, y, platform_rust)
    c.set(tower_x + tower_width - 1, y, platform_rust)

# Check stats
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=False))

# Submit
finish(c)
