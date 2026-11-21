from pixelbench_api import *

# Create 64x64 canvas for sky pirate girl portrait
c = new_canvas(64, 64, background=None)

# Define color palette - keeping under 86 colors
# Skin tones
skin_light = c.color((255, 230, 210), "skin_light")
skin_mid = c.color((240, 200, 170), "skin_mid")
skin_shadow = c.color((220, 170, 140), "skin_shadow")
skin_dark = c.color((200, 145, 115), "skin_dark")

# Hair colors (wind-swept, dynamic)
hair_main = c.color((180, 140, 80), "hair_main")
hair_light = c.color((220, 180, 110), "hair_light")
hair_shadow = c.color((140, 100, 50), "hair_shadow")
hair_dark = c.color((100, 70, 30), "hair_dark")

# Navy coat
navy_dark = c.color((30, 40, 80), "navy_dark")
navy_mid = c.color((50, 65, 110), "navy_mid")
navy_light = c.color((70, 90, 140), "navy_light")
navy_highlight = c.color((90, 115, 170), "navy_highlight")

# Red scarf
scarlet = c.color((220, 40, 50), "scarlet")
scarlet_light = c.color((255, 80, 90), "scarlet_light")
scarlet_shadow = c.color((170, 25, 35), "scarlet_shadow")
scarlet_dark = c.color((130, 15, 25), "scarlet_dark")

# Goggles
goggle_frame = c.color((200, 180, 100), "goggle_frame")
goggle_glass = c.color((100, 180, 220, 180), "goggle_glass")
goggle_dark = c.color((80, 140, 180), "goggle_dark")

# Eyes (anime style - large, expressive)
eye_white = c.color((255, 255, 255), "eye_white")
eye_blue = c.color((60, 140, 220), "eye_blue")
eye_dark_blue = c.color((30, 80, 150), "eye_dark_blue")
eye_highlight = c.color((255, 255, 255), "eye_highlight")
eye_outline = c.color((40, 30, 50), "eye_outline")

# Eyebrows
brow_color = c.color((120, 85, 50), "brow_color")

# Lips
lip_color = c.color((220, 120, 110), "lip_color")
lip_shadow = c.color((180, 80, 70), "lip_shadow")

# Blush
blush = c.color((255, 180, 170, 150), "blush")

# Background (transparent - we want clear silhouette)
# No background color - leave transparent

# Start drawing - three-quarter view, face turned slightly right
# Head base (oval shape for three-quarter view)
# Position: centered horizontally, upper portion of canvas

# Draw hair back layer first (wind-swept, flowing)
# Left side hair flowing back
c.poly([
    (18, 12), (12, 15), (8, 22), (5, 30), (6, 40), (10, 48),
    (14, 52), (18, 50), (20, 45), (22, 38), (24, 30), (22, 20),
    (20, 14)
], hair_shadow, fill=True)

# Right side hair flowing
c.poly([
    (46, 12), (52, 14), (56, 20), (58, 28), (59, 36), (57, 44),
    (54, 50), (50, 52), (48, 48), (47, 42), (46, 35), (45, 25),
    (46, 16)
], hair_shadow, fill=True)

# Top hair flowing back
c.poly([
    (22, 10), (28, 6), (35, 4), (42, 6), (48, 10),
    (46, 14), (42, 12), (35, 10), (28, 12), (24, 14)
], hair_shadow, fill=True)

# Main hair volume
c.poly([
    (20, 14), (26, 10), (32, 8), (38, 8), (44, 10), (48, 14),
    (50, 20), (51, 28), (50, 36), (48, 44), (45, 50), (42, 54),
    (38, 56), (32, 56), (26, 54), (22, 50), (18, 44), (16, 36),
    (15, 28), (16, 20), (18, 14)
], hair_main, fill=True)

# Hair highlights (wind-swept strands)
c.poly([
    (24, 12), (30, 10), (36, 10), (42, 12), (40, 16),
    (36, 14), (30, 14), (26, 16)
], hair_light, fill=True)

