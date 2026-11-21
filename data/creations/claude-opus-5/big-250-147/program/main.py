"""Sunset -> clear noon. Sky is rebuilt (no sun, no clouds); terrain keeps its
silhouette and tonal structure but is relit for an overhead sun."""

W, H = 250, 147
pal = {e['index']: e['rgba'] for e in input_canvas.palette()}
grid = [[input_canvas.get(x, y) for x in range(W)] for y in range(H)]


def lum(i):
    r, g, b = pal[i][:3]
    return 0.299 * r + 0.587 * g + 0.114 * b


def is_terrain(i):
    """Validated against the input: gives a clean, monotone skyline."""
    r, g, b = pal[i][:3]
    L = lum(i)
    return L < 80 or (r - g >= 70 and b - g <= 14 and L < 190)


# --- per-column ridge line -------------------------------------------------
top = []
for x in range(W):
    t = H
    for y in range(H):
        if is_terrain(grid[y][x]):
            t = y
            break
    top.append(t)
horizon = max(top)

# --- palettes --------------------------------------------------------------
SKY = ["#2f6ec4", "#3779cc", "#4083d2", "#498dd8", "#5397dd", "#5ea1e2", "#69abe6",
       "#75b5ea", "#82bfee", "#90c9f1", "#9fd2f4", "#aedbf7", "#bee4f9", "#cdecfb"]
ROCK = ["#3f4e4a", "#4c5c52", "#5d6e61", "#708172", "#879684"]
LIT = ["#8e9a84", "#a2ac93", "#b6bda4"]
TREE = ["#18260f", "#213216", "#2a3f1b", "#344d21", "#3f5c28", "#4b6d2f", "#5a7e38"]

BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def classify(i):
    r, g, b = pal[i][:3]
    L = lum(i)
    if r - g >= 70 and b - g <= 14 and L >= 100:
        return "lit", L
    if b - g >= 25 and L > 95:          # stray sky tones inside the ridge
        return "lit", 100.0
    if b - g >= 12:
        return "rock", L
    return "tree", L


def rock_idx(L):
    for n, t in enumerate((34, 40, 48, 58)):
        if L < t:
            return n
    return 4


def lit_idx(L):
    return 0 if L < 125 else (1 if L < 140 else 2)


def tree_idx(L):
    for n, t in enumerate((13, 17, 22, 28, 38, 50)):
        if L < t:
            return n
    return 6


def hx(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    ca, cb = hx(a), hx(b)
    return "#%02x%02x%02x" % tuple(
        int(round(ca[n] + (cb[n] - ca[n]) * t)) for n in range(3))


def sky_at(y):
    """Sky colour of row y, used as the haze target for depth."""
    p = min(1.0, max(0.0, y / float(horizon))) * (len(SKY) - 1)
    i0 = int(p)
    return mix(SKY[i0], SKY[min(len(SKY) - 1, i0 + 1)], p - i0)


HAZE = {}


def hazed(col, y):
    """Distant (high) ridges sit further back, so they wash toward the sky."""
    t = 0.30 * max(0.0, (horizon - y) / float(horizon))
    key = (col, y)
    if key not in HAZE:
        HAZE[key] = mix(col, sky_at(y), t)
    return HAZE[key]


out = input_canvas.copy(name="output")

# pass 1: classes, so lighting can look at neighbours
kind = [[None] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        kind[y][x] = "sky" if y < top[x] else classify(grid[y][x])[0]

for y in range(H):
    for x in range(W):
        k = kind[y][x]
        if k == "sky":
            # ordered-dithered vertical gradient, deep blue overhead to pale haze
            p = min(1.0, y / float(horizon)) * (len(SKY) - 1)
            i0 = int(p)
            frac = p - i0
            thr = (BAYER[y & 3][x & 3] + 0.5) / 16.0
            idx = min(len(SKY) - 1, i0 + (1 if frac > thr else 0))
            out.set(x, y, SKY[idx])
            continue

        _, L = classify(grid[y][x])
        above_other = y == 0 or kind[y - 1][x] != k
        if k == "tree":
            n = tree_idx(L)
            if above_other:                     # canopy tips catch the high sun
                n = min(len(TREE) - 1, n + 1)
            out.set(x, y, TREE[n])               # foreground: no haze
        elif k == "lit":
            n = lit_idx(L)
            if above_other:
                n = min(len(LIT) - 1, n + 1)
            out.set(x, y, hazed(LIT[n], y))
        else:
            n = rock_idx(L)
            if above_other:                     # sunlit crest
                n = min(len(ROCK) - 1, n + 1)
            out.set(x, y, hazed(ROCK[n], y))

print(out.stats_text())
view(out)
save("noon", out)
finish(out)
