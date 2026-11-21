from pixelbench_api import *

c = new_canvas(48, 48)

# --- PALETTE DEFINITION ---
# Wood Tones (Sunlit Exterior)
W_SPECULAR = '#fff2db'
W_SHINE    = '#fce2ba'
W_HI       = '#e2a96e'
W_LIGHT    = '#bd7d44'
W_MID      = '#915325'
W_DARK     = '#663615'
W_SHADOW   = '#42200b'
W_OUTLINE  = '#180a03'

# Wood Tones (Interior Rim Lighting from Magic Purple Crystal)
W_RIM_WHITE= '#faebff'
W_RIM_PALE = '#eabaff'
W_RIM_LAV  = '#d080fa'
W_RIM_MID  = '#a73ce0'
W_RIM_DARK = '#631894'

# Gold / Brass Accents
G_SHINE    = '#fff5b8'
G_HI       = '#f7de59'
G_LIGHT    = '#cfa42d'
G_MID      = '#8e6916'
G_DARK     = '#4a3407'

# Leather Grip Wrap
L_HI       = '#c99667'
L_LIGHT    = '#99683f'
L_MID      = '#6b4324'
L_DARK     = '#3d2411'

# Sprouting Leaves
V_SHINE    = '#bbf797'
V_HI       = '#8fe05a'
V_LIGHT    = '#4fa32d'
V_MID      = '#2c6b17'
V_DARK     = '#133308'

# Magic Purple (Crystal, Glow & Particles)
M_WHITE    = '#ffffff'
M_PALE     = '#f7e3ff'
M_LAVENDER = '#e69fff'
M_NEON     = '#cf5cff'
M_VIVID    = '#ab2cf2'
M_BRIGHT   = '#8815d4'
M_MID      = '#630da8'
M_DARK     = '#410775'
M_DEEP     = '#28034a'
M_DARKEST  = '#19012e'

px = {}

def set_px(x, y, col):
    if 0 <= x < 48 and 0 <= y < 48:
        px[(int(x), int(y))] = col

# --- 1. BASE & POMMEL ---
set_px(6, 45, G_DARK)
set_px(7, 45, G_MID)
set_px(8, 45, G_DARK)

set_px(7, 44, G_LIGHT)
set_px(8, 44, G_HI)
set_px(9, 44, G_MID)

set_px(8, 43, M_NEON)    # Pommel mana power gem
set_px(9, 43, G_LIGHT)
set_px(10, 43, G_DARK)

# --- 2. MAIN SHAFT (y=42 to y=20) ---
shaft_def = [
    # y, x_start, [cols]
    (42, 8, [W_LIGHT, W_MID, W_DARK]),
    (41, 9, [W_HI, W_LIGHT, W_MID, W_DARK]),
    (40, 10, [W_HI, W_LIGHT, W_MID, W_DARK]),
    (39, 10, [W_HI, W_LIGHT, W_MID, W_DARK]),
    (38, 11, [W_HI, W_LIGHT, W_MID, W_DARK]),
    (37, 12, [W_HI, W_LIGHT, W_MID, W_DARK]),
    # Gold lower grip ring at y=36
    (36, 12, [G_HI, G_LIGHT, G_MID, G_DARK]),
    # Leather wrap (y=35..29) with diagonal strapping
    (35, 13, [L_HI, L_LIGHT, L_MID, L_DARK]),
    (34, 14, [L_LIGHT, L_MID, L_HI, L_DARK]),
    (33, 14, [L_HI, L_LIGHT, L_MID, L_DARK]),
    (32, 15, [L_LIGHT, L_MID, L_HI, L_DARK]),
    (31, 16, [L_HI, L_LIGHT, L_MID, L_DARK]),
    (30, 16, [L_LIGHT, L_MID, L_HI, L_DARK]),
    (29, 17, [L_HI, L_LIGHT, L_MID, L_DARK]),
    # Gold upper grip ring at y=28
    (28, 18, [G_HI, G_LIGHT, G_MID, G_DARK]),
    # Upper shaft
    (27, 18, [W_HI, W_LIGHT, W_MID, W_DARK]),
    (26, 19, [W_HI, W_LIGHT, W_MID, W_DARK]),
    # Glowing runic vein carved into wood at y=25, 24
    (25, 20, [W_HI, M_NEON, W_MID, W_DARK]),
    (24, 20, [W_HI, M_VIVID, W_MID, W_DARK]),
    (23, 21, [W_HI, W_LIGHT, W_MID, W_DARK]),
    (22, 22, [W_HI, W_LIGHT, W_MID, W_DARK]),
    # Gold neck collar at y=21
    (21, 22, [G_HI, G_LIGHT, G_MID, G_DARK]),
    # Neck node at y=20
    (20, 23, [W_SHINE, W_HI, W_LIGHT, W_MID, W_DARK]),
]

