from pixelbench_api import *

c = new_canvas(48, 48, background=None, name="magic_staff")
c = canvas("magic_staff")

# ============================
# COLOR PALETTE
# ============================
wood_dark = c.color((74, 48, 22), name="wood_dark")
wood_mid = c.color((110, 70, 32), name="wood_mid")
wood_light = c.color((145, 95, 45), name="wood_light")
wood_highlight = c.color((180, 122, 62), name="wood_highlight")
wood_shadow = c.color((48, 30, 13), name="wood_shadow")

purple_dark = c.color((80, 32, 125), name="purple_dark")
purple_mid = c.color((135, 62, 195), name="purple_mid")
purple_light = c.color((185, 115, 235), name="purple_light")
purple_bright = c.color((225, 175, 255), name="purple_bright")
purple_glow = c.color((155, 78, 215, 140), name="purple_glow")

# ============================
# STAFF SHAFT (vertical pole)
# ============================
# Shaft runs from y=6 to y=47, centered around x=24-25
for y in range(6, 48):
    # Wood texture with color variation along length
    c.set(24, y, wood_mid)
    c.set(25, y, wood_mid)
    
    # Left edge with light/highlight
    if y % 4 == 0:
        c.set(23, y, wood_highlight)
    else:
        c.set(23, y, wood_light)
    
    # Right edge with shadow
    if y % 5 == 1:
        c.set(26, y, wood_shadow)
    else:
        c.set(26, y, wood_dark)
    
    # Grain lines
    if y % 7 == 2:
        c.set(24, y, wood_dark)
    if y % 7 == 5:
        c.set(25, y, wood_light)

# Bottom end cap (wider)
for dx in range(22, 28):
    c.set(dx, 46, wood_dark)
    c.set(dx, 47, wood_dark)
c.set(22, 45, wood_dark)
c.set(27, 45, wood_dark)
c.set(23, 45, wood_mid)
c.set(24, 45, wood_mid)
c.set(25, 45, wood_mid)
c.set(26, 45, wood_mid)

# ============================
# CURVED HEAD
# ============================
# A curved hook at the top: rises from the shaft and curves left
# Drawing the wooden curve as a thick arc

# Curve path coordinates - from shaft top curving left in a smooth arc
# Main body of the curve (3px thick)
curve_body = [
    # Rising from shaft, curving left
    (25, 6), (25, 5), (24, 5), (24, 4), (23, 4),
    (22, 3), (21, 3), (20, 3), (19, 3), (18, 3),
    (17, 3), (16, 3), (15, 4), (14, 4),
    # The wrap-around at the top going left
    (13, 5), (12, 6), (11, 7), (10, 8), (9, 9),
    # The tip curls slightly down
    (8, 10), (8, 11),
]

# Curved head inner/top edge (light color)
curve_top = [
    (25, 4), (24, 4), (23, 3), (22, 2), (21, 2), (20, 2),
    (19, 2), (18, 2), (17, 2), (16, 2), (15, 3), (14, 3),
    (13, 4), (12, 5), (11, 6), (10, 7), (9, 8), (8, 9), (7, 10),
]

# Curved head bottom edge (dark color)
curve_bottom = [
    (25, 7), (24, 7), (23, 6), (22, 5), (21, 4), (20, 4),
    (19, 4), (18, 4), (17, 4), (16, 4), (15, 5), (14, 5),
    (13, 6), (12, 7), (11, 8), (10, 9), (9, 10), (9, 11), (9, 12),
]

# Fill in the curve body with mid wood
for x, y in curve_body:
    c.set(x, y, wood_mid)

# Top edge - light
for x, y in curve_top:
    c.set(x, y, wood_light)

# Add highlights at key spots
c.set(25, 4, wood_highlight)
c.set(22, 2, wood_highlight)
c.set(17, 2, wood_highlight)
c.set(13, 3, wood_highlight)
c.set(9, 7, wood_highlight)

