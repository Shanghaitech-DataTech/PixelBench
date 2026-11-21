from pixelbench_api import *

c = new_canvas(16, 16)

c_seam = c.color('#221206')
c_dark = c.color('#3e220f')
c_base1 = c.color('#5c3418')
c_base2 = c.color('#7a4722')
c_light = c.color('#9c5e30')
c_high = c.color('#bf7945')

# Sliding windows for smooth wood grain
W_B0 = [
  [c_light, c_base2, c_base1],
  [c_base2, c_base1, c_base2],
  [c_base1, c_base2, c_light],
  [c_base2, c_light, c_base2]
]

W_B1 = [
  [c_base2, c_base1, c_dark],
  [c_base1, c_dark, c_base1],
  [c_dark, c_base1, c_base2],
  [c_base1, c_base2, c_base1]
]

W_B2 = W_B0
W_B3 = W_B1

def draw_board(bx, W, pattern):
    for y in range(16):
        colors = W[pattern[y]]
        c.set(bx, y, colors[0])
        c.set(bx+1, y, colors[1])
        c.set(bx+2, y, colors[2])

# Draw the 4 vertical boards with varying grain patterns
draw_board(0, W_B0, [0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0])
draw_board(4, W_B1, [2, 3, 3, 2, 1, 0, 0, 1, 2, 3, 3, 2, 1, 1, 2, 2])
draw_board(8, W_B2, [1, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 2, 1, 1])
draw_board(12, W_B3, [3, 2, 1, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 1, 2, 3])

# Knots
def knot(bx, by, dark_col):
    c.set(bx+1, by%16, c_seam)
    c.set(bx, by%16, dark_col)
    c.set(bx+2, by%16, dark_col)
    c.set(bx+1, (by-1)%16, dark_col)
    c.set(bx+1, (by+1)%16, dark_col)

knot(0, 11, c_base1)
knot(4, 5, c_dark)
knot(8, 2, c_base1)
knot(12, 8, c_dark)

# Vertical seams
for x in [3, 7, 11, 15]:
    c.line(x, 0, x, 15, c_seam)

# Horizontal seams with alternating light/dark ends and nails
h_seams = [
    (0, 5, c_dark, c_high), (0, 15, c_dark, c_high),
    (4, 1, c_dark, c_light), (4, 9, c_dark, c_light),
    (8, 6, c_dark, c_high), (8, 13, c_dark, c_high),
    (12, 3, c_dark, c_light), (12, 12, c_dark, c_light)
]

for bx, by, shadow_c, high_c in h_seams:
    # Seam groove
    c.line(bx, by, bx+2, by, c_seam)
    # Shadow on the bottom of the upper board
    c.line(bx, (by-1)%16, bx+2, (by-1)%16, shadow_c)
    # Highlight on the top of the lower board
    c.line(bx, (by+1)%16, bx+2, (by+1)%16, high_c)
    
    # Nails
    c.set(bx+1, (by-2)%16, c_seam)
    c.set(bx+1, (by+2)%16, c_seam)

finish(c)
