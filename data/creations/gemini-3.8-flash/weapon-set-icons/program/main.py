from pixelbench_api import *

# Initialize 64x64 canvas
c = new_canvas(64, 64)

# =============================================================================
# PALETTE DEFINITION (Unified 16-bit RPG Palette)
# =============================================================================
palette = {
    '.': None,               # Transparent
    'k': '#14121a',          # Deepest dark outline / crevices
    'd': '#231e2b',          # Dark shadow outline
    
    # Steel / Iron
    'S': '#293242',          # Steel deep shadow
    's': '#414e66',          # Steel shadow
    'm': '#647999',          # Steel midtone
    'l': '#99b0cc',          # Steel light
    'h': '#d0e2f2',          # Steel bright highlight
    'w': '#ffffff',          # Specular glint
    
    # Gold / Brass
    'G': '#42240b',          # Gold deep shadow
    'g': '#754511',          # Gold shadow
    'y': '#b87b1c',          # Gold midtone
    'Y': '#e5ab30',          # Bright gold
    'j': '#fad45a',          # Gold highlight
    'J': '#fff5a6',          # Gold specular
    
    # Wood
    'W': '#26140b',          # Wood dark shadow
    'u': '#4d2814',          # Wood shadow
    'b': '#7a4320',          # Wood midtone
    't': '#aa6535',          # Wood light
    'T': '#d18e5c',          # Wood highlight
    
    # Leather / Straps
    'L': '#2b1b14',          # Leather shadow
    'e': '#593728',          # Leather mid
    'a': '#8a5c45',          # Leather light
    'A': '#b8866e',          # Leather highlight
    
    # Ruby Red / Velvet
    'R': '#3b0a14',          # Ruby deep shadow
    'r': '#731424',          # Ruby shadow
    'v': '#b02035',          # Ruby midtone
    'V': '#e33d52',          # Ruby bright
    'p': '#ff788a',          # Ruby highlight
    
    # Teal Feathers / Bowstring / Accents
    'f': '#3d5252',          # Feather shadow
    'c': '#648787',          # Feather midtone
    'C': '#9ec2bf',          # Feather light
    'o': '#e2f5f2',          # Feather bright / string
    'O': '#b8ccd1',          # String midtone
}

for char, hex_val in palette.items():
    if hex_val is not None:
        c.color(hex_val, name=char)

def p(x, y, char):
    if 0 <= x < 64 and 0 <= y < 64 and char in palette and palette[char] is not None:
        c.set(x, y, palette[char])


