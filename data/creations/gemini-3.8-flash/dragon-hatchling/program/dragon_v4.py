import numpy as np
from pixelbench_api import *

PAL = {
    '..': None,
    # Selective outlines & shadows
    'k0': '#14030c',  # darkest outline
    'k1': '#260615',  # dark contour
    'k2': '#3d0a20',  # soft shadow outline
    'k3': '#5a1027',  # lit contour / crease

    # Red dragon scales (Ruby / Crimson)
    'r1': '#520e20',  # deep scale shadow
    'r2': '#74142a',  # scale shadow
    'r3': '#9a1a32',  # scale midtone dark
    'r4': '#bf253a',  # scale base red
    'r5': '#e23a44',  # scale bright red
    'r6': '#f45c50',  # scale highlight
    'r7': '#ff8a72',  # scale specular highlight

    # Pale underbelly plates (Warm cream / pale peach-gold scutes)
    'b0': '#341c10',  # belly dark crease
    'b1': '#583218',  # belly deep shadow
    'b2': '#845028',  # belly shadow
    'b3': '#b2743e',  # belly midtone
    'b4': '#d69a58',  # belly warm cream
    'b5': '#eec07a',  # belly pale buff
    'b6': '#fade9e',  # belly highlight
    'b7': '#fff2d0',  # belly bright specular

    # Leathery wings (warm terracotta / glowing amber)
    'w0': '#2c0e14',  # wing edge dark
    'w1': '#4a171e',  # wing deep shade
    'w2': '#6c2124',  # wing shade
    'w3': '#8e2d26',  # wing midtone
    'w4': '#b2402e',  # wing warm mid
    'w5': '#ce5a34',  # wing warm bright
    'w6': '#e67a42',  # wing glowing amber
    'w7': '#f79c5a',  # wing rim light

    # Horns, spikes, claws (Ivory / Horn)
    'h0': '#201610',  # horn dark outline
    'h1': '#3c2c22',  # horn shadow
    'h2': '#624a3a',  # horn mid
    'h3': '#8e745e',  # horn base
    'h4': '#b89e86',  # horn light ivory
    'h5': '#d8c4ae',  # horn pale ivory
    'h6': '#f8eee2',  # horn tip highlight

    # Eye
    'e0': '#100205',  # pupil / socket depth
    'e1': '#360612',  # eye contour
    'e2': '#964800',  # amber shadow
    'e3': '#dc7a00',  # amber mid
    'e4': '#fcaa00',  # bright gold iris
    'e5': '#ffe444',  # intense yellow glow
    'e6': '#ffffff',  # white catchlight

    # Mouth interior & teeth
    'm0': '#140207',  # deep throat
    'm1': '#380514',  # mouth dark cavity
    'm2': '#600e22',  # tongue shadow
    'm3': '#8e1836',  # tongue mid
    'm4': '#c4345a',  # tongue highlight
    'm5': '#fff8f0',  # sharp white fangs
    'm6': '#ceb8a2',  # teeth shaded base

    # Flame spark & smoke
    'f0': '#88120c',  # flame dark
    'f1': '#bc2c0e',  # flame mid red
    'f2': '#e45414',  # flame orange
    'f3': '#f4921c',  # flame gold
    'f4': '#ffee60',  # flame yellow core
    's0': '#3a222a',  # smoke shadow
    's1': '#60404a',  # smoke mid
    's2': '#8a6472',  # smoke light
}

