from pixelbench_api import *
import math

c = new_canvas(32, 32, name="steamer")

bl  = c.color("#F0DCA8", "bamboo_light")
bm  = c.color("#D6AC5F", "bamboo_mid")
bd  = c.color("#B9883B", "bamboo_dark")
bs  = c.color("#8F6426", "bamboo_shadow")
inr = c.color("#5F3D14", "interior")
ind = c.color("#3A2309", "inner_dark")
dw  = c.color("#FBF6EA", "dumpling_white")
dc  = c.color("#E3D6BC", "dumpling_shade")
dp  = c.color("#C9B187", "pleat")
st  = c.color((235, 243, 252, 190), "steam")
st2 = c.color((235, 243, 252, 110), "steam2")

# ---- steamer body: vertical bamboo slats ----
for x in range(4, 29):
    dx = abs(x - 16) / 12.0
    if dx > 1:
        continue
    half = int(8 * math.sqrt(max(0.0, 1.0 - dx * dx)))
    if half <= 0:
        c.set(x, 21, bl)
        continue
    col = bl if (x % 2 == 0) else bm
    c.line(x, 21 - half, x, 21 + half, col)

c.ellipse(16, 21, 12, 8, bs, fill=False)      # body silhouette

for y in (24, 27):                            # binding rings
    half = math.sqrt(max(0.0, 1.0 - ((y - 21) / 8.0) ** 2)) * 12.0
    if half > 0:
        c.line(int(16 - half), y, int(16 + half), y, bd)

# ---- opening / interior ----
c.ellipse(16, 18, 9, 5, bs, fill=False)      # rim edge dark
c.ellipse(16, 18, 9, 5, inr)                 # interior wall
c.ellipse(16, 20, 6, 2, ind)                 # deep bottom

# ---- three clearly separated dumplings in the visible opening ----
def dumpling(cx, cy):
    c.circle(cx, cy, 2, dw)                    # white body
    c.ellipse(cx, cy + 1, 2, 1, dc)            # lower shading
    c.set(cx, cy + 2, ind)                     # contact shadow
    c.set(cx - 1, cy - 1, dp)                  # top stitch
    c.set(cx + 1, cy - 1, dp)
    c.set(cx, cy - 1, dc)
    c.set(cx, cy - 2, dp)
    c.set(cx, cy, dw)                          # centre light

dumpling(21, 16)
dumpling(18, 21)
dumpling(24, 18)

# ---- lid: round bamboo lid slid to the left, partially open ----
c.ellipse(10, 18, 7, 4, bs)                    # soft shadow behind lid
c.ellipse(10, 16, 7, 5, bd)                    # rim
c.ellipse(10, 15, 6, 4, bm)                    # side band
c.ellipse(9, 15, 5, 3, bl)                     # woven top
c.ellipse(9, 15, 5, 3, bs, fill=False)         # weave edge
# woven dot pattern
for (wx, wy) in [(8,14),(11,14),(14,15),(7,15),(10,16),(13,16),(9,13),(12,13),(8,16),(11,17),(14,17)]:
    c.set(wx, wy, bm)
# knob
c.circle(9, 10, 2, bd)
c.circle(9, 10, 1, bl)
c.set(8, 9, bs)

# ---- steam rising from the open right side ----
for (sx, sy) in [(19,14),(20,13),(21,13),(22,12),(23,12),(24,11),(25,10),(25,9),
                 (24,8),(23,7),(22,7),(21,8),(20,9),(19,11),(18,12),(17,13),
                 (23,9),(22,10),(24,9),(21,5),(22,4)]:
    c.set(sx, sy, st)
for (sx, sy) in [(18,13),(19,12),(20,11),(21,11),(22,9),(23,8),(24,10),(25,11),
                 (22,6),(23,6),(24,7),(21,7),(20,8),(19,10),(18,11),(17,12),
                 (21,4),(23,4),(22,3),(20,5)]:
    c.set(sx, sy, st2)

print(c.stats_text())
print(c.matrix_text())

finish(c)
