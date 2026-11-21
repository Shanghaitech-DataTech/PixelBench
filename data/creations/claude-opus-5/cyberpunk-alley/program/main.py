import random

random.seed(7)
W = H = 128

sc = new_canvas(W, H, background="#070910", name="scene")

# ------------------------------------------------------------------- palette
SKY0, SKY1, SKY2 = "#070910", "#0a0d18", "#141b33"
G1, G2, G3 = "#1d2443", "#273061", "#313c75"
NEON_M, NEON_MG, NEON_MD = "#ff2fa0", "#ff7fc8", "#5a1340"
NEON_C, NEON_CG, NEON_CD = "#26e0ff", "#9ff4ff", "#12566b"
NEON_Y, NEON_G = "#ffd23f", "#3cff9e"
WARM, WARMD, WARMG = "#ffb347", "#6a3f18", "#ffdc9a"
WHITE, OFFW = "#ffffff", "#cfe6f2"
DARK, CABLE = "#07070c", "#05050a"
GRD = ["#141826", "#1b2030", "#232b40"]
WL = ["#15121d", "#1c1827", "#241f33"]
WR = ["#111622", "#19202e", "#222a3c"]
EDGE = "#222a3c"

# ------------------------------------------------------------------ sky bands
sc.rect(0, 10, 128, 8, SKY1)
sc.rect(0, 18, 128, 10, SKY1)
sc.rect(0, 28, 128, 42, SKY2)

# far glow down the alley
sc.ellipse(64, 64, 30, 22, G1)
sc.ellipse(64, 64, 24, 17, G2)
sc.ellipse(64, 64, 17, 12, G3)

# ------------------------------------------------------------- distant towers
towers = [(45, 20, 8, 50, "#121829"), (54, 28, 7, 42, "#172038"),
          (62, 12, 9, 58, "#101628"), (72, 24, 7, 46, "#172038"),
          (79, 17, 6, 53, "#121829")]
for (tx, ty, tw, th, col) in towers:
    sc.rect(tx, ty, tw, th, col)
for (tx, ty, tw, th, col) in towers:
    for yy in range(ty + 2, ty + th - 4, 3):
        for xx in range(tx + 1, tx + tw - 1, 3):
            r = random.random()
            if r < 0.28:
                sc.set(xx, yy, "#8f7a4a")
            elif r < 0.38:
                sc.set(xx, yy, "#4a6a86")

# distant billboard
sc.rect(56, 33, 15, 7, "#2a1024")
sc.rect(56, 33, 15, 7, NEON_MD, fill=False)
sc.line(58, 36, 68, 36, NEON_M)
sc.set(60, 38, NEON_MG)
sc.set(64, 38, NEON_MG)

# street-level backlight haze
sc.ellipse(64, 68, 22, 9, "#3e4a87")
sc.ellipse(64, 69, 14, 6, "#5a68a8")
sc.ellipse(64, 70, 7, 3, "#8190c6")

# -------------------------------------------------------------------- floor
sc.poly([(0, 127), (44, 68), (84, 68), (127, 127)], GRD[0])
sc.poly([(0, 127), (49, 74), (79, 74), (127, 127)], GRD[1])
sc.poly([(14, 127), (55, 80), (73, 80), (113, 127)], GRD[2])

# ---------------------------------------------------------------- side walls
sc.poly([(0, 0), (44, 24), (44, 68), (0, 127)], WL[0])
sc.poly([(127, 0), (84, 24), (84, 68), (127, 127)], WR[0])
for i, (x0, x1) in enumerate([(0, 14), (14, 26), (26, 36), (36, 44)]):
    col = WL[1] if i % 2 == 0 else WL[0]
    sc.poly([(x0, int(0.545 * x0)), (x1, int(0.545 * x1)),
             (x1, 127 - int(1.34 * x1)), (x0, 127 - int(1.34 * x0))], col)
sc.line(0, 127, 44, 68, EDGE)
sc.line(0, 0, 44, 24, WL[2])
for i, (x0, x1) in enumerate([(84, 94), (94, 106), (106, 118), (118, 127)]):
    col = WR[1] if i % 2 == 0 else WR[0]
    sc.poly([(x0, 24 - int((x0 - 84) * 0.558)), (x1, 24 - int((x1 - 84) * 0.558)),
             (x1, 68 + int((x1 - 84) * 1.37)), (x0, 68 + int((x0 - 84) * 1.37))], col)
sc.line(127, 127, 84, 68, EDGE)
sc.line(127, 0, 84, 24, EDGE)