# Left hair strand flowing
c.poly([
    (14, 35), (12, 42), (11, 50), (13, 56), (16, 58),
    (18, 54), (17, 46), (16, 38)
], hair_light, fill=True)

# Right hair strand flowing
c.poly([
    (50, 35), (52, 42), (54, 50), (53, 56), (50, 58),
    (48, 54), (49, 46), (50, 38)
], hair_light, fill=True)

# Hair shadows for depth
c.poly([
    (22, 48), (26, 52), (32, 54), (38, 54), (42, 52), (44, 48),
    (42, 44), (38, 42), (32, 42), (26, 44)
], hair_dark, fill=True)

# Face shape (three-quarter view - slightly turned)
c.poly([
    (24, 18), (26, 16), (30, 15), (34, 15), (38, 16), (40, 18),
    (41, 24), (41, 30), (40, 36), (38, 41), (35, 44), (32, 45),
    (29, 44), (26, 41), (24, 36), (23, 30), (23, 24)
], skin_mid, fill=True)

# Face shading (three-quarter lighting from upper left)
c.poly([
    (36, 20), (40, 24), (41, 30), (40, 36), (38, 38),
    (36, 34), (35, 28), (35, 22)
], skin_shadow, fill=True)

# Cheek highlight (left side, catching light)
c.poly([
    (25, 28), (28, 26), (30, 28), (29, 32), (26, 32)
], skin_light, fill=True)

# Blush on cheeks
c.set(27, 34, blush)
c.set(28, 34, blush)
c.set(27, 35, blush)
c.set(37, 32, blush)
c.set(38, 32, blush)
c.set(37, 33, blush)

# Nose (simple, anime style)
c.set(34, 32, skin_shadow)
c.set(34, 33, skin_shadow)
c.set(33, 34, skin_shadow)

# Mouth (confident smile)
c.poly([
    (30, 39), (33, 38), (36, 39), (36, 41), (33, 42), (30, 41)
], lip_color, fill=True)
c.set(33, 41, lip_shadow)

# Eyes - anime style, large and expressive
# Left eye (visible, three-quarter view)
c.poly([
    (27, 24), (30, 23), (33, 23), (35, 24), (35, 26),
    (34, 28), (31, 29), (28, 28), (27, 26)
], eye_outline, fill=True)

# Left eye white
c.poly([
    (28, 24), (30, 24), (33, 24), (34, 25), (34, 27),
    (33, 28), (30, 28), (28, 27)
], eye_white, fill=True)

# Left eye iris
c.poly([
    (29, 25), (31, 25), (33, 25), (33, 27), (31, 28), (29, 27)
], eye_blue, fill=True)

# Left eye pupil
c.set(31, 26, eye_dark_blue)
c.set(31, 27, eye_dark_blue)
c.set(30, 26, eye_dark_blue)
c.set(32, 26, eye_dark_blue)

# Left eye highlight
c.set(30, 25, eye_highlight)
c.set(32, 25, eye_highlight)

# Right eye (partially visible due to three-quarter view)
c.poly([
    (37, 23), (39, 22), (41, 22), (42, 23), (42, 25),
    (41, 26), (39, 27), (37, 26), (37, 24)
], eye_outline, fill=True)

# Right eye white
c.poly([
    (38, 23), (39, 23), (41, 23), (41, 24), (41, 25),
    (40, 26), (39, 26), (38, 25)
], eye_white, fill=True)

# Right eye iris
c.poly([
    (39, 24), (40, 24), (41, 24), (41, 25), (40, 25), (39, 25)
], eye_blue, fill=True)

# Right eye pupil
c.set(40, 24, eye_dark_blue)
c.set(40, 25, eye_dark_blue)

# Right eye highlight
c.set(39, 24, eye_highlight)

# Eyebrows (confident expression - slightly raised)
c.poly([
    (27, 21), (29, 20), (32, 20), (34, 21)
], brow_color, fill=False)
c.set(29, 20, brow_color)
c.set(30, 20, brow_color)
c.set(31, 20, brow_color)
c.set(32, 20, brow_color)

