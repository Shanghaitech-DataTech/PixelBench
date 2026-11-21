# RPG grass material tile — 16x16, seamless, interleaved green speckles,
# tiny yellow flowers, small dark tufts, sparse dirt patches.
c = new_canvas(16, 16, name="grass")

A = c.color("#4a8a3a", "grass_base")
B = c.color("#6cb055", "grass_light")
C = c.color("#35682b", "grass_dark")
D = c.color("#234a1f", "grass_tuft")
E = c.color("#9a7248", "dirt")
F = c.color("#755432", "dirt_dark")
G = c.color("#f5d54a", "flower_petal")
H = c.color("#c98f1e", "flower_heart")

grid = [[A] * 16 for _ in range(16)]


def put(pts, col):
    for x, y in pts:
        grid[y % 16][x % 16] = col


# --- light green speckles / short blades -------------------------------
put([
    (2, 0), (3, 0),
    (6, 1),
    (12, 1),
    (9, 2), (13, 2),
    (14, 3),
    (4, 4),
    (0, 5), (15, 5),   # streak crossing the horizontal seam
    (6, 5),
    (9, 6),
    (12, 7),
    (3, 8),
    (7, 8),
    (14, 9),
    (10, 10),
    (6, 11),
    (1, 12), (9, 12),
    (13, 13),
    (8, 14),
    (4, 15),
    (15, 15),
], B)

# --- dark green speckles ----------------------------------------------
put([
    (1, 0),
    (7, 1),
    (11, 2),
    (15, 3),
    (4, 3),
    (0, 6),
    (5, 6),
    (8, 7),
    (12, 8),
    (2, 9),
    (7, 9),
    (15, 10),
    (9, 11),
    (6, 12),
    (1, 13),
    (6, 13),
    (11, 13),
    (0, 15),
    (7, 15), (7, 0),   # blade crossing the vertical seam
    (10, 14),
    (14, 10),
], C)

# --- small darker grass tufts (V shaped) -------------------------------
put([(7, 3), (8, 4), (9, 3)], D)
put([(2, 13), (3, 14), (4, 13)], D)
put([(12, 11), (13, 12), (14, 11)], D)

# --- sparse bare-dirt patches -----------------------------------------
put([(4, 9), (3, 10), (4, 10), (5, 10), (3, 11), (4, 11)], E)
put([(5, 11)], F)
put([(12, 4), (13, 4), (12, 5)], E)
put([(13, 5), (11, 5)], F)
put([(9, 4)], E)
put([(2, 6)], E)

# --- tiny yellow flowers ----------------------------------------------
put([(10, 6), (9, 7), (11, 7), (10, 8)], G)
put([(10, 7)], H)
put([(1, 2), (3, 2), (2, 1)], G)
put([(2, 2)], H)
put([(12, 14), (14, 14)], G)
put([(13, 14)], H)

for y in range(16):
    for x in range(16):
        c.set(x, y, grid[y][x])

print(c.stats_text())
print(c.matrix_text())
save("rpg-grass-material", c)
finish(c)
