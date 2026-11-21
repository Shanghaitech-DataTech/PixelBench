import math
import random

random.seed(7)

c = new_canvas(128, 128, background="#bde2f9", name="summer_seaside")

# ---------------- Sky gradient ----------------
sky_bands = [
    (0, 14, "#2f8fdd"),
    (14, 26, "#4aa2e6"),
    (26, 38, "#6db9ee"),
    (38, 48, "#93cff4"),
    (48, 56, "#bde2f9"),
]
for y0, y1, col in sky_bands:
    c.rect(0, y0, 128, y1 - y0, col)
# dithered transitions between sky bands (reuses existing colours)
for i in range(len(sky_bands) - 1):
    yb = sky_bands[i][1]
    c.dither(0, yb - 1, 128, 2, [sky_bands[i][2], sky_bands[i + 1][2]], "bayer4")

# ---------------- Sun ----------------
sx, sy = 100, 18
c.circle(sx, sy, 11, "#ffd94d")
c.circle(sx, sy, 8, "#ffe873")
c.circle(sx, sy, 5, "#fff6c9")
c.circle(sx, sy, 2, "#fffdf0")
for k in range(8):
    a = k * math.pi / 4
    for d in (13, 14, 15):
        c.set(round(sx + math.cos(a) * d), round(sy + math.sin(a) * d), "#ffe873")

# ---------------- Clouds ----------------
def cloud(cx, cy):
    c.ellipse(cx, cy + 2, 11, 4, "#d8ecf7")
    c.ellipse(cx - 8, cy + 1, 6, 3, "#ffffff")
    c.ellipse(cx + 9, cy + 1, 6, 3, "#ffffff")
    c.ellipse(cx, cy, 10, 4, "#ffffff")
    c.ellipse(cx - 3, cy - 3, 5, 3, "#ffffff")

cloud(28, 15)
cloud(66, 34)
cloud(104, 45)
cloud(13, 43)

# ---------------- Sea (deep blue at horizon -> teal near shore) ----------------
sea_bands = [
    (56, 57, "#174e8c"),
    (57, 64, "#1b5da8"),
    (64, 71, "#2377b8"),
    (71, 78, "#3190c6"),
    (78, 85, "#47a9cc"),
    (85, 91, "#55c0bd"),
]
for y0, y1, col in sea_bands:
    c.rect(0, y0, 128, y1 - y0, col)
for i in range(len(sea_bands) - 1):
    yb = sea_bands[i][1]
    c.dither(0, yb - 1, 128, 2, [sea_bands[i][2], sea_bands[i + 1][2]], "bayer4")

