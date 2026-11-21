from pixelbench_api import *

# Gold coin with a 5-pointed star, 16x16, at most 6 colors

W, H = 16, 16
c = new_canvas(W, H, background=None, name="gold-star-coin")

DARK = "#8a5a00"
MED  = "#d4a017"
STAR = "#fff7d4"
SHADE = "#b8860b"

# Coin
c.circle(7, 8, 7, DARK, fill=True)
c.circle(7, 8, 6, MED, fill=True)

# Shading at bottom of the coin  
c.ellipse(7, 13, 3, 1, SHADE, fill=True)

# 5-pointed star
star_poly = [
    (7, 2.5), (8.5, 6), (12, 7), (8.5, 9), (9.5, 12),
    (7, 10), (4.5, 12), (5.5, 9), (2, 7), (5.5, 6),
]
c.poly(star_poly, STAR, fill=True)

print(c.stats_text())
print(c.matrix_text(region=(0,0,15,15)))
finish(c)
