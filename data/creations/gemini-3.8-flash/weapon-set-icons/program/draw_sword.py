from pixelbench_api import *
from generate_icons import build_palette, paste_ascii

def get_sword_grid():
    grid = [['.' for _ in range(32)] for _ in range(32)]
    def p(y, x, c):
        if 0 <= y < 32 and 0 <= x < 32:
            grid[y][x] = c
            
    # Tapered tip to (27, 1):
    p(1, 27, 'k')
    p(2, 26, 'k'); p(2, 27, 'w'); p(2, 28, 'k')
    p(3, 25, 'k'); p(3, 26, 'h'); p(3, 27, 's'); p(3, 28, 'k')
    p(4, 24, 'k'); p(4, 25, 'h'); p(4, 26, 'l'); p(4, 27, 's'); p(4, 28, 'k')
    
    # Rows 5 to 13: perfectly parallel blade
    for y in range(5, 14):
        xl = 28 - y
        p(y, xl,     'k')
        p(y, xl + 1, 'h')
        p(y, xl + 2, 'l')
        p(y, xl + 3, 'm')
        p(y, xl + 4, 's')
        p(y, xl + 5, 'k')

    # Sparkle / Glint near tip:
    p(2, 27, 'w')
    p(3, 26, 'w')
    p(3, 25, 'h')
    p(4, 26, 'h')
    
    # Crossguard:
    p(10, 8, 'k'); p(10, 9, 'k')
    p(11, 7, 'k'); p(11, 8, 'j'); p(11, 9, 'Y'); p(11, 10, 'k')
    p(12, 7, 'k'); p(12, 8, 'Y'); p(12, 9, 'j'); p(12, 10, 'Y'); p(12, 11, 'k')
    p(13, 8, 'k'); p(13, 9, 'g'); p(13, 10, 'Y'); p(13, 11, 'j'); p(13, 12, 'Y'); p(13, 13, 'k')
    
    # Center guard & Ruby
    p(14, 10, 'k'); p(14, 11, 'g'); p(14, 12, 'Y'); p(14, 13, 'v'); p(14, 14, 'p'); p(14, 15, 'Y'); p(14, 16, 'k')
    p(15, 11, 'k'); p(15, 12, 'G'); p(15, 13, 'r'); p(15, 14, 'v'); p(15, 15, 'Y'); p(15, 16, 'j'); p(15, 17, 'k')
    
    # Right quillon
    p(16, 12, 'k'); p(16, 13, 'k'); p(16, 14, 'G'); p(16, 15, 'g'); p(16, 16, 'Y'); p(16, 17, 'j'); p(16, 18, 'k')
    p(17, 15, 'k'); p(17, 16, 'g'); p(17, 17, 'Y'); p(17, 18, 'j'); p(17, 19, 'k')
    p(18, 16, 'k'); p(18, 17, 'G'); p(18, 18, 'g'); p(18, 19, 'Y'); p(18, 20, 'k')
    p(19, 18, 'k'); p(19, 19, 'k'); p(19, 20, 'k')

    # Grip:
    p(16, 11, 'k'); p(16, 12, 'a'); p(16, 13, 'L'); p(16, 14, 'k')
    p(17, 10, 'k'); p(17, 11, 'A'); p(17, 12, 'a'); p(17, 13, 'k')
    p(18, 9, 'k'); p(18, 10, 'e'); p(18, 11, 'Y'); p(18, 12, 'k')
    p(19, 8, 'k'); p(19, 9, 'a'); p(19, 10, 'L'); p(19, 11, 'k')
    p(20, 7, 'k'); p(20, 8, 'A'); p(20, 9, 'a'); p(20, 10, 'k')
    p(21, 6, 'k'); p(21, 7, 'e'); p(21, 8, 'Y'); p(21, 9, 'k')
    p(22, 5, 'k'); p(22, 6, 'a'); p(22, 7, 'L'); p(22, 8, 'k')

    # Pommel:
    p(23, 4, 'k'); p(23, 5, 'g'); p(23, 6, 'Y'); p(23, 7, 'j'); p(23, 8, 'k')
    p(24, 3, 'k'); p(24, 4, 'g'); p(24, 5, 'v'); p(24, 6, 'p'); p(24, 7, 'Y'); p(24, 8, 'k')
    p(25, 3, 'k'); p(25, 4, 'G'); p(25, 5, 'r'); p(25, 6, 'v'); p(25, 7, 'g'); p(25, 8, 'k')
    p(26, 4, 'k'); p(26, 5, 'G'); p(26, 6, 'g'); p(26, 7, 'k')
    p(27, 5, 'k'); p(27, 6, 'k')

    return ["".join(row) for row in grid]

c = new_canvas(32, 32)
pal = build_palette(c)
paste_ascii(c, 0, 0, get_sword_grid(), pal)
view(c)
