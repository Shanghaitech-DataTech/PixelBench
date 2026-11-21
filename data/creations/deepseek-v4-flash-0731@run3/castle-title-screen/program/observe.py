import math
from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, name="title")

def band(y0, y1, col):
    c.rect(0, y0, W, y1 - y0 + 1, col)

for y0, y1, col in [
    (0, 7, "#2a1440"), (8, 15, "#421a55"), (16, 23, "#5c2260"),
    (24, 31, "#7a2e60"), (32, 39, "#9a3c57"), (40, 47, "#b84d48"),
    (48, 55, "#d4623a"), (56, 63, "#ec7a30"), (64, 71, "#f99a2c"),
]:
    band(y0, y1, col)

for y0, y1, col in [
    (72, 74, "#b84358"), (75, 79, "#8a2c52"), (80, 84, "#62204e"),
    (85, 91, "#461a4a"), (92, 96, "#331448"),
]:
    band(y0, y1, col)

c.circle(88, 60, 14, "#ff8a1e")
c.circle(88, 60, 11, "#ffd44d")
c.circle(88, 60, 8, "#ffe97a")
c.rect(74, 73, 29, 3, "#b84358")

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
hl(wavy(52, 120, 57, 65, 2, "#a8413c", phase=0.5), "#ff9e4e")
for (x0, x1, y) in [(50, 70, 50), (96, 122, 53), (58, 80, 55)]:
    c.rect(x0, y, x1 - x0 + 1, 1, "#ffb02e")

c.rect(79, 73, 19, 5, "#ff8a1e")
c.rect(83, 76, 11, 3, "#ffb02e")
for i, r in enumerate(range(79, 93, 2)):
    wdt = 3 + (i % 3)
    col = ["#ffd44d", "#ff9e2c", "#d4623a"][i % 3]
    c.rect(88 - wdt // 2, r, wdt, 1, col)
for (x, y) in [(76, 80), (92, 84), (82, 88), (96, 90)]:
    c.set(x, y, "#ffd44d")
    c.set(x + 1, y, "#ffb02e")

cliff = [(0, 128), (0, 70), (12, 64), (26, 68), (40, 60), (54, 68),
        (62, 78), (68, 90), (72, 106), (76, 128)]
c.poly(cliff, "#241438")
c.line(54, 68, 62, 78, "#8a3a52")
c.line(62, 78, 68, 90, "#8a3a52")

K = "#1c1030"
c.rect(6, 34, 12, 34, K)
for tx in (6, 11, 15):
    c.rect(tx, 30, 3, 4, K)
c.rect(40, 30, 12, 38, K)
for tx in (40, 45, 49):
    c.rect(tx, 26, 3, 4, K)
c.rect(18, 48, 22, 20, K)
c.poly([(18, 48), (30, 36), (42, 48)], K)
c.line(30, 36, 42, 48, "#8a3a52")
c.line(40, 30, 40, 68, "#d4623a")
c.rect(27, 58, 6, 10, "#170d28")
WCOL = "#ffc24e"
c.rect(9, 42, 3, 4, WCOL)
c.rect(13, 49, 3, 3, WCOL)
c.rect(43, 40, 3, 4, WCOL)
c.rect(47, 47, 3, 3, WCOL)
c.rect(23, 52, 2, 2, WCOL)
c.rect(35, 52, 2, 2, WCOL)

c.line(12, 30, 12, 22, K)
c.poly([(12, 22), (24, 22), (12, 28)], "#d63a3a")
c.line(46, 26, 46, 17, K)
c.poly([(46, 17), (58, 17), (46, 23)], "#d63a3a")

rockL = [(0, 128), (0, 96), (12, 90), (26, 94), (38, 90), (50, 98),
         (58, 108), (62, 120), (66, 128)]
c.poly(rockL, "#0f0a1c")
for (a, b) in [((0, 96), (12, 90)), ((12, 90), (26, 94)), ((26, 94), (38, 90)),
              ((38, 90), (50, 98)), ((50, 98), (58, 108))]:
    c.line(a[0], a[1], b[0], b[1], "#1c1030")

rockR = [(128, 128), (128, 90), (118, 86), (104, 88), (94, 94), (88, 104),
         (84, 116), (82, 128)]
c.poly(rockR, "#0a0614")
for (a, b) in [((128, 90), (118, 86)), ((118, 86), (104, 88)), ((104, 88), (94, 94)),
              ((94, 94), (88, 104))]:
    c.line(a[0], a[1], b[0], b[1], "#1c1030")

for (x, y) in [(30, 18), (37, 15), (24, 12)]:
    c.line(x, y, x - 2, y - 2, K)
    c.line(x, y, x + 2, y - 2, K)

print("=== CASTLE ===")
print(c.matrix_text(region=(0, 14, 62, 72), indices=False))
print("=== SUN/SKY ===")
print(c.matrix_text(region=(60, 8, 127, 72), indices=False))
print("=== SEA+ROCKS ===")
print(c.matrix_text(region=(0, 72, 127, 112), indices=False))
