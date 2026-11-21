from pixelbench_api import *

# Create 64x64 canvas with transparent background
c = new_canvas(64, 64, background=None, name="dragon_hatchling")

# Define color palette (keeping under 86 colors)
# Main body - teal/green shades
body_dark = c.color("#1a3a35")
body_mid = c.color("#2a5a50")
body_light = c.color("#3a7a65")
body_highlight = c.color("#4a9a75")

# Belly - pale cream
belly_light = c.color("#f5ebd5")
belly_mid = c.color("#e5dbc5")

# Wing membrane - purple/pink tones
wing_dark = c.color("#653050")
wing_mid = c.color("#855070")
wing_light = c.color("#a57090")

# Horns, claws, spikes - bone/ivory
bone = c.color("#f8f0e0")
bone_shadow = c.color("#e0d0b0")

# Eyes
eye_white = c.color("#ffffff")
eye_pupil = c.color("#0a0a0a")
eye_accent = c.color("#ffaa00")

# Mouth interior
mouth_dark = c.color("#551525")
mouth_tongue = c.color("#b84050")

# ============ TAIL (left side, curving down) ============
for x, y in [
    (26, 44), (27, 44), (28, 44), (29, 44), (30, 44),
    (25, 45), (26, 45), (27, 45), (28, 45), (29, 45),
    (24, 46), (25, 46), (26, 46), (27, 46), (28, 46),
    (23, 47), (24, 47), (25, 47), (26, 47), (27, 47),
    (22, 48), (23, 48), (24, 48), (25, 48), (26, 48),
    (21, 49), (22, 49), (23, 49), (24, 49), (25, 49),
    (20, 50), (21, 50), (22, 50), (23, 50), (24, 50),
    (19, 51), (20, 51), (21, 51), (22, 51),
    (18, 52), (19, 52), (20, 52),
    (17, 53), (18, 53),
    (16, 54)
]:
    c.set(x, y, body_dark if x < 22 else body_mid)

# Tail spikes
c.set(29, 43, bone)
c.set(27, 45, bone_shadow)
c.set(25, 47, bone)
c.set(23, 49, bone_shadow)
c.set(21, 51, bone)
c.set(19, 53, bone)
c.set(17, 55, bone)

# ============ BACK LEGS ============
for y in range(48, 53):
    for x in range(27, 31):
        c.set(x, y, body_dark if y >= 51 else body_mid)
c.set(26, 53, bone)
c.set(27, 53, bone)
c.set(28, 53, bone)
c.set(29, 53, bone)
c.set(30, 53, bone)
c.set(31, 53, bone)

for y in range(48, 53):
    for x in range(37, 41):
        c.set(x, y, body_dark if y >= 51 else body_mid)
c.set(36, 53, bone)
c.set(37, 53, bone)
c.set(38, 53, bone)
c.set(39, 53, bone)
c.set(40, 53, bone)
c.set(41, 53, bone)

# ============ BELLY (pale underbelly) ============
for y in range(39, 49):
    if y == 39:
        for x in range(29, 38):
            c.set(x, y, belly_mid)
    elif y <= 46:
        c.set(28, y, belly_mid)
        for x in range(29, 38):
            c.set(x, y, belly_light)
        c.set(38, y, belly_mid)
    else:
        for x in range(29, 38):
            c.set(x, y, belly_mid)

# ============ BODY (main mass) ============
for y in range(35, 39):
    if y == 35:
        for x in range(27, 38):
            c.set(x, y, body_mid)
    elif y == 36:
        for x in range(26, 39):
            c.set(x, y, body_mid)
    elif y == 37:
        for x in range(25, 40):
            c.set(x, y, body_light)
    else:
        c.set(26, y, body_mid)
        c.set(39, y, body_mid)

# Scale texture
c.set(28, 36, body_light)
c.set(32, 36, body_light)
c.set(36, 36, body_light)
c.set(30, 37, body_highlight)
c.set(34, 37, body_highlight)

# Back spikes
c.set(28, 34, bone_shadow)
c.set(29, 34, bone)
c.set(32, 34, bone)
c.set(33, 34, bone)
c.set(36, 34, bone)
c.set(37, 34, bone_shadow)

# ============ WINGS (half-spread) ============
# Left wing
c.line(26, 37, 17, 29, bone_shadow)
c.line(17, 29, 12, 27, bone)
c.line(17, 29, 16, 35, bone_shadow)
c.poly([(26, 37), (17, 29), (12, 27), (10, 31), (14, 37), (18, 39), (26, 37)], wing_mid, fill=True)
c.line(17, 29, 12, 27, bone)
c.line(17, 29, 16, 35, bone_shadow)
c.set(14, 31, wing_light)
c.set(16, 33, wing_light)

