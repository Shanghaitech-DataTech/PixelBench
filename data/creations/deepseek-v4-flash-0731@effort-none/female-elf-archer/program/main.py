from pixelbench_api import *

# Create 64x64 canvas
c = new_canvas(64, 64, name="portrait")

# Palette definitions
SKIN = "#eec39a"
SKIN_SHADE = "#d9a87c"
SKIN_DARK = "#c08a62"
EAR_PINK = "#e8af84"

HAIR = "#2f9047"
HAIR_MID = "#257a3a"
HAIR_DARK = "#1c5e2c"
HAIR_LIGHT = "#4cb060"
HAIR_LINE = "#123d1c"

OUTFIT = "#a8d861"
OUTFIT_MID = "#8fc44a"
OUTFIT_DARK = "#72a538"
OUTFIT_LIGHT = "#c2ea82"
CHEST = "#b7df72"

LEATHER = "#8a5a2b"
LEATHER_DARK = "#6e4520"

BOW = "#6b4423"
BOW_DARK = "#4f3118"
BOW_STRING = "#e8e8e8"

ARROW = "#9c7c4a"
ARROW_HEAD = "#c0c0c0"
ARROW_FLETCH = "#e04040"
QUIVER = "#7a4a24"
QUIVER_DARK = "#5c3718"

EYE_WHITE = "#f0f0f0"
EYE = "#3ab442"
PUPIL = "#1a5a20"
BROW = "#1c5e2c"
LIP = "#d88070"
NOSE = "#d9a87c"

BELT = "#4a3420"
BELT_BUCKLE = "#d0d0d0"
BELT_DETAIL = "#5d4328"

LEG = "#9cc85a"
LEG_DARK = "#86b04c"
LEG_HL = "#b8d878"
BOOT = "#6e4520"
BOOT_DARK = "#553519"

# Background gradient idea - soft sky
BG_TOP = "#8fd4ec"
BG_MID = "#a5ddf0"
GROUND = "#5da844"
GROUND_DARK = "#4d9238"

def px(x, y, col):
    c.set(x, y, col)

# --- BACKGROUND ---
for y in range(64):
    for x in range(64):
        px(x, y, BG_TOP if y < 44 else BG_MID)

# Ground
c.ellipse(32, 61, 27, 7, GROUND, fill=True)
c.ellipse(32, 61, 24, 5, GROUND_DARK, fill=True)

# --- LAYERING ORDER: back to front ---

# --- BACK HAIR (behind head and body) ---
# Long green hair mass on the back
c.rect(23, 15, 18, 38, HAIR)  # main back hair
# Hair shading into darker at bottom
for y in range(20, 50):
    if y % 4 == 0:
        for x in range(24, 32):
            px(x, y, HAIR_MID)

# --- BOW on back (behind body, visible left side) ---
# Bowstaff curving on left
c.path("M 13 33 Q 7 48 12 60", BOW, fill=False)
c.path("M 14 33 Q 7 48 13 60", BOW, fill=False)
# Bow tips
c.path("M 12 32 Q 14 30 16 33", BOW, fill=True)

# --- QUIVER on back (right side) ---
c.rect(41, 35, 6, 22, QUIVER, fill=True)
c.rect(42, 37, 4, 18, QUIVER_DARK, fill=True)
# Arrow shafts
px(43, 18, ARROW); c.line(43, 18, 43, 37, ARROW)
px(45, 20, ARROW); c.line(45, 20, 45, 37, ARROW)
px(47, 22, ARROW); c.line(47, 22, 47, 37, ARROW)
# Arrow heads
px(43, 17, ARROW_HEAD); px(44, 17, ARROW_HEAD); px(43, 18, ARROW_HEAD)
px(45, 19, ARROW_HEAD); px(46, 19, ARROW_HEAD); px(45, 20, ARROW_HEAD)
px(47, 21, ARROW_HEAD); px(48, 21, ARROW_HEAD); px(47, 22, ARROW_HEAD)
# Fletching (red feathers)
px(42, 18, ARROW_FLETCH); px(44, 18, ARROW_FLETCH)
px(44, 20, ARROW_FLETCH); px(46, 20, ARROW_FLETCH)
px(46, 22, ARROW_FLETCH); px(48, 22, ARROW_FLETCH)

# --- BODY ---
# Torso (light green tunic)
c.ellipse(31, 46, 10, 13, OUTFIT, fill=True)
# Torso shading
c.rect(28, 40, 7, 12, OUTFIT_MID, fill=True)
c.rect(30, 39, 2, 3, OUTFIT_LIGHT, fill=True)  # chest highlight

# --- HEAD ---
# Head
c.ellipse(31, 26, 10, 13, SKIN, fill=True)
# Neck
c.rect(28, 37, 6, 4, SKIN_SHADE, fill=True)

# --- EARS (pointed elf ears) ---
# Left ear
c.poly([(22, 24), (12, 20), (11, 22), (21, 30)], EAR_PINK, fill=True)
c.poly([(20, 25), (14, 22), (13, 23), (19, 27)], SKIN_SHADE, fill=True)  # inner ear
# Right ear
c.poly([(40, 24), (50, 20), (51, 22), (41, 30)], EAR_PINK, fill=True)
c.poly([(42, 25), (48, 22), (49, 23), (43, 27)], SKIN_SHADE, fill=True)

