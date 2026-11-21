import math
from pixelbench_api import *

inp = input_canvas
out = inp.copy(name='output')
W = H = 64

white_idx = inp.color('#ffffff')
sky   = out.color('#8ecdf0')
sun   = out.color('#ffd75e')
cloud = out.color('#ffffff')
hill_far = out.color('#a3d46e')
hill_mid = out.color('#7cc250')
grass = out.color('#5da441')
grass2 = out.color('#6cb14d')
dirt  = out.color('#c08a4f')
roadc = out.color('#9a9a9a')
roadd = out.color('#7f7f7f')
dash  = out.color('#ffe98a')
trunk = out.color('#6b4a2a')
leafd = out.color('#2f7d3a')
leafl = out.color('#4f9c4e')
flr_r = out.color('#e2574f')
bird  = out.color('#333333')

def hilltop(x):
    return 15 - 3.5*math.exp(-((x-14)/6.0)**2) - 4.5*math.exp(-((x-47)/9.0)**2)

def in_circle(x, y, cx, cy, r):
    return (x-cx)**2 + (y-cy)**2 <= r*r

def in_ell(x, y, cx, cy, rx, ry):
    return ((x-cx)/rx)**2 + ((y-cy)/ry)**2 <= 1.0

def road_hw(y):
    return min(8 + (y-23)*0.55, 30)

def base_col(x, y):
    t = hilltop(x)
    if y < t:
        return sky
    if y < 20:
        return hill_far
    if y < 23:
        return hill_mid
    dx = abs(x - 32)
    w = road_hw(y)
    if dx <= w:
        return roadd if dx >= w - 1.3 else roadc
    if dx <= w + 2.5:
        return dirt
    if ((x//3) + (y//3)) % 2 == 0:
        return grass
    return grass2

flowers = [(2, 54), (5, 60), (60, 51), (58, 58), (0, 50), (63, 55)]

def cloud_px(x, y):
    return (in_ell(x, y, 26, 5, 9, 2.5) or
            in_ell(x, y, 45, 10, 7, 2.0) or
            in_ell(x, y, 35, 3, 5, 1.8))

def tree_px(x, y):
    if in_circle(x, y, 2, 12, 5):
        return leafl if (x+y) % 3 else leafd
    if 1 <= x <= 2 and 12 <= y <= 19:
        return trunk
    if in_circle(x, y, 61, 12, 5):
        return leafl if (x+y) % 3 else leafd
    if 61 <= x <= 62 and 12 <= y <= 19:
        return trunk
    return None

for y in range(H):
    for x in range(W):
        if inp.get(x, y) != white_idx:
            continue
        base = base_col(x, y)
        col = base
        if in_circle(x, y, 10, 5, 4):
            col = sun
        elif cloud_px(x, y):
            col = cloud
        elif (x, y) in [(30,2),(31,1),(32,2),(35,3),(36,2),(37,3)]:
            col = bird
        elif (x, y) in flowers:
            if base == grass or base == grass2:
                col = flr_r
        else:
            t = tree_px(x, y)
            if t is not None:
                col = t
        if y >= 24 and abs(x - 32) <= 1.0 and road_hw(y) >= 2 and ((y-24)//3) % 2 == 0:
            col = dash
        out.set(x, y, col)

print(out.stats_text())
finish(out)
