import math
import random

W = H = 16

# replicate the exact generator used in main.py for a seamlessness check
def smooth(t):
    return t * t * (3.0 - 2.0 * t)


def norm2d(m):
    lo = min(min(r) for r in m)
    hi = max(max(r) for r in m)
    d = (hi - lo) or 1.0
    return [[(v - lo) / d for v in r] for r in m]


def toroidal_noise(seed, cx, cy):
    rng = random.Random(seed)
    lat = [[rng.random() for _ in range(cx)] for _ in range(cy)]
    out = [[0.0] * W for _ in range(H)]
    sx, sy = cx / float(W), cy / float(H)
    for y in range(H):
        fy = y * sy
        y0 = int(math.floor(fy)) % cy
        y1 = (y0 + 1) % cy
        ty = smooth(fy - math.floor(fy))
        for x in range(W):
            fx = x * sx
            x0 = int(math.floor(fx)) % cx
            x1 = (x0 + 1) % cx
            tx = smooth(fx - math.floor(fx))
            a = lat[y0][x0] * (1 - tx) + lat[y0][x1] * tx
            b = lat[y1][x0] * (1 - tx) + lat[y1][x1] * tx
            out[y][x] = a * (1 - ty) + b * ty
    return norm2d(out)


SEED = 88
clod = toroidal_noise(SEED, 4, 4)
blotch = toroidal_noise(SEED + 77, 5, 7)
lump = toroidal_noise(SEED + 131, 6, 6)
grit = toroidal_noise(SEED + 211, 9, 9)
raw = [[0.24 * clod[y][x] + 0.32 * blotch[y][x] + 0.28 * lump[y][x]
        + 0.16 * grit[y][x] for x in range(W)] for y in range(H)]
tone = norm2d(raw)
# check wrap: tone at x=0 vs interior statistics, and gradient across the seam
diff_seam_x = sum(abs(tone[y][0] - tone[y][W - 1]) for y in range(H)) / H
diff_avg_x = sum(abs(tone[y][x] - tone[y][(x + 1) % W])
                 for y in range(H) for x in range(W)) / 256
diff_seam_y = sum(abs(tone[0][x] - tone[H - 1][x]) for x in range(W)) / W
diff_avg_y = sum(abs(tone[y][x] - tone[(y + 1) % H][x])
                 for y in range(H) for x in range(W)) / 256
print("seam-x %.4f  avg-x %.4f" % (diff_seam_x, diff_avg_x))
print("seam-y %.4f  avg-y %.4f" % (diff_seam_y, diff_avg_y))
