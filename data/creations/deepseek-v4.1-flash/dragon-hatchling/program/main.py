import math

# ---------------- palette ----------------
INK       = '#110b15'
BODY_D    = '#1c5440'
BODY_M    = '#2f7f5c'
BODY_L    = '#4aa87a'
BODY_H    = '#7ed7a4'
FARBODY   = '#245f46'
MEMB_D    = '#3b8c66'
MEMB_M    = '#69bd91'
MEMB_L    = '#8fd7ad'
FARMEMB   = '#1c4c39'
FARMEMB_D = '#143a2b'
BELLY_D   = '#b39a6d'
BELLY_M   = '#e2d5a4'
BELLY_L   = '#f6efcd'
HORN_D    = '#8d6a34'
HORN_M    = '#d4a94f'
HORN_L    = '#f4dd93'
CLAW      = '#f8f2dd'
MOUTH     = '#3d1120'
TONGUE    = '#b13a55'
TONGUE_L  = '#dc6a80'
TOOTH     = '#f8f3e6'
EYE       = '#ffcf3d'
EYE_D     = '#c8890f'
PUPIL     = '#1a0d16'
NOSTRIL   = '#123024'

W = H = 64
c = new_canvas(W, H, background=None, name="dragon")


def limb(cv, pts, radii, colour, steps=None):
    n = len(pts) - 1
    if steps is None:
        L = sum(math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(n))
        steps = max(int(L * 3), 10)
    for i in range(steps + 1):
        t = i / steps * n
        k = min(int(t), n - 1)
        u = t - k
        x = pts[k][0] + (pts[k + 1][0] - pts[k][0]) * u
        y = pts[k][1] + (pts[k + 1][1] - pts[k][1]) * u
        r = radii[k] + (radii[k + 1] - radii[k]) * u
        cv.circle(int(round(x)), int(round(y)), int(round(r)), colour)


def part(name, fn, post=None):
    p = new_canvas(W, H, background=None, name=name)
    fn(p)
    p.outline(INK)
    if post:
        post(p)
    return p


# ================= FAR WING =================
def _farwing(p):
    p.path("M28 29 L34 11 L45 4 Q42 9 48 12 Q42 16 43 19 Q38 21 35 23 L30 27 Z",
           FARMEMB, fill=True)
    p.line(28, 29, 34, 11, FARMEMB_D)
    p.line(34, 11, 45, 4, FARMEMB_D)
    p.line(34, 11, 48, 12, FARMEMB_D)
    p.line(34, 11, 43, 19, FARMEMB_D)
    p.line(34, 11, 35, 23, FARMEMB_D)


farwing = part("farwing", _farwing)

# ================= TAIL =================
def _tail(p):
    limb(p, [(44, 43), (50, 45), (55, 43), (58, 38), (57, 34)],
         [3.2, 2.6, 2.1, 1.6, 1.1], BODY_D)
    # spade
    p.poly([(56, 27), (61, 33), (56, 37), (52, 32)], BODY_D, fill=True)
    p.line(56, 29, 60, 33, BODY_M)
    # dorsal spikes
    p.poly([(46, 40), (48, 36), (49, 41)], BODY_L, fill=True)
    p.poly([(50, 41), (52, 37), (53, 42)], BODY_L, fill=True)


tail = part("tail", _tail)

# ================= FAR HIND LEG =================
def _farleg(p):
    limb(p, [(43, 42), (44, 47), (42, 50)], [3.4, 2.9, 2.5], FARBODY)
    p.poly([(33, 50), (42, 48), (45, 52), (33, 53)], FARBODY, fill=True)


farleg = part("farleg", _farleg)

# ================= NEAR WING =================
def _nearwing(p):
    p.path("M31 32 L37 23 L43 15 L53 7 Q50 12 56 16 Q51 20 51 24 Q46 27 43 29 L37 32 Z",
           MEMB_M, fill=True)
    limb(p, [(31, 32), (37, 23), (43, 15)], [1.5, 1.2, 1.0], MEMB_D)
    p.line(43, 15, 53, 7, MEMB_D)
    p.line(43, 15, 56, 16, MEMB_D)
    p.line(43, 15, 51, 24, MEMB_D)
    p.line(43, 15, 43, 29, MEMB_D)
    p.line(46, 17, 51, 11, MEMB_L)
    p.line(46, 18, 53, 17, MEMB_L)


nearwing = part("nearwing", _nearwing)

