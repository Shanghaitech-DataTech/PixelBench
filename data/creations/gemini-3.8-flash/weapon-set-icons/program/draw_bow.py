from pixelbench_api import *
from generate_icons import build_palette, paste_ascii
import math

def get_bow_grid():
    grid = [['.' for _ in range(32)] for _ in range(32)]
    def p(y, x, c):
        if 0 <= y < 32 and 0 <= x < 32:
            grid[y][x] = c

    # Let's plot the smooth arc:
    # Stave width is 3 pixels: outer outline, wood core (with highlight on outer side), inner outline
    # Center of arc: (26, 26).
    # Radii: R_outer = 20, R_core = 19, R_inner = 18.
    
    # Let's rasterize the circular arc from theta = 92 deg to 178 deg:
    angles = [90 + i * (90.0 / 40.0) for i in range(41)]
    
    cx, cy = 25.0, 25.0
    
    # Let's directly craft the pixel-perfect arc coordinates:
    # Outer outline points (symmetric across x=y):
    # We define (x, y) for y <= x, and mirror to (y, x):
    stave_pixels = {
        # Recurve tip:
        (26, 8): ('k', 'l'),
        (25, 7): ('k', 'w'),
        (24, 7): ('Y', 'j'), # Gold band
        (23, 7): ('k', 't'),
        # Arc:
        (22, 7): ('k', 'T'), (22, 8): ('t', 'u'), (22, 9): ('k', 'k'),
        (21, 8): ('k', 'T'), (21, 9): ('t', 'u'), (21, 10): ('k', 'k'),
        (20, 9): ('k', 'T'), (20, 10): ('t', 'u'), (20, 11): ('k', 'k'),
        (19, 10): ('k', 'T'), (19, 11): ('t', 'u'), (19, 12): ('k', 'k'),
        (18, 11): ('k', 'T'), (18, 12): ('t', 'u'), (18, 13): ('k', 'k'),
        (17, 12): ('k', 'T'), (17, 13): ('t', 'u'), (17, 14): ('k', 'k'),
        (16, 13): ('k', 'T'), (16, 14): ('t', 'u'), (16, 15): ('k', 'k'),
        (15, 14): ('k', 'T'), (15, 15): ('t', 'u'), (15, 16): ('k', 'k'),
    }

    # Instead of dictionary guessing, let's write out the 32x32 ASCII directly,
    # ensuring each row is clean and visible!
    pass

