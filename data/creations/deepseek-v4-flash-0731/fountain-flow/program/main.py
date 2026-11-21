from pixelbench_api import *

src = input_canvas
c = src.copy(name="output")

water  = c.color("#2f6fdb")
wlight = c.color("#6cb6ff")
foam   = c.color("#d7ecff")
white  = c.color("#ffffff")

ia = src.color("#413e51")
ic = src.color("#645d72")
id_ = src.color("#ffffff")
ie = src.color("#e1e2ba")
ig = src.color("#2ec7dc")
if_ = src.color("#1d8baa")

def rep(y0, y1, x0, x1, colors_water, colors_foam):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            col = src.get(x, y)
            if col in colors_water:
                c.set(x, y, water)
            elif col in colors_foam:
                c.set(x, y, foam)

# --- basins turned to water ---
rep(5, 7, 10, 53, (ia,), (id_,))
rep(8, 19, 18, 45, (ia, ig, if_, ic), (id_,))
rep(20, 31, 10, 53, (ia, ic, if_, ig), (id_,))
rep(34, 44, 10, 53, (ia, ic, ie), (id_,))
rep(38, 44, 20, 43, (ig, if_), (id_,))

# --- jet from the top finial ---
c.rect(30, 0, 5, 6, water)
c.rect(31, 1, 3, 4, wlight)
c.set(31, 0, white); c.set(32, 0, wlight); c.set(33, 1, white)
c.set(32, 2, white)
for (x, y) in [(28, 1), (36, 1), (27, 3), (37, 3), (29, 4), (35, 4)]:
    c.set(x, y, water)
for (x, y) in [(29, 2), (35, 2), (30, 3), (34, 3)]:
    c.set(x, y, wlight)
for (x, y) in [(28, 0), (36, 0), (29, 1), (35, 1)]:
    c.set(x, y, white)

# --- upper bowl surface shimmer & overflow ---
for (x, y) in [(23, 20), (31, 20), (40, 20), (25, 22), (33, 22),
               (29, 24), (37, 24), (27, 27), (32, 27), (38, 28)]:
    c.set(x, y, white)
for (x, y) in [(21, 21), (35, 22), (42, 23), (24, 25), (31, 29)]:
    c.set(x, y, foam)
for (x, y) in [(17, 29), (45, 29), (16, 31), (47, 31), (16, 33), (47, 33)]:
    c.set(x, y, water)
for (x, y) in [(17, 32), (46, 32), (15, 30), (48, 30)]:
    c.set(x, y, wlight)

# --- lower basin shimmer ---
for (x, y) in [(18, 36), (25, 36), (33, 36), (41, 36), (22, 38),
               (29, 38), (36, 38), (43, 39), (24, 41), (31, 41),
               (38, 42), (26, 43), (33, 43), (40, 44)]:
    c.set(x, y, white)
for (x, y) in [(19, 37), (28, 40), (35, 40), (43, 41)]:
    c.set(x, y, foam)

# --- cascades down the pedestal sides ---
c.rect(12, 45, 3, 14, water)
c.rect(49, 45, 3, 14, water)
c.rect(13, 46, 1, 12, wlight)
c.rect(50, 46, 1, 12, wlight)
for (x, y) in [(11, 47), (52, 47), (15, 50), (48, 50), (10, 52), (53, 52),
               (14, 54), (49, 54), (11, 56), (52, 56)]:
    c.set(x, y, wlight)
for (x, y) in [(12, 48), (51, 48), (13, 53), (50, 53), (12, 56), (51, 56)]:
    c.set(x, y, white)

# --- pool at the very base (submerges the bottom foot) ---
c.ellipse(31, 69, 23, 6, water, fill=True)     # rows 63-75
c.ellipse(31, 69, 18, 5, wlight, fill=False)
c.ellipse(31, 69, 12, 3, wlight, fill=False)
for (x, y) in [(19, 64), (27, 66), (36, 65), (44, 64), (23, 68),
               (33, 69), (40, 67), (29, 71), (35, 70), (20, 66),
               (26, 63), (38, 63), (25, 70), (36, 68), (22, 64),
               (30, 73), (33, 72)]:
    c.set(x, y, white)
# splashes where the cascades hit the pool
for (x, y) in [(12, 62), (15, 62), (49, 62), (52, 62), (13, 63), (51, 63),
               (11, 64), (53, 64), (14, 63), (50, 63)]:
    c.set(x, y, white)
for (x, y) in [(14, 64), (50, 64)]:
    c.set(x, y, foam)

print(c.stats_text())
finish(c)