# Right wing
c.line(40, 37, 50, 29, bone_shadow)
c.line(50, 29, 56, 27, bone)
c.line(50, 29, 54, 35, bone)
c.line(50, 29, 52, 41, bone_shadow)
c.poly([(40, 37), (50, 29), (56, 27), (58, 31), (56, 37), (54, 43), (40, 37)], wing_mid, fill=True)
c.line(50, 29, 56, 27, bone)
c.line(50, 29, 54, 35, bone)
c.line(50, 29, 52, 41, bone_shadow)
c.set(52, 31, wing_light)
c.set(54, 33, wing_light)
c.set(52, 37, wing_dark)

# Wing tip spikes
c.set(12, 27, bone)
c.set(56, 27, bone)

# ============ NECK ============
for y in range(29, 34):
    if y == 33:
        for x in range(31, 37):
            c.set(x, y, body_mid)
    elif y == 32:
        for x in range(30, 38):
            c.set(x, y, body_mid)
    elif y == 31:
        for x in range(31, 37):
            c.set(x, y, body_mid)
    elif y == 30:
        for x in range(32, 36):
            c.set(x, y, body_light)
    else:
        for x in range(33, 36):
            c.set(x, y, body_light)

c.set(31, 33, body_light)
c.set(35, 33, body_light)
c.set(33, 34, body_highlight)

# ============ HEAD ============
for y in range(20, 28):
    if y == 20:
        for x in range(30, 38):
            c.set(x, y, body_mid)
    elif y == 21:
        for x in range(29, 39):
            c.set(x, y, body_mid)
    elif y <= 26:
        c.set(29, y, body_mid)
        for x in range(30, 39):
            c.set(x, y, body_mid)
    else:
        for x in range(31, 39):
            c.set(x, y, body_mid)

# Top of head
for x in range(31, 37):
    c.set(x, 19, body_light)
for x in range(32, 37):
    c.set(x, 18, body_light)
c.set(34, 17, body_light)

# Snout
c.set(32, 27, body_light)
c.set(33, 27, body_light)
c.set(34, 27, body_light)

# Nostrils
c.set(36, 26, body_dark)
c.set(37, 26, body_dark)

# Horns
c.set(30, 19, bone)
c.set(31, 18, bone)
c.set(32, 17, bone)
c.set(33, 16, bone)
c.set(36, 17, bone_shadow)
c.set(37, 18, bone_shadow)
c.set(38, 19, bone_shadow)

# Ear spike
c.set(28, 20, bone_shadow)
c.set(27, 21, bone_shadow)
c.set(28, 22, bone_shadow)

# ============ EYES ============
# Large expressive eye
c.set(36, 22, eye_white)
c.set(37, 22, eye_white)
c.set(38, 22, eye_white)
c.set(36, 23, eye_white)
c.set(37, 23, eye_white)
c.set(38, 23, eye_white)
c.set(37, 23, eye_pupil)
c.set(38, 23, eye_pupil)
c.set(36, 24, eye_accent)
c.set(37, 24, eye_accent)

# Eye ridge/brow for expression
c.set(35, 21, body_dark)
c.set(36, 21, body_dark)
c.set(37, 21, body_dark)
c.set(38, 21, body_dark)
c.set(39, 21, body_dark)
c.set(39, 22, body_dark)

# ============ MOUTH (open, growling) ============
# Upper jaw
for x in range(33, 39):
    c.set(x, 28, body_mid)

# Lower jaw
for x in range(32, 39):
    c.set(x, 29, body_mid)
for x in range(33, 39):
    c.set(x, 30, body_mid)
c.set(34, 31, belly_light)
c.set(35, 31, belly_light)
c.set(36, 31, belly_light)

# Open mouth - dark interior visible
c.set(38, 28, mouth_dark)
c.set(38, 29, mouth_dark)
c.set(38, 30, mouth_tongue)

# Teeth
c.set(37, 28, bone)
c.set(37, 30, bone)
c.set(35, 29, bone)
c.set(36, 29, bone)

# ============ FRONT LEGS ============
for y in range(42, 46):
    for x in range(29, 33):
        c.set(x, y, body_dark if y >= 45 else body_mid)
c.set(29, 46, bone)
c.set(30, 46, bone)
c.set(31, 46, bone)
c.set(32, 46, bone)
c.set(33, 46, bone)

for y in range(42, 46):
    for x in range(38, 42):
        c.set(x, y, body_dark if y >= 45 else body_mid)
c.set(38, 46, bone)
c.set(39, 46, bone)
c.set(40, 46, bone)
c.set(41, 46, bone)
c.set(42, 46, bone)

# ============ DETAILS ============
# Body highlights
c.set(27, 38, body_highlight)
c.set(38, 38, body_highlight)
c.set(30, 43, body_highlight)
c.set(36, 43, body_highlight)

# Check stats
print(c.stats_text())
print(f"Color count: {len(c.palette())}")

# Submit
finish(c)