# =============================================================================
# 1. SWORD (Quadrant Top-Left: x in 0..31, y in 0..31)
# =============================================================================
def draw_sword():
    # Tip to (27, 1):
    p(27, 1, 'k')
    p(26, 2, 'k'); p(27, 2, 'w'); p(28, 2, 'k')
    p(25, 3, 'k'); p(26, 3, 'h'); p(27, 3, 's'); p(28, 3, 'k')
    p(24, 4, 'k'); p(25, 4, 'h'); p(26, 4, 'l'); p(27, 4, 's'); p(28, 4, 'k')
    
    # Glints near tip:
    p(27, 2, 'w')
    p(26, 3, 'w'); p(25, 3, 'h')

    # Blade rows 5 to 13
    for y in range(5, 14):
        xl = 28 - y
        p(xl,     y, 'k')
        p(xl + 1, y, 'h')
        p(xl + 2, y, 'l')
        p(xl + 3, y, 'm')
        p(xl + 4, y, 's')
        p(xl + 5, y, 'k')

    # Sparkle on edge:
    p(19, 9, 'w')

    # Golden Winged Crossguard
    p(8, 10, 'k'); p(9, 10, 'k')
    p(7, 11, 'k'); p(8, 11, 'j'); p(9, 11, 'Y'); p(10, 11, 'k')
    p(7, 12, 'k'); p(8, 12, 'Y'); p(9, 12, 'j'); p(10, 12, 'Y'); p(11, 12, 'k')
    p(8, 13, 'k'); p(9, 13, 'g'); p(10, 13, 'Y'); p(11, 13, 'j'); p(12, 13, 'Y'); p(13, 13, 'k')
    
    # Center guard & Ruby
    p(10, 14, 'k'); p(11, 14, 'g'); p(12, 14, 'Y'); p(13, 14, 'v'); p(14, 14, 'p'); p(15, 14, 'Y'); p(16, 14, 'k')
    p(11, 15, 'k'); p(12, 15, 'G'); p(13, 15, 'r'); p(14, 15, 'v'); p(15, 15, 'Y'); p(16, 15, 'j'); p(17, 15, 'k')
    
    # Right quillon
    p(12, 16, 'k'); p(13, 16, 'k'); p(14, 16, 'G'); p(15, 16, 'g'); p(16, 16, 'Y'); p(17, 16, 'j'); p(18, 16, 'k')
    p(15, 17, 'k'); p(16, 17, 'g'); p(17, 17, 'Y'); p(18, 17, 'j'); p(19, 17, 'k')
    p(16, 18, 'k'); p(17, 18, 'G'); p(18, 18, 'g'); p(19, 18, 'Y'); p(20, 18, 'k')
    p(18, 19, 'k'); p(19, 19, 'k'); p(20, 19, 'k')

    # Leather wrapped grip with gold wire
    p(11, 16, 'k'); p(12, 16, 'a'); p(13, 16, 'L'); p(14, 16, 'k')
    p(10, 17, 'k'); p(11, 17, 'A'); p(12, 17, 'a'); p(13, 17, 'k')
    p(9,  18, 'k'); p(10, 18, 'e'); p(11, 18, 'Y'); p(12, 18, 'k')
    p(8,  19, 'k'); p(9,  19, 'a'); p(10, 19, 'L'); p(11, 19, 'k')
    p(7,  20, 'k'); p(8,  20, 'A'); p(9,  20, 'a'); p(10, 20, 'k')
    p(6,  21, 'k'); p(7,  21, 'e'); p(8,  21, 'Y'); p(9,  21, 'k')
    p(5,  22, 'k'); p(6,  22, 'a'); p(7,  22, 'L'); p(8,  22, 'k')

    # Golden Pommel with ruby inlay
    p(4, 23, 'k'); p(5, 23, 'g'); p(6, 23, 'Y'); p(7, 23, 'j'); p(8, 23, 'k')
    p(3, 24, 'k'); p(4, 24, 'g'); p(5, 24, 'v'); p(6, 24, 'p'); p(7, 24, 'Y'); p(8, 24, 'k')
    p(3, 25, 'k'); p(4, 25, 'G'); p(5, 25, 'r'); p(6, 25, 'v'); p(7, 25, 'g'); p(8, 25, 'k')
    p(4, 26, 'k'); p(5, 26, 'G'); p(6, 26, 'g'); p(7, 26, 'k')
    p(5, 27, 'k'); p(6, 27, 'k')


