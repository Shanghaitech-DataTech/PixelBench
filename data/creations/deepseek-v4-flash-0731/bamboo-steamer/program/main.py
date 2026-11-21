import math
from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="steamer")

# ---- palette ----
BAM   = c.color('#d9a94f')   # bamboo wood
BAM_L = c.color('#ecc98f')   # light bamboo
BAM_D = c.color('#a97b33')   # dark bamboo
BAM_X = c.color('#7d5a20')   # weave
IN    = c.color('#6b4420')   # dark interior floor
IN_D  = c.color('#4a2c10')   # floor slat grooves
D     = c.color('#fbf4e6')   # dumpling white
DS    = c.color('#e6d7bc')   # dumpling shade
DD    = c.color('#c4a87e')   # dumpling crease
ST    = c.color('#f3f8fa')   # steam light
ST2   = c.color('#cfdde2')   # steam soft

# ---- steamer basket (top view) ----
c.circle(16, 18, 13, BAM)              # outer bamboo ring
c.circle(16, 18, 11, BAM_L)            # rim band
c.circle(16, 18, 11, BAM_D, fill=False)  # groove
c.circle(16, 18, 9, IN)                # interior floor

# woven dashes on the rim band
for deg in range(0, 360, 30):
    a = math.radians(deg)
    x0 = 16 + 10.2 * math.cos(a)
    y0 = 18 + 10.2 * math.sin(a)
    tx, ty = -math.sin(a), math.cos(a)
    for t in (-0.7, 0.7):
        c.set(int(round(x0 + tx * t)), int(round(y0 + ty * t)), BAM_X)

# slat grooves across the floor
for x in range(8, 25):
    c.set(x, 20, IN_D)
for x in range(10, 23):
    c.set(x, 24, IN_D)

# ---- three dumplings in the opening ----
def dumpling(cx, cy):
    c.circle(cx + 1, cy + 1, 3, IN_D)          # shadow
    c.circle(cx, cy, 3, D)                     # white body
    c.circle(cx, cy, 3, DD, fill=False)         # pleated rim
    c.set(cx - 1, cy, DD)                       # folds
    c.set(cx + 1, cy, DD)
    c.set(cx, cy + 1, DS)                        # under-shade

dumpling(9, 13)
dumpling(10, 17)
dumpling(11, 21)

# soft shadow the lid casts onto the floor along its left edge
for yy in range(13, 24):
    c.set(12, yy, IN_D)

# ---- lid: slid toward the upper right, left opening exposed ----
c.circle(21, 15, 9, BAM_L)
c.circle(21, 15, 9, BAM_D, fill=False)

for deg in range(0, 360, 45):
    a = math.radians(deg)
    x0 = 21 + 6.8 * math.cos(a)
    y0 = 15 + 6.8 * math.sin(a)
    tx, ty = -math.sin(a), math.cos(a)
    for t in (-0.7, 0.7):
        c.set(int(round(x0 + tx * t)), int(round(y0 + ty * t)), BAM_X)

# lid knob
c.circle(21, 15, 2, BAM_D)
c.set(20, 14, BAM_L)
c.set(22, 16, BAM_X)

# ---- small steam rising from the open side ----
for x, y in [(5, 9), (6, 9), (4, 8), (6, 8), (7, 7), (5, 6), (6, 6), (7, 6),
             (4, 5), (5, 5), (6, 4), (4, 3), (5, 3), (6, 2)]:
    c.set(x, y, ST)
for x, y in [(4, 9), (6, 8), (6, 7), (5, 6), (4, 5), (6, 4), (6, 3), (5, 2)]:
    c.set(x, y, ST2)

print(c.stats_text())
print(c.matrix_text())
finish(c)
