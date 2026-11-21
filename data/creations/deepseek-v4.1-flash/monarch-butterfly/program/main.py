from collections import deque

ORANGE   = "#EF7C13"   # main wing orange
ORANGE_D = "#C2560B"   # deeper orange at the wing root
BLACK    = "#1E1712"   # veins / borders / body
WHITE    = "#F7F3EA"   # spots

W, H = 32, 32

# ---------------- silhouette of the LEFT half (spans are inclusive) ----------
FORE = {
    1: (5, 7), 2: (4, 9), 3: (3, 11), 4: (2, 12), 5: (2, 13), 6: (2, 14),
    7: (2, 14), 8: (3, 14), 9: (4, 14), 10: (5, 14), 11: (7, 14),
    12: (9, 14), 13: (11, 14), 14: (13, 14),
}
HIND = {
    15: (11, 14), 16: (9, 14), 17: (7, 14), 18: (5, 14), 19: (4, 14),
    20: (3, 14), 21: (2, 14), 22: (2, 14), 23: (3, 14), 24: (3, 14),
    25: (4, 14), 26: (6, 14), 27: (8, 14), 28: (10, 14),
}

shape, fw, hw = set(), set(), set()
for rows, tgt in ((FORE, fw), (HIND, hw)):
    for y, (x0, x1) in rows.items():
        for x in range(x0, x1 + 1):
            shape.add((x, y)); tgt.add((x, y))

# ---------------- body (head, thorax, abdomen) ------------------------------
body_rows = {4: (15, 16), 5: (15, 16), 6: (15, 16), 7: (14, 17),
             8: (14, 17), 9: (14, 17), 10: (15, 16), 11: (15, 16),
             12: (15, 16), 13: (15, 16), 14: (15, 16), 15: (15, 16),
             16: (15, 16), 17: (15, 16), 18: (15, 16), 19: (15, 16),
             20: (15, 16), 21: (15, 16)}
body = set()
for y, (x0, x1) in body_rows.items():
    for x in range(x0, x1 + 1):
        body.add((x, y))

ANT = [(15, 3), (14, 2), (13, 1), (12, 1)]

full = shape | body | set(ANT)
NB4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dist_map(s):
    """4-connected distance from the outside of the union silhouette."""
    dist, q = {}, deque()
    for p in s:
        if any(((p[0] + dx, p[1] + dy) not in s) for dx, dy in NB4):
            dist[p] = 1
            q.append(p)
    while q:
        p = q.popleft()
        for dx, dy in NB4:
            n = (p[0] + dx, p[1] + dy)
            if n in s and n not in dist:
                dist[n] = dist[p] + 1
                q.append(n)
    return dist


D = dist_map(full)

# ---------------- veins -----------------------------------------------------
vein_c = new_canvas(W, H, name="veins")
VEINS = [((13, 12), (4, 1)),    # forewing, low
         ((13, 9), (8, 1)),     # forewing, mid
         ((13, 6), (10, 1)),    # forewing, high
         ((10, 15), (4, 19)),   # hindwing, upper
         ((13, 19), (4, 24)),   # hindwing, mid
         ((13, 19), (9, 28))]   # hindwing, lower
for a, b in VEINS:
    vein_c.line(a[0], a[1], b[0], b[1], "#ffffff")
vein_px = {(x, y) for y in range(H) for x in range(W) if vein_c.get(x, y) != 0}

# ---------------- colour the left half --------------------------------------
pix = {p: (BLACK if D[p] == 1 else ORANGE) for p in shape}

# darker orange where the wings meet the body
for p in shape:
    if pix[p] == ORANGE and p[0] >= 13:
        pix[p] = ORANGE_D

# black apex across the forewing tip
for p in fw:
    x, y = p
    if (x + y) <= 9 and D[p] <= 5:
        pix[p] = BLACK

# veins
for p in shape:
    if p in vein_px and pix[p] != BLACK:
        pix[p] = BLACK

# body + antennae
for p in body | set(ANT):
    pix[p] = BLACK

# white spots on the dark margins
SPOTS = [(6, 2), (9, 3), (4, 4), (3, 6), (3, 23), (7, 26), (12, 28)]
for (x, y) in SPOTS:
    if pix.get((x, y)) == BLACK:
        pix[(x, y)] = WHITE

half = new_canvas(W, H, name="half")
for (x, y), col in pix.items():
    half.set(x, y, col)

right = half.copy(name="right").mirror("h")
result = new_canvas(W, H, name="result")
result.blit(right, 0, 0)
result.blit(half, 0, 0)

print(result.stats_text())
print(result.matrix_text())
save("monarch_butterfly", result)
finish(result)
