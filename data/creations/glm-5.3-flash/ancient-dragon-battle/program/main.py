try:
    from pixelbench_api import *  # noqa: F401,F403
except Exception:
    pass

W = H = 256
OUTLINE = "#0d0913"


def h32(x, y, s=0):
    return ((x * 2654435761) ^ (y * 40503) ^ (s * 97)) & 0xFFFFFFFF


def texture(c, x0, y0, x1, y1, light, dark, step=3, seed=1):
    for yy in range(y0, y1, step):
        for xx in range(x0, x1, step):
            v = h32(xx, yy, seed)
            if v % 7 == 0:
                c.set(xx, yy, light)
            elif v % 11 == 0:
                c.set(xx, yy, dark)


def flames(c, x0, ybase, hs):
    """Tongued fire: hs = one peak height per 4px step."""
    def tongue(scale, col):
        pts = [(x0, ybase)]
        for i, h in enumerate(hs):
            pts.append((x0 + i * 4 + 2, ybase - max(1, int(h * scale))))
        pts.append((x0 + len(hs) * 4, ybase))
        c.poly(pts, col)
    tongue(1.0, "#ff5a2a")
    tongue(0.66, "#ff9a3a")
    tongue(0.34, "#ffd06b")


def knight(c, x, y, shield="#8a2a26", ov=None):
    k = (lambda col: ov if ov else col)
    c.line(x + 3, y - 12, x + 3, y - 1, k("#c8b088"))
    c.set(x + 3, y - 13, k("#efe4c0"))
    c.set(x, y - 1, k("#241c26"))
    c.set(x + 2, y - 1, k("#241c26"))
    c.rect(x, y - 6, 3, 5, k("#8a92a4"))
    c.rect(x, y - 8, 3, 2, k("#b8c0d0"))
    c.set(x + 1, y - 8, k("#d8dee8"))
    c.rect(x - 2, y - 6, 2, 4, k(shield))
    c.set(x - 2, y - 5, k("#d8c8a0"))


def outlined_knight(c, x, y, shield):
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        knight(c, x + dx, y + dy, shield, ov=OUTLINE)
    knight(c, x, y, shield)


