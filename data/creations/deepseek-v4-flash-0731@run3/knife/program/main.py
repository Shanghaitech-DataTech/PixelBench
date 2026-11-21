from pixelbench_api import *
import math

src = input_canvas
W, H = src.stats()["size"]
ang = 54.111357044784
rot = src.select(0, 0, W, H).rotate(-ang, algorithm="rotsprite").preview("rot")
posed = rot.copy("posed")
posed.mirror("h")  # tip now RIGHT, cutting edge (bottom light band) DOWN


def alpha_copy(s, a, name):
    w, h = s.stats()["size"]
    data = s.to_rgba()[2]
    out = new_canvas(w, h, name=name)
    for y in range(h):
        for x in range(w):
            i = (y * w + x) * 4
            if data[i + 3] > 0:
                out.set(x, y, (data[i], data[i + 1], data[i + 2], round(data[i + 3] * a)))
    return out


def quad_band(cv, p0, p1, p2, w0, w1, color, n=28):
    # filled tapered band along a quadratic bezier
    L = []
    R = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        dx = 2 * (1.0 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])
        dy = 2 * (1.0 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1])
        Ln = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / Ln, dx / Ln
        w = w0 + (w1 - w0) * t
        L.append((x + nx * w, y + ny * w))
        R.append((x - nx * w, y - ny * w))
    cv.poly(L + R[::-1], color, fill=True)


g1 = alpha_copy(posed, 0.30, "ghost1")
g2 = alpha_copy(posed, 0.50, "ghost2")
g3 = alpha_copy(posed, 0.70, "ghost3")

out = new_canvas(280, 170, name="output")
xf, fy = 100, 8
out.blit(g1, xf - 96, fy)
out.blit(g2, xf - 64, fy)
out.blit(g3, xf - 32, fy)

# --- white slash effect (drawn behind the final knife) ---
# soft glow sweep arcing toward the tip
quad_band(out, (138, 90), (198, 56), (258, 72), 8.0, 3.5, (255, 255, 255, 70))
# crisp sweep
quad_band(out, (158, 84), (202, 60), (253, 74), 2.6, 1.0, (255, 255, 255, 235))
# thin bright core ending at the tip
quad_band(out, (164, 82), (204, 61), (250, 77), 1.4, 0.6, (255, 255, 255, 255))
# small speed dashes trailing beneath the blade
for (sx, sy, sl) in [(128, 98, 16), (150, 102, 12), (172, 99, 14), (196, 96, 12), (216, 93, 10)]:
    out.line(sx, sy, sx + sl, sy, (255, 255, 255, 120))
# faint double-tip flare just ahead of the point
quad_band(out, (248, 78), (258, 68), (266, 60), 1.0, 0.3, (255, 255, 255, 140))

out.blit(posed, xf, fy)

# tip flash glints over the knife
out.set(253, 77, (255, 255, 255, 255))
out.set(251, 74, (255, 255, 255, 210))
out.set(256, 80, (255, 255, 255, 170))
out.set(248, 72, (255, 255, 255, 130))
out.set(256, 73, (255, 255, 255, 110))

print(out.stats_text())

# close look at the tip / slash-end
print(out.matrix_text(region=(220, 60, 265, 100)))

finish(out)
