def bez(p0, p1, p2, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t**2*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t**2*p2[1]
        pts.append((x, y))
    return pts

c = input_canvas.copy(name="output")
f1 = c

f2 = input_canvas.copy(name="slash")
BLACK = f2.color("#000000", name="slash_black")
WHITE = f2.color("#f2f2f6", name="slash_edge")
STEEL = f2.color("#e9edf5", name="blade")
EDGE  = f2.color("#9aa6bd", name="blade_edge")
GUARD = f2.color("#1a1420", name="tsuba")

# ---- slash trail: lower-left -> upper-right, bulging slightly down-right ----
P0, C, P1 = (3, 63), (48, 28), (58, 13)
pts = bez(P0, C, P1, 80)
n = len(pts)

def width_at(f):
    if f < 0.08 or f > 0.92:
        return 1
    if f < 0.22 or f > 0.80:
        return 2
    return 3

# pale rim on the upper-left (leading) side first, black trail over it
for i in range(4, n - 4):
    x, y = pts[i]
    xi, yi = int(round(x)), int(round(y))
    f2.set(xi - 2, yi - 1, WHITE)

for i, (x, y) in enumerate(pts):
    xi, yi = int(round(x)), int(round(y))
    w = width_at(i / (n - 1))
    off = (w - 1) // 2
    f2.rect(xi - off, yi - off, w, w, BLACK)

# ---- sword blade gripped in the LEFT hand at ~(39,42) ----
gx, gy = 39, 42
tx, ty = 59, 13          # tip, up-right, tangent to the trail
steps = 26
for i in range(steps + 1):
    t = i / steps
    x = gx + (tx - gx) * t
    y = gy + (ty - gy) * t
    xi, yi = int(round(x)), int(round(y))
    f2.set(xi, yi, STEEL)          # main blade
    f2.set(xi + 1, yi, EDGE)       # lower edge shading
    if i > steps - 4:              # taper to a point
        f2.set(xi + 1, yi, STEEL)
# bright glints near the tip
f2.set(52, 21, "#ffffff")
f2.set(55, 17, "#ffffff")

# cross-guard (tsuba) just below the grip, perpendicular to the blade
f2.line(37, 45, 41, 44, GUARD)
f2.line(37, 46, 41, 45, GUARD)
# hilt (tsuka) in the fist, continuing down-left behind the hand
for i in range(1, 5):
    f2.set(gx - i, gy + i + 1, GUARD)
    f2.set(gx - i + 1, gy + i + 1, "#3d2c32")

print("f1:", f1.stats_text())
print("f2:", f2.stats_text())
view(f2, scale=6)
finish([f1, f2])
