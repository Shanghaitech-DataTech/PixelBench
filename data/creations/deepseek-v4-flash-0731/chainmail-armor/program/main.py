from pixelbench_api import new_canvas, finish

W = H = 32
c = new_canvas(W, H)

# palette
OUT = c.color("#10141a")     # dark outline
HOLE = c.color("#2c323b")    # ring holes / deep shadow
A_BASE = c.color("#c8ced6")
A_HI = c.color("#eef1f5")
A_SH = c.color("#79818c")
B_BASE = c.color("#9fa7b1")
B_HI = c.color("#c2c8d1")
B_SH = c.color("#5d6470")

# silhouette rows (inclusive x range per y)
rows = {}
for y in range(32):
    if y == 2:
        rows[y] = (12, 19)
    elif y == 3:
        rows[y] = (9, 22)
    elif y == 4:
        rows[y] = (7, 24)
    elif y == 5:
        rows[y] = (6, 25)
    elif y == 6:
        rows[y] = (5, 26)
    elif 7 <= y <= 13:
        rows[y] = (5, 26)
    elif 14 <= y <= 20:
        rows[y] = (6, 25)
    elif 21 <= y <= 24:
        rows[y] = (7, 24)
    elif y == 25:
        rows[y] = (8, 23)
    elif y == 26:
        rows[y] = (9, 22)
    elif y == 27:
        rows[y] = (10, 21)
    elif y == 28:
        rows[y] = (11, 20)

# neck opening (transparent)
notch = {4: (14, 17), 5: (13, 18), 6: (13, 18), 7: (14, 17)}


def inside(x, y):
    if y not in rows:
        return False
    x0, x1 = rows[y]
    if not (x0 <= x <= x1):
        return False
    if y in notch:
        n0, n1 = notch[y]
        if n0 <= x <= n1:
            return False
    return True


# interlocking ring pattern: rows of 3x3 rings, staggered, alternating shade
for r in range(9):
    cy = 3 + r * 3
    sx = 5 + (r % 2)
    for k in range(9):
        cx = sx + 3 * k
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                px, py = cx + dx, cy + dy
                if not inside(px, py):
                    continue
                if dy == -1:
                    cc = A_HI if r % 2 == 0 else B_HI
                elif dy == 1:
                    cc = A_SH if r % 2 == 0 else B_SH
                else:
                    cc = A_BASE if r % 2 == 0 else B_BASE
                c.set(px, py, cc)
        if inside(cx, cy):
            c.set(cx, cy, HOLE)

# 1px dark outline around the whole armor (and the neck opening)
for y in range(32):
    for x in range(32):
        if not inside(x, y):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + dx < 32 and 0 <= y + dy < 32 and inside(x + dx, y + dy):
                    c.set(x, y, OUT)
                    break

print(c.stats_text())
finish(c)