# ================= BODY =================
def _body(p):
    p.poly([(20, 20), (23, 24), (30, 33), (27, 38), (18, 28)], BODY_M, fill=True)
    p.poly([(26, 31), (32, 29), (39, 31), (44, 36), (45, 42), (43, 47),
            (37, 49), (30, 47), (26, 42), (24, 36)], BODY_M, fill=True)
    # spine spikes
    p.poly([(20, 21), (22, 17), (24, 23)], BODY_L, fill=True)
    p.poly([(24, 25), (27, 21), (28, 27)], BODY_L, fill=True)
    p.poly([(38, 31), (41, 27), (42, 33)], BODY_L, fill=True)
    # belly
    p.poly([(26, 31), (24, 36), (26, 42), (30, 47), (35, 48), (37, 45),
            (33, 44), (29, 40), (28, 35), (29, 31)], BELLY_M, fill=True)
    # throat
    p.poly([(21, 25), (27, 30), (27, 36), (20, 32)], BELLY_M, fill=True)
    # right-side volume shadow
    p.poly([(40, 31), (44, 36), (45, 42), (43, 47), (41, 46), (43, 41), (42, 36), (38, 32)],
           BODY_D, fill=True)
    # shoulder highlight
    p.poly([(28, 32), (33, 30), (36, 32), (31, 34)], BODY_L, fill=True)
    # belly plates
    for (y, x0, x1) in ((35, 27, 31), (38, 26, 31), (41, 26, 32), (44, 28, 33), (46, 30, 34)):
        p.line(x0, y, x1, y, BELLY_D)
    p.line(27, 34, 31, 34, BELLY_L)
    p.line(26, 37, 31, 37, BELLY_L)
    p.line(26, 40, 32, 40, BELLY_L)


body = part("body", _body)

# ================= NEAR HIND LEG =================
def _nearleg(p):
    limb(p, [(38, 44), (35, 48), (34, 51)], [4.2, 3.4, 2.9], BODY_M)
    # shadow separating leg from belly
    limb(p, [(34, 43), (32, 48), (31, 51)], [1.0, 1.0, 1.0], BODY_D)
    p.poly([(25, 53), (34, 50), (38, 54), (37, 56), (24, 56)], BODY_M, fill=True)
    p.line(26, 52, 34, 50, BODY_L)
    p.line(30, 52, 36, 54, BODY_D)
    p.poly([(24, 53), (26, 55), (23, 55)], CLAW, fill=True)
    p.poly([(27, 54), (29, 56), (26, 56)], CLAW, fill=True)
    p.poly([(31, 54), (33, 56), (30, 56)], CLAW, fill=True)


nearleg = part("nearleg", _nearleg)

# ================= FRONT ARM =================
def _arm(p):
    limb(p, [(27, 37), (24, 42), (22, 44)], [2.6, 2.0, 1.6], BODY_M)
    p.circle(20, 45, 1.6, BODY_M)
    p.line(26, 38, 23, 42, BODY_L)


arm = part("arm", _arm)

# ================= HEAD =================
HEAD_SIL = [(3, 19), (6, 17), (10, 14), (17, 12), (21, 14), (22, 19), (21, 25),
            (18, 31), (13, 35), (5, 34), (4, 30), (5, 27), (3, 24)]
UPPER = [(3, 19), (6, 17), (10, 14), (17, 12), (21, 14), (22, 19), (21, 24),
         (17, 25), (8, 26), (4, 25), (3, 24)]
LOWER = [(4, 30), (16, 26), (18, 30), (13, 34), (5, 34), (3, 31)]


def _head(p):
    p.poly(HEAD_SIL, MOUTH, fill=True)
    p.poly(UPPER, BODY_M, fill=True)
    p.poly(LOWER, BODY_M, fill=True)
    # pale chin edge
    p.poly([(5, 32), (9, 34), (13, 34), (16, 30), (13, 30), (9, 32), (7, 31)], BELLY_M, fill=True)
    # snout top highlight
    p.line(6, 19, 11, 17, BODY_L)
    # horns
    p.poly([(14, 13), (17, 12), (21, 6)], HORN_D, fill=True)
    p.poly([(17, 12), (21, 14), (26, 8)], HORN_M, fill=True)
    p.poly([(21, 20), (25, 19), (22, 25)], HORN_M, fill=True)


def _head_post(p):
    p.ellipse(15, 18, 2.3, 2.0, EYE_D)
    p.ellipse(15, 18, 1.7, 1.5, EYE)
    p.rect(15, 17, 1, 3, PUPIL)
    p.set(14, 17, CLAW)
    p.line(12, 16, 17, 14, BODY_D)
    p.set(5, 21, NOSTRIL)
    p.set(6, 22, NOSTRIL)
    p.line(6, 26, 6, 28, TOOTH)
    p.line(11, 25, 11, 27, TOOTH)
    p.line(9, 29, 9, 28, TOOTH)
    p.ellipse(8, 28, 2.4, 1.0, TONGUE)
    p.line(6, 28, 9, 28, TONGUE_L)
    p.line(19, 13, 24, 9, HORN_L)


head = part("head", _head, _head_post)

# ================= ASSEMBLE =================
for p in (farwing, tail, farleg, nearwing, body, nearleg, arm, head):
    c.blit(p, 0, 0)

for (y, x0, x1) in ():
    c.line(x0, y, x1, y, BELLY_L)
c.set(18, 44, CLAW)
c.set(19, 46, CLAW)

result = c
print(result.stats_text())
print("colors used:", len(result.palette()))
save("dragon-hatchling", result)
finish(result)
