from pixelbench_api import *

C = {
    'ink':   '#150a12', 'ink2':  '#2a1424',
    # sky
    'sky1':  '#120a20', 'sky2':  '#1e1030', 'sky3':  '#33153c', 'sky4': '#521c3e',
    'sky5':  '#7d2637', 'sky6':  '#ab3a2c', 'sky7':  '#d4582a', 'sky8': '#ef7f31',
    'sky9':  '#fba03c',
    'sun1':  '#ffb03a', 'sun2':  '#ffd25e', 'sun3':  '#ffe89a', 'sun4': '#fff6cf',
    'cl1':   '#241230', 'cl2':   '#3d1a3a', 'cl3':   '#6a2a3c', 'cl4':  '#a04438',
    'far1':  '#1d1029', 'far2':  '#2c1836', 'far3':  '#40203f',
    # ground
    'gnd1':  '#6b3a2e', 'gnd2':  '#452428', 'gnd3':  '#301a22', 'gnd4': '#22121b',
    'gnd5':  '#160c13', 'gndhi': '#9c5533',
    'rim1':  '#ff9a3c', 'rim2':  '#ffd07a',
    # knight
    'k_r0':  '#3d0a16', 'k_r1':  '#6b1223', 'k_r2':  '#9c1d2c', 'k_r3': '#c8312f',
    'k_r4':  '#ef5b3c', 'k_r5':  '#ff9163',
    'k_s0':  '#2b3242', 'k_s1':  '#4a5468', 'k_s2':  '#77839c', 'k_s3': '#a9b7ce',
    'k_s4':  '#dfe8f7',
    'k_g1':  '#7d5210', 'k_g2':  '#c9922a', 'k_g3':  '#f5cf63',
    'k_eye': '#ffe14d',
    'k_cp1': '#2c0713', 'k_cp2': '#4d0d1e', 'k_cp3': '#71152a', 'k_cp4': '#96203a',
    'k_le':  '#54392a',
    # rogue
    'g_c0':  '#0b2417', 'g_c1':  '#123a22', 'g_c2':  '#1d5c33', 'g_c3': '#2f8444',
    'g_c4':  '#4fae57', 'g_c5':  '#86d96e',
    'g_l0':  '#1c120c', 'g_l1':  '#33221a', 'g_l2':  '#54392a', 'g_l3': '#7d5739',
    'g_t1':  '#8a6a34', 'g_t2':  '#c39a4a',
    'g_m1':  '#39424f', 'g_m2':  '#6f7d92', 'g_m3':  '#a9b8cc', 'g_m4': '#e2ecf8',
    'g_eye': '#7dffb0', 'g_skin': '#e8bd93', 'g_sk2': '#b9825c', 'g_hair': '#cfdcec',
    # fx
    'fx1':   '#ffe9a8', 'fx2':   '#ff9a3c', 'fx3':   '#7dffb0', 'fx4':  '#ffffff',
}


def limb(c, x0, y0, x1, y1, w0, w1, col):
    dx, dy = float(x1 - x0), float(y1 - y0)
    L = (dx * dx + dy * dy) ** 0.5
    if L == 0:
        L = 1.0
    nx, ny = -dy / L, dx / L
    pts = [(int(round(x0 + nx * w0 / 2.0)), int(round(y0 + ny * w0 / 2.0))),
           (int(round(x1 + nx * w1 / 2.0)), int(round(y1 + ny * w1 / 2.0))),
           (int(round(x1 - nx * w1 / 2.0)), int(round(y1 - ny * w1 / 2.0))),
           (int(round(x0 - nx * w0 / 2.0)), int(round(y0 - ny * w0 / 2.0)))]
    c.poly(pts, col)


def seg(c, pts, widths, col):
    for i in range(len(pts) - 1):
        limb(c, pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1],
             widths[i], widths[i + 1], col)


