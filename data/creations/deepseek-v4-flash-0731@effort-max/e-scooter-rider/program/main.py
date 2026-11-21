from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

WHEEL   = c.color("#17181c")
HUB     = c.color("#c9d1d9")
FRAME   = c.color("#8b939c")
FRAME_D = c.color("#3a3f47")
HELMET  = c.color("#e23c30")
HELMET_HI = c.color("#f47067")
BRIM    = c.color("#a3261d")
SKIN    = c.color("#f6c896")
SHIRT   = c.color("#2f7fd1")
PANTS   = c.color("#3d4786")
PANTS_D = c.color("#2a3157")
SHOE    = c.color("#20242c")
SHADOW  = c.color((0, 0, 0, 70))
SHADOW2 = c.color((0, 0, 0, 40))
MOTION  = c.color((255, 255, 255, 70))

def row(x0, x1, y, col):
    for x in range(x0, x1 + 1):
        c.set(x, y, col)

# ---- ground shadow ----
row(4, 27, 30, SHADOW)
c.set(6, 29, SHADOW)
c.set(25, 29, SHADOW)
row(5, 26, 31, SHADOW2)

# ---- motion dashes behind rear wheel ----
row(1, 2, 28, MOTION)
row(0, 0, 29, MOTION)
c.set(3, 29, MOTION)

# ---- wheels ----
for cx in (6, 25):
    c.circle(cx, 28, 2, WHEEL)
    c.circle(cx, 28, 1, HUB)

# ---- deck ----
row(4, 21, 27, FRAME)
row(5, 21, 28, FRAME_D)
row(7, 19, 28, SHOE)  # dark inlay front/back feet zone

# ---- stem ----
for y in range(15, 27):
    c.set(20, y, FRAME)
    c.set(21, y, FRAME_D)

# ---- fork to front wheel ----
for y in range(19, 28):
    x = 21 + (y - 19) // 3
    c.set(x, y + 0, FRAME_D)

# ---- handlebars ----
row(18, 26, 13, FRAME)
row(17, 25, 14, FRAME_D)
c.set(17, 13, WHEEL)
c.set(26, 13, WHEEL)

# ---- left leg (behind) ----
row(10, 11, 21, PANTS_D)
row(10, 11, 22, PANTS_D)
row(9, 10, 23, PANTS_D)
row(9, 10, 24, PANTS_D)
c.set(9, 25, PANTS_D)
row(8, 11, 26, PANTS_D)
row(8, 11, 27, SHOE)

# ---- right leg (front) ----
for y in range(21, 26):
    row(12, 13, y, PANTS)
c.set(14, 26, PANTS)
row(12, 14, 26, PANTS)
row(12, 15, 27, SHOE)

# ---- torso ----
row(13, 15, 13, SHIRT)
row(13, 15, 14, SHIRT)
row(12, 15, 15, SHIRT)
row(12, 14, 16, SHIRT)
row(12, 14, 17, SHIRT)
row(12, 14, 18, SHIRT)
row(12, 14, 19, SHIRT)
row(11, 14, 20, SHIRT)

# ---- right arm reaching to the handlebar ----
row(15, 18, 15, SHIRT)
c.set(19, 15, SHIRT)
c.set(18, 14, SHIRT)
c.set(19, 14, SKIN)   # hand
c.set(20, 14, SKIN)
c.set(20, 15, SKIN)
c.set(21, 13, SKIN)

# ---- head + helmet (face right) ----
row(15, 15, 6, HELMET)
row(13, 17, 7, HELMET)
row(14, 16, 7, HELMET_HI)
row(12, 18, 8, HELMET)
row(13, 17, 8, HELMET_HI)
row(12, 18, 9, HELMET)
row(13, 17, 9, HELMET_HI)
row(13, 17, 10, BRIM)
row(13, 17, 11, SKIN)
row(13, 17, 12, SKIN)
row(14, 16, 13, SKIN)
c.set(15, 12, WHEEL)  # eye

print(c.stats_text())
finish(c)
