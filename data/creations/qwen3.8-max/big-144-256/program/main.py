from pixelbench_api import *

output = input_canvas.copy(name="output")

# ---- palette ----
VINE_D  = output.color('#1d4a2a', 'vine_dark')
VINE    = output.color('#2e6b3c', 'vine_green')
VINE_L  = output.color('#55913f', 'vine_light')
LEAF    = output.color('#3f7f46', 'leaf')
CLOAK_D = output.color('#221a30', 'cloak_dark')
CLOAK   = output.color('#372a4d', 'cloak_mid')
CLOAK_L = output.color('#544070', 'cloak_light')
BOOT    = output.color('#1a1420', 'boot')
WOOD    = output.color('#6b4a2a', 'staff_wood')
SKIN    = output.color('#d8a06a', 'skin')
CORE    = output.color('#fff6c8', 'glow_core')

def vine(c, pts):
    for i in range(len(pts) - 1):
        c.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], VINE_D)

def leaf(c, x, y, dx):
    c.set(x, y, LEAF)
    c.set(x + dx, y, VINE_L)
    c.set(x, y + 1, LEAF)

def ivy_patch(c, x0, y0, x1, y1, p, seed):
    import random
    rnd = random.Random(seed)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            r = rnd.random()
            if r < p:
                t = rnd.random()
                c.set(x, y, VINE if t < 0.45 else (LEAF if t < 0.8 else VINE_L))
            elif r < p + 0.15:
                c.set(x, y, VINE_D)
    n = max(2, (x1 - x0) * (y1 - y0) // 40)
    for i in range(n):
        cx = rnd.randint(x0 + 1, x1 - 2)
        cy = rnd.randint(y0 + 1, y1 - 2)
        c.rect(cx, cy, 2, 2, LEAF)
        c.set(cx + rnd.randint(0, 1), cy - 1, VINE_L)

# ---- ivy patches covering parts of the tower walls ----
ivy_patch(output, 52, 96, 60, 142, 0.5, 11)    # left of upper shaft slit
ivy_patch(output, 65, 172, 70, 210, 0.45, 22)  # lower wall right of archway
ivy_patch(output, 87, 178, 93, 208, 0.35, 33)  # lower wall right of window
ivy_patch(output, 68, 104, 74, 140, 0.35, 44)  # right of upper shaft
ivy_patch(output, 48, 159, 86, 165, 0.3, 55)   # shoulder band above the arch

# ---- climbing vines ----
# vine 1: climbs left side of tower shaft
vine(output, [(57,152),(55,140),(58,128),(56,116),(59,104),(57,92),(60,80),(58,68)])
for (x, y, dx) in [(54,146,-1),(58,138,1),(54,126,-1),(59,118,1),
                   (55,108,-1),(60,98,1),(56,88,-1),(59,76,1)]:
    leaf(output, x, y, dx)
output.line(56,120,50,114, VINE_D)
leaf(output, 48,112,-1); leaf(output, 50,110,1)
output.line(59,100,64,94, VINE_D)
leaf(output, 64,92,1); leaf(output, 65,95,1)

# vine 2: lower wall, between arch and window
vine(output, [(70,214),(69,204),(71,196),(70,186),(72,178)])
for (x, y, dx) in [(68,210,-1),(71,200,1),(68,192,-1),(72,182,1)]:
    leaf(output, x, y, dx)

# vine 3: horizontal creeper along the band above the arch, with droppers
vine(output, [(50,163),(58,161),(66,163),(74,161),(82,163),(86,162)])
output.line(54,162,54,170, VINE_D)
output.line(66,163,66,169, VINE_D)
output.line(78,162,78,172, VINE_D)
for (x, y, dx) in [(52,160,1),(60,164,-1),(70,160,1),(80,164,-1),
                   (53,169,-1),(65,168,1),(77,171,1)]:
    leaf(output, x, y, dx)

# vine 4: right edge of tower shaft
vine(output, [(84,150),(86,138),(84,126),(86,114)])
for (x, y, dx) in [(83,144,-1),(86,132,1),(83,120,-1)]:
    leaf(output, x, y, dx)

# ---- mage layer (back view, walking into the archway) ----
mage = new_canvas(144, 256, name='mage')
# hood
mage.circle(57, 196, 3, CLOAK)
mage.set(57, 192, CLOAK); mage.set(56, 193, CLOAK); mage.set(58, 193, CLOAK)
mage.line(54, 199, 60, 199, CLOAK_D)          # hood rim shadow over shoulders
# cloak body flaring to hem
mage.poly([(54,200),(60,200),(62,206),(62,210),(52,210),(52,206)], CLOAK)
mage.line(57, 201, 57, 209, CLOAK_D)          # back fold
mage.line(52, 210, 62, 210, CLOAK_D)          # hem trim
mage.line(53, 202, 52, 209, CLOAK_D)          # shadow side
mage.line(60, 201, 62, 207, CLOAK_L)          # rim light from staff
mage.set(60, 195, CLOAK_L); mage.set(60, 196, CLOAK_L); mage.set(59, 194, CLOAK_L)
# sleeve reaching to staff + hand
mage.poly([(60,204),(64,206),(64,208),(60,207)], CLOAK)
mage.set(64, 207, SKIN)
# boots: left planted, right lifted mid-step
mage.rect(55, 211, 2, 2, BOOT)
mage.rect(59, 210, 2, 2, BOOT)
# soft shadow on the threshold step
mage.rect(53, 213, 12, 1, (10, 8, 14, 110))
# staff
mage.line(64, 195, 64, 213, WOOD)
mage.set(63, 195, WOOD); mage.set(65, 195, WOOD)

# ---- glow layer ----
glow = new_canvas(144, 256, name='glow')
glow.circle(64, 192, 4, (255, 214, 102, 70))
glow.circle(64, 192, 3, (255, 220, 120, 110))
glow.circle(64, 192, 2, (255, 232, 150, 180))
glow.circle(64, 192, 1, CORE)
for (sx, sy) in [(64,186),(64,198),(58,192),(70,192)]:
    glow.set(sx, sy, (255, 230, 150, 120))
glow.ellipse(64, 214, 4, 1, (255, 214, 102, 60))
for (sx, sy) in [(66,200),(66,205),(65,210)]:
    glow.set(sx, sy, (255, 214, 102, 80))

result = flatten([output, mage, glow], name='result')
print(view(result, size=(512, 512)))
sel = result.select(40, 155, 64, 75)
print(view(sel.preview(), scale=8, margin=0))
finish(result)