# =============================================================================
# 2. BOW (Quadrant Top-Right: x in 32..63, y in 0..31)
# =============================================================================
def draw_bow():
    ox = 32
    oy = 0
    
    arc_points = [
        (10, 10), (11, 10), (12, 9), (13, 9), (14, 8), (15, 8),
        (16, 7), (17, 7), (18, 7), (19, 6), (20, 6), (21, 6), (22, 6)
    ]
    
    for x, y in arc_points:
        if (x, y) == (10, 10):
            col = 'Y'
        elif x in (21, 22):
            col = 'Y'
        else:
            col = 'T'
            
        p(ox + x, oy + y, col)
        p(ox + y, oy + x, col)
        
        p(ox + x, oy + y + 1, 'b')
        p(ox + y + 1, oy + x, 'b')
        
    tips = [(23, 6, 'h'), (24, 6, 'w'), (25, 7, 'l'), (25, 8, 's')]
    for x, y, col in tips:
        p(ox + x, oy + y, col)
        p(ox + y, oy + x, col)

    # Leather wrapped handle with ruby:
    p(ox + 9,  oy + 9,  'Y'); p(ox + 10, oy + 9,  'j')
    p(ox + 9,  oy + 10, 'j'); p(ox + 10, oy + 10, 'v'); p(ox + 10, oy + 11, 'p')
    p(ox + 11, oy + 10, 'r'); p(ox + 11, oy + 11, 'v')
    p(ox + 11, oy + 12, 'a'); p(ox + 12, oy + 11, 'a'); p(ox + 12, oy + 12, 'e')

    # Continuous outer dark outline:
    outer_line = [
        (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 7), (14, 7),
        (15, 6), (16, 6), (17, 6), (18, 5), (19, 5), (20, 5), (21, 5),
        (22, 5), (23, 5), (24, 5), (25, 6), (26, 6), (26, 7), (26, 8), (25, 9)
    ]
    for x, y in outer_line:
        p(ox + x, oy + y, 'k')
        p(ox + y, oy + x, 'k')

    # Continuous inner dark outline:
    inner_line = [
        (13, 11), (14, 10), (15, 10), (16, 9), (17, 9), (18, 9),
        (19, 8), (20, 8), (21, 8), (22, 8), (23, 8), (24, 8), (24, 9)
    ]
    for x, y in inner_line:
        p(ox + x, oy + y, 'k')
        p(ox + y, oy + x, 'k')

    # Bowstring connecting tips along x + y = 33:
    for i in range(9, 25):
        x = i
        y = 33 - i
        p(ox + x, oy + y, 'o')

    # Notched Arrow along diagonal x = y:
    arrowhead = [
        (3, 3, 'k'),
        (3, 4, 'k'), (4, 3, 'k'), (4, 4, 'w'),
        (3, 5, 'k'), (5, 3, 'k'), (4, 5, 'h'), (5, 4, 'h'), (5, 5, 'l'),
        (4, 6, 'k'), (6, 4, 'k'), (5, 6, 'l'), (6, 5, 'l'), (6, 6, 'm'),
        (5, 7, 'k'), (7, 5, 'k'), (6, 7, 's'), (7, 6, 's'), (7, 7, 'S'),
        (6, 8, 'k'), (8, 6, 'k'),
    ]
    for x, y, col in arrowhead:
        p(ox + x, oy + y, col)

    # Arrow shaft along x = y:
    for i in range(8, 20):
        if (i, i) not in [(10, 10), (11, 11)]:
            p(ox + i, oy + i, 't')
            p(ox + i, oy + i + 1, 'u')

    # Fletchings at (19..23, 19..23):
    fletching = [
        (19, 18, 'C'), (18, 19, 'C'),
        (20, 18, 'o'), (18, 20, 'o'), (20, 19, 'C'), (19, 20, 'C'),
        (21, 19, 'o'), (19, 21, 'o'), (21, 20, 'c'), (20, 21, 'c'),
        (22, 20, 'C'), (20, 22, 'C'), (22, 21, 'f'), (21, 22, 'f'),
        (23, 21, 'k'), (21, 23, 'k'), (23, 22, 'k'), (22, 23, 'k'),
        (22, 22, 'Y'), (23, 23, 'j'), (24, 24, 'k')
    ]
    for x, y, col in fletching:
        p(ox + x, oy + y, col)


