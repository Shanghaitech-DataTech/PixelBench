import math

c = new_canvas(32, 32, name="result")


def col(h, n):
    return c.color(h, n)


BL = col('#f8e4b8', 'bamboo_light')
BM = col('#dcb56d', 'bamboo')
BD = col('#b2823a', 'bamboo_dark')
BS = col('#7c5520', 'bamboo_shadow')
IN = col('#573a19', 'inner')
HI = col('#ffffff', 'highlight')
DM = col('#fef9ec', 'dumpling')
DS = col('#eedcb6', 'dumpling_shade')
DL = col('#c8ab7c', 'dumpling_line')
ST = col('#c9e4ec', 'steam')


def paint(pred, colr, x0=0, y0=0, x1=31, y1=31):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if pred(x, y):
                c.set(x, y, colr)


def epre(cx, cy, rx, ry, rot=0.0, a0=0.0, a1=360.0, irx=None, iry=None):
    rr = math.radians(rot)
    cr, sr = math.cos(rr), math.sin(rr)
    full = abs(((a1 - a0) % 360.0)) < 1e-9

    def p(x, y):
        dx = x - cx
        dy = y - cy
        u = dx * cr + dy * sr
        v = -dx * sr + dy * cr
        if (u * u) / (rx * rx) + (v * v) / (ry * ry) > 1.0:
            return False
        if irx is not None:
            if (u * u) / (irx * irx) + (v * v) / (iry * iry) < 1.0:
                return False
        if full:
            return True
        t = math.degrees(math.atan2(v / ry, u / rx)) % 360.0
        a = a0 % 360.0
        b = a1 % 360.0
        return (a <= t <= b) if a <= b else (t >= a or t <= b)
    return p


def bnd_of(pred):
    def b(x, y):
        return pred(x, y) and any(not pred(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    return b


# ---------------- lid (behind, tilted open) ----------------
LX, LY, LR = 22.5, 9.0, 32.0
disc = epre(LX, LY, 8.1, 4.1, LR)
dbnd = bnd_of(disc)


def upper(x, y):
    return math.degrees(math.atan2(y - LY, x - LX)) % 360.0


paint(disc, BM)                                                    # disc
paint(lambda x, y: dbnd(x, y) and 168 <= upper(x, y) <= 358, BL)   # lit upper edge
paint(lambda x, y: dbnd(x, y) and not (168 <= upper(x, y) <= 358), BS)  # dark lower edge
paint(epre(LX, LY, 5.9, 2.6, LR), BL)                              # inner panel
paint(epre(LX, LY, 5.9, 2.6, LR, a0=25, a1=155, irx=5.0, iry=2.0), BM)
paint(epre(LX, LY, 2.2, 1.1, LR), BM)                              # knob
paint(epre(LX, LY, 0.9, 0.6, LR), BD)

# ---------------- basket body ----------------
BOT = epre(16, 26.5, 11.5, 3.0)


def body(x, y):
    if 19 <= y <= 26 and abs(x - 16) <= 11.5:
        return True
    return BOT(x, y)


paint(body, BM)
paint(lambda x, y: body(x, y) and x > 17 and not body(x + 1.6, y), BD)
paint(lambda x, y: body(x, y) and x < 15 and not body(x - 1.6, y), BL)
for x in (7, 11, 15, 19, 23):
    yb = 27
    if abs(x - 16) <= 11.5:
        yb = int(26.5 + 3.0 * math.sqrt(max(0.0, 1 - ((x - 16) / 11.5) ** 2)))
    c.line(x, 20, x, yb - 1, BD)
paint(epre(16, 26.5, 11.5, 3.0, a0=10, a1=170, irx=10.4, iry=2.3), BD)
paint(epre(16, 26.5, 11.5, 3.0, a0=30, a1=150, irx=11.0, iry=2.7), BS)

# ---------------- rim ----------------
paint(epre(16, 17, 12.5, 4.4), BM)
paint(epre(16, 17, 10.3, 2.4), IN)
paint(epre(16, 17, 12.5, 4.4, a0=185, a1=355, irx=11.9, iry=3.8), BL)
paint(epre(16, 17, 12.5, 4.4, a0=150, a1=210, irx=11.6, iry=3.5), BL)


# ---------------- dumplings ----------------
def dumpling(cx, cy, s=1.0):
    bx, by = cx, cy + 0.9 * s
    brx, bry = 3.9 * s, 2.9 * s
    nx, ny = cx, cy - 2.2 * s
    nrx, nry = 2.4 * s, 2.0 * s
    bodyp = epre(bx, by, brx, bry)
    neckp = epre(nx, ny, nrx, nry)

    def mask(x, y):
        return bodyp(x, y) or neckp(x, y)

    mb = bnd_of(mask)
    paint(mask, DL)
    paint(lambda x, y: mask(x, y) and not mb(x, y), DM)
    core = epre(bx - 0.8, by - 0.8, brx - 0.9, bry - 0.9)
    paint(lambda x, y: mask(x, y) and not mb(x, y) and not neckp(x, y)
          and not core(x, y) and x >= bx - 0.4, DS)
    h1 = epre(bx - 1.9, by - 1.3, 1.0, 0.9)
    h2 = epre(bx - 2.3, by - 0.2, 0.5, 1.0)
    paint(lambda x, y: mask(x, y) and not mb(x, y) and (h1(x, y) or h2(x, y)), HI)


dumpling(9, 14, 1.0)
dumpling(23, 14, 1.0)
dumpling(16, 16, 1.0)

# ---------------- front rim ----------------
paint(epre(16, 17, 12.5, 4.4, a0=0, a1=180, irx=10.3, iry=2.4), BM)
paint(epre(16, 17, 12.5, 4.4, a0=5, a1=175, irx=11.8, iry=3.7), BD)
paint(epre(16, 17, 10.8, 2.8, a0=10, a1=170, irx=10.3, iry=2.4), BL)

# ---------------- steam ----------------
c.path("M5,10 Q7,8 4,6 Q2,4 5,2", ST, fill=False)
c.path("M12,10 Q14,8 11,6 Q9,4 12,2", ST, fill=False)

print(c.stats_text())
print(c.matrix_text())
save("bamboo_steamer", c)
finish(c)