# ---------------------------------------------------------------- background
def background(c):
    bands = [(0, 10, 'sky1'), (10, 10, 'sky2'), (20, 10, 'sky3'), (30, 10, 'sky4'),
             (40, 9, 'sky5'), (49, 9, 'sky6'), (58, 8, 'sky7'), (66, 8, 'sky8'),
             (74, 10, 'sky9')]
    for y, h, k in bands:
        c.rect(0, y, 128, h, C[k])
    for y, k1, k2 in [(8, 'sky1', 'sky2'), (18, 'sky2', 'sky3'), (28, 'sky3', 'sky4'),
                      (38, 'sky4', 'sky5'), (47, 'sky5', 'sky6'), (56, 'sky6', 'sky7'),
                      (64, 'sky7', 'sky8'), (72, 'sky8', 'sky9')]:
        c.dither(0, y, 128, 5, [C[k1], C[k2]], 'bayer4')

    # sun, half set behind the horizon
    c.circle(64, 82, 31, C['sun1'])
    c.circle(64, 82, 24, C['sun2'])
    c.circle(64, 82, 16, C['sun3'])
    c.circle(64, 82, 8, C['sun4'])

    # cloud streaks crossing the sky and the sun
    streaks = [
        (18, 30, 30, 3, 'cl1'), (78, 26, 34, 3, 'cl1'),
        (6, 42, 40, 4, 'cl2'), (86, 40, 38, 4, 'cl2'),
        (30, 52, 26, 3, 'cl2'), (74, 54, 30, 3, 'cl2'),
        (2, 62, 34, 4, 'cl3'), (94, 60, 32, 4, 'cl3'),
        (24, 70, 30, 3, 'cl3'), (76, 72, 34, 3, 'cl3'),
        (44, 60, 16, 2, 'cl4'), (70, 66, 18, 2, 'cl4'),
        (40, 76, 20, 2, 'cl4'), (72, 78, 22, 2, 'cl4'),
    ]
    for x, y, w, h, k in streaks:
        c.ellipse(x + w // 2, y, w // 2, h, C[k])
    # lit undersides on a few clouds
    for x, y, w in [(8, 65, 30), (96, 63, 28), (26, 73, 26), (78, 75, 30)]:
        c.line(x, y, x + w, y, C['rim1'])

    # distant ridge
    c.poly([(0, 84), (0, 74), (10, 68), (18, 74), (26, 66), (36, 76), (44, 72),
            (52, 80), (60, 84)], C['far2'])
    c.poly([(127, 84), (127, 72), (118, 66), (110, 74), (100, 64), (92, 74),
            (84, 70), (76, 80), (68, 84)], C['far2'])
    c.poly([(0, 84), (0, 78), (8, 74), (16, 79), (24, 73), (34, 81), (44, 78),
            (54, 84)], C['far1'])
    c.poly([(127, 84), (127, 77), (120, 73), (112, 79), (102, 72), (94, 80),
            (84, 77), (74, 84)], C['far1'])
    # broken tower silhouette on the left ridge
    c.poly([(14, 74), (14, 52), (18, 48), (22, 52), (22, 74)], C['far1'])
    c.poly([(14, 56), (22, 56), (22, 60), (14, 60)], C['far2'])
    c.poly([(108, 74), (108, 58), (112, 54), (116, 58), (116, 74)], C['far1'])

    # ground
    c.rect(0, 84, 128, 2, C['gnd1'])
    c.rect(0, 86, 128, 6, C['gnd2'])
    c.rect(0, 92, 128, 10, C['gnd3'])
    c.rect(0, 102, 128, 12, C['gnd4'])
    c.rect(0, 114, 128, 14, C['gnd5'])
    c.dither(0, 84, 128, 5, [C['gnd1'], C['gnd2']], 'bayer4')
    c.dither(0, 90, 128, 5, [C['gnd2'], C['gnd3']], 'bayer4')
    c.dither(0, 100, 128, 5, [C['gnd3'], C['gnd4']], 'bayer4')
    c.dither(0, 112, 128, 5, [C['gnd4'], C['gnd5']], 'bayer4')

    # sun reflection on the plain: broken light path, fading fast
    for y, w in [(85, 10), (88, 8), (91, 12), (95, 9), (99, 14), (104, 10),
                 (110, 16)]:
        c.rect(64 - w // 2, y, w, 1, C['gndhi'])
    for y, w in [(86, 12), (93, 14), (101, 16), (112, 20)]:
        c.dither(64 - w // 2, y, w, 2, [C['gndhi'], C['gnd2']], 'checker')
    # warm bounce under each fighter
    for x in (24, 98):
        c.line(x - 8, 86, x + 8, 86, C['gnd1'])

    # cracks radiating across the plain
    cracks = [(20, 120, 44, 104), (88, 100, 112, 116), (10, 96, 30, 92),
              (98, 92, 122, 98), (34, 126, 52, 116), (76, 124, 96, 112)]
    for x0, y0, x1, y1 in cracks:
        c.line(x0, y0, x1, y1, C['gnd5'])
        c.line(x0, y0 - 1, x1, y1 - 1, C['gnd3'])

    # scattered rocks
    for x, y, r in [(16, 100, 3), (54, 96, 2), (86, 106, 3), (112, 96, 2),
                    (40, 118, 4), (104, 122, 4), (8, 116, 3)]:
        c.circle(x, y, r, C['gnd4'])
        c.circle(x, y - 1, max(1, r - 2), C['gnd3'])
        c.set(x - 1, y - r, C['gnd1'])

    # contact shadows
    c.ellipse(23, 113, 22, 5, C['gnd5'])
    c.ellipse(98, 113, 22, 5, C['gnd5'])
    c.ellipse(23, 112, 15, 3, C['ink'])
    c.ellipse(98, 112, 15, 3, C['ink'])
    # small rim-lit rocks in the centre foreground
    for x, y, r in [(62, 116, 3), (70, 121, 2), (55, 123, 2)]:
        c.circle(x, y, r, C['gnd4'])
        c.circle(x, y - 1, max(1, r - 2), C['gnd3'])
        c.set(x - 1, y - r, C['rim1'])
        c.set(x, y - r, C['gndhi'])


# ---------------------------------------------------------------- knight
def knight(c):
    K = C
    # ---- cape, billowing back to the left ----
    c.path("M18,48 C6,56 -1,76 1,96 C2,106 8,112 15,110 C19,100 19,86 21,76 "
           "C23,66 26,56 28,50 Z", K['k_cp2'])
    c.path("M18,48 C9,58 3,78 5,95 C6,102 9,106 12,106 C14,95 15,82 18,72 "
           "C20,62 23,54 25,49 Z", K['k_cp1'])
    c.path("M20,52 C13,62 9,80 10,96", K['k_cp3'], fill=False)
    c.path("M24,54 C19,66 16,82 16,98", K['k_cp3'], fill=False)
    c.path("M6,88 C9,96 12,102 15,106", K['k_cp4'], fill=False)
    # tattered hem
    c.poly([(1, 96), (5, 104), (7, 96), (11, 106), (14, 98), (17, 108), (19, 100)],
           K['k_cp2'])

    # ---- far leg ----
    seg(c, [(19, 74), (16, 90), (15, 102)], [12, 10, 9], K['k_s0'])
    seg(c, [(19, 74), (16, 90), (15, 102)], [8, 7, 6], K['k_s1'])
    c.poly([(10, 101), (21, 101), (23, 111), (8, 111)], K['k_s0'])
    c.poly([(11, 103), (20, 103), (21, 108), (10, 108)], K['k_s1'])
    c.line(11, 109, 22, 109, K['k_s2'])

    # ---- near leg ----
    seg(c, [(28, 74), (31, 90), (32, 102)], [13, 11, 10], K['k_s1'])
    seg(c, [(29, 74), (32, 90), (33, 100)], [8, 7, 6], K['k_s2'])
    c.poly([(26, 101), (38, 101), (42, 111), (25, 111)], K['k_s0'])
    c.poly([(27, 103), (37, 103), (40, 108), (26, 108)], K['k_s1'])
    c.line(28, 109, 40, 109, K['k_s2'])
    # knee guards
    c.ellipse(16, 90, 5, 4, K['k_s1'])
    c.ellipse(32, 90, 5, 4, K['k_s2'])
    c.ellipse(32, 89, 3, 2, K['k_s3'])
    # tabard hanging between the legs
    c.poly([(19, 76), (27, 76), (26, 96), (23, 101), (20, 96)], K['k_r1'])
    c.poly([(21, 76), (27, 76), (26, 96), (23, 101)], K['k_r2'])
    c.poly([(24, 76), (27, 76), (26, 96), (24, 99)], K['k_r3'])
    c.line(20, 94, 26, 94, K['k_g2'])
    c.line(23, 80, 23, 92, K['k_g1'])

    # ---- faulds ----
    c.poly([(13, 68), (32, 68), (33, 78), (30, 85), (15, 85), (12, 78)], K['k_r1'])
    c.poly([(15, 68), (32, 68), (33, 78), (30, 85), (24, 85)], K['k_r2'])
    for y in (72, 76, 80):
        c.line(13, y, 32, y, K['k_r0'])
    c.line(15, 84, 30, 84, K['k_r0'])

    # ---- greatsword (drawn behind the torso, blade up to the left) ----
    # blade
    c.poly([(11, 38), (15, 37), (8, 6), (6, 3), (4, 7)], K['k_s2'])
    c.poly([(11, 38), (13, 37), (7, 6), (6, 3), (5, 6)], K['k_s3'])
    c.line(12, 36, 6, 7, K['k_s4'])
    c.line(15, 36, 8, 7, K['k_s0'])
    c.line(13, 34, 7, 9, K['k_s1'])
    # crossguard
    limb(c, 5, 41, 21, 37, 4, 4, K['k_g1'])
    limb(c, 6, 40, 20, 36, 2, 2, K['k_g2'])
    c.line(6, 39, 19, 35, K['k_g3'])
    c.circle(5, 41, 2, K['k_g2'])
    c.circle(21, 37, 2, K['k_g2'])
    # grip + pommel
    limb(c, 13, 39, 17, 52, 5, 5, K['k_le'])
    c.line(13, 41, 16, 51, K['g_l1'])
    c.circle(18, 54, 4, K['k_g1'])
    c.circle(17, 53, 3, K['k_g2'])
    c.set(16, 52, K['k_g3'])

    # ---- torso ----
    c.poly([(12, 48), (33, 48), (32, 60), (30, 72), (15, 72), (13, 60)], K['k_r2'])
    c.poly([(12, 48), (18, 48), (17, 72), (15, 72), (13, 60)], K['k_r1'])
    c.poly([(12, 48), (15, 48), (14, 60), (15, 72), (13, 72), (12, 60)], K['k_r0'])
    c.poly([(28, 48), (33, 48), (32, 60), (30, 72), (27, 72)], K['k_r3'])
    c.poly([(31, 48), (33, 48), (32, 60), (31, 68)], K['k_r4'])
    # chest eagle / gold trim
    c.path("M16,51 L22,59 L29,51", K['k_g1'], fill=False)
    c.path("M17,50 L22,57 L28,50", K['k_g2'], fill=False)
    c.circle(22, 60, 3, K['k_g1'])
    c.circle(22, 60, 2, K['k_g3'])
    # belt
    c.rect(14, 66, 17, 5, K['k_g1'])
    c.rect(15, 67, 15, 3, K['k_g2'])
    c.rect(20, 66, 6, 5, K['k_g3'])
    c.line(14, 71, 30, 71, K['ink'])

    # ---- pauldrons ----
    c.ellipse(11, 53, 9, 8, K['k_r0'])
    c.ellipse(10, 52, 8, 7, K['k_r1'])
    c.ellipse(9, 50, 5, 4, K['k_r2'])
    c.ellipse(34, 54, 10, 9, K['k_r1'])
    c.ellipse(35, 53, 9, 8, K['k_r2'])
    c.ellipse(36, 51, 6, 5, K['k_r3'])
    c.ellipse(37, 49, 3, 3, K['k_r4'])
    # laminated edges
    c.path("M26,50 C30,46 40,46 44,52", K['k_g2'], fill=False)
    c.path("M27,56 C31,52 40,52 44,58", K['k_g1'], fill=False)
    c.path("M3,49 C6,45 14,45 18,49", K['k_g1'], fill=False)
    # spikes on the near pauldron
    c.poly([(35, 48), (37, 40), (39, 48)], K['k_s2'])
    c.poly([(40, 50), (43, 43), (44, 51)], K['k_s2'])
    c.line(37, 41, 38, 47, K['k_s3'])
    c.line(43, 44, 43, 50, K['k_s3'])

    # ---- far arm, raised to the sword grip ----
    seg(c, [(11, 56), (6, 50), (12, 44)], [9, 8, 7], K['k_s0'])
    seg(c, [(11, 55), (7, 50), (12, 45)], [6, 5, 5], K['k_s1'])
    c.circle(13, 44, 5, K['k_s1'])
    c.circle(13, 43, 3, K['k_s2'])
    c.line(11, 41, 16, 42, K['k_s0'])
    c.line(11, 45, 16, 46, K['k_s0'])

    # ---- neck ----
    c.rect(18, 44, 9, 7, K['k_s0'])
    c.rect(19, 44, 7, 4, K['k_s1'])

    # ---- helmet ----
    c.ellipse(22, 38, 8, 9, K['k_s0'])
    c.ellipse(22, 37, 7, 8, K['k_s1'])
    c.ellipse(24, 35, 5, 5, K['k_s2'])
    c.ellipse(25, 33, 3, 3, K['k_s3'])
    c.set(26, 31, K['k_s4'])
    # face opening
    c.poly([(17, 40), (27, 40), (27, 45), (22, 47), (17, 45)], K['ink'])
    c.poly([(18, 41), (26, 41), (26, 44), (22, 46), (18, 44)], K['ink2'])
    # glowing eyes
    c.rect(18, 41, 3, 2, K['k_eye'])
    c.rect(24, 41, 3, 2, K['k_eye'])
    c.set(19, 41, K['fx4'])
    c.set(25, 41, K['fx4'])
    # nasal bar
    c.line(22, 40, 22, 46, K['k_s1'])
    # brow + cheek guards
    c.line(16, 39, 28, 39, K['k_s2'])
    c.line(16, 38, 28, 38, K['k_s3'])
    c.poly([(16, 44), (18, 44), (18, 49), (16, 47)], K['k_s1'])
    c.poly([(27, 44), (29, 44), (29, 48), (27, 49)], K['k_s1'])
    # plume streaming back from the helm
    c.path("M20,30 C14,23 7,23 3,27 C7,30 13,30 19,32 Z", K['k_r3'])
    c.path("M19,31 C14,27 9,27 5,28 C9,30 14,30 19,32 Z", K['k_r1'])
    c.path("M19,29 C14,23 8,23 4,26", K['k_r4'], fill=False)
    c.rect(19, 29, 7, 3, K['k_r1'])
    c.line(19, 31, 26, 31, K['k_g2'])
    c.line(26, 30, 28, 25, K['rim1'])

    # ---- shield on the near arm ----
    c.poly([(29, 49), (45, 49), (45, 66), (37, 81), (29, 66)], K['k_s0'])
    c.poly([(30, 50), (44, 50), (44, 66), (37, 79), (30, 66)], K['k_r1'])
    c.poly([(32, 52), (42, 52), (42, 65), (37, 75), (32, 65)], K['k_r2'])
    c.poly([(36, 52), (42, 52), (42, 65), (37, 75)], K['k_r3'])
    c.poly([(29, 49), (45, 49), (45, 66), (37, 81), (29, 66)], K['k_g2'], fill=False)
    c.circle(37, 62, 5, K['k_s1'])
    c.circle(37, 61, 4, K['k_s3'])
    c.circle(37, 60, 2, K['k_s4'])
    c.line(33, 55, 41, 55, K['k_g1'])
    c.line(33, 70, 41, 70, K['k_g1'])


def knight_rim(c):
    K = C
    # warm back-light from the setting sun on the knight's right (sun side)
    c.line(29, 32, 30, 40, K['rim1'])
    c.line(30, 34, 30, 39, K['rim2'])
    c.line(42, 47, 44, 52, K['rim1'])
    c.line(43, 52, 44, 62, K['rim1'])
    c.line(44, 55, 44, 64, K['rim2'])
    c.line(43, 66, 38, 78, K['rim1'])
    c.line(33, 47, 40, 46, K['rim1'])
    c.line(30, 50, 33, 70, K['rim1'])
    c.line(31, 74, 33, 82, K['rim1'])
    c.line(35, 84, 37, 98, K['rim1'])
    c.line(36, 90, 37, 100, K['rim2'])
    c.line(39, 104, 41, 110, K['rim1'])
    c.line(24, 20, 27, 24, K['rim1'])
    # cool sky bounce on the left
    c.line(3, 76, 2, 92, K['k_cp4'])
    c.line(6, 8, 5, 20, K['k_s4'])


# ---------------------------------------------------------------- rogue
def rogue(c):
    K = C
    # ---- cloak, billowing back to the right ----
    c.path("M104,50 C118,47 129,60 127,80 C126,92 121,101 115,105 L112,95 "
           "L107,107 L103,95 L97,104 C94,88 96,66 99,54 Z", K['g_c2'])
    c.path("M104,50 C115,48 124,58 124,74 C124,86 120,95 115,100 L112,92 "
           "L108,101 L104,92 L100,98 C98,84 99,64 101,53 Z", K['g_c1'])
    c.path("M106,54 C116,54 122,62 122,74 C122,84 118,92 114,96", K['g_c3'], fill=False)
    c.path("M102,58 C110,60 116,70 116,82", K['g_c3'], fill=False)
    c.path("M108,52 C120,52 127,64 126,78", K['g_c4'], fill=False)
    # tattered hem spikes
    c.poly([(97, 100), (100, 110), (103, 98), (107, 112), (111, 98), (115, 108),
            (118, 96)], K['g_c1'])
    c.poly([(99, 102), (101, 108), (103, 100)], K['g_c0'])

    # ---- front cloak panel over the near shoulder ----
    c.path("M93,54 C88,64 85,80 87,94 C90,98 94,98 96,94 C94,80 95,66 98,56 Z",
           K['g_c1'])
    c.path("M94,56 C90,66 88,80 89,92", K['g_c2'], fill=False)

    # ---- far leg (screen right, braced back) ----
    seg(c, [(103, 76), (112, 90), (109, 104)], [11, 9, 8], K['g_l1'])
    seg(c, [(103, 76), (112, 90), (109, 103)], [7, 6, 5], K['g_l2'])
    c.poly([(104, 103), (114, 103), (118, 111), (103, 111)], K['g_l0'])
    c.poly([(105, 105), (113, 105), (116, 109), (104, 109)], K['g_l1'])
    c.line(106, 110, 117, 110, K['g_l2'])
    # straps
    c.line(106, 94, 114, 92, K['g_t1'])
    c.line(107, 98, 113, 97, K['g_t1'])

    # ---- near leg (screen left, bent forward) ----
    seg(c, [(95, 76), (86, 88), (87, 103)], [12, 10, 8], K['g_l1'])
    seg(c, [(95, 76), (87, 88), (88, 102)], [8, 7, 5], K['g_l2'])
    seg(c, [(94, 78), (88, 88), (89, 100)], [4, 3, 3], K['g_l3'])
    c.poly([(82, 102), (93, 102), (94, 111), (78, 111)], K['g_l0'])
    c.poly([(83, 104), (92, 104), (93, 108), (80, 108)], K['g_l1'])
    c.line(81, 109, 93, 109, K['g_l2'])
    c.line(84, 92, 92, 90, K['g_t1'])

    # ---- torso, leaning into the fight ----
    c.poly([(92, 52), (107, 52), (106, 66), (104, 78), (94, 78), (92, 64)], K['g_l1'])
    c.poly([(99, 52), (107, 52), (106, 66), (104, 78), (100, 78)], K['g_l2'])
    c.poly([(92, 52), (96, 52), (95, 78), (94, 78), (92, 64)], K['g_l0'])
    # chest straps crossing
    c.line(93, 56, 106, 66, K['g_l0'])
    c.line(93, 58, 106, 68, K['g_t1'])
    c.line(106, 56, 94, 68, K['g_l0'])
    # belt + pouches
    c.rect(93, 72, 12, 5, K['g_l0'])
    c.rect(94, 73, 10, 3, K['g_t1'])
    c.rect(96, 72, 4, 5, K['g_t2'])
    c.rect(101, 74, 4, 5, K['g_l2'])
    c.rect(102, 75, 3, 3, K['g_t1'])
    # two knives on the belt
    c.line(105, 74, 109, 68, K['g_m2'])
    c.line(106, 75, 110, 69, K['g_l0'])

    # ---- far arm flung back ----
    seg(c, [(106, 56), (114, 60), (119, 55)], [8, 7, 6], K['g_l1'])
    seg(c, [(106, 56), (114, 60), (119, 56)], [5, 4, 4], K['g_l2'])
    c.circle(120, 54, 4, K['g_skin'])
    c.circle(120, 53, 3, K['g_sk2'])
    c.line(122, 50, 125, 47, K['g_skin'])
    c.line(123, 52, 126, 50, K['g_skin'])
    c.line(123, 55, 126, 54, K['g_skin'])

    # ---- scarf ----
    c.path("M95,50 C100,54 106,54 110,50 C114,54 120,54 124,50 "
           "C122,58 112,60 104,58 C99,57 96,54 95,50 Z", K['g_c3'])
    c.path("M110,52 C118,54 124,52 127,48 C126,56 118,59 110,57 Z", K['g_c2'])
    c.line(96, 51, 108, 52, K['g_c4'])

    # ---- near arm, dagger held up by the head ----
    seg(c, [(94, 57), (88, 55), (89, 48)], [9, 7, 6], K['g_l1'])
    seg(c, [(94, 57), (89, 55), (90, 49)], [6, 5, 4], K['g_l2'])
    # bracer
    seg(c, [(89, 53), (89, 48)], [8, 7], K['g_t1'])
    c.line(86, 51, 92, 50, K['g_l0'])
    c.line(86, 48, 92, 47, K['g_l0'])
    # hand
    c.circle(89, 46, 4, K['g_skin'])
    c.circle(89, 45, 3, K['g_sk2'])
    # dagger
    limb(c, 88, 44, 76, 28, 5, 2, K['g_m2'])
    limb(c, 87, 43, 77, 29, 2, 1, K['g_m4'])
    c.line(78, 30, 76, 27, K['g_m3'])
    c.line(88, 43, 78, 30, K['g_m1'])
    limb(c, 83, 46, 93, 41, 4, 4, K['g_t1'])
    c.line(84, 44, 92, 40, K['g_t2'])
    limb(c, 89, 46, 92, 51, 4, 4, K['g_l0'])
    c.circle(93, 52, 2, K['g_t2'])

    # ---- hood ----
    c.poly([(92, 52), (92, 42), (96, 35), (104, 33), (111, 38), (112, 48),
            (106, 54), (96, 54)], K['g_c1'])
    c.poly([(94, 51), (94, 42), (98, 36), (104, 35), (109, 39), (110, 47),
            (105, 52), (97, 52)], K['g_c2'])
    c.poly([(100, 36), (105, 35), (109, 40), (108, 46), (104, 40)], K['g_c3'])
    # hood point trailing back
    c.poly([(110, 39), (117, 37), (119, 43), (111, 47)], K['g_c1'])
    c.poly([(111, 40), (116, 39), (117, 43), (112, 45)], K['g_c2'])
    # face shadow inside the hood
    c.poly([(93, 41), (102, 39), (103, 50), (96, 52), (93, 48)], K['ink'])
    c.poly([(94, 42), (101, 41), (102, 49), (96, 51), (94, 47)], K['g_l0'])
    # glowing eyes
    c.rect(95, 44, 2, 2, K['g_eye'])
    c.set(95, 44, K['fx4'])
    c.rect(99, 44, 2, 2, K['g_eye'])
    c.set(99, 44, K['fx4'])
    # mask over the lower face
    c.poly([(93, 47), (102, 46), (102, 51), (95, 52)], K['g_l1'])
    c.line(94, 48, 101, 47, K['g_l2'])
    # silver hair spilling out
    c.path("M94,40 C90,42 88,47 89,52 C91,48 93,44 96,42 Z", K['g_hair'])
    c.path("M96,38 C93,39 91,43 91,47", K['g_m3'], fill=False)
    # hood rim
    c.path("M92,44 C93,37 98,33 105,33", K['g_c4'], fill=False)


def rogue_rim(c):
    K = C
    # sun-side rim on the rogue's left
    c.line(93, 38, 92, 46, K['rim1'])
    c.line(94, 36, 93, 41, K['rim2'])
    c.line(92, 54, 90, 64, K['rim1'])
    c.line(88, 68, 87, 80, K['rim1'])
    c.line(87, 84, 88, 94, K['rim1'])
    c.line(86, 56, 88, 52, K['rim1'])
    c.line(84, 104, 82, 109, K['rim1'])
    c.line(93, 78, 92, 88, K['rim1'])
    c.line(88, 90, 87, 100, K['rim2'])
    c.line(79, 33, 84, 40, K['rim2'])
    c.line(96, 34, 104, 33, K['rim1'])


# ---------------------------------------------------------------- effects
def fx(c):
    import random
    random.seed(1234)
    K = C
    # impact crack glowing between the two
    c.line(48, 106, 58, 100, K['gnd5'])
    c.line(58, 100, 70, 108, K['gnd5'])
    c.line(50, 105, 58, 99, K['fx2'])
    c.line(58, 99, 69, 107, K['fx2'])
    c.set(58, 99, K['fx1'])
    c.set(54, 102, K['fx1'])
    c.set(64, 103, K['fx1'])

    # embers / dust drifting up
    for i in range(90):
        x = random.randint(0, 127)
        y = random.randint(24, 122)
        t = random.random()
        if t < 0.45:
            c.set(x, y, K['fx2'])
        elif t < 0.75:
            c.set(x, y, K['fx1'])
        elif t < 0.9:
            c.set(x, y, K['rim1'])
        else:
            c.set(x, y, K['fx4'])

    # bigger sparks near the centre of the standoff
    for x, y, col in [(52, 60, 'fx1'), (60, 46, 'fx2'), (68, 66, 'fx1'),
                      (74, 40, 'fx2'), (56, 78, 'fx1'), (64, 34, 'fx4'),
                      (70, 88, 'fx2'), (50, 44, 'fx1'), (76, 56, 'fx1'),
                      (58, 92, 'fx4'), (66, 24, 'fx2'), (54, 30, 'fx1')]:
        c.set(x, y, K[col])
        c.set(x + 1, y, K['fx2'])
        c.set(x, y + 1, K['fx2'])
        c.set(x - 1, y, K['fx2'])
        c.set(x, y - 1, K['fx2'])

    # wind streaks rushing through the gap
    for y, x0, ln in [(52, 50, 10), (68, 56, 14), (84, 48, 8), (40, 62, 12),
                      (96, 54, 10)]:
        c.line(x0, y, x0 + ln, y, K['rim1'])
        for xx in range(x0 + 2, x0 + ln - 1, 4):
            c.set(xx, y, K['fx1'])
