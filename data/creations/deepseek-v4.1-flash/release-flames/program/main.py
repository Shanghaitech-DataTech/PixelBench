W, H = 100, 72
DX, DY = 6, 4

C_RIM = '#b0300e'
C_MID = '#f27219'
C_OR = '#f4a30c'
C_YL = '#fed32c'
C_HOT = '#fff3b0'
DARK = ('#240b0cff', '#0b0102ff', '#010202ff', '#0b0b13ff', '#443d45ff')

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, DX, DY)

f2 = new_canvas(W, H, name="f2")
f2.blit(input_canvas, DX, DY)


def hex_of(c, v):
    r = c.palette()[v]['rgba']
    return r.lower() if isinstance(r, str) else '#%02x%02x%02x%02x' % tuple(r[:4])


def transparent_set(c):
    s = set()
    for p in c.palette():
        r = p['rgba']
        if isinstance(r, str):
            if r[-2:].lower() == '00':
                s.add(p['index'])
        elif len(r) > 3 and r[3] == 0:
            s.add(p['index'])
    s.add(None)
    return s


for col in (C_RIM, C_MID, C_OR, C_YL, C_HOT):
    f2.color(col)

TRANS = transparent_set(f2)


def move_region(c, x0, y0, w, h, dx, dy):
    grid = [[c.get(x0 + i, y0 + j) for i in range(w)] for j in range(h)]
    for j in range(h):
        for i in range(w):
            c.set(x0 + i, y0 + j, None)
    for j in range(h):
        for i in range(w):
            v = grid[j][i]
            if v not in TRANS:
                c.set(x0 + i + dx, y0 + j + dy, v)


def shear_rows(c, y_start, y_end, dxf):
    rows = {}
    for y in range(y_start, y_end + 1):
        rows[y] = [c.get(x, y) for x in range(W)]
        c.clear(0, y, W, 1)
    for y, row in rows.items():
        d = dxf(y)
        if d == 0:
            continue
        for x, v in enumerate(row):
            nx = x + d
            if v not in TRANS and 0 <= nx < W:
                c.set(nx, y, v)


HIP = 44
MAXLEAN = 7


def lean_dx(y):
    d = int(round((HIP - y) * 0.18))
    return max(0, min(MAXLEAN, d))


# ---- frame 2: pose ------------------------------------------------
shear_rows(f2, DY, HIP, lean_dx)         # body leans into the spell
move_region(f2, 6, 58, 14, 9, 5, -1)     # left (back) boot steps forward
move_region(f2, 25, 58, 14, 8, 2, 0)     # right (front) boot slides ahead

# the little embers of the casting frame are consumed by the spell
for y in range(H):
    for x in range(28, W):
        v = f2.get(x, y)
        if v in TRANS:
            continue
        if hex_of(f2, v) in ('#f27219ff', '#f4a30cff', '#fed32cff'):
            f2.set(x, y, None)

# warm light spilling on the leading edge of the body
for y in range(DY, HIP + 1):
    edge = None
    for x in range(60, 0, -1):
        v = f2.get(x, y)
        if v not in TRANS:
            edge = x
            break
    if edge is not None and hex_of(f2, f2.get(edge, y)) in DARK:
        f2.set(edge, y, C_MID)

# ---- frame 2: the released flame ----------------------------------
# dark red silhouette: jet, head, licks, leading spike
f2.poly([(37, 25), (67, 16), (67, 39), (37, 30)], C_RIM)
f2.circle(75, 27, 10, C_RIM)
f2.poly([(83, 20), (95, 27), (83, 34)], C_RIM)
f2.poly([(65, 21), (60, 8), (69, 13), (77, 19)], C_RIM)
f2.poly([(77, 19), (89, 7), (87, 17), (83, 21)], C_RIM)
f2.poly([(61, 33), (53, 44), (67, 40), (73, 35)], C_RIM)
f2.poly([(78, 32), (86, 41), (70, 35)], C_RIM)
f2.poly([(48, 25), (55, 20), (63, 24), (56, 28)], C_RIM)

# orange body
f2.poly([(40, 26), (67, 19), (67, 36), (40, 29)], C_MID)
f2.circle(75, 27, 8, C_MID)
f2.poly([(84, 22), (91, 27), (84, 32)], C_MID)
f2.poly([(66, 21), (63, 11), (70, 15), (76, 19)], C_MID)
f2.poly([(78, 19), (87, 10), (86, 17), (83, 20)], C_MID)
f2.poly([(62, 33), (56, 41), (67, 38), (72, 35)], C_MID)
f2.poly([(78, 33), (84, 38), (72, 34)], C_MID)

# hot core
f2.poly([(44, 26), (67, 22), (67, 33), (44, 29)], C_OR)
f2.circle(76, 26, 6, C_OR)
f2.poly([(85, 24), (89, 27), (85, 30)], C_OR)

f2.circle(77, 26, 3, C_YL)
f2.poly([(49, 27), (65, 25), (65, 29), (49, 29)], C_YL)
f2.poly([(86, 26), (88, 27), (86, 28)], C_YL)

f2.circle(78, 26, 1, C_HOT)

# sparks thrown off the spell
for (x, y, w, h, col) in [
    (90, 12, 2, 2, C_OR),
    (93, 19, 1, 1, C_YL),
    (90, 39, 2, 1, C_MID),
    (55, 9, 1, 2, C_YL),
    (49, 45, 2, 1, C_OR),
    (65, 47, 1, 2, C_MID),
    (44, 12, 2, 2, C_OR),
    (43, 41, 1, 1, C_YL),
    (34, 33, 2, 2, C_MID),
]:
    f2.rect(x, y, w, h, col)

print(f1.stats_text())
print(f2.stats_text())

save("frame1", f1)
save("frame2", f2)
finish([f1, f2])