# --- FRONT HAIR ---
# Top of hair
c.circle(31, 17, 6, HAIR, fill=True)
# Side fringes
c.poly([(21, 20), (24, 15), (26, 13), (25, 26), (22, 27)], HAIR, fill=True)
c.poly([(41, 20), (38, 15), (36, 13), (37, 26), (40, 27)], HAIR, fill=True)
# Hair line/highlight on top
for (x, y) in [(28, 13), (30, 12), (33, 12), (35, 13)]:
    px(x, y, HAIR_LIGHT)

# --- FACE ---
# Eyes (three-quarter, slightly right)
# Left eye
px(26, 27, EYE_WHITE); px(27, 27, EYE_WHITE)
px(26, 28, EYE); px(27, 28, EYE); px(26, 29, PUPIL)
px(28, 27, EYE_WHITE); px(28, 28, EYE)
# Right eye (further right for three-quarter)
px(33, 27, EYE_WHITE); px(34, 27, EYE_WHITE)
px(33, 28, EYE); px(34, 28, PUPIL)
px(35, 27, EYE_WHITE); px(35, 28, EYE)
# Brows
c.line(24, 24, 28, 24, BROW)
c.line(32, 24, 36, 24, BROW)
# Nose
px(31, 30, NOSE); px(31, 31, NOSE)
# Mouth
px(29, 34, LIP); px(30, 34, LIP); px(31, 34, LIP)
px(29, 35, SKIN_SHADE); px(31, 35, SKIN_SHADE)
# Cheek blush
px(25, 31, SKIN_SHADE); px(24, 30, SKIN_SHADE)
px(37, 31, SKIN_SHADE)

# --- FRONT HAIR strands over shoulders ---
# Left strand (falls from beside head down beside torso)
c.poly([(21, 25), (23, 22), (24, 45), (21, 50), (20, 45)], HAIR, fill=True)
c.poly([(22, 25), (23, 49), (21, 48)], HAIR_MID, fill=True)
# Right strand
c.poly([(42, 25), (40, 22), (39, 45), (42, 50), (43, 45)], HAIR, fill=True)
c.poly([(41, 25), (40, 49), (42, 48)], HAIR_MID, fill=True)
# Hair tips
px(22, 50, HAIR); px(40, 50, HAIR)

# --- ARMS ---
# Left arm (with tunic sleeve)
c.rect(23, 40, 4, 6, OUTFIT, fill=True)
c.rect(23, 46, 4, 3, SKIN, fill=True)  # hand
c.rect(23, 46, 2, 3, SKIN_SHADE, fill=True)
# Right arm
c.rect(37, 40, 4, 6, OUTFIT, fill=True)
c.rect(37, 46, 4, 3, SKIN, fill=True)  # hand
c.rect(39, 46, 2, 3, SKIN_SHADE, fill=True)

# --- BELT ---
c.rect(27, 48, 9, 2, BELT, fill=True)
px(31, 48, BELT_BUCKLE); px(32, 48, BELT_BUCKLE)

# --- LEGS ---
c.rect(27, 50, 4, 7, LEG, fill=True)
c.rect(32, 50, 4, 7, LEG, fill=True)
# Leg shading
c.rect(27, 52, 2, 5, LEG_DARK, fill=True)
c.rect(34, 52, 2, 5, LEG_DARK, fill=True)
c.rect(33, 50, 1, 7, LEG_HL, fill=True)

# --- BOOTS ---
c.rect(26, 56, 5, 2, BOOT, fill=True)
c.rect(33, 56, 5, 2, BOOT, fill=True)
c.rect(26, 57, 2, 1, BOOT_DARK, fill=True)
c.rect(36, 57, 2, 1, BOOT_DARK, fill=True)

# --- OUTLINE pass ---
# Head outline (dark hair color)
c.poly([(22, 20), (25, 13), (38, 13), (42, 20), (42, 25),
        (40, 31), (37, 36), (33, 38), (29, 38), (25, 36), (22, 31), (20, 25)], HAIR_LINE, fill=False)

# --- BOW STRING visible (in front of bow) ---
c.line(14, 33, 13, 59, BOW_STRING)

# --- FINAL POLISH ---
# Add shine to hair (few highlights)
for (x, y) in [(23, 15), (25, 14), (28, 13), (30, 12), (33, 12), (36, 14)]:
    px(x, y, HAIR_LIGHT)

# Add under-chin shadow
for x in range(28, 35):
    px(x, 36, SKIN_SHADE)

# Add a light fur/trim at outfit neckline
c.line(26, 39, 36, 39, OUTFIT_LIGHT)
px(28, 40, OUTFIT_LIGHT)

# Belt detail (buckle)
c.rect(30, 48, 3, 3, BELT_DETAIL)
px(31, 49, BELT_BUCKLE)

# --- CLEANUP: remove neck artifacts, refine face ---
# Nose shadow (subtle)
px(32, 31, SKIN_SHADE)

# Add a simple collar highlight at shoulders
c.line(26, 40, 24, 41, OUTFIT_MID)
c.line(36, 40, 38, 41, OUTFIT_MID)

# Define waist/hip with mild tunic flare
c.line(30, 51, 34, 51, OUTFIT_MID)

# Add detail to bow - wrap at center
c.rect(14, 44, 3, 3, BOW_DARK)

# Quiver strap (shoulder strap going over right shoulder, high up)
c.line(35, 33, 38, 37, LEATHER)
c.line(36, 33, 39, 37, LEATHER_DARK)

print(c.stats_text())

finish(c)
