from pixelbench_api import *

# 64x64 RPG character portrait
c = new_canvas(64, 64, background=None, name="portrait")

# Palette setup
# Skin tones
SKIN_LIGHT = "#e0b090"
SKIN_MID = "#c89070"
SKIN_DARK = "#a07050"
SKIN_SHADOW = "#704030"

# White hair
HAIR_WHITE = "#e8e8e8"
HAIR_SHADOW = "#b0b0b0"
HAIR_DARK = "#808080"

# Metal / robotic
METAL_BRIGHT = "#c8d0d8"
METAL_MID = "#9098a8"
METAL_DARK = "#505860"
METAL_DARKEST = "#282c34"
METAL_SHADOW = "#181c20"

# Glowing eye
GLOW = "#00ff88"
GLOW_BRIGHT = "#a0ffd0"
GLOW_DARK = "#009955"

# Lab coat
COAT_LIGHT = "#d8d8d8"
COAT_MID = "#b8b8b8"
COAT_DARK = "#888888"
COAT_DIRTY = "#a09080"
COAT_BROWN = "#6a5a4a"

# Leather apron
LEATHER = "#6b3d1f"
LEATHER_DARK = "#4a2a12"
LEATHER_LIGHT = "#8a5a30"

# Tool belt
BELT = "#3a2a1a"
BUCKLE = "#d0b060"
POCKET = "#55442a"

# Background - dark, high contrast backdrop
BG_DARK = "#101018"
BG_MID = "#1c1c28"
BG_LIGHT = "#2a2a3a"
BG_GLOW = "#0a3020"

# Cables
CABLE_RED = "#cc3333"
CABLE_YELLOW = "#e0a020"
CABLE_BLUE = "#3366cc"
CABLE_BLACK = "#202024"

# Teeth
TEETH = "#f0e0c0"
TEETH_SHADOW = "#c0a080"

# Eye human
EYE_WHITE = "#f8f8f8"
EYE_BLUE = "#4060a0"

LIPS = "#a05040"

# Background fill
c.rect(0, 0, 64, 64, BG_DARK)

# A subtle radial-style backdrop glow (concentric darker/lighter regions)
c.rect(2, 2, 60, 60, BG_MID)
c.rect(6, 6, 52, 52, BG_LIGHT)
c.rect(4, 30, 12, 20, BG_GLOW)  # glow behind the robotic side eye area

# ---- HEAD SHAPE ----
# Overall head silhouette (skull region roughly 14-50)
# Broad skull
c.rect(15, 12, 34, 6, SKIN_LIGHT)  # top of head behind hair

# Face base shape - human left, robotic right
# We'll build the left human face with skin, right with metal

# ---- LEFT SIDE: HUMAN FACE ----
# Face left half (x 14-38)
c.rect(14, 15, 22, 8, SKIN_LIGHT)
c.rect(14, 22, 24, 16, SKIN_LIGHT)
# chin (below the mouth)
c.rect(16, 42, 19, 3, SKIN_LIGHT)
c.rect(17, 45, 17, 3, SKIN_LIGHT)
c.rect(19, 48, 14, 2, SKIN_MID)

# Face shading (left side shadow toward nose)
c.rect(33, 17, 4, 16, SKIN_MID)
c.rect(31, 30, 6, 6, SKIN_MID)
c.rect(31, 32, 8, 6, SKIN_DARK)
c.rect(30, 38, 6, 4, SKIN_DARK)

# ---- RIGHT SIDE: ROBOTIC METAL HEAD ----
# Metal covering right half from around x30+
c.rect(34, 14, 18, 7, METAL_MID)
c.rect(34, 21, 20, 14, METAL_MID)
c.rect(34, 32, 16, 5, METAL_MID)
# metal jaw (below the mouth)
c.rect(35, 43, 14, 3, METAL_MID)
c.rect(37, 46, 12, 3, METAL_MID)

