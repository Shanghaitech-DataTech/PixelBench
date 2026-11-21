from pixelbench_api import *
from generate_icons import build_palette, paste_ascii

# Let's write the complete 64x64 canvas generator with all 4 weapons,
# pixel by pixel, cleanly and beautifully.

c = new_canvas(64, 64)
pal = build_palette(c)

def p(x, y, char):
    if 0 <= x < 64 and 0 <= y < 64 and char in pal and pal[char] is not None:
        c.set(x, y, pal[char])

# -------------------------------------------------------------
# 1. SWORD (Quadrant 0: 0..31, 0..31)
# -------------------------------------------------------------
from preview_all import draw_sword, draw_shield

# -------------------------------------------------------------
# 2. DIAGONAL RECURVE BOW (Quadrant 1: 32..63, 0..31)
# -------------------------------------------------------------
# Local quadrant 32x32:
# Tips at (26, 6) and (6, 26).
# Handle/belly at (10, 10).
# Bowstring connecting (26, 7) down-left to (7, 26).
# With an arrow notched along the diagonal (x=y) from (4, 4) to (20, 20)!
def draw_diagonal_bow():
    ox = 32
    oy = 0
    
    # We define the bow stave coordinates symmetrically:
    # Stave width: 3 pixels (outer outline 'k', highlight 'T', core 't'/'b', inner outline 'k')
    # Points along the arc from handle (10, 10) to tip (26, 6):
    # (x, y) coordinates:
    arc_points = [
        # (x, y) of the wood core
        (10, 10), (11, 10), (12, 9), (13, 9), (14, 8), (15, 8),
        (16, 7), (17, 7), (18, 7), (19, 6), (20, 6), (21, 6), (22, 6)
    ]
    
    # Draw upper half and mirror to lower half across x=y:
    for x, y in arc_points:
        # Wood highlight and core
        if (x, y) == (10, 10):
            # Handle gold & ruby
            col = 'Y'
        elif x in (21, 22):
            col = 'Y' # Gold collar
        else:
            col = 'T'
            
        p(ox + x, oy + y, col)
        p(ox + y, oy + x, col) # Transpose!
        
        # Inner wood core:
        p(ox + x, oy + y + 1, 'b')
        p(ox + y + 1, oy + x, 'b')
        
    # Recurve tip finials (carved steel/horn):
    tips = [(23, 6, 'h'), (24, 6, 'w'), (25, 7, 'l'), (25, 8, 's')]
    for x, y, col in tips:
        p(ox + x, oy + y, col)
        p(ox + y, oy + x, col)

    # Leather wrapped handle at (10..12, 10..12):
    p(ox + 9,  oy + 9,  'Y'); p(ox + 10, oy + 9,  'j')
    p(ox + 9,  oy + 10, 'j'); p(ox + 10, oy + 10, 'v'); p(ox + 10, oy + 11, 'p') # Ruby
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

    # Bowstring connecting (25, 8) to (8, 25) along x + y = 33:
    for i in range(9, 25):
        x = i
        y = 33 - i
        # Don't draw over arrow
        p(ox + x, oy + y, 'o')

    # Notched Arrow along diagonal x = y:
    # Arrowhead at (3, 3) to (7, 7):
    arrowhead = [
        (3, 3, 'k'),
        (3, 4, 'k'), (4, 3, 'k'), (4, 4, 'w'),
        (3, 5, 'k'), (5, 3, 'k'), (4, 5, 'h'), (5, 4, 'h'), (5, 5, 'l'),
        (4, 6, 'k'), (6, 4, 'k'), (5, 6, 'l'), (6, 5, 'l'), (6, 6, 'm'),
        (5, 7, 'k'), (7, 5, 'k'), (6, 7, 's'), (7, 6, 's'), (7, 7, 'S'),
        (6, 8, 'k'), (8, 6, 'k'), # barbs
    ]
    for x, y, col in arrowhead:
        p(ox + x, oy + y, col)

    # Arrow shaft along x = y:
    for i in range(8, 20):
        if (i, i) not in [(10, 10), (11, 11)]: # let ruby show
            p(ox + i, oy + i, 't')
            p(ox + i, oy + i + 1, 'u')

    # Fletchings at (19..23, 19..23):
    fletching = [
        (19, 18, 'C'), (18, 19, 'C'),
        (20, 18, 'o'), (18, 20, 'o'), (20, 19, 'C'), (19, 20, 'C'),
        (21, 19, 'o'), (19, 21, 'o'), (21, 20, 'c'), (20, 21, 'c'),
        (22, 20, 'C'), (20, 22, 'C'), (22, 21, 'f'), (21, 22, 'f'),
        (23, 21, 'k'), (21, 23, 'k'), (23, 22, 'k'), (22, 23, 'k'),
        (22, 22, 'Y'), (23, 23, 'j'), (24, 24, 'k') # Nock
    ]
    for x, y, col in fletching:
        p(ox + x, oy + y, col)


