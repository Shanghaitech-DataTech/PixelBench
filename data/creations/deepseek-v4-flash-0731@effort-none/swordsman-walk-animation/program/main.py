from pixelbench_api import *

# Create the 64x32 output canvas - two 32x32 frames side by side
result = new_canvas(64, 32, name="swordsman-walk")

# Palette definitions
# Hair - red
HAIR = "#d82828"
HAIR_LIGHT = "#f85038"
HAIR_DARK = "#8c1414"
# Skin
SKIN = "#f0c090"
SKIN_SHADOW = "#d0a070"
SKIN_DARK = "#b89060"
# Armor plate
STEEL = "#b8b8c8"
STEEL_LIGHT = "#e0e0f0"
STEEL_DARK = "#787890"
# Shirt
SHIRT = "#e8e8e0"
SHIRT_SHADOW = "#b8b8b0"
# Cape - dark blue
CAPE = "#2c2c5c"
CAPE_DARK = "#1c1c3c"
CAPE_MID = "#3a3a74"
# Pants - brown
PANTS = "#5c4030"
PANTS_DARK = "#3c2c20"
BOOTS = "#2a1c12"
# Belt
BELT = "#383028"
BUCKLE = "#c8a848"
# Sword
BLADE = "#c8c8d8"
BLADE_LIGHT = "#f0f0f8"
BLADE_DARK = "#707080"
GRIP = "#5c2c14"
GUARD = "#b07838"
# Luna (outline)
INK = "#141414"
# Ground shadow (semi-transparent)
SHADOW = (0, 0, 0, 90)

