from pixelbench_api import *
from generate_icons import build_palette

c = new_canvas(64, 64)
pal = build_palette(c)

def p(x, y, char):
    if 0 <= x < 64 and 0 <= y < 64 and char in pal and pal[char] is not None:
        c.set(x, y, pal[char])

# =========================================================================
# QUADRANT 0: SWORD (0..31, 0..31)
# =========================================================================
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

    # Crossguard
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

    # Grip
    p(11, 16, 'k'); p(12, 16, 'a'); p(13, 16, 'L'); p(14, 16, 'k')
    p(10, 17, 'k'); p(11, 17, 'A'); p(12, 17, 'a'); p(13, 17, 'k')
    p(9,  18, 'k'); p(10, 18, 'e'); p(11, 18, 'Y'); p(12, 18, 'k')
    p(8,  19, 'k'); p(9,  19, 'a'); p(10, 19, 'L'); p(11, 19, 'k')
    p(7,  20, 'k'); p(8,  20, 'A'); p(9,  20, 'a'); p(10, 20, 'k')
    p(6,  21, 'k'); p(7,  21, 'e'); p(8,  21, 'Y'); p(9,  21, 'k')
    p(5,  22, 'k'); p(6,  22, 'a'); p(7,  22, 'L'); p(8,  22, 'k')

    # Pommel
    p(4, 23, 'k'); p(5, 23, 'g'); p(6, 23, 'Y'); p(7, 23, 'j'); p(8, 23, 'k')
    p(3, 24, 'k'); p(4, 24, 'g'); p(5, 24, 'v'); p(6, 24, 'p'); p(7, 24, 'Y'); p(8, 24, 'k')
    p(3, 25, 'k'); p(4, 25, 'G'); p(5, 25, 'r'); p(6, 25, 'v'); p(7, 25, 'g'); p(8, 25, 'k')
    p(4, 26, 'k'); p(5, 26, 'G'); p(6, 26, 'g'); p(7, 26, 'k')
    p(5, 27, 'k'); p(6, 27, 'k')


