import random

c = new_canvas(128, 128, name="cyberpunk_alley")

# ---------- sky gradient ----------
bands = [(0, 8, "#06060e"), (8, 16, "#080814"), (16, 26, "#0a0a1c"),
         (26, 38, "#0d0d24"), (38, 50, "#10102e"), (50, 62, "#131338"),
         (62, 76, "#161642"), (76, 90, "#181848"), (90, 98, "#151540")]
for y0, y1, co in bands:
    c.rect(0, y0, 128, y1 - y0, co)

# dim background rain (behind everything)
rng = random.Random(5)
for _ in range(120):
    x = rng.randint(3, 127)
    y = rng.randint(1, 124)
    co = rng.choice(["#5a7aae", "#5a7aae", "#5a7aae", "#9fd8ff"])
    c.line(x, y, x - 2, y + 3, co)

# ---------- street / wet ground ----------
c.rect(0, 96, 128, 32, "#0c0c1c")
c.rect(0, 100, 128, 8, "#10102c")
c.rect(0, 110, 128, 8, "#141434")
c.rect(0, 118, 128, 10, "#181840")
c.rect(0, 96, 128, 1, "#0a0a1c")
c.ellipse(64, 112, 44, 9, "#202048")
c.line(24, 106, 40, 106, "#262658")
c.line(30, 116, 46, 116, "#262658")
c.line(78, 108, 94, 108, "#262658")
c.line(88, 118, 104, 118, "#262658")

# warm pool spilling from the doorway
c.rect(57, 98, 14, 10, "#3a2410")
c.rect(59, 100, 10, 8, "#8a5a14")
c.rect(60, 101, 8, 6, "#ffb84d")

# pink neon reflections (left)
c.rect(12, 102, 3, 12, "#c91f78")
c.rect(20, 104, 3, 13, "#c91f78")
c.rect(13, 105, 2, 6, "#ff2d95")
c.rect(21, 106, 2, 7, "#ff2d95")

# cyan reflections (right)
c.rect(98, 102, 4, 14, "#00a8cc")
c.rect(106, 104, 3, 12, "#00a8cc")
c.rect(113, 101, 4, 15, "#00a8cc")
c.rect(99, 104, 2, 8, "#00e5ff")
c.rect(107, 106, 2, 6, "#00e5ff")
c.rect(114, 103, 2, 9, "#00e5ff")
c.rect(104, 104, 3, 8, "#c91f78")
c.rect(105, 105, 2, 5, "#ff2d95")

# dark figure reflection
c.rect(60, 112, 8, 11, "#06060f")

# ---------- back wall (far alley end) ----------
c.poly([(44, 44), (84, 44), (90, 96), (38, 96)], "#0e0e22")
c.line(60, 44, 60, 8, "#04040a")
c.set(60, 5, "#ff3b30")
for wx, wy in [(46, 16), (72, 16), (46, 26), (72, 26), (46, 36), (72, 36)]:
    c.rect(wx, wy, 10, 8, "#141434")
c.rect(48, 18, 6, 4, "#3a2410")
c.rect(70, 28, 6, 4, "#3a2410")
c.rect(48, 26, 10, 8, "#3a2410")
c.line(48, 30, 56, 30, "#0e0e22")
c.line(51, 26, 51, 34, "#0e0e22")

# neon sign above the door
c.rect(48, 46, 32, 14, "#7a1448")
c.rect(50, 48, 28, 12, "#080810")
c.rect(53, 50, 22, 9, "#ff2d95")
c.text(55, 51, "BAR", "#ff8cc4")

# glowing doorway
c.rect(56, 78, 16, 18, "#3a2410")
c.rect(58, 80, 12, 16, "#8a5a14")
c.rect(60, 82, 8, 14, "#ffb84d")
c.line(56, 78, 56, 96, "#07070f")
c.line(72, 78, 72, 96, "#07070f")

# ---------- left building ----------
c.poly([(0, 0), (38, 0), (44, 44), (38, 96), (0, 96)], "#0b0b1a")
c.rect(36, 0, 8, 48, "#101028")

for wx, wy in [(10, 14), (24, 14), (10, 26), (12, 38)]:
    c.rect(wx, wy, 6, 8, "#131338")
c.rect(24, 26, 6, 8, "#3a2410")
c.line(24, 30, 30, 30, "#0b0b1a")
c.line(27, 26, 27, 34, "#0b0b1a")
c.rect(28, 38, 6, 8, "#3a2410")
c.line(28, 42, 34, 42, "#0b0b1a")
c.line(31, 38, 31, 46, "#0b0b1a")

# vertical neon tube (left)
c.rect(2, 20, 8, 42, "#7a1448")
c.rect(4, 22, 4, 38, "#ff2d95")
c.rect(5, 23, 2, 36, "#ff8cc4")

# pipes
c.line(0, 58, 42, 58, "#07070f")
c.line(0, 63, 40, 63, "#07070f")
c.line(35, 57, 35, 62, "#07070f")

# vending machine (left wall)
c.rect(6, 64, 26, 32, "#07070f")
c.text(10, 60, "24H", "#ffd600")
c.rect(8, 66, 22, 2, "#00e5ff")
rowcols = [["#39ff88", "#ffd600", "#ff2d95", "#8ef4ff"],
          ["#00e5ff", "#b14bff", "#ff3b30", "#00e5ff"],
          ["#ffd600", "#39ff88", "#8ef4ff", "#ff2d95"]]
