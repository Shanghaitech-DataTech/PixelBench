from pixelbench_api import *
import math

test_c = new_canvas(128, 128, "#051117")

def catmull_rom_2d(p0, p1, p2, p3, num_pts):
    pts = []
    for s in range(num_pts):
        t = s / float(num_pts)
        t2 = t * t
        t3 = t2 * t
        x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
        y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
        pts.append((x, y))
    return pts

waypoints = [
    (140, 10),
    (127, 16),
    (106, 26),
    (88, 42),
    (98, 60),
    (82, 76),
    (78, 84),
    (76, 92)
]

full_path = []
for i in range(len(waypoints) - 3):
    p0 = waypoints[i]
    p1 = waypoints[i+1]
    p2 = waypoints[i+2]
    p3 = waypoints[i+3]
    seg = catmull_rom_2d(p0, p1, p2, p3, 30)
    full_path.extend(seg)

for x, y in full_path:
    test_c.circle(int(round(x)), int(round(y)), 5, "#ffffff", fill=True)

view(test_c)