def build_dragon_v4():
    buf = np.full((64, 64), '..', dtype=object)

    def p(x, y, tok):
        if 0 <= x < 64 and 0 <= y < 64:
            buf[y, x] = tok

    def poly(pts, tok):
        ys = [pt[1] for pt in pts]
        min_y = max(0, min(ys))
        max_y = min(63, max(ys))
        n = len(pts)
        for y in range(min_y, max_y + 1):
            nodes = []
            for i in range(n):
                j = (i + 1) % n
                y1, y2 = pts[i][1], pts[j][1]
                x1, x2 = pts[i][0], pts[j][0]
                if (y1 < y and y2 >= y) or (y2 < y and y1 >= y):
                    nodes.append(x1 + (y - y1) / (y2 - y1) * (x2 - x1))
            nodes.sort()
            for k in range(0, len(nodes) - 1, 2):
                x_start = max(0, int(np.ceil(nodes[k])))
                x_end = min(63, int(np.floor(nodes[k+1])))
                for x in range(x_start, x_end + 1):
                    buf[y, x] = tok

    def line(x0, y0, x1, y1, tok):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        x, y = x0, y0
        while True:
            p(x, y, tok)
            if x == x1 and y == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

    # ====================================================
    # 1. FAR WING (Background Wing, spread up-left)
    # ====================================================
    # Webbing panels
    poly([(12, 8), (8, 9), (5, 12), (8, 14), (12, 11)], 'w1')
    poly([(12, 11), (8, 14), (7, 18), (10, 19), (13, 16)], 'w1')
    poly([(13, 16), (10, 19), (11, 23), (15, 23), (17, 19)], 'w1')

    # Translucent interior
    poly([(11, 10), (7, 12), (9, 14), (12, 12)], 'w2')
    poly([(11, 13), (8, 17), (10, 18), (12, 16)], 'w2')
    poly([(13, 17), (11, 21), (13, 22), (15, 19)], 'w2')
    p(9, 13, 'w3'); p(10, 17, 'w3'); p(12, 20, 'w3')

    # Far wing finger ribs
    line(12, 8, 5, 12, 'r2')
    line(12, 9, 7, 18, 'r2')
    line(13, 11, 11, 23, 'r2')

    # Far wing arm
    line(23, 21, 17, 14, 'r2')
    line(17, 14, 12, 8, 'r3')
    line(18, 14, 13, 8, 'r4')
    # Wrist claw
    p(11, 7, 'h4'); p(10, 7, 'h5')

    # Outer scalloped silhouette
    for (x, y) in [(4, 12), (5, 11), (6, 13), (6, 15), (7, 17), (8, 19), (10, 21), (11, 23)]:
        p(x, y, 'k0')

    # ====================================================
    # 2. FAR HORN & FAR LEGS
    # ====================================================
    # Far Horn: curves back smoothly from (19, 16) to (27, 14)
    poly([(19, 16), (22, 15), (25, 14), (27, 14), (25, 15), (22, 16), (19, 17)], 'h2')
    line(20, 16, 26, 14, 'h3')
    p(26, 14, 'h4'); p(27, 14, 'h5'); p(28, 14, 'k0')

    # Far Foreleg (x = 27..32, y = 44..52)
    poly([(27, 43), (31, 43), (32, 49), (29, 52), (26, 52), (26, 46)], 'r1')
    poly([(27, 45), (30, 45), (30, 49), (28, 51)], 'r2')
    p(26, 53, 'h4'); p(28, 53, 'h4'); p(30, 53, 'h4')
    p(26, 54, 'k0'); p(28, 54, 'k0'); p(30, 54, 'k0')

    # Far Hindleg (x = 43..48, y = 45..53)
    poly([(43, 44), (48, 44), (49, 50), (46, 53), (43, 52)], 'r1')
    poly([(44, 45), (47, 45), (47, 49), (45, 51)], 'r2')
    p(44, 53, 'h4'); p(46, 53, 'h4'); p(48, 53, 'h4')
    p(44, 54, 'k0'); p(46, 54, 'k0'); p(48, 54, 'k0')

    # ====================================================
    # 3. TAIL (Spiked, Sweeping S-Curve)
    # ====================================================
    pts_tail = [
        (42, 35), (46, 37), (50, 40), (54, 43), (56, 46), (55, 49),
        (52, 49), (48, 46), (44, 41), (42, 37)
    ]
    poly(pts_tail, 'r2')

    pts_curl = [
        (54, 48), (57, 46), (59, 43), (60, 38), (59, 33), (57, 29),
        (55, 29), (56, 34), (57, 39), (55, 44), (52, 47)
    ]
    poly(pts_curl, 'r2')

    # Tail highlights
    poly([(43, 36), (47, 38), (51, 41), (54, 44), (53, 43), (49, 40), (45, 37)], 'r3')
    poly([(44, 36), (48, 38), (52, 41), (50, 40), (46, 37)], 'r4')
    line(45, 36, 49, 38, 'r5')

    poly([(56, 43), (58, 39), (58, 34), (56, 30), (57, 30), (59, 35), (59, 40), (57, 44)], 'r3')
    poly([(57, 39), (58, 35), (57, 31), (58, 32), (59, 36)], 'r4')
    line(58, 36, 57, 31, 'r5')

    poly([(47, 45), (51, 48), (54, 48), (51, 46), (47, 43)], 'r1')

    # Tail spikes
    tail_spikes = [
        (46, 33, 45, 36, 48, 37),
        (51, 36, 49, 39, 52, 41),
        (55, 39, 54, 42, 57, 44),
        (61, 41, 59, 43, 60, 39),
        (61, 33, 59, 36, 58, 31),
    ]
    for sx, sy, b1x, b1y, b2x, b2y in tail_spikes:
        poly([(sx, sy), (b1x, b1y), (b2x, b2y)], 'h2')
        line(sx, sy, b1x, b1y, 'h4')
        p(sx, sy, 'h5')
        p(sx, sy-1, 'h6')
        p(b2x, b2y, 'h1')

    # Tail spade
    poly([(56, 29), (53, 26), (56, 24), (59, 26), (56, 29)], 'h3')
    line(54, 26, 56, 24, 'h4')
    line(55, 25, 57, 25, 'h5')
    p(56, 23, 'h6'); p(56, 22, 'k0')
    p(52, 26, 'k0'); p(60, 26, 'k0')

    # ====================================================
    # 4. HINDQUARTER & THIGH
    # ====================================================
    pts_thigh = [
        (35, 34), (43, 34), (46, 38), (45, 43), (42, 47), (37, 48),
        (33, 45), (32, 40), (35, 34)
    ]
    poly(pts_thigh, 'r2')
    poly([(36, 35), (42, 35), (44, 38), (42, 42), (37, 44), (34, 40)], 'r3')
    poly([(37, 36), (41, 36), (42, 39), (39, 41), (35, 39)], 'r4')
    poly([(38, 37), (41, 37), (41, 38), (38, 40)], 'r5')
    p(39, 38, 'r6'); p(40, 38, 'r7')

    # Lower hind leg
    poly([(33, 44), (37, 44), (43, 48), (43, 52), (39, 54), (34, 53), (32, 48)], 'r2')
    poly([(34, 46), (38, 46), (41, 49), (38, 52), (34, 50)], 'r3')
    poly([(35, 48), (38, 48), (39, 50), (36, 51)], 'r4')

    # Foot & claws
    poly([(34, 53), (42, 53), (42, 56), (33, 56)], 'r2')
    for cx in [35, 38, 41]:
        p(cx, 55, 'h3')
        p(cx, 56, 'h4')
        p(cx-1, 57, 'h5')
        p(cx-1, 58, 'h6')
        p(cx-1, 59, 'k0')

    # ====================================================
    # 5. TORSO & DORSAL SPIKES
    # ====================================================
    pts_torso = [
        (26, 30), (34, 31), (43, 34), (42, 38), (35, 42), (28, 42),
        (23, 38), (24, 32), (26, 30)
    ]
    poly(pts_torso, 'r2')
    poly([(27, 31), (34, 32), (40, 34), (38, 38), (31, 39), (25, 35)], 'r3')
    poly([(28, 32), (33, 33), (37, 35), (34, 37), (27, 36)], 'r4')
    poly([(29, 33), (33, 34), (33, 36), (29, 35)], 'r5')

    back_spikes = [
        (29, 28, 28, 30, 31, 30),
        (34, 29, 33, 31, 36, 31),
        (39, 30, 38, 32, 41, 32),
    ]
    for sx, sy, b1x, b1y, b2x, b2y in back_spikes:
        poly([(sx, sy), (b1x, b1y), (b2x, b2y)], 'h2')
        line(sx, sy, b1x, b1y, 'h4')
        p(sx, sy, 'h5')
        p(sx, sy-1, 'h6')

    # ====================================================
    # 6. PALE UNDERBELLY (Anatomically True Placement!)
    # ====================================================
    # The pale belly covers:
    # 1. Throat & Neck ventral line: x=17..21, y=34..39
    # 2. Chest (front of chest, left of near shoulder): x=17..22, y=39..44
    # 3. Ventral Abdomen (along the bottom edge between legs): x=24..35, y=45..48
    pts_belly_throat = [
        (17, 34), (20, 33), (22, 35), (23, 39),
        (21, 43), (17, 43), (16, 40), (16, 37), (17, 34)
    ]
    poly(pts_belly_throat, 'b2')
    poly([(17, 35), (20, 34), (21, 36), (22, 39), (20, 42), (17, 42), (17, 37)], 'b3')
    poly([(18, 35), (20, 35), (21, 38), (20, 41), (18, 41), (18, 38)], 'b4')
    poly([(18, 36), (19, 36), (20, 38), (19, 40), (18, 40)], 'b5')
    p(18, 37, 'b6'); p(19, 37, 'b7')
    p(18, 39, 'b6'); p(19, 39, 'b7')

    # Ventral underbelly plates (under the abdomen between legs)
    pts_belly_ventral = [
        (22, 44), (26, 43), (31, 44), (35, 45), (36, 48),
        (32, 48), (27, 47), (23, 46), (21, 45)
    ]
    poly(pts_belly_ventral, 'b2')
    poly([(23, 45), (27, 44), (31, 45), (34, 46), (34, 47), (30, 47), (25, 46), (22, 45)], 'b3')
    poly([(24, 45), (28, 45), (32, 46), (31, 47), (27, 46), (24, 46)], 'b4')
    poly([(25, 45), (28, 45), (30, 46), (29, 46), (26, 46)], 'b5')

    # Scute creases on throat/chest
    for x, y in [(17, 36), (18, 36), (20, 35)]:
        p(x, y, 'b0'); p(x, y+1, 'b5')
    for x, y in [(17, 38), (19, 38), (21, 38)]:
        p(x, y, 'b0'); p(x, y+1, 'b5')
    for x, y in [(17, 41), (19, 41), (21, 41)]:
        p(x, y, 'b0'); p(x, y+1, 'b5')

    # Scute creases on ventral belly
    for x, y in [(25, 44), (26, 45), (26, 46)]:
        p(x, y, 'b0'); p(x+1, y, 'b5')
    for x, y in [(29, 45), (30, 46), (30, 47)]:
        p(x, y, 'b0'); p(x+1, y, 'b5')

    # ====================================================
    # 7. NEAR FORELEG (Anatomically placed on flank & chest side!)
    # ====================================================
    # Shoulder on flank (x = 22..28, y = 38..44)
    poly([(22, 38), (27, 38), (28, 42), (26, 45), (23, 44), (21, 41)], 'r2')
    poly([(23, 39), (26, 39), (27, 42), (25, 44), (23, 43)], 'r3')
    poly([(24, 40), (26, 40), (26, 42), (24, 43)], 'r4')
    p(25, 41, 'r5')

    # Forearm angles forward-down: x = 21..25, y = 44..50
    poly([(22, 44), (26, 44), (25, 50), (21, 50), (20, 46)], 'r2')
    poly([(22, 45), (25, 45), (24, 49), (22, 49)], 'r3')
    poly([(23, 46), (24, 46), (23, 48)], 'r4')

    # Paw / wrist: x = 17..23, y = 50..54
    poly([(17, 50), (23, 50), (23, 54), (17, 54)], 'r2')
    poly([(18, 51), (22, 51), (21, 53), (18, 53)], 'r3')
    poly([(19, 51), (21, 51), (20, 53)], 'r4')

    # 3 Front talons gripping ground
    # Toe 1 (left)
    poly([(14, 53), (17, 53), (16, 56), (14, 56)], 'r2')
    p(15, 54, 'r3'); p(16, 54, 'r4')
    p(14, 56, 'h4'); p(13, 57, 'h5'); p(12, 57, 'h6'); p(12, 58, 'k0')
    # Toe 2 (middle)
    poly([(17, 53), (20, 53), (20, 56), (17, 56)], 'r2')
    p(18, 54, 'r3'); p(19, 54, 'r4')
    p(18, 56, 'h4'); p(17, 57, 'h5'); p(16, 57, 'h6'); p(16, 58, 'k0')
    # Toe 3 (right)
    poly([(20, 53), (23, 53), (23, 56), (20, 56)], 'r2')
    p(21, 54, 'r3'); p(22, 54, 'r4')
    p(21, 56, 'h4'); p(20, 57, 'h5'); p(19, 57, 'h6'); p(19, 58, 'k0')

    # ====================================================
    # 8. NECK & HEAD
    # ====================================================
    # Neck dorsal curve
    poly([(22, 23), (27, 27), (28, 31), (24, 31), (21, 26)], 'r2')
    poly([(23, 24), (26, 27), (27, 30), (25, 30), (22, 26)], 'r3')
    poly([(24, 25), (26, 27), (26, 29), (24, 28)], 'r4')

    neck_spikes = [
        (22, 21, 22, 23, 24, 23),
        (26, 24, 25, 26, 28, 27),
    ]
    for sx, sy, b1x, b1y, b2x, b2y in neck_spikes:
        poly([(sx, sy), (b1x, b1y), (b2x, b2y)], 'h2')
        line(sx, sy, b1x, b1y, 'h4')
        p(sx, sy, 'h5')

    # Head cranium
    pts_head = [
        (17, 18), (23, 17), (26, 19), (25, 24), (20, 24), (16, 21), (17, 18)
    ]
    poly(pts_head, 'r2')
    poly([(18, 19), (22, 18), (24, 20), (23, 23), (19, 23), (17, 21)], 'r3')
    poly([(19, 19), (22, 19), (23, 21), (21, 22), (18, 21)], 'r4')
    p(20, 19, 'r5'); p(21, 19, 'r6')

    # Snout & Upper Jaw (predatory curve with hooked tip)
    pts_snout = [
        (10, 23), (15, 21), (18, 21), (18, 26), (11, 26), (10, 23)
    ]
    poly(pts_snout, 'r2')
    poly([(11, 23), (15, 22), (17, 22), (17, 25), (12, 25)], 'r3')
    poly([(12, 23), (15, 22), (16, 22), (16, 24), (13, 24)], 'r4')
    p(13, 23, 'r5'); p(14, 23, 'r6')

    # Snout tip hook
    p(10, 24, 'r2'); p(11, 25, 'r3')
    p(12, 23, 'k0'); p(12, 22, 'r2')

    # Near Horn (sweeps back gracefully along top of neck)
    pts_horn = [
        (23, 18), (26, 17), (29, 18), (32, 20), (34, 22),
        (32, 21), (29, 19), (26, 18), (23, 19)
    ]
    poly(pts_horn, 'h2')
    line(23, 18, 33, 21, 'h3')
    line(24, 17, 33, 20, 'h4')
    p(27, 17, 'h5'); p(30, 18, 'h5'); p(33, 20, 'h5'); p(34, 21, 'h6'); p(35, 22, 'h6')
    p(35, 23, 'k0')
    line(23, 19, 33, 22, 'h1')

    # Cheek Horn
    poly([(22, 24), (26, 25), (24, 26), (22, 25)], 'h3')
    p(25, 25, 'h4'); p(26, 25, 'h5'); p(27, 25, 'h6')

    # Fierce Eye & Scowling Brow
    p(17, 19, 'r3'); p(18, 19, 'r4'); p(19, 19, 'r5'); p(20, 20, 'r4')
    p(17, 20, 'k1'); p(21, 20, 'k1')
    p(18, 20, 'e1'); p(19, 20, 'e1'); p(20, 21, 'e1')
    p(18, 21, 'e2'); p(19, 21, 'e3'); p(20, 22, 'e4'); p(21, 21, 'e2')
    p(19, 21, 'e0')  # vertical slit pupil
    p(20, 21, 'e5')  # golden glow
    p(20, 20, 'e6')  # catchlight

    # ====================================================
    # 9. GROWL & OPEN MOUTH (Sharp Interlocking Fangs!)
    # ====================================================
    # Mouth interior (deep dark red cavity)
    pts_mouth = [
        (12, 26), (21, 26), (22, 29), (18, 31), (14, 31), (12, 28)
    ]
    poly(pts_mouth, 'm0')
    poly([(14, 27), (20, 27), (21, 29), (17, 30), (14, 30)], 'm1')

    # Tongue curled inside bottom
    poly([(15, 29), (19, 29), (18, 31), (15, 31)], 'm2')
    p(16, 29, 'm3'); p(17, 29, 'm4')
    p(16, 30, 'm3')

    # Upper Fangs:
    # ONE primary front fang pointing down
    p(14, 26, 'm6'); p(14, 27, 'm5'); p(14, 28, 'm5')
    # ONE small rear fang
    p(18, 26, 'm6'); p(18, 27, 'm5')

    # Lower Jaw (sleek tapered dragon jawline)
    pts_lower_jaw = [
        (13, 31), (21, 30), (22, 33), (18, 34), (14, 34), (13, 32)
    ]
    poly(pts_lower_jaw, 'r2')
    poly([(14, 32), (20, 31), (20, 33), (17, 33), (14, 33)], 'r3')
    poly([(15, 33), (19, 32), (18, 33)], 'r4')
    p(14, 34, 'r4'); p(15, 34, 'r5')

    # Lower Fangs:
    # ONE primary lower canine fang pointing UP into the mouth gap
    p(16, 31, 'm6'); p(16, 30, 'm5'); p(16, 29, 'm5')
    # ONE small front incisor
    p(13, 31, 'm5')

    # ====================================================
    # 10. NEAR WING (Foreground Wing, arched high & spread)
    # ====================================================
    # Arm bone: shoulder (29, 27) -> elbow (36, 17) -> wrist (43, 7)
    pts_arm = [
        (29, 27), (32, 22), (36, 16), (39, 12), (42, 8), (43, 7),
        (44, 8), (42, 12), (38, 17), (35, 22), (32, 26), (30, 28)
    ]
    poly(pts_arm, 'r2')
    pts_arm_hi = [
        (30, 26), (33, 21), (36, 16), (39, 11), (42, 7),
        (43, 8), (40, 12), (37, 16), (34, 21), (31, 25)
    ]
    for x, y in pts_arm_hi: p(x, y, 'r4')
    p(43, 7, 'r5'); p(42, 7, 'r6')

    # Thumb Claw at wrist (42, 6)
    p(42, 6, 'h4'); p(41, 5, 'h5'); p(40, 5, 'h6')
    p(42, 7, 'h2'); p(43, 6, 'h1')

    # Wing Membranes (Glowing translucent amber-terracotta arches)
    # Panel 1: Arm to Strut 1 (to 54, 8)
    poly([(43, 7), (47, 6), (51, 6), (54, 8), (50, 10), (45, 9), (43, 8)], 'w3')
    poly([(45, 7), (49, 7), (52, 8), (49, 9), (46, 8)], 'w4')
    p(48, 8, 'w5'); p(49, 8, 'w6')

    # Panel 2: Strut 1 to Strut 2 (to 59, 15)
    poly([
        (43, 8), (54, 8), (56, 11), (58, 13), (59, 15),
        (55, 15), (50, 13), (45, 10), (43, 8)
    ], 'w2')
    poly([(45, 9), (52, 9), (56, 11), (57, 13), (54, 13), (49, 11), (45, 10)], 'w3')
    poly([(47, 10), (51, 10), (54, 12), (52, 12), (47, 11)], 'w4')
    p(49, 11, 'w5'); p(50, 11, 'w6')

    # Panel 3: Strut 2 to Strut 3 (to 56, 25)
    poly([
        (42, 10), (50, 12), (59, 15), (58, 19), (57, 22), (56, 25),
        (51, 22), (47, 19), (43, 15), (42, 11)
    ], 'w2')
    poly([(44, 11), (50, 14), (55, 17), (55, 20), (53, 22), (48, 19), (44, 15)], 'w3')
    poly([(46, 13), (51, 16), (53, 18), (50, 18), (46, 15)], 'w4')
    p(48, 16, 'w5'); p(49, 16, 'w6')

    # Panel 4: Strut 3 to Flank (41, 33)
    poly([
        (41, 14), (47, 19), (56, 25), (52, 28), (48, 30), (42, 33),
        (40, 29), (40, 22), (41, 16)
    ], 'w1')
    poly([(42, 17), (47, 21), (51, 26), (48, 28), (44, 29), (41, 25)], 'w2')
    poly([(43, 19), (46, 22), (48, 25), (45, 26), (42, 23)], 'w3')

    # Strut bone lines & finger claws
    line(43, 7, 54, 8, 'r3')
    p(54, 8, 'h4'); p(55, 8, 'h5'); p(56, 8, 'k0')
    line(43, 8, 59, 15, 'r3')
    p(59, 15, 'h4'); p(60, 15, 'h5'); p(61, 15, 'k0')
    line(42, 10, 56, 25, 'r3')
    p(56, 25, 'h4'); p(57, 26, 'h5'); p(58, 26, 'k0')

    # ====================================================
    # 11. GROWL SMOKE & EMBER
    # ====================================================
    # Hot ember curling from mouth
    p(10, 26, 'f2'); p(9, 26, 'f3'); p(9, 25, 'f4')
    p(8, 25, 'f3'); p(8, 26, 'f2'); p(7, 25, 'f1')
    p(9, 24, 'f2'); p(10, 24, 'f1')
    # Wispy smoke puff curling up
    p(6, 24, 's1'); p(5, 23, 's2'); p(6, 22, 's1'); p(7, 22, 's0')
    p(8, 22, 's1'); p(8, 21, 's2'); p(7, 20, 's1')

    # ====================================================
    # 12. SELECTIVE OUTLINING & POLISH
    # ====================================================
    line(43, 6, 54, 7, 'k0')
    line(54, 8, 59, 14, 'k0')
    line(11, 22, 15, 21, 'k1')
    line(15, 21, 18, 18, 'k1')
    line(13, 34, 18, 34, 'k0')

    return buf

def render(buf):
    c = new_canvas(64, 64)
    for y in range(64):
        for x in range(64):
            tok = buf[y, x]
            if tok != '..' and tok in PAL and PAL[tok] is not None:
                c.set(x, y, PAL[tok])
    return c

buf = build_dragon_v4()
c = render(buf)
view(c)
print("Canvas stats:", c.stats())
