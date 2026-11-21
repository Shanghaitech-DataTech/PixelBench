from pixelbench_api import new_canvas, view, save, finish

W = H = 16

# ---------------------------------------------------------------- palette ----
# Minecraft-ish dirt: warm browns from deep shadow to sunlit grain,
# plus two cool grey tones for tiny embedded pebbles.
PAL = [
    "#4A3524",  # 0 deepest shadow
    "#57402B",  # 1
    "#634A31",  # 2
    "#71553A",  # 3
    "#7E6042",  # 4 base mid
    "#8B6C4A",  # 5
    "#987A55",  # 6
    "#A68A62",  # 7 highlight grain
    "#3F2D1F",  # 8 deep pit grain
    "#B49468",  # 9 sunlit grain
]

c = new_canvas(W, H, name="dirt")


# ------------------------------------------------------------------ noise ----
def hash2(x, y, seed):
    """Deterministic 0..1 hash, integer lattice -> seamless on any multiple."""
    n = (x * 374761393 + y * 668265263 + seed * 2246822519) & 0xFFFFFFFF
    n = ((n ^ (n >> 13)) * 1274126177) & 0xFFFFFFFF
    n = (n ^ (n >> 16)) & 0xFFFFFFFF
    return n / 4294967295.0


def coarse(x, y, cell, seed):
    """Block noise at `cell` px resolution; 16 % cell == 0 keeps it tileable."""
    return hash2((x // cell) % (W // cell), (y // cell) % (H // cell), seed)


def fine(x, y, seed):
    return hash2(x % W, y % H, seed)


# ------------------------------------------------------------- tone field ----
# weighted per-pixel grain: mostly mid browns, sprinkled darks and lights
BINS = [(0.05, 0), (0.15, 1), (0.33, 2), (0.57, 3),
        (0.79, 4), (0.90, 5), (0.97, 6), (1.01, 7)]


def base_tone(u):
    for thr, t in BINS:
        if u < thr:
            return t
    return 7


tones = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        t = base_tone(fine(x, y, 71))
        # soft 4px patches nudge whole clumps one step lighter/darker
        patch = (coarse(x, y, 4, 29) - 0.5) * 2.0
        t += 1 if patch > 0.45 else (-1 if patch < -0.45 else 0)
        # rare hard speckles: deep pits and sunlit grains
        s = fine(x, y, 99)
        if s < 0.045:
            t = 0
        elif s > 0.965:
            t = 7
        tones[y][x] = max(0, min(7, t))

# ------------------------------------------------------- pebble inclusions ---
# a handful of small cool-grey grit specks, deterministic positions
PEBBLES = [(2, 3), (3, 3), (11, 6), (12, 6), (6, 11), (7, 11), (14, 13), (0, 9)]
for i, (px, py) in enumerate(PEBBLES):
    tones[py % H][px % W] = 9 if i % 2 == 0 else 8

# ------------------------------------------------------- darken grain edges --
# give a few pixels an extra-deep shadow so the texture reads as granular
DEEP = [(5, 1), (13, 2), (1, 7), (9, 9), (15, 10), (4, 14), (10, 15), (7, 5)]
for (px, py) in DEEP:
    tones[py % H][px % W] = 0

# ------------------------------------------------------------------ paint ----
for y in range(H):
    for x in range(W):
        c.set(x, y, PAL[tones[y][x]])

print(c.stats_text())
print(c.matrix_text(indices=True))
view(c, scale=16, margin=0)

# seam check: 2x2 tiling must show no visible grid lines
tiled = new_canvas(32, 32, name="tiled")
for ty in (0, 16):
    for tx in (0, 16):
        tiled.blit(c, tx, ty)
view(tiled, scale=10, margin=0)

save("dirt", c)
finish(c)