def wave_line(y, color, x0=0, x1=127, amp=1.0, period=18, phase=0, dash=None):
    for x in range(x0, x1 + 1):
        if dash and ((x + phase) // dash) % 2 == 1:
            continue
        yy = y + int(round(amp * math.sin((x + phase) * 2 * math.pi / period)))
        c.set(x, yy, color)

wave_line(62, "#3d83c4", period=22, dash=9)
wave_line(70, "#5aa7d4", period=19, phase=5, dash=8)
wave_line(78, "#79c6dd", period=16, phase=11, dash=7)
wave_line(85, "#a5e6e2", period=14, phase=3, dash=6)
wave_line(88, "#eafcfb", period=24, phase=9, dash=5)

# sea sparkles
for _ in range(26):
    x = random.randrange(0, 128)
    y = random.randrange(60, 88)
    c.set(x, y, "#cdeff5")

# ---------------- Sailboat (far out) ----------------
bx = 95
c.poly([(88, 68), (103, 68), (100, 72), (91, 72)], "#7a4a2b")
c.line(88, 68, 103, 68, "#a9713f")
c.line(bx, 67, bx, 57, "#5d4037")
c.poly([(96, 58), (96, 67), (103, 67)], "#ffffff")
c.poly([(94, 58), (94, 67), (87, 67)], "#f2ede0")
c.set(96, 57, "#e63946")
for px, py in [(91, 74), (94, 75), (98, 74), (95, 76)]:
    c.set(px, py, "#bfe9ee")

# ---------------- Sand ----------------
c.rect(0, 90, 128, 38, "#f4d68e")
c.rect(0, 90, 128, 10, "#e6c07a")  # wet sand band
for _ in range(170):
    x = random.randrange(0, 128)
    y = random.randrange(90, 128)
    c.set(x, y, random.choice(["#dfb870", "#f9e3ab"]))

# ---------------- Foam waves rolling in ----------------
for x in range(128):
    top = 91 + int(round(2 * math.sin(x * 2 * math.pi / 26 + 1)))
    bot = top + 3 + int(round(1.5 * math.sin(x * 2 * math.pi / 13 + 2)))
    for y in range(top, bot + 1):
        c.set(x, y, "#ffffff")
    if (x // 4) % 2 == 0:
        c.set(x, bot + 1, "#cfeef2")
wave_line(101, "#ffffff", period=20, phase=8, dash=6)
for _ in range(50):
    x = random.randrange(0, 128)
    y = random.randrange(96, 106)
    c.set(x, y, "#ffffff")

# ---------------- Beach umbrella ----------------
ux, uy = 40, 86
c.ellipse(47, 102, 13, 3, "#dcaf66")          # shadow on sand
c.rect(39, 84, 2, 32, "#8a5a3b")              # pole
c.line(39, 84, 39, 115, "#a9764f")            # pole highlight
# canopy base (top half disc)
c.path("M 21 86 A 19 19 0 0 1 59 86 Z", "#e63946")
# white panels: vertical candy stripes clipped to the canopy disc
for sx0 in (26, 34, 42, 50):
    for x in range(sx0, sx0 + 4):
        for y in range(68, 86):
            if (x - 40) ** 2 + (y - 86) ** 2 <= 18 ** 2:
                c.set(x, y, "#faf6ec")
# scalloped rim
for xsc, col in [(24, "#faf6ec"), (30, "#e63946"), (37, "#faf6ec"),
                 (43, "#e63946"), (50, "#faf6ec"), (56, "#e63946")]:
    c.circle(xsc, 87, 3, col)
# canopy outline + cap
c.path("M 21 86 A 19 19 0 0 1 59 86", "#b02a37", fill=False)
c.circle(40, 68, 2, "#a52433")

# ---------------- Striped towel ----------------
tx, ty, tw, th = 80, 100, 28, 18
c.rect(tx, ty, tw, th, "#fbfbf7")
for i, xx in enumerate(range(tx, tx + tw, 4)):
    if i % 2 == 0:
        c.rect(xx, ty, 4, th, "#ff6f61")
c.rect(tx, ty, tw, th, "#e05548", fill=False)
c.poly([(tx + tw, ty + 11), (tx + tw, ty + th), (tx + tw - 6, ty + th)], "#e6e2d4")
for j, yy in enumerate(range(ty, ty + th, 2)):
    c.set(tx - 1, yy, "#ff6f61" if j % 2 else "#fbfbf7")
    c.set(tx + tw, yy, "#fbfbf7" if j % 2 else "#ff6f61")
c.rect(tx + 1, ty + th, tw - 2, 1, "#e0b96e")

# ---------------- Flip-flops ----------------
c.ellipse(73, 113, 2, 4, "#ffb703")
c.line(73, 111, 71, 114, "#9c6b09")
c.line(73, 111, 75, 114, "#9c6b09")
c.set(73, 113, "#9c6b09")
c.ellipse(66, 118, 2, 4, "#ef476f")
c.line(66, 116, 64, 119, "#a12d49")
c.line(66, 116, 68, 119, "#a12d49")
c.set(66, 118, "#a12d49")

# ---------------- Starfish & shell ----------------
cx0, cy0 = 18, 118
for k in range(5):
    a = math.radians(-90 + 72 * k)
    for d in (1, 2, 3):
        c.set(round(cx0 + math.cos(a) * d), round(cy0 + math.sin(a) * d), "#ff8c42")
c.set(cx0, cy0, "#e56b1f")
c.set(111, 116, "#fff3f0"); c.set(112, 115, "#fff3f0"); c.set(113, 116, "#fff3f0")
c.set(111, 117, "#f3c9c0"); c.set(112, 117, "#f3c9c0"); c.set(113, 117, "#f3c9c0")

# ---------------- Gulls ----------------
c.path("M 16 28 Q 20 24 24 28 Q 28 24 32 28", "#3d4f61", fill=False)
c.path("M 36 21 Q 39 18 42 21 Q 45 18 48 21", "#3d4f61", fill=False)

view(c)
print(c.stats_text())
finish(c)