# =============================================================================
# 3. SHIELD (Quadrant Bottom-Left: x in 0..31, y in 32..63)
# =============================================================================
def draw_shield():
    ox = 0
    oy = 32
    
    shield_rows = {
        4:  (8, 23),
        5:  (7, 24),
        6:  (6, 25),
        7:  (5, 26),
        8:  (5, 26),
        9:  (5, 26),
        10: (5, 26),
        11: (5, 26),
        12: (5, 26),
        13: (5, 26),
        14: (5, 26),
        15: (5, 26),
        16: (5, 26),
        17: (6, 25),
        18: (6, 25),
        19: (7, 24),
        20: (7, 24),
        21: (8, 23),
        22: (9, 22),
        23: (10, 21),
        24: (11, 20),
        25: (12, 19),
        26: (13, 18),
        27: (14, 17),
        28: (15, 16),
    }

    # Outer outline 'k'
    for y, (xs, xe) in shield_rows.items():
        p(ox + xs - 1, oy + y, 'k')
        p(ox + xe + 1, oy + y, 'k')
    for x in range(8, 24): p(ox + x, oy + 3, 'k')
    p(ox + 15, oy + 29, 'k'); p(ox + 16, oy + 29, 'k')

    # Heavy rim and inner field:
    for y, (xs, xe) in shield_rows.items():
        for x in range(xs, xe + 1):
            is_rim = (x in (xs, xs + 1, xe - 1, xe) or y in (4, 5, 27, 28))
            if is_rim:
                if x <= xs + 1 or y <= 5:
                    if x == xs or y == 4:
                        p(ox + x, oy + y, 'j')
                    else:
                        p(ox + x, oy + y, 'Y')
                else:
                    if x == xe or y >= 27:
                        p(ox + x, oy + y, 'G')
                    else:
                        p(ox + x, oy + y, 'g')
            else:
                dist_from_left = x - xs
                if dist_from_left <= 4 and y <= 16:
                    p(ox + x, oy + y, 'V')
                elif dist_from_left <= 8 and y <= 19:
                    p(ox + x, oy + y, 'v')
                elif x >= xe - 4 or y >= 22:
                    p(ox + x, oy + y, 'R')
                else:
                    p(ox + x, oy + y, 'r')

    # Golden rivets at the corners:
    rivets = [(7, 6), (24, 6), (7, 16), (24, 16), (10, 22), (21, 22)]
    for rx, ry in rivets:
        p(ox + rx, oy + ry, 'J')
        p(ox + rx, oy + ry + 1, 'G')

    # Golden Knight Cross:
    for cy in range(8, 23):
        p(ox + 15, oy + cy, 'Y')
        p(ox + 16, oy + cy, 'j')
        p(ox + 14, oy + cy, 'k')
        p(ox + 17, oy + cy, 'k')
    for cx in range(9, 23):
        p(ox + cx, oy + 12, 'j')
        p(ox + cx, oy + 13, 'Y')
        p(ox + cx, oy + 11, 'k')
        p(ox + cx, oy + 14, 'k')
        
    # Cross flared ends:
    p(ox + 14, oy + 8, 'j'); p(ox + 17, oy + 8, 'Y')
    p(ox + 13, oy + 7, 'k'); p(ox + 14, oy + 7, 'j'); p(ox + 15, oy + 7, 'J'); p(ox + 16, oy + 7, 'j'); p(ox + 17, oy + 7, 'Y'); p(ox + 18, oy + 7, 'k')
    p(ox + 9,  oy + 11, 'j'); p(ox + 9,  oy + 14, 'Y')
    p(ox + 8,  oy + 11, 'k'); p(ox + 8,  oy + 12, 'j'); p(ox + 8,  oy + 13, 'Y'); p(ox + 8,  oy + 14, 'k')
    p(ox + 22, oy + 11, 'j'); p(ox + 22, oy + 14, 'Y')
    p(ox + 23, oy + 11, 'k'); p(ox + 23, oy + 12, 'j'); p(ox + 23, oy + 13, 'Y'); p(ox + 23, oy + 14, 'k')
    p(ox + 14, oy + 22, 'j'); p(ox + 17, oy + 22, 'Y')
    p(ox + 14, oy + 23, 'k'); p(ox + 15, oy + 23, 'Y'); p(ox + 16, oy + 23, 'g'); p(ox + 17, oy + 23, 'k')

    # Central Diamond Boss Gem:
    p(ox + 15, oy + 12, 'w')
    p(ox + 16, oy + 12, 'h')
    p(ox + 15, oy + 13, 'l')
    p(ox + 16, oy + 13, 's')
    p(ox + 14, oy + 12, 'G'); p(ox + 14, oy + 13, 'G')
    p(ox + 17, oy + 12, 'g'); p(ox + 17, oy + 13, 'g')


