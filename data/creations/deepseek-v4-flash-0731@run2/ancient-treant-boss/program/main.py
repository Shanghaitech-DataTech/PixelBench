import random
random.seed(2024)
FINISH = True

W = 256
main = new_canvas(256, 256, name="treant")

def C(spec, name):
    return main.color(spec, name)

OUT = C("#070503", "out")
EDGE = C("#120b06", "edge")
TD  = C("#201406", "td")
TM  = C("#3a260f", "tm")
TL  = C("#543817", "tl")
TH  = C("#6b4a1e", "th")
TRc = C("#835e26", "rim")
TR2 = C("#a07a32", "rim2")
M1  = C("#2f5c1d", "moss1")
M2  = C("#3f7c26", "moss2")
M3  = C("#55a02e", "moss3")
MD  = C("#234717", "mossd")
VN1 = C("#1b3a12", "vine1")
VN2 = C("#2a4d1b", "vine2")
EYE = C("#46e020", "eye")
HOT = C("#c8ff9a", "hot")
PUP = C("#0a1405", "pupil")
MOU = C("#040604", "mouth")
TTH = C("#4a3a20", "tooth")
G1  = C("#2f5f30", "grass1")
G2  = C("#254c26", "grass2")
G3  = C("#3a7036", "grass3")

# ---- background forest ----
bands = [(0, 40, "#050d08"), (40, 95, "#08150d"), (95, 150, "#0a1a10"), (150, 205, "#0e2115"), (205, 256, "#132a1a")]
for y0, y1, hx in bands:
    main.rect(0, y0, 256, y1 - y0, main.color(hx))

# vignette + distant trunks
main.rect(0, 0, 12, 256, main.color("#040a06"))
main.rect(244, 0, 12, 256, main.color("#040a06"))
main.rect(12, 0, 10, 256, main.color("#07110a"))
main.rect(234, 0, 10, 256, main.color("#07110a"))
main.rect(20, 0, 6, 256, main.color("#0a1710"))
main.rect(28, 0, 3, 256, main.color("#08130c"))
main.rect(225, 0, 3, 256, main.color("#08130c"))
main.rect(231, 0, 6, 256, main.color("#0a1710"))

