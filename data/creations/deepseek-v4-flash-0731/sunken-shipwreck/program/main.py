import math, random
from pixelbench_api import new_canvas, save, finish

c = new_canvas(64, 64)

# ---- palette ----
WAT   = ["#146FA0", "#11628F", "#0E547E", "#0B466D",
        "#09395C", "#072B4B", "#051E3A", "#03101F"]
RAY   = "#2E8FC0"
SAND_D = "#7D5F3D"; SAND_M = "#A58050"; SAND_L = "#C8A067"
WOOD_D = "#3F2410"; WOOD_M = "#663C1D"; WOOD_L = "#8C5327"; WOOD_HL = "#B06E34"
RUST_D = "#6F451F"; RUST = "#96602C"; RUST_L = "#BF7E3E"
COR_D = "#7F2B42"; COR = "#B04860"; COR_L = "#DD7F90"
KELP_D = "#0E4A26"; KELP = "#1D6D38"; KELP_L = "#34914F"
F_O = "#E89A3A"; F_L = "#FFD06E"; F_D = "#9C5C20"; EYE = "#1A0F08"
BUB = "#9FD4E8"; BUB_H = "#D8F2FB"
INT = "#140803"; ROCK = "#5A4A5E"; ROCKD = "#453A4E"; ROPE = "#C9A878"; PAT = "#3E7F66"

def arc_points(x0, y0, x1, y1, rise, n=24):
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append((round(x0 + (x1 - x0) * t),
                    round(y0 + (y1 - y0) * t - rise * math.sin(math.pi * t))))
    return pts

# 1) water bands
for i, col in enumerate(WAT):
    c.rect(0, i * 8, 64, 8, col)

# 2) light shafts
for (x0, x1) in [(3, 24), (22, 42), (40, 58), (50, 62)]:
    for j in range(3):
        c.line(x0 + j, -1, x1 + j, 44, RAY)

# 3) drifting particles
random.seed(3)
for _ in range(46):
    x = random.randint(0, 63); y = random.randint(2, 40)
    c.set(x, y, random.choice([BUB_H, "#1E80B4", RAY, RAY]))

# 4) hull silhouette
surf = arc_points(2, 54, 62, 54, 29, 24)
hull = surf + [(62, 58), (2, 58)]
c.poly(hull, WOOD_M)
c.poly(hull, WOOD_D, fill=False)

# planks
for d in (23, 17, 11, 5):
    c.poly(arc_points(3, 53, 61, 53, 29 - d, 20), WOOD_D, fill=False)
for d in (20, 14, 8):
    c.poly(arc_points(3, 53, 61, 53, 29 - d, 20), WOOD_L, fill=False)

# broken section: dark hole with exposed ribs
up = arc_points(25, 50, 45, 50, 23, 16)
c.poly(up + [(45, 50), (25, 50)], INT)
for x0 in (28, 32, 36):
    pts = arc_points(x0 - 2, 50, x0 + 2, 50, 21, 8)
    c.poly(pts + [(x0 + 2, 50), (x0 - 2, 50)], WOOD_D)
c.line(28, 36, 28, 42, WOOD_L)
c.line(32, 33, 32, 44, WOOD_L)
c.line(36, 39, 36, 46, WOOD_L)

# portholes with rust
c.circle(16, 41, 2, RUST_D)
c.circle(16, 41, 2, RUST, fill=False)
c.set(16, 40, RUST_L)
c.circle(23, 44, 2, RUST_D)
c.circle(23, 44, 2, RUST, fill=False)
c.set(23, 43, RUST_L)

# corroded rust patch
c.ellipse(50, 40, 5, 7, RUST)
c.ellipse(50, 40, 3, 5, RUST_L)
c.ellipse(47, 38, 1, 2, RUST_L)
c.ellipse(54, 45, 2, 3, PAT)
c.line(51, 45, 53, 51, RUST)
c.line(47, 46, 45, 52, RUST_D)

# 5) sandy sea floor (buries the hull)
for x in range(64):
    top = 50 + round(3 * math.sin(x * 0.55) + 2 * math.sin(x * 0.23 + 1.3))
    if 5 <= x <= 19:
        top -= round(5 * math.sin(math.pi * (x - 5) / 14))
    if 43 <= x <= 60:
        top -= round(4 * math.sin(math.pi * (x - 43) / 17))
    c.rect(x, top, 1, 64 - top, SAND_M)
    c.set(x, top, SAND_L)
