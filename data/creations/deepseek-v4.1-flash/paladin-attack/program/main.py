import math

SRC = input_canvas
W, H = 64, 68
DX, DY = 0, 4

f1 = new_canvas(W, H, background=None, name="frame1")
f1.blit(SRC, DX, DY)
f2 = new_canvas(W, H, background=None, name="frame2")
f2.blit(SRC, DX, DY)

WHITE = f2.color('#ffffff')
FRINGE = f2.color('#cfc4d2')

PX, PY = 33.0, 19.5          # grip / pivot, input coords
TH = math.radians(175.0)
cT, sT = math.cos(TH), math.sin(TH)


def dist_seg(x, y, x0, y0, x1, y1):
    vx, vy = x1 - x0, y1 - y0
    wx, wy = x - x0, y - y0
    L2 = vx * vx + vy * vy
    t = 0.0 if L2 == 0 else max(0.0, min(1.0, (wx * vx + wy * vy) / L2))
    return math.hypot(x - (x0 + t * vx), y - (y0 + t * vy))


def in_head(x, y):
    if 0 <= y <= 7 and 16 <= x <= 30:
        return True
    if 8 <= y <= 9 and 20 <= x <= 31:
        return True
    if y == 10 and 22 <= x <= 34:
        return True
    return False


def in_weapon(x, y):
    if math.hypot(x - PX, y - PY) <= 5.8:
        return False
    if in_head(x, y):
        return True
    return dist_seg(x, y, 26, 9, 41, 19) <= 3.6


weapon = {}
for y in range(0, 25):
    for x in range(14, 43):
        if in_weapon(x, y):
            i = SRC.get(x, y)
            if i != 0:
                weapon[(x, y)] = i

for (x, y) in weapon:
    f2.set(x + DX, y + DY, None)

# ---- motion trail (under the weapon) ----
AX, AY = PX + DX, PY + DY
a0, a1 = math.radians(-112.0), math.radians(56.0)
R = 19.0
trail_cells = []


def stroke(col, k, n, aa0, aa1):
    for i in range(n + 1):
        t = i / n
        a = aa0 + (aa1 - aa0) * t
        h = (0.7 + 1.55 * t) * k
        ca, sa = math.cos(a), math.sin(a)
        steps = max(1, int(round(h * 2)))
        for j in range(-steps, steps + 1):
            rr = R + h * j / steps
            x = int(round(AX + rr * ca))
            y = int(round(AY + rr * sa))
            trail_cells.append((x, y, col))


stroke(FRINGE, 1.45, 300, a0, a1)
stroke(WHITE, 1.0, 300, a0, a1)
stroke(FRINGE, 0.4, 70, math.radians(-124.0), a0)
for (x, y, col) in trail_cells:
    f2.set(x, y, col)
trail_set = set((x, y) for (x, y, col) in trail_cells)

# ---- rotated weapon: the haft butt is left out so it never covers the face ----
wdest = set()
for Y in range(0, 50):
    for X in range(16, 63):
        dx = X - PX
        dy = Y - PY
        sx = PX + dx * cT + dy * sT
        sy = PY - dx * sT + dy * cT
        rx, ry = int(round(sx)), int(round(sy))
        r = math.hypot(rx - PX, ry - PY)
        ang = math.degrees(math.atan2(ry - PY, rx - PX))
        if r < 11.2 and -62.0 <= ang <= 18.0:
            continue
        i = weapon.get((rx, ry))
        if i is not None:
            f2.set(X + DX, Y + DY, i)
            wdest.add((X + DX, Y + DY))

# ---- left foot steps forward (sheared so the leg stays attached) ----
STEPX, STEPY = 5, 0
foot = []
for y in range(48, 59):
    sh = int((y - 48) * STEPX / 10.0 + 0.5)
    for x in range(3, 18):
        i = f2.get(x + DX, y + DY)
        if i not in (0, 41):
            foot.append((x, y, i, sh))
for (x, y, i, sh) in foot:
    f2.set(x + DX, y + DY, None)
foot_dest = set()
for (x, y, i, sh) in foot:
    f2.set(x + DX + sh, y + DY + STEPY, i)
    foot_dest.add((x + DX + sh, y + DY + STEPY))

print('weapon source px', len(weapon), 'drawn', len(wdest), 'trail', len(trail_set))
print(f2.stats_text())

# ---- diagnostic map of frame 2 (actual final state) ----
print('    ' + ''.join(str(x % 10) for x in range(W)))
for y in range(H):
    row = ''
    for x in range(W):
        i = f2.get(x, y)
        if i == 0:
            row += ' '
        elif i == 41:
            row += ','
        elif (x, y) in wdest:
            row += 'W'
        elif (x, y) in foot_dest:
            row += 'F'
        elif (x, y) in trail_set:
            row += 'o'
        else:
            row += '#'
    print('%3d|%s|' % (y, row))

finish([f1, f2])
