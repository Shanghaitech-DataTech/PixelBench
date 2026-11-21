import random
from pixelbench_api import new_canvas, finish

W = H = 16


def make_dirt(seed=13):
    c = new_canvas(W, H, background=None)
    rng = random.Random(seed)

    # Toroidal value-noise lattice: 4x4 cells over the 16x16 tile.
    N = 4
    lat = [[rng.random() for _ in range(N)] for _ in range(N)]

    def smooth(t):
        return t * t * (3 - 2 * t)

    def lattice(x, y):
        fx = x / 4.0
        fy = y / 4.0
        i = int(fx) % N
        j = int(fy) % N
        tx = smooth(fx - i)
        ty = smooth(fy - j)
        a = lat[i][j] * (1 - tx) + lat[(i + 1) % N][j] * tx
        b = lat[i][(j + 1) % N] * (1 - tx) + lat[(i + 1) % N][(j + 1) % N] * tx
        return a * (1 - ty) + b * ty

    def fine(x, y):
        h = (x * 374761393 + y * 668265263 + seed * 9746343) & 0xFFFFFFFF
        h = ((h ^ (h >> 13)) * 1274126177) & 0xFFFFFFFF
        h ^= h >> 16
        return h / 0xFFFFFFFF

    # Dirt palette, darkest to lightest (7 colours).
    palette = [
        "#42270F",  # dark clumps
        "#533114",
        "#66401B",
        "#7B4F24",
        "#8F5E2D",
        "#A36E37",
        "#B87F42",  # sandy highlights
    ]

    for y in range(H):
        for x in range(W):
            v = lattice(x, y)
            f = fine(x, y)
            t = v * 0.72 + f * 0.28
            idx = min(6, int(t * 7))
            # fine speckles: isolated dark grit / light grains
            if f > 0.93 and v < 0.5:
                c.set(x, y, palette[0])
            elif f < 0.05 and v > 0.55:
                c.set(x, y, palette[6])
            else:
                c.set(x, y, palette[idx])
    return c


result = make_dirt()
print(result.stats_text())
finish(result)