# Bottom edge - dark
for x, y in curve_bottom:
    c.set(x, y, wood_dark)

# Additional shading near the shaft connection
c.set(23, 5, wood_mid)
c.set(24, 6, wood_mid)
c.set(25, 8, wood_mid)
c.set(26, 6, wood_dark)
c.set(26, 5, wood_dark)

# ============================
# CRYSTAL ORB at curve tip
# ============================
orb_cx, orb_cy = 10, 9

# Purple aura/glow
for dy in range(-4, 5):
    for dx in range(-4, 5):
        dist = (dx*dx + dy*dy) ** 0.5
        if dist > 2.5 and dist <= 4.0:
            c.set(orb_cx + dx, orb_cy + dy, purple_glow)

# Crystal orb
c.circle(orb_cx, orb_cy, 3, purple_dark)
c.circle(orb_cx, orb_cy, 2, purple_mid)
c.set(orb_cx - 1, orb_cy - 1, purple_light)
c.set(orb_cx, orb_cy, purple_bright)

# Orb sparkle
c.set(orb_cx - 1, orb_cy, purple_light)
c.set(orb_cx, orb_cy - 1, purple_light)

# ============================
# PURPLE PARTICLES
# ============================
particles = [
    # Around the head/orb
    (6, 5, purple_light), (8, 3, purple_light),
    (12, 2, purple_bright), (15, 1, purple_mid),
    (18, 5, purple_glow), (20, 1, purple_light),
    (28, 3, purple_mid), (30, 6, purple_glow),
    (6, 8, purple_glow), (5, 11, purple_light),
    (13, 10, purple_glow), (12, 12, purple_mid),
    
    # Along the shaft
    (21, 15, purple_mid), (28, 14, purple_light),
    (28, 22, purple_mid), (21, 25, purple_light),
    (28, 30, purple_bright), (20, 33, purple_glow),
    (28, 38, purple_mid), (21, 41, purple_light),
    (27, 44, purple_glow), (20, 45, purple_light),
    
    # Scattered near edges
    (15, 18, purple_glow), (32, 18, purple_light),
    (32, 27, purple_glow), (17, 29, purple_mid),
    (31, 35, purple_bright), (15, 37, purple_light),
    (10, 22, purple_glow), (33, 42, purple_glow),
    (34, 24, purple_light), (14, 26, purple_mid),
    
    # Rising wisps
    (24, 1, purple_glow), (27, 0, purple_glow),
    (19, 6, purple_light),
]

for x, y, col in particles:
    c.set(x, y, col)

# Small purple decorative gem on shaft
c.set(27, 20, purple_mid)
c.set(28, 20, purple_light)
c.set(27, 19, purple_bright)
c.set(27, 21, purple_dark)
c.set(28, 19, purple_light)

# === Extra purple energy wisps ===
# Small connector particles between curve and orb tip
c.set(8, 12, purple_glow)
c.set(7, 12, purple_light)
c.set(11, 13, purple_glow)
c.set(13, 11, purple_mid)

# Finer particle wisps streaming upward from the shaft
for i in range(4):
    c.set(20 - i, 30 - i * 3, purple_glow)
    c.set(30 + i, 28 - i * 3, purple_glow)

# === Enhance the curved head ===
# Add more depth to the curve so it reads clearly as a wooden hook
# Strengthen the arc connection
c.set(24, 3, wood_mid)
c.set(23, 3, wood_light)
c.set(22, 3, wood_light)
c.set(21, 3, wood_mid)

# Make the curve tip slightly more pronounced
c.set(9, 10, wood_light)
c.set(10, 11, wood_light)
c.set(11, 12, wood_mid)
c.set(10, 12, wood_mid)
c.set(9, 13, wood_dark)
c.set(8, 12, wood_dark)

# Small connecting ridge between curve and orb  
c.set(8, 11, wood_mid)
c.set(7, 11, wood_light)
c.set(6, 10, purple_glow)

# Check stats  
print(c.stats_text())

finish(c)