for y, x_start, cols in shaft_def:
    set_px(x_start - 1, y, W_OUTLINE)
    for i, col in enumerate(cols):
        set_px(x_start + i, y, col)
    set_px(x_start + len(cols), y, W_OUTLINE)

# Sprouting leaves on shaft at y=23
set_px(19, 23, V_HI)
set_px(20, 23, V_LIGHT)
set_px(19, 24, V_MID)
set_px(20, 24, V_DARK)
set_px(18, 23, V_DARK)

# --- 3. CURVED HEAD (THE CROOK) ---
crook_def = [
    # y=19: rising from neck
    (19, 23, [W_SHINE, W_HI, W_LIGHT, W_MID]),
    # y=18
    (18, 23, [W_SHINE, W_HI, W_LIGHT, W_MID]),
    # y=17
    (17, 23, [W_SHINE, W_HI, W_LIGHT, W_MID]),
    # y=16: curving slightly left before arching
    (16, 23, [W_SHINE, W_HI, W_LIGHT, W_MID, W_RIM_DARK]),
    # y=15
    (15, 24, [W_SHINE, W_HI, W_LIGHT, W_RIM_MID]),
    # y=14
    (14, 24, [W_SHINE, W_HI, W_LIGHT, W_RIM_LAV]),
    # y=13
    (13, 25, [W_SHINE, W_HI, W_LIGHT, W_RIM_PALE]),
    # y=12
    (12, 26, [W_SHINE, W_HI, W_LIGHT, W_RIM_PALE]),
    # y=11
    (11, 27, [W_SHINE, W_HI, W_LIGHT, W_RIM_MID]),
    # y=10
    (10, 29, [W_SHINE, W_HI, W_LIGHT, W_MID]),
    # y=9 - rounding smoothly over top
    (9,  31, [W_SHINE, W_HI, W_LIGHT, W_MID]),
    # y=8
    (8,  33, [W_SHINE, W_HI, W_LIGHT, W_MID]),
    # y=7 - rounding toward crest
    (7,  35, [W_SHINE, W_HI, W_LIGHT, W_MID]),
    # y=6 - rounded arch crest
    (6,  37, [W_SPECULAR, W_SHINE, W_HI, W_LIGHT]),
    (5,  38, [W_SPECULAR, W_SHINE, W_HI, W_LIGHT]),
    (5,  39, [W_SPECULAR, W_SHINE, W_HI, W_LIGHT]),
    (6,  40, [W_SHINE, W_HI, W_LIGHT, W_MID]),
    # y=7 - right rounded slope
    (7,  42, [W_HI, W_LIGHT, W_MID, W_DARK]),
    # y=8
    (8,  43, [W_LIGHT, W_MID, W_DARK, W_SHADOW]),
    # y=9
    (9,  44, [W_LIGHT, W_MID, W_DARK, W_SHADOW]),
    # y=10
    (10, 45, [W_LIGHT, W_MID, W_DARK, W_SHADOW]),
    # y=11
    (11, 45, [W_LIGHT, W_MID, W_DARK, W_SHADOW]),
    # y=12 - inner surface catches purple rim light
    (12, 44, [W_RIM_PALE, W_LIGHT, W_MID, W_DARK]),
    # y=13
    (13, 44, [W_RIM_PALE, W_LIGHT, W_MID, W_DARK]),
    # y=14 - curving back under
    (14, 43, [W_RIM_PALE, W_LIGHT, W_MID, W_DARK]),
    # y=15
    (15, 41, [W_RIM_WHITE, W_RIM_PALE, W_LIGHT, W_MID]),
    # y=16
    (16, 39, [W_RIM_WHITE, W_RIM_PALE, W_LIGHT, W_MID]),
    # y=17 - terminal curl pointing toward crystal
    (17, 36, [W_RIM_WHITE, W_HI, W_MID]),
    # y=18: curled spiral tip
    (18, 34, [W_RIM_WHITE, W_HI]),
]