# a few dark distant trunks
for (tx, ty, thh, tw) in [(6, 90, 120, 6), (8, 40, 60, 5), (244, 70, 100, 5), (196, 14, 40, 4), (58, 10, 46, 4), (206, 190, 46, 4)]:
    main.rect(tx, ty, tw, thh, main.color("#0c1810"))
    main.line(tx + tw // 2 - 1, ty, tx + tw // 2 + 2, ty, main.color("#101e15"))

# ---- god rays (narrow beams through canopy gaps) ----
rays = new_canvas(256, 256, name="rays")
rays.poly([(58, -10), (84, -10), (90, 70), (46, 70)], rays.color((200, 232, 160, 64)))
rays.poly([(98, -10), (150, -10), (140, 62), (106, 62)], rays.color((214, 242, 175, 78)))
rays.poly([(120, -10), (142, -10), (134, 34), (124, 34)], rays.color((228, 248, 200, 64)))
rays.poly([(168, -10), (196, -10), (206, 84), (172, 84)], rays.color((196, 228, 150, 56)))
rays.poly([(86, 8), (172, 8), (158, 76), (98, 76)], rays.color((150, 192, 122, 22)))
main.blit(rays, 0, 0)

# ---- ground ----
main.rect(0, 196, 256, 60, main.color("#1d3a26"))
main.ellipse(64, 238, 72, 20, main.color("#255137"))
main.ellipse(196, 240, 58, 17, main.color("#255137"))
main.ellipse(128, 246, 92, 12, main.color("#2c5a3c"))
main.rect(0, 248, 256, 8, main.color("#16331f"))

pools = new_canvas(256, 256, name="pools")
pools.ellipse(70, 238, 60, 17, pools.color((170, 200, 130, 30)))
pools.ellipse(190, 240, 54, 15, pools.color((165, 195, 125, 26)))
main.blit(pools, 0, 0)

def mirror(pts, cx=128):
    return [(2 * cx - x, y) for (x, y) in pts]

# ---- treant silhouette ----
body = [(84, 224), (80, 206), (75, 184), (77, 160), (71, 136), (75, 114), (81, 98),
        (87, 87), (95, 78), (105, 70), (116, 64), (128, 62), (140, 64), (150, 70),
        (158, 80), (164, 92), (170, 108), (176, 128), (181, 150), (177, 172), (181, 194),
        (176, 216), (128, 222)]

body_hl = [(84, 224), (80, 206), (75, 184), (77, 160), (71, 136), (75, 114), (81, 98),
          (87, 87), (95, 78), (105, 70), (116, 64), (112, 66), (104, 72), (97, 82),
          (90, 94), (85, 110), (81, 128), (80, 152), (80, 176), (84, 202), (88, 222)]

main.poly(body, TM)
main.poly([(128, 62), (140, 64), (150, 70), (158, 80), (164, 92), (170, 108), (176, 128),
           (181, 150), (177, 172), (181, 194), (176, 216), (128, 222)], TD)
main.poly(body_hl, TL)

left_shoulder = [(56, 152), (38, 132), (34, 114), (41, 106), (50, 114), (64, 132), (76, 150)]
right_shoulder = mirror(left_shoulder)
main.poly(left_shoulder, TM)
main.poly(right_shoulder, TM)
main.poly(mirror([(56, 152), (44, 138), (38, 122), (40, 112), (46, 118), (58, 136), (70, 148)]), TD)

left_arm = [(62, 140), (44, 116), (32, 92), (28, 70), (31, 60), (39, 64), (43, 78), (50, 98), (66, 126)]
right_arm = mirror(left_arm)
left_arm_hl = [(62, 140), (48, 120), (38, 100), (36, 90), (40, 95), (46, 108), (58, 130)]
main.poly(left_arm, TM)
main.poly(right_arm, TM)
main.poly(left_arm_hl, TL)
main.poly(mirror(left_arm_hl), TL)

# claws
clawsL = [((30, 62), (14, 34)), ((34, 58), (17, 24)), ((38, 63), (26, 30)),
         ((42, 69), (31, 40)), ((46, 76), (37, 50))]
clawsR = [((226, 62), (242, 34)), ((222, 58), (239, 24)), ((218, 63), (230, 30)),
          ((214, 69), (225, 40)), ((210, 76), (219, 50))]
for a, b in clawsL:
    main.line(a[0], a[1], b[0], b[1], EDGE)
    main.line(a[0] - 1, a[1] + 1, b[0] - 1, b[1] + 1, EDGE)
for a, b in clawsR:
    main.line(a[0], a[1], b[0], b[1], EDGE)
    main.line(a[0] + 1, a[1] + 1, b[0] + 1, b[1] + 1, EDGE)

# crown branches
crown = [((104, 68), (96, 44)), ((112, 63), (108, 32)), ((121, 62), (118, 24)),
        ((134, 62), (138, 24)), ((144, 63), (148, 32)), ((152, 67), (158, 44))]
for a, b in crown:
    main.line(a[0], a[1], b[0], b[1], EDGE)
    main.line(a[0] - 1, a[1] + 1, b[0] - 1, b[1] + 1, EDGE)
    main.line(a[0] + 1, a[1] + 1, b[0] + 1, b[1] + 1, EDGE)
    main.line(a[0], a[1], b[0], b[1], TD)
    main.line(a[0] - 1, a[1] + 1, b[0] - 1, b[1] + 1, TD)
for a, b in [((108, 32), (100, 14)), ((118, 24), (122, 6)), ((138, 24), (134, 8)),
            ((148, 32), (156, 16)), ((38, 112), (28, 90)), ((42, 108), (26, 84)),
            ((218, 112), (228, 90)), ((214, 108), (230, 84)),
            ((100, 44), (86, 30)), ((96, 40), (78, 26)), ((158, 44), (174, 36)),
            ((164, 40), (182, 30)), ((126, 14), (136, 2)), ((132, 10), (126, 0)),
            ((44, 96), (52, 80)), ((212, 96), (204, 80)), ((48, 70), (58, 58)),
            ((206, 70), (198, 58))]:
    main.line(a[0], a[1], b[0], b[1], EDGE)
    main.line(a[0] - 1, a[1] + 1, b[0] - 1, b[1] + 1, EDGE)
# twig joints
for (jx, jy) in [(108, 32), (118, 24), (138, 24), (148, 32), (100, 44), (158, 44), (122, 6), (134, 8)]:
    main.circle(jx, jy, 2, EDGE)
# foliage tufts at tips
for (fx, fy) in [(100, 14), (122, 6), (134, 8), (156, 16), (86, 30), (78, 26), (174, 36), (182, 30),
                (136, 2), (126, 0), (58, 58), (198, 58), (204, 80), (52, 80), (28, 90), (230, 90)]:
    for _ in range(3):
        main.circle(fx + random.randint(-3, 3), fy + random.randint(-2, 3), random.randint(1, 2),
                   random.choice([MD, M1, VN1]))
    main.circle(fx, fy, random.randint(0, 1), VN2)

# roots
left_root_rise = [(78, 218), (58, 204), (46, 186), (40, 170), (47, 165), (55, 178), (66, 194), (84, 212)]
right_root_rise = mirror(left_root_rise)
main.poly(left_root_rise, TM)
main.poly(right_root_rise, TM)
baseL = [(82, 222), (60, 228), (38, 234), (32, 240), (40, 244), (62, 240), (88, 232)]
baseR = mirror(baseL)
main.poly(baseL, TM)
main.poly(baseR, TM)
main.poly([(104, 224), (94, 234), (90, 244), (98, 248), (108, 244), (116, 236)], TM)
main.poly([(152, 224), (162, 234), (166, 244), (158, 248), (148, 244), (140, 236)], TD)

# ---- bark texture ----
def barkline(x, y, l, sw, col):
    main.line(x, y, x + sw // 2, y + l // 2, col)
    main.line(x + sw // 2, y + l // 2, x + sw, y + l, col)

def face_area(x, y):
    if 97 <= x <= 159 and 88 <= y <= 152:
        return True
    if 104 <= x <= 152 and 92 <= y <= 106:
        return True
    return False

for _ in range(320):
    x = random.randint(86, 170)
    y = random.randint(74, 212)
    if face_area(x, y):
        continue
    col = EDGE if random.random() < 0.62 else TD
    barkline(x, y, random.randint(5, 12), random.randint(-4, 4), col)

for _ in range(150):
    x = random.randint(88, 148)
    y = random.randint(76, 208)
    if face_area(x, y):
        continue
    barkline(x, y, random.randint(3, 8), random.randint(-3, 3), TH)

for _ in range(16):
    x = random.randint(94, 162)
    y = random.randint(90, 206)
    if face_area(x, y):
        continue
    main.circle(x, y, random.randint(1, 2), TD)

# ---- moss ----
moss_zones = [(40, 108), (52, 124), (64, 142), (48, 86), (38, 102), (72, 152), (82, 172),
             (90, 190), (30, 112), (24, 92), (128, 70), (112, 146), (144, 146), (162, 70),
             (200, 120), (212, 92), (216, 110), (228, 86), (198, 140), (190, 160), (176, 184),
             (168, 202), (96, 220), (160, 220), (110, 232), (146, 232), (70, 210), (186, 210)]
for (zx, zy) in moss_zones:
    n = random.randint(3, 6)
    for _ in range(n):
        ox = zx + random.randint(-6, 6)
        oy = zy + random.randint(-5, 5)
        r = random.randint(1, 3)
        main.circle(ox, oy, r, random.choice([M1, MD]))
    for _ in range(2):
        ox = zx + random.randint(-4, 4)
        oy = zy + random.randint(-3, 3)
        main.circle(ox, oy, random.randint(1, 2), random.choice([M2, M3]))

# moss drapes on shoulders
for sx in range(14, 200, 4):
    for sy, n in [(110, 4), (126, 5), (142, 4)]:
        for k in range(n):
            main.circle(sx + random.randint(-3, 3), sy + random.randint(-2, 3), random.randint(1, 2),
                       random.choice([MD, M1]))

# ---- hanging vines ----
vine_starts = [(40, 122), (44, 120), (50, 116), (56, 126), (38, 96), (44, 88), (34, 72),
              (52, 96), (40, 68), (58, 134), (70, 140), (74, 150), (80, 152), (86, 172),
              (94, 188), (186, 172), (182, 150), (176, 152), (162, 140), (196, 120), (204, 96),
              (212, 86), (212, 70), (200, 68), (186, 126), (172, 134)]
for (vx, vy) in vine_starts:
    length = random.randint(16, 42)
    sway = random.randint(-8, 8)
    h1 = vy + length // 2
    main.line(vx, vy, vx + sway // 3, h1, VN1)
    main.line(vx + sway // 3, h1, vx + sway, vy + length, VN1)
    main.line(vx + 1, vy + 2, vx + 1 + sway // 3, h1 + 1, VN2)

# ---- eye glow (menacing angled brows) ----
glow = new_canvas(256, 256, name="glow")
for cx in (112, 144):
    glow.circle(cx, 98, 13, glow.color((150, 255, 110, 38)))
    glow.circle(cx, 98, 9, glow.color((110, 248, 80, 70)))
    glow.circle(cx, 98, 7, glow.color((85, 235, 55, 105)))
main.blit(glow, 0, 0)
for cx in (112, 144):
    main.circle(cx, 98, 5, EYE)
    main.ellipse(cx, 98, 1, 3, PUP)
    main.circle(cx - 1, 97, 1, HOT)
    main.circle(cx - 1, 100, 1, HOT)
    # angled bark brows (toward the middle = menacing)
    main.line(cx - 14, 86, cx + 4, 92, TD)
    main.line(cx - 13, 84, cx + 5, 91, EDGE)
    # heavy upper lid
    main.line(cx - 8, 92, cx + 9, 92, EDGE)
    main.poly([(cx - 12, 86), (cx + 8, 92), (cx + 8, 95), (cx - 12, 90)], EDGE)

# ---- mouth ----
main.poly([(104, 128), (110, 123), (116, 129), (122, 125), (128, 131), (134, 125), (140, 129),
           (146, 123), (152, 128), (148, 139), (140, 135), (134, 142), (128, 137), (122, 142),
           (116, 135), (110, 140)], MOU)
main.poly([(106, 132), (110, 126), (114, 131)], TTH)
main.poly([(120, 128), (124, 133), (128, 128)], TTH)
main.poly([(136, 133), (132, 127), (128, 132)], TTH)
main.poly([(146, 130), (142, 126), (138, 131)], TTH)

# ---- outlines ----
for shp in [body, left_shoulder, right_shoulder, left_arm, right_arm,
           left_root_rise, right_root_rise, baseL, baseR,
           [(104, 224), (94, 234), (90, 244), (98, 248), (108, 244), (116, 236)],
           [(152, 224), (162, 234), (166, 244), (158, 248), (148, 244), (140, 236)]]:
    main.poly(shp, OUT, fill=False)

# ---- rim light from god rays ----
left_edge = body[:12]
for (px, py) in left_edge:
    main.line(px, py, px + 5, py, TRc)
main.line(28, 70, 38, 82, TRc)
main.line(34, 56, 40, 66, TR2)
right_edge = [(2 * 128 - px, py) for (px, py) in body[:12]]
for (px, py) in right_edge:
    main.line(px, py, px - 4, py, TH)
main.circle(56, 152, 3, TRc)

# ---- armor knots / fissures ----
for (kx, ky) in [(92, 180), (104, 200), (122, 210), (142, 206), (156, 188), (170, 170), (88, 150),
                (164, 142), (110, 172), (146, 172), (84, 196), (172, 208), (120, 84), (136, 84),
                (84, 118), (172, 118), (96, 162), (158, 162)]:
    main.circle(kx, ky, random.choice([2, 2, 3]), TD)
    main.circle(kx + 1, ky + 1, 1, TH)

# ---- rocks / rubble ----
for (rx, ry, rr, col) in [(86, 246, 7, "#1a3022"), (170, 246, 6, "#182e20"), (58, 247, 5, "#1c3828"),
                         (200, 247, 5, "#1c3828"), (34, 242, 4, "#162c1c"), (222, 243, 4, "#162c1c")]:
    main.circle(rx, ry, rr, main.color(col))
    main.circle(rx - rr // 2, ry - rr // 2, 1, main.color("#2c5238"))
    main.circle(rx - rr // 2, ry - rr // 2, rr + 0, main.color(col), fill=False)

# ---- foreground grass ----
for _ in range(170):
    x = random.randint(4, 252)
    y = random.randint(236, 252)
    g = random.choice([G1, G2])
    main.line(x, y, x + random.randint(-2, 2), y - random.randint(5, 12), g)
    if random.random() < 0.4:
        main.line(x + 2, y - 2, x + random.randint(0, 3), y - random.randint(2, 6), G3)

# ---- floating spores ----
spores = new_canvas(256, 256, name="spores")
for _ in range(26):
    sx = random.randint(20, 70)
    sy = random.randint(10, 240)
    spores.circle(sx, sy, random.randint(0, 1), spores.color((210, 245, 180, 95)))
main.blit(spores, 0, 0)
for _ in range(8):
    sx = random.randint(20, 236)
    sy = random.randint(6, 240)
    main.circle(sx, sy, random.randint(0, 1), G3)

print(main.stats_text())
if FINISH:
    finish(main)
