import numpy as np
from pixelbench_api import new_canvas, view, finish

def render_mage():
    c = new_canvas(64, 64)
    
    PAL = {
        # Ground Shadows
        'gnd_0': '#0d0b17',
        'gnd_1': '#161326',
        'gnd_2': '#221e38',
        
        # Outlines
        'ink_cloak': '#0c0f21',
        'ink_hair': '#36200c',
        'ink_skin': '#663224',
        'ink_boot': '#1a1c2b',
        
        # Dark Blue Cloak (Exterior)
        'cloak_0': '#0f142b',  # deepest shadow
        'cloak_1': '#172042',  # dark fold
        'cloak_2': '#233263',  # midtone navy
        'cloak_3': '#34498c',  # royal blue highlight
        'cloak_4': '#4b66b8',  # bright fold crest
        'cloak_5': '#6c8ad9',  # rim glint
        
        # Cloak Lining (Velvet Indigo)
        'lining_0': '#140f24',
        'lining_1': '#22193b',
        'lining_2': '#352757',
        
        # Gold Trim & Ornaments
        'gold_0': '#3d2704',
        'gold_1': '#70490a',
        'gold_2': '#b87f17',
        'gold_3': '#ebb431',
        'gold_4': '#fcdc63',
        'gold_5': '#fff7be',
        
        # Skin Tones
        'skin_shadow2': '#9e5645',
        'skin_shadow': '#cb7560',
        'skin_mid': '#f1a48e',
        'skin_light': '#fcd1be',
        'skin_hl': '#fff0e8',
        'blush': '#f0827c',
        'lip': '#de5b66',
        
        # Eyes (Brilliant Sapphire Blue)
        'eye_dark': '#0a1021',
        'eye_deep': '#122552',
        'eye_mid': '#1b4a9e',
        'eye_light': '#337de8',
        'eye_aqua': '#54ddf0',
        'eye_white': '#edf2fc',
        
        # Hair (Warm Honey Blonde)
        'hair_0': '#3d2309',
        'hair_1': '#6b3e12',
        'hair_2': '#a86d22',
        'hair_3': '#dc9a37',
        'hair_4': '#f3c45b',
        'hair_5': '#fbe087',
        'hair_shine': '#fff2ae',
        
        # Outfit: Blouse & Skirt (Cream / Ivory)
        'cloth_shadow2': '#4c475e',
        'cloth_shadow': '#777091',
        'cloth_mid': '#aba5c2',
        'cloth_light': '#e3dfe0',
        'cloth_white': '#ffffff',
        
        # Corset / Vest (Midnight Navy)
        'corset_0': '#0f1221',
        'corset_1': '#1a2038',
        'corset_2': '#283257',
        
        # Leather Accessories
        'leather_0': '#211108',
        'leather_1': '#452815',
        'leather_2': '#734524',
        'potion_red': '#de2657',
        'potion_glass': '#9ff0fc',
        
        # Stockings (Midnight Navy/Black)
        'stocking_0': '#0f0f1c',
        'stocking_1': '#1c1d33',
        'stocking_2': '#2d2f4f',
        
        # White Boots
        'boot_sole': '#1c181e',
        'boot_heel': '#332b36',
        'boot_shadow2': '#4c4c63',
        'boot_shadow': '#787996',
        'boot_mid': '#b2b3c7',
        'boot_light': '#e2e3ee',
        'boot_white': '#ffffff',
        
        # Staff Wood
        'wood_0': '#211209',
        'wood_1': '#422715',
        'wood_2': '#6e4427',
        'wood_3': '#99633c',
        
        # Glowing Amber Gem & Magic
        'amber_0': '#661a01',
        'amber_1': '#a33402',
        'amber_2': '#dd5705',
        'amber_3': '#f7810e',
        'amber_4': '#fcb120',
        'amber_5': '#fde145',
        'amber_core': '#fffdb5',
        'amber_white': '#ffffff',
        'amber_spark': '#ffda59',
    }
    
    grid = [[None for _ in range(64)] for _ in range(64)]
    
    def P(x, y, col):
        if 0 <= x < 64 and 0 <= y < 64:
            grid[y][x] = col
            
    def H(x1, x2, y, col):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            P(x, y, col)

    # 1. GROUND SHADOW
    H(23, 43, 58, 'gnd_1')
    H(22, 44, 59, 'gnd_0')
    H(24, 42, 60, 'gnd_2')
    H(46, 52, 58, 'gnd_0')
    H(45, 53, 59, 'gnd_1')
    P(21, 59, 'gnd_2')
    P(45, 59, 'gnd_2')
    P(54, 59, 'gnd_2')

    # 2. BACK CLOAK (Flowing behind character)
    cloak_backdrop = [
        (23, 20, 43),
        (24, 19, 44),
        (25, 18, 44),
        (26, 17, 45),
        (27, 17, 45),
        (28, 16, 46),
        (29, 16, 46),
        (30, 16, 46),
        (31, 16, 46),
        (32, 16, 45),
        (33, 16, 45),
        (34, 16, 45),
        (35, 16, 44),
        (36, 17, 44),
        (37, 17, 43),
        (38, 17, 42),
        (39, 18, 42),
        (40, 18, 41),
        (41, 19, 41),
        (42, 19, 40),
        (43, 20, 40),
        (44, 20, 39),
        (45, 21, 38),
        (46, 22, 37),
        (47, 23, 35),
        (48, 24, 30),
    ]
    for y, xl, xr in cloak_backdrop:
        for x in range(xl, xr + 1):
            P(x, y, 'cloak_1')
        P(xl, y, 'ink_cloak')
        P(xr, y, 'ink_cloak')
        P(xl + 1, y, 'cloak_0')
        P(xr - 1, y, 'cloak_0')
        if xl + 2 <= xr:
            P(xl + 2, y, 'cloak_2')
            if (x + y) % 3 == 0:
                P(xl + 2, y, 'cloak_3')

    # Velvet indigo lining between skirt and boots:
    for y in range(40, 48):
        for x in range(32, 35):
            P(x, y, 'lining_0')
            if (x + y) % 2 == 0:
                P(x, y, 'lining_1')

    # Gold trim on cloak bottom hem:
    for x in range(23, 30):
        P(x, 48, 'gold_2')
    P(24, 48, 'gold_3')
    P(25, 47, 'gold_1')

    # 3. LEGS & STOCKINGS (Zettai Ryouiki)
    for y in range(38, 45):
        # Left leg (standing straight)
        for x in range(28, 32):
            P(x, y, 'stocking_1')
        P(28, y, 'stocking_0')
        P(31, y, 'stocking_0')
        P(29, y, 'stocking_2')
        # Right leg (relaxed outward)
        for x in range(35, 39):
            P(x, y, 'stocking_1')
        P(35, y, 'stocking_0')
        P(38, y, 'stocking_0')
        P(36, y, 'stocking_2')

    # Bare skin strip at top of stockings (y=38..39):
    for x in range(28, 32):
        P(x, 38, 'skin_light')
        P(x, 39, 'skin_mid')
    for x in range(35, 39):
        P(x, 38, 'skin_light')
        P(x, 39, 'skin_mid')

    # 4. WHITE BOOTS
    # Left Boot:
    H(27, 32, 44, 'boot_white')
    H(27, 32, 45, 'boot_light')
    P(27, 44, 'boot_shadow')
    P(32, 44, 'boot_shadow')
    P(27, 45, 'boot_shadow2')
    P(32, 45, 'boot_shadow2')
    # Gold buckle:
    P(29, 44, 'gold_4')
    P(30, 44, 'gold_2')
    H(28, 31, 46, 'boot_shadow2')

    # Left Shaft:
    for y in range(47, 53):
        H(28, 32, y, 'boot_light')
        P(28, y, 'boot_shadow')
        P(29, y, 'boot_white')
        P(30, y, 'boot_white')
        P(32, y, 'boot_shadow2')
    P(27, 52, 'boot_shadow')

    # Left Foot:
    for y in range(53, 57):
        H(27, 32, y, 'boot_light')
        P(27, y, 'boot_shadow')
        P(32, y, 'boot_shadow2')
    P(26, 55, 'boot_shadow')
    P(26, 56, 'boot_light')
    P(27, 56, 'boot_white')
    P(28, 56, 'boot_white')
    H(26, 32, 57, 'boot_sole')
    P(26, 56, 'boot_heel')
    P(32, 56, 'boot_heel')

    # Right Boot (Relaxed outward angle):
    H(34, 40, 44, 'boot_white')
    H(34, 40, 45, 'boot_light')
    P(34, 44, 'boot_shadow')
    P(40, 44, 'boot_shadow')
    P(34, 45, 'boot_shadow2')
    P(40, 45, 'boot_shadow2')
    P(37, 44, 'gold_4')
    P(38, 44, 'gold_2')
    H(35, 39, 46, 'boot_shadow2')

    # Right Shaft:
    for y in range(47, 53):
        H(35, 39, y, 'boot_light')
        P(35, y, 'boot_shadow')
        P(36, y, 'boot_white')
        P(37, y, 'boot_white')
        P(39, y, 'boot_shadow2')

    # Right Foot:
    for y in range(53, 57):
        H(35, 40, y, 'boot_light')
        P(35, y, 'boot_shadow')
        P(40, y, 'boot_shadow2')
    P(41, 55, 'boot_shadow')
    P(41, 56, 'boot_light')
    P(36, 56, 'boot_white')
    P(37, 56, 'boot_white')
    P(38, 56, 'boot_white')
    H(35, 41, 57, 'boot_sole')
    P(35, 56, 'boot_heel')
    P(41, 56, 'boot_heel')

    # 5. SKIRT (Pleated Cream Skirt with Gold Scalloped Hem)
    skirt_data = [
        (32, 27, 36),
        (33, 26, 37),
        (34, 25, 38),
        (35, 24, 38),
        (36, 24, 39),
        (37, 23, 39),
        (38, 23, 40),
    ]
    for y, xl, xr in skirt_data:
        H(xl, xr, y, 'cloth_light')
        
    H(27, 36, 32, 'cloth_shadow')
    H(26, 37, 33, 'cloth_mid')
    for y in range(34, 38):
        P(24, y, 'cloth_shadow2')
        P(25, y, 'cloth_shadow')
        P(27, y, 'cloth_shadow')
        P(28, y, 'cloth_white')
        P(29, y, 'cloth_light')
        P(31, y, 'cloth_shadow')
        P(32, y, 'cloth_white')
        P(33, y, 'cloth_light')
        P(35, y, 'cloth_shadow')
        P(36, y, 'cloth_white')
        P(37, y, 'cloth_light')
        P(39, y, 'cloth_shadow2')

    for x in range(23, 41):
        P(x, 38, 'gold_2')
    P(24, 38, 'gold_0')
    P(28, 38, 'gold_4')
    P(32, 38, 'gold_4')
    P(36, 38, 'gold_4')
    P(40, 38, 'gold_0')
    H(28, 31, 39, 'cloth_shadow2')
    H(35, 38, 39, 'cloth_shadow2')

    # 6. WAIST, BELT & ACCESSORIES
    H(27, 36, 31, 'leather_1')
    P(27, 31, 'leather_0')
    P(36, 31, 'leather_0')
    P(31, 31, 'gold_4')
    P(32, 31, 'gold_3')
    
    # Potion flask:
    P(26, 32, 'leather_0')
    P(25, 33, 'potion_red')
    P(26, 33, 'potion_glass')
    P(25, 34, 'leather_0')
    P(26, 34, 'potion_red')

    # 7. TORSO: BLOUSE & CORSET
    for y in range(24, 31):
        H(27, 36, y, 'cloth_light')
    for y in range(25, 31):
        P(27, y, 'corset_0')
        P(28, y, 'corset_1')
        P(35, y, 'corset_1')
        P(36, y, 'corset_0')
    # Buttons:
    P(31, 26, 'gold_3')
    P(32, 26, 'gold_4')
    P(31, 28, 'gold_3')
    P(32, 28, 'gold_4')
    P(31, 30, 'gold_3')
    P(32, 30, 'gold_4')
    # Ruffles:
    H(29, 34, 24, 'cloth_white')
    H(29, 34, 25, 'cloth_light')
    P(31, 24, 'cloth_shadow')
    P(32, 24, 'cloth_shadow')

    # 8. HEAD, NECK & DELICATE ANIME FACE
    # Neck: y=22..23, x=30..34
    for y in (22, 23):
        H(30, 34, y, 'skin_shadow')
    P(31, 22, 'skin_mid')
    P(32, 22, 'skin_mid')
    P(33, 22, 'skin_mid')

    # Face base:
    face_grid = [
        (15, 27, 36),
        (16, 27, 36),
        (17, 27, 36),
        (18, 27, 36),
        (19, 28, 35),
        (20, 29, 34),
        (21, 30, 33),
        (22, 31, 32),
    ]
    for y, xl, xr in face_grid:
        H(xl, xr, y, 'skin_light')
        
    P(31, 22, 'skin_shadow')
    P(32, 22, 'skin_shadow')
    P(30, 21, 'skin_mid')
    P(33, 21, 'skin_mid')
    P(29, 20, 'skin_mid')
    P(34, 20, 'skin_mid')

    # Rosy Cheeks (Blush):
    P(28, 19, 'blush')
    P(29, 19, 'blush')
    P(34, 19, 'blush')
    P(35, 19, 'blush')
    P(29, 20, 'skin_mid')
    P(34, 20, 'skin_mid')

    # Tiny anime nose:
    P(32, 19, 'skin_shadow2')

    # Sweet smile:
    P(31, 21, 'lip')
    P(32, 21, 'lip')
    P(31, 20, 'skin_mid')
    P(32, 20, 'skin_mid')

    # Nose bridge clean skin (x=31..32):
    for y in range(15, 19):
        P(31, y, 'skin_light')
        P(32, y, 'skin_light')

    # Eyebrows (golden-brown delicate arcs at y=14):
    P(28, 14, 'hair_1')
    P(29, 14, 'hair_2')
    P(30, 14, 'hair_2')
    P(33, 14, 'hair_2')
    P(34, 14, 'hair_2')
    P(35, 14, 'hair_1')

    # ANIME EYES
    # Soft skin above eyes at y=15:
    P(28, 15, 'skin_light')
    P(29, 15, 'skin_light')
    P(30, 15, 'skin_light')
    P(33, 15, 'skin_light')
    P(34, 15, 'skin_light')
    P(35, 15, 'skin_light')

    # Left eye: x=29, 30 at y=16..18
    # Lash line (y=16):
    P(28, 16, 'skin_light')
    P(29, 16, 'eye_dark')
    P(30, 16, 'eye_dark')
    # Pupil & catchlight (y=17): catchlight at upper-right (x=30)
    P(28, 17, 'skin_light')
    P(29, 17, 'eye_deep')     # deep pupil
    P(30, 17, 'amber_white')  # bright catchlight!
    # Lower iris & glow (y=18):
    P(28, 18, 'skin_light')
    P(29, 18, 'eye_mid')      # sapphire iris
    P(30, 18, 'eye_aqua')     # radiant aqua sparkle!

    # Right eye: x=33, 34 at y=16..18
    # Lash line (y=16):
    P(33, 16, 'eye_dark')
    P(34, 16, 'eye_dark')
    P(35, 16, 'skin_light')
    # Pupil & catchlight (y=17): catchlight at upper-right (x=34)
    P(33, 17, 'eye_deep')     # deep pupil
    P(34, 17, 'amber_white')  # bright catchlight!
    P(35, 17, 'skin_light')
    # Lower iris & glow (y=18):
    P(33, 18, 'eye_mid')      # sapphire iris
    P(34, 18, 'eye_aqua')     # radiant aqua sparkle!
    P(35, 18, 'skin_light')

    # 9. HAIR (Golden Blonde Anime Styling)
    hair_crown = [
        (6,  29, 34),
        (7,  27, 36),
        (8,  26, 37),
        (9,  25, 38),
        (10, 24, 39),
        (11, 24, 39),
        (12, 24, 39),
        (13, 24, 39),
    ]
    for y, xl, xr in hair_crown:
        H(xl, xr, y, 'hair_2')
        P(xl, y, 'hair_0')
        P(xr, y, 'hair_0')
        P(xl + 1, y, 'hair_1')
        P(xr - 1, y, 'hair_1')

    # Ahoge:
    P(31, 4, 'hair_1')
    P(32, 4, 'hair_3')
    P(32, 5, 'hair_4')
    P(33, 5, 'hair_2')

    # Hair shine halo:
    H(27, 36, 8, 'hair_3')
    H(28, 35, 9, 'hair_4')
    P(29, 9, 'hair_shine')
    P(30, 9, 'hair_shine')
    P(33, 9, 'hair_shine')
    P(34, 9, 'hair_shine')

    # Bangs framing forehead:
    P(25, 12, 'hair_3')
    P(25, 13, 'hair_2')
    P(25, 14, 'hair_1')
    P(26, 12, 'hair_4')
    P(26, 13, 'hair_3')
    P(26, 14, 'hair_2')
    P(27, 12, 'hair_3')
    P(27, 13, 'hair_3')
    P(27, 14, 'hair_2')
    P(28, 12, 'hair_4')
    P(28, 13, 'hair_3')
    P(29, 12, 'hair_4')
    P(29, 13, 'hair_3')
    P(30, 13, 'hair_3')
    P(31, 12, 'hair_2')
    P(31, 13, 'hair_3')
    P(31, 14, 'hair_3')
    P(32, 12, 'hair_4')
    P(32, 13, 'hair_3')
    P(32, 14, 'hair_3')
    P(33, 12, 'hair_4')
    P(33, 13, 'hair_3')
    P(34, 12, 'hair_3')
    P(34, 13, 'hair_3')
    P(34, 14, 'hair_2')
    P(35, 12, 'hair_4')
    P(35, 13, 'hair_3')
    P(36, 12, 'hair_4')
    P(36, 13, 'hair_3')
    P(36, 14, 'hair_2')
    P(37, 12, 'hair_3')
    P(37, 13, 'hair_2')
    P(37, 14, 'hair_1')

    # Side Locks:
    # Left lock:
    left_lock = [
        (24, 14, 'hair_1'), (25, 14, 'hair_3'), (26, 14, 'hair_3'),
        (24, 15, 'hair_1'), (25, 15, 'hair_4'), (26, 15, 'hair_3'), (27, 15, 'hair_2'),
        (24, 16, 'hair_0'), (25, 16, 'hair_3'), (26, 16, 'hair_2'), (27, 16, 'hair_2'),
        (24, 17, 'hair_0'), (25, 17, 'hair_2'), (26, 17, 'hair_2'), (27, 17, 'hair_1'),
        (24, 18, 'hair_0'), (25, 18, 'hair_3'), (26, 18, 'hair_2'), (27, 18, 'hair_1'),
        (25, 19, 'hair_4'), (26, 19, 'hair_3'), (27, 19, 'hair_2'),
        (25, 20, 'hair_3'), (26, 20, 'hair_2'), (27, 20, 'hair_1'),
        (25, 21, 'hair_2'), (26, 21, 'hair_1'),
        (25, 22, 'hair_1'), (26, 22, 'hair_0'),
        (25, 23, 'hair_0'),
    ]
    for x, y, col in left_lock:
        P(x, y, col)

    # Right lock:
    right_lock = [
        (37, 14, 'hair_3'), (38, 14, 'hair_3'), (39, 14, 'hair_1'),
        (36, 15, 'hair_2'), (37, 15, 'hair_3'), (38, 15, 'hair_4'), (39, 15, 'hair_1'),
        (36, 16, 'hair_2'), (37, 16, 'hair_2'), (38, 16, 'hair_3'), (39, 16, 'hair_0'),
        (36, 17, 'hair_1'), (37, 17, 'hair_2'), (38, 17, 'hair_2'), (39, 17, 'hair_0'),
        (36, 18, 'hair_1'), (37, 18, 'hair_2'), (38, 18, 'hair_3'), (39, 18, 'hair_0'),
        (36, 19, 'hair_2'), (37, 19, 'hair_3'), (38, 19, 'hair_4'),
        (36, 20, 'hair_1'), (37, 20, 'hair_2'), (38, 20, 'hair_3'),
        (37, 21, 'hair_1'), (38, 21, 'hair_2'),
        (37, 22, 'hair_0'), (38, 22, 'hair_1'),
        (38, 23, 'hair_0'),
    ]
    for x, y, col in right_lock:
        P(x, y, col)

    # Hair accessory (left side ribbon/pin):
    P(24, 11, 'gold_3')
    P(23, 11, 'gold_2')
    P(24, 10, 'cloak_3')
    P(23, 10, 'cloak_2')
    P(24, 12, 'cloak_3')
    P(23, 12, 'cloak_2')

    # 10. FRONT CLOAK & MANTLE (Dark Blue Cloak)
    # Shoulder Mantles:
    left_mantle = [
        (22, 23, 'cloak_1'), (23, 23, 'cloak_2'),
        (21, 24, 'cloak_1'), (22, 24, 'cloak_2'), (23, 24, 'cloak_3'), (24, 24, 'cloak_4'),
        (20, 25, 'cloak_0'), (21, 25, 'cloak_1'), (22, 25, 'cloak_2'), (23, 25, 'cloak_3'),
        (21, 26, 'cloak_0'), (22, 26, 'cloak_1'), (23, 26, 'cloak_2'),
        (22, 27, 'cloak_0'), (23, 27, 'cloak_1'),
    ]
    for x, y, col in left_mantle:
        P(x, y, col)

    right_mantle = [
        (40, 23, 'cloak_2'), (41, 23, 'cloak_1'),
        (39, 24, 'cloak_4'), (40, 24, 'cloak_3'), (41, 24, 'cloak_2'), (42, 24, 'cloak_1'),
        (40, 25, 'cloak_3'), (41, 25, 'cloak_2'), (42, 25, 'cloak_1'), (43, 25, 'cloak_0'),
        (40, 26, 'cloak_2'), (41, 26, 'cloak_1'), (42, 26, 'cloak_0'),
        (40, 27, 'cloak_1'), (41, 27, 'cloak_0'),
    ]
    for x, y, col in right_mantle:
        P(x, y, col)

    # Gold embroidered mantle trim:
    P(22, 24, 'gold_3')
    P(23, 25, 'gold_2')
    P(41, 24, 'gold_3')
    P(40, 25, 'gold_2')

    # Golden Brooch with Glowing Amber Gem at collar center (y=23..24):
    P(31, 23, 'gold_3')
    P(32, 23, 'gold_4')
    P(33, 23, 'gold_3')
    P(31, 24, 'gold_1')
    P(32, 24, 'amber_3')  # Amber jewel in brooch
    P(33, 24, 'gold_1')

    # Left front cloak folds cascading down along the side:
    left_front_drape = [
        (19, 28, 'cloak_0'), (20, 28, 'cloak_1'), (21, 28, 'cloak_2'),
        (18, 29, 'cloak_0'), (19, 29, 'cloak_1'), (20, 29, 'cloak_2'), (21, 29, 'cloak_3'),
        (18, 30, 'cloak_0'), (19, 30, 'cloak_1'), (20, 30, 'cloak_2'), (21, 30, 'cloak_4'),
        (18, 31, 'cloak_0'), (19, 31, 'cloak_1'), (20, 31, 'cloak_2'), (21, 31, 'cloak_3'),
        (18, 32, 'cloak_0'), (19, 32, 'cloak_1'), (20, 32, 'cloak_2'), (21, 32, 'cloak_3'),
        (19, 33, 'cloak_0'), (20, 33, 'cloak_1'), (21, 33, 'cloak_2'),
        (19, 34, 'cloak_0'), (20, 34, 'cloak_1'), (21, 34, 'cloak_2'),
        (20, 35, 'cloak_0'), (21, 35, 'cloak_1'), (22, 35, 'cloak_2'),
        (20, 36, 'cloak_0'), (21, 36, 'cloak_1'),
    ]
    for x, y, col in left_front_drape:
        P(x, y, col)
        
    P(21, 30, 'gold_2')
    P(21, 32, 'gold_2')
    P(22, 35, 'gold_2')

    # Right front cloak folds:
    right_front_drape = [
        (42, 28, 'cloak_2'), (43, 28, 'cloak_1'),
        (42, 29, 'cloak_2'), (43, 29, 'cloak_1'), (44, 29, 'cloak_0'),
        (42, 30, 'cloak_2'), (43, 30, 'cloak_1'),
        (41, 31, 'cloak_2'), (42, 31, 'cloak_1'),
        (41, 32, 'cloak_2'), (42, 32, 'cloak_1'),
        (40, 33, 'cloak_2'), (41, 33, 'cloak_1'),
    ]
    for x, y, col in right_front_drape:
        P(x, y, col)

    # 11. ARMS & HANDS (Relaxed Pose)
    # Right arm (viewer's left): relaxed at side, dark blue sleeve with gold cuff
    for y in range(26, 29):
        P(23, y, 'cloak_1')
        P(24, y, 'cloak_2')
    for y in range(29, 32):
        P(23, y, 'cloak_1')
        P(24, y, 'cloak_2')
    P(23, 31, 'gold_2')
    P(24, 31, 'gold_3')
    # Right Hand:
    P(23, 32, 'skin_light')
    P(24, 32, 'skin_hl')
    P(23, 33, 'skin_mid')
    P(24, 33, 'skin_light')
    P(24, 34, 'skin_shadow')

    # Left arm (viewer's right): holding staff
    for y in range(26, 29):
        P(39, y, 'cloak_1')
        P(40, y, 'cloak_2')
        P(41, y, 'cloak_3')
    P(42, 28, 'cloak_3')
    P(43, 28, 'cloak_4')
    P(42, 29, 'cloak_2')
    P(43, 29, 'cloak_3')
    P(44, 29, 'cloak_4')
    P(45, 29, 'cloak_4')
    # Gold cuff:
    P(46, 28, 'gold_4')
    P(46, 29, 'gold_3')
    P(46, 30, 'gold_2')
    # Hand gripping staff:
    P(47, 29, 'skin_hl')
    P(48, 29, 'skin_light')
    P(47, 30, 'skin_light')
    P(48, 30, 'skin_mid')
    P(47, 31, 'skin_shadow')
    P(48, 31, 'skin_shadow2')

    # 12. GLOWING AMBER STAFF
    for y in range(17, 58):
        if y in (29, 30, 31):
            P(49, y, 'wood_1')
            P(50, y, 'wood_0')
        else:
            P(48, y, 'wood_2')
            P(49, y, 'wood_1')
            P(50, y, 'wood_0')

    for y in (27, 28, 32, 33):
        P(48, y, 'gold_2')
        P(49, y, 'leather_1')
        P(50, y, 'leather_0')

    P(48, 56, 'gold_3')
    P(49, 56, 'gold_2')
    P(50, 56, 'gold_1')
    P(48, 57, 'gold_2')
    P(49, 57, 'gold_0')

    # Staff Head Ornament (Gold crescent wings holding the amber gem):
    H(47, 51, 16, 'gold_2')
    P(48, 16, 'gold_3')
    P(49, 16, 'gold_4')
    P(48, 17, 'gold_3')
    P(49, 17, 'gold_2')

    left_crescent = [
        (46, 15, 'gold_3'),
        (45, 14, 'gold_3'), (46, 14, 'gold_4'),
        (44, 13, 'gold_3'), (45, 13, 'gold_4'),
        (44, 12, 'gold_2'), (45, 12, 'gold_3'),
        (44, 11, 'gold_1'), (45, 11, 'gold_2'),
        (45, 10, 'gold_3'), (46, 10, 'gold_4'),
        (46, 9,  'gold_3'), (47, 9,  'gold_2'),
    ]
    for x, y, col in left_crescent:
        P(x, y, col)

    right_crescent = [
        (52, 15, 'gold_2'),
        (52, 14, 'gold_3'), (53, 14, 'gold_1'),
        (53, 13, 'gold_4'), (54, 13, 'gold_2'),
        (53, 12, 'gold_3'), (54, 12, 'gold_1'),
        (53, 11, 'gold_2'), (54, 11, 'gold_0'),
        (52, 10, 'gold_3'), (53, 10, 'gold_2'),
        (51, 9,  'gold_2'), (52, 9,  'gold_1'),
    ]
    for x, y, col in right_crescent:
        P(x, y, col)

    P(49, 7, 'gold_4')
    P(48, 8, 'gold_3')
    P(49, 8, 'gold_5')
    P(50, 8, 'gold_3')

    # GLOWING AMBER GEM:
    amber_facets = [
        (48, 10, 'amber_4'), (49, 10, 'amber_5'), (50, 10, 'amber_4'),
        (47, 11, 'amber_3'), (48, 11, 'amber_core'), (49, 11, 'amber_white'), (50, 11, 'amber_5'), (51, 11, 'amber_3'),
        (46, 12, 'amber_2'), (47, 12, 'amber_4'), (48, 12, 'amber_core'), (49, 12, 'amber_white'), (50, 12, 'amber_5'), (51, 12, 'amber_4'), (52, 12, 'amber_2'),
        (46, 13, 'amber_1'), (47, 13, 'amber_3'), (48, 13, 'amber_4'), (49, 13, 'amber_core'), (50, 13, 'amber_5'), (51, 13, 'amber_3'), (52, 13, 'amber_1'),
        (47, 14, 'amber_1'), (48, 14, 'amber_2'), (49, 14, 'amber_3'), (50, 14, 'amber_2'), (51, 14, 'amber_1'),
        (48, 15, 'amber_1'), (49, 15, 'amber_2'), (50, 15, 'amber_1'),
    ]
    for x, y, col in amber_facets:
        P(x, y, col)

    P(48, 11, 'amber_white')
    P(49, 11, 'amber_white')
    P(48, 12, 'amber_core')

    # Magic Sparks:
    magic_sparks = [
        (49, 5, 'amber_5'),
        (50, 6, 'amber_4'),
        (43, 11, 'amber_4'),
        (43, 12, 'amber_spark'),
        (55, 11, 'amber_4'),
        (55, 12, 'amber_5'),
        (56, 13, 'amber_3'),
        (44, 15, 'amber_4'),
        (53, 16, 'amber_5'),
        (47, 17, 'amber_4'),
        (52, 17, 'amber_3'),
        (52, 4, 'amber_spark'),
        (54, 5, 'amber_white'),
        (57, 9, 'amber_4'),
        (58, 10, 'amber_5'),
        (56, 16, 'amber_4'),
        (55, 20, 'amber_spark'),
        (53, 23, 'amber_5'),
        (52, 34, 'amber_4'),
        (53, 35, 'amber_spark'),
        (51, 44, 'amber_5'),
    ]
    for x, y, col in magic_sparks:
        P(x, y, col)

    # Ambient light on character's right side from staff:
    P(39, 13, 'hair_4')
    P(39, 14, 'hair_shine')
    P(39, 15, 'amber_4')
    P(39, 21, 'amber_4')
    P(40, 22, 'amber_4')
    P(41, 23, 'amber_5')
    P(42, 24, 'amber_4')
    # Warm light reflecting on right cloak:
    P(44, 28, 'amber_3')
    P(45, 29, 'amber_4')
    P(45, 30, 'amber_3')

    # Paint into canvas
    for y in range(64):
        for x in range(64):
            if grid[y][x] is not None:
                c.set(x, y, PAL[grid[y][x]])
                
    return c

c = render_mage()
print("Stats:", c.stats())
view(c)
finish(c)