for y, xs, cols in crook_def:
    set_px(xs - 1, y, W_OUTLINE)
    for i, col in enumerate(cols):
        set_px(xs + i, y, col)
    set_px(xs + len(cols), y, W_OUTLINE)

# Sprout on outer arch of crook at (21, 14)
set_px(22, 14, W_HI)
set_px(21, 13, W_SHINE)
set_px(21, 14, W_MID)
set_px(20, 12, V_HI)
set_px(20, 13, V_LIGHT)
set_px(19, 12, V_DARK)

# Secondary lower wooden spur branching from (25, 20)
spur = [
    (20, 26, [W_LIGHT, W_MID]),
    (21, 27, [W_LIGHT, W_MID, W_DARK]),
    (21, 28, [W_HI, W_LIGHT, W_MID]),
    (20, 29, [W_SHINE, W_HI, W_LIGHT]),
    (19, 30, [W_RIM_WHITE, W_HI]),  # tip pointing up
]
for y, xs, cols in spur:
    set_px(xs - 1, y, W_OUTLINE)
    for i, col in enumerate(cols):
        set_px(xs + i, y, col)
    set_px(xs + len(cols), y, W_OUTLINE)

# Sprout at base of spur
set_px(28, 22, V_HI)
set_px(29, 22, V_LIGHT)
set_px(28, 23, V_DARK)

# --- 4. FLOATING MAGIC AMETHYST CRYSTAL ---
# Centered at (35, 13)
# Beautiful glowing faceted diamond crystal levitating in mid-air inside the crook
crystal = [
    # y=10: top tip
    (35, 10, M_WHITE),
    # y=11
    (34, 11, M_PALE), (35, 11, M_WHITE), (36, 11, M_LAVENDER),
    # y=12
    (33, 12, M_PALE), (34, 12, M_WHITE), (35, 12, M_WHITE), (36, 12, M_LAVENDER), (37, 12, M_NEON),
    # y=13 - widest belt
    (32, 13, M_LAVENDER), (33, 13, M_WHITE), (34, 13, M_WHITE), (35, 13, M_PALE), (36, 13, M_NEON), (37, 13, M_BRIGHT), (38, 13, M_MID),
    # y=14
    (33, 14, M_LAVENDER), (34, 14, M_PALE), (35, 14, M_NEON), (36, 14, M_VIVID), (37, 14, M_BRIGHT),
    # y=15
    (34, 15, M_NEON), (35, 15, M_VIVID), (36, 15, M_BRIGHT), (37, 15, M_MID),
    # y=16: bottom tip
    (35, 16, M_BRIGHT), (36, 16, M_DEEP),
]

for x, y, col in crystal:
    set_px(x, y, col)

# Crisp solid aura glow accents around the crystal
aura_motes = [
    (35, 9, M_LAVENDER),
    (33, 11, M_PALE), (37, 11, M_NEON),
    (31, 13, M_PALE), (39, 13, M_MID),
    (33, 15, M_NEON), (37, 15, M_VIVID),
    (35, 17, M_BRIGHT),
]
for x, y, col in aura_motes:
    set_px(x, y, col)

