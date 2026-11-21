from pixelbench_api import new_canvas, finish, load

c = new_canvas(128, 128, name="mountain-village-sunrise")

def reg(hx, a=255):
    if a < 255:
        hx = hx + ("%02x" % a)
    return c.color(hx)

bands = [(0, "#171238"), (5, "#2b1c4e"), (11, "#402559"), (17, "#4f2c60"),
         (23, "#5d3463"), (29, "#713d64"), (35, "#8a4b6a"), (41, "#a75b6b"),
         (47, "#c06e6b"), (53, "#d9826c"), (59, "#eea06d"), (65, "#f7b470"),
         (71, "#ffc985")]
for i in range(len(bands) - 1):
    y0, col = bands[i]
    y1 = bands[i + 1][0]
    ci = c.color(col)
    for y in range(y0, y1):
        for x in range(128):
            c.set(x, y, ci)
for y in range(bands[-1][0], 76):
    ci = c.color(bands[-1][1])
    for x in range(128):
        c.set(x, y, ci)

bird = reg("#3a2444")
for (bx, by) in [(88, 26), (95, 23), (102, 27)]:
    c.line(bx - 2, by, bx, by - 1, bird)
    c.line(bx, by - 1, bx + 2, by, bird)

cl = reg("#dd8f9c", 130)
c.ellipse(30, 40, 17, 4, cl)
c.ellipse(96, 33, 20, 4, cl)
c.ellipse(72, 48, 14, 3, cl)
c.ellipse(18, 55, 14, 3, cl)
c.ellipse(114, 52, 12, 3, cl)

c.circle(64, 70, 16, reg("#ffb866", 105))
c.circle(64, 70, 11, reg("#ffe29a", 215))
c.circle(64, 70, 8, "#fff3be")
c.circle(64, 70, 5, "#fffbe2")
c.rect(0, 72, 128, 8, reg("#f6cfa6", 80))

distant = reg("#967f9e")
c.poly([(0, 72), (15, 64), (31, 69), (47, 58), (63, 67), (79, 55), (95, 64), (111, 58), (127, 68),
        (127, 82), (0, 82)], distant)
cap = reg("#eebcaa")
rl = reg("#b99cb0")
for (px, py) in [(15, 64), (47, 58), (79, 55), (111, 58)]:
    c.poly([(px - 4, py + 2), (px + 4, py + 2), (px, py - 4)], cap)
pts = [(0, 72), (15, 64), (31, 69), (47, 58), (63, 67), (79, 55), (95, 64), (111, 58), (127, 68)]
for i in range(len(pts) - 1):
    c.line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1], rl)

mid = reg("#6b5580")
c.poly([(0, 84), (20, 73), (40, 79), (61, 67), (82, 75), (103, 70), (127, 81),
        (127, 92), (0, 92)], mid)
rl2 = reg("#8d77a0")
pts2 = [(0, 84), (20, 73), (40, 79), (61, 67), (82, 75), (103, 70), (127, 81)]
for i in range(len(pts2) - 1):
    c.line(pts2[i][0], pts2[i][1], pts2[i + 1][0], pts2[i + 1][1], rl2)

back = reg("#4c6a50")
c.poly([(0, 90), (24, 85), (48, 82), (64, 80), (80, 82), (104, 85), (127, 90),
        (127, 128), (0, 128)], back)
back2 = reg("#3f5a44")
c.poly([(64, 80), (80, 82), (104, 85), (127, 90), (127, 128), (64, 128)], back2)
c.ellipse(64, 100, 54, 14, reg("#5d7b57"))

wall = reg("#8f5a36")
wall2 = reg("#7d4e30")
beam = reg("#7c4a2e")
roof = reg("#3f2c20")
roof2 = reg("#4a3426")
chim = reg("#8a6a4e")
door = reg("#3a2518")
win = reg("#ffdf9e")
smk = reg("#eae2d6", 110)


def house(x, y, w, h, wcol, rcol):
    c.rect(x, y, w, h, wcol)
    c.rect(x, y, 3, h, beam)
    c.poly([(x - 3, y), (x + w + 3, y), (x + w // 2, y - 7)], rcol)
    c.line(x + w // 2, y - 7, x + w + 3, y, chim)
    c.rect(x + w - 6, y - 11, 4, 11, rcol)
    c.rect(x + w - 6, y - 12, 4, 2, chim)
    c.rect(x + w // 2 - 2, y + h - 5, 5, 5, door)
    c.rect(x + 3, y + 3, 4, 4, win)
    c.rect(x + w - 7, y + 3, 4, 4, win)


def smoke(cx, cy):
    for i in range(5):
        c.circle(cx - i * 2, cy - i * 5, 2 + i, smk)


house(23, 90, 16, 12, wall2, roof)
house(86, 89, 16, 12, wall2, roof)
smoke(35, 80)
smoke(96, 79)
house(55, 84, 20, 15, wall, roof2)
smoke(71, 74)

trunk = reg("#4a3526")
dark = reg("#1e3a2a")
midp = reg("#24422f")


def pine(x, base, h, w, col):
    c.rect(x - 1, base - 2, 4, 4, trunk)
    c.rect(x, base - 4, 2, 3, trunk)
    n = 3
    step = h / n
    for i in range(n):
        yb = base - i * step
        half = int(w / 2 * ((i + 1) / n))
        c.poly([(x, yb - step), (x - half, yb), (x + half, yb)], col)


c.poly([(0, 110), (28, 105), (50, 103), (64, 101), (82, 103), (102, 106), (127, 110),
        (127, 128), (0, 128)], reg("#2e4a3a"))
pine(10, 120, 28, 16, dark)
pine(28, 124, 19, 11, dark)
pine(106, 118, 25, 15, dark)
pine(120, 124, 18, 11, dark)
pine(45, 111, 16, 9, midp)
pine(84, 112, 15, 9, midp)
c.rect(0, 120, 128, 8, reg("#1f3528", 130))

c.poly([(56, 128), (72, 128), (67, 109), (61, 109)], reg("#8a745c"))
c.poly([(59, 128), (69, 128), (65, 111), (63, 111)], reg("#9a8266"))
edge = reg("#6f5c46")
stone = reg("#b49a76")
for (sx, sy, sw) in [(60, 113, 5), (65, 116, 7), (60, 120, 6), (66, 123, 6), (61, 126, 8)]:
    c.rect(sx, sy, sw, 2, edge)
    c.rect(sx + 1, sy, sw - 2, 1, stone)

c.circle(48, 107, 5, reg("#ffd98c", 110))
c.rect(46, 106, 4, 5, reg("#3a2a1e"))
c.rect(47, 109, 2, 11, reg("#3a2a1e"))
c.rect(47, 107, 2, 2, reg("#ffe9a8"))

grass = reg("#3f5f45")
for (gx, gy) in [(20, 114), (36, 118), (92, 116), (108, 113), (78, 122), (50, 120)]:
    c.rect(gx, gy, 3, 1, grass)

print(c.stats_text())
finish(c)
