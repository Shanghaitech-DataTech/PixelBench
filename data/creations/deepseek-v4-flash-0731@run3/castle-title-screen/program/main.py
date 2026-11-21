import math
from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, name="title")

def band(y0, y1, col):
    c.rect(0, y0, W, y1 - y0 + 1, col)

# ---------- sky gradient (top -> horizon) ----------
for y0, y1, col in [
    (0, 7, "#2a1440"), (8, 15, "#421a55"), (16, 23, "#5c2260"),
    (24, 31, "#7a2e60"), (32, 39, "#9a3c57"), (40, 47, "#b84d48"),
    (48, 55, "#d4623a"), (56, 63, "#ec7a30"), (64, 71, "#f99a2c"),
]:
    band(y0, y1, col)

# ---------- sea ----------
for y0, y1, col in [
    (72, 74, "#b84358"), (75, 79, "#8a2c52"), (80, 84, "#62204e"),
    (85, 91, "#461a4a"), (92, 96, "#331448"),
]:
    band(y0, y1, col)

# ---------- sun ----------
c.circle(88, 56, 15, "#ff8a1e")
c.circle(88, 56, 12, "#ffd44d")
c.circle(88, 56, 9, "#ffe97a")
# dip sun into the sea
c.rect(74, 73, 29, 3, "#b84358")

# ---------- layered clouds ----------
def wavy(x0, x1, y0, y1, amp, col, phase=0.0, period=42.0):
    xs = list(range(x0, x1 + 1, 4))
    if xs[-1] != x1:
        xs.append(x1)
    top = [(x, y0 + int(round(amp * math.sin((x - x0) / period * math.tau + phase)))) for x in xs]
    bot = [(x, y1 + int(round(amp * math.sin((x - x0) / period * math.tau + phase + 1.1)))) for x in xs]
    c.poly(top + list(reversed(bot)), col)
    return top

def hl(points, col):
    for i in range(len(points) - 1):
        c.line(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1], col)

hl(wavy(0, 127, 17, 26, 3, "#331548", phase=0.0), "#5c2260")
hl(wavy(0, 127, 32, 40, 3, "#4a1a45", phase=2.2), "#7a2e60")
hl(wavy(14, 112, 45, 52, 2, "#6d2a60", phase=1.0), "#9a3c57")
hl(wavy(50, 125, 66, 73, 2, "#a8413c", phase=0.5), "#ff9e4e")
# bright thin streaks near the sun
for (x0, x1, y) in [(50, 70, 50), (96, 122, 53), (58, 80, 58)]:
    c.rect(x0, y, x1 - x0 + 1, 1, "#ffb02e")

# ---------- sun reflection on water ----------
c.rect(79, 73, 19, 5, "#ff8a1e")
c.rect(83, 76, 11, 3, "#ffb02e")
for i, r in enumerate(range(79, 93, 2)):
    wdt = 3 + (i % 3)
    col = ["#ffd44d", "#ff9e2c", "#d4623a"][i % 3]
    c.rect(88 - wdt // 2, r, wdt, 1, col)
for (x, y) in [(76, 80), (92, 84), (82, 88), (96, 90)]:
    c.set(x, y, "#ffd44d")
    c.set(x + 1, y, "#ffb02e")

# ---------- cliff (left) ----------
cliff = [(0, 128), (0, 70), (12, 64), (26, 68), (40, 60), (54, 68),
        (62, 78), (68, 90), (72, 106), (76, 128)]
c.poly(cliff, "#241438")
c.line(54, 68, 62, 78, "#8a3a52")
c.line(62, 78, 68, 90, "#8a3a52")

# ---------- castle ----------
K = "#1c1030"
# left tower
c.rect(6, 34, 12, 34, K)
for tx in (6, 11, 15):
    c.rect(tx, 30, 3, 4, K)
# right tower (taller)
c.rect(40, 30, 12, 38, K)
for tx in (40, 45, 49):
    c.rect(tx, 26, 3, 4, K)
# central keep wall + gable
c.rect(18, 48, 22, 20, K)
c.poly([(18, 48), (30, 36), (42, 48)], K)
c.line(30, 36, 42, 48, "#8a3a52")
c.line(40, 30, 40, 68, "#d4623a")   # sunlit edge of right tower
# gate
c.rect(27, 58, 6, 10, "#170d28")
# lit windows
WCOL = "#ffc24e"
c.rect(9, 42, 3, 4, WCOL)
c.rect(13, 49, 3, 3, WCOL)
c.rect(43, 40, 3, 4, WCOL)
c.rect(47, 47, 3, 3, WCOL)
c.rect(23, 52, 2, 2, WCOL)
c.rect(35, 52, 2, 2, WCOL)

# ---------- flags (two towers) ----------
c.line(12, 30, 12, 22, K)
c.poly([(12, 22), (24, 22), (12, 28)], "#d63a3a")
c.line(46, 26, 46, 17, K)
c.poly([(46, 17), (58, 17), (46, 23)], "#d63a3a")

# ---------- foreground rocks ----------
rockL = [(0, 128), (0, 96), (12, 90), (26, 94), (38, 90), (50, 98),
         (58, 108), (62, 120), (66, 128)]
c.poly(rockL, "#0f0a1c")
for (a, b) in [((0, 96), (12, 90)), ((12, 90), (26, 94)), ((26, 94), (38, 90)),
              ((38, 90), (50, 98)), ((50, 98), (58, 108))]:
    c.line(a[0], a[1], b[0], b[1], "#1c1030")

rockR = [(127, 128), (127, 88), (118, 82), (104, 85), (95, 91), (89, 101),
         (85, 113), (83, 128)]
c.poly(rockR, "#0a0614")
for (a, b) in [((127, 88), (118, 82)), ((118, 82), (104, 85)), ((104, 85), (95, 91)),
              ((95, 91), (89, 101))]:
    c.line(a[0], a[1], b[0], b[1], "#1c1030")

# ---------- birds ----------
for (x, y) in [(30, 18), (37, 15), (24, 12)]:
    c.line(x, y, x - 2, y - 2, K)
    c.line(x, y, x + 2, y - 2, K)

# ---------- observation (text only) ----------
groups = {
    "S": {"ffd44d", "ffe97a", "ff8a1e", "ff9e2c", "ffb02e", "ffc24e"},
    "C": {"331548", "4a1a45", "6d2a60", "a8413c", "ff9e4e", "5c2260", "7a2e60", "9a3c57", "d4623a"},
    "W": {"b84358", "8a2c52", "62204e", "461a4a", "331448"},
    "K": {"1c1030", "241438", "170d28", "8a3a52"},
    "F": {"d63a3a"},
    "R": {"0f0a1c", "0a0614"},
}
pal = {p["index"]: "#%02x%02x%02x" % (p["rgba"][0], p["rgba"][1], p["rgba"][2]) for p in c.palette()}

def ch(x, y):
    hx = pal.get(c.get(x, y), "?")
    for g, s in groups.items():
        if hx[1:] in s:
            return g
    return "."

print(c.stats_text())
for y in range(0, 128, 2):
    print("".join(ch(x, y) for x in range(0, 128, 2)))

finish(c)
