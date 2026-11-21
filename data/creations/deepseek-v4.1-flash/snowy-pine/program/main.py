import math

result = input_canvas.copy(name="output")
W, H = 82, 135
FOL = {1, 2, 3, 4}
SNOW, SHADE = 9, 8
LUM = {1: 1.00, 2: 0.28, 3: 0.66, 4: 0.80}

orig = [[result.get(x, y) for x in range(W)] for y in range(H)]
tree = [[orig[y][x] in FOL for x in range(W)] for y in range(H)]


def hsh(a, b, s=0):
    v = (a * 374761393 + b * 668265263 + s * 1442695041) & 0xFFFFFFFF
    v = ((v ^ (v >> 13)) * 1274126177) & 0xFFFFFFFF
    return ((v ^ (v >> 16)) & 0xFFFF) / 65535.0


def wav(x, ph):
    return (0.50 * math.sin(x * 0.38 + ph)
            + 0.30 * math.sin(x * 0.91 - ph * 0.5 + 1.3)
            + 0.20 * math.sin(x * 1.77 + 2.1))


# --- blurred brightness of the canopy (bright = exposed branch tops/gaps) ---
lbl = [[0.0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if not tree[y][x]:
            continue
        s = 0.0
        n = 0
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                xx = x + dx
                yy = y + dy
                if 0 <= xx < W and 0 <= yy < H and tree[yy][xx]:
                    s += LUM[orig[yy][xx]]
                    n += 1
        lbl[y][x] = s / n if n else 0.0

kind = [[0] * W for _ in range(H)]   # 0 = bare needles, 1 = shaded snow, 2 = snow

# --- snow rims along the top of every branch layer ---
for x in range(W):
    y = 0
    while y < H:
        if not tree[y][x]:
            y += 1
            continue
        y0 = y
        while y < H and tree[y][x]:
            y += 1
        h = y - y0
        g = 0
        yy = y0 - 1
        while yy >= 0 and not tree[yy][x] and g < 8:
            g += 1
            yy -= 1
        ph = y0 * 0.13 + hsh(0, y0, 5) * 2.5
        base = 9.5 * (0.75 + 0.50 * wav(x, ph))
        if y0 < 45:
            base += 3.0
        if g <= 1:
            base *= 0.50
        d = int(round(base))
        if d > h:
            d = h
        if d > 18:
            d = 18
        if d < 1:
            d = 1
        for r in range(d):
            kind[y0 + r][x] = 2
        # slightly irregular bottom edge of the snow band
        if d >= 2:
            v = (0.5 + 0.45 * math.sin(x * 1.30 + y0 * 0.85)
                 + 0.35 * (hsh(x, y0, 1) - 0.5))
            if v > 1.00:
                kind[y0 + d - 1][x] = 1
        # soft shadow / melt line just below the snow
        for k, thr in ((d, 0.90), (d + 1, 0.42), (d + 2, 0.16)):
            yy2 = y0 + k
            if yy2 < H and tree[yy2][x]:
                v = (0.5 + 0.50 * math.sin(x * 0.90 + y0 * 0.70 + 0.60)
                     + 0.40 * (hsh(x, y0, 10 + k) - 0.5))
                if v < thr:
                    kind[yy2][x] = 1
        # piled-up snow that spills a little above the silhouette
        if g >= 1 and d >= 5 and hsh(x, y0, 3) < 0.45 and y0 - 1 >= 0:
            kind[y0 - 1][x] = 2

# --- frosty speckle in the bright parts of the canopy ---
for y in range(H):
    for x in range(W):
        if not tree[y][x] or kind[y][x] != 0:
            continue
        p = (lbl[y][x] - 0.42) * 1.15
        if p > 0.0 and hsh(x, y, 7) < p:
            kind[y][x] = 1

n_snow = n_shade = n_bare = 0
for y in range(H):
    for x in range(W):
        k = kind[y][x]
        if tree[y][x]:
            if k == 2:
                result.set(x, y, SNOW)
                n_snow += 1
            elif k == 1:
                result.set(x, y, SHADE)
                n_shade += 1
            else:
                n_bare += 1
        elif k == 2:
            result.set(x, y, SNOW)
            n_snow += 1

print("snow", n_snow, "shade", n_shade, "bare", n_bare)
print(result.stats_text())

LEG = {0: '.', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 's', 9: 'W'}
for y in range(H):
    print("%3d|%s|" % (y, "".join(LEG[result.get(x, y)] for x in range(W))))

finish(result)