def soldier(c, x, y, h, shield="#8a2a26", big=False):
    hb = max(2, (h * 2) // 5)
    hs = max(2, h // 3)
    sx = x + hs + 1
    c.line(sx, y - h - 2, sx, y - 1, "#c8b088")
    c.set(sx, y - h - 3, "#efe4c0")
    c.rect(x - hs // 2 - 1, y - hb - hs, hs, hs, "#9aa2b4")
    c.rect(x - hs // 2 - 1, y - hb, hs + 1, hb, "#565a68")
    sw = 3 if big else 2
    c.rect(x - hs // 2 - 1 - sw, y - hb - 1, sw, hb + 2, shield)
    if big:
        c.set(x - hs // 2 - sw + 1, y - hb, "#d8c8a0")


def horseman(c, x, y, col="#1c1424"):
    c.ellipse(x, y - 4, 7, 3, col)
    c.ellipse(x - 8, y - 7, 3, 2, col)
    c.line(x - 6, y - 2, x - 7, y + 1, col)
    c.line(x - 3, y - 2, x - 3, y + 1, col)
    c.line(x + 3, y - 2, x + 3, y + 1, col)
    c.line(x + 6, y - 2, x + 7, y + 1, col)
    c.rect(x - 1, y - 11, 3, 5, col)
    c.set(x, y - 12, col)
    c.line(x + 2, y - 17, x + 2, y - 9, "#8a6a3a")
    c.line(x + 2, y - 17, x + 7, y - 15, "#8a2a26")


def arrow(c, x0, y0, x1, y1, col="#d8c8a0"):
    c.line(x0, y0, x1, y1, col)
    c.set(x1, y1, "#f0ead4")
    c.set(x0, y0, "#8a7a58")
    c.set(x0 + (1 if x1 >= x0 else -1), y0, "#8a7a58")


# =================================================================== SKY
sky = new_canvas(W, H, name="sky")

BANDS = [
    (0, "#221238"), (18, "#2c1848"), (36, "#3c1f56"), (54, "#562564"),
    (72, "#7c305e"), (88, "#9e3957"), (104, "#bc4849"), (120, "#d86640"),
    (136, "#f08b47"), (150, "#ffb35c"),
]
for i, (y0, col) in enumerate(BANDS):
    y1 = BANDS[i + 1][0] if i + 1 < len(BANDS) else 164
    sky.rect(0, y0, W, y1 - y0, col)
    if i + 1 < len(BANDS):
        sky.dither(0, y1 - 1, W, 2, [col, BANDS[i + 1][1]], pattern="checker")

# low sun on the far ridge
sky.circle(216, 118, 22, "#ffcf7a")
sky.circle(216, 118, 15, "#ffe9a8")
sky.circle(216, 114, 8, "#fff6cf")

# dark cloud streaks overhead
sky.ellipse(56, 28, 46, 6, "#1a0d2c")
sky.ellipse(150, 20, 40, 5, "#180c2a")
sky.ellipse(214, 38, 34, 5, "#1e1030")
sky.ellipse(36, 64, 44, 7, "#2a1540")
sky.ellipse(118, 76, 52, 8, "#331a48")
sky.ellipse(236, 68, 30, 6, "#2a1540")
# streaks lit by the sun
sky.ellipse(196, 98, 36, 4, "#c8503f")
sky.ellipse(228, 108, 26, 3, "#e8703c")
sky.ellipse(194, 111, 22, 3, "#f79a4a")
sky.ellipse(218, 93, 20, 2, "#ffb35c")
sky.rect(160, 104, 60, 1, "#ffcf7a")
sky.rect(190, 96, 50, 1, "#ffb35c")

# distant wyverns
for bx, by in ((40, 54), (56, 46), (84, 58)):
    sky.line(bx, by, bx + 2, by - 1, "#20122e")
    sky.line(bx + 2, by - 1, bx + 4, by, "#20122e")

# =================================================================== LAND
land = new_canvas(W, H, name="land")

land.poly([(0, 146), (24, 124), (52, 140), (84, 112), (112, 138), (146, 120),
           (178, 140), (206, 126), (232, 142), (256, 130), (256, 158), (0, 158)],
          "#2e1a3e")
land.poly([(0, 150), (36, 132), (74, 148), (116, 130), (156, 148), (196, 134),
           (236, 150), (256, 140), (256, 172), (0, 172)], "#221232")

land.rect(0, 152, W, 18, "#33241a")
land.rect(0, 168, W, 24, "#2a1d15")
land.rect(0, 190, W, 28, "#22170f")
land.rect(0, 216, W, 40, "#1a110b")
land.dither(0, 167, W, 2, ["#33241a", "#2a1d15"], pattern="checker")
land.dither(0, 189, W, 2, ["#2a1d15", "#22170f"], pattern="checker")
land.dither(0, 215, W, 2, ["#22170f", "#1a110b"], pattern="checker")
for yy in range(154, 256, 3):
    for xx in range(0, W, 3):
        v = h32(xx, yy, 5)
        if v % 19 == 0:
            land.set(xx, yy, "#150e09")
        elif v % 23 == 0:
            land.set(xx, yy, "#3f2e1e")

land.poly([(116, 152), (130, 152), (146, 196), (168, 256), (92, 256), (108, 196)],
          "#3a2a1c")
land.poly([(120, 152), (126, 152), (134, 200), (146, 256), (112, 256), (122, 200)],
          "#443222")

for px in (18, 28, 226, 238):
    land.line(px, 152, px, 140, "#1a1220")

for fx, fy in ((36, 176), (226, 188), (88, 200)):
    land.circle(fx, fy, 3, "#8a2a20")
    land.circle(fx, fy, 2, "#ff7a2a")
    land.set(fx, fy - 1, "#ffd06b")

land.poly([(34, 150), (56, 126), (84, 116), (120, 112), (158, 114), (186, 124),
           (210, 148)], "#33241a")
land.poly([(34, 150), (56, 126), (84, 116), (98, 116), (72, 132), (54, 150)],
          "#241a12")
for rx, ry in ((70, 136), (96, 128), (150, 126), (176, 134), (60, 144), (192, 142)):
    land.set(rx, ry, "#241a12")
    land.set(rx + 1, ry, "#3f2e20")

# =================================================================== CASTLE
castle = new_canvas(W, H, name="castle")
STONE, STONE_D, STONE_L = "#423e4a", "#2f2b38", "#504b5a"
WIN = "#1a1620"
WARM = "#5a3230"

castle.rect(64, 102, 130, 26, STONE)                      # curtain wall
for mx in range(66, 192, 9):
    castle.rect(mx, 96, 5, 6, STONE)
castle.rect(56, 76, 22, 52, STONE)                        # left tower
castle.rect(53, 70, 28, 7, STONE_D)
for mx in (54, 60, 66, 72):
    castle.rect(mx, 64, 4, 6, STONE)
castle.rect(170, 74, 24, 54, STONE)                       # right tower, broken top
castle.rect(94, 80, 54, 48, STONE)                        # great keep
castle.rect(91, 74, 60, 7, STONE_D)
for mx in range(92, 141, 6):
    castle.rect(mx, 68, 4, 6, STONE)
castle.rect(110, 108, 28, 20, STONE_D)                    # gatehouse
castle.poly([(118, 128), (118, 118), (124, 113), (130, 118), (130, 128)], "#141018")
for gx in (121, 124, 127):
    castle.line(gx, 121, gx, 128, "#5a5464")

texture(castle, 64, 96, 194, 128, STONE_L, STONE_D, 3, 3)
texture(castle, 56, 64, 78, 122, STONE_L, STONE_D, 3, 7)
texture(castle, 170, 74, 194, 122, STONE_L, STONE_D, 3, 11)
texture(castle, 94, 68, 148, 122, STONE_L, STONE_D, 3, 13)

for wx, wy in ((62, 88), (68, 100), (176, 88), (184, 100)):
    castle.rect(wx, wy, 2, 5, WIN)
for wx, wy in ((102, 90), (116, 90), (130, 90)):
    castle.rect(wx, wy, 3, 6, WIN)
for wx, wy in ((65, 110), (180, 112), (109, 104), (123, 104)):
    castle.rect(wx, wy, 2, 5, "#ff8a2a")
castle.rect(188, 118, 2, 4, "#ffb03a")

# ---- fire (drawn before the outline pass, battlements go back on top) ----
castle.ellipse(122, 74, 24, 4, "#a03024")
flames(castle, 104, 76, [16, 22, 13, 19, 24, 15, 20, 12, 17, 14])   # keep roof
flames(castle, 170, 74, [14, 18, 11, 16, 20, 12])                   # broken tower
flames(castle, 152, 100, [8, 11, 7, 10, 13])                        # wall top

# battlements re-drawn over the fire
castle.rect(91, 74, 60, 7, STONE_D)
for mx in range(92, 141, 6):
    castle.rect(mx - 1, 67, 6, 8, OUTLINE)
    castle.rect(mx, 68, 4, 6, STONE)
castle.rect(100, 75, 44, 2, WARM)
CROWN = [(168, 76), (170, 64), (174, 68), (178, 58), (182, 66), (186, 60),
         (190, 68), (194, 64), (196, 76)]
castle.poly(CROWN, STONE)
for i in range(len(CROWN) - 1):
    castle.line(CROWN[i][0], CROWN[i][1], CROWN[i + 1][0], CROWN[i + 1][1], OUTLINE)
castle.rect(172, 70, 20, 3, WARM)
for mx in (156, 165):
    castle.rect(mx - 1, 95, 7, 8, OUTLINE)
    castle.rect(mx, 96, 5, 6, STONE)

castle.outline(OUTLINE)

KNIGHTS = [(68, 102, "#8a2a26"), (78, 102, "#2a4a6a"), (88, 102, "#8a2a26"),
           (104, 102, "#2a4a6a"), (118, 102, "#8a2a26"), (132, 102, "#2a4a6a"),
           (144, 102, "#8a2a26"), (62, 70, "#8a2a26"), (70, 70, "#2a4a6a"),
           (96, 74, "#8a2a26"), (144, 74, "#2a4a6a")]
for kx, ky, kc in KNIGHTS:
    outlined_knight(castle, kx, ky, kc)

# banners
castle.line(62, 44, 62, 64, "#5a4630")
castle.poly([(62, 44), (62, 53), (75, 48)], "#a03028")
castle.line(146, 52, 146, 74, "#5a4630")
castle.poly([(146, 52), (146, 61), (159, 56)], "#a03028")

# ---- smoke ----------------------------------------------------------
SMOKE = ["#3e3848", "#494256", "#544e62"]
plume = [(140, 50, 6), (150, 42, 7), (162, 33, 8), (176, 24, 9), (190, 16, 10),
         (206, 12, 11), (222, 15, 11)]
for i, (px, py, pr) in enumerate(plume):
    castle.ellipse(px, py, pr, max(3, int(pr * 0.8)), SMOKE[i % 3])
    if i % 2 == 0:
        castle.ellipse(px + 1, py - 1, max(2, pr - 4), max(2, pr - 5), "#655d72")
plume2 = [(178, 62, 4), (182, 54, 5), (186, 46, 5), (190, 38, 6)]
for i, (px, py, pr) in enumerate(plume2):
    castle.ellipse(px, py, pr, max(3, int(pr * 0.8)), SMOKE[(i + 1) % 3])

EMBERS = [(146, 56), (152, 50), (136, 48), (142, 44),
          (186, 12), (194, 8), (202, 6), (210, 9), (218, 13), (226, 18), (234, 24),
          (168, 58), (176, 56), (184, 54), (192, 52),
          (150, 88), (158, 84), (166, 86), (174, 90)]
EMBER_C = ["#ffd06b", "#ff9a3a", "#ff5a2a"]
for i, (ex, ey) in enumerate(EMBERS):
    castle.set(ex, ey, EMBER_C[i % 3])

# =================================================================== DRAGON
dragon = new_canvas(W, H, name="dragon")
BODY, BODY_L = "#16101f", "#3a2c44"
MEMB, MEMB_D = "#261c38", "#1d1528"
RIM = "#c05648"

# far wing, raised behind the head
dragon.poly([(176, 30), (112, 2), (122, 12), (118, 16), (136, 18), (132, 22),
             (150, 24), (158, 30)], MEMB_D)
dragon.line(168, 28, 120, 8, OUTLINE)

# tail with spikes
dragon.poly([(196, 36), (218, 28), (238, 32), (254, 38), (252, 46), (236, 42),
             (216, 38), (198, 48)], BODY)
dragon.poly([(244, 38), (256, 36), (252, 50)], BODY)
dragon.poly([(208, 32), (212, 25), (215, 33)], BODY)
dragon.poly([(224, 30), (228, 23), (231, 32)], BODY)
dragon.poly([(240, 34), (244, 28), (246, 36)], BODY)

# body, neck, head, jaw, tucked legs
dragon.ellipse(178, 42, 26, 10, BODY)
dragon.poly([(134, 24), (156, 20), (162, 32), (144, 38)], BODY)
dragon.poly([(102, 28), (110, 20), (124, 14), (138, 20), (142, 28), (132, 36),
             (114, 36)], BODY)
dragon.poly([(100, 32), (114, 36), (128, 40), (124, 45), (110, 41), (98, 37)], BODY)
dragon.poly([(160, 48), (168, 46), (170, 56), (162, 56)], BODY)
dragon.poly([(186, 48), (194, 46), (196, 56), (188, 56)], BODY)

# near wing, sweeping down toward the burning tower
dragon.poly([(186, 40), (208, 50), (228, 64), (244, 76), (238, 84), (230, 72),
             (222, 78), (212, 64), (204, 68), (196, 58)], MEMB)
dragon.line(192, 46, 226, 70, OUTLINE)
dragon.line(192, 46, 206, 62, OUTLINE)

dragon.outline(OUTLINE)

# horns (lighter so they read against the far wing)
dragon.poly([(128, 24), (142, 14), (144, 18), (132, 27)], BODY_L)
dragon.poly([(136, 28), (150, 20), (151, 24), (139, 31)], BODY_L)
dragon.set(142, 15, RIM)
dragon.set(150, 21, RIM)

# eye, mouth fire, teeth
dragon.set(128, 24, "#ffb03a")
dragon.set(129, 24, "#ffd06b")
dragon.set(128, 25, "#ffd06b")
dragon.poly([(102, 34), (120, 37), (130, 41), (122, 44), (106, 42), (100, 38)],
            "#ff5a2a")
for tx, ty in ((104, 35), (110, 36), (116, 37), (122, 38), (127, 40)):
    dragon.set(tx, ty, "#e8e4d8")

# rim light
RIM_PTS = [(114, 4), (122, 7), (130, 11), (138, 15), (146, 18), (162, 26), (170, 29),
           (124, 43), (118, 41), (110, 40), (102, 37),
           (158, 51), (166, 51), (174, 51), (182, 51), (190, 51), (198, 50),
           (162, 55), (168, 55), (188, 55), (194, 55),
           (246, 48), (238, 44), (228, 41), (214, 41), (204, 46),
           (190, 43), (196, 46), (202, 49), (207, 51), (212, 55), (218, 59),
           (224, 63), (232, 69), (238, 74), (240, 82)]
for rx, ry in RIM_PTS:
    dragon.set(rx, ry, RIM)
for bx, by in ((156, 49), (164, 49), (172, 49), (180, 49), (188, 49)):
    dragon.set(bx, by, BODY_L)

# fire breath onto the keep roof
dragon.poly([(106, 36), (114, 42), (120, 52), (126, 62), (130, 72), (120, 70),
             (112, 76), (104, 68), (102, 56), (104, 44)], "#ff5a2a")
dragon.poly([(108, 40), (116, 48), (122, 58), (126, 66), (118, 66), (110, 60),
             (106, 50)], "#ff9a3a")
dragon.poly([(110, 44), (116, 52), (120, 60), (122, 64), (114, 62), (110, 54)],
            "#ffd06b")
for sx, sy, sc in ((118, 70, "#ffe08a"), (110, 72, "#ffe08a"), (124, 68, "#ffe08a"),
                   (128, 74, "#ff9a3a"), (106, 64, "#ff9a3a")):
    dragon.set(sx, sy, sc)

# =================================================================== ARMY
army = new_canvas(W, H, name="army")
WOOD, WOOD_D, WOOD_L = "#4a3423", "#2f2015", "#5f4630"

army.rect(12, 154, 46, 88, "#3a2a1c")
army.rect(16, 158, 38, 80, WOOD)
for bx in (16, 30, 44):
    army.rect(bx, 154, 3, 88, WOOD_D)
for by in (168, 182, 196, 210, 224):
    army.rect(12, by, 46, 3, WOOD_D)
army.rect(8, 140, 54, 16, WOOD)
army.rect(6, 136, 58, 5, WOOD_D)
army.rect(22, 144, 14, 10, "#1a120c")
army.set(27, 147, "#9aa2b4")
army.rect(26, 149, 3, 4, "#565a68")
army.rect(58, 142, 7, 46, WOOD_L)
army.line(62, 138, 62, 142, WOOD_D)
for cx in (24, 46):
    army.circle(cx, 246, 8, WOOD_D)
    army.circle(cx, 246, 4, "#1a120c")
    army.line(cx - 6, 246, cx + 6, 246, WOOD)
    army.line(cx, 240, cx, 252, WOOD)

army.rect(198, 162, 44, 80, "#3a2a1c")
army.rect(202, 166, 36, 72, WOOD)
for bx in (202, 214, 226):
    army.rect(bx, 162, 3, 80, WOOD_D)
for by in (176, 190, 204, 218):
    army.rect(198, by, 44, 3, WOOD_D)
army.rect(194, 148, 52, 16, WOOD)
army.rect(192, 144, 56, 5, WOOD_D)
army.rect(208, 152, 14, 10, "#1a120c")
army.set(214, 155, "#9aa2b4")
army.rect(213, 157, 3, 4, "#565a68")
army.rect(191, 150, 7, 44, WOOD_L)
for cx in (210, 232):
    army.circle(cx, 246, 7, WOOD_D)
    army.circle(cx, 246, 3, "#1a120c")
    army.line(cx - 5, 246, cx + 5, 246, WOOD)

horseman(army, 86, 174)
horseman(army, 128, 170)
horseman(army, 168, 174)

army.outline("#100c14")

army.line(138, 158, 148, 104, WOOD_L)
army.line(144, 158, 154, 104, WOOD_L)
for i in range(9):
    t = i / 8.0
    yy = int(158 - 54 * t)
    xa = int(138 + 10 * t)
    xb = int(144 + 10 * t)
    army.line(xa, yy, xb, yy, WOOD)

ROWS = [(176, 4, range(80, 181, 8)), (188, 5, range(74, 186, 9)),
        (202, 6, range(70, 191, 10)), (218, 7, range(72, 191, 12)),
        (238, 9, range(70, 193, 16))]
for ri, (fy, fh, xs) in enumerate(ROWS):
    for si, sx in enumerate(xs):
        shield = "#8a2a26" if (si + ri) % 2 == 0 else "#2a4a6a"
        soldier(army, sx, fy, fh, shield, big=(ri == 4))

for bxx, byy, bhh in ((104, 238, 9), (150, 218, 7)):
    soldier(army, bxx, byy, bhh, "#8a2a26", big=True)
    army.line(bxx - 4, byy - bhh - 9, bxx - 4, byy - 1, "#5a4630")
    army.rect(bxx - 4, byy - bhh - 9, 7, 5, "#a03028")
    army.set(bxx + 2, byy - bhh - 7, "#d8c8a0")

for ax0, ay0, ax1, ay1 in ((24, 148, 46, 130), (44, 164, 70, 144),
                           (96, 148, 118, 130), (150, 156, 174, 136),
                           (182, 168, 206, 148), (210, 138, 232, 120),
                           (120, 168, 142, 150), (60, 132, 80, 116)):
    arrow(army, ax0, ay0, ax1, ay1)
for ax0, ay0, ax1, ay1 in ((96, 250, 104, 240), (140, 254, 150, 244),
                           (176, 248, 184, 238), (30, 236, 38, 226)):
    army.line(ax0, ay0, ax1, ay1, "#6a5230")
    army.set(ax1, ay1, "#c8b088")

for tx, ty in ((68, 244), (190, 246)):
    army.line(tx, ty, tx, ty - 8, WOOD)
    army.circle(tx, ty - 10, 2, "#ff9a3a")
    army.set(tx, ty - 11, "#ffd06b")
for dx, dy, dr in ((96, 232, 5), (150, 240, 6), (120, 252, 7), (206, 236, 4)):
    army.ellipse(dx, dy, dr, 2, "#171008")
army.line(90, 236, 100, 240, "#6a5230")
army.line(160, 246, 172, 242, "#6a5230")
for ex, ey in ((70, 230), (192, 232), (110, 224), (160, 228), (86, 214),
               (176, 212), (140, 210)):
    army.set(ex, ey, "#ff9a3a")

# =================================================================== FLATTEN
result = flatten([sky, land, castle, dragon, army], name="result")
print(result.stats_text())
print(len(result.palette()), "palette entries")
finish(result)
