# Farm Chicken - Stardew Valley style pixel art
# 32x32, plump white chicken, gentle side view facing LEFT
# Final version

c = new_canvas(32, 32)

# --- Warm muted palette ---
cream        = c.color("#e8d5b8")
cream_light  = c.color("#f2e6cf")
cream_shadow = c.color("#c9af8e")
cream_dark   = c.color("#a08662")
orange       = c.color("#e0a75c")
orange_dark  = c.color("#c08a45")
red          = c.color("#d4674a")
red_dark     = c.color("#b55238")
eye_brown    = c.color("#4a3328")
eye_white    = c.color("#ffffff")
wing_tone    = c.color("#dcc7a4")
wing_detail  = c.color("#b09672")

def px(x, y, color):
    c.set(x, y, color)

# =============================================
# SILHOUETTE: Connected body + head + tail
# =============================================
c.ellipse(17, 19, 10, 7, cream)
c.ellipse(9, 12, 5, 4, cream)

# Tail feathers at back
for (x, y) in [
    (25, 8),  (26, 8),
    (24, 9),  (25, 9),  (26, 9),
    (23, 10), (24, 10), (25, 10), (26, 10), (27, 10),
    (23, 11), (24, 11), (25, 11), (26, 11), (27, 11), (28, 11),
    (23, 12), (24, 12), (25, 12), (26, 12), (27, 12),
    (23, 13), (24, 13), (25, 13),
    (23, 14), (24, 14),
]:
    px(x, y, cream_light)

# Body-to-tail connection
for (x, y) in [
    (20, 12), (21, 12), (22, 12),
    (20, 13), (21, 13), (22, 13),
    (20, 14), (21, 14), (22, 14),
    (21, 15), (22, 15), (22, 16),
]:
    px(x, y, cream)

# Head-body connection at row 12
for (x, y) in [(14, 12), (15, 12), (16, 12), (17, 12), (18, 12), (19, 12)]:
    px(x, y, cream)

# Neck connection
for (x, y) in [(12, 11), (13, 11), (12, 10)]:
    px(x, y, cream)

# Fill gaps in head
px(8, 8, cream)
px(7, 8, cream)
px(8, 7, cream)

# Remove stray bottom pixels
px(27, 25, None)
px(17, 26, None)
px(26, 25, None)

# =============================================
# COMB - three red bumps
# =============================================
for (x, y) in [
    (7, 3),  (8, 3),
    (6, 4),  (7, 4),  (8, 4),  (9, 4),
    (5, 5),  (6, 5),  (7, 5),  (8, 5),  (9, 5),
    (5, 6),  (6, 6),  (7, 6),  (8, 6),  (9, 6),  (10, 6),
    (6, 7),  (7, 7),  (8, 7),  (9, 7),  (10, 7),
]:
    px(x, y, red)
px(9, 5, red)
px(10, 5, red)
# Comb shadow detail
px(8, 5, red_dark)
px(7, 4, red_dark)

# =============================================
# BEAK
# =============================================
for (x, y) in [(2, 10), (3, 10), (1, 11), (2, 11), (3, 11), (4, 11), (2, 12), (3, 12)]:
    px(x, y, orange)
px(0, 11, orange)
px(3, 12, orange_dark)

# =============================================
# WATTLE
# =============================================
for (x, y) in [(1, 13), (2, 13), (3, 13),
               (1, 14), (2, 14), (3, 14),
               (2, 15)]:
    px(x, y, red)
px(2, 15, red_dark)

# =============================================
# EYE
# =============================================
px(7, 10, eye_brown)
px(6, 9, eye_white)

# =============================================
# WING
# =============================================
for (x, y) in [
    (15, 17), (16, 17), (17, 17), (18, 17),
    (15, 18), (16, 18), (17, 18), (18, 18),
    (15, 19), (16, 19), (17, 19), (18, 19),
    (16, 20), (17, 20),
]:
    px(x, y, wing_tone)

# Wing feather detail
px(16, 18, wing_detail)
px(17, 18, wing_detail)

# =============================================
# LIGHT & SHADOW
# =============================================
# Light on upper body
for (x, y) in [
    (11, 13), (12, 13), (13, 13),
    (10, 14), (11, 14), (12, 14),
    (10, 15), (11, 15),
    (9, 8),  (10, 8), (8, 9),
]:
    px(x, y, cream_light)

# Shadow along body
for (x, y) in [
    (11, 23), (12, 23),
    (12, 24), (13, 24),
    (20, 22), (21, 22), (22, 22),
    (21, 23), (22, 23),
    (16, 23), (17, 23),
    (14, 22), (18, 22), (19, 21), (20, 21), (21, 20), (22, 20),
]:
    px(x, y, cream_shadow)

# Deep shadow bottom
for (x, y) in [
    (15, 25), (16, 25), (17, 25), (18, 25),
    (16, 24), (17, 24), (18, 24),
]:
    px(x, y, cream_dark)

# Tail feather shadows
px(27, 10, cream_shadow)
px(28, 11, cream_shadow)

# =============================================
# LEGS & FEET
# =============================================
# Near leg (orange)
for (x, y) in [
    (13, 25), (14, 25),
    (13, 26), (14, 26),
    (13, 27), (14, 27),
    (13, 28), (14, 28),
]:
    px(x, y, orange)

# Far leg (darker)
for (x, y) in [
    (20, 25), (21, 25),
    (20, 26), (21, 26),
    (20, 27), (21, 27),
    (20, 28), (21, 28),
]:
    px(x, y, orange_dark)

# Feet
for x in range(11, 17):
    px(x, 29, orange)
for x in range(19, 24):
    px(x, 29, orange_dark)

# =============================================
# FINAL POLISH
# =============================================
# Make sure the head and neck look smooth
# The head ellipse at (9,12) rx=5 ry=4 produces a rounded head
# Make the top of the head nice and smooth

# Clean up any odd gaps in the body/head shape
# Row 12 should connect from beak area all the way to tail smoothly

# Check body needs a smooth rounded shape
# Light body highlight
px(12, 12, cream)

# Make sure the wattle doesn't look disconnected
px(4, 13, None)  # remove stray if present

print(c.matrix_text(region=(0,0,31,31), indices=False))
print(c.stats_text())

# =============================================
# SUBMIT
# =============================================
finish(c)
