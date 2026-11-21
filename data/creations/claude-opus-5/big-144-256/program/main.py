import random
from mage import draw_mage, draw_glow

out = input_canvas.copy(name="output")
W, H = 144, 256

# ---------------------------------------------------------------- palette
STEM  = out.color("#223a26", "vine_stem")
STEM2 = out.color("#2b4a31", "vine_stem2")
LF_D  = out.color("#1e3722", "leaf_dark")
LF_M  = out.color("#2e5133", "leaf_mid")
LF_L  = out.color("#41703f", "leaf_light")

# ---------------------------------------------------------------- vines
vines = new_canvas(W, H, name="vines")


def cubic_pts(p0, p1, p2, p3, n=48):
    pts = []
    for i in range(n + 1):
        t = i / n
        m = 1 - t
        x = m*m*m*p0[0] + 3*m*m*t*p1[0] + 3*m*t*t*p2[0] + t*t*t*p3[0]
        y = m*m*m*p0[1] + 3*m*m*t*p1[1] + 3*m*t*t*p2[1] + t*t*t*p3[1]
        q = (round(x), round(y))
        if not pts or pts[-1] != q:
            pts.append(q)
    return pts


def leaf(c, x, y, side, big=True):
    if big:
        px = [(0, 0, LF_M), (1, 0, LF_M), (2, 0, LF_D),
              (0, 1, LF_D), (1, 1, LF_M), (1, -1, LF_D), (0, -1, LF_L)]
    else:
        px = [(0, 0, LF_M), (1, 0, LF_D), (0, -1, LF_L)]
    for dx, dy, col in px:
        c.set(x + side * dx, y + dy, col)


def vine(c, p0, p1, p2, p3, every=3, seed=1, tip=True):
    pts = cubic_pts(p0, p1, p2, p3)
    rnd = random.Random(seed)
    for i in range(len(pts) - 1):
        col = STEM if i % 5 else STEM2
        c.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], col)
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        if i < 1:
            continue
        if i % every == 0:
            side = 1 if (i // every) % 2 == 0 else -1
            big = i < n * 0.8 and rnd.random() < 0.8
            leaf(c, x + side, y, side, big)
    if tip:
        tx, ty = pts[-1]
        c.set(tx, ty + 1, STEM)


# strands hanging from the cornice over the lower facade
HANG = [
    (33, 152, 186,  4, 3),
    (38, 152, 172, -3, 3),
    (44, 153, 164,  2, 3),
    (51, 153, 163, -2, 4),
    (58, 152, 162,  3, 4),
    (65, 152, 180, -4, 3),
    (71, 152, 192,  4, 3),
    (78, 152, 174, -3, 4),
    (85, 152, 200,  5, 3),
    (91, 152, 168, -4, 3),
    (97, 152, 188,  3, 3),
    (104, 152, 178, -4, 3),
    (110, 153, 196,  4, 3),
    (117, 155, 176, -3, 4),
    (124, 157, 198,  5, 3),
    (131, 159, 180, -4, 4),
    (137, 161, 190,  3, 3),
]
for i, (x, y0, y1, bend, ev) in enumerate(HANG):
    h = y1 - y0
    vine(vines,
         (x, y0),
         (x + bend, y0 + h * 0.35),
         (x - bend, y0 + h * 0.7),
         (x + bend // 2, y1),
         every=ev, seed=10 + i)

# creepers climbing the round tower wall
vine(vines, (43, 152), (39, 136), (48, 122), (43, 100), every=3, seed=3)
vine(vines, (49, 151), (54, 138), (47, 124), (52, 106), every=4, seed=4)
vine(vines, (57, 151), (61, 140), (55, 128), (59, 114), every=4, seed=5)
vine(vines, (100, 150), (104, 137), (97, 124), (101, 104), every=3, seed=6)
vine(vines, (94, 150), (90, 139), (96, 128), (92, 112), every=4, seed=7)
vine(vines, (106, 152), (110, 142), (104, 132), (108, 120), every=4, seed=8)
# creepers rising from the ground along the facade
vine(vines, (31, 214), (35, 200), (29, 188), (33, 170), every=3, seed=11)
vine(vines, (68, 212), (72, 198), (66, 186), (70, 168), every=3, seed=12)
vine(vines, (113, 214), (117, 200), (111, 190), (115, 174), every=3, seed=13)
vine(vines, (140, 212), (136, 198), (142, 186), (138, 172), every=4, seed=14)
# a horizontal runner along the cornice
vine(vines, (30, 153), (60, 149), (100, 156), (140, 152), every=5, seed=15)

# keep the archway mouth and the lanterns clear of foliage
vines.clear(46, 164, 18, 52)

out.blit(vines, 0, 0)

# ---------------------------------------------------------------- mage + glow
ox, oy = draw_mage(out, cx=55, top=182, floor=211)
draw_glow(out, ox, oy, floor=211)

print(out.stats_text())
view(out)
view(out.copy(name="zoom_in").select(40, 160, 36, 60).preview(), scale=8)
