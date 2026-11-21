W = H = 32
c = new_canvas(W, H, background=None, name="carpet")

BG   = c.color("#8a2b1d", "bg")
BGD  = c.color("#712013", "bg_dark")
GOLD = c.color("#d9a441", "gold")
CREAM= c.color("#f0e0bd", "cream")
DARK = c.color("#3d130c", "dark")
RED  = c.color("#b8402a", "red")

def wset(x, y, col):
    """Plot with wrap-around so the pattern tiles seamlessly."""
    c.set(x % W, y % H, col)

# woven background: two-tone warm checker
for y in range(H):
    for x in range(W):
        c.set(x, y, BG if (x + y) % 2 == 0 else BGD)

def diamond(cx, cy, r, col, fill=True):
    if fill:
        for dy in range(-r, r + 1):
            w = r - abs(dy)
            for dx in range(-w, w + 1):
                wset(cx + dx, cy + dy, col)
    else:
        for i in range(r + 1):
            wset(cx + i, cy + (r - i), col)
            wset(cx + i, cy - (r - i), col)
            wset(cx - i, cy + (r - i), col)
            wset(cx - i, cy - (r - i), col)

# corner medallions (drawn once at (0,0); wrap fills all four corners)
diamond(0, 0, 7, DARK)
diamond(0, 0, 6, GOLD)
diamond(0, 0, 3, CREAM)
diamond(0, 0, 1, RED)

# central medallion
diamond(16, 16, 9, DARK)
diamond(16, 16, 8, GOLD)
diamond(16, 16, 5, DARK)
diamond(16, 16, 4, CREAM)
diamond(16, 16, 2, RED)
wset(16, 16, GOLD)

# floral buds sitting on the tile edges (wrap keeps them seamless)
def flower(cx, cy):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx or dy:
                wset(cx + dx, cy + dy, DARK)
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        wset(cx + dx, cy + dy, CREAM)
    wset(cx, cy, GOLD)
    for dx, dy in ((0, -2), (0, 2), (-2, 0), (2, 0)):
        wset(cx + dx, cy + dy, GOLD)

for fx, fy in ((16, 0), (16, 32), (0, 16), (32, 16)):
    flower(fx, fy)

# small accent dots in the gaps between motifs
for ax, ay in ((9, 9), (23, 9), (9, 23), (23, 23),
               (11, 0), (21, 0), (11, 32), (21, 32),
               (0, 11), (0, 21), (32, 11), (32, 21)):
    wset(ax, ay, GOLD)

# --- seam verification: tiling must be continuous across all four edges ---
rgba = c.to_rgba()
px = rgba[2]
def at(x, y):
    i = (y % H) * W + (x % W)
    return px[i*4:i*4+4]
ok = True
for y in range(H):
    if at(0, y) != at(32, y) or at(-1, y) != at(31, y):
        ok = False; print("h-seam mismatch at y", y)
for x in range(W):
    if at(x, 0) != at(x, 32) or at(x, -1) != at(x, 31):
        ok = False; print("v-seam mismatch at x", x)
print("seams OK" if ok else "SEAM BROKEN")

print(c.stats_text())
save("carpet", c)
finish(c)