# ------------------------------------------------------- left wall neon stack
sc.ellipse(10, 45, 11, 24, "#2a0c20")
sc.ellipse(9, 45, 8, 21, "#44122f")
sc.rect(4, 28, 12, 34, "#140a13")
sc.rect(4, 28, 12, 34, NEON_M, fill=False)
sc.text(6, 29, "\u9152", NEON_MG, font="8px")
sc.text(6, 39, "\u5834", NEON_MG, font="8px")
sc.text(6, 49, "\u5c4b", WHITE, font="8px")
sc.rect(16, 43, 4, 2, NEON_MD)

sc.ellipse(29, 32, 9, 8, "#0c2b38")
sc.ellipse(29, 32, 6, 6, "#14465a")
sc.rect(23, 27, 13, 9, "#09161c")
sc.rect(23, 27, 13, 9, NEON_C, fill=False)
sc.text(25, 29, "BAR", NEON_CG, font="5x7")

sc.ellipse(39, 50, 5, 5, "#3a2a0c")
sc.rect(37, 48, 5, 5, NEON_Y)
sc.set(38, 49, WHITE)

# ------------------------------------------------------ right wall neon stack
sc.ellipse(118, 44, 12, 23, "#0b2a36")
sc.ellipse(119, 44, 9, 20, "#114452")
sc.rect(112, 26, 12, 36, "#08151b")
sc.rect(112, 26, 12, 36, NEON_C, fill=False)
sc.text(114, 28, "\u9eba", NEON_CG, font="8px")
sc.text(114, 38, "\u5bb6", NEON_CG, font="8px")
sc.text(114, 48, "\u96fb", WHITE, font="8px")
sc.rect(108, 42, 4, 2, NEON_CD)

sc.ellipse(99, 36, 8, 6, "#0d3326")
sc.rect(94, 33, 11, 6, "#07140f")
sc.rect(94, 33, 11, 6, NEON_G, fill=False)
sc.line(96, 36, 102, 36, NEON_G)

for (wx, wy, ww, wh) in [(88, 46, 4, 5), (96, 50, 5, 6), (104, 54, 5, 7)]:
    sc.rect(wx - 1, wy - 1, ww + 2, wh + 2, WARMD)
    sc.rect(wx, wy, ww, wh, WARM)
    sc.rect(wx + 1, wy + 1, max(1, ww - 2), max(1, wh - 2), WARMG)
sc.poly([(104, 68), (112, 68), (120, 90), (104, 86)], "#2c2436")
sc.poly([(105, 68), (110, 68), (113, 82), (105, 80)], "#3a2c3c")

# pipes / AC on right wall
sc.path("M 126 18 Q 104 26 86 40", "#20283a", fill=False)
sc.path("M 127 24 Q 106 32 86 44", "#171e2c", fill=False)
sc.poly([(96, 20), (106, 15), (106, 24), (96, 28)], "#262d3f")
sc.poly([(98, 21), (104, 18), (104, 23), (98, 26)], "#1a202e")

# --------------------------------------------------------- vending machines
sc.poly([(23, 69), (39, 55), (39, 79), (23, 97)], "#232a3e")
sc.poly([(25, 71), (37, 60), (37, 76), (25, 92)], "#121724")
sc.poly([(26, 72), (36, 63), (36, 74), (26, 89)], "#15455a")
for k in range(4):
    y0 = 75 + k * 4
    sc.line(27, y0, 35, y0 - 7 - k, "#1fc6e0")
for (px, py, pc) in [(28, 78, "#ff3b3b"), (31, 76, NEON_Y), (34, 71, NEON_G),
                     (29, 84, NEON_Y), (32, 81, "#ff3b3b"), (28, 88, NEON_G)]:
    sc.set(px, py, pc)
    sc.set(px + 1, py, pc)
sc.poly([(24, 69), (38, 56), (38, 58), (24, 71)], OFFW)
sc.poly([(25, 70), (36, 61), (36, 62), (25, 71)], NEON_M)

sc.poly([(39, 55), (47, 49), (47, 66), (39, 78)], "#1d2434")
sc.poly([(41, 57), (46, 52), (46, 64), (41, 74)], "#113a4c")
sc.poly([(40, 55), (46, 50), (46, 52), (40, 57)], OFFW)
for k in range(3):
    sc.line(42, 62 + k * 4, 45, 59 + k * 4, "#1fc6e0")

sc.poly([(23, 97), (39, 79), (52, 84), (33, 112)], "#1e2a3f")
sc.poly([(26, 95), (39, 80), (46, 83), (31, 106)], "#26384f")

# ------------------------------------------------------------- power cables
for (d, col) in [("M 2 14 Q 64 36 126 10", CABLE),
                 ("M 0 22 Q 64 44 127 19", "#07070e"),
                 ("M 4 6 Q 62 26 124 4", CABLE),
                 ("M 44 24 Q 64 32 84 24", "#07070e")]:
    sc.path(d, col, fill=False)
