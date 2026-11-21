from pixelbench_api import new_canvas, finish

# ---------- warm palette ----------
tmp = new_canvas(1, 1)
BG_A   = tmp.color((122, 30, 42))
BG_B   = tmp.color((104, 26, 38))
BG_C   = tmp.color((141, 37, 51))
FRAME  = tmp.color((49, 13, 21))
GOLD   = tmp.color((222, 168, 66))
GOLD_D = tmp.color((178, 126, 44))
CREAM  = tmp.color((244, 228, 186))
ROSE   = tmp.color((199, 88, 58))
LEAF   = tmp.color((86, 118, 56))
CGOLD  = tmp.color((238, 198, 94))

W = 32
P = new_canvas(96, 96, name="plane")
OFF = (-64, -32, 0, 32, 64)

# ---------- 1. periodic woven background ----------
for y in range(96):
    for x in range(96):
        P.set(x, y, BG_A if (x + y) % 2 == 0 else BG_B)
for y in range(96):
    for x in range(96):
        if (x % 8 == 0 or y % 8 == 0) and (x + y) % 2 == 0:
            P.set(x, y, BG_C)

# ---------- 2. periodic frame band ----------
for y in range(96):
    for x in range(96):
        if x % 32 in (0, 1, 2, 29, 30, 31) or y % 32 in (0, 1, 2, 29, 30, 31):
            P.set(x, y, FRAME)

# ---------- motif points (tile-local) ----------
FRAME_ROS = [(1, 1), (16, 1), (31, 1), (1, 16), (31, 16),
            (1, 31), (16, 31), (31, 31)]
TIP_ROS   = [(16, 5), (26, 16), (16, 27), (6, 16)]
INNER_LEAF = [(16, 9), (22, 16), (16, 23), (10, 16)]
FLOWER    = [(0, 0), (2, 0), (0, 2), (2, 2), (0, -2), (2, -2), (-2, 0), (-2, 2), (-2, -2)]

petal_ops   = []   # rose petals / flower petals
center_ops = []   # gold centers

for ox in OFF:
    for oy in OFF:
        for rx, ry in FRAME_ROS:
            cx, cy = rx + 32 + ox, ry + 32 + oy
            for dx in (-2, 0, 2):
                for dy in (-2, 0, 2):
                    if dx or dy:
                        petal_ops.append(((cx + dx, cy + dy), ROSE))
                    else:
                        center_ops.append(((cx, cy), CGOLD))
        for tx, ty in TIP_ROS:
            cx, cy = tx + 32 + ox, ty + 32 + oy
            for dx in (-2, 0, 2):
                for dy in (-2, 0, 2):
                    if dx or dy:
                        petal_ops.append(((cx + dx, cy + dy), ROSE))
                    else:
                        center_ops.append(((cx, cy), CGOLD))
        for dx in (-2, 0, 2):
            for dy in (-2, 0, 2):
                if dx or dy:
                    petal_ops.append(((48 + dx + ox, 48 + dy + oy), LEAF if (dx and dy) else ROSE))
# flower heart per tile
        center_ops.append(((48 + ox, 48 + oy), CGOLD))

# ---------- 3. gold rings + diamonds + leaves per tile first ----------
for ox in OFF:
    for oy in OFF:
        # double gold rings around the medallion
        P.rect(33 + ox, 33 + oy, 30, 30, GOLD, fill=False)
        P.rect(34 + ox, 34 + oy, 28, 28, GOLD_D, fill=False)
        for yy in (33 + oy, 62 + oy):
            for xx in range(32 + ox, 64 + ox):
                if xx % 4 in (0, 3):
                    P.set(xx, yy, GOLD_D)
        for xx in (33 + ox, 62 + ox):
            for yy in range(32 + oy, 64 + oy):
                if yy % 4 in (0, 3):
                    P.set(xx, yy, GOLD_D)
        # diamond medallion
        P.poly([(48 + ox, 37 + oy), (58 + ox, 48 + oy), (48 + ox, 59 + oy), (38 + ox, 48 + oy)], GOLD)
        P.poly([(48 + ox, 37 + oy), (58 + ox, 48 + oy), (48 + ox, 59 + oy), (38 + ox, 48 + oy)], FRAME, fill=False)
        P.poly([(48 + ox, 41 + oy), (54 + ox, 48 + oy), (48 + ox, 55 + oy), (42 + ox, 48 + oy)], CREAM)
        P.poly([(48 + ox, 41 + oy), (54 + ox, 48 + oy), (48 + ox, 55 + oy), (42 + ox, 48 + oy)], GOLD_D, fill=False)
        # leaves at inner diamond tips
        for lx, ly in INNER_LEAF:
            P.set(lx + 32 + ox, ly + 32 + oy, LEAF)

# ---------- 4. rosette / flower pixels in fixed priority phases ----------
for (px, py), col in petal_ops:
    P.set(px, py, col)
for (px, py), col in center_ops:
    P.set(px, py, col)

# ---------- verify strict plane periodicity ----------
bad = 0
for y in range(96):
    for x in range(64):
        if P.get(x + 32, y) != P.get(x, y):
            bad += 1
print("periodic mismatches:", bad)

# ---------- extract the 32x32 tile ----------
result = new_canvas(32, 32, name="carpet")
for y in range(W):
    for x in range(W):
        result.set(x, y, P.get(x + 32, y + 32))

print(result.stats_text())
finish(result)