for row, cols in enumerate(rowcols):
    for xi, co in enumerate(cols):
        c.rect(8 + xi * 5, 70 + row * 6, 4, 4, co)
c.rect(8, 90, 22, 3, "#101028")
c.set(9, 91, "#4d4d70")
c.set(23, 91, "#4d4d70")
c.rect(8, 95, 22, 2, "#0e0e22")
c.rect(5, 96, 28, 2, "#00a8cc")

# vending machine 2 (right wall)
c.rect(104, 58, 18, 33, "#07070f")
c.text(99, 54, "24H", "#ffd600")
c.rect(105, 60, 16, 2, "#ff2d95")
for row in range(3):
    for xi in range(3):
        co = ["#00e5ff", "#39ff88", "#ffd600"][(row + xi) % 3]
        c.rect(105 + xi * 5, 64 + row * 6, 4, 4, co)
c.rect(105, 84, 16, 3, "#101028")
c.set(106, 85, "#4d4d70")
c.set(116, 85, "#4d4d70")
c.rect(105, 89, 16, 2, "#0e0e22")
c.rect(103, 91, 18, 3, "#ff2d95")

# ---------- right building ----------
c.poly([(128, 0), (90, 0), (84, 44), (90, 96), (128, 96)], "#0b0b1a")
c.rect(84, 0, 8, 48, "#101028")

for wx, wy in [(92, 14), (110, 14), (112, 26), (96, 38)]:
    c.rect(wx, wy, 6, 8, "#131338")
c.rect(94, 26, 6, 8, "#3a2410")
c.line(94, 30, 100, 30, "#0b0b1a")
c.line(97, 26, 97, 34, "#0b0b1a")
c.rect(96, 38, 6, 7, "#3a2410")
c.line(96, 41, 102, 41, "#0b0b1a")
c.line(99, 38, 99, 45, "#0b0b1a")

# vertical neon tube (right)
c.rect(96, 4, 6, 26, "#7a1448")
c.rect(97, 5, 4, 24, "#ff2d95")
c.rect(98, 6, 2, 22, "#ff8cc4")

# big cyan sign
c.rect(90, 20, 36, 12, "#006a80")
c.rect(92, 21, 32, 10, "#080810")
c.rect(93, 22, 26, 8, "#00a8cc")
c.text(94, 22, "CYBER", "#c9fbff")
c.set(120, 25, "#ff3b30")
c.set(121, 26, "#ff3b30")

# roof hardware
c.rect(104, 0, 14, 6, "#06060e")
c.line(108, 6, 110, 20, "#07070f")
c.line(110, 6, 112, 20, "#07070f")
c.rect(88, 8, 10, 7, "#06060e")
c.line(0, 52, 40, 52, "#07070f")
c.line(0, 57, 38, 57, "#07070f")

# ---------- power cables ----------
c.path("M 30 6 Q 64 26 98 6", "#04040a", False)
c.path("M 34 4 Q 64 30 94 5", "#04040a", False)
c.set(78, 13, "#04040a")
c.set(82, 12, "#04040a")
c.set(50, 15, "#04040a")

# ---------- person with transparent umbrella ----------
# translucent dome (tinted but readable plastic)
c.path("M 52 74 A 12 12 0 0 1 76 74 Z", "#152238", True)
c.path("M 51 74 A 12 12 0 0 1 77 74", "#8ef4ff", False)
c.line(64, 63, 52, 74, "#2a4a70")
c.line(64, 63, 76, 74, "#2a4a70")
c.line(64, 64, 64, 74, "#2a4a70")
c.line(64, 65, 64, 86, "#04040a")
# figure
c.circle(64, 80, 3, "#04040a")
c.line(60, 88, 64, 86, "#04040a")
c.rect(58, 86, 13, 9, "#04040a")
c.rect(56, 94, 17, 6, "#04040a")
c.rect(59, 99, 5, 12, "#04040a")
c.rect(58, 111, 6, 3, "#04040a")
c.rect(66, 99, 4, 10, "#04040a")
c.rect(69, 108, 5, 3, "#04040a")
# rim light on the silhouette
c.line(57, 87, 57, 93, "#c91f78")
c.line(70, 87, 70, 93, "#00a8cc")
c.line(70, 100, 70, 107, "#3a5f8a")
c.set(71, 101, "#00a8cc")
# rain beading on the umbrella
for sx, sy in [(58, 62), (66, 60), (70, 66), (61, 65)]:
    c.set(sx, sy, "#c9fbff")

# ---------- foreground rain ----------
front = [(30, 22, "#c9fbff"), (52, 40, "#9fd8ff"), (88, 34, "#c9fbff"),
         (64, 52, "#9fd8ff"), (30, 86, "#9fd8ff"), (96, 64, "#9fd8ff"),
         (120, 90, "#9fd8ff"), (20, 100, "#9fd8ff"), (84, 66, "#c9fbff"),
         (44, 94, "#9fd8ff"), (8, 88, "#9fd8ff"), (104, 118, "#9fd8ff")]
for rx, ry, co in front:
    c.line(rx, ry, rx - 2, ry + 3, co)

# sparkle on wet metal
c.set(97, 97, "#c9fbff")
c.set(96, 98, "#c9fbff")

# ---------- report ----------
print(c.stats_text())
print("palette size:", len(c.palette()))
print(c.matrix_text(region=(50, 56, 80, 114), indices=True))

finish(c)
