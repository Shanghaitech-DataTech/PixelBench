W, H = 144, 256

base = input_canvas.copy(name="base")

# ---------------- palette ----------------
C_STEM   = base.color("#2b5230")
C_STEMD  = base.color("#1b3822")
C_LEAF   = [base.color("#3f7a3a"), base.color("#5a9a4b"),
            base.color("#7cb757"), base.color("#28512e")]

M_CLOAK  = base.color("#33265c")
M_CLOAKD = base.color("#1f1740")
M_CLOAKL = base.color("#4b3a82")
M_RIM    = base.color("#93dcbc")
M_HEMD   = base.color("#191234")
M_BOOT   = base.color("#140f26")
M_HAND   = base.color("#c9a07a")
S_WOOD   = base.color("#6f4d2f")
S_WOODD  = base.color("#45311d")
O_CORE   = base.color("#f4fffa")
O_MID    = base.color("#a9ffda")
O_SPK    = base.color("#daffec")
OUT_COL  = base.color("#0d0a18")

# ================= VINES =================
vines = new_canvas(W, H, name="vines")

def _dense(pts):
    d = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i + 1]
        n = max(abs(x1 - x0), abs(y1 - y0), 1)
        for t in range(n + 1):
            x = int(round(x0 + (x1 - x0) * t / n))
            y = int(round(y0 + (y1 - y0) * t / n))
            if not d or d[-1] != (x, y):
                d.append((x, y))
    return d

def leaf(m, x, y, dx, dy, col):
    lx, ly = x + dx, y + dy
    m.line(x, y, lx, ly, col)
    m.ellipse(lx, ly, 1, 1, col)

def draw_vine(m, pts, leaf_step=3):
    d = _dense(pts)
    for i, (x, y) in enumerate(d):
        m.set(x, y, C_STEM)
        if i % 2 == 0:
            m.set(x + 1, y, C_STEMD)
    k = 0
    for i, (x, y) in enumerate(d):
        if i % leaf_step:
            continue
        k += 1
        side = 1 if k % 2 else -1
        col = C_LEAF[k % 4]
        r = k % 3
        if r == 0:   dx, dy = side, -1
        elif r == 1: dx, dy = side * 2, 0
        else:        dx, dy = side, 1
        leaf(m, x, y, dx, dy, col)

def tendril(m, x, y, col):
    m.line(x, y, x, y - 3, col)
    m.line(x, y - 3, x + 2, y - 5, col)
    m.set(x + 3, y - 4, col)

def leaf_cluster(m, x, y):
    pts = [(-2, 0, 0), (2, -1, 1), (0, -2, 2), (-1, -3, 3),
           (2, -3, 0), (-3, -2, 1), (3, -2, 2), (0, -4, 1)]
    for dx, dy, ci in pts:
        m.ellipse(x + dx, y + dy, 1, 1, C_LEAF[ci])

VA = [(46,150),(45,138),(47,126),(45,114),(46,102),(44,90),(46,78),
      (45,66),(47,54),(45,42),(46,30)]
VB = [(79,150),(81,138),(79,126),(81,114),(80,102),(82,90),(80,78),
      (81,66),(79,54),(81,42),(80,30)]
VC = [(51,92),(56,88),(62,91),(68,87)]
VD = [(52,36),(58,32),(64,35),(70,31)]
B1 = [(45,114),(49,110)]
B2 = [(46,78),(51,74)]
B3 = [(81,114),(77,110)]
B4 = [(80,78),(75,74)]

for route in (VA, VB, VC, VD, B1, B2, B3, B4):
    draw_vine(vines, route)

tendril(vines, 47, 120, C_LEAF[1])
tendril(vines, 80, 96, C_LEAF[2])
tendril(vines, 58, 40, C_LEAF[1])
tendril(vines, 66, 88, C_LEAF[0])
leaf_cluster(vines, 46, 151)
leaf_cluster(vines, 79, 151)

# ================= GLOW =================
glow = new_canvas(W, H, name="glow")

