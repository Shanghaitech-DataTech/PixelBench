import sys
from pixelbench_api import *

# battery-status-set: 64x64 pixel art
# Four battery icons in one horizontal row:
# 1. 100% charge
# 2. 60% charge
# 3. 20% charge
# 4. Active charging
# Identical battery outlines, clearly distinguished fill states.

c = new_canvas(64, 64, name="battery_status_set")
c.rect(0, 0, 64, 64, "#0e111a")

# Palette definition
# Metallic chassis & casing
metal_specular = "#cbd5e1"
metal_highlight = "#94a3b8"
metal_light = "#64748b"
metal_mid = "#334155"
metal_dark = "#1e293b"
casing_border = "#0a0d14"

# Glass chamber background & unlit recessed slots
chamber_bg = "#0d1017"
unlit_slot_bg = "#141822"
unlit_slot_border = "#0f131a"
unlit_slot_hi = "#1a202c"
unlit_glass_sheen = "#232b3b"

# Green palette (100% and 60% charge)
g_spec = "#d1fae5"
g_hi = "#6ee7b7"
g_light = "#34d399"
g_main = "#10b981"
g_dark = "#059669"
g_deep = "#047857"

# Red palette (20% low charge warning)
r_spec = "#fee2e2"
r_hi = "#fca5a5"
r_light = "#f87171"
r_main = "#ef4444"
r_dark = "#dc2626"
r_deep = "#991b1b"

# Cyan palette (Charging energy cells)
c_spec = "#cffafe"
c_hi = "#67e8f9"
c_light = "#22d3ee"
c_main = "#06b6d4"
c_dark = "#0891b2"
c_deep = "#0e7490"

# Yellow/White for lightning bolt & sparks
y_white = "#ffffff"
y_spec = "#fef9c3"
y_hi = "#fef08a"
y_main = "#facc15"
y_dark = "#eab308"
y_deep = "#ca8a04"
bolt_border = "#0a0d14"

def draw_casing(bx):
    # 1. Top positive terminal cap: x = bx+3..bx+7 (width 5), y = 14..16 (height 3)
    c.rect(bx + 3, 14, 5, 3, casing_border)
    c.set(bx + 4, 14, metal_specular)
    c.set(bx + 5, 14, metal_highlight)
    c.set(bx + 6, 14, metal_light)
    c.set(bx + 4, 15, metal_highlight)
    c.set(bx + 5, 15, metal_light)
    c.set(bx + 6, 15, metal_mid)
    c.set(bx + 4, 16, metal_light)
    c.set(bx + 5, 16, metal_mid)
    c.set(bx + 6, 16, metal_dark)

    # 2. Main battery outer outline: bx..bx+10, y = 17..49 (width 11, height 33)
    c.rect(bx, 17, 11, 33, casing_border)
    # Rounded corners
    c.set(bx, 17, "#0e111a")
    c.set(bx + 10, 17, "#0e111a")
    c.set(bx, 49, "#0e111a")
    c.set(bx + 10, 49, "#0e111a")

    # 3. Inner metallic bezel & plates
    # Top shoulder plate: y = 18
    c.line(bx + 1, 18, bx + 9, 18, metal_mid)
    c.set(bx + 1, 18, metal_highlight)
    c.set(bx + 2, 18, metal_light)
    c.set(bx + 9, 18, metal_dark)
    
    # Bottom base plate: y = 48
    c.line(bx + 1, 48, bx + 9, 48, metal_dark)
    c.set(bx + 1, 48, metal_mid)
    c.set(bx + 9, 48, casing_border)

    # Left & right inner rims
    c.line(bx + 1, 19, bx + 1, 47, metal_mid)
    c.line(bx + 9, 19, bx + 9, 47, metal_dark)

    # 4. Glass chamber interior: bx+2..bx+8 (width 7), y = 19..47 (height 29)
    c.rect(bx + 2, 19, 7, 29, chamber_bg)

    # 5 unlit recessed cell slots: y = 20..24, 26..30, 32..36, 38..42, 44..48
    for sy in [20, 26, 32, 38, 44]:
        c.rect(bx + 2, sy, 7, 5, unlit_slot_bg)
        c.line(bx + 2, sy, bx + 8, sy, unlit_slot_hi)
        c.line(bx + 2, sy, bx + 2, sy + 4, unlit_slot_hi)
        c.line(bx + 2, sy + 4, bx + 8, sy + 4, unlit_slot_border)
        c.line(bx + 8, sy, bx + 8, sy + 4, unlit_slot_border)
        c.set(bx + 2, sy, unlit_glass_sheen)

def draw_lit_bar(bx, sy, spec, hi, light, main, dark, deep):
    # 7x5 energized cell (x: bx+2..bx+8, y: sy..sy+4)
    c.rect(bx + 2, sy, 7, 5, main)
    # Top highlight line
    c.line(bx + 2, sy, bx + 7, sy, light)
    c.set(bx + 2, sy, spec)
    c.set(bx + 3, sy, hi)
    # Left highlight line
    c.line(bx + 2, sy + 1, bx + 2, sy + 3, light)
    c.set(bx + 2, sy + 1, hi)
    # Bottom shadow line
    c.line(bx + 3, sy + 4, bx + 8, sy + 4, deep)
    # Right shadow line
    c.line(bx + 8, sy + 1, bx + 8, sy + 3, dark)
    c.set(bx + 8, sy + 4, deep)
    # Glowing cell core
    c.set(bx + 4, sy + 2, hi)
    c.set(bx + 5, sy + 2, light)

