import math

OUT    = "#32200f"  # dark outline
# ---------- helpers ----------
def rr(c, x, y, w, h, r, col):
    """rounded-ish rectangle"""
    c.rect(x + r, y, w - 2 * r, h, col)
    c.rect(x, y + r, w, h - 2 * r, col)
    c.circle(x + r, y + r, r, col)
    c.circle(x + w - 1 - r, y + r, r, col)
    c.circle(x + r, y + h - 1 - r, r, col)
    c.circle(x + w - 1 - r, y + h - 1 - r, r, col)

c = new_canvas(64, 64, background="#2e5b57", name="combo")

# table vignette
c.rect(0, 0, 64, 2, "#254a47"); c.rect(0, 62, 64, 2, "#254a47")
c.rect(0, 0, 2, 64, "#254a47"); c.rect(62, 0, 2, 64, "#254a47")

# ---------- tray ----------
rr(c, 6, 9, 56, 53, 6, "#1d3835")          # drop shadow
rr(c, 3, 5, 58, 56, 6, OUT)                # outline
rr(c, 4, 6, 56, 54, 5, "#c0452f")          # tray red
rr(c, 6, 8, 52, 49, 4, "#a8381f")          # inner wall
rr(c, 8, 10, 48, 43, 3, "#f0e3c2")         # paper liner
# rim light / shade for 45-degree depth
c.rect(10, 8, 44, 1, "#e0634a")
c.rect(56, 11, 1, 42, "#8a2a1a")
c.rect(8, 53, 48, 3, "#8a2a1a")
c.rect(5, 56, 54, 1, "#e0634a")
c.rect(5, 57, 54, 3, "#8a2a1a")
# liner diagonal stripes
for i in range(0, 48, 9):
    x0 = 8 + i
    ex = x0 - 42
    ey = 52
    if ex < 8:
        ey = 10 + (x0 - 8); ex = 8
    c.line(x0, 10, ex, ey, "#e2d0a8")
for j in range(0, 43, 9):
    y0 = 10 + j
    c.line(55, y0, 13 + j, 52, "#e2d0a8")

# ---------- contact shadows on liner ----------
c.ellipse(21, 49, 12, 3, "#d8c49c")
c.ellipse(44, 25, 8, 2, "#d8c49c")
c.rect(43, 46, 14, 3, "#d8c49c")
c.ellipse(36, 48, 6, 2, "#d8c49c")
c.ellipse(44, 51, 6, 1, "#d8c49c")
c.ellipse(50, 48, 6, 2, "#d8c49c")
c.ellipse(12, 16, 5, 2, "#d8c49c")
c.ellipse(22, 13, 4, 1, "#d8c49c")

# ---------- dipping sauce cups (back-left) ----------
c.circle(12, 12, 4, OUT); c.circle(12, 12, 3, "#f2ede2"); c.circle(12, 12, 2, "#c62f1e")
c.set(10, 10, "#e0563f"); c.set(11, 10, "#e0563f"); c.set(14, 14, "#cfc4b0")
c.circle(22, 10, 3, OUT); c.circle(22, 10, 2, "#f2ede2"); c.circle(22, 10, 1, "#e8a01c")
c.set(21, 9, "#f7c34e")

# ---------- cola cup (back-right) ----------
c.line(49, 15, 54, 5, "#d43a2a")                               # straw (behind rim)
c.line(48, 15, 53, 5, "#d43a2a")
for i in range(11):
    t = i / 10
    if i % 3 == 1:
        c.set(round(48 + 5 * t), round(15 - 10 * t), "#f2ede2")  # candy stripes
    if i % 3 == 2:
        c.set(round(49 + 5 * t), round(15 - 10 * t), "#f2ede2")
c.set(52, 4, "#d43a2a"); c.set(53, 4, "#d43a2a")               # bent tip
c.poly([(35, 15), (53, 15), (51, 25), (37, 25)], OUT)          # body outline
c.poly([(36, 16), (52, 16), (50, 24), (38, 24)], "#f2ede2")   # cup
c.line(37, 19, 51, 19, "#d43a2a")                              # red band
c.line(38, 20, 50, 20, "#d43a2a")
c.line(39, 21, 49, 21, "#d43a2a")
c.line(49, 17, 48, 23, "#cfc4b0")
c.line(38, 17, 39, 22, "#ffffff")
c.ellipse(44, 12, 8, 4, OUT)                                   # rim outline
c.ellipse(44, 12, 7, 3, "#f2ede2")                             # rim
c.ellipse(44, 13, 6, 2, "#3a1f10")                             # cola (offset -> pale lip)
c.rect(40, 11, 3, 3, "#aed6d6"); c.rect(40, 11, 2, 2, "#e8f4f4")  # ice
c.rect(46, 13, 3, 3, "#aed6d6"); c.rect(46, 13, 2, 2, "#e8f4f4")
c.set(40, 11, "#ffffff"); c.set(46, 13, "#ffffff")
c.set(44, 14, "#6a4020"); c.set(49, 12, "#6a4020")             # bubbles

