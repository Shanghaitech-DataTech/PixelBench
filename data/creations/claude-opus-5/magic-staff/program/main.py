import math

c = new_canvas(48, 48, name="output")

# ---- palette ----
W_DK = "#2a1709"   # wood shadow
W_MD = "#5a3620"   # wood mid
W_LT = "#8a5a33"   # wood light
W_HL = "#b5834f"   # wood highlight
GR_DK = "#3f2353"  # wrap shadow
GR_MD = "#6a3c92"  # wrap mid
GR_LT = "#9a63c4"  # wrap light
P_CORE = "#f2e2ff"
P_LT = "#d9a6ff"
P_MD = "#a455ef"
P_DK = "#6a23b8"
P_GLOW = "#8a3fd055"
P_FAINT = "#b06cf088"

CX, CY = 23.0, 11.0
R_MID = 5.7


def hook_sample(t):
    ang = math.radians(90 - 290 * t)
    half = 1.45 - 0.95 * (t ** 2.2)          # tapers toward the tip
    r = R_MID
    return ang, r, half


# ---- hook body (filled band) ----
outer, inner = [], []
steps = 120
for i in range(steps + 1):
    t = i / steps
    ang, r, half = hook_sample(t)
    co, si = math.cos(ang), math.sin(ang)
    outer.append((CX + (r + half) * co, CY + (r + half) * si))
    inner.append((CX + (r - half) * co, CY + (r - half) * si))

poly_pts = [(int(round(x)), int(round(y))) for x, y in outer + inner[::-1]]
c.poly(poly_pts, W_MD, fill=True)

# rim shading: light on the outside, shadow on the inside
for i in range(steps + 1):
    t = i / steps
    ang, r, half = hook_sample(t)
    co, si = math.cos(ang), math.sin(ang)
    ox, oy = CX + (r + half - 0.35) * co, CY + (r + half - 0.35) * si
    ix, iy = CX + (r - half + 0.35) * co, CY + (r - half + 0.35) * si
    deg = 90 - 290 * t
    c.set(int(round(ox)), int(round(oy)), W_LT if -210 < deg < 30 else W_MD)
    c.set(int(round(ix)), int(round(iy)), W_DK)

# tip gets a bright point
c.set(17, 14, W_HL)
c.set(16, 13, W_LT)

# ---- shaft ----
for y in range(17, 48):
    f = (y - 17) / 30.0
    cxs = 23.0 - 3.0 * f
    x0 = int(round(cxs)) - 1
    c.set(x0, y, W_LT)
    c.set(x0 + 1, y, W_MD)
    c.set(x0 + 2, y, W_DK)

# wood grain flecks
for (gx, gy) in [(22, 20), (22, 24), (21, 38), (20, 42), (23, 19), (21, 27)]:
    c.set(gx, gy, W_DK)
for (gx, gy) in [(21, 22), (21, 31), (20, 40), (22, 18)]:
    c.set(gx, gy, W_HL)

# ---- grip wrap ----
for y in range(28, 38):
    f = (y - 17) / 30.0
    cxs = 23.0 - 3.0 * f
    x0 = int(round(cxs)) - 1
    cols = [GR_MD, GR_LT, GR_DK]
    if (y - 28) % 3 == 0:
        cols = [GR_LT, GR_MD, GR_MD]
    elif (y - 28) % 3 == 2:
        cols = [GR_DK, GR_MD, GR_DK]
    for k in range(3):
        c.set(x0 + k, y, cols[k])

# wrap ends
c.set(20, 27, GR_DK)
c.set(21, 27, GR_DK)
c.set(22, 27, GR_DK)
c.set(20, 38, GR_DK)
c.set(21, 38, GR_DK)
c.set(19, 38, GR_DK)

# ---- butt cap ----
c.rect(19, 44, 3, 3, W_DK, fill=True)
c.set(19, 44, W_MD)
c.set(20, 45, W_MD)
c.set(20, 47, W_DK)
c.set(19, 47, W_DK)
c.set(21, 47, W_DK)

# ---- orb in the hook ----
c.circle(23, 11, 4, P_GLOW, fill=False)
c.circle(23, 11, 3, P_FAINT, fill=True)
c.circle(23, 11, 2, P_MD, fill=True)
c.set(23, 13, P_DK)
c.set(22, 13, P_DK)
c.set(24, 12, P_DK)
c.set(22, 10, P_LT)
c.set(23, 10, P_LT)
c.set(22, 9, P_CORE)

# ---- particles ----
sparks = [(33, 6), (13, 21), (30, 24), (29, 7)]
for (sx, sy) in sparks:
    c.set(sx, sy, P_CORE)
    c.set(sx - 1, sy, P_LT)
    c.set(sx + 1, sy, P_LT)
    c.set(sx, sy - 1, P_LT)
    c.set(sx, sy + 1, P_LT)

motes_lt = [(31, 3), (18, 5), (34, 11), (28, 17), (14, 9), (16, 26), (27, 31)]
motes_md = [(36, 14), (12, 15), (20, 2), (10, 25), (38, 9), (33, 19), (15, 34), (26, 1)]
motes_dk = [(8, 20), (32, 37), (12, 39), (37, 30), (29, 12), (17, 31), (35, 24)]
for (px, py) in motes_lt:
    c.set(px, py, P_LT)
for (px, py) in motes_md:
    c.set(px, py, P_MD)
for (px, py) in motes_dk:
    c.set(px, py, P_FAINT)

view(c)
finish(c)
