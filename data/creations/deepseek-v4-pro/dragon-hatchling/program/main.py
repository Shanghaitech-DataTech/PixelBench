from pixelbench_api import *

# Palette
OUTLINE = "#20182a"
GREEN = "#4aa04e"
GREEN_DARK = "#2f7038"
GREEN_LIGHT = "#66b85c"
BELLY = "#ecd9a4"
BELLY_SHADE = "#c9b277"
MEMBRANE = "#8fbd6a"
MEMBRANE_DARK = "#6e9c50"
BONE = "#efe6c6"
HORN = "#e6dcb8"
MOUTH = "#7a2436"
TONGUE = "#c05548"
TOOTH = "#ffffff"
EYE = "#ffd23f"
PUPIL = "#20182a"
CLAW = "#e6dcb8"

c = new_canvas(64, 64, None, name="dragon")

# --- Wings (large, half-spread, behind everything) ---
c.poly([(32, 30), (4, 4), (13, 18), (21, 25), (29, 29)], MEMBRANE, fill=True)
c.poly([(32, 30), (60, 4), (51, 18), (43, 25), (35, 29)], MEMBRANE_DARK, fill=True)

# wing finger bones
c.line(11, 11, 13, 18, BONE)
c.line(18, 16, 21, 25, BONE)
c.line(53, 11, 51, 18, BONE)
c.line(46, 16, 43, 25, BONE)

# --- Tail (thick base attached to body, tapering to a spiked tip) ---
c.poly([(44, 38), (52, 36), (58, 40), (62, 44), (60, 47), (54, 46), (47, 46), (44, 43)], GREEN, fill=True)

# tail spikes + arrow tip
c.poly([(50, 35), (48, 29), (52, 35)], BONE, fill=True)
c.poly([(56, 38), (56, 31), (59, 38)], BONE, fill=True)
c.poly([(60, 41), (63, 39), (61, 45)], BONE, fill=True)

# --- Neck / throat (wide bridge between jaw and body) ---
c.poly([(15, 28), (24, 27), (32, 32), (40, 37), (30, 35), (18, 34)], GREEN, fill=True)

# --- Body ---
c.ellipse(36, 42, 12, 10, GREEN, fill=True)

# --- Head ---
c.ellipse(22, 25, 6.5, 6, GREEN, fill=True)
# snout / upper jaw (overlaps cranium)
c.poly([(22, 19), (10, 20), (7, 23), (10, 26), (17, 26), (20, 23)], GREEN, fill=True)
# lower jaw (open)
c.poly([(20, 28), (12, 27), (8, 30), (9, 33), (12, 34), (17, 33), (20, 31)], GREEN, fill=True)
# mouth interior (growling open mouth)
c.poly([(7, 23), (17, 26), (20, 28), (12, 27), (8, 30)], MOUTH, fill=True)

# --- Legs ---
c.ellipse(28, 51, 3, 3.5, GREEN, fill=True)
c.ellipse(43, 50, 3.5, 4, GREEN, fill=True)

# --- Belly ---
c.ellipse(35, 46, 7, 5, BELLY, fill=True)

# --- Horns ---
c.poly([(18, 19), (16, 11), (21, 18)], HORN, fill=True)
c.poly([(24, 18), (25, 10), (28, 17)], HORN, fill=True)

# --- Claws ---
c.poly([(26, 53), (25, 56), (28, 54)], CLAW, fill=True)
c.poly([(29, 53), (30, 56), (31, 53)], CLAW, fill=True)
c.poly([(41, 53), (40, 56), (43, 54)], CLAW, fill=True)
c.poly([(44, 53), (45, 56), (46, 53)], CLAW, fill=True)

# --- Strong silhouette outline ---
c.outline(OUTLINE)

# --- Details (after outline, stay crisp) ---
# eye (yellow with vertical slit pupil + glint)
c.ellipse(20, 23, 2, 2.5, EYE, fill=True)
c.line(19, 22, 19, 24, PUPIL)
c.set(21, 23, TOOTH)
# angry brow
c.line(18, 21, 21, 21, OUTLINE)
# nostril
c.set(11, 22, OUTLINE)
# teeth / fangs
c.poly([(10, 25), (9, 27), (12, 25)], TOOTH, fill=True)
c.poly([(14, 25), (13, 27), (16, 25)], TOOTH, fill=True)
c.poly([(11, 28), (10, 26), (13, 28)], TOOTH, fill=True)
# tongue
c.poly([(11, 28), (14, 28), (12, 30)], TONGUE, fill=True)

# --- Scale texture on body ---
for sx, sy in [(30, 38), (34, 40), (38, 38), (42, 40), (32, 44), (39, 44)]:
    c.line(sx - 1, sy, sx, sy - 1, GREEN_DARK)
    c.line(sx, sy - 1, sx + 1, sy, GREEN_DARK)

# belly shade
c.line(29, 49, 41, 49, BELLY_SHADE)
c.line(30, 50, 40, 50, BELLY_SHADE)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=False))
finish(c)
