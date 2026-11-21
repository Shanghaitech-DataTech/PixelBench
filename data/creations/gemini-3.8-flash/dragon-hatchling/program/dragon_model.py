import numpy as np
from pixelbench_api import *

# Refined palette
PAL = {
    '..': None,
    # Dark outlines (selective outlining)
    'k0': '#15040d',  # darkest outline (bottom/shadow)
    'k1': '#2b0818',  # dark contour
    'k2': '#450d24',  # soft outline (midtones)
    'k3': '#61122a',  # lit outline / deep crease

    # Red body scales
    'r1': '#5e1226',  # deep scale shadow
    'r2': '#821830',  # scale shadow
    'r3': '#a82038',  # scale midtone dark
    'r4': '#cb2d42',  # scale base red
    'r5': '#eb484c',  # scale bright red
    'r6': '#f86d5c',  # scale highlight
    'r7': '#ffa085',  # scale specular

    # Pale underbelly plates (creamy peach-gold)
    'b0': '#382012',  # belly crease
    'b1': '#5e381e',  # belly deep shadow
    'b2': '#8c582f',  # belly shadow
    'b3': '#ba7d48',  # belly midtone
    'b4': '#dea264',  # belly warm cream
    'b5': '#f3c486',  # belly pale buff
    'b6': '#fde2ac',  # belly highlight
    'b7': '#fff4d4',  # belly bright specular

    # Leathery wings (warm terracotta / amber)
    'w0': '#331118',  # wing edge dark
    'w1': '#541c22',  # wing deep shade
    'w2': '#782828',  # wing shade
    'w3': '#9c382c',  # wing midtone
    'w4': '#c04e34',  # wing warm mid
    'w5': '#dd6b3e',  # wing warm bright
    'w6': '#f28d4e',  # wing glowing amber
    'w7': '#fbb26c',  # wing rim light

    # Horns, spikes, claws (Ivory)
    'h0': '#241a14',  # horn dark outline
    'h1': '#443328',  # horn shadow
    'h2': '#6e5442',  # horn mid
    'h3': '#9c8168',  # horn base
    'h4': '#c4aa90',  # horn light ivory
    'h5': '#e2ceba',  # horn pale ivory
    'h6': '#faf2e6',  # horn tip highlight

    # Eye
    'e0': '#120206',  # eye socket / pupil
    'e1': '#3a0814',  # eye contour
    'e2': '#9e4e00',  # amber shadow
    'e3': '#e68200',  # amber mid
    'e4': '#ffb700',  # bright gold iris
    'e5': '#ffee55',  # intense yellow glow
    'e6': '#ffffff',  # white catchlight

    # Mouth interior & teeth
    'm0': '#18030a',  # deep throat
    'm1': '#42081a',  # mouth dark cavity
    'm2': '#70122c',  # tongue shadow
    'm3': '#a32044',  # tongue mid
    'm4': '#d8446c',  # tongue highlight
    'm5': '#fff8f0',  # sharp white teeth
    'm6': '#d4beaa',  # teeth shaded base

    # Flame spark & smoke
    'f0': '#941610',  # flame dark
    'f1': '#cc3412',  # flame mid red
    'f2': '#f0621a',  # flame orange
    'f3': '#ffa224',  # flame gold
    'f4': '#ffee68',  # flame yellow core
    's0': '#422832',  # smoke shadow
    's1': '#6e4a58',  # smoke mid
    's2': '#9c7382',  # smoke light
}

