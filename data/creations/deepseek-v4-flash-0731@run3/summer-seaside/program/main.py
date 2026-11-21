import math
from pixelbench_api import new_canvas, save, finish, view

W = H = 128
result = new_canvas(W, H, name="summer_seaside")


def hline(y, col, x0=0, x1=W - 1):
    result.line(x0, y, x1, y, col)


def band(y0, y1, col):
    for y in range(y0, y1 + 1):
        hline(y, col)


# ---------------- SKY ----------------
sky = [
    (0, 5,   "#2E8FE0"),
    (6, 12,  "#3E9DEB"),
    (13, 19, "#50ACF2"),
    (20, 26, "#64BBF6"),
    (27, 33, "#7BC9F8"),
    (34, 40, "#95D6FA"),
    (41, 47, "#B0E2FB"),
]
for y0, y1, col in sky:
    band(y0, y1, col)

# ---------------- SUN (bright, upper right) ----------------
result.circle(102, 15, 14, "#FFF0A0")
result.circle(102, 15, 10, "#FFE66E")
result.circle(102, 15, 6,  "#FFDD3C")

# ---------------- CLOUDS (soft white puffs) ----------------
def puffy(cx, cy, r):
    result.circle(cx, cy + 1, r, "#D9EFFD")   # soft shaded base
    result.circle(cx, cy, r, "#FFFFFF")       # white top

puffy(16, 15, 6)
puffy(25, 12, 8)
puffy(35, 15, 6)
puffy(24, 19, 5)

puffy(68, 30, 6)
puffy(77, 27, 7)
puffy(86, 30, 6)
puffy(73, 33, 4)

puffy(106, 36, 5)
puffy(113, 35, 4)

# ---------------- GULLS ----------------
def gull(x, y):
    result.line(x - 6, y + 3, x - 3, y - 1, "#FFFFFF")
    result.line(x - 3, y - 1, x,     y + 1, "#FFFFFF")
    result.line(x,     y + 1, x + 3, y - 1, "#FFFFFF")
    result.line(x + 3, y - 1, x + 6, y + 3, "#FFFFFF")

gull(28, 32)
gull(60, 20)

# ---------------- SEA (deep at horizon -> teal at shore) ----------------
sea = [
    (48, 48, "#8FD0F0"),
    (49, 55, "#125FB2"),
    (56, 63, "#1873C2"),
    (64, 71, "#1F8AD2"),
    (72, 78, "#28A3DE"),
    (79, 84, "#32BEE4"),
    (85, 86, "#55D8E6"),
]
for y0, y1, col in sea:
    band(y0, y1, col)

# sun sparkle path on the water
spark = [(90, 52, 3), (97, 57, 4), (88, 63, 3), (95, 69, 4), (90, 75, 5), (97, 81, 6), (87, 85, 4)]
for sx, sy, ln in spark:
    hline(sy, "#FFEFAE", sx, sx + ln)

# ---------------- SMALL WHITE SAILBOAT ----------------
result.rect(65, 63, 20, 3, "#8A4A3A")          # hull
result.line(66, 62, 83, 62, "#9C5A44")
result.poly([(70, 53), (70, 63), (84, 63)], "#FFFFFF")   # sail
result.line(70, 51, 70, 63, "#F4F7FA")         # mast

# ---------------- FOAM WAVES ----------------
foam_rows = [
    (87, [(2, 12), (18, 30), (38, 52), (60, 74), (84, 98), (106, 120)]),
    (88, [(8, 22), (28, 42), (54, 70), (80, 90), (100, 112), (122, 127)]),
    (89, [(0, 8), (14, 26), (38, 50), (62, 78), (92, 106), (114, 124)]),
]
for y, segs in foam_rows:
    for x0, x1 in segs:
        hline(y, "#FFFFFF", x0, x1)
foam_edge = [
    (86, [(4, 16), (24, 36), (46, 58), (70, 82), (90, 102), (112, 122)]),
    (88, [(0, 6), (12, 26), (32, 40), (58, 72), (88, 98), (108, 118)]),
]
for y, segs in foam_edge:
    for x0, x1 in segs:
        hline(y, "#C9F2EE", x0, x1)

# ---------------- SAND ----------------
band(90, 95, "#D3AF66")     # wet sand
band(96, 104, "#E7C783")
band(105, 127, "#F2D9A2")   # golden dry sand

# wet sand streaks + sparkles
for sx, sy, ln in [(6, 92, 14), (24, 93, 10), (50, 91, 12), (74, 94, 16), (100, 92, 12), (118, 90, 8)]:
    hline(sy, "#C4A258", sx, sx + ln)
for sx, sy in [(14, 100), (40, 108), (70, 112), (100, 118), (120, 125), (30, 120), (88, 110), (58, 126)]:
    result.set(sx, sy, "#FFEDB2")

# umbrella soft shadow on sand
result.ellipse(34, 120, 26, 5, "#C9A35C")

# ---------------- RED-AND-WHITE UMBRELLA ----------------
cx0, cy0, R = 34, 94, 26
for y in range(cy0 - R, cy0 + 1):
    for x in range(cx0 - R, cx0 + R + 1):
        dx = x - cx0
        dy = y - cy0
        if dx * dx + dy * dy <= R * R:
            sec = int((math.atan2(dy, dx) + math.pi) / (math.pi / 8)) % 8
            result.set(x, y, "#E03A3A" if sec % 2 == 0 else "#FFFFFF")
result.circle(34, 69, 2, "#E03A3A")            # tip
result.line(34, 94, 34, 121, "#8C5A33")        # pole

# ---------------- STRIPED TOWEL ----------------
for y in range(103, 123):
    for x in range(54, 100):
        idx = ((x - 54) // 4) % 4
        col = ["#FF8D5E", "#FFFFFF", "#2FAF9E", "#FFD166"][idx]
        result.set(x, y, col)
result.line(54, 122, 99, 122, "#C96A44")       # hem
result.line(54, 103, 99, 103, "#FFE9B8")

# ---------------- FLIP-FLOPS ----------------
def flipflop(x, y):
    result.ellipse(x + 5, y + 2, 5, 2, "#FFD055")   # sole
    result.line(x + 2, y, x + 5, y + 1, "#FF5A5A")   # strap
    result.line(x + 8, y, x + 5, y + 1, "#FF5A5A")
    result.ellipse(x + 5, y + 4, 6, 1, "#C9A35C")    # tiny shadow

flipflop(94, 121)
flipflop(108, 121)

print(result.stats_text())
finish(result)