# Metal panel lines / plates
c.line(34, 14, 34, 37, METAL_DARK)
c.line(38, 15, 38, 24, METAL_DARK)
c.line(42, 14, 42, 24, METAL_DARK)
c.line(47, 15, 47, 37, METAL_DARK)
c.line(52, 15, 52, 36, METAL_DARK)
c.line(36, 28, 54, 28, METAL_DARK)
c.line(36, 33, 54, 33, METAL_DARK)

# Metal edge highlights
c.line(35, 15, 35, 28, METAL_BRIGHT)
c.line(35, 29, 35, 37, METAL_DARKEST)
c.line(39, 16, 39, 23, METAL_BRIGHT)

# ---- MESSY WHITE HAIR ----
# Wild spiky hair on top and sides
c.rect(12, 6, 40, 4, HAIR_WHITE)
c.rect(10, 10, 44, 4, HAIR_WHITE)
c.rect(9, 14, 46, 3, HAIR_WHITE)
c.rect(10, 8, 6, 4, HAIR_WHITE)
c.rect(8, 12, 4, 4, HAIR_WHITE)
c.rect(13, 5, 6, 2, HAIR_WHITE)
c.rect(18, 4, 8, 2, HAIR_WHITE)
c.rect(26, 3, 8, 3, HAIR_WHITE)
c.rect(34, 4, 9, 2, HAIR_WHITE)
c.rect(42, 5, 8, 2, HAIR_WHITE)
c.rect(48, 7, 7, 3, HAIR_WHITE)
c.rect(52, 10, 5, 4, HAIR_WHITE)
c.rect(9, 17, 3, 5, HAIR_WHITE)
c.rect(10, 20, 3, 4, HAIR_WHITE)
c.rect(11, 18, 3, 3, HAIR_DARK)

# Hair shadow / lint
c.rect(16, 8, 30, 3, HAIR_SHADOW)
c.rect(12, 12, 40, 2, HAIR_SHADOW)
c.rect(14, 9, 4, 2, HAIR_DARK)
c.rect(22, 7, 5, 2, HAIR_DARK)
c.rect(36, 8, 3, 2, HAIR_DARK)
c.rect(46, 8, 4, 2, HAIR_DARK)
c.rect(50, 12, 3, 3, HAIR_DARK)
c.rect(24, 5, 5, 2, HAIR_DARK)

# ---- EYES ----
# Left (human) eye - wide, crazed
c.rect(20, 21, 8, 5, EYE_WHITE)
c.rect(22, 22, 4, 4, EYE_BLUE)
c.rect(23, 23, 2, 2, "#202030")
c.rect(24, 23, 1, 1, "#f0f0f0")
c.set(21, 22, "#d0e0f0")
# eye socket shadow
c.rect(19, 20, 10, 1, SKIN_MID)
c.rect(19, 26, 10, 1, SKIN_MID)
# under-eye dark bags (mad scientist)
c.line(20, 27, 28, 27, SKIN_DARK)

# Eyebrow (wild, raised high)
c.rect(18, 17, 11, 2, HAIR_WHITE)
c.rect(19, 16, 6, 1, HAIR_WHITE)
# forehead wrinkle
c.line(20, 19, 29, 19, SKIN_DARK)

# Right (cybernetic glowing eye)
# Dark socket recessed
c.rect(40, 18, 12, 10, METAL_DARKEST)
c.rect(41, 19, 10, 8, METAL_DARK)
# glowing iris - large, menacing
c.rect(43, 20, 6, 6, GLOW)
c.rect(44, 21, 4, 4, GLOW_BRIGHT)
c.rect(45, 22, 2, 2, "#ffffff")
# glowing pupil slit
c.rect(45, 21, 1, 4, "#301010")
# glow aura (strong)
c.circle(45, 23, 9, GLOW_DARK, fill=False)
c.circle(45, 23, 7, GLOW_DARK, fill=False)
c.circle(45, 23, 5, GLOW_DARK, fill=False)
# eye socket rim
c.line(39, 18, 53, 18, METAL_BRIGHT)
c.line(39, 28, 53, 28, METAL_BRIGHT)
c.set(39, 19, METAL_DARKEST)
c.set(53, 27, METAL_DARKEST)

