import math

c = new_canvas(48, 48, name="staff")

# palette
wood_deep = c.color("#4a2c12", "wood_deep")
wood_dark = c.color("#5a3a1e", "wood_dark")
wood = c.color("#8b5a2b", "wood")
wood_light = c.color("#c68b4e", "wood_light")

p_deep = c.color("#5b21b6", "p_deep")
p_mid = c.color("#9333ea", "p_mid")
p_light = c.color("#c084fc", "p_light")
p_pale = c.color("#ede9fe", "p_pale")
p_glow = c.color((147, 51, 234, 55), "p_glow")

def stamp(x, y, r, color):
    c.circle(int(round(x)), int(round(y)), r, color)

# ---- staff geometry ----
# vertical-ish shaft, then a crook that bends left over the top and curls down
shaft = []
for i in range(41):
    t = i / 40
    x = 23 + t * 1.0          # 23 -> 24, slight lean right
    y = 44 - t * 22.0         # 44 -> 22
    shaft.append((x, y, t))

# curved head: cubic bezier, crook opening to the lower right
HP0 = (24, 22)
HP1 = (24, 11)
HP2 = (10, 11)
HP3 = (15, 30)
head = []
for i in range(61):
    t = i / 60
    mt = 1 - t
    x = mt**3 * HP0[0] + 3 * mt * mt * t * HP1[0] + 3 * mt * t * t * HP2[0] + t**3 * HP3[0]
    y = mt**3 * HP0[1] + 3 * mt * mt * t * HP1[1] + 3 * mt * t * t * HP2[1] + t**3 * HP3[1]
    head.append((x, y, t))

def r_main(t):
    return 2 if t < 0.5 else 1

def r_dark(t):
    return r_main(t) + 1

# ---- soft purple glow behind the head ----
c.circle(19, 23, 4, p_glow)
c.circle(27, 13, 3, p_glow)
c.circle(11, 20, 2, p_glow)

# ---- staff body: dark outline pass, then wood pass ----
for x, y, t in shaft:
    stamp(x, y, r_dark(t), wood_dark)
for x, y, t in head:
    stamp(x, y, 2, wood_dark)

for x, y, t in shaft:
    stamp(x, y, r_main(t), wood)
for x, y, t in head:
    stamp(x, y, 1, wood)

# ---- highlights and grain ----
# shaft: light streak on the left face
c.line(21, 42, 22, 24, wood_light)
# head: light along the outer (top/left) edge
for i in range(8, len(head) - 8):
    x, y, t = head[i]
    xp, yp, _ = head[i + 1]
    xm, ym, _ = head[i - 1]
    tx = xp - xm
    ty = yp - ym
    L = math.hypot(tx, ty) or 1.0
    nx = -ty / L
    ny = tx / L
    if ny > 0:
        nx, ny = -nx, -ny
    stamp(x + nx * 0.7, y + ny * 0.7, 0, wood_light)

# grain specks down the middle of the shaft
for gy in (42, 38, 34, 30, 26):
    c.set(24, gy, wood_deep)

# ---- floating purple crystal inside the crook ----
gem = [(19, 20), (22, 24), (19, 28), (16, 24)]
c.poly(gem, p_mid, fill=True)
c.poly([(19, 20), (16, 24), (19, 28)], p_light, fill=True)
c.line(19, 20, 19, 28, p_deep)
c.set(19, 20, p_pale)
c.set(18, 23, p_pale)
c.set(19, 27, p_deep)
c.set(20, 25, p_deep)

# ---- sparkles ----
def sparkle(x, y):
    c.set(x, y, p_pale)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        c.set(x + dx, y + dy, p_light)

sparkle(33, 8)
sparkle(7, 15)
sparkle(28, 33)

# ---- purple particle effects ----
for px, py, pr, col in [
    (30, 8, 1, p_mid), (35, 12, 0, p_light), (38, 18, 0, p_mid),
    (28, 4, 0, p_pale), (24, 2, 0, p_pale), (13, 5, 0, p_light),
    (8, 12, 1, p_mid), (5, 18, 0, p_pale), (6, 26, 0, p_light),
    (9, 33, 1, p_deep), (12, 38, 0, p_mid), (17, 14, 0, p_pale),
    (31, 17, 0, p_light), (33, 24, 0, p_mid), (36, 27, 0, p_deep),
    (15, 36, 0, p_light), (21, 37, 0, p_deep), (4, 9, 0, p_deep),
    (27, 29, 0, p_pale), (11, 27, 0, p_mid),
]:
    c.circle(px, py, pr, col)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 47, 47), indices=False))
finish(c)
