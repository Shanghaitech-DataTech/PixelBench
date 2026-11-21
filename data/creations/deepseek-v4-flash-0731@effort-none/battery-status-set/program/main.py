from pixelbench_api import *

c = new_canvas(64, 64)

# Palette colors
body = (200, 200, 200)
outline_dark = (30, 30, 30)
green = (60, 200, 80)
red = (220, 60, 50)
yellow = (240, 210, 60)

y0 = 19
bw, bh = 12, 22
nb_w = 4
gap = 3
# starts: 3, 18, 33, 48  (span ends: 14, 29, 44, 59)

def draw_battery(x, fill_height, fill_color):
    # terminal nub
    c.rect(x + (bw - nb_w)//2, y0, nb_w, 2, outline_dark)
    # body outline
    c.rect(x, y0 + 2, bw, bh, outline_dark)
    # interior
    c.rect(x+1, y0+3, bw-2, bh-2, body)
    # fill from bottom
    fw = bw - 2
    fy = y0 + 3 + (bh - 2 - fill_height)
    c.rect(x+1, fy, fw, fill_height, fill_color)

xs = [3, 18, 33, 48]

# 100%
draw_battery(xs[0], 20, green)

# 60%
draw_battery(xs[1], 12, green)

# 20%
draw_battery(xs[2], 4, red)

# Active charging
draw_battery(xs[3], 8, yellow)
# lightning bolt in the interior
bx = xs[3] + 1
by = y0 + 3
bolt = (60, 200, 80)
c.poly([
    (bx+4, by), (bx+4, by+2), (bx+2, by+2), (bx+2, by+7),
    (bx+5, by+7), (bx+3, by+13), (bx+8, by+6), (bx+5, by+6), (bx+7, by)
], bolt)

finish(c)
print(c.stats_text())