# =============================================================================
# 4. BATTLE AXE (Quadrant Bottom-Right: x in 32..63, y in 32..63)
# =============================================================================
def draw_axe():
    ox = 32
    oy = 32
    
    # Shaft: diagonal from (5, 27) up to (22, 10)
    for i in range(6, 23):
        x = i - 1
        y = 31 - i
        p(ox + x,     oy + y,     't')
        p(ox + x + 1, oy + y,     'u')
        p(ox + x - 1, oy + y,     'k')
        p(ox + x + 2, oy + y,     'k')
        if i in (8, 12, 16):
            p(ox + x,     oy + y, 'a')
            p(ox + x + 1, oy + y, 'e')
        elif i in (10, 14):
            p(ox + x,     oy + y, 'Y')
            p(ox + x + 1, oy + y, 'g')

    # Spiked Pommel at bottom-left:
    p(ox + 3, oy + 26, 'k'); p(ox + 4, oy + 26, 'j'); p(ox + 5, oy + 26, 'Y'); p(ox + 6, oy + 26, 'k')
    p(ox + 3, oy + 27, 'k'); p(ox + 4, oy + 27, 'Y'); p(ox + 5, oy + 27, 'g'); p(ox + 6, oy + 27, 'k')
    p(ox + 4, oy + 28, 'k'); p(ox + 5, oy + 28, 'k')
    p(ox + 2, oy + 28, 'k'); p(ox + 3, oy + 28, 'h'); p(ox + 2, oy + 29, 'k')

    # Central Golden Socket with Ruby at (19..22, 8..11):
    p(ox + 18, oy + 11, 'k'); p(ox + 19, oy + 11, 'Y'); p(ox + 20, oy + 11, 'j'); p(ox + 21, oy + 11, 'g'); p(ox + 22, oy + 11, 'k')
    p(ox + 19, oy + 10, 'k'); p(ox + 20, oy + 10, 'v'); p(ox + 21, oy + 10, 'p'); p(ox + 22, oy + 10, 'k')
    p(ox + 20, oy + 9,  'k'); p(ox + 21, oy + 9,  'r'); p(ox + 22, oy + 9,  'v'); p(ox + 23, oy + 9,  'k')
    p(ox + 20, oy + 8,  'k'); p(ox + 21, oy + 8,  'Y'); p(ox + 22, oy + 8,  'j'); p(ox + 23, oy + 8,  'g'); p(ox + 24, oy + 8,  'k')

    # Top Spear Spike at (23..26, 3..7):
    p(ox + 25, oy + 3, 'k')
    p(ox + 24, oy + 4, 'k'); p(ox + 25, oy + 4, 'w'); p(ox + 26, oy + 4, 'k')
    p(ox + 23, oy + 5, 'k'); p(ox + 24, oy + 5, 'h'); p(ox + 25, oy + 5, 'l'); p(ox + 26, oy + 5, 'k')
    p(ox + 22, oy + 6, 'k'); p(ox + 23, oy + 6, 'h'); p(ox + 24, oy + 6, 'm'); p(ox + 25, oy + 6, 's'); p(ox + 26, oy + 6, 'k')
    p(ox + 22, oy + 7, 'k'); p(ox + 23, oy + 7, 'm'); p(ox + 24, oy + 7, 's'); p(ox + 25, oy + 7, 'k')

    # Primary Crescent Blade (Left / Top):
    # Shifted 2px closer to the shaft for perfect double-bitted symmetry:
    left_blade = [
        # row 4:
        (10, 4, 'k'), (11, 4, 'k'),
        # row 5:
        (9,  5, 'k'), (10, 5, 'w'), (11, 5, 'h'), (12, 5, 'k'),
        # row 6:
        (8,  6, 'k'), (9,  6, 'h'), (10, 6, 'l'), (11, 6, 'm'), (12, 6, 's'), (13, 6, 'k'),
        # row 7:
        (7,  7, 'k'), (8,  7, 'h'), (9,  7, 'l'), (10, 7, 'm'), (11, 7, 'm'), (12, 7, 's'), (13, 7, 's'), (14, 7, 'k'), (19, 7, 'k'), (20, 7, 'k'),
        # row 8:
        (7,  8, 'k'), (8,  8, 'w'), (9,  8, 'l'), (10, 8, 'm'), (11, 8, 'm'), (12, 8, 's'), (13, 8, 's'), (14, 8, 's'), (15, 8, 'S'), (16, 8, 'S'), (17, 8, 's'), (18, 8, 's'), (19, 8, 'k'),
        # row 9:
        (7,  9, 'k'), (8,  9, 'h'), (9,  9, 'l'), (10, 9, 'm'), (11, 9, 's'), (12, 9, 's'), (13, 9, 's'), (14, 9, 'S'), (15, 9, 'S'), (16, 9, 's'), (17, 9, 's'), (18, 9, 'k'),
        # row 10:
        (8,  10, 'k'), (9,  10, 'h'), (10, 10, 'l'), (11, 10, 'm'), (12, 10, 's'), (13, 10, 's'), (14, 10, 's'), (15, 10, 'S'), (16, 10, 's'), (17, 10, 'k'),
        # row 11:
        (9,  11, 'k'), (10, 11, 'h'), (11, 11, 'l'), (12, 11, 'm'), (13, 11, 's'), (14, 11, 's'), (15, 11, 's'), (16, 11, 'k'),
        # row 12:
        (10, 12, 'k'), (11, 12, 'w'), (12, 12, 'l'), (13, 12, 'm'), (14, 12, 's'), (15, 12, 'k'),
        # row 13:
        (11, 13, 'k'), (12, 13, 'h'), (13, 13, 'k'),
        # row 14:
        (12, 14, 'k'),
    ]
    for x, y, col in left_blade:
        p(ox + x, oy + y, col)

    # Secondary Crescent Blade (Right / Bottom):
    right_blade = [
        # row 8:
        (25, 8, 'k'), (26, 8, 'w'), (27, 8, 'k'),
        # row 9:
        (25, 9, 's'), (26, 9, 'l'), (27, 9, 'h'), (28, 9, 'k'),
        # row 10:
        (23, 10, 'k'), (24, 10, 'S'), (25, 10, 's'), (26, 10, 'm'), (27, 10, 'l'), (28, 10, 'h'), (29, 10, 'k'),
        # row 11:
        (23, 11, 'k'), (24, 11, 'S'), (25, 11, 's'), (26, 11, 'm'), (27, 11, 'l'), (28, 11, 'h'), (29, 11, 'k'),
        # row 12:
        (22, 12, 'k'), (23, 12, 'S'), (24, 12, 's'), (25, 12, 's'), (26, 12, 'm'), (27, 12, 'l'), (28, 12, 'w'), (29, 12, 'k'),
        # row 13:
        (22, 13, 'k'), (23, 13, 'S'), (24, 13, 's'), (25, 13, 's'), (26, 13, 'm'), (27, 13, 'l'), (28, 13, 'h'), (29, 13, 'k'),
        # row 14:
        (21, 14, 'k'), (22, 14, 'S'), (23, 14, 's'), (24, 14, 's'), (25, 14, 'm'), (26, 14, 'l'), (27, 14, 'h'), (28, 14, 'k'),
        # row 15:
        (21, 15, 'k'), (22, 15, 'S'), (23, 15, 's'), (24, 15, 'm'), (25, 15, 'l'), (26, 15, 'h'), (27, 15, 'k'),
        # row 16:
        (22, 16, 'k'), (23, 16, 's'), (24, 16, 'm'), (25, 16, 'l'), (26, 16, 'w'), (27, 16, 'k'),
        # row 17:
        (23, 17, 'k'), (24, 17, 'm'), (25, 17, 'h'), (26, 17, 'k'),
        # row 18:
        (24, 18, 'k'), (25, 18, 'k'),
    ]
    for x, y, col in right_blade:
        p(ox + x, oy + y, col)

# Draw all four weapons into the 2x2 grid
draw_sword()
draw_bow()
draw_shield()
draw_axe()

# Check stats
stats = c.stats()
print("Stats:", stats['size'], "Colors used:", stats['colors_used'], "Coverage:", stats['coverage'])

view(c)
finish(c)
