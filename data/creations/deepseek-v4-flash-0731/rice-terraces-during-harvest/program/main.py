from pixelbench_api import new_canvas, finish
import math, random

W = H = 64
c = new_canvas(W, H)

def col(spec):
    return c.color(spec)

# Terrace gradient: deep green (low, wet) -> blazing harvest gold (high)
terr_specs = ["#4E5B16", "#5F6E1D", "#718124", "#84942B", "#97A532", "#A9B239",
             "#B9BE40", "#C7C747", "#D4CD4D", "#E0D154", "#EAD45B", "#F2D662",
             "#F8D768", "#FCD76E", "#FFD774", "#FFD97C"]
terr = [col(s) for s in terr_specs]
forest = col("#3A4410")
ridge  = col("#2B2110")
lip    = col("#8A6A2E")
tex    = col("#9A7420")
water  = col("#FFE9A8")
shade  = col("#241A0C")

cx, cy = 4, 86
rx, ry = 31, 49

def elev(x, y):
    e = math.sqrt(((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2)
    e += 0.032 * math.sin((x + y) * 0.30) + 0.028 * math.cos((x - y) * 0.24)
    return e

def raw_fid(x, y):
    n = int(elev(x, y) * 7.0)
    return min(n, 16)

# mode-smoothing pass on the elevation field -> clean terrace bands
grid = [[raw_fid(x, y) for x in range(W)] for y in range(H)]

def sm(x, y):
    counts = {}
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H:
                v = grid[ny][nx]
                counts[v] = counts.get(v, 0) + 1
    bc = max(counts.values())
    cur = grid[y][x]
    if counts.get(cur, 0) == bc:
        return cur
    out = cur
    for v, n in counts.items():
        if n == bc:
            out = v
            break
    return out

fid = [[sm(x, y) for x in range(W)] for y in range(H)]

def is_ridge(x, y):
    n = fid[y][x]
    if x > 0 and fid[y][x - 1] != n: return True
    if x < W - 1 and fid[y][x + 1] != n: return True
    if y > 0 and fid[y - 1][x] != n: return True
    if y < H - 1 and fid[y + 1][x] != n: return True
    return False

def fieldval(x, y):
    n = fid[y][x]
    return forest if n >= 15 else terr[n]

# 1) terrace bodies + dike ridges
for y in range(H):
    for x in range(W):
        c.set(x, y, ridge if is_ridge(x, y) else fieldval(x, y))

# 2) sunlit downhill lip of each terrace step -> layered depth
for y in range(1, H):
    for x in range(W):
        if not is_ridge(x, y) and is_ridge(x, y - 1):
            c.set(x, y, lip)

# 3) elevation-aware harvest texture: water glints low, stubble high
rng = random.Random(11)
for y in range(H):
    for x in range(W):
        if is_ridge(x, y):
            continue
        n = fid[y][x]
        r = rng.random()
        if r < 0.018 * (0.3 + n / 16.0):
            c.set(x, y, tex)
        elif r < 0.018 * (0.3 + n / 16.0) + 0.022 * (1.0 - n / 16.0):
            c.set(x, y, water)

# 4) winding village path wandering down from the settlement
pathcol = col("#D4B878")
for (px, py) in [(37, 15), (36, 16), (35, 17), (34, 18), (33, 19), (32, 20), (31, 22), (30, 24), (29, 26)]:
    c.set(px, py, pathcol)

# 5) distant trees on the upper slopes
def tree(tx, ty):
    c.rect(tx + 1, ty + 1, 2, 2, shade)
    c.circle(tx, ty, 1, col("#2E3A0C"))
tree(51, 5)
tree(56, 10)
tree(47, 13)
tree(59, 3)

# 6) simple village houses in the distance
def house(hx, hy, roof, hi):
    c.rect(hx + 1, hy + 1, 3, 3, shade)
    c.rect(hx, hy, 3, 3, roof)
    c.rect(hx, hy, 3, 1, hi)
house(34, 7, col("#6E5540"), col("#8A6E46"))
house(39, 11, col("#7A5A3E"), col("#96744E"))
house(30, 12, col("#664C36"), col("#7E6644"))

# 7) anchor each farmer on a horizontal ridge run
def find_ridge(tx, ty, radius=7):
    best = None
    for dy in range(-radius, radius + 1):
        for dx in range(-radius, radius + 1):
            x, y = tx + dx, ty + dy
            if 0 <= x < W and 0 <= y < H and is_ridge(x, y):
                horiz = (x > 0 and is_ridge(x - 1, y)) or (x < W - 1 and is_ridge(x + 1, y))
                if not horiz:
                    continue
                score = 100 - abs(dy) * 5 - abs(dx) // 2
                if best is None or score > best[0]:
                    best = (score, x, y)
    return best

def farmer(rx, ry, shirt):
    fx, fy = rx, ry - 3
    c.rect(fx, fy + 2, 4, 3, shade)              # ground shadow on the dike
    c.rect(fx - 1, fy + 2, 3, 2, col("#4A2E14"))  # legs
    c.rect(fx - 1, fy, 3, 3, shirt)              # body
    c.circle(fx, fy, 2, col("#C28F3B"))            # straw hat brim
    c.circle(fx, fy, 1, col("#F3CE78"))            # hat crown

f1 = find_ridge(44, 38)
f2 = find_ridge(52, 47)
if f1:
    farmer(f1[1], f1[2], col("#8C4A2A"))
if f2:
    farmer(f2[1], f2[2], col("#5E6E4A"))

print("farmer anchors:", f1, f2)
print(c.stats_text())
finish(c)
