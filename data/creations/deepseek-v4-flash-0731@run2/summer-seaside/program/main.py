import math
from pixelbench_api import new_canvas, finish

W = H = 128
c = new_canvas(W, H, name="summer-seaside")
SUNX = 104
SUNY = 16


def band(y0, y1, color):
    c.rect(0, y0, W, y1 - y0 + 1, color)


# ---------- Sky ----------
sky_edges = [0, 10, 20, 30, 40, 50, 58]
sky_cols = ["#1E88E5", "#3FA2F2", "#64B5F6", "#8FCBFA", "#B7E1FC", "#D9EDFE"]
for i in range(len(sky_cols)):
    band(sky_edges[i], sky_edges[i + 1] - 1, sky_cols[i])

# Bright sun with soft glow
c.circle(SUNX, SUNY, 12, "#FFF6B8")
c.circle(SUNX, SUNY, 8, "#FFEB3B")
c.circle(SUNX, SUNY, 4, "#FFF9C4")


def cloud(cx, cy, s):
    c.ellipse(cx, cy, int(10 * s), int(5 * s), "#FFFFFF")
    c.ellipse(cx - int(8 * s), cy + int(1 * s), int(6 * s), int(4 * s), "#FFFFFF")
    c.ellipse(cx + int(8 * s), cy + int(1 * s), int(6 * s), int(4 * s), "#FFFFFF")
    c.ellipse(cx, cy + int(3 * s), int(9 * s), int(2 * s), "#EAF4FF")


cloud(24, 18, 1.4)
cloud(58, 30, 1.0)
cloud(76, 12, 1.1)
cloud(100, 34, 0.8)

# Gulls
c.path("M 48 43 Q 52 39 56 43 Q 60 39 64 43", "#FFFFFF", fill=False)
c.path("M 72 37 Q 75 34 78 37 Q 81 34 84 37", "#FFFFFF", fill=False)

# ---------- Sea (deep blue at horizon -> teal near shore) ----------
sea_edges = [58, 61, 64, 67, 70, 73, 76, 79, 82, 86]
sea_cols = ["#0E4D92", "#13579F", "#1A6BA8", "#1F7FB0", "#2694B8",
           "#2BA6BC", "#2FB8C0", "#33C7C0", "#3AD6BE"]
for i in range(len(sea_cols)):
    band(sea_edges[i], sea_edges[i + 1] - 1, sea_cols[i])

# Sun glitter path on the water
for (y, ln) in [(60, 4), (63, 6), (66, 8), (69, 10), (72, 12), (75, 12),
               (78, 11), (81, 9), (84, 7)]:
    x0 = SUNX - ln // 2
    c.line(x0, y, x0 + ln - 1, y, "#FFF6C9")

# White wave crests
for base in (64, 71, 78):
    parts = []
    for x0 in range(0, 112, 16):
        parts.append("M %d %d Q %d %d %d %d" % (x0, base, x0 + 8, base - 3, x0 + 16, base))
    c.path(" ".join(parts), "#FFFFFF", fill=False)

# Small white sailboat far out
c.line(19, 58, 19, 66, "#8D6E63")
c.poly([(17, 59), (24, 65), (17, 65)], "#FFFFFF")
c.poly([(21, 61), (13, 65), (21, 65)], "#FFFFFF")
c.rect(14, 65, 11, 2, "#FFFFFF")
c.line(14, 67, 24, 67, "#C9E4EC")

# ---------- Sand ----------
band(86, 89, "#ECCC86")   # wet sand
band(90, 127, "#F6DA8F")  # dry golden sand

# Shore foam
for y in range(86, 93):
    for x in range(0, 128):
        if (x * 7 + y * 13) % 19 < 4:
            c.set(x, y, "#FFFFFF")
for x0 in range(0, 118, 10):
    c.path("M %d 90 Q %d 87 %d 90" % (x0, x0 + 5, x0 + 10), "#FFFFFF", fill=False)

# Sand texture
for y in range(94, 126, 3):
    for x in range(2, 128, 7):
        if (x * 13 + y * 7) % 11 < 2:
            c.set(x, y, "#FBE9A8")
for y in range(96, 125, 5):
    for x in range(4, 128, 11):
        if (x * 5 + y * 3) % 13 < 2:
            c.set(x, y, "#E7C57E")

# ---------- Beach umbrella ----------
c.ellipse(46, 109, 18, 4, "#E4C07C")   # shadow on sand
c.rect(44, 95, 3, 27, "#9C6B43")       # pole
cx_, cy_, r = 46, 101, 15
c.path("M %d %d A %d %d 0 0 1 %d %d Z" % (cx_ - r, cy_, r, r, cx_ + r, cy_), "#E53935")
n = 8
cols = ["#E53935", "#FFFFFF"]
for k in range(n):
    a1 = 180 - 22.5 * k
    a2 = 180 - 22.5 * (k + 1)
    pts = [(cx_, cy_)]
    for a in (a1, a2):
        rad = math.radians(a)
        pts.append((int(cx_ + r * math.cos(rad)), int(cy_ - r * math.sin(rad))))
    c.poly(pts, cols[k % 2])
c.circle(cx_, cy_ - r, 1, "#E53935")

# ---------- Striped towel ----------
c.ellipse(86, 121, 16, 3, "#E3BF7B")   # towel shadow
c.rect(72, 101, 30, 16, "#FFFFFF")
for dy, h, col in [(101, 4, "#FF7043"), (105, 3, "#FFFFFF"), (108, 4, "#4FC3F7"),
                 (112, 3, "#FFD54F"), (115, 2, "#FFFFFF")]:
    c.rect(72, dy, 30, h, col)

# ---------- Flip-flops ----------
def flipflop(x, y):
    c.ellipse(x, y, 5, 3, "#26C6DA")
    c.ellipse(x, y - 1, 4, 2, "#18B2C9")
    c.line(x - 4, y - 1, x, y - 3, "#FFFFFF")
    c.line(x + 4, y - 1, x, y - 3, "#FFFFFF")
    c.line(x, y - 3, x, y + 1, "#FFFFFF")


flipflop(53, 114)
flipflop(64, 117)

# ---------- Little shell ----------
c.poly([(19, 124), (26, 124), (22, 115)], "#FBE7DC")
c.line(22, 117, 19, 124, "#EFC9B8")
c.line(22, 117, 23, 124, "#E9BFAE")

print(c.stats_text())
print("palette size:", len(c.palette()))
finish(c)