# eyebrow on robot side (metal ridge, angry angle)
c.line(40, 16, 47, 16, METAL_BRIGHT)
c.line(47, 16, 53, 18, METAL_BRIGHT)
c.line(40, 17, 47, 17, METAL_DARK)
# rivets on brow
c.set(41, 17, METAL_BRIGHT)
c.set(48, 16, METAL_BRIGHT)

# ---- BROW / forehead ----
c.rect(20, 18, 14, 1, SKIN_MID)
c.line(32, 18, 40, 17, SKIN_MID)

# ---- NOSE (center, half flesh half metal) ----
c.rect(30, 28, 3, 7, SKIN_MID)
c.rect(31, 27, 4, 8, SKIN_MID)
c.rect(31, 34, 4, 2, SKIN_DARK)
# nostril shadow
c.set(30, 35, SKIN_DARK)
c.set(31, 36, SKIN_DARK)
# metal half of nose
c.rect(35, 28, 3, 7, METAL_MID)
c.rect(35, 34, 3, 2, METAL_DARK)
c.set(35, 27, METAL_DARK)

# ---- MANIACAL GRIN ----
# Wide open mouth spanning the whole face width
c.rect(20, 39, 30, 7, "#301010")
c.rect(19, 38, 32, 2, LIPS)
c.rect(18, 37, 2, 4, SKIN_MID)
# lip corners pulled up (mad grin)
c.set(18, 38, SKIN_MID)
c.set(19, 37, SKIN_MID)
c.set(49, 38, METAL_DARK)
c.set(50, 37, METAL_DARK)
# upper teeth row (bared teeth at top of mouth)
c.rect(21, 39, 4, 2, TEETH)
c.rect(26, 39, 4, 2, TEETH)
c.rect(31, 39, 4, 2, TEETH)
c.rect(36, 39, 4, 2, TEETH)
c.rect(41, 39, 4, 2, TEETH)
c.rect(46, 39, 3, 2, TEETH)
# tooth gaps (dark between teeth)
c.set(25, 39, "#301010")
c.set(30, 39, "#301010")
c.set(35, 39, "#301010")
c.set(40, 39, "#301010")
c.set(45, 39, "#301010")
# dark mouth interior
c.rect(26, 42, 18, 3, "#301010")
# tongue
c.rect(29, 44, 12, 2, "#501020")
# lower lip
c.rect(20, 46, 22, 1, TEETH_SHADOW)
# mouth shadow below
c.rect(19, 47, 22, 1, SKIN_DARK)
# metal jaw lower overlay (right half of mouth rim)
c.line(47, 43, 50, 45, METAL_DARK)
c.rect(47, 44, 4, 3, METAL_MID)
# cheek wrinkle lines (maniacal laugh crinkles)
c.line(17, 33, 20, 36, SKIN_DARK)
c.line(51, 42, 54, 40, METAL_DARK)

# ---- CHEEKS / wrinkles ----
c.line(19, 30, 21, 32, SKIN_DARK)
c.line(18, 34, 21, 36, SKIN_DARK)
c.line(50, 40, 54, 41, METAL_DARK)
c.rect(34, 24, 2, 3, METAL_DARKEST)

# ---- JAW transition metal seam ----
c.line(36, 12, 36, 20, METAL_DARK)
c.line(33, 32, 52, 32, METAL_DARK)
c.line(34, 47, 46, 47, METAL_DARK)
# clear center split between human and robot face
c.line(33, 12, 33, 18, METAL_DARKEST)
c.line(34, 18, 34, 23, METAL_DARKEST)
c.line(34, 29, 34, 37, METAL_DARKEST)
# exposed cabling at the transition line
c.set(35, 24, CABLE_RED)
c.set(35, 27, CABLE_YELLOW)
c.set(34, 31, CABLE_BLUE)
c.set(35, 33, CABLE_RED)