# -------------------------------------------------------------
# 3. BATTLE AXE (Quadrant 3: 32..63, 32..63)
# -------------------------------------------------------------
# Shifted 2 pixels to the left so it has plenty of margin!
def draw_perfect_axe():
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
        # Leather wraps:
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
    # Bottom spike:
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
    # Roots into socket at (19, 10).
    # Flares out to sharp horns at (8, 4) and (14, 13).
    # Outer cutting edge bows out towards (6, 8):
    left_blade = [
        # row 4:
        (8, 4, 'k'), (9, 4, 'k'),
        # row 5:
        (7, 5, 'k'), (8, 5, 'w'), (9, 5, 'h'), (10, 5, 'k'),
        # row 6:
        (6, 6, 'k'), (7, 6, 'h'), (8, 6, 'l'), (9, 6, 'm'), (10, 6, 's'), (11, 6, 'k'),
        # row 7:
        (5, 7, 'k'), (6, 7, 'h'), (7, 7, 'l'), (8, 7, 'm'), (9, 7, 'm'), (10, 7, 's'), (11, 7, 's'), (12, 7, 'k'), (19, 7, 'k'), (20, 7, 'k'),
        # row 8:
        (5, 8, 'k'), (6, 8, 'w'), (7, 8, 'l'), (8, 8, 'm'), (9, 8, 'm'), (10, 8, 's'), (11, 8, 's'), (12, 8, 's'), (13, 8, 'S'), (14, 8, 'S'), (15, 8, 's'), (16, 8, 's'), (17, 8, 's'), (18, 8, 's'), (19, 8, 'k'),
        # row 9:
        (5, 9, 'k'), (6, 9, 'h'), (7, 9, 'l'), (8, 9, 'm'), (9, 9, 's'), (10, 9, 's'), (11, 9, 's'), (12, 9, 'S'), (13, 9, 'S'), (14, 9, 'S'), (15, 9, 's'), (16, 9, 's'), (17, 9, 's'), (18, 9, 'k'),
        # row 10:
        (6, 10, 'k'), (7, 10, 'h'), (8, 10, 'l'), (9, 10, 'm'), (10, 10, 's'), (11, 10, 's'), (12, 10, 's'), (13, 10, 'S'), (14, 10, 's'), (15, 10, 's'), (16, 10, 's'), (17, 10, 'k'),
        # row 11:
        (7, 11, 'k'), (8, 11, 'h'), (9, 11, 'l'), (10, 11, 'm'), (11, 11, 's'), (12, 11, 's'), (13, 11, 's'), (14, 11, 's'), (15, 11, 'k'),
        # row 12:
        (8, 12, 'k'), (9, 12, 'w'), (10, 12, 'l'), (11, 12, 'm'), (12, 12, 's'), (13, 12, 'k'),
        # row 13:
        (9, 13, 'k'), (10, 13, 'h'), (11, 13, 'k'),
        # row 14:
        (10, 14, 'k'),
    ]
    for x, y, col in left_blade:
        p(ox + x, oy + y, col)

    # Secondary Crescent Blade (Right / Bottom):
    # Roots into socket at (21, 10).
    # Flares out to sharp horns at (26, 8) and (28, 18).
    # Cutting edge bows out towards (29, 13):
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


draw_sword()
draw_shield()
draw_diagonal_bow()
draw_perfect_axe()

view(c)
