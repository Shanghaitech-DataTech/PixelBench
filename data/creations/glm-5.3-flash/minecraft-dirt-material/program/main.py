# Minecraft-style dirt block material, 16x16, seamless tile, <=10 colours.
# The texture field is generated with wrap-around (toroidal) blur, so the tile
# is seamless by construction: field(x+16,y) == field(x,y).

import math
import random

W = H = 16

# tone ladder, dark -> light (8 steps for fine apparent granularity)
PAL = [
    ("k", "#3A2716"),  # darkest shadow speck
    ("d", "#4E3520"),  # dark brown clump
    ("e", "#5A3D25"),  # dark-mid
    ("m", "#66452A"),  # mid dark
    ("M", "#7B5734"),  # mid base
    ("l", "#8F6940"),  # light brown
    ("L", "#A37D4F"),  # light tan
    ("h", "#BA9161"),  # highlight speck
]
NAMES = [p[0] for p in PAL]
NT = len(NAMES)

SEED_A = 7        # fine clump field
SEED_B = 11       # broad patch field
SEED_G = 23       # fine grain field (wrap-continuous, replaces pixel jitter)
PASSES_A = 3
PASSES_B = 4
PASSES_G = 0
W_A, W_B, W_G = 0.50, 0.30, 0.20
FRACS = (0.06, 0.24, 0.47, 0.70, 0.88, 0.965)


def blur_wrap(f, passes):
    for _ in range(passes):
        out = [[0.0] * W for _ in range(H)]
        for y in range(H):
            for x in range(W):
                s = 0.0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        w = 2.0 if (dx == 0 and dy == 0) else 1.0
                        s += w * f[(y + dy) % H][(x + dx) % W]
                out[y][x] = s / 10.0
        f = out
    return f


def norm(f):
    lo = min(min(r) for r in f)
    hi = max(max(r) for r in f)
    span = (hi - lo) or 1.0
    return [[(v - lo) / span for v in row] for row in f]


def field(seed, passes):
    rnd = random.Random(seed)
    return norm(blur_wrap([[rnd.random() for _ in range(W)] for _ in range(H)], passes))


def build(cfg):
    fa = field(cfg["sa"], cfg["pa"])
    fb = field(cfg["sb"], cfg["pb"])
    fg = field(cfg["sg"], cfg["pg"])
    f = [[cfg["wa"] * fa[y][x] + cfg["wb"] * fb[y][x] + cfg["wg"] * fg[y][x]
          for x in range(W)] for y in range(H)]
    if cfg["wp"]:
        # exactly periodic sinusoidal grain: integer wave numbers -> seamless
        for y in range(H):
            for x in range(W):
                p = (math.sin(2 * math.pi * (2 * x + 3 * y) / W + 0.7)
                     + 0.8 * math.sin(2 * math.pi * (5 * x - 2 * y) / W + 2.1))
                f[y][x] += cfg["wp"] * p
    f = norm(f)

    # rank-based quantisation: exact band populations, all tones used.
    # a whisper of white-noise jitter breaks plateaus into single-pixel speckle.
    flat = []
    for y in range(H):
        for x in range(W):
            flat.append((f[y][x] + cfg["jw"] * fg[y][x], y, x))
    flat.sort()
    n = len(flat)
    fr = cfg["fracs"]
    assert len(fr) == NT - 1, "need one threshold per tone boundary"
    bounds = [int(round(q * n)) for q in fr]
    grid = [[0] * W for _ in range(H)]
    for rank, (v, y, x) in enumerate(flat):
        t = 0
        for b in bounds:
            if rank >= b:
                t += 1
        grid[y][x] = t

    # scattered specks, keyed off the exactly-periodic jitter field so the
    # tile stays seamless: light "stone" grains and dark "shadow" grains,
    # selected by percentile so the counts are predictable.
    if cfg["speck"]:
        dark_frac, light_frac, jump = cfg["speck"]
        js = sorted(fg[y][x] for y in range(H) for x in range(W))
        n = len(js)
        lo_t = js[max(0, int(round(dark_frac * n)) - 1)]
        hi_t = js[min(n - 1, n - int(round(light_frac * n)))]
        for y in range(H):
            for x in range(W):
                j = fg[y][x]
                if j >= hi_t and 1 <= grid[y][x] <= NT - 1 - jump:
                    grid[y][x] += jump
                elif j <= lo_t and jump <= grid[y][x] <= NT - 1:
                    grid[y][x] -= jump
    return grid


def seam_metrics(grid):
    """Max and mean level step across each tile boundary vs interior."""
    def steps(pairs):
        d = [abs(a - b) for a, b in pairs]
        return max(d), sum(d) / len(d)
    hx = [(grid[y][W - 1], grid[y][0]) for y in range(H)]
    vx = [(grid[H - 1][x], grid[0][x]) for x in range(W)]
    inter = []
    for y in range(H):
        for x in range(W - 1):
            inter.append((grid[y][x], grid[y][x + 1]))
    for y in range(H - 1):
        for x in range(W):
            inter.append((grid[y][x], grid[y + 1][x]))
    return steps(hx), steps(vx), steps(inter)


def grid_text(grid):
    return "\n".join("".join(NAMES[v] for v in row) for row in grid)


