import math

c = new_canvas(48, 48, background=None, name="magic-staff")

# ---- palette ----
WOOD_D = c.color("#3e2714", "wood_dark")
WOOD_M = c.color("#6b4423", "wood_mid")
WOOD_L = c.color("#96693a", "wood_light")
GEM_D  = c.color("#3c1361", "gem_dark")
GEM_M  = c.color("#7b2fbf", "gem_mid")
GEM_L  = c.color("#b47ae8", "gem_light")
GEM_H  = c.color("#e9d4ff", "gem_hi")
P1     = c.color("#9d4edd", "particle_deep")
P2     = c.color("#c77dff", "particle_mid")
P3     = c.color("#e0aaff", "particle_bright")

CX, CY = 18.0, 12.0   # curl centre


def thick_poly(pts, w0, w1, off0=0.0, off1=0.0):
    """Polygon around a centerline with interpolated width and lateral offset."""
    n = len(pts)
    normals = []
    for i in range(n):
        if i == 0:
            dx, dy = pts[1][0] - pts[0][0], pts[1][1] - pts[0][1]
        elif i == n - 1:
            dx, dy = pts[-1][0] - pts[-2][0], pts[-1][1] - pts[-2][1]
        else:
            dx, dy = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
        L = math.hypot(dx, dy) or 1.0
        normals.append((-dy / L, dx / L))
    outer, inner = [], []
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        w = (w0 + (w1 - w0) * t) / 2.0
        off = off0 + (off1 - off0) * t
        nx, ny = normals[i]
        ox, oy = x + nx * off, y + ny * off
        outer.append((ox + nx * w, oy + ny * w))
        inner.append((ox - nx * w, oy - ny * w))
    return outer + inner[::-1]


def spiral_pts(cx, cy, a0, turns, r0, r1, steps=110, direction=1):
    out = []
    for i in range(steps + 1):
        t = i / steps
        a = math.radians(a0 + direction * t * turns * 360.0)
        r = r0 + (r1 - r0) * t
        out.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return out


def bezier(p0, p1, p2, steps=26):
    out = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        out.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return out


# ---- centerlines ----
curl = spiral_pts(CX, CY, 90, 1.0, 7.0, 4.2)          # one full loop, tip curling inward
shaft = bezier((18.0, 20.0), (19.0, 33.0), (23.0, 46.0))

CW0, CW1 = 2.6, 1.9    # curl band width
SW0, SW1 = 3.4, 4.8    # shaft width

# ---- wood: dark base, mid body, light edge (light from upper-left) ----
c.poly(thick_poly(shaft, SW0, SW1), WOOD_D)
c.poly(thick_poly(curl, CW0, CW1), WOOD_D)

c.poly(thick_poly(shaft, SW0 - 1.2, SW1 - 1.2, off0=0.2, off1=0.2), WOOD_M)
c.poly(thick_poly(curl, CW0 - 1.1, CW1 - 1.1, off0=-0.15, off1=-0.15), WOOD_M)

c.poly(thick_poly(shaft, 1.0, 1.0, off0=(SW0 / 2 - 0.55), off1=(SW1 / 2 - 0.55)), WOOD_L)
c.poly(thick_poly(curl, 1.0, 0.9, off0=-(CW0 / 2 - 0.55), off1=-(CW1 / 2 - 0.5)), WOOD_L)

# wood grain flecks
for gx, gy in ((21, 27), (23, 32), (21, 37), (23, 42)):
    c.set(gx, gy, WOOD_D)

# leather grip wraps on the shaft
GRIP_D = c.color("#4a2c1a", "grip_dark")
GRIP_M = c.color("#7a4a2a", "grip_mid")
for gy in (30, 31, 33, 34, 36, 37):
    for gx in range(14, 30):
        if c.get(gx, gy):
            c.set(gx, gy, GRIP_D if (gx + gy) % 2 == 0 else GRIP_M)
# highlight edge on each wrap
for gx, gy in ((18, 30), (19, 33), (20, 36)):
    if c.get(gx, gy):
        c.set(gx, gy, GRIP_M)

# ---- gem nested in the curl ----
c.ellipse(CX, CY, 3.3, 3.3, GEM_M)
c.ellipse(CX + 0.9, CY + 0.9, 2.2, 2.2, GEM_D)
c.ellipse(CX - 1.1, CY - 1.2, 1.2, 1.2, GEM_L)
c.set(16, 9, GEM_H)
c.set(15, 10, GEM_H)
c.set(16, 10, GEM_L)


def sparkle(x, y, col):
    c.set(x, y, col)
    c.set(x - 1, y, col)
    c.set(x + 1, y, col)
    c.set(x, y - 1, col)
    c.set(x, y + 1, col)


# ---- purple particles ----
c.circle(7, 8, 1, P1)
c.circle(29, 6, 1, P2)
sparkle(6, 18, P3)
sparkle(31, 17, P3)
sparkle(26, 10, GEM_H)
for px, py, col in ((4, 14, P2), (9, 2, P2), (16, 1, P2), (22, 2, P1),
                    (25, 3, P3), (32, 11, P1), (33, 21, P1), (12, 23, P2),
                    (27, 28, P2), (15, 33, P1), (26, 38, P3), (28, 43, P1),
                    (12, 12, P3), (13, 3, P1), (35, 26, P2), (34, 32, P3),
                    (11, 28, P1), (20, 4, P3), (9, 40, P2), (33, 40, P2)):
    c.set(px, py, col)

print(c.stats_text())
print(c.matrix_text())
finish(c)
