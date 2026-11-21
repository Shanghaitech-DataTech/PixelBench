# farm-chicken - 32x32 Stardew-style plump chicken, gentle side view, transparent bg

c = new_canvas(32, 32, None, "chicken")

OUT = c.color("#5A3B2B", "outline")
CRM = c.color("#F5E7C8", "cream")
SHD = c.color("#E3CCA4", "shade")
DEP = c.color("#C9A87C", "deep")
WNG = c.color("#EED9AF", "wing")
WNS = c.color("#D6B98B", "wing_shade")
CB  = c.color("#C65B4E", "comb")
BK  = c.color("#E8A94F", "beak")
BKD = c.color("#C9862F", "beak_dark")
EYE = c.color("#43302A", "eye")
LG  = c.color("#D9974A", "leg")
LGD = c.color("#B0702F", "leg_dark")

# ---------------- 1. silhouette (head + plump body + tail plume) ----------------
SPANS = [
    (4, 9, 15),
    (5, 8, 16), (5, 27, 29),
    (6, 8, 17), (6, 26, 30),
    (7, 7, 17), (7, 26, 30),
    (8, 7, 17), (8, 25, 30),
    (9, 7, 17), (9, 25, 30),
    (10, 7, 18), (10, 24, 29),
    (11, 7, 21), (11, 24, 28),
    (12, 7, 28),
    (13, 6, 28),
    (14, 5, 28),
    (15, 4, 28),
    (16, 4, 28),
    (17, 3, 28),
    (18, 3, 28),
    (19, 3, 28),
    (20, 4, 27),
    (21, 4, 27),
    (22, 4, 26),
    (23, 5, 25),
    (24, 5, 23),
    (25, 6, 22),
    (26, 7, 21),
]
grid = [[False] * 32 for _ in range(32)]
for y, x0, x1 in SPANS:
    c.rect(x0, y, x1 - x0 + 1, 1, CRM)
    for x in range(x0, x1 + 1):
        grid[y][x] = True


def dist_to(x, y, dx, dy, cap=7):
    d = 0
    while d < cap:
        nx, ny = x + dx * (d + 1), y + dy * (d + 1)
        if not (0 <= nx < 32 and 0 <= ny < 32) or not grid[ny][nx]:
            return d + 1
        d += 1
    return cap + 1


# ---------------- 2. shading ----------------
# head: soft shade down the right side of the face
for y, xs in [(7, (15, 16)), (8, (15, 16)), (9, (15, 16)), (10, (16, 17))]:
    for x in xs:
        if grid[y][x]:
            c.set(x, y, SHD)

# body: shade hugging the right and belly edges, deep accent at the rear
for y, x0, x1 in SPANS:
    if y < 11:
        continue
    for x in range(x0, x1 + 1):
        dr = dist_to(x, y, 1, 0)
        dd = dist_to(x, y, 0, 1)
        if dr <= 5 or (dd <= 3 and x >= 10):
            c.set(x, y, DEP if (dr <= 2 and y >= 14) else SHD)

# tail: lit on the upper-left edge, shaded toward the base
TAIL = [(5, 27, 29), (6, 26, 30), (7, 26, 30), (8, 25, 30),
        (9, 25, 30), (10, 24, 29), (11, 24, 28)]
for y, x0, x1 in TAIL:
    for x in range(x0, x1 + 1):
        c.set(x, y, SHD if (x + y) >= 35 else CRM)

# ---------------- 3. silhouette outline ----------------
c.outline(OUT)

# ---------------- 4. comb ----------------
c.set(10, 1, OUT); c.set(11, 1, OUT)
c.set(13, 1, OUT); c.set(14, 1, OUT)
c.set(9, 2, OUT);  c.set(12, 2, OUT); c.set(15, 2, OUT)
c.rect(10, 2, 2, 1, CB); c.rect(13, 2, 2, 1, CB)
c.set(9, 3, OUT);  c.set(15, 3, OUT)
c.rect(10, 3, 5, 1, CB)

# ---------------- 5. beak ----------------
c.rect(4, 8, 3, 1, OUT)
c.rect(4, 9, 3, 1, BK)
c.rect(4, 10, 3, 1, BKD)
c.rect(4, 11, 3, 1, OUT)
c.set(3, 9, OUT); c.set(3, 10, OUT)

# ---------------- 6. wattle ----------------
for y in range(12, 16):
    c.set(4, y, OUT)
c.rect(5, 12, 2, 3, CB)
c.set(5, 15, OUT); c.set(6, 15, OUT)

# ---------------- 7. eye ----------------
c.rect(9, 7, 2, 2, EYE)

# ---------------- 8. wing (built on its own layer for a clean rim) ----------------
wing = new_canvas(13, 11, None, "wing")
wing.ellipse(6, 5, 5, 4, WNG)
WING_IDX = wing.color(WNG)
for yy in range(11):
    for xx in range(13):
        if wing.get(xx, yy) == WING_IDX and (xx - 6) + (yy - 5) * 1.2 > 2:
            wing.set(xx, yy, WNS)
wing.outline(OUT)
# two small notches in the lower rim suggest separate feathers
wing.clear(4, 8, 1, 1)
wing.clear(7, 8, 1, 1)
c.blit(wing, 13, 14)

# ---------------- 9. legs ----------------
for y in (27, 28):
    c.set(10, y, OUT); c.set(13, y, OUT); c.rect(11, y, 2, 1, LG)
    c.set(16, y, OUT); c.set(19, y, OUT); c.rect(17, y, 2, 1, LGD)
c.set(9, 29, OUT);  c.rect(10, 29, 3, 1, LG);  c.set(13, 29, OUT)
c.rect(9, 30, 5, 1, OUT)
c.set(16, 29, OUT); c.rect(17, 29, 3, 1, LGD); c.set(20, 29, OUT)
c.rect(16, 30, 5, 1, OUT)

# ---------------- centre ----------------
c.shift(-1, 0)

print(c.stats_text())
print(c.matrix_text())
print(c.matrix_text(region=(19, 4, 31, 12), indices=True))
finish(c)
