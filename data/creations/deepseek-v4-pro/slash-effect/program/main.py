import math

def bezier_pts(a, b, c, steps=50):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) * (1 - t) * a[0] + 2 * (1 - t) * t * c[0] + t * t * b[0]
        y = (1 - t) * (1 - t) * a[1] + 2 * (1 - t) * t * c[1] + t * t * b[1]
        pts.append((round(x), round(y)))
    return pts

def crescent(a, b, h_out, h_in, steps=50, side=1):
    mid = ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)
    vx = b[0] - a[0]
    vy = b[1] - a[1]
    L = math.hypot(vx, vy)
    ux, uy = vx / L, vy / L
    nx, ny = -uy * side, ux * side
    c_out = (mid[0] + nx * h_out, mid[1] + ny * h_out)
    c_in = (mid[0] + nx * h_in, mid[1] + ny * h_in)
    outer = bezier_pts(a, b, c_out, steps)
    inner = bezier_pts(a, b, c_in, steps)
    pts = outer + inner[::-1]
    out = []
    for p in pts:
        if not out or out[-1] != p:
            out.append(p)
    return out

c = new_canvas(48, 48, name="slash")
white = c.color("#ffffff", "white")
trail1 = c.color((255, 255, 255, 130), "trail1")
trail2 = c.color((255, 255, 255, 70), "trail2")

a = (5, 43)
b = (43, 5)
# thin trailing streak lines behind the main arc
c.path("M 5 43 Q 26 26 43 5", trail2, fill=False)
c.path("M 5 43 Q 29 29 43 5", trail1, fill=False)
c.poly(crescent(a, b, 22, 10, side=1), white, fill=True)
c.set(5, 43, white)
c.set(43, 5, white)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 47, 47)))

finish(c)
