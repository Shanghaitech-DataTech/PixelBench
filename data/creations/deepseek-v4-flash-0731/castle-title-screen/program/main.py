import math
from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, name="castle-title")


def cband(y0, rmin, rmax, amp, hexv, phase=0.0, step=4):
    for x in range(-rmax - 6, W + rmax + 6, step):
        r = rmin + (rmax - rmin) * (0.5 + 0.5 * math.sin(x * 0.10 + phase))
        yy = y0 + amp * math.sin(x * 0.055 + phase * 1.3)
        c.circle(x, int(yy), int(r) + 1, hexv)


# ---- sky gradient (sunset: deep purple -> magenta -> orange) ----
sky = ["#100c2c", "#160f36", "#1d1440", "#251a4c", "#2f2056", "#3a265c",
       "#482c5e", "#56345e", "#653e5c", "#744a5a", "#845656", "#946250",
       "#a46c4a", "#b47644", "#c48040", "#d48a3e", "#e0943e", "#e89c40",
       "#eca448", "#efa84c"]
for y in range(88):
    c.rect(0, y, W, 1, sky[min(19, y * 20 // 88)])

# ---- layered clouds (back layers) ----
cband(18, 3, 7, 4, "#382052")
cband(34, 5, 9, 5, "#5c2e5c")
cband(32, 3, 6, 4, "#6e3866", phase=2)
cband(50, 6, 10, 6, "#944858", phase=3)

# ---- large orange sun ----
sx, sy = 58, 72
c.circle(sx, sy, 18, "#e07842")
c.circle(sx, sy, 14, "#f0902e")
c.circle(sx, sy, 9, "#f8b04e")
c.circle(sx, sy, 5, "#ffd070")

# ---- front cloud layer (partly in front of the sun) ----
cband(70, 6, 10, 5, "#c86a50", phase=4)

# ---- sea ----
sea = ["#543c60", "#46365c", "#3a3054", "#302a4c", "#282648",
       "#222040", "#1c1c38", "#181832"]
for y in range(88, 128):
    c.rect(0, y, W, 1, sea[(y - 88) * 8 // 40])

for y in range(92, 126, 6):
    c.rect(0, y, W, 1, "#5c5080")
for y in range(95, 126, 8):
    c.rect(0, y, W, 1, "#221e40")

# sun reflection shimmer
refs = ["#e8a048", "#f0b058", "#d88c3c"]
for i, yy in enumerate(range(90, 124, 2)):
    t = (yy - 90) / 34.0
    wpx = max(4, int(24 * (1 - t) + 8 * t))
    c.rect(sx - wpx // 2, yy, wpx, 1, refs[i % 3])

# ---- small sailing ship on the sea ----
boat = "#160f20"
c.poly([(33, 93), (42, 96), (33, 99)], boat)
c.rect(26, 98, 14, 2, boat)

# ---- seaside cliff (right) ----
c.poly([(84, 54), (88, 46), (94, 38), (100, 32), (110, 27), (120, 25),
        (127, 24), (127, 127), (92, 127), (86, 116), (84, 98), (83, 76)], "#32243c")

# ---- castle with two towers and flags ----
stone = "#523e54"
shadow = "#3e3044"
win = "#ffcf5e"
flagc = "#c84040"
flagh = "#e05858"
gate = "#241a28"

# left tower
c.rect(92, 34, 12, 30, stone)
for mx in (93, 97, 101):
    c.rect(mx, 30, 3, 4, stone)
c.rect(92, 34, 2, 30, shadow)
# right tower
c.rect(114, 30, 13, 34, stone)
for mx in (115, 119, 123):
    c.rect(mx, 26, 3, 4, stone)
c.rect(124, 30, 3, 34, shadow)
# keep
c.rect(103, 42, 11, 22, stone)
for mx in (104, 108, 112):
    c.rect(mx, 38, 3, 4, stone)
c.rect(103, 42, 2, 22, shadow)
# gate
c.rect(106, 55, 3, 9, gate)
c.rect(107, 53, 1, 2, gate)
# lit windows
c.rect(95, 48, 3, 3, win)
c.rect(120, 44, 3, 3, win)
c.rect(106, 52, 3, 3, win)
# flags on the towers
c.rect(97, 22, 1, 12, shadow)
c.poly([(97, 22), (107, 25), (97, 28)], flagc)
c.rect(97, 22, 10, 1, flagh)
c.rect(120, 18, 1, 12, shadow)
c.poly([(120, 18), (127, 21), (120, 24)], flagc)
c.rect(120, 18, 7, 1, flagh)

# ---- dark foreground rocks ----
c.poly([(0, 112), (8, 110), (16, 114), (24, 108), (32, 112), (44, 110),
        (56, 115), (70, 112), (84, 116), (96, 113), (108, 116), (118, 112),
        (127, 114), (127, 127), (0, 127)], "#181226")
for (rx, ry) in [(8, 110), (24, 108), (44, 110), (96, 113), (118, 112)]:
    c.rect(rx, ry, 3, 1, "#241c30")
c.poly([(0, 120), (6, 122), (14, 118), (24, 123), (36, 120), (50, 124),
        (64, 122), (80, 126), (92, 123), (104, 126), (116, 122), (127, 125),
        (127, 127), (0, 127)], "#0c0912")

# ---- birds ----
for (bx, by) in [(24, 26), (40, 22), (58, 28)]:
    c.set(bx, by, "#120e26")
    c.set(bx - 1, by - 1, "#120e26")
    c.set(bx + 1, by - 1, "#120e26")

print(c.stats_text())
finish(c)