c.rect(0, 58, 64, 6, SAND_D)
for x in range(0, 64, 2):
    c.set(x, 57, SAND_L)
random.seed(11)
for _ in range(70):
    x = random.randint(0, 63); y = random.randint(50, 63)
    c.set(x, y, SAND_L if random.random() < 0.5 else SAND_D)

# 6) broken mast & yard
c.poly([(29, 6), (33, 5), (34, 25), (31, 29), (30, 29), (28, 27)], WOOD_M)
c.poly([(29, 6), (33, 5), (34, 25), (31, 29), (30, 29), (28, 27)], WOOD_D, fill=False)
c.line(30, 9, 31, 24, WOOD_L)
c.line(31, 4, 32, 6, WOOD_HL)
c.poly([(20, 14), (42, 9), (41, 12), (19, 17)], WOOD_M)
c.line(20, 14, 42, 9, WOOD_D)
c.line(19, 16, 17, 23, ROPE)
c.line(38, 11, 35, 19, ROPE)
c.line(21, 15, 24, 22, ROPE)

# 7) rock + coral
rock_pts = [(3, 48), (8, 43), (14, 46), (16, 51), (13, 57), (4, 56)]
c.poly(rock_pts, ROCK)
c.poly(rock_pts, ROCKD, fill=False)
c.circle(8, 41, 3, COR)
c.set(7, 40, COR_L); c.set(9, 39, COR_L); c.set(8, 43, COR_D)
c.line(6, 38, 4, 34, COR); c.set(6, 36, COR_L)
c.circle(12, 44, 2, COR)
c.set(12, 43, COR_L)
c.circle(52, 46, 3, COR)
c.set(52, 45, COR_L); c.set(53, 44, COR_L); c.set(50, 46, COR_D)
c.circle(57, 48, 2, COR)
c.set(57, 47, COR_L)

# 8) seaweed strands
def strand(cx, y0, h, sway, col, col2=None):
    pts = [(round(cx + sway * math.sin(t * 2.6)), round(y0 - h * t)) for t in [i / 9 for i in range(10)]]
    c.poly(pts, col, fill=False)
    if col2:
        c.poly([(p[0] + 1, p[1]) for p in pts], col2, fill=False)

strand(6, 57, 16, 3, KELP, KELP_L)
strand(10, 57, 20, -2, KELP)
strand(13, 57, 13, 3, KELP_L)
strand(49, 57, 18, -3, KELP)
strand(54, 57, 23, 2, KELP, KELP_L)
strand(58, 57, 14, -2, KELP_L)

# 9) school of fish (facing left)
def fish(x, y):
    c.set(x, y, F_O); c.set(x + 1, y, EYE); c.set(x + 2, y, F_O)
    c.set(x + 3, y, F_D); c.set(x + 1, y + 1, F_L)

school = [(34, 12), (30, 13), (26, 14), (22, 15), (18, 16), (14, 17),
         (38, 11), (32, 11), (24, 12), (20, 13), (29, 17), (35, 15),
         (33, 9), (40, 15), (27, 10), (31, 16), (16, 12), (36, 8)]
for p in school:
    fish(*p)
# stray fish near the wreck
for p in [(54, 24), (58, 27), (61, 30), (4, 24)]:
    fish(*p)

# surface shimmer on the top band
for (sx, sy) in [(6, 1), (14, 1), (22, 2), (31, 1), (39, 2), (47, 1), (55, 1), (60, 2)]:
    c.set(sx, sy, BUB_H)

# 10) bubbles
for (bx, by) in [(27, 20), (25, 14), (22, 9), (40, 18), (38, 12), (45, 16),
                (14, 11), (24, 7), (30, 5), (46, 20)]:
    c.set(bx, by, BUB); c.set(bx + 1, by + 1, BUB_H)

# 11) foreground kelp blades, bottom corners
c.poly([(0, 63), (3, 51), (7, 56), (2, 63)], KELP_D)
c.poly([(63, 63), (59, 49), (56, 57), (61, 63)], KELP_D)

print(c.stats_text())

finish(c)