# --- 5. PURPLE PARTICLE EFFECTS ---
# A) 4-Pointed Sparkle Stars:
# 1. Radiant star at top-right (43, 3)
sparkle1 = [
    (43, 3, M_WHITE),
    (42, 3, M_PALE), (44, 3, M_PALE), (43, 2, M_PALE), (43, 4, M_PALE),
    (41, 3, M_NEON), (45, 3, M_NEON), (43, 1, M_NEON), (43, 5, M_NEON),
]
for x, y, col in sparkle1: set_px(x, y, col)

# 2. Celestial star at top-left (27, 3)
sparkle2 = [
    (27, 3, M_WHITE),
    (26, 3, M_PALE), (28, 3, M_PALE), (27, 2, M_PALE), (27, 4, M_PALE),
    (27, 1, M_BRIGHT), (27, 5, M_BRIGHT), (25, 3, M_BRIGHT), (29, 3, M_BRIGHT),
]
for x, y, col in sparkle2: set_px(x, y, col)

# 3. Glowing star in crook lower opening (33, 21)
sparkle3 = [
    (33, 21, M_WHITE),
    (32, 21, M_PALE), (34, 21, M_PALE), (33, 20, M_NEON), (33, 22, M_NEON),
    (33, 19, M_BRIGHT), (33, 23, M_BRIGHT),
]
for x, y, col in sparkle3: set_px(x, y, col)

# 4. Small star near outer curl (41, 18)
sparkle4 = [
    (41, 18, M_WHITE),
    (40, 18, M_PALE), (42, 18, M_PALE), (41, 17, M_NEON), (41, 19, M_NEON),
]
for x, y, col in sparkle4: set_px(x, y, col)

# 5. Small star near grip on shaft (19, 31)
sparkle5 = [
    (19, 31, M_WHITE),
    (18, 31, M_LAVENDER), (20, 31, M_LAVENDER), (19, 30, M_NEON), (19, 32, M_NEON),
]
for x, y, col in sparkle5: set_px(x, y, col)

# B) Floating Magical Motes & Orbital Stream:
motes = [
    # Top celestial sparks
    (32, 2, M_LAVENDER),
    (36, 1, M_PALE),
    (39, 2, M_NEON),
    (46, 2, M_VIVID),
    (47, 5, M_PALE),
    (46, 7, M_NEON),

    # Outer orbital cascade
    (47, 10, M_WHITE),
    (46, 12, M_NEON),
    (47, 14, M_LAVENDER),
    (46, 16, M_BRIGHT),
    (45, 19, M_VIVID),
    (44, 21, M_PALE),
    (42, 23, M_WHITE),
    (39, 24, M_NEON),
    (36, 25, M_LAVENDER),
    (31, 25, M_VIVID),
    (28, 24, M_PALE),

    # Magic trail spiraling along and across the shaft:
    (26, 23, M_NEON),
    (24, 21, M_WHITE),   # Spark crossing over the gold neck collar (3D depth!)
    (24, 25, M_LAVENDER),
    (23, 27, M_PALE),
    (21, 29, M_VIVID),
    (17, 34, M_LAVENDER),
    (16, 36, M_WHITE),
    (14, 38, M_PALE),
    (13, 41, M_NEON),
    (11, 43, M_LAVENDER),
    (9, 46, M_VIVID),

    # Spark crossing right arch
    (44, 11, M_WHITE),

    # Ambient sparks on left side
    (21, 9, M_PALE),
    (22, 7, M_NEON),
    (18, 11, M_VIVID),
    (17, 15, M_PALE),
    (16, 17, M_LAVENDER),
    (15, 20, M_NEON),
    (16, 22, M_BRIGHT),
]
for x, y, col in motes:
    set_px(x, y, col)

# Render to canvas
for (x, y), col in px.items():
    c.set(x, y, col)

print(c.stats_text())
view(c)
finish(c)