c.poly([
    (37, 20), (39, 19), (41, 19), (43, 20)
], brow_color, fill=False)
c.set(39, 19, brow_color)
c.set(40, 19, brow_color)
c.set(41, 19, brow_color)

# Goggles (on forehead, pushed up)
c.poly([
    (25, 14), (28, 13), (32, 12), (36, 12), (40, 13), (43, 14),
    (44, 16), (44, 19), (43, 21), (40, 22), (36, 22), (32, 21),
    (28, 20), (25, 19), (24, 17)
], goggle_frame, fill=True)

# Goggle lenses (two circles)
c.circle(30, 17, 4, goggle_glass, fill=True)
c.circle(38, 17, 4, goggle_glass, fill=True)

# Goggle frame inner
c.circle(30, 17, 3, goggle_dark, fill=False)
c.circle(38, 17, 3, goggle_dark, fill=False)

# Goggle strap
c.poly([
    (22, 16), (25, 15), (25, 18), (22, 19)
], navy_dark, fill=True)
c.poly([
    (43, 16), (46, 15), (46, 18), (43, 19)
], navy_dark, fill=True)

# Goggle highlights
c.set(29, 16, goggle_frame)
c.set(37, 16, goggle_frame)

# Navy coat (short, visible at bottom)
c.poly([
    (18, 48), (24, 46), (32, 45), (40, 46), (46, 48),
    (48, 54), (48, 60), (46, 63), (42, 63), (38, 62),
    (32, 62), (26, 62), (22, 63), (18, 63), (16, 60), (16, 54)
], navy_dark, fill=True)

# Coat collar
c.poly([
    (24, 46), (28, 44), (32, 44), (36, 44), (40, 46),
    (38, 48), (34, 47), (30, 47), (26, 48)
], navy_mid, fill=True)

# Coat highlights
c.poly([
    (20, 50), (24, 49), (32, 48), (40, 49), (44, 50),
    (44, 54), (40, 53), (32, 52), (24, 53), (20, 54)
], navy_mid, fill=True)

# Coat buttons
c.set(32, 52, goggle_frame)
c.set(32, 56, goggle_frame)
c.set(32, 60, goggle_frame)

# Red scarf (flowing, wind-swept)
c.poly([
    (26, 44), (30, 43), (34, 43), (38, 43), (42, 44),
    (44, 46), (46, 50), (48, 54), (50, 58), (52, 62),
    (50, 63), (46, 62), (44, 58), (42, 54), (40, 50),
    (38, 47), (34, 46), (30, 47), (26, 48)
], scarlet, fill=True)

# Scarf highlights (wind catching it)
c.poly([
    (34, 44), (38, 44), (42, 46), (44, 50), (46, 54),
    (44, 55), (40, 52), (36, 50), (32, 48)
], scarlet_light, fill=True)

# Scarf shadows
c.poly([
    (28, 46), (32, 45), (36, 45), (40, 46), (38, 48),
    (34, 48), (30, 49), (28, 48)
], scarlet_shadow, fill=True)

# Scarf flowing end (left side)
c.poly([
    (18, 50), (22, 48), (26, 47), (28, 49), (26, 52),
    (24, 56), (22, 60), (20, 63), (17, 63), (16, 60),
    (16, 56), (17, 52)
], scarlet, fill=True)

# Scarf flowing end highlight
c.poly([
    (20, 50), (24, 49), (26, 50), (24, 54), (22, 58), (20, 56)
], scarlet_light, fill=True)

# Add some final hair details - loose strands
c.line(14, 40, 12, 46, hair_light)
c.line(50, 40, 52, 46, hair_light)
c.line(16, 52, 14, 58, hair_main)
c.line(48, 52, 50, 58, hair_main)

# Outline the character for clear silhouette
# This helps define the edges against any background
c.outline(c.color((60, 50, 70), "outline"))

# Check stats
print(c.stats_text())

# Submit the canvas
finish(c)