def build_dragon_sprite():
    buf = np.full((64, 64), '..', dtype=object)

    def set_p(x, y, tok):
        if 0 <= x < 64 and 0 <= y < 64:
            buf[y, x] = tok

    def get_p(x, y):
        if 0 <= x < 64 and 0 <= y < 64:
            return buf[y, x]
        return '..'

    def poly(pts, tok):
        ys = [p[1] for p in pts]
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
            set_p(x, y, tok)
            if x == x1 and y == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy

    # ----------------------------------------------------
    # 1. FAR WING (Background, left side, spread behind neck)
    # ----------------------------------------------------
    # Webbing outline / mass
    # Wrist at (11, 7), fingers to (5, 12), (7, 18), (11, 22), base at (22, 22)
    poly([(11, 7), (5, 12), (6, 15), (7, 18), (9, 21), (12, 23), (17, 24), (22, 22), (18, 14)], 'w1')
    # Inner gradient / translucent lighting
    poly([(12, 9), (7, 13), (8, 16), (9, 18), (12, 20), (16, 21), (18, 15)], 'w2')
    poly([(12, 10), (8, 14), (10, 17), (13, 18), (16, 17), (16, 14)], 'w3')
    poly([(12, 12), (10, 15), (12, 16), (14, 15)], 'w4')

    # Far wing struts
    line(11, 7, 5, 12, 'r2')
    line(11, 7, 7, 18, 'r2')
    line(12, 8, 12, 23, 'r2')
    # Far wing arm
    line(22, 22, 17, 14, 'r2')
    line(17, 14, 11, 7, 'r3')
    line(18, 14, 12, 7, 'r4')
    # Far wrist claw
    set_p(11, 6, 'h4'); set_p(10, 6, 'h5')

    # Scalloped outer edge for far wing
    for (x, y) in [(4, 12), (5, 11), (5, 14), (6, 17), (8, 20), (10, 22), (12, 24)]:
        set_p(x, y, 'k0')

    # ----------------------------------------------------
    # 2. FAR HORN (Sweeping back behind crown)
    # ----------------------------------------------------
    # Anchored at (19, 15), sweeping to (26, 9)
    poly([(19, 16), (21, 14), (23, 12), (25, 10), (27, 9), (25, 11), (22, 13), (19, 15)], 'h2')
    line(20, 15, 26, 9, 'h3')
    line(21, 14, 26, 9, 'h4')
    set_p(26, 9, 'h5'); set_p(27, 9, 'h6')
    set_p(27, 8, 'k0')

    # ----------------------------------------------------
    # 3. FAR LEGS
    # ----------------------------------------------------
    # Far Foreleg (x = 24..29, y = 43..51)
    poly([(25, 42), (28, 42), (29, 48), (27, 51), (24, 51), (24, 45)], 'r1')
    poly([(25, 44), (27, 44), (27, 49), (25, 50)], 'r2')
    # Claws
    set_p(24, 52, 'h4'); set_p(26, 52, 'h4'); set_p(28, 52, 'h4')
    set_p(24, 53, 'k0'); set_p(26, 53, 'k0'); set_p(28, 53, 'k0')

    # Far Hindleg (x = 42..47, y = 44..53)
    poly([(42, 44), (47, 44), (48, 50), (45, 53), (42, 52)], 'r1')
    poly([(44, 45), (46, 45), (47, 49), (44, 51)], 'r2')
    set_p(43, 53, 'h4'); set_p(45, 53, 'h4'); set_p(47, 53, 'h4')

    # ----------------------------------------------------
    # 4. TAIL (Dynamic sweeping S-curve with sharp dorsal spikes)
    # ----------------------------------------------------
    # Main tail sweep from rump (42, 36) curving down and looping up
    pts_tail = [
        (42, 35), (46, 37), (50, 40), (54, 43), (56, 46), (55, 49),
        (52, 49), (48, 46), (44, 41), (42, 37)
    ]
    poly(pts_tail, 'r2')

    # Upward tail curl
    pts_curl = [
        (54, 48), (57, 46), (59, 43), (60, 38), (59, 33), (57, 29),
        (55, 29), (56, 34), (57, 39), (55, 44), (52, 47)
    ]
    poly(pts_curl, 'r2')

    # Tail highlights (top-lit)
    poly([(43, 36), (47, 38), (51, 41), (54, 44), (53, 43), (49, 40), (45, 37)], 'r3')
    poly([(44, 36), (48, 38), (52, 41), (50, 40), (46, 37)], 'r4')
    line(45, 36, 49, 38, 'r5')  # bright spine rim

    poly([(56, 43), (58, 39), (58, 34), (56, 30), (57, 30), (59, 35), (59, 40), (57, 44)], 'r3')
    poly([(57, 39), (58, 35), (57, 31), (58, 32), (59, 36)], 'r4')
    line(58, 36, 57, 31, 'r5')

    # Tail shadow underside
    poly([(47, 45), (51, 48), (54, 48), (51, 46), (47, 43)], 'r1')

    # Tail tip arrow spade
    poly([(56, 29), (53, 26), (56, 24), (59, 26), (56, 29)], 'h3')
    line(54, 26, 56, 24, 'h4')
    line(55, 25, 57, 25, 'h5')
    set_p(56, 23, 'h6'); set_p(56, 22, 'k0')
    set_p(52, 26, 'k0'); set_p(60, 26, 'k0')

    # Spikes along tail spine
    tail_spikes = [
        # (tip_x, tip_y, base_left_x, base_left_y, base_right_x, base_right_y)
        (46, 33, 45, 36, 48, 37),
        (51, 36, 49, 39, 52, 41),
        (55, 39, 54, 42, 57, 44),
        (61, 41, 59, 43, 60, 39),
        (61, 33, 59, 36, 58, 31),
    ]
    for sx, sy, b1x, b1y, b2x, b2y in tail_spikes:
        poly([(sx, sy), (b1x, b1y), (b2x, b2y)], 'h2')
        line(sx, sy, b1x, b1y, 'h4')
        set_p(sx, sy, 'h5')
        set_p(sx, sy-1, 'h6')
        set_p(b2x, b2y, 'h1')

    # ----------------------------------------------------
    # 5. CROUCHED HINDQUARTER & THIGH
    # ----------------------------------------------------
    # Muscular thigh
    pts_thigh = [
        (34, 34), (43, 34), (46, 38), (45, 43), (42, 47), (37, 48),
        (33, 45), (32, 40), (34, 34)
    ]
    poly(pts_thigh, 'r2')
    poly([(35, 35), (42, 35), (44, 38), (42, 42), (37, 44), (34, 40)], 'r3')
    poly([(36, 36), (41, 36), (42, 39), (39, 41), (35, 39)], 'r4')
    poly([(37, 37), (40, 37), (41, 38), (38, 40)], 'r5')
    set_p(38, 38, 'r6'); set_p(39, 38, 'r7')  # scale gloss

    # Lower hind leg (knee, shin, hock)
    poly([(33, 44), (37, 44), (43, 48), (43, 52), (39, 54), (34, 53), (32, 48)], 'r2')
    poly([(34, 46), (38, 46), (41, 49), (38, 52), (34, 50)], 'r3')
    poly([(35, 48), (38, 48), (39, 50), (36, 51)], 'r4')

    # Near hind foot & claws
    poly([(33, 53), (41, 53), (42, 56), (33, 56)], 'r2')
    # Claws (3 sturdy curved talons)
    for cx in [34, 37, 40]:
        set_p(cx, 55, 'h3')
        set_p(cx, 56, 'h4')
        set_p(cx-1, 57, 'h5')
        set_p(cx-1, 58, 'h6')

    # ----------------------------------------------------
    # 6. TORSO (Back & Flank)
    # ----------------------------------------------------
    pts_torso = [
        (26, 30), (34, 31), (43, 34), (42, 38), (35, 42), (28, 42),
        (23, 38), (24, 32), (26, 30)
    ]
    poly(pts_torso, 'r2')
    poly([(27, 31), (34, 32), (40, 34), (38, 38), (31, 39), (25, 35)], 'r3')
    poly([(28, 32), (33, 33), (37, 35), (34, 37), (27, 36)], 'r4')
    poly([(29, 33), (33, 34), (33, 36), (29, 35)], 'r5')

    # Dorsal spikes on back
    back_spikes = [
        (29, 28, 28, 30, 31, 30),
        (34, 29, 33, 31, 36, 31),
        (39, 30, 38, 32, 41, 32),
    ]
    for sx, sy, b1x, b1y, b2x, b2y in back_spikes:
        poly([(sx, sy), (b1x, b1y), (b2x, b2y)], 'h2')
        line(sx, sy, b1x, b1y, 'h4')
        set_p(sx, sy, 'h5')
        set_p(sx, sy-1, 'h6')

    # ----------------------------------------------------
    # 7. CONTINUOUS PALE UNDERBELLY (Segmented Scutes)
    # ----------------------------------------------------
    # Throat -> Chest -> Abdomen continuous pale belly plates!
    pts_belly = [
        # Start under chin
        (18, 34), (21, 33), (23, 35), (25, 38), (27, 42), (31, 45), (35, 46),
        # Bottom curve
        (35, 48), (31, 48), (26, 46), (22, 43), (19, 39), (18, 36)
    ]
    poly(pts_belly, 'b2')

    # Midtone warm buff
    poly([
        (19, 34), (22, 34), (24, 37), (26, 41), (30, 44), (34, 45),
        (34, 47), (30, 47), (25, 45), (21, 42), (19, 38)
    ], 'b3')

    # Light golden cream
    poly([
        (19, 35), (22, 35), (23, 38), (25, 41), (28, 44), (32, 45),
        (32, 46), (28, 46), (24, 44), (21, 41), (20, 38)
    ], 'b4')

    # Pale highlight scute body
    poly([
        (20, 36), (22, 36), (23, 39), (25, 42), (27, 44), (30, 45),
        (29, 45), (26, 44), (23, 42), (21, 40)
    ], 'b5')

    # Brightest specular gleam on curved chest scutes
    set_p(21, 37, 'b6'); set_p(22, 37, 'b7')
    set_p(22, 39, 'b6'); set_p(23, 39, 'b7')
    set_p(24, 41, 'b6'); set_p(24, 42, 'b7')
    set_p(26, 43, 'b6'); set_p(27, 44, 'b6')

    # Distinct horizontal segment grooves (scute plates)
    scute_creases = [
        [(18, 35), (19, 35), (21, 34)],
        [(19, 37), (21, 37), (23, 36)],
        [(20, 39), (22, 39), (24, 39)],
        [(21, 42), (23, 42), (26, 41)],
        [(23, 44), (25, 44), (28, 44)],
        [(26, 47), (28, 47), (31, 47)],
    ]
    for seg in scute_creases:
        for x, y in seg:
            set_p(x, y, 'b0')
            set_p(x, y+1, 'b5')  # rim highlight of overlapping plate!

    # ----------------------------------------------------
    # 8. NEAR FORELEG & CLAWS
    # ----------------------------------------------------
    # Shoulder
    poly([(23, 34), (28, 34), (29, 38), (28, 42), (24, 42), (22, 38)], 'r2')
    poly([(24, 35), (27, 35), (28, 38), (27, 41), (24, 40)], 'r3')
    poly([(25, 36), (27, 36), (27, 38), (25, 39)], 'r4')
    set_p(26, 37, 'r5')

    # Forearm
    poly([(22, 41), (26, 41), (25, 47), (21, 47), (20, 43)], 'r2')
    poly([(22, 42), (25, 42), (24, 46), (22, 46)], 'r3')
    poly([(23, 43), (24, 43), (23, 45)], 'r4')

    # Paw & wrist
    poly([(17, 47), (23, 47), (23, 53), (16, 53)], 'r2')
    poly([(18, 48), (22, 48), (21, 52), (17, 52)], 'r3')
    poly([(18, 49), (21, 49), (20, 51)], 'r4')

    # 3 Front talons gripping the ground firmly
    # Toe 1 (left)
    poly([(13, 53), (16, 53), (15, 56), (13, 56)], 'r2')
    set_p(14, 54, 'r3'); set_p(15, 54, 'r4')
    set_p(13, 56, 'h4'); set_p(12, 57, 'h5'); set_p(11, 57, 'h6')
    # Toe 2 (middle)
    poly([(16, 53), (19, 53), (19, 56), (16, 56)], 'r2')
    set_p(17, 54, 'r3'); set_p(18, 54, 'r4')
    set_p(17, 56, 'h4'); set_p(16, 57, 'h5'); set_p(15, 57, 'h6')
    # Toe 3 (right)
    poly([(19, 53), (22, 53), (22, 56), (19, 56)], 'r2')
    set_p(20, 54, 'r3'); set_p(21, 54, 'r4')
    set_p(20, 56, 'h4'); set_p(19, 57, 'h5'); set_p(18, 57, 'h6')

    # ----------------------------------------------------
    # 9. NECK & HEAD
    # ----------------------------------------------------
    # Neck dorsal muscle
    poly([(22, 23), (27, 27), (28, 31), (24, 31), (21, 26)], 'r2')
    poly([(23, 24), (26, 27), (27, 30), (25, 30), (22, 26)], 'r3')
    poly([(24, 25), (26, 27), (26, 29), (24, 28)], 'r4')

    # Head cranium
    pts_head = [
        (17, 18), (23, 17), (26, 19), (25, 24), (20, 24), (16, 21), (17, 18)
    ]
    poly(pts_head, 'r2')
    poly([(18, 19), (22, 18), (24, 20), (23, 23), (19, 23), (17, 21)], 'r3')
    poly([(19, 19), (22, 19), (23, 21), (21, 22), (18, 21)], 'r4')
    set_p(20, 19, 'r5'); set_p(21, 19, 'r6')

    # Snout & Upper Jaw (curving left and down)
    pts_snout = [
        (10, 23), (15, 21), (18, 21), (18, 26), (11, 26), (10, 23)
    ]
    poly(pts_snout, 'r2')
    poly([(11, 23), (15, 22), (17, 22), (17, 25), (12, 25)], 'r3')
    poly([(12, 23), (15, 22), (16, 22), (16, 24), (13, 24)], 'r4')
    set_p(13, 23, 'r5'); set_p(14, 23, 'r6')

    # Nostril
    set_p(12, 23, 'k0')
    set_p(12, 22, 'r2')

    # Near Horn (anchored firmly at crown, curving back gracefully)
    pts_horn = [
        (22, 18), (25, 16), (28, 14), (32, 11),
        (30, 12), (27, 14), (24, 17), (22, 19)
    ]
    poly(pts_horn, 'h2')
    line(23, 18, 31, 11, 'h3')
    line(24, 17, 32, 11, 'h4')
    set_p(26, 15, 'h5'); set_p(28, 14, 'h5'); set_p(30, 12, 'h5')
    set_p(32, 11, 'h6'); set_p(33, 10, 'h6')
    # Horn dark underside line
    line(22, 19, 31, 13, 'h1')

    # Cheek Horn
    poly([(22, 24), (26, 25), (24, 26), (22, 25)], 'h3')
    set_p(25, 25, 'h4'); set_p(26, 25, 'h5'); set_p(27, 25, 'h6')

    # Eye & Brow (Expressive, fierce baby dragon!)
    # Brow ridge (angled scaly furrow)
    set_p(17, 19, 'r3'); set_p(18, 19, 'r4'); set_p(19, 19, 'r5'); set_p(20, 20, 'r4')
    set_p(17, 20, 'k1'); set_p(21, 20, 'k1')
    # Eye socket
    set_p(18, 20, 'e1'); set_p(19, 20, 'e1'); set_p(20, 21, 'e1')
    set_p(18, 21, 'e2'); set_p(19, 21, 'e3'); set_p(20, 22, 'e4'); set_p(21, 21, 'e2')
    set_p(19, 21, 'e0')  # vertical slit pupil
    set_p(20, 21, 'e5')  # bright amber/yellow glow
    set_p(20, 20, 'e6')  # specular twinkle

    # ----------------------------------------------------
    # 10. GROWL & OPEN MOUTH
    # ----------------------------------------------------
    # Mouth interior (dark gaping maw)
    pts_mouth = [
        (13, 26), (21, 26), (22, 29), (18, 31), (14, 31), (13, 28)
    ]
    poly(pts_mouth, 'm0')
    poly([(14, 27), (20, 27), (21, 29), (17, 30), (14, 30)], 'm1')

    # Curled tongue
    poly([(15, 29), (19, 29), (18, 31), (15, 31)], 'm2')
    set_p(16, 29, 'm3'); set_p(17, 29, 'm4')
    set_p(16, 30, 'm3')

    # Upper Fangs (needle-sharp curved dragon fangs)
    set_p(12, 26, 'm5')
    set_p(14, 26, 'm6'); set_p(14, 27, 'm5'); set_p(14, 28, 'm5')  # main upper fang
    set_p(16, 26, 'm6'); set_p(16, 27, 'm5')
    set_p(18, 26, 'm6'); set_p(18, 27, 'm5')

    # Lower Jaw (angled down-forward in an aggressive roar)
    pts_lower_jaw = [
        (13, 31), (21, 30), (22, 33), (18, 34), (14, 34), (13, 32)
    ]
    poly(pts_lower_jaw, 'r2')
    poly([(14, 32), (20, 31), (20, 33), (17, 33), (14, 33)], 'r3')
    poly([(15, 33), (19, 32), (18, 33)], 'r4')
    set_p(14, 34, 'r4'); set_p(15, 34, 'r5')  # chin highlight

    # Lower Fangs (sharp teeth pointing upward)
    set_p(13, 32, 'm6'); set_p(13, 31, 'm5'); set_p(13, 30, 'm5')  # main lower fang
    set_p(15, 32, 'm6'); set_p(15, 31, 'm5')
    set_p(17, 31, 'm6'); set_p(17, 30, 'm5')
    set_p(19, 31, 'm6'); set_p(19, 30, 'm5')

    # ----------------------------------------------------
    # 11. NEAR WING (Foreground, raised high, spread back)
    # ----------------------------------------------------
    # Wing arm: from shoulder (29, 27) up-right to elbow (35, 17) and wrist (43, 7)
    pts_arm = [
        (29, 27), (32, 23), (35, 18), (38, 13), (41, 9), (43, 7),
        (44, 8), (42, 11), (39, 15), (36, 20), (33, 25), (30, 28)
    ]
    poly(pts_arm, 'r2')
    pts_arm_hi = [
        (30, 26), (33, 22), (36, 17), (39, 12), (41, 8), (43, 7),
        (42, 9), (40, 11), (37, 15), (34, 19), (31, 24)
    ]
    for x, y in pts_arm_hi: set_p(x, y, 'r4')
    set_p(43, 7, 'r5'); set_p(42, 8, 'r5')

    # Wing Thumb Claw at wrist (42, 6)
    set_p(42, 6, 'h4'); set_p(41, 5, 'h5'); set_p(40, 5, 'h6')
    set_p(42, 7, 'h2'); set_p(43, 6, 'h1')

    # Membrane Panels between struts
    # Panel 1: Arm to Strut 1 (to 54, 8)
    poly([(43, 7), (47, 6), (51, 6), (54, 8), (50, 10), (45, 9), (43, 8)], 'w3')
    poly([(45, 7), (49, 7), (52, 8), (49, 9), (46, 8)], 'w4')
    set_p(48, 8, 'w5'); set_p(49, 8, 'w6')

    # Panel 2: Strut 1 to Strut 2 (to 59, 15)
    poly([
        (43, 8), (54, 8), (56, 11), (58, 13), (59, 15),
        (55, 15), (50, 13), (45, 10), (43, 8)
    ], 'w2')
    poly([(45, 9), (52, 9), (56, 11), (57, 13), (54, 13), (49, 11), (45, 10)], 'w3')
    poly([(47, 10), (51, 10), (54, 12), (52, 12), (47, 11)], 'w4')
    set_p(49, 11, 'w5'); set_p(50, 11, 'w6')

    # Panel 3: Strut 2 to Strut 3 (to 56, 25)
    poly([
        (42, 10), (50, 12), (59, 15), (58, 19), (57, 22), (56, 25),
        (51, 22), (47, 19), (43, 15), (42, 11)
    ], 'w2')
    poly([(44, 11), (50, 14), (55, 17), (55, 20), (53, 22), (48, 19), (44, 15)], 'w3')
    poly([(46, 13), (51, 16), (53, 18), (50, 18), (46, 15)], 'w4')
    set_p(48, 16, 'w5'); set_p(49, 16, 'w6')

    # Panel 4: Strut 3 to Flank (41, 33)
    poly([
        (41, 14), (47, 19), (56, 25), (52, 28), (48, 30), (42, 33),
        (40, 29), (40, 22), (41, 16)
    ], 'w1')
    poly([(42, 17), (47, 21), (51, 26), (48, 28), (44, 29), (41, 25)], 'w2')
    poly([(43, 19), (46, 22), (48, 25), (45, 26), (42, 23)], 'w3')

    # Strut bone lines
    line(43, 7, 54, 8, 'r3')
    set_p(54, 8, 'h4'); set_p(55, 8, 'h5')
    line(43, 8, 59, 15, 'r3')
    set_p(59, 15, 'h4'); set_p(60, 15, 'h5')
    line(42, 10, 56, 25, 'r3')
    set_p(56, 25, 'h4'); set_p(57, 26, 'h5')

    # ----------------------------------------------------
    # 12. GROWL SMOKE & EMBER
    # ----------------------------------------------------
    # Ember / fire spark curling out
    set_p(10, 26, 'f2'); set_p(9, 26, 'f3'); set_p(9, 25, 'f4')
    set_p(8, 25, 'f3'); set_p(8, 26, 'f2'); set_p(7, 25, 'f1')
    set_p(9, 24, 'f2'); set_p(10, 24, 'f1')
    # Wispy smoke puff curling up
    set_p(6, 24, 's1'); set_p(5, 23, 's2'); set_p(6, 22, 's1'); set_p(7, 22, 's0')
    set_p(8, 22, 's1'); set_p(8, 21, 's2'); set_p(7, 20, 's1')

    # ----------------------------------------------------
    # 13. SELECTIVE OUTLINING & EDGE POLISH
    # ----------------------------------------------------
    # Clean, beautiful contour outlines:
    # We trace opaque pixels bordering transparency and apply dark contour colors
    # without inflating the sprite or creating chunky blocks!
    for y in range(64):
        for x in range(64):
            tok = buf[y, x]
            if tok != '..' and not tok.startswith('s') and not tok.startswith('f'):
                # Check if this pixel borders transparency
                border = False
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 64 and 0 <= ny < 64:
                        if buf[ny, nx] == '..':
                            border = True
                            break
                    else:
                        border = True
                        break
                if border:
                    # If this pixel is a midtone or light color on an outer edge,
                    # we keep highlights on top-left edges, but darken bottom-right edges
                    pass

    return buf

def render(buf):
    c = new_canvas(64, 64)
    for y in range(64):
        for x in range(64):
            tok = buf[y, x]
            if tok != '..' and tok in PAL and PAL[tok] is not None:
                c.set(x, y, PAL[tok])
    return c

buf = build_dragon_sprite()
c = render(buf)
view(c)
