from collections import deque

W = H = 32

# ---------------------------------------------------------------- silhouette
SIL = [(11, 2), (20, 2), (22, 4), (27, 6), (29, 10), (28, 16), (24, 17),
       (24, 29), (20, 30), (11, 30), (7, 29), (7, 17), (3, 16), (2, 10),
       (4, 6), (9, 4)]

mask = new_canvas(W, H, name="mask")
mask.poly(SIL, "#ffffff")
_, _, rgba = mask.to_rgba()
inside = [[rgba[(y * W + x) * 4 + 3] > 0 for x in range(W)] for y in range(H)]

print("silhouette mask")
for y in range(0, H, 4):
    print("%2d %s" % (y, "".join("#" if inside[y][x] else "." for x in range(W))))

# ------------------------------------------------------- distance to outside
INF = 99
dist = [[INF] * W for _ in range(H)]
q = deque()
for y in range(H):
    for x in range(W):
        if not inside[y][x]:
            dist[y][x] = 0
            q.append((x, y))
while q:
    x, y = q.popleft()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H and dist[ny][nx] > dist[y][x] + 1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((nx, ny))

print("distance field (every 4th row)")
for y in range(0, H, 4):
    print("%2d %s" % (y, "".join(str(min(dist[y][x], 9)) if inside[y][x] else "."
                                 for x in range(W))))

# ------------------------------------------------------------------- palette
OUT = "#101320"          # dark outline / gaps between rings
RAMPS = {
    2: dict(L="#e6ebf9", l="#b4bed9", M="#828cab", h="#2a3044"),
    1: dict(L="#b6c0da", l="#8b95b4", M="#646d8c", h="#20263a"),
    0: dict(L="#8b94b0", l="#6a7390", M="#4d5570", h="#232838"),
}
SPEC = "#f6f9ff"

TILE = [
    ".LL.",
    "LhhM",
    "lhhM",
    ".MM.",
]

# ------------------------------------------------------------------- canvas
c = new_canvas(W, H, name="chainmail")
c.poly(SIL, OUT)


def ring_depth(cx, cy):
    best = -1
    for ty in range(4):
        for tx in range(4):
            x, y = cx + tx, cy + ty
            if 0 <= x < W and 0 <= y < H and inside[y][x]:
                best = max(best, dist[y][x])
    return best


def level_of(d, cx, cy):
    if d < 1:
        return None
    if d <= 2:
        return 0
    v = d + (14.0 - (cx + 1.5)) * 0.26 + (12.0 - (cy + 1.5)) * 0.12
    if v >= 4.7:
        lv = 2
    elif v >= 3.1:
        lv = 1
    else:
        lv = 0
    if 8 <= cy <= 10:            # shadow cast by the collar
        lv = min(lv, 1)
    return lv


rows = list(range(-4, H + 1, 3))
rows.reverse()                      # draw bottom rows first -> upper overlap
for i, cy in enumerate(rows):
    off = 2 if (i % 2 == 0) else 0
    for cx in range(-4 + off, W + 2, 4):
        d = ring_depth(cx, cy)
        lv = level_of(d, cx, cy)
        if lv is None:
            continue
        ramp = RAMPS[lv]
        j = ((cx * 7 + cy * 13) // 4) % 5
        if not (8 <= cy <= 10):
            if j == 1 and lv < 2:
                ramp = RAMPS[lv + 1]      # sparkle: ring catches the light
            elif j == 4 and lv > 0:
                ramp = RAMPS[lv - 1]      # sparkle: ring turned away
        for ty in range(4):
            for tx in range(4):
                ch = TILE[ty][tx]
                if ch == ".":
                    continue
                x, y = cx + tx, cy + ty
                if 0 <= x < W and 0 <= y < H and inside[y][x]:
                    c.set(x, y, ramp[ch])

# specular glints on a few bright rings
for i, cy in enumerate(rows):
    off = 2 if (i % 2 == 0) else 0
    for cx in range(-4 + off, W + 2, 4):
        if ring_depth(cx, cy) >= 5 and level_of(ring_depth(cx, cy), cx, cy) == 2 \
                and (cx + 2 * cy) % 8 == 0:
            x, y = cx + 1, cy + 1
            if 0 <= x < W and 0 <= y < H and inside[y][x] and dist[y][x] >= 3:
                c.set(x, y, SPEC)

# ------------------------------------------------------------------- details
# collar with a painted neck opening
for y in (2, 3):
    for x in range(W):
        if inside[y][x] and dist[y][x] >= 1:
            c.set(x, y, "#98a2c2")
for x in range(13, 19):
    c.set(x, 2, OUT)
    c.set(x, 3, "#2b3143")
for x in (12, 19):
    c.set(x, 3, "#5d6580")
for x in range(W):
    if inside[4][x] and dist[4][x] >= 1:
        c.set(x, 4, "#98a2c2")
for x in range(W):
    if inside[5][x] and dist[5][x] >= 1:
        c.set(x, 5, "#5d6580")
for x in range(W):
    if inside[6][x] and dist[6][x] >= 1:
        c.set(x, 6, "#454c64")
for x in range(W):
    if inside[7][x] and dist[7][x] >= 2:
        c.set(x, 7, OUT)

# hem band with a dark trim line
for y in (28, 29):
    for x in range(W):
        if inside[y][x] and dist[y][x] >= 2:
            c.set(x, y, "#4d5570" if y == 28 else "#2b3143")
for x in range(W):
    if inside[27][x] and dist[27][x] >= 3:
        c.set(x, 27, OUT)

# sleeve cuffs
for x in range(W):
    for y in (15, 16):
        if inside[y][x] and dist[y][x] >= 1 and (x <= 6 or x >= 25):
            c.set(x, y, "#4d5570" if y == 15 else "#2b3143")
for x in range(W):
    if inside[14][x] and dist[14][x] >= 2 and (x <= 6 or x >= 25):
        c.set(x, 14, OUT)

c.outline(OUT)

print(c.stats_text())
print(view(c, scale=16, margin=0))
print(view(c, scale=8, margin=0))
save("chainmail_armor", c)
finish(c)