# ---- EARS ----
# left ear
c.rect(11, 22, 3, 6, SKIN_LIGHT)
c.rect(12, 23, 2, 4, SKIN_SHADOW)
# right ear (metal)
c.rect(53, 22, 3, 8, METAL_MID)
c.rect(54, 23, 2, 6, METAL_DARK)

# ---- BRAIN ELECTRODE PLUGS ----
# On the side/top of the head - metal plugs sticking out
# left side plugs
c.rect(13, 14, 3, 3, METAL_DARK)
c.rect(14, 15, 2, 2, METAL_BRIGHT)
c.circle(14, 15, 2, METAL_DARKEST)
# plug wires trailing
c.line(15, 16, 12, 20, CABLE_RED)
c.line(12, 13, 9, 8, CABLE_BLUE)
c.line(16, 18, 15, 24, CABLE_YELLOW)

# top plugs (robot side brain electrodes)
c.rect(39, 5, 5, 4, METAL_MID)
c.rect(40, 6, 4, 3, METAL_BRIGHT)
c.line(41, 4, 41, 1, METAL_DARK)
c.line(43, 4, 43, 1, METAL_BRIGHT)
c.rect(46, 5, 5, 4, METAL_MID)
c.rect(47, 6, 4, 3, METAL_BRIGHT)
c.line(48, 4, 48, 1, METAL_DARK)
c.line(50, 4, 50, 1, METAL_BRIGHT)
c.rect(51, 6, 4, 3, METAL_DARK)
c.line(53, 5, 53, 2, METAL_BRIGHT)
c.line(53, 9, 55, 13, METAL_DARK)
# small wire from plug
c.line(40, 8, 37, 12, CABLE_RED)
c.line(47, 8, 51, 12, CABLE_BLUE)

# ---- NECK (half flesh, half metal) ----
# neck on left (flesh)
c.rect(19, 47, 12, 5, SKIN_MID)
c.rect(20, 51, 11, 3, SKIN_SHADOW)
# neck robot side
c.rect(31, 47, 16, 5, METAL_MID)
c.rect(31, 51, 16, 3, METAL_DARK)
# neck junction line running down center
c.line(31, 47, 31, 54, METAL_DARKEST)
# metal neck bolts
c.set(33, 49, METAL_BRIGHT)
c.set(38, 48, METAL_BRIGHT)
c.set(44, 49, METAL_BRIGHT)

# ---- COLLAR / lab coat ----
c.rect(14, 51, 46, 4, COAT_MID)
c.rect(12, 54, 50, 10, COAT_LIGHT)
c.rect(12, 51, 14, 4, COAT_MID)
# collar fold
c.rect(16, 54, 10, 3, COAT_DARK)
c.rect(26, 53, 8, 4, COAT_DIRTY)
c.line(30, 51, 30, 54, COAT_DARK)

# ---- LEATHER APRON over coat ----
c.rect(24, 55, 22, 9, LEATHER)
c.rect(25, 56, 20, 7, LEATHER_LIGHT)
c.line(24, 55, 24, 64, LEATHER_DARK)
c.line(46, 55, 46, 64, LEATHER_DARK)
c.line(23, 55, 47, 55, LEATHER_DARK)
# apron strap
c.rect(22, 54, 24, 2, LEATHER)
c.rect(24, 54, 4, 1, BUCKLE)
c.rect(34, 54, 4, 1, BUCKLE)
# pocket
c.rect(30, 58, 10, 4, LEATHER_DARK)
c.line(30, 60, 40, 60, LEATHER)
# stains on apron
c.set(34, 56, LEATHER_DARK)
c.set(28, 63, LEATHER_DARK)
c.set(40, 62, LEATHER_DARK)

