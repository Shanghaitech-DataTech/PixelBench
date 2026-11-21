c = new_canvas(32, 32, background=None, name="chainmail-armor")

# ---- colours ---------------------------------------------------------------
OUTLINE   = c.color("#0c0e12", name="outline")
BASE_TOP  = c.color("#3b434f", name="base_top")
BASE_MID  = c.color("#313845", name="base_mid")
BASE_LOW  = c.color("#272d37", name="base_low")

A_TOP = c.color("#c9d4df", name="ring_top_a")
B_TOP = c.color("#9aa7b7", name="ring_top_b")
A_MID = c.color("#97a3b3", name="ring_mid_a")
B_MID = c.color("#6d7a8a", name="ring_mid_b")
A_LOW = c.color("#596475", name="ring_low_a")
B_LOW = c.color("#424c5a", name="ring_low_b")

# ---- armour silhouette mask --------------------------------------------------
# symmetric about x=15.5: a row with left edge L fills [L, 31-L]
ROWS = {
    0: 12, 1: 10, 2: 8, 3: 7, 4: 6, 5: 6, 6: 7, 7: 7, 8: 7, 9: 7,
    10: 8, 11: 8, 12: 8, 13: 8, 14: 9, 15: 9, 16: 9, 17: 9,
    18: 10, 19: 10, 20: 10, 21: 11, 22: 11, 23: 11, 24: 12, 25: 12, 26: 12,
}

# V-shaped neck opening (transparent)
NECK = {1: (13, 18), 2: (14, 17), 3: (15, 16)}

mask = [[False] * 32 for _ in range(32)]
for y, L in ROWS.items():
    for x in range(L, 32 - L):
        mask[y][x] = True

for y, (nx0, nx1) in NECK.items():
    for x in range(nx0, nx1 + 1):
        mask[y][x] = False

def base_colour(y):
    if y <= 8:
        return BASE_TOP
    if y <= 17:
        return BASE_MID
    return BASE_LOW

def ring_pair(y):
    if y <= 7:
        return (A_TOP, B_TOP)
    if y <= 16:
        return (A_MID, B_MID)
    return (A_LOW, B_LOW)

for y in range(32):
    for x in range(32):
        if mask[y][x]:
            c.set(x, y, base_colour(y))

# ---- interlocking ring texture ---------------------------------------------
# radius-2 ring outline, drawn as the 12 perimeter pixels of a 5x5 ring
RING_OFFSETS = [
    (0, -2), (-2, -1), (-1, -1), (1, -1), (2, -1),
    (-2, 0), (2, 0),
    (-2, 1), (-1, 1), (1, 1), (2, 1),
    (0, 2),
]

for yi, yc in enumerate([1, 4, 7, 10, 13, 16, 19, 22, 25]):
    a_col, b_col = ring_pair(yc)
    x0 = 1 + (2 if yi % 2 else 0)
    for xi in range(8):
        xc = x0 + 4 * xi
        if xc < 0 or xc > 31:
            continue
        col = a_col if (yi + xi) % 2 == 0 else b_col
        for dx, dy in RING_OFFSETS:
            x, y = xc + dx, yc + dy
            if 0 <= x < 32 and 0 <= y < 32 and mask[y][x]:
                c.set(x, y, col)

# ---- dark outline -----------------------------------------------------------
c.outline(OUTLINE)

print(c.stats_text())
finish(c)
