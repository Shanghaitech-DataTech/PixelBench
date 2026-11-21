from pixelbench_api import *

c = new_canvas(64, 32, name="swordsman_walk")

PALETTE = {
    # Hair (Fiery crimson/red)
    'H_HL': '#ffb280', # Bright fiery highlight
    'H_L':  '#ff5738', # Light vibrant red
    'H_M':  '#cf212b', # Main crimson red
    'H_D':  '#800d1a', # Dark shadow red
    'H_DD': '#45060f', # Deep outline red

    # Skin (Warm peach tones)
    'S_HL': '#fff2e5', # Forehead / nose highlight
    'S_L':  '#f5c5a3', # Base skin
    'S_M':  '#d48a6d', # Mid shadow
    'S_D':  '#99503c', # Dark shadow (jaw, ear, neck)
    'S_DD': '#632e22', # Deepest neck crease
    'EYE':  '#142236', # Eye pupil / dark brow
    'WHITE':'#ffffff',

    # Dark Blue Cape (Rich royal navy velvet)
    'C_HL': '#5e89db', # Edge fold highlight
    'C_L':  '#3d60ad', # Mid-light blue
    'C_M':  '#243a75', # Base royal blue
    'C_D':  '#14224a', # Deep shadow blue
    'C_DD': '#0a1026', # Outline / darkest crease

    # Armor (Polished silver steel)
    'A_HL': '#f2f6fc', # Specular steel gleam
    'A_L':  '#d6e3f2', # Light steel plate
    'A_M':  '#8ca4c4', # Mid steel
    'A_D':  '#4c617d', # Shadow steel
    'A_DD': '#232e3d', # Deep steel outline

    # Gold Trim & Brooch & Buckles
    'G_HL': '#ffed78', # Bright gold shine
    'G_M':  '#dba823', # Gold base
    'G_D':  '#7d570a', # Gold shadow

    # Pants / Tunic cloth (Dark slate navy/grey)
    'P_L':  '#444f66', # Pants highlight
    'P_M':  '#2c3345', # Pants midtone
    'P_D':  '#171c29', # Pants shadow

    # Belt & Leather Straps / Gloves
    'L_HL': '#b06f3c',
    'L_L':  '#87532a',
    'L_M':  '#593418',
    'L_D':  '#301a09',

    # Boots (Foreground leg - rich polished leather)
    'B_HL': '#ad7248', # Leather highlight
    'B_M':  '#784626', # Leather base
    'B_D':  '#4a2713', # Leather shadow
    'B_DD': '#261107', # Sole / outline

    # Boots (Background leg - shadowed for depth)
    'F_HL': '#704121',
    'F_M':  '#4a2713',
    'F_D':  '#2a1408',
    'F_DD': '#140802',

    # Long Sword (Shining double-edged steel longsword)
    'SW_W': '#ffffff', # Pure white glint
    'SW_L': '#cddcf0', # Blade cutting edge (light steel)
    'SW_M': '#8ba2c2', # Blade fuller (mid steel)
    'SW_D': '#4d627e', # Blade underside shadow
    'SW_GH':'#ffed7d', # Guard gold shine
    'SW_G': '#cfa423', # Guard gold base
    'SW_GD':'#755309', # Guard gold shadow
    'SW_H': '#5e321a', # Leather hilt grip
    'SW_P': '#ffd63b', # Gold pommel

    # Ground Contact Shadow
    'SH':   '#0d0e17',
}

for k, v in PALETTE.items():
    c.color(v, name=k)

