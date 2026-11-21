from pixelbench_api import *
import math

W = H = 64
c = new_canvas(W, H, name="void-eye")

def rgba(hexv, a=255):
    h = hexv.lstrip('#')
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)

CX, CY = 32, 27

# ---------------- palette ----------------
BODY_DEEP = c.color('#0a0314', 'body-deep')
BODY_DARK = c.color('#150828', 'body-dark')
BODY_MID  = c.color('#221044', 'body-mid')
RIM       = c.color('#4a2a8c', 'rim')
IRIS_OUT  = c.color('#170734', 'iris-out')
IRIS_1    = c.color('#2e1157', 'iris-1')
IRIS_2    = c.color('#4a1e8c', 'iris-2')
IRIS_3    = c.color('#6f31c2', 'iris-3')
IRIS_4    = c.color('#9749e9', 'iris-4')
P_G1      = c.color('#dbbdff', 'pupil-glow')
P_G2      = c.color('#eee0ff', 'pupil-glow2')
P_HOT     = c.color('#ffffff', 'pupil-hot')
TIPT      = c.color('#5c309f', 'tip')
TIPB      = c.color('#8b5ecd', 'tip-b')
HILITE    = c.color('#a66fe8', 'hilite')
VEIN      = c.color('#33215e', 'vein')
SHAD_A    = c.color(rgba('#0d0522', 72), 'shadow-a')
SHAD_B    = c.color(rgba('#0d0522', 36), 'shadow-b')
SHAD_C    = c.color(rgba('#0d0522', 110), 'shadow-c')
DOT       = c.color(rgba('#8f5ad8', 92), 'aura-dot')

# ---------------- body (giant eyeball) ----------------
c.ellipse(CX, CY, 17, 16, BODY_DARK)
c.ellipse(CX, CY, 16, 15, BODY_MID)
c.circle(21, 19, 5, BODY_MID)
c.circle(43, 19, 5, BODY_MID)
c.ellipse(CX, 30, 15, 9, BODY_MID)
c.ellipse(CX, 34, 11, 6, BODY_DEEP)

# ---------------- horns ----------------
c.poly([(17, 15), (12, 4), (24, 15)], BODY_DARK)
c.poly([(47, 15), (52, 4), (40, 15)], BODY_DARK)

# ---------------- tentacles ----------------
def tentacle(p0, pc, p2, r0, r1, col):
    n = 12
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * pc[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * pc[1] + t * t * p2[1]
        r = max(1, round(r0 + (r1 - r0) * t))
        c.circle(round(x), round(y), r, col)

tents = [
    ((15, 29), (10, 33), (8, 39), 2.6, 1),
    ((20, 39), (17, 46), (15, 50), 3.0, 1),
    ((25, 42), (23, 48), (21, 52), 3.0, 1),
    ((32, 43), (31, 50), (30, 53), 3.0, 1),
    ((39, 42), (41, 48), (43, 52), 3.0, 1),
    ((44, 39), (47, 46), (49, 50), 3.0, 1),
    ((49, 29), (54, 33), (56, 39), 2.6, 1),
]
for p0, pc, p2, r0, r1 in tents:
    tentacle(p0, pc, p2, r0, r1, BODY_DARK)
    tentacle(p0, pc, p2, r0, r1, BODY_MID)
for p0, pc, p2, r0, r1 in tents:
    tx, ty = p2
    c.circle(tx, ty, 1, TIPT)
    c.set(tx, ty, TIPB)

# ---------------- silhouette rim ----------------
c.outline(RIM)
c.outline(RIM)

# ---------------- eye socket & iris ----------------
c.circle(CX, CY, 11, BODY_DEEP)
c.circle(CX, CY, 10, IRIS_OUT)
c.circle(CX, CY, 8, IRIS_1)
c.circle(CX, CY, 6, IRIS_2)
c.circle(CX, CY, 5, IRIS_3)

# iris spokes (rays)
for a in range(0, 360, 45):
    rad = math.radians(a)
    x0 = CX + round(5 * math.cos(rad))
    y0 = CY + round(5 * math.sin(rad))
    x1 = CX + round(10 * math.cos(rad))
    y1 = CY + round(10 * math.sin(rad))
    c.line(x0, y0, x1, y1, IRIS_1)

# faintly glowing pupil
c.circle(CX, CY, 4, rgba('#8b5ecd', 55))
c.circle(CX, CY, 3, P_G1)
c.circle(CX, CY, 2, P_G2)
c.circle(CX, CY, 1, P_HOT)

# brow / hood shading the top of the iris
c.ellipse(CX, 15, 16, 5, BODY_DEEP)

# lower inner shade (kept off the pupil)
c.ellipse(CX, 34, 11, 3, BODY_DEEP)
# side sclera shading, outside the iris columns
c.ellipse(17, 27, 3, 13, BODY_DEEP)
c.ellipse(47, 27, 3, 13, BODY_DEEP)

# veins from iris to sclera edge
for a in (60, 120, 240, 300):
    rad = math.radians(a)
    x0 = CX + round(10 * math.cos(rad))
    y0 = CY + round(10 * math.sin(rad))
    x1 = CX + round(14 * math.cos(rad))
    y1 = CY + round(14 * math.sin(rad))
    c.line(x0, y0, x1, y1, VEIN)

# sheen
c.circle(23, 22, 2, HILITE)
c.set(24, 21, HILITE)

# ---------------- floating aura motes ----------------
for (mx, my) in [(12, 9), (25, 3), (39, 3), (52, 9), (58, 21), (57, 31), (52, 42), (11, 20), (9, 31)]:
    c.circle(mx, my, 1, DOT)

# ---------------- soft shadow beneath ----------------
c.ellipse(CX, 58, 16, 4, SHAD_B)
c.ellipse(CX, 58, 14, 3, SHAD_B)
c.ellipse(CX, 58, 10, 3, SHAD_A)
c.ellipse(CX, 58, 6, 2, SHAD_C)
# drifting wisp shadows (hovering feel)
c.ellipse(24, 61, 6, 2, SHAD_B)
c.ellipse(41, 61, 6, 2, SHAD_B)
c.ellipse(18, 60, 4, 1, SHAD_A)
c.ellipse(47, 60, 4, 1, SHAD_A)

# ---------------- report ----------------
print(c.stats_text())
print("colors:", len(c.palette()))

finish(c)