# ---------- fries in red carton (right) ----------
c.rect(43, 27, 14, 4, "#7e1f14")                               # carton interior
def fry(x, yt, lean=0):
    for yy in range(yt, 31):
        xx = x + lean if (lean and yy < yt + 3) else x
        c.set(xx, yy, "#f2c14e"); c.set(xx + 1, yy, "#d9a53a")
    xt = x + lean if lean else x
    c.set(xt, yt, "#f9d97e"); c.set(xt + 1, yt, "#f9d97e")
fry(44, 23); fry(46, 21, -1); fry(48, 24); fry(50, 22, 1); fry(52, 24); fry(54, 22, 1); fry(49, 26)
c.poly([(42, 30), (58, 30), (56, 47), (44, 47)], OUT)          # carton front outline
c.poly([(43, 31), (57, 31), (55, 46), (45, 46)], "#d43a2a")    # front face
c.line(44, 31, 56, 31, "#ef5a3f")
c.line(56, 32, 54, 45, "#a8231a")
c.line(45, 33, 46, 44, "#ef5a3f")
c.ellipse(50, 38, 3, 2, "#f2c14e")                             # emblem

# ---------- cheeseburger (left, stacked layers) ----------
cx = 21
c.circle(cx, 39, 12, OUT); c.circle(cx, 39, 11, "#c98a3f")     # bottom bun
c.circle(cx, 36, 13, OUT); c.circle(cx, 36, 12, "#6e3f1e")     # patty
c.set(18, 46, "#4e2a10"); c.set(24, 46, "#4e2a10"); c.set(28, 45, "#4e2a10")
c.circle(cx, 33, 13, OUT); c.circle(cx, 33, 12, "#f7a823")     # cheese
c.rect(15, 44, 2, 3, "#f7a823"); c.rect(25, 44, 3, 4, "#f7a823"); c.rect(20, 45, 2, 2, "#f7a823")  # drips
for px, py in [(15,46),(16,46),(25,47),(26,47),(27,47),(20,46),(21,46)]:
    c.set(px, py, "#e08912")
c.set(17, 44, "#ffc95e"); c.set(24, 44, "#ffc95e")
c.circle(cx, 30, 13, OUT); c.circle(cx, 30, 12, "#58a63c")     # lettuce
for dx in range(-11, 12):                                       # wavy lettuce fringe
    yb = 30 + int(math.sqrt(max(0, 144 - dx * dx)))
    c.set(cx + dx, yb, "#3e7a28")
    if dx % 3 == 0 and yb + 1 <= 43:
        c.set(cx + dx, yb + 1, "#58a63c")
c.circle(cx, 27, 13, OUT); c.circle(cx, 27, 12, "#e8a84e")     # top bun
for dx in range(-11, 12):                                       # bun shading
    for dy in range(-11, 12):
        d2 = dx * dx + dy * dy
        if d2 <= 120:
            px, py = cx + dx, 27 + dy
            if dy >= 7 and d2 >= 64:
                c.set(px, py, "#b5762e")
            elif (dy <= -7 and -4 <= dx <= 1) or (dx <= -9 and -4 <= dy <= 1):
                c.set(px, py, "#f6c979")
for sx, sy in [(15,21),(23,19),(27,21),(12,25),(17,24),(24,17)]:  # sesame seeds
    c.set(sx, sy, "#f7e6bd"); c.set(sx + 1, sy, "#f7e6bd")
c.set(29, 24, "#f7e6bd"); c.set(29, 25, "#f7e6bd")
c.set(18, 28, "#f7e6bd"); c.set(18, 29, "#f7e6bd")

# ---------- chicken nuggets (front-center) ----------
def nugget(nx, ny):
    c.circle(nx - 2, ny - 1, 4, OUT); c.circle(nx + 2, ny + 1, 4, OUT)
    c.circle(nx - 2, ny - 1, 3, "#e2a34c"); c.circle(nx + 2, ny + 1, 3, "#e2a34c")
    c.set(nx - 3, ny - 2, "#f4c876"); c.set(nx - 2, ny - 3, "#f4c876"); c.set(nx + 1, ny - 1, "#f4c876")
    c.set(nx + 1, ny + 2, "#b9772e"); c.set(nx + 3, ny + 1, "#b9772e"); c.set(nx - 1, ny + 1, "#b9772e")
nugget(36, 44); nugget(44, 48); nugget(50, 45)

# ---------- crumbs ----------
c.set(14, 51, "#b5762e"); c.set(29, 52, "#b5762e")
c.set(40, 52, "#b9772e"); c.set(54, 51, "#b9772e")

view(c)
finish(c)