# =========================================================================
# QUADRANT 1: BOW (32..63, 0..31) -> offset x += 32
# =========================================================================
def draw_bow():
    ox = 32
    oy = 0
    
    # Recurve hunting bow angled gracefully
    # Upper tip at (ox + 26, oy + 5)
    # Stave curves through (ox + 16, oy + 7), handle at (ox + 10, oy + 15),
    # lower stave through (ox + 16, oy + 23), lower tip at (ox + 26, oy + 25)
    # Bowstring runs between the tips, pulled back to (ox + 15, oy + 15) with an arrow!
    
    # Let's define the bow stave coordinates:
    # Stave runs from y=5 down to y=25:
    stave_def = [
        # y, x_inner, x_wood, x_wood_hi, x_outer (facing left/belly)
        (5,  [26],     [25],   [24],      [23]),     # Upper tip
        (6,  [24],     [23],   [22],      [21]),
        (7,  [21],     [20],   [19],      [18]),
        (8,  [19],     [18],   [17],      [16]),
        (9,  [17],     [16],   [15],      [14]),
        (10, [15],     [14],   [13],      [12]),
        (11, [14],     [13],   [12],      [11]),
        (12, [13],     [12],   [11],      [10]),
        (13, [12],     [11],   [10],      [9]),
        (14, [11],     [10],   [9],       [8]),      # Grip / riser
        (15, [11],     [10],   [9],       [8]),
        (16, [11],     [10],   [9],       [8]),
        (17, [12],     [11],   [10],      [9]),
        (18, [13],     [12],   [11],      [10]),
        (19, [14],     [13],   [12],      [11]),
        (20, [15],     [14],   [13],      [12]),
        (21, [17],     [16],   [15],      [14]),
        (22, [19],     [18],   [17],      [16]),
        (23, [21],     [20],   [19],      [18]),
        (24, [24],     [23],   [22],      [21]),
        (25, [26],     [25],   [24],      [23]),     # Lower tip
    ]
    
    for y, x_in, x_wd, x_hi, x_out in stave_def:
        # Outer outline (facing left/belly)
        for x in x_out: p(ox + x - 1, oy + y, 'k')
        # Wood highlight / outer wood
        for x in x_hi:
            if 13 <= y <= 17:
                p(ox + x, oy + y, 'Y') # Gold wrap at grip
            elif y in (7, 23):
                p(ox + x, oy + y, 'Y') # Gold collar
            elif y in (5, 6, 24, 25):
                p(ox + x, oy + y, 'h') # Steel tip
            else:
                p(ox + x, oy + y, 'T')
        # Wood core
        for x in x_wd:
            if 13 <= y <= 17:
                p(ox + x, oy + y, 'a') # Leather grip
            elif y in (7, 23):
                p(ox + x, oy + y, 'g')
            elif y in (5, 6, 24, 25):
                p(ox + x, oy + y, 'l')
            else:
                p(ox + x, oy + y, 't')
        # Inner wood / shadow
        for x in x_in:
            if 13 <= y <= 17:
                p(ox + x, oy + y, 'e')
            elif y in (5, 6, 24, 25):
                p(ox + x, oy + y, 's')
            else:
                p(ox + x, oy + y, 'b')
        # Inner outline
        for x in x_in: p(ox + x + 1, oy + y, 'k')
        
    # Tips end caps:
    p(ox + 26, oy + 4, 'k'); p(ox + 27, oy + 5, 'k')
    p(ox + 26, oy + 26, 'k'); p(ox + 27, oy + 25, 'k')
    # Ruby in center of grip:
    p(ox + 9, oy + 15, 'v'); p(ox + 10, oy + 15, 'p')

    # Bowstring:
    # String connects (26, 5) -> nock at (16, 15) -> (26, 25)
    def bres_string(x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        while True:
            p(ox + x0, oy + y0, 'o')
            if x0 == x1 and y0 == y1: break
            e2 = 2 * err
            if e2 > -dy: err -= dy; x0 += sx
            if e2 < dx: err += dx; y0 += sy

    bres_string(25, 6, 16, 15)
    bres_string(16, 15, 25, 24)

    # Arrow:
    # Rest on grip at (8, 15), nocked at (16, 15)
    # Points to the LEFT (towards x=3)!
    # Arrowhead at (ox + 3..6, oy + 14..16):
    p(ox + 2, oy + 15, 'k')
    p(ox + 3, oy + 14, 'k'); p(ox + 3, oy + 15, 'w'); p(ox + 3, oy + 16, 'k')
    p(ox + 4, oy + 13, 'k'); p(ox + 4, oy + 14, 'h'); p(ox + 4, oy + 15, 'l'); p(ox + 4, oy + 16, 'h'); p(ox + 4, oy + 17, 'k')
    p(ox + 5, oy + 13, 'k'); p(ox + 5, oy + 14, 'l'); p(ox + 5, oy + 15, 's'); p(ox + 5, oy + 16, 's'); p(ox + 5, oy + 17, 'k')
    p(ox + 6, oy + 14, 'k'); p(ox + 6, oy + 16, 'k') # barbs
    
    # Arrow shaft:
    for x in range(6, 21):
        if x < 8 or x > 11: # don't overwrite grip
            p(ox + x, oy + 15, 't')
            p(ox + x, oy + 14, 'k')
            p(ox + x, oy + 16, 'k')

    # Fletchings at (ox + 18..22, oy + 13..17):
    # Top feather vane:
    p(ox + 18, oy + 13, 'k'); p(ox + 19, oy + 13, 'C'); p(ox + 20, oy + 13, 'o'); p(ox + 21, oy + 13, 'k')
    p(ox + 17, oy + 14, 'k'); p(ox + 18, oy + 14, 'c'); p(ox + 19, oy + 14, 'C')
    # Bottom feather vane:
    p(ox + 17, oy + 16, 'k'); p(ox + 18, oy + 16, 'c'); p(ox + 19, oy + 16, 'C')
    p(ox + 18, oy + 17, 'k'); p(ox + 19, oy + 17, 'f'); p(ox + 20, oy + 17, 'c'); p(ox + 21, oy + 17, 'k')
    # Nock:
    p(ox + 21, oy + 15, 'Y'); p(ox + 22, oy + 15, 'k')


# =========================================================================
# QUADRANT 2: SHIELD (0..31, 32..63) -> offset y += 32
# =========================================================================
def draw_shield():
    ox = 0
    oy = 32
    
    # Classic knight heater shield:
    # Width: x from 5 to 26 (center x=15.5)
    # Height: y from 4 to 28 (center y=16)
    
    # Shape of heater shield per row y:
    shield_rows = {
        # y: (x_start, x_end)
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
    # Top and bottom outline caps:
    for x in range(8, 24): p(ox + x, oy + 3, 'k')
    p(ox + 15, oy + 29, 'k'); p(ox + 16, oy + 29, 'k')

    # Heavy rim (2px thick gold/steel) and inner field:
    for y, (xs, xe) in shield_rows.items():
        for x in range(xs, xe + 1):
            is_rim = (x in (xs, xs + 1, xe - 1, xe) or y in (4, 5, 27, 28))
            if is_rim:
                # Rim shading: light source from top-left
                if x <= xs + 1 or y <= 5:
                    if x == xs or y == 4:
                        p(ox + x, oy + y, 'j') # bright gold highlight
                    else:
                        p(ox + x, oy + y, 'Y') # gold
                else:
                    if x == xe or y >= 27:
                        p(ox + x, oy + y, 'G') # deep gold shadow
                    else:
                        p(ox + x, oy + y, 'g') # gold shadow
            else:
                # Inner field: deep crimson ruby with curved 3D lighting!
                # Left side is brightly lit ('V', 'v'), center/right is 'r', 'R'
                dist_from_left = x - xs
                if dist_from_left <= 4 and y <= 16:
                    p(ox + x, oy + y, 'V') # bright red
                elif dist_from_left <= 8 and y <= 19:
                    p(ox + x, oy + y, 'v') # mid red
                elif x >= xe - 4 or y >= 22:
                    p(ox + x, oy + y, 'R') # deep wine shadow
                else:
                    p(ox + x, oy + y, 'r') # dark crimson

    # Golden rivets at the corners:
    rivets = [(7, 6), (24, 6), (7, 16), (24, 16), (10, 22), (21, 22)]
    for rx, ry in rivets:
        p(ox + rx, oy + ry, 'J')
        p(ox + rx, oy + ry + 1, 'G')

    # Magnificent Golden Crest Emblem in center of shield:
    # A golden crowned heraldic lion / knight cross!
    # Let's draw an ornate Golden Knight Cross with central gem:
    # Vertical bar at x=15, 16: y from 8 to 22
    # Horizontal bar at y=12, 13: x from 9 to 22
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
        
    # Cross flared ends (Pattée ends):
    # Top end:
    p(ox + 14, oy + 8, 'j'); p(ox + 17, oy + 8, 'Y')
    p(ox + 13, oy + 7, 'k'); p(ox + 14, oy + 7, 'j'); p(ox + 15, oy + 7, 'J'); p(ox + 16, oy + 7, 'j'); p(ox + 17, oy + 7, 'Y'); p(ox + 18, oy + 7, 'k')
    # Left end:
    p(ox + 9, oy + 11, 'j'); p(ox + 9, oy + 14, 'Y')
    p(ox + 8, oy + 11, 'k'); p(ox + 8, oy + 12, 'j'); p(ox + 8, oy + 13, 'Y'); p(ox + 8, oy + 14, 'k')
    # Right end:
    p(ox + 22, oy + 11, 'j'); p(ox + 22, oy + 14, 'Y')
    p(ox + 23, oy + 11, 'k'); p(ox + 23, oy + 12, 'j'); p(ox + 23, oy + 13, 'Y'); p(ox + 23, oy + 14, 'k')
    # Bottom end:
    p(ox + 14, oy + 22, 'j'); p(ox + 17, oy + 22, 'Y')
    p(ox + 14, oy + 23, 'k'); p(ox + 15, oy + 23, 'Y'); p(ox + 16, oy + 23, 'g'); p(ox + 17, oy + 23, 'k')

    # Central Blue / Ruby Boss Gem in center of cross (x=15..16, y=12..13):
    p(ox + 15, oy + 12, 'w') # specular spark
    p(ox + 16, oy + 12, 'h')
    p(ox + 15, oy + 13, 'l')
    p(ox + 16, oy + 13, 's')
    # Dark border around central boss:
    p(ox + 14, oy + 12, 'G'); p(ox + 14, oy + 13, 'G')
    p(ox + 17, oy + 12, 'g'); p(ox + 17, oy + 13, 'g')


# =========================================================================
# QUADRANT 3: BATTLE AXE (32..63, 32..63) -> offset x += 32, y += 32
# =========================================================================
def draw_axe():
    ox = 32
    oy = 32
    
    # Diagonal Shaft from (6, 26) to (24, 8)
    # Axe head at top-right (around 19..25, 6..12)
    # Double-bitted massive curved blades:
    # Blade 1 (Left/Top) curves up-left to (12, 4)
    # Blade 2 (Right/Bottom) curves down-right to (26, 18)
    # Top thrusting spear-point at (26, 6)
    
    # 1. Shaft (wood with leather criss-cross wraps and gold rings):
    for i in range(7, 26):
        x = i
        y = 32 - i
        # 2-pixel wide shaft
        p(ox + x, oy + y, 't')
        p(ox + x + 1, oy + y, 'u')
        # Outlines:
        p(ox + x - 1, oy + y, 'k')
        p(ox + x + 2, oy + y, 'k')
        # Leather wraps:
        if i in (10, 14, 18):
            p(ox + x, oy + y, 'a')
            p(ox + x + 1, oy + y, 'e')
        elif i in (12, 16):
            p(ox + x, oy + y, 'Y')
            p(ox + x + 1, oy + y, 'g')

    # Spiked / Golden Pommel at (ox + 5..7, oy + 25..27):
    p(ox + 4, oy + 27, 'k'); p(ox + 5, oy + 27, 'j'); p(ox + 6, oy + 27, 'Y'); p(ox + 7, oy + 27, 'k')
    p(ox + 4, oy + 28, 'k'); p(ox + 5, oy + 28, 'Y'); p(ox + 6, oy + 28, 'g'); p(ox + 7, oy + 28, 'k')
    p(ox + 5, oy + 29, 'k'); p(ox + 6, oy + 29, 'k')
    # Bottom spike:
    p(ox + 3, oy + 29, 'k'); p(ox + 4, oy + 29, 'h'); p(ox + 3, oy + 30, 'k')

    # 2. Axe Head Collar / Socket at (21..23, 9..11):
    # Heavy gold band with ruby:
    p(ox + 20, oy + 12, 'k'); p(ox + 21, oy + 12, 'Y'); p(ox + 22, oy + 12, 'j'); p(ox + 23, oy + 12, 'g'); p(ox + 24, oy + 12, 'k')
    p(ox + 21, oy + 11, 'k'); p(ox + 22, oy + 11, 'v'); p(ox + 23, oy + 11, 'p'); p(ox + 24, oy + 11, 'k')
    p(ox + 22, oy + 10, 'k'); p(ox + 23, oy + 10, 'r'); p(ox + 24, oy + 10, 'v'); p(ox + 25, oy + 10, 'k')
    p(ox + 22, oy + 9,  'k'); p(ox + 23, oy + 9,  'Y'); p(ox + 24, oy + 9,  'j'); p(ox + 25, oy + 9,  'g'); p(ox + 26, oy + 9,  'k')

    # 3. Top Thrusting Spike at (25..28, 4..8):
    p(ox + 27, oy + 4, 'k')
    p(ox + 26, oy + 5, 'k'); p(ox + 27, oy + 5, 'w'); p(ox + 28, oy + 5, 'k')
    p(ox + 25, oy + 6, 'k'); p(ox + 26, oy + 6, 'h'); p(ox + 27, oy + 6, 'l'); p(ox + 28, oy + 6, 'k')
    p(ox + 24, oy + 7, 'k'); p(ox + 25, oy + 7, 'h'); p(ox + 26, oy + 7, 'm'); p(ox + 27, oy + 7, 's'); p(ox + 28, oy + 7, 'k')
    p(ox + 24, oy + 8, 'k'); p(ox + 25, oy + 8, 'm'); p(ox + 26, oy + 8, 's'); p(ox + 27, oy + 8, 'k')

    # 4. Upper/Left Crescent Blade:
    # Sweeps out to (10, 4) with sharp curved cutting edge:
    # Outer cutting edge:
    p(ox + 10, oy + 4, 'k')
    p(ox + 9,  oy + 5, 'k'); p(ox + 10, oy + 5, 'w'); p(ox + 11, oy + 5, 'k')
    p(ox + 9,  oy + 6, 'k'); p(ox + 10, oy + 6, 'h'); p(ox + 11, oy + 6, 'l'); p(ox + 12, oy + 6, 'k')
    p(ox + 10, oy + 7, 'k'); p(ox + 11, oy + 7, 'h'); p(ox + 12, oy + 7, 'l'); p(ox + 13, oy + 7, 'm'); p(ox + 14, oy + 7, 'k')
    p(ox + 11, oy + 8, 'k'); p(ox + 12, oy + 8, 'h'); p(ox + 13, oy + 8, 'm'); p(ox + 14, oy + 8, 's'); p(ox + 15, oy + 8, 'k')
    p(ox + 13, oy + 9, 'k'); p(ox + 14, oy + 9, 'l'); p(ox + 15, oy + 9, 'm'); p(ox + 16, oy + 9, 's'); p(ox + 17, oy + 9, 'k')
    p(ox + 15, oy + 10, 'k'); p(ox + 16, oy + 10, 'm'); p(ox + 17, oy + 10, 's'); p(ox + 18, oy + 10, 'k')
    p(ox + 17, oy + 11, 'k'); p(ox + 18, oy + 11, 's'); p(ox + 19, oy + 11, 'S'); p(ox + 20, oy + 11, 'k')
    # Blade inner throat cutout:
    p(ox + 12, oy + 5, 'k'); p(ox + 13, oy + 6, 'k'); p(ox + 14, oy + 6, 'k')
    p(ox + 15, oy + 7, 'k'); p(ox + 16, oy + 8, 'k'); p(ox + 17, oy + 8, 'k'); p(ox + 18, oy + 9, 'k')
    # Sparkle glint on upper blade tip:
    p(ox + 10, oy + 5, 'w'); p(ox + 9, oy + 5, 'h'); p(ox + 10, oy + 4, 'h')

    # 5. Lower/Right Crescent Blade:
    # Sweeps down to (27, 20) with sharp curved cutting edge:
    p(ox + 21, oy + 13, 'k'); p(ox + 22, oy + 13, 'S'); p(ox + 23, oy + 13, 's'); p(ox + 24, oy + 13, 'k')
    p(ox + 22, oy + 14, 'k'); p(ox + 23, oy + 14, 's'); p(ox + 24, oy + 14, 'm'); p(ox + 25, oy + 14, 'k')
    p(ox + 23, oy + 15, 'k'); p(ox + 24, oy + 15, 'm'); p(ox + 25, oy + 15, 'l'); p(ox + 26, oy + 15, 'k')
    p(ox + 24, oy + 16, 'k'); p(ox + 25, oy + 16, 'l'); p(ox + 26, oy + 16, 'h'); p(ox + 27, oy + 16, 'k')
    p(ox + 25, oy + 17, 'k'); p(ox + 26, oy + 17, 'h'); p(ox + 27, oy + 17, 'w'); p(ox + 28, oy + 17, 'k')
    p(ox + 26, oy + 18, 'k'); p(ox + 27, oy + 18, 'h'); p(ox + 28, oy + 18, 'k')
    p(ox + 27, oy + 19, 'k')
    # Inner throat cutout for lower blade:
    p(ox + 21, oy + 14, 'k'); p(ox + 22, oy + 15, 'k'); p(ox + 23, oy + 16, 'k')
    p(ox + 24, oy + 17, 'k'); p(ox + 25, oy + 18, 'k'); p(ox + 26, oy + 19, 'k')
    # Sparkle on lower blade:
    p(ox + 27, oy + 17, 'w')

draw_sword()
draw_bow()
draw_shield()
draw_axe()

view(c)
