"""Seamless 32x32 carpet tile: warm diamond medallion ringed by a floral border.

Every colour decision is a function of torus coordinates (distance to the tile
centre, distance to the nearest corner, wrapped distances to the edge
midpoints), so the left/right and top/bottom edges join exactly by construction.
"""
from math import hypot, cos, sin, pi

N = 32

# ---------------- palette (warm carpet tones) ----------------
INK    = "#24100a"      # near-black walnut, outlines & hearts
DARK   = "#5e1b12"      # deep brick
WINE   = "#7f2416"      # brick
RUST   = "#932e1b"      # mid brick
TERRA  = "#a83a22"      # field, weave dark
TERRA2 = "#b0402a"      # field, weave light
OCHRE  = "#c07a2b"      # ochre
GOLD   = "#e3ad48"      # gold
CREAM  = "#faeed6"      # cream


def wrapd(v, size=N):
    """signed shortest distance on the torus"""
    v %= size
    if v > size // 2:
        v -= size
    return v


def petal_dist(sx, sy, n, rad, phase=pi):
    """distance to the nearest petal centre, plus that petal's index"""
    best = 1e9
    bi = 0
    for k in range(n):
        a = 2 * pi * k / n + phase / n
        d = hypot(sx - rad * cos(a), sy - rad * sin(a))
        if d < best:
            best, bi = d, k
    return best, bi


def colour(x, y):
    ax = abs(x - 16)
    ay = abs(y - 16)
    m = ax + ay                      # diamond metric around the tile centre
    sx = x if x < 16 else x - 32     # signed offset from the nearest corner
    sy = y if y < 16 else y - 32
    r = hypot(sx, sy)                # distance from that corner
    wv = (x + y) & 1                 # fine weave checker (period 2, so seamless)

    # ---------------- 1. central diamond medallion ----------------
    if m <= 12:
        if m == 12:
            return INK                        # outline
        if m == 11:
            return GOLD                       # bright piping
        if m >= 9:
            return RUST if wv else DARK       # woven dark band
        if m >= 7:
            return GOLD if wv else OCHRE       # woven gold band
        if m >= 5:
            return CREAM
        if m <= 2:
            return INK if m == 0 else CREAM   # cream heart, ink centre
        if m == 3 and (ax == 0 or ay == 0):
            return GOLD                       # gold tips round the heart
        return WINE

    # ---------------- 2. corner rosettes (join across the seams) ----------------
    if r <= 6.8:
        if r > 5.8:
            return INK                          # outline ring
        dpet, k = petal_dist(sx, sy, 8, 4.1)
        if r <= 0.95:
            return INK
        if r <= 2.2:
            return CREAM
        if dpet <= 1.3:
            return GOLD if (k & 1) == 0 else OCHRE
        return WINE

    # ---------------- 3. small diamonds on the four edge midpoints ----------------
    dm = min(abs(wrapd(x - 16)) + abs(wrapd(y)),
             abs(wrapd(x)) + abs(wrapd(y - 16)))
    if dm <= 2:
        if dm == 0:
            return INK
        if dm == 1:
            return CREAM
        return GOLD

    # ---------------- 4. four-petal blossoms on the diagonals ----------------
    u = min(abs(x - 7), abs(x - 25))
    v = min(abs(y - 7), abs(y - 25))
    d = hypot(u, v)
    if d <= 2.35:
        if d <= 0.5:
            return INK
        if min(hypot(u - 1.45, v), hypot(u, v - 1.45)) <= 0.9:
            return CREAM
        return OCHRE

    # ---------------- woven field ----------------
    return TERRA2 if wv else TERRA


out = new_canvas(N, N, name="result")
for y in range(N):
    for x in range(N):
        out.set(x, y, colour(x, y))

print(out.stats_text())
print(out.matrix_text())
save("seamless_carpet", out)
finish(out)
