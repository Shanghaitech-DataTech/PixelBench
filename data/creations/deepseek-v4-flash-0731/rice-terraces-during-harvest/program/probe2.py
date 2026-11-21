from pixelbench_api import new_canvas, finish
import math, random

W = H = 64
c = new_canvas(W, H)

def col(spec):
    return c.color(spec)

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
    n = int(elev(x, y) * 5.2)
    return min(n, 16)

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

# whole-map contour print
chars = "0123456789ABCDEFGH"
for y in range(H):
    line = ""
    for x in range(W):
        if is_ridge(x, y):
            line += "#"
        else:
            n = fid[y][x]
            line += "F" if n >= 15 else chars[n]
    print(line)