ORB_X, ORB_Y = 73, 100
for r, rgba in [(22,(80,235,165,8)),(18,(95,242,175,13)),(15,(110,248,185,20)),
                (12,(130,252,198,32)),(9,(155,255,212,50)),(7,(185,255,226,74)),
                (5,(215,255,240,105)),(3,(240,255,250,150))]:
    glow.circle(ORB_X, ORB_Y, r, rgba)

# light spilling into the archway behind the mage
for rx, ry, a in [(13,17,8),(9,13,15),(6,9,24),(3,6,36)]:
    glow.ellipse(62, 122, rx, ry, (130,255,205,a))

# pool of light on the step at the staff base
glow.ellipse(75, 148, 8, 2, (150,255,210,38))
glow.ellipse(75, 148, 5, 1, (190,255,230,55))

# ================= MAGE =================
mage = new_canvas(W, H, name="mage")

SIL = [
 (112,62,62),(113,61,63),(114,61,63),(115,60,64),(116,60,64),
 (117,59,65),(118,59,65),(119,58,66),(120,58,66),(121,58,66),
 (122,57,67),(123,57,67),(124,56,67),(125,56,68),(126,56,68),
 (127,55,68),(128,55,68),(129,55,69),(130,54,69),(131,54,69),
 (132,54,70),(133,53,70),(134,53,70),(135,53,71),(136,53,71),
 (137,52,71),(138,52,71),(139,52,72),(140,52,72),(141,52,72),
 (142,52,72),(143,53,71),(144,54,70),
]

# staff (drawn first: cloak and hand overlap it)
for t in range(0, 47):
    y = 148 - t
    x = 75 - int(round(t * 2.0 / 46.0))
    mage.set(x - 1, y, S_WOODD)
    mage.set(x,     y, S_WOOD)
    mage.set(x + 1, y, S_WOODD)

# cloak silhouette
for y, x0, x1 in SIL:
    for x in range(x0, x1 + 1):
        mage.set(x, y, M_CLOAK)

# shading
for y, x0, x1 in SIL:
    if y <= 114:
        continue
    if y <= 121:                       # hood
        mage.set(x1, y, M_CLOAKL)
        mage.set(x0, y, M_CLOAKD)
        if y >= 117:
            mage.set(x1, y, M_RIM)
    else:                              # cloak body
        mage.set(x1, y, M_RIM if y <= 140 else M_CLOAKL)
        if x1 - 1 > x0 + 2:
            mage.set(x1 - 1, y, M_CLOAKL)
        mage.set(x0, y, M_CLOAKD)
        if x0 + 1 < x1 - 2:
            mage.set(x0 + 1, y, M_CLOAKD)

# cloth folds
for y in range(125, 143):
    mage.set(58 + (1 if (y % 8) < 4 else 0), y, M_CLOAKD)
for y in range(128, 142):
    mage.set(64 + (1 if (y % 7) < 3 else 0), y, M_CLOAKD)

# hem
for y in (143, 144):
    for yy, x0, x1 in SIL:
        if yy == y:
            for x in range(x0, x1 + 1):
                mage.set(x, y, M_HEMD)

# boots (left planted, right lifted mid-stride)
mage.rect(55, 145, 5, 3, M_BOOT)
mage.rect(63, 145, 5, 2, M_BOOT)

# sleeve reaching for the staff + hand
mage.line(65, 125, 71, 129, M_CLOAK)
mage.line(65, 126, 72, 130, M_CLOAKD)
mage.rect(73, 129, 2, 2, M_HAND)

mage.outline(OUT_COL)

# restore the orb-lit rim after outlining
for y, x0, x1 in SIL:
    if 117 <= y <= 140:
        mage.set(x1, y, M_RIM)

# ================= ORB =================
orb = new_canvas(W, H, name="orb")
orb.circle(ORB_X, ORB_Y, 2, O_MID)
orb.circle(ORB_X, ORB_Y, 1, O_CORE)
orb.set(ORB_X, ORB_Y - 4, O_SPK)
orb.set(ORB_X, ORB_Y + 4, O_SPK)
orb.set(ORB_X - 4, ORB_Y, O_SPK)
orb.set(ORB_X + 4, ORB_Y, O_SPK)

result = flatten([base, vines, glow, mage, orb], name="output")

print(result.stats_text())
finish(result)