CONFIGS = [
    dict(sa=7, pa=3, sb=11, pb=4, sg=23, pg=0, wa=0.50, wb=0.30, wg=0.20,
         wp=0.025, jw=0.10, speck=(0.006, 0.006, 2),
         fracs=(0.08, 0.28, 0.50, 0.72, 0.89, 0.965, 0.99)),
    dict(sa=3, pa=3, sb=19, pb=4, sg=23, pg=0, wa=0.50, wb=0.30, wg=0.20,
         wp=0.025, jw=0.10, speck=(0.006, 0.006, 2),
         fracs=(0.08, 0.28, 0.50, 0.72, 0.89, 0.965, 0.99)),
    dict(sa=7, pa=2, sb=11, pb=3, sg=23, pg=0, wa=0.50, wb=0.30, wg=0.20,
         wp=0.025, jw=0.10, speck=(0.006, 0.006, 2),
         fracs=(0.08, 0.28, 0.50, 0.72, 0.89, 0.965, 0.99)),
    dict(sa=7, pa=3, sb=11, pb=4, sg=23, pg=0, wa=0.40, wb=0.30, wg=0.30,
         wp=0.025, jw=0.10, speck=(0.006, 0.006, 2),
         fracs=(0.08, 0.28, 0.50, 0.72, 0.89, 0.965, 0.99)),
    dict(sa=7, pa=3, sb=11, pb=4, sg=23, pg=0, wa=0.50, wb=0.40, wg=0.10,
         wp=0.025, jw=0.10, speck=(0.006, 0.006, 2),
         fracs=(0.08, 0.28, 0.50, 0.72, 0.89, 0.965, 0.99)),
    dict(sa=7, pa=3, sb=11, pb=4, sg=23, pg=0, wa=0.50, wb=0.30, wg=0.20,
         wp=0.040, jw=0.10, speck=(0.006, 0.006, 2),
         fracs=(0.08, 0.28, 0.50, 0.72, 0.89, 0.965, 0.99)),
    dict(sa=7, pa=3, sb=11, pb=4, sg=23, pg=0, wa=0.50, wb=0.30, wg=0.20,
         wp=0.025, jw=0.10, speck=(0.006, 0.006, 2),
         fracs=(0.12, 0.34, 0.56, 0.76, 0.91, 0.97, 0.995)),
    dict(sa=7, pa=3, sb=11, pb=4, sg=23, pg=0, wa=0.50, wb=0.30, wg=0.20,
         wp=0.025, jw=0.10, speck=(0.006, 0.006, 2),
         fracs=(0.05, 0.22, 0.46, 0.70, 0.88, 0.96, 0.99)),
]


def largest_blob(g, tones):
    """Largest 4-connected wrap-aware region of any tone in `tones`."""
    seen = [[False] * W for _ in range(H)]
    best = 0
    for y in range(H):
        for x in range(W):
            if g[y][x] in tones and not seen[y][x]:
                stack = [(y, x)]
                seen[y][x] = True
                size = 0
                while stack:
                    cy, cx = stack.pop()
                    size += 1
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = (cy + dy) % H, (cx + dx) % W
                        if g[ny][nx] in tones and not seen[ny][nx]:
                            seen[ny][nx] = True
                            stack.append((ny, nx))
                best = max(best, size)
    return best


def granularity(g):
    """Fraction of neighbour pairs (wrap-aware) that differ."""
    tot = same = 0
    for y in range(H):
        for x in range(W):
            for dy, dx in ((0, 1), (1, 0)):
                tot += 1
                if g[(y + dy) % H][(x + dx) % W] == g[y][x]:
                    same += 1
    return 1.0 - same / tot


best = None
for ci, cfg in enumerate(CONFIGS):
    g = build(cfg)
    sh, sv, si = seam_metrics(g)
    score = max(sh[0], sv[0]) - si[0] + (sh[1] + sv[1]) / 2 - si[1]
    counts = [sum(1 for row in g for v in row if v == t) for t in range(NT)]
    print(f"cfg{ci} score={score:+.3f} H={sh} V={sv} interior={si} "
          f"gran={granularity(g):.3f} blobD={largest_blob(g, (0, 1))} "
          f"blobL={largest_blob(g, (5, 6, 7))} counts={counts}")
    if best is None or score < best[0]:
        best = (score, ci, g)

score, ci, grid = best
print("chosen cfg", ci)
print(grid_text(grid))

print("seam (max,mean): H", seam_metrics(grid)[0], "V", seam_metrics(grid)[1],
      "interior", seam_metrics(grid)[2])

# lighten the tone ladder toward Minecraft's mid-brown dirt read
LIGHT = ["#523A28", "#64492F", "#745737", "#856742",
         "#93744C", "#A28355", "#B29260", "#C1A06E"]
PAL = [(NAMES[i], LIGHT[i]) for i in range(NT)]

c = new_canvas(W, H, background=None, name="dirt")
idx = {}
for ch, hexv in PAL:
    idx[ch] = c.color(hexv, name="dirt_" + ch)
for y in range(H):
    for x in range(W):
        c.set(x, y, idx[NAMES[grid[y][x]]])

print(c.stats_text())
print("final seam check: H", seam_metrics(grid)[0], "V", seam_metrics(grid)[1],
      "interior", seam_metrics(grid)[2])
print(grid_text(grid))
finish(c)