def draw_swordsman(canvas, ox, frame=1):
    # ox: 0 for Frame 1, 32 for Frame 2

    # 1. GROUND SHADOW (Y=29)
    if frame == 1:
        for x in range(ox + 8, ox + 14):
            canvas.set(x, 29, PALETTE['SH'])
        for x in range(ox + 18, ox + 24):
            canvas.set(x, 29, PALETTE['SH'])
    else:
        for x in range(ox + 9, ox + 14):
            canvas.set(x, 29, PALETTE['SH'])
        for x in range(ox + 17, ox + 23):
            canvas.set(x, 29, PALETTE['SH'])

    # 2. CAPE (Back layer)
    if frame == 1:
        cape_data = [
            (11, 11, 'C_M'), (12, 11, 'C_L'), (13, 11, 'C_HL'),
            (10, 12, 'C_M'), (11, 12, 'C_L'), (12, 12, 'G_M'),
            (9, 13, 'C_D'), (10, 13, 'C_M'), (11, 13, 'C_L'), (12, 13, 'C_HL'),
            (8, 14, 'C_D'), (9, 14, 'C_M'), (10, 14, 'C_L'), (11, 14, 'C_HL'), (12, 14, 'C_L'),
            (7, 15, 'C_DD'), (8, 15, 'C_D'), (9, 15, 'C_M'), (10, 15, 'C_L'), (11, 15, 'C_HL'), (12, 15, 'C_L'),
            (6, 16, 'C_DD'), (7, 16, 'C_D'), (8, 16, 'C_M'), (9, 16, 'C_L'), (10, 16, 'C_HL'), (11, 16, 'C_M'),
            (5, 17, 'C_DD'), (6, 17, 'C_D'), (7, 17, 'C_M'), (8, 17, 'C_L'), (9, 17, 'C_HL'), (10, 17, 'C_M'),
            (4, 18, 'C_DD'), (5, 18, 'C_D'), (6, 18, 'C_M'), (7, 18, 'C_L'), (8, 18, 'C_HL'), (9, 18, 'C_M'), (10, 18, 'C_D'),
            (4, 19, 'C_DD'), (5, 19, 'C_D'), (6, 19, 'C_M'), (7, 19, 'C_L'), (8, 19, 'C_HL'), (9, 19, 'C_M'),
            (4, 20, 'C_DD'), (5, 20, 'C_D'), (6, 20, 'C_M'), (7, 20, 'C_L'), (8, 20, 'C_M'),
            (5, 21, 'C_DD'), (6, 21, 'C_D'), (7, 21, 'C_M'), (8, 21, 'C_M'),
            (6, 22, 'C_DD'), (7, 22, 'C_D'), (8, 22, 'C_DD'),
            (7, 23, 'C_DD'), (8, 23, 'C_DD'),
        ]
    else:
        cape_data = [
            (11, 11, 'C_M'), (12, 11, 'C_L'), (13, 11, 'C_HL'),
            (10, 12, 'C_M'), (11, 12, 'C_L'), (12, 12, 'G_M'),
            (9, 13, 'C_D'), (10, 13, 'C_M'), (11, 13, 'C_L'), (12, 13, 'C_L'),
            (8, 14, 'C_D'), (9, 14, 'C_M'), (10, 14, 'C_HL'), (11, 14, 'C_L'),
            (7, 15, 'C_DD'), (8, 15, 'C_D'), (9, 15, 'C_M'), (10, 15, 'C_HL'), (11, 15, 'C_L'),
            (6, 16, 'C_DD'), (7, 16, 'C_D'), (8, 16, 'C_M'), (9, 16, 'C_HL'), (10, 16, 'C_L'), (11, 16, 'C_M'),
            (5, 17, 'C_DD'), (6, 17, 'C_D'), (7, 17, 'C_M'), (8, 17, 'C_L'), (9, 17, 'C_HL'), (10, 17, 'C_M'),
            (4, 18, 'C_DD'), (5, 18, 'C_D'), (6, 18, 'C_M'), (7, 18, 'C_L'), (8, 18, 'C_HL'), (9, 18, 'C_M'),
            (3, 19, 'C_DD'), (4, 19, 'C_D'), (5, 19, 'C_M'), (6, 19, 'C_L'), (7, 19, 'C_HL'), (8, 19, 'C_M'),
            (3, 20, 'C_DD'), (4, 20, 'C_D'), (5, 20, 'C_M'), (6, 20, 'C_L'), (7, 20, 'C_HL'), (8, 20, 'C_D'),
            (4, 21, 'C_DD'), (5, 21, 'C_D'), (6, 21, 'C_M'), (7, 21, 'C_L'), (8, 21, 'C_DD'),
            (5, 22, 'C_DD'), (6, 22, 'C_D'), (7, 22, 'C_M'), (8, 22, 'C_DD'),
            (6, 23, 'C_DD'), (7, 23, 'C_D'), (8, 23, 'C_DD'),
            (7, 24, 'C_DD'),
        ]
    for px, py, cname in cape_data:
        canvas.set(ox + px, py, PALETTE[cname])

    # 3. BACKGROUND (FAR) LEG & BOOT
    if frame == 1:
        bg_leg = [
            (12, 19, 'P_D'), (13, 19, 'P_M'),
            (11, 20, 'P_D'), (12, 20, 'P_M'),
            (11, 21, 'P_D'), (12, 21, 'P_D'),
            # Knee & Cuff
            (10, 22, 'F_D'), (11, 22, 'F_M'), (12, 22, 'G_D'),
            (10, 23, 'F_D'), (11, 23, 'F_M'),
            # Shaft
            (9, 24, 'F_DD'), (10, 24, 'F_D'), (11, 24, 'F_M'),
            (9, 25, 'F_DD'), (10, 25, 'F_D'), (11, 25, 'F_M'),
            (9, 26, 'F_DD'), (10, 26, 'F_D'), (11, 26, 'F_M'),
            # Foot
            (8, 27, 'F_DD'), (9, 27, 'F_D'), (10, 27, 'F_M'), (11, 27, 'F_HL'),
            (8, 28, 'F_DD'), (9, 28, 'F_DD'), (10, 28, 'F_D'), (11, 28, 'F_D'),
        ]
    else:
        bg_leg = [
            (14, 19, 'P_M'), (15, 19, 'P_L'),
            (15, 20, 'P_M'), (16, 20, 'P_L'),
            (16, 21, 'P_D'), (17, 21, 'P_M'),
            # Knee & Cuff
            (17, 22, 'F_D'), (18, 22, 'F_M'), (19, 22, 'G_D'),
            (17, 23, 'F_D'), (18, 23, 'F_M'),
            # Shaft
            (17, 24, 'F_DD'), (18, 24, 'F_D'), (19, 24, 'F_M'),
            (18, 25, 'F_DD'), (19, 25, 'F_D'), (20, 25, 'F_M'),
            (18, 26, 'F_DD'), (19, 26, 'F_D'), (20, 26, 'F_M'),
            # Foot
            (18, 27, 'F_DD'), (19, 27, 'F_D'), (20, 27, 'F_M'), (21, 27, 'F_HL'),
            (18, 28, 'F_DD'), (19, 28, 'F_DD'), (20, 28, 'F_DD'), (21, 28, 'F_D'),
        ]
    for px, py, cname in bg_leg:
        canvas.set(ox + px, py, PALETTE[cname])

    # 4. TORSO, ARMOR & BELT
    torso_pixels = [
        (13, 11, 'A_M'), (14, 11, 'A_L'), (15, 11, 'A_HL'),
        (13, 12, 'A_D'), (14, 12, 'A_M'), (15, 12, 'A_L'), (16, 12, 'A_HL'), (17, 12, 'A_L'),
        (13, 13, 'A_D'), (14, 13, 'A_M'), (15, 13, 'A_L'), (16, 13, 'A_HL'), (17, 13, 'A_L'),
        (13, 14, 'A_D'), (14, 14, 'A_M'), (15, 14, 'A_L'), (16, 14, 'A_HL'), (17, 14, 'A_M'),
        (13, 15, 'A_DD'),(14, 15, 'A_D'), (15, 15, 'A_M'), (16, 15, 'A_L'), (17, 15, 'A_M'),
        (13, 16, 'L_D'), (14, 16, 'G_HL'), (15, 16, 'G_M'), (16, 16, 'L_M'), (17, 16, 'L_D'),
        (13, 17, 'A_D'), (14, 17, 'A_M'), (15, 17, 'A_L'), (16, 17, 'A_M'), (17, 17, 'A_D'),
        (13, 18, 'P_D'), (14, 18, 'P_M'), (15, 18, 'P_L'), (16, 18, 'P_M'),
    ]
    for px, py, cname in torso_pixels:
        canvas.set(ox + px, py, PALETTE[cname])

    # 5. FOREGROUND (NEAR) LEG & BOOT
    if frame == 1:
        fg_leg = [
            (14, 19, 'P_M'), (15, 19, 'P_L'), (16, 19, 'P_L'),
            (15, 20, 'P_M'), (16, 20, 'P_L'), (17, 20, 'P_L'),
            (16, 21, 'P_D'), (17, 21, 'P_M'), (18, 21, 'P_L'),
            # Knee & Cuff
            (17, 22, 'B_D'), (18, 22, 'B_M'), (19, 22, 'B_HL'), (20, 22, 'G_M'),
            (17, 23, 'B_D'), (18, 23, 'B_M'), (19, 23, 'B_HL'),
            # Shaft
            (18, 24, 'B_DD'),(19, 24, 'B_M'), (20, 24, 'B_HL'),
            (18, 25, 'B_DD'),(19, 25, 'B_M'), (20, 25, 'B_HL'),
            (18, 26, 'B_DD'),(19, 26, 'B_D'), (20, 26, 'B_M'), (21, 26, 'B_HL'),
            # Foot
            (18, 27, 'B_DD'),(19, 27, 'B_D'), (20, 27, 'B_M'), (21, 27, 'B_M'), (22, 27, 'B_HL'),
            (18, 28, 'B_DD'),(19, 28, 'B_DD'),(20, 28, 'B_D'), (21, 28, 'B_D'), (22, 28, 'B_DD'),
        ]
    else:
        fg_leg = [
            (13, 19, 'P_M'), (14, 19, 'P_L'), (15, 19, 'P_M'),
            (12, 20, 'P_D'), (13, 20, 'P_M'), (14, 20, 'P_L'),
            (12, 21, 'P_D'), (13, 21, 'P_M'),
            # Knee & Cuff
            (11, 22, 'B_D'), (12, 22, 'B_M'), (13, 22, 'B_HL'), (14, 22, 'G_M'),
            (11, 23, 'B_D'), (12, 23, 'B_M'), (13, 23, 'B_HL'),
            # Shaft
            (10, 24, 'B_DD'),(11, 24, 'B_D'), (12, 24, 'B_M'), (13, 24, 'B_HL'),
            (10, 25, 'B_DD'),(11, 25, 'B_D'), (12, 25, 'B_M'),
            (10, 26, 'B_DD'),(11, 26, 'B_D'), (12, 26, 'B_M'),
            # Foot
            (9, 27, 'B_DD'), (10, 27, 'B_D'), (11, 27, 'B_M'), (12, 27, 'B_HL'),
            (9, 28, 'B_DD'), (10, 28, 'B_DD'),(11, 28, 'B_D'), (12, 28, 'B_D'),
        ]
    for px, py, cname in fg_leg:
        canvas.set(ox + px, py, PALETTE[cname])

    # 6. HEAD, FACE & RED HAIR
    hx = ox + 11

    # Y=2: Spikes on top
    canvas.set(hx + 1, 2, PALETTE['H_L'])
    canvas.set(hx + 2, 2, PALETTE['H_HL'])
    canvas.set(hx + 3, 2, PALETTE['H_HL'])

    # Y=3: Upper hair crest with back spike
    canvas.set(hx - 2, 3, PALETTE['H_D'])
    canvas.set(hx - 1, 3, PALETTE['H_M'])
    canvas.set(hx,     3, PALETTE['H_L'])
    canvas.set(hx + 1, 3, PALETTE['H_HL'])
    canvas.set(hx + 2, 3, PALETTE['H_HL'])
    canvas.set(hx + 3, 3, PALETTE['H_L'])
    canvas.set(hx + 4, 3, PALETTE['H_M'])

    # Y=4: Hair body with backward flare
    canvas.set(hx - 3, 4, PALETTE['H_DD'])
    canvas.set(hx - 2, 4, PALETTE['H_D'])
    canvas.set(hx - 1, 4, PALETTE['H_M'])
    canvas.set(hx,     4, PALETTE['H_L'])
    canvas.set(hx + 1, 4, PALETTE['H_HL'])
    canvas.set(hx + 2, 4, PALETTE['H_L'])
    canvas.set(hx + 3, 4, PALETTE['H_M'])
    canvas.set(hx + 4, 4, PALETTE['H_D'])

    # Y=5: Forehead bangs & back hair
    canvas.set(hx - 2, 5, PALETTE['H_D'])
    canvas.set(hx - 1, 5, PALETTE['H_M'])
    canvas.set(hx,     5, PALETTE['H_L'])
    canvas.set(hx + 1, 5, PALETTE['H_L'])
    canvas.set(hx + 2, 5, PALETTE['H_M'])
    canvas.set(hx + 3, 5, PALETTE['H_L'])  # Forehead bang
    canvas.set(hx + 4, 5, PALETTE['S_HL']) # Forehead skin
    canvas.set(hx + 5, 5, PALETTE['H_M'])  # Front lock tip

    # Y=6: Brow level & Nose Bridge
    canvas.set(hx - 2, 6, PALETTE['H_DD'])
    canvas.set(hx - 1, 6, PALETTE['H_D'])
    canvas.set(hx,     6, PALETTE['H_M'])  # Sideburn
    canvas.set(hx + 1, 6, PALETTE['S_M'])  # Temple
    canvas.set(hx + 2, 6, PALETTE['S_L'])  # Brow skin
    canvas.set(hx + 3, 6, PALETTE['EYE'])  # Eyebrow dark accent
    canvas.set(hx + 4, 6, PALETTE['S_HL']) # Brow ridge
    canvas.set(hx + 5, 6, PALETTE['S_L'])  # Nose bridge top

    # Y=7: Eye level & Nose Profile
    canvas.set(hx - 1, 7, PALETTE['H_D'])
    canvas.set(hx,     7, PALETTE['H_M'])  # Sideburn
    canvas.set(hx + 1, 7, PALETTE['S_D'])  # Ear
    canvas.set(hx + 2, 7, PALETTE['S_M'])  # Cheek shadow
    canvas.set(hx + 3, 7, PALETTE['WHITE'])# Eye white
    canvas.set(hx + 4, 7, PALETTE['EYE'])  # Determined dark pupil
    canvas.set(hx + 5, 7, PALETTE['S_HL']) # Sharp nose tip!

    # Y=8: Nose base, Cheek & Philtrum
    canvas.set(hx - 1, 8, PALETTE['H_D'])
    canvas.set(hx,     8, PALETTE['H_M'])
    canvas.set(hx + 1, 8, PALETTE['S_D'])  # Ear lobe
    canvas.set(hx + 2, 8, PALETTE['S_M'])  # Lower cheek
    canvas.set(hx + 3, 8, PALETTE['S_L'])  # Cheek
    canvas.set(hx + 4, 8, PALETTE['S_M'])  # Nose underside shadow
    canvas.set(hx + 5, 8, PALETTE['S_L'])  # Upper lip

    # Y=9: Mouth & Chin
    canvas.set(hx - 1, 9, PALETTE['H_DD'])
    canvas.set(hx,     9, PALETTE['H_D'])
    canvas.set(hx + 1, 9, PALETTE['S_D'])  # Jaw angle
    canvas.set(hx + 2, 9, PALETTE['S_M'])  # Lower jaw
    canvas.set(hx + 3, 9, PALETTE['S_L'])  # Chin base
    canvas.set(hx + 4, 9, PALETTE['S_D'])  # Mouth line
    canvas.set(hx + 5, 9, PALETTE['S_L'])  # Chin point!

    # Y=10: Strong neck connecting jaw to armor
    canvas.set(hx,     10, PALETTE['H_DD']) # Back hair lock
    canvas.set(hx + 1, 10, PALETTE['S_DD']) # Deep neck crease
    canvas.set(hx + 2, 10, PALETTE['S_D'])  # Back neck shadow
    canvas.set(hx + 3, 10, PALETTE['S_M'])  # Mid neck
    canvas.set(hx + 4, 10, PALETTE['S_L'])  # Throat / front neck

    # 7. FOREGROUND ARM & MAGNIFICENT LONG SWORD
    if frame == 1:
        # Pauldron
        canvas.set(ox + 14, 12, PALETTE['A_M'])
        canvas.set(ox + 15, 12, PALETTE['A_HL'])
        canvas.set(ox + 14, 13, PALETTE['A_D'])
        canvas.set(ox + 15, 13, PALETTE['A_L'])
        canvas.set(ox + 16, 13, PALETTE['A_HL'])
        # Arm / vambrace
        canvas.set(ox + 15, 14, PALETTE['A_DD'])
        canvas.set(ox + 16, 14, PALETTE['A_M'])
        canvas.set(ox + 16, 15, PALETTE['A_L'])
        # Leather gauntlet & hand at x=17, y=16
        canvas.set(ox + 17, 15, PALETTE['L_M'])
        canvas.set(ox + 17, 16, PALETTE['L_HL'])
        canvas.set(ox + 18, 16, PALETTE['L_M'])

        # Long Sword Hilt:
        canvas.set(ox + 16, 17, PALETTE['SW_P'])  # Gold pommel
        canvas.set(ox + 17, 17, PALETTE['SW_H'])  # Grip
        # Gold crossguard
        canvas.set(ox + 18, 15, PALETTE['SW_GH']) # Guard top quillon
        canvas.set(ox + 18, 16, PALETTE['SW_G'])  # Guard center
        canvas.set(ox + 19, 17, PALETTE['SW_GD']) # Guard bottom quillon

        # Long Blade: 11 px long, solid uniform 2:1 angle forward-downward
        # Top cutting edge: SW_L (solid light steel line)
        # Fuller / underside: SW_M (mid steel body)
        blade_pixels = [
            (19, 16, 'SW_L'), (19, 17, 'SW_M'),
            (20, 16, 'SW_L'), (20, 17, 'SW_M'),
            (21, 17, 'SW_L'), (21, 18, 'SW_M'),
            (22, 17, 'SW_L'), (22, 18, 'SW_M'),
            (23, 18, 'SW_L'), (23, 19, 'SW_M'),
            (24, 18, 'SW_L'), (24, 19, 'SW_M'),
            (25, 19, 'SW_L'), (25, 20, 'SW_M'),
            (26, 19, 'SW_L'), (26, 20, 'SW_M'),
            (27, 20, 'SW_L'), (27, 21, 'SW_M'),
            (28, 20, 'SW_L'), (28, 21, 'SW_M'),
            (29, 20, 'SW_L'), # Pointed tip!
        ]
        for bx, by, cname in blade_pixels:
            canvas.set(ox + bx, by, PALETTE[cname])

    else:
        # Frame 2: Arm swings forward, blade levels horizontally!
        # Pauldron
        canvas.set(ox + 14, 12, PALETTE['A_D'])
        canvas.set(ox + 15, 12, PALETTE['A_M'])
        canvas.set(ox + 16, 12, PALETTE['A_HL'])
        canvas.set(ox + 15, 13, PALETTE['A_D'])
        canvas.set(ox + 16, 13, PALETTE['A_L'])
        canvas.set(ox + 17, 13, PALETTE['A_HL'])
        # Arm swinging forward
        canvas.set(ox + 16, 14, PALETTE['A_DD'])
        canvas.set(ox + 17, 14, PALETTE['A_M'])
        canvas.set(ox + 17, 15, PALETTE['A_L'])
        # Gauntlet & Hand at x=18, y=15
        canvas.set(ox + 18, 14, PALETTE['L_M'])
        canvas.set(ox + 18, 15, PALETTE['L_HL'])
        canvas.set(ox + 19, 15, PALETTE['L_M'])

        # Long Sword Hilt:
        canvas.set(ox + 17, 16, PALETTE['SW_P'])
        canvas.set(ox + 18, 16, PALETTE['SW_H'])
        # Gold crossguard
        canvas.set(ox + 19, 14, PALETTE['SW_GH'])
        canvas.set(ox + 19, 15, PALETTE['SW_G'])
        canvas.set(ox + 19, 16, PALETTE['SW_GD'])

        # Long Blade: solid, perfectly horizontal steel blade!
        # Top edge: Y=15 (SW_L solid light steel)
        # Underside: Y=16 (SW_M solid mid steel)
        blade_pixels = [
            (20, 15, 'SW_L'), (20, 16, 'SW_M'),
            (21, 15, 'SW_L'), (21, 16, 'SW_M'),
            (22, 15, 'SW_L'), (22, 16, 'SW_M'),
            (23, 15, 'SW_L'), (23, 16, 'SW_M'),
            (24, 15, 'SW_L'), (24, 16, 'SW_M'),
            (25, 15, 'SW_L'), (25, 16, 'SW_M'),
            (26, 15, 'SW_L'), (26, 16, 'SW_M'),
            (27, 15, 'SW_L'), (27, 16, 'SW_M'),
            (28, 15, 'SW_L'), (28, 16, 'SW_M'),
            (29, 15, 'SW_L'), (29, 16, 'SW_M'),
            (30, 15, 'SW_L'), # Pointed tip!
        ]
        for bx, by, cname in blade_pixels:
            canvas.set(ox + bx, by, PALETTE[cname])

draw_swordsman(c, 0, frame=1)
draw_swordsman(c, 32, frame=2)

print("Canvas stats:", c.stats_text())
finish(c)
view(c)

