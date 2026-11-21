from pixelbench_api import *

c = new_canvas(48, 48, name="slash")
white = c.color("#ffffff")

# Clean white arc slash effect on 48x48.
# A sweeping arc slash from upper-right to lower-left.
# Thick cutting blade in the middle, tapering at both ends, with a trailing streak.

import math

def bezier_quad(p0, p1, p2, t):
    x = (1-t)*(1-t)*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0]
    y = (1-t)*(1-t)*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
    return (x, y)

# Arc curve: start upper-right (36,5), control (20,16), end lower-left (14,40)
points = [bezier_quad((36, 5), (20, 16), (14, 40), t/80) for t in range(81)]

def perp(x0,y0,x1,y1):
    dx,dy = x1-x0, y1-y0
    l = math.sqrt(dx*dx+dy*dy)
    if l < 0.001: return (1.0, 0.0)
    return (-dy/l, dx/l)

# Variable thickness: thin at both tips, thick in the main cutting section
def thickness2(t):
    # Sharp start tip at t~0, full thickness by t~0.15
    # Taper back to point around t~0.9
    if t < 0.1:
        return 3.0 * (t / 0.1)
    if t > 0.85:
        return max(0.5, 3.0 * ((1.0 - t) / 0.15))
    return 3.0

# Build one side out and the other back to make a filled variable-width blade
left_side = []
right_side = []
for i, (x, y) in enumerate(points):
    if i < len(points)-1:
        nx, ny = perp(x, y, points[i+1][0], points[i+1][1])
    else:
        nx, ny = perp(points[-2][0], points[-2][1], x, y)
    t = i / 80
    th = thickness2(t)
    left_side.append((x + nx * th, y + ny * th))
    right_side.append((x - nx * th, y - ny * th))

poly = left_side + right_side[::-1]
c.poly([(int(round(x)), int(round(y))) for x,y in poly], white, fill=True)

# Ensure the center line is solid
for i in range(len(points)-1):
    c.line(int(round(points[i][0])), int(round(points[i][1])),
           int(round(points[i+1][0])), int(round(points[i+1][1])), white)

# Trailing streak extending from the lower-left tip
end_pt = points[-1]
prev_pt = points[-4]
dx = end_pt[0] - prev_pt[0]
dy = end_pt[1] - prev_pt[1]
l = math.sqrt(dx*dx + dy*dy)
if l > 0.001:
    ux, uy = dx/l, dy/l
    for ext in range(1, 10):
        sx1 = int(round(end_pt[0] + ux * ext))
        sy1 = int(round(end_pt[1] + uy * ext))
        sx2 = int(round(end_pt[0] + ux * (ext+1)))
        sy2 = int(round(end_pt[1] + uy * (ext+1)))
        if 0 <= sx2 < 48 and 0 <= sy2 < 48:
            c.line(sx1, sy1, sx2, sy2, white)

# Slightly thicker trail - add a parallel thin line for substance
if l > 0.001:
    ux, uy = dx/l, dy/l
    px, py = -uy, ux
    for ext in range(2, 8):
        sx1 = int(round(end_pt[0] + ux * ext + px))
        sy1 = int(round(end_pt[1] + uy * ext + py))
        sx2 = int(round(end_pt[0] + ux * (ext+0.6)))
        sy2 = int(round(end_pt[1] + uy * (ext+0.6)))
        if 0 <= sx2 < 48 and 0 <= sy2 < 48:
            c.line(sx1, sy1, sx2, sy2, white)

result = [c]
finish(result)
