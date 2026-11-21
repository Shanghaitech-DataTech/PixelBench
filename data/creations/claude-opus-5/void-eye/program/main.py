import math

W = H = 64
CX, CY, R = 31, 25, 18

shadow_l = new_canvas(W, H, name="shadow")
tent_l   = new_canvas(W, H, name="tentacles")
orb_l    = new_canvas(W, H, name="orb")
c = orb_l  # shared palette

# ---------------- palette ----------------
body_dk   = c.color("#120a1e", "body_dk")
body_md   = c.color("#2c1944", "body_md")
body_lt   = c.color("#4a2d6b", "body_lt")
body_hi   = c.color("#8158ad", "body_hi")

sclera_dk = c.color("#9f8cb8", "sclera_dk")
sclera_md = c.color("#cdc0e0", "sclera_md")
sclera_lt = c.color("#f6f2ff", "sclera_lt")

iris_dk   = c.color("#230947", "iris_dk")
iris_md   = c.color("#48108e", "iris_md")
iris_lt   = c.color("#7c2fd8", "iris_lt")

pupil     = c.color("#06030d", "pupil")
glow1     = c.color("#a85cff", "glow1")
glow2     = c.color("#e8c9ff", "glow2")

shadow_a  = c.color("#120a1e2e", "shadow_a")
shadow_b  = c.color("#120a1e5c", "shadow_b")

# ---------------- soft ground shadow ----------------
shadow_l.ellipse(31, 60, 15, 3, shadow_a)
shadow_l.ellipse(31, 60, 9, 2, shadow_b)

# ---------------- short tentacles ----------------
def tendril(cv, p0, p1, p2, w0, w1, steps=20):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y, w0 + (w1 - w0) * t))
    for x, y, w in pts:
        cv.circle(int(round(x)), int(round(y)), max(0, int(round(w / 2))), body_dk)
    for x, y, w in pts:
        r = int(round(w / 2)) - 1
        if r >= 0:
            cv.circle(int(round(x - 1)), int(round(y)), r, body_md)
    for x, y, w in pts[: int(len(pts) * 0.65)]:
        r = int(round(w / 2)) - 2
        if r >= 0:
            cv.circle(int(round(x - 1)), int(round(y - 1)), r, body_lt)

TENTS = [
    ((15, 34), (11, 39), (10, 44), 5, 1),
    ((21, 39), (18, 45), (19, 50), 6, 1),
    ((27, 42), (26, 48), (23, 53), 6, 1),
    ((33, 42), (35, 49), (33, 54), 7, 1),
    ((39, 40), (42, 46), (40, 51), 6, 1),
    ((44, 35), (48, 41), (49, 45), 5, 1),
]
for p0, p1, p2, w0, w1 in TENTS:
    tendril(tent_l, p0, p1, p2, w0, w1)

# ---------------- orb body ----------------
orb_l.circle(CX, CY, R, body_dk)
orb_l.circle(CX, CY, R - 1, body_lt)
orb_l.circle(CX + 1, CY + 2, R - 2, body_md)
orb_l.circle(CX + 3, CY + 4, R - 4, body_dk)
# rim light hugging the upper-left shoulder, fading at both ends
for a in range(185, 290):
    rad = math.radians(a)
    t = min(1.0, min(a - 185, 289 - a) / 22.0)
    col = body_hi if t > 0.45 else body_lt
    for rr in (R, R - 1):
        orb_l.set(int(round(CX + math.cos(rad) * rr)),
                  int(round(CY + math.sin(rad) * rr)), col)
# dark lip along the lower-right rim
for a in range(10, 110):
    rad = math.radians(a)
    for rr in (R, R - 1, R - 2):
        orb_l.set(int(round(CX + math.cos(rad) * rr)),
                  int(round(CY + math.sin(rad) * rr)), body_dk)

# ---------------- sclera ----------------
orb_l.circle(CX, CY, 12, sclera_dk)
orb_l.circle(CX, CY + 1, 11, sclera_md)
orb_l.circle(CX, CY + 2, 10, sclera_lt)
orb_l.line(21, 21, 25, 24, sclera_dk)
orb_l.line(41, 29, 37, 27, sclera_dk)
orb_l.line(30, 35, 31, 32, sclera_dk)

# ---------------- iris ----------------
orb_l.circle(CX, CY, 8, iris_dk)
orb_l.circle(CX, CY, 7, iris_md)
for a in range(0, 360, 20):
    rad = math.radians(a)
    orb_l.line(int(round(CX + math.cos(rad) * 4)), int(round(CY + math.sin(rad) * 4)),
               int(round(CX + math.cos(rad) * 7)), int(round(CY + math.sin(rad) * 7)), iris_lt)
orb_l.circle(CX, CY, 8, iris_dk, fill=False)

# ---------------- pupil with faint inner glow ----------------
orb_l.circle(CX, CY, 5, glow1)
orb_l.circle(CX, CY, 4, iris_dk)
orb_l.circle(CX, CY, 3, pupil)
# bloom rising from the pupil core
orb_l.set(CX, CY - 1, glow1)
orb_l.set(CX, CY + 1, glow1)
orb_l.set(CX - 1, CY, glow1)
orb_l.set(CX + 1, CY, glow1)
orb_l.set(CX, CY, glow2)

# ---------------- specular highlight ----------------
orb_l.rect(23, 18, 3, 2, sclera_lt)
orb_l.set(25, 17, sclera_lt)
orb_l.set(22, 20, sclera_md)

result = flatten([shadow_l, tent_l, orb_l], name="void-eye")
view(result)
print(result.stats_text())
finish(result)