# Subtle ambient floor shadow under each battery
for i in range(4):
    bx = 4 + i * 15
    c.rect(bx + 1, 51, 9, 2, "#080a11")
    c.rect(bx + 2, 53, 7, 1, "#0a0c14")

# Draw identical casings for all four batteries
for i in range(4):
    draw_casing(4 + i * 15)

# --- Icon 1: 100% Charge (all 5 segments energized green) ---
bx0 = 4
for sy in [20, 26, 32, 38, 44]:
    draw_lit_bar(bx0, sy, g_spec, g_hi, g_light, g_main, g_dark, g_deep)

# --- Icon 2: 60% Charge (bottom 3 segments energized green, top 2 unlit) ---
bx1 = 19
for sy in [32, 38, 44]:
    draw_lit_bar(bx1, sy, g_spec, g_hi, g_light, g_main, g_dark, g_deep)

# --- Icon 3: 20% Charge (bottom 1 segment energized red, top 4 unlit) ---
bx2 = 34
draw_lit_bar(bx2, 44, r_spec, r_hi, r_light, r_main, r_dark, r_deep)

# --- Icon 4: Active Charging (cyan charging cells with electric lightning bolt) ---
bx3 = 49
for sy in [32, 38, 44]:
    draw_lit_bar(bx3, sy, c_spec, c_hi, c_light, c_main, c_dark, c_deep)

# Centered lightning bolt
bolt_pixels = [
    (bx3 + 6, 22), (bx3 + 7, 22),
    (bx3 + 6, 23), (bx3 + 7, 23),
    (bx3 + 5, 24), (bx3 + 6, 24),
    (bx3 + 5, 25), (bx3 + 6, 25),
    (bx3 + 4, 26), (bx3 + 5, 26),
    (bx3 + 4, 27), (bx3 + 5, 27),
    (bx3 + 3, 28), (bx3 + 4, 28),
    (bx3 + 3, 29), (bx3 + 4, 29),
    (bx3 + 2, 30), (bx3 + 3, 30),
    (bx3 + 2, 31), (bx3 + 3, 31), (bx3 + 4, 31), (bx3 + 5, 31), (bx3 + 6, 31), (bx3 + 7, 31), (bx3 + 8, 31),
    (bx3 + 6, 32), (bx3 + 7, 32), (bx3 + 8, 32),
    (bx3 + 6, 33), (bx3 + 7, 33),
    (bx3 + 5, 34), (bx3 + 6, 34),
    (bx3 + 5, 35), (bx3 + 6, 35),
    (bx3 + 4, 36), (bx3 + 5, 36),
    (bx3 + 4, 37), (bx3 + 5, 37),
    (bx3 + 3, 38), (bx3 + 4, 38),
    (bx3 + 3, 39), (bx3 + 4, 39),
    (bx3 + 3, 40),
    (bx3 + 3, 41),
]

bolt_set = set(bolt_pixels)

# Crisp dark outline around bolt, strictly clamped to interior chamber
for px, py in bolt_pixels:
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            pt = (px + dx, py + dy)
            if pt not in bolt_set:
                if (bx3 + 2 <= pt[0] <= bx3 + 8) and (19 <= pt[1] <= 47):
                    c.set(pt[0], pt[1], bolt_border)

# Main golden yellow fill
for px, py in bolt_pixels:
    c.set(px, py, y_main)

# Warm gold bevel/shading on right & bottom edges
gold_edge = [
    (bx3 + 7, 22), (bx3 + 7, 23), (bx3 + 6, 24), (bx3 + 6, 25), (bx3 + 5, 26), (bx3 + 5, 27), (bx3 + 4, 28), (bx3 + 4, 29), (bx3 + 3, 30),
    (bx3 + 8, 31),
    (bx3 + 8, 32), (bx3 + 7, 33), (bx3 + 6, 34), (bx3 + 6, 35), (bx3 + 5, 36), (bx3 + 5, 37), (bx3 + 4, 38), (bx3 + 4, 39), (bx3 + 3, 40), (bx3 + 3, 41)
]
for px, py in gold_edge:
    if (px, py) in bolt_set:
        c.set(px, py, y_dark)

# Pure white specular core down the center
white_core = [
    (bx3 + 6, 23),
    (bx3 + 5, 24),
    (bx3 + 5, 25),
    (bx3 + 4, 26),
    (bx3 + 4, 27),
    (bx3 + 3, 28),
    (bx3 + 3, 29),
    (bx3 + 2, 30),
    (bx3 + 3, 31), (bx3 + 4, 31), (bx3 + 5, 31), (bx3 + 6, 31), (bx3 + 7, 31),
    (bx3 + 6, 32),
    (bx3 + 6, 33),
    (bx3 + 5, 34),
    (bx3 + 5, 35),
    (bx3 + 4, 36),
    (bx3 + 4, 37),
    (bx3 + 3, 38),
    (bx3 + 3, 39),
]
for px, py in white_core:
    c.set(px, py, y_white)

# Electric charging sparks
c.set(bx3 + 2, 23, y_hi)
c.set(bx3 + 8, 26, y_hi)
c.set(bx3 + 8, 36, y_hi)
c.set(bx3 + 2, 37, y_hi)

view(c)
save("battery_status_set", c)
finish(c)