# ---- TOOL BELT ----
c.rect(12, 54, 52, 3, BELT)
c.rect(14, 53, 14, 5, BELT)
c.rect(26, 54, 3, 3, BUCKLE)
c.set(27, 55, "#f0d080")
# belt pouches
c.rect(12, 55, 4, 6, POCKET)
c.rect(14, 55, 2, 5, COAT_DARK)
c.rect(56, 54, 5, 6, POCKET)

# ---- ROBOTIC ARM with exposed cables ----
# Mechanical right arm coming from shoulder area (upper arm)
c.rect(42, 48, 14, 5, METAL_MID)
c.rect(45, 53, 12, 3, METAL_DARK)
c.rect(42, 49, 12, 3, METAL_BRIGHT)
# arm segment joints
c.line(44, 47, 44, 56, METAL_DARKEST)
c.line(50, 48, 50, 57, METAL_DARK)
c.line(56, 49, 56, 56, METAL_DARK)
# rivets
c.set(43, 49, METAL_DARKEST)
c.set(52, 49, METAL_DARKEST)
c.set(57, 50, METAL_DARKEST)

# Suspended cables hanging from shoulder (exposed)
c.line(48, 57, 46, 63, CABLE_RED)
c.line(50, 57, 53, 63, CABLE_YELLOW)
c.line(44, 55, 41, 62, CABLE_BLUE)
c.line(42, 53, 39, 60, CABLE_BLACK)
c.line(52, 57, 55, 60, CABLE_YELLOW)
c.set(46, 63, CABLE_RED)
c.set(53, 63, CABLE_YELLOW)
c.set(39, 60, CABLE_BLACK)
# cable connector ports
c.set(43, 51, METAL_DARKEST)
c.set(55, 52, METAL_DARKEST)

# ---- PROSTHETIC HAND with cables ----
# robotic hand lower right (open gripper pose)
c.rect(44, 57, 12, 4, METAL_MID)
c.rect(42, 60, 14, 3, METAL_DARK)
# fingers (spread open claws)
c.rect(42, 61, 5, 2, METAL_MID)
c.rect(48, 61, 5, 2, METAL_MID)
c.rect(40, 62, 4, 1, METAL_DARK)
c.rect(53, 62, 4, 1, METAL_DARK)
c.rect(41, 60, 3, 1, METAL_DARK)
# finger joint highlights
c.rect(43, 61, 2, 1, METAL_BRIGHT)
c.rect(49, 61, 2, 1, METAL_BRIGHT)
c.rect(41, 62, 2, 1, METAL_BRIGHT)
c.rect(54, 62, 2, 1, METAL_BRIGHT)
# finger tips with claw
c.set(40, 63, METAL_BRIGHT)
c.set(52, 63, METAL_DARKEST)
c.set(43, 63, METAL_DARKEST)
# cable into hand
c.line(47, 58, 51, 59, CABLE_BLUE)
c.set(51, 59, CABLE_YELLOW)
c.set(50, 58, CABLE_RED)

# ---- LEFT ARM (hidden mostly) ----
# left arm border
c.rect(10, 52, 4, 8, COAT_MID)
c.rect(10, 52, 3, 5, COAT_DARK)

# ---- extra shadows under chin ----
c.rect(18, 49, 12, 2, SKIN_DARK)

# ---- light contrast: bright rim light on metal left edges ----
c.line(13, 13, 13, 40, COAT_LIGHT)
c.line(9, 11, 9, 20, HAIR_WHITE)

# ---- scattered sparks / glow dots near glowing eye ----
c.set(36, 17, GLOW_DARK)
c.set(56, 28, GLOW_DARK)
c.set(52, 44, GLOW_DARK)

# Save preview
save("portrait", c)

finish(c)