def draw_frame(ox, frame_num):
    """Draw one 32x32 frame at x-offset ox. frame_num 1 or 2."""
    c = result
    body_bob = 0 if frame_num == 1 else -1

    # === CAPE (behind body, dark blue) ===
    # Upper cape drape over shoulders
    c.rect(ox+5, 4+body_bob, 6, 5, CAPE)
    c.rect(ox+4, 6+body_bob, 2, 4, CAPE_DARK)
    # Lower cape body
    c.rect(ox+4, 9+body_bob, 7, 7, CAPE_DARK)
    # Cape bottom droop
    c.rect(ox+5, 15+body_bob, 5, 2, CAPE)
    # Cape billowing tail (wind from right, cape streams behind-left)
    if frame_num == 1:
        # Cape tip flicking up
        c.rect(ox+2, 7+body_bob, 3, 2, CAPE)
        c.rect(ox+3, 5+body_bob, 2, 2, CAPE_DARK)
    else:
        # Cape tip flicking lower
        c.rect(ox+2, 9+body_bob, 3, 2, CAPE)
        c.rect(ox+3, 11+body_bob, 2, 2, CAPE_DARK)
    # Cape inner shading line
    c.rect(ox+8, 4+body_bob, 2, 9, CAPE_MID)
    # Cape edge highlight catch
    c.set(ox+10, 4+body_bob, CAPE_MID)
    c.set(ox+10, 13+body_bob, CAPE)
    # Cape bottom highlight
    c.rect(ox+6, 15+body_bob, 3, 1, CAPE_MID)

    # === HEAD ===
    # Hair - top with light catch
    c.rect(ox+15, 1+body_bob, 6, 1, HAIR_LIGHT)
    c.rect(ox+14, 2+body_bob, 8, 2, HAIR)
    c.rect(ox+14, 3+body_bob, 9, 2, HAIR)
    # Hair side/back - darker
    c.rect(ox+21, 3+body_bob, 2, 3, HAIR_DARK)
    # Hair bangs
    c.rect(ox+14, 5+body_bob, 5, 2, HAIR)
    c.set(ox+14, 7+body_bob, HAIR)
    # Hair flick at top back
    c.rect(ox+15, 1+body_bob, 2, 1, HAIR_LIGHT)
    # Hair strand highlights
    c.set(ox+16, 2+body_bob, HAIR_LIGHT)
    c.set(ox+15, 4+body_bob, HAIR)
    c.set(ox+14, 4+body_bob, HAIR_LIGHT)
    # Hair line at top of forehead
    c.set(ox+19, 4+body_bob, HAIR_DARK)

    # Face silhouette - hair frames the face
    # Face
    c.rect(ox+16, 6+body_bob, 5, 3, SKIN)
    # Face cheek/chin shadow
    c.set(ox+17, 8+body_bob, SKIN_SHADOW)
    c.set(ox+18, 8+body_bob, SKIN_SHADOW)
    # Chin dark
    c.set(ox+18, 9+body_bob, SKIN_SHADOW)
    # Eye - single pixel facing right
    c.set(ox+20, 7+body_bob, INK)
    # Eyebrow (hair line over eye)
    c.set(ox+20, 6+body_bob, HAIR_DARK)
    # Nose
    c.set(ox+19, 8+body_bob, SKIN_DARK)
    # Ear
    c.set(ox+16, 7+body_bob, SKIN_SHADOW)
    # Under-chin shadow
    c.set(ox+17, 9+body_bob, SKIN_DARK)

    # === NECK ===
    c.set(ox+17, 9+body_bob, SKIN)
    c.set(ox+18, 9+body_bob, SKIN)

    # === TORSO ===
    # Main shirt body - white/cream tunic
    c.rect(ox+15, 10+body_bob, 6, 7, SHIRT)
    # Torso right shadow
    c.rect(ox+19, 10+body_bob, 2, 7, SHIRT_SHADOW)
    # Tunic front hem
    c.rect(ox+15, 15+body_bob, 6, 2, SHIRT_SHADOW)
    # Chest light hit
    c.set(ox+16, 10+body_bob, SHIRT)
    # Collar
    c.rect(ox+16, 10+body_bob, 3, 1, SHIRT_SHADOW)
    # Collar edge
    c.set(ox+19, 10+body_bob, SHIRT)

    # Armor shoulder plate (front shoulder)
    c.rect(ox+19, 9+body_bob, 3, 2, STEEL)
    c.set(ox+19, 9+body_bob, STEEL_LIGHT)
    c.set(ox+20, 9+body_bob, STEEL_LIGHT)
    # Back shoulder armor
    c.set(ox+13, 10+body_bob, STEEL)
    c.set(ox+13, 11+body_bob, STEEL_DARK)
    # Shoulder armor lower trim
    c.set(ox+20, 11+body_bob, STEEL_DARK)
    c.set(ox+19, 11+body_bob, STEEL_DARK)

    # === BELT ===
    c.rect(ox+15, 17+body_bob, 6, 1, BELT)
    c.rect(ox+16, 18+body_bob, 4, 1, BELT)
    c.set(ox+18, 17+body_bob, BUCKLE)
    c.set(ox+18, 18+body_bob, BUCKLE)
    # Belt edge highlight
    c.set(ox+16, 17+body_bob, BELT)

    # === SWORD ARM (front arm, carrying sword) ===
    if frame_num == 1:
        # Arm forward, sword raised slightly
        c.rect(ox+20, 11+body_bob, 3, 2, SHIRT_SHADOW)
        # Hand
        c.rect(ox+22, 11+body_bob, 3, 2, SKIN)
        # Hand shadow
        c.set(ox+24, 12+body_bob, SKIN_SHADOW)
        # Grip (brown)
        c.rect(ox+22, 12+body_bob, 1, 2, GRIP)
        # Guard - wider
        c.rect(ox+23, 9+body_bob, 1, 5, GUARD)
        # Blade - substantial, angled up-forward
        c.rect(ox+24, 7+body_bob, 5, 1, BLADE_LIGHT)
        c.rect(ox+24, 8+body_bob, 6, 1, BLADE)
        c.rect(ox+24, 9+body_bob, 6, 1, BLADE)
        # Blade tip - sharp point up
        c.rect(ox+29, 7+body_bob, 3, 1, BLADE_LIGHT)
        c.set(ox+31, 6+body_bob, BLADE_LIGHT)
        # Blade bottom edge shadow
        c.rect(ox+24, 10+body_bob, 6, 1, BLADE_DARK)
        # Blade glint
        c.set(ox+25, 8+body_bob, BLADE_LIGHT)
        c.set(ox+27, 7+body_bob, BLADE_LIGHT)
        c.set(ox+28, 9+body_bob, BLADE_LIGHT)
    else:
        # Arm slightly lower
        c.rect(ox+20, 12+body_bob, 3, 2, SHIRT_SHADOW)
        c.rect(ox+22, 12+body_bob, 3, 2, SKIN)
        c.set(ox+24, 13+body_bob, SKIN_SHADOW)
        c.rect(ox+22, 13+body_bob, 1, 2, GRIP)
        c.rect(ox+23, 10+body_bob, 1, 5, GUARD)
        # Blade - angled more level
        c.rect(ox+24, 9+body_bob, 6, 1, BLADE_LIGHT)
        c.rect(ox+24, 10+body_bob, 6, 1, BLADE)
        c.rect(ox+29, 9+body_bob, 3, 1, BLADE)
        # Blade tip
        c.set(ox+31, 8+body_bob, BLADE_LIGHT)
        # Blade bottom edge
        c.rect(ox+24, 11+body_bob, 6, 1, BLADE_DARK)
        # Blade glints
        c.set(ox+25, 9+body_bob, BLADE_LIGHT)
        c.set(ox+27, 10+body_bob, BLADE)
        c.set(ox+28, 9+body_bob, BLADE_LIGHT)
        c.set(ox+26, 10+body_bob, BLADE)

    # === BACK ARM (swings) ===
    if frame_num == 1:
        # Back arm behind body
        c.rect(ox+12, 12+body_bob, 2, 3, SHIRT_SHADOW)
        # Fist/glove
        c.set(ox+12, 15+body_bob, SKIN)
        c.set(ox+13, 15+body_bob, SKIN)
        c.set(ox+13, 16+body_bob, SKIN_DARK)
    else:
        # Back arm swinging forward
        c.rect(ox+13, 12+body_bob, 2, 3, SHIRT_SHADOW)
        c.set(ox+13, 15+body_bob, SKIN)
        c.set(ox+14, 15+body_bob, SKIN)
        c.set(ox+14, 16+body_bob, SKIN_DARK)

    # === LEGS ===
    if frame_num == 1:
        # CONTACT - wide stance, both feet planted
        # Front leg - forward stride
        c.rect(ox+17, 18+body_bob, 4, 3, PANTS)
        c.rect(ox+18, 21+body_bob, 4, 1, PANTS)
        # Front boot - grounded
        c.rect(ox+18, 22+body_bob, 4, 1, BOOTS)
        # Front boot sole
        c.rect(ox+19, 23+body_bob, 3, 1, BOOTS)
        c.set(ox+22, 23+body_bob, BOOTS)
        # Front boot highlight
        c.set(ox+20, 22+body_bob, BOOTS)
        # Back leg - trailing
        c.rect(ox+13, 18+body_bob, 3, 4, PANTS_DARK)
        # Back boot - planted behind
        c.rect(ox+12, 22+body_bob, 3, 1, BOOTS)
        c.rect(ox+12, 23+body_bob, 2, 1, BOOTS)
    else:
        # PASSING - feet lifting
        # Front leg - bent, lifting forward
        c.rect(ox+17, 18+body_bob, 4, 1, PANTS)
        c.rect(ox+18, 19+body_bob, 3, 2, PANTS)
        # Front boot lifted
        c.rect(ox+18, 21+body_bob, 3, 1, BOOTS)
        c.rect(ox+17, 22+body_bob, 2, 1, BOOTS)
        # Back leg - pushing off behind
        c.rect(ox+13, 18+body_bob, 3, 2, PANTS_DARK)
        c.rect(ox+13, 20+body_bob, 3, 2, BOOTS)
        # Back boot toe
        c.set(ox+13, 22+body_bob, BOOTS)

    # === GROUND SHADOW ===
    if frame_num == 1:
        # Broad soft shadow under character during contact
        c.rect(ox+12, 24, 11, 1, SHADOW)
        c.set(ox+13, 24, SHADOW)
        c.set(ox+22, 24, SHADOW)
    else:
        # Slightly narrower shadow during passing
        c.rect(ox+13, 24, 10, 1, SHADOW)
        c.set(ox+12, 24, SHADOW)

# Draw both frames
draw_frame(0, 1)
draw_frame(32, 2)

print(result.stats_text())
finish(result)