for (lx, ly) in [(50, 30), (78, 31)]:
    sc.line(lx, ly - 4, lx, ly - 1, "#07070e")
    sc.ellipse(lx, ly + 1, 3, 3, WARMD)
    sc.ellipse(lx, ly + 1, 1, 1, WARMG)
sc.poly([(8, 16), (18, 20), (18, 26), (8, 23)], "#1a202e")

# ------------------------------------------------------- floor / reflections
def refl(c, x, y0, y1, cols):
    y, i = y0, 0
    while y < y1:
        ln = random.choice([1, 2, 2, 3])
        c.line(x, y, x, min(y + ln, y1), cols[i % len(cols)])
        y += ln + random.choice([1, 2, 2, 3])
        i += 1


sc.ellipse(36, 108, 16, 6, "#202740")
sc.ellipse(93, 100, 13, 5, "#202740")
sc.ellipse(64, 119, 22, 7, "#232b45")

for x in range(12, 30, 2):
    refl(sc, x, 86 + (30 - x), 127, ["#4a1030", "#8e2062", NEON_M])
for x in range(96, 118, 2):
    refl(sc, x, 80 + (x - 96), 127, ["#0c3140", "#17788f", NEON_C])
for x in range(54, 76, 2):
    refl(sc, x, 73, 127, ["#2b3765", "#44538f", "#6f7eb6"])
for x in range(104, 114, 2):
    refl(sc, x, 88, 118, ["#2c2436", WARMD])

# ------------------------------------------------------------------ far rain
for i in range(110):
    rx = random.randrange(0, 130)
    ry = random.randrange(0, 118)
    L = random.choice([3, 3, 4, 5])
    col = "#232b45" if random.random() < 0.6 else "#3b4d68"
    sc.line(rx, ry, rx - 1, ry + L, col)

# ------------------------------------------------------------- the person
for x in (61, 63, 65, 67):
    refl(sc, x, 112, 126, ["#13161f", "#111622"])

sc.poly([(60, 92), (68, 92), (69, 106), (59, 106)], DARK)   # coat
sc.poly([(61, 106), (67, 106), (66, 112), (62, 112)], DARK)  # legs block
sc.rect(61, 110, 2, 3, DARK)
sc.rect(65, 110, 2, 3, DARK)
sc.set(60, 113, DARK)
sc.set(67, 113, DARK)
sc.ellipse(64, 88, 2, 3, DARK)                               # head
sc.rect(62, 90, 5, 3, DARK)                                  # shoulders
sc.line(69, 94, 70, 99, DARK)                                # raised arm
# rim light: cyan from the right wall, magenta from the left
sc.line(69, 93, 70, 98, NEON_CG)
sc.set(68, 92, NEON_CG)
sc.set(66, 86, NEON_CG)
sc.set(66, 87, NEON_CG)
sc.line(59, 95, 59, 103, NEON_MG)
sc.set(60, 93, NEON_MG)
sc.set(62, 86, "#ff9fd4")
sc.set(67, 105, NEON_CG)
for x in (61, 63, 65, 66):
    sc.set(x, 114, "#2b3765")

# ----------------------------------- transparent umbrella (stencilled canopy)
um = new_canvas(W, H, name="umbrella")
CANOPY = "#a9dcf2"
um.path("M 50 82 Q 64 65 78 82 Z", CANOPY)
for d in ["M 51 81 Q 57 70 64 66", "M 77 81 Q 71 70 64 66",
          "M 57 82 Q 60 72 64 66", "M 71 82 Q 68 72 64 66"]:
    um.path(d, "#8fd3ea", fill=False)
# punch a checker of holes so the scene reads through the canopy
for y in range(64, 83):
    for x in range(48, 81):
        if (x + y) % 2 == 0:
            um.set(x, y, None)
# crisp wet rim + tip, drawn solid after stencilling
um.path("M 50 82 Q 64 65 78 82", "#dff6ff", fill=False)
um.line(64, 63, 64, 66, "#dff6ff")
um.set(50, 83, "#dff6ff")
um.set(78, 83, "#dff6ff")
# shaft and handle down to the raised hand
um.line(69, 77, 69, 97, "#9fb6c6")
um.set(68, 97, "#9fb6c6")

# bright foreground rain through the lit centre
for i in range(44):
    rx = random.randrange(34, 98)
    ry = random.randrange(12, 122)
    L = random.choice([3, 4, 5, 6])
    col = "#8190c6" if random.random() < 0.55 else "#c9e4f5"
    um.line(rx, ry, rx - 1, ry + L, col)

result = flatten([sc, um], name="result")
print(result.stats_text())
view(result)
save("cyberpunk_alley", result)
finish(result)
