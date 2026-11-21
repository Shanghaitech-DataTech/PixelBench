import numpy as np
from pixelbench_api import *

# Palette definition
P = {
    '..': None,
    # Outline & dark contour
    'k0': '#15040d',  # darkest outline
    'k1': '#260817',  # dark contour
    'k2': '#3d0c24',  # deep shadow
    'k3': '#54122e',  # dark shadow crease

    # Red dragon scales (main body)
    'r1': '#6e152d',  # scale shadow
    'r2': '#8e1b34',  # scale deep mid
    'r3': '#b3233a',  # scale midtone
    'r4': '#d43243',  # scale bright red
    'r5': '#ee4d4b',  # scale highlight
    'r6': '#fa6e5c',  # scale bright rim
    'r7': '#ff9478',  # scale specular

    # Underbelly plates (pale warm cream / peach / gold)
    'b0': '#3a2014',  # belly dark contour
    'b1': '#613b20',  # belly deep crease
    'b2': '#8c5932',  # belly shadow
    'b3': '#b87e4a',  # belly midtone
    'b4': '#dba668',  # belly cream base
    'b5': '#f0c78a',  # belly light cream
    'b6': '#fae2b1',  # belly highlight
    'b7': '#fff2d6',  # belly bright specular

    # Leathery wings (warm terracotta / amber)
    'w0': '#36121a',  # wing edge dark
    'w1': '#5c1d22',  # wing dark
    'w2': '#822a28',  # wing shadow
    'w3': '#a83c2e',  # wing midtone
    'w4': '#c95436',  # wing warm mid
    'w5': '#e27343',  # wing light
    'w6': '#f39459',  # wing glow
    'w7': '#fbb875',  # wing rim light

    # Horns, spikes, claws (Ivory / Horn)
    'h0': '#221a16',  # horn dark outline
    'h1': '#42332a',  # horn shadow
    'h2': '#6b5444',  # horn mid shadow
    'h3': '#9c816a',  # horn base
    'h4': '#c4ab93',  # horn light ivory
    'h5': '#e2d2bf',  # horn pale ivory
    'h6': '#fcf8f2',  # horn tip highlight

    # Eye
    'e0': '#120308',  # eye socket / pupil slit
    'e1': '#420815',  # eye contour
    'e2': '#9e5000',  # eye amber shadow
    'e3': '#e68a00',  # eye bright amber
    'e4': '#ffc400',  # eye bright gold
    'e5': '#ffee66',  # eye intense yellow
    'e6': '#ffffff',  # eye white catchlight

    # Mouth interior & teeth
    'm0': '#1f040d',  # throat depth
    'm1': '#4a0a1f',  # mouth dark cavity
    'm2': '#781532',  # tongue dark
    'm3': '#b0254c',  # tongue mid
    'm4': '#e04a72',  # tongue highlight
    'm5': '#fff0e8',  # teeth ivory white

    # Flame spark / ember & smoke puff
    'f0': '#9e1a12',  # flame dark
    'f1': '#d93b16',  # flame mid red
    'f2': '#f76a1e',  # flame orange
    'f3': '#ffa826',  # flame bright gold
    'f4': '#ffea6c',  # flame yellow core
    's0': '#4a2f38',  # smoke shadow
    's1': '#75525d',  # smoke mid
    's2': '#a37c88',  # smoke light
}

def create_dragon_grid():
    grid = np.full((64, 64), '..', dtype=object)

    def p(x, y, token):
        if 0 <= x < 64 and 0 <= y < 64:
            grid[y, x] = token

    def fill_poly(pts, token):
        # Scanline polygon fill
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
                    grid[y, x] = token

    # ==========================================
    # LAYER 1: FAR WING (Background Wing, top-left)
    # ==========================================
    # Webbing base
    pts_far_wing = [
        (24, 22), (18, 14), (13, 8), (11, 8), (5, 12), (7, 16),
        (8, 20), (11, 22), (14, 24), (20, 26), (24, 22)
    ]
    fill_poly(pts_far_wing, 'w1')

    # Membrane shading for far wing
    fill_poly([(18, 14), (13, 10), (7, 13), (8, 17), (12, 19), (18, 18)], 'w2')
    fill_poly([(16, 15), (12, 12), (8, 15), (10, 18), (15, 17)], 'w3')
    fill_poly([(14, 14), (10, 14), (11, 16), (14, 16)], 'w4')

    # Far wing bone struts
    pts_f_strut1 = [(13, 8), (10, 10), (5, 12)]
    for x, y in pts_f_strut1: p(x, y, 'r2')
    pts_f_strut2 = [(14, 11), (11, 15), (8, 20)]
    for x, y in pts_f_strut2: p(x, y, 'r2')
    pts_f_strut3 = [(16, 14), (14, 19), (14, 24)]
    for x, y in pts_f_strut3: p(x, y, 'r2')

    # Main arm of far wing
    pts_f_arm = [(24, 22), (22, 19), (19, 15), (16, 12), (13, 8)]
    for x, y in pts_f_arm:
        p(x, y, 'r3')
        p(x, y-1, 'r4')
        p(x+1, y, 'r2')
    # Claw on far wing wrist
    p(12, 7, 'h4')
    p(11, 7, 'h5')
    p(10, 8, 'h2')

    # Outline for far wing
    pts_f_out = [
        (4, 12), (5, 11), (6, 11), (7, 12), (8, 13), (9, 13),
        (6, 15), (6, 16), (7, 18), (8, 20), (9, 21), (10, 22),
        (12, 23), (13, 24), (14, 25), (15, 25), (16, 25)
    ]
    for x, y in pts_f_out: p(x, y, 'k0')

    # ==========================================
    # LAYER 2: FAR LEGS & FAR HORN
    # ==========================================
    # Far Horn (sweeping back behind head)
    pts_f_horn = [(20, 16), (22, 13), (24, 11), (27, 9)]
    for x, y in pts_f_horn:
        p(x, y, 'h3')
        p(x+1, y, 'h1')
    p(26, 10, 'h4')
    p(27, 9, 'h5')
    p(28, 9, 'h6')
    p(28, 8, 'k0')

    # Far Foreleg (planted back at x=26..31, y=44..52)
    fill_poly([(26, 42), (30, 42), (31, 48), (28, 52), (25, 52), (25, 46)], 'r1')
    fill_poly([(27, 44), (29, 44), (29, 49), (27, 51)], 'r2')
    # Far claws
    p(25, 53, 'h4'); p(27, 53, 'h4'); p(29, 53, 'h4')
    p(24, 52, 'k0'); p(26, 52, 'k0'); p(28, 52, 'k0'); p(30, 52, 'k0')

    # Far Hindleg
    fill_poly([(43, 44), (48, 44), (49, 51), (46, 54), (43, 52)], 'r1')
    fill_poly([(45, 45), (47, 45), (48, 50), (45, 52)], 'r2')
    p(44, 54, 'h4'); p(46, 54, 'h4'); p(48, 54, 'h4')

    # ==========================================
    # LAYER 3: TAIL (Sweeping back and curled up)
    # ==========================================
    # Tail main curve
    pts_tail = [
        (42, 36), (46, 38), (51, 41), (55, 44), (57, 47), (55, 50),
        (51, 49), (47, 45), (44, 40), (42, 38)
    ]
    fill_poly(pts_tail, 'r2')

    # Tail upward curl
    pts_tail_curl = [
        (54, 48), (57, 47), (59, 44), (60, 39), (59, 34), (57, 30),
        (55, 30), (56, 35), (57, 40), (55, 44), (53, 46)
    ]
    fill_poly(pts_tail_curl, 'r2')

    # Tail highlights (top edge)
    fill_poly([(44, 37), (48, 39), (52, 42), (55, 44), (54, 43), (50, 40), (45, 38)], 'r3')
    fill_poly([(45, 37), (49, 39), (53, 42), (52, 41), (48, 38)], 'r4')
    fill_poly([(57, 44), (58, 40), (58, 35), (56, 32), (57, 32), (59, 36), (59, 41), (58, 44)], 'r3')
    fill_poly([(58, 39), (58, 35), (57, 32), (58, 33), (59, 37)], 'r4')

    # Tail underside shadow
    fill_poly([(48, 46), (52, 49), (55, 49), (52, 47), (48, 44)], 'r1')

    # Tail tip spade / arrow barb
    pts_spade = [(56, 30), (53, 27), (56, 25), (59, 27), (56, 30)]
    fill_poly(pts_spade, 'h3')
    p(56, 25, 'h5'); p(56, 24, 'h6')
    p(53, 27, 'h4'); p(59, 27, 'h2')
    p(55, 26, 'h4'); p(57, 26, 'h4')

    # Spikes along tail
    tail_spikes = [
        # (tip_x, tip_y, b1_x, b1_y, b2_x, b2_y)
        (46, 34, 45, 37, 48, 38),
        (51, 37, 50, 40, 53, 42),
        (56, 40, 55, 43, 58, 45),
        (61, 41, 59, 43, 60, 39),
        (61, 34, 59, 36, 58, 32),
    ]
    for sx, sy, b1x, b1y, b2x, b2y in tail_spikes:
        fill_poly([(sx, sy), (b1x, b1y), (b2x, b2y)], 'h3')
        p(sx, sy, 'h5')
        p(sx, sy-1, 'h6')
        p(b1x, b1y, 'h2')

    # ==========================================
    # LAYER 4: TORSO & CROUCHED HINDQUARTERS
    # ==========================================
    # Pelvis & thigh
    pts_thigh = [
        (35, 34), (43, 34), (46, 38), (46, 43), (43, 47), (38, 48),
        (33, 45), (32, 40), (35, 34)
    ]
    fill_poly(pts_thigh, 'r2')

    # Thigh volume & shading
    fill_poly([(36, 35), (42, 35), (44, 38), (42, 42), (37, 43), (34, 39)], 'r3')
    fill_poly([(37, 36), (41, 36), (42, 39), (39, 41), (36, 38)], 'r4')
    fill_poly([(38, 37), (40, 37), (41, 38), (38, 39)], 'r5')
    p(39, 37, 'r6')  # specular scale highlight on thigh

    # Near Hindleg (knee, hock, foot)
    fill_poly([(33, 44), (37, 44), (43, 48), (43, 52), (39, 54), (34, 53), (33, 48)], 'r2')
    fill_poly([(35, 46), (39, 46), (41, 49), (38, 52), (35, 50)], 'r3')
    fill_poly([(36, 48), (38, 48), (39, 50), (37, 51)], 'r4')

    # Near hind foot & talons
    fill_poly([(34, 53), (41, 53), (42, 56), (34, 56)], 'r2')
    # Talons (3 sharp claws)
    p(34, 57, 'h5'); p(35, 56, 'h4'); p(35, 55, 'h3')
    p(37, 57, 'h5'); p(38, 56, 'h4'); p(38, 55, 'h3')
    p(40, 57, 'h5'); p(41, 56, 'h4'); p(41, 55, 'h3')

    # Torso back / dorsal region
    pts_torso = [
        (26, 31), (35, 32), (43, 34), (43, 38), (35, 42), (28, 42),
        (23, 38), (24, 33), (26, 31)
    ]
    fill_poly(pts_torso, 'r2')
    fill_poly([(27, 32), (34, 33), (40, 35), (38, 38), (31, 38), (26, 35)], 'r3')
    fill_poly([(28, 33), (33, 34), (37, 36), (34, 37), (28, 36)], 'r4')
    fill_poly([(29, 34), (33, 35), (32, 36), (29, 35)], 'r5')

    # Dorsal spikes on back
    back_spikes = [
        (29, 29, 28, 31, 31, 31),
        (34, 30, 33, 32, 36, 32),
        (39, 31, 38, 33, 41, 33),
    ]
    for sx, sy, b1x, b1y, b2x, b2y in back_spikes:
        fill_poly([(sx, sy), (b1x, b1y), (b2x, b2y)], 'h3')
        p(sx, sy, 'h5')
        p(sx, sy-1, 'h6')

    # ==========================================
    # LAYER 5: PALE UNDERBELLY (Segmented Scutes)
    # ==========================================
    # Underbelly plates running from throat under chest to groin
    pts_belly = [
        (21, 34), (24, 34), (25, 38), (28, 43), (32, 46), (36, 47),
        (35, 49), (30, 49), (25, 46), (22, 42), (20, 38), (20, 35)
    ]
    fill_poly(pts_belly, 'b2')

    # Belly plates base shading
    fill_poly([
        (21, 35), (23, 35), (24, 38), (26, 42), (30, 45), (34, 46),
        (33, 48), (29, 48), (24, 45), (21, 41), (21, 37)
    ], 'b3')

    fill_poly([
        (22, 36), (23, 36), (24, 39), (26, 42), (29, 45), (32, 46),
        (31, 47), (28, 47), (23, 44), (21, 40)
    ], 'b4')

    fill_poly([
        (22, 37), (23, 37), (24, 40), (25, 42), (27, 44), (29, 45),
        (28, 46), (25, 45), (23, 43), (22, 40)
    ], 'b5')

    # Brightest center highlight on chest scutes
    p(23, 38, 'b6'); p(23, 39, 'b6'); p(24, 41, 'b6'); p(25, 42, 'b6'); p(26, 43, 'b6')
    p(23, 39, 'b7'); p(24, 41, 'b7')  # specular shine

    # Belly plate segment creases (dark grooves between scutes)
    creases = [
        [(20, 36), (21, 36), (23, 35)],
        [(20, 38), (22, 38), (24, 38)],
        [(21, 41), (23, 41), (26, 41)],
        [(23, 44), (25, 44), (28, 44)],
        [(26, 47), (28, 47), (31, 47)],
    ]
    for seg in creases:
        for x, y in seg:
            p(x, y, 'b0')
            p(x, y+1, 'b5')  # bottom highlight of scute edge

    # ==========================================
    # LAYER 6: NEAR FORELEG & CLAWS
    # ==========================================
    # Muscular shoulder
    fill_poly([(23, 34), (28, 34), (30, 38), (28, 43), (24, 42), (22, 38)], 'r2')
    fill_poly([(24, 35), (27, 35), (28, 38), (27, 41), (24, 40)], 'r3')
    fill_poly([(25, 36), (27, 36), (27, 38), (25, 39)], 'r4')
    p(26, 37, 'r5')

    # Forearm
    fill_poly([(23, 41), (27, 41), (26, 47), (21, 47), (21, 43)], 'r2')
    fill_poly([(23, 42), (25, 42), (24, 46), (22, 46)], 'r3')
    fill_poly([(23, 43), (24, 43), (24, 45)], 'r4')

    # Front paw & wrist
    fill_poly([(18, 47), (24, 47), (24, 53), (17, 53)], 'r2')
    fill_poly([(19, 48), (23, 48), (22, 52), (18, 52)], 'r3')
    fill_poly([(19, 49), (22, 49), (21, 51)], 'r4')

    # 3 Front talons
    # Toe 1 (left)
    fill_poly([(14, 53), (17, 53), (16, 56), (14, 56)], 'r2')
    p(14, 54, 'r3'); p(15, 54, 'r4')
    p(13, 56, 'h4'); p(13, 57, 'h5'); p(12, 57, 'h6')
    # Toe 2 (middle)
    fill_poly([(17, 53), (20, 53), (20, 56), (17, 56)], 'r2')
    p(18, 54, 'r3'); p(19, 54, 'r4')
    p(17, 56, 'h4'); p(17, 57, 'h5'); p(16, 57, 'h6')
    # Toe 3 (right)
    fill_poly([(20, 53), (23, 53), (23, 56), (20, 56)], 'r2')
    p(21, 54, 'r3'); p(22, 54, 'r4')
    p(21, 56, 'h4'); p(21, 57, 'h5'); p(20, 57, 'h6')

    # ==========================================
    # LAYER 7: NECK & HEAD (Fierce hatchling growl!)
    # ==========================================
    # Neck dorsal curve
    fill_poly([(23, 23), (28, 28), (29, 32), (24, 32), (21, 26)], 'r2')
    fill_poly([(24, 24), (27, 28), (28, 31), (25, 31), (22, 26)], 'r3')
    fill_poly([(25, 25), (27, 28), (27, 30), (24, 28)], 'r4')

    # Neck spikes
    neck_spikes = [
        (22, 21, 22, 23, 24, 23),
        (26, 24, 25, 26, 28, 27),
    ]
    for sx, sy, b1x, b1y, b2x, b2y in neck_spikes:
        fill_poly([(sx, sy), (b1x, b1y), (b2x, b2y)], 'h3')
        p(sx, sy, 'h5')

    # Head crown & cranium
    pts_head = [
        (17, 18), (23, 17), (26, 20), (25, 24), (20, 24), (16, 21), (17, 18)
    ]
    fill_poly(pts_head, 'r2')
    fill_poly([(18, 19), (22, 18), (24, 21), (23, 23), (19, 23), (17, 21)], 'r3')
    fill_poly([(19, 19), (22, 19), (23, 21), (21, 22), (18, 21)], 'r4')
    p(20, 19, 'r5'); p(21, 19, 'r6')

    # Snout & Upper Jaw (extending forward-left)
    pts_snout = [
        (10, 23), (16, 21), (19, 21), (19, 26), (11, 26), (10, 23)
    ]
    fill_poly(pts_snout, 'r2')
    fill_poly([(11, 23), (15, 22), (18, 22), (18, 25), (12, 25)], 'r3')
    fill_poly([(12, 23), (15, 22), (17, 22), (17, 24), (13, 24)], 'r4')
    p(13, 23, 'r5'); p(14, 23, 'r6')  # bridge of nose highlight

    # Nostril
    p(12, 23, 'k0')
    p(12, 22, 'r1')

    # Near Horn (curving back from crown)
    pts_horn = [
        (23, 17), (25, 15), (28, 13), (32, 11),
        (30, 12), (27, 14), (24, 17)
    ]
    fill_poly(pts_horn, 'h3')
    p(25, 16, 'h4'); p(27, 14, 'h4'); p(29, 13, 'h4'); p(31, 12, 'h5'); p(32, 11, 'h6')
    p(33, 10, 'h6')  # sharp horn tip
    # Horn shadow edge
    p(24, 18, 'h1'); p(26, 16, 'h1'); p(28, 14, 'h1'); p(31, 13, 'h1')

    # Cheek Horn / spike
    fill_poly([(22, 24), (26, 25), (24, 26), (22, 25)], 'h3')
    p(26, 25, 'h5'); p(27, 25, 'h6')

    # Brow crest / ridge above eye
    p(17, 20, 'r4'); p(18, 19, 'r5'); p(19, 19, 'r5'); p(20, 20, 'r4')

    # Eye (Big, fierce dragon hatchling eye!)
    p(18, 21, 'e1'); p(19, 21, 'e1'); p(20, 21, 'e1'); p(21, 21, 'e1')
    p(18, 22, 'e2'); p(19, 22, 'e3'); p(20, 22, 'e4'); p(21, 22, 'e2')
    p(19, 22, 'e0')  # vertical slit pupil
    p(20, 22, 'e5')  # bright gold iris glow
    p(20, 21, 'e6')  # sharp catchlight

    # MOUTH & LOW GROWL (Wide open mouth showing fangs and tongue)
    # Mouth interior cavity (dark deep throat)
    pts_mouth = [
        (13, 26), (21, 26), (22, 29), (18, 31), (14, 31), (13, 28)
    ]
    fill_poly(pts_mouth, 'm0')
    fill_poly([(15, 27), (20, 27), (21, 29), (17, 30), (15, 29)], 'm1')

    # Tongue inside mouth
    fill_poly([(15, 29), (19, 29), (18, 31), (15, 31)], 'm2')
    p(16, 29, 'm3'); p(17, 29, 'm4')

    # Upper Fangs (sharp needle teeth hanging down)
    p(12, 26, 'm5')
    p(14, 27, 'm5'); p(14, 28, 'm5')  # big front fang
    p(16, 27, 'm5')
    p(18, 27, 'm5')

    # Lower Jaw (dropped open in a growl)
    pts_lower_jaw = [
        (13, 31), (22, 30), (23, 33), (18, 34), (14, 34), (13, 32)
    ]
    fill_poly(pts_lower_jaw, 'r2')
    fill_poly([(14, 32), (21, 31), (21, 33), (17, 33), (14, 33)], 'r3')
    fill_poly([(15, 33), (19, 32), (18, 33)], 'r4')

    # Lower Fangs (sharp teeth pointing up)
    p(13, 31, 'm5'); p(13, 30, 'm5')  # lower front canine fang
    p(15, 31, 'm5')
    p(17, 30, 'm5')
    p(19, 30, 'm5')

    # Chin scale highlight
    p(14, 34, 'r4'); p(15, 34, 'r5')

    # ==========================================
    # LAYER 8: NEAR WING (Foreground Wing, arched high & spread)
    # ==========================================
    # Near Wing Arm (sweeping from shoulder up-right to wrist)
    # Shoulder base: (29, 27)
    # Elbow: (36, 17)
    # Wrist: (44, 7)
    pts_arm_bone = [
        (29, 28), (32, 24), (35, 19), (38, 14), (41, 10), (44, 7),
        (45, 8), (42, 12), (39, 16), (36, 21), (33, 26), (30, 29)
    ]
    fill_poly(pts_arm_bone, 'r2')
    # Arm highlight
    pts_arm_hi = [
        (30, 27), (33, 23), (36, 18), (39, 13), (42, 9), (44, 7),
        (43, 8), (40, 11), (37, 15), (34, 20), (31, 24)
    ]
    for x, y in pts_arm_hi: p(x, y, 'r4')
    p(44, 7, 'r5'); p(43, 8, 'r5')

    # Wing Thumb Claw at wrist (43, 6)
    p(43, 6, 'h4'); p(42, 5, 'h5'); p(41, 5, 'h6')
    p(43, 7, 'h2'); p(44, 6, 'h1')

    # Wing Struts (Fingers) radiating from wrist (44, 7):
    # Strut 1: to (54, 8)
    # Strut 2: to (59, 16)
    # Strut 3: to (56, 26)
    # Strut 4 / trailing edge: to (41, 33)

    # Near wing membrane webbing
    # Membrane section 1: between arm and strut 1
    pts_mem1 = [
        (44, 7), (47, 6), (51, 6), (54, 8),
        (50, 10), (46, 10), (44, 8)
    ]
    fill_poly(pts_mem1, 'w3')
    fill_poly([(46, 7), (49, 7), (52, 8), (49, 9), (46, 9)], 'w4')
    p(48, 8, 'w5'); p(49, 8, 'w6')

    # Membrane section 2: between strut 1 and strut 2
    pts_mem2 = [
        (44, 8), (54, 8), (56, 11), (58, 14), (59, 16),
        (55, 16), (50, 14), (46, 11), (44, 8)
    ]
    fill_poly(pts_mem2, 'w2')
    fill_poly([(46, 9), (53, 9), (56, 12), (57, 14), (54, 14), (49, 12), (46, 10)], 'w3')
    fill_poly([(48, 10), (52, 10), (54, 12), (52, 13), (48, 11)], 'w4')
    p(50, 11, 'w5'); p(51, 11, 'w6')  # translucent glow

    # Membrane section 3: between strut 2 and strut 3
    pts_mem3 = [
        (43, 10), (51, 13), (59, 16), (58, 20), (57, 23), (56, 26),
        (52, 23), (48, 20), (44, 16), (43, 12)
    ]
    fill_poly(pts_mem3, 'w2')
    fill_poly([(45, 12), (51, 15), (56, 18), (56, 21), (54, 23), (49, 20), (45, 16)], 'w3')
    fill_poly([(47, 14), (52, 17), (54, 19), (51, 19), (47, 16)], 'w4')
    p(49, 17, 'w5'); p(50, 17, 'w6')

    # Membrane section 4: between strut 3 and flank (41, 33)
    pts_mem4 = [
        (42, 15), (48, 20), (56, 26), (53, 29), (49, 31), (43, 33),
        (41, 30), (41, 23), (42, 17)
    ]
    fill_poly(pts_mem4, 'w1')
    fill_poly([(43, 18), (48, 22), (52, 27), (49, 29), (45, 30), (42, 26)], 'w2')
    fill_poly([(44, 20), (47, 23), (49, 26), (46, 27), (43, 24)], 'w3')

    # Finger bone lines (struts)
    # Strut 1
    pts_s1 = [(44, 7), (47, 7), (50, 8), (54, 8)]
    for x, y in pts_s1: p(x, y, 'r3')
    p(54, 8, 'h4'); p(55, 8, 'h5')  # claw at tip of finger 1

    # Strut 2
    pts_s2 = [(44, 8), (48, 11), (52, 13), (56, 15), (59, 16)]
    for x, y in pts_s2: p(x, y, 'r3')
    p(59, 16, 'h4'); p(60, 16, 'h5')  # claw at tip of finger 2

    # Strut 3
    pts_s3 = [(43, 11), (47, 16), (51, 20), (54, 23), (56, 26)]
    for x, y in pts_s3: p(x, y, 'r3')
    p(56, 26, 'h4'); p(57, 27, 'h5')  # claw at tip of finger 3

    # ==========================================
    # LAYER 9: GROWL EFFECTS (Smoke wisp & spark)
    # ==========================================
    # Fire ember / spark emerging from mouth
    p(10, 26, 'f2'); p(9, 26, 'f3'); p(9, 25, 'f4')
    p(8, 25, 'f3'); p(8, 26, 'f2'); p(7, 25, 'f1')
    p(9, 24, 'f2'); p(10, 24, 'f1')
    # Tiny smoke curl
    p(6, 24, 's1'); p(5, 23, 's2'); p(6, 22, 's1'); p(7, 22, 's0')
    p(8, 22, 's1'); p(8, 21, 's2'); p(7, 20, 's1')

    # ==========================================
    # LAYER 10: CRISP SPRITE OUTLINE (Selective Outlining)
    # ==========================================
    # Add dark outlines along outer edges touching transparent background
    def add_outline():
        outlines = []
        for y in range(64):
            for x in range(64):
                if grid[y, x] != '..':
                    # check 4 neighbors
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 64 and 0 <= ny < 64:
                            if grid[ny, nx] == '..':
                                outlines.append((nx, ny, x, y))
                        else:
                            pass
        # Only put outline on transparent pixels that border opaque pixels
        # But we want the sprite bounded within the canvas
        for nx, ny, sx, sy in outlines:
            # We don't overwrite the sprite itself, nx, ny is transparent!
            # Determine outline shade based on neighboring sprite color
            s_tok = grid[sy, sx]
            if s_tok and not s_tok.startswith('s') and not s_tok.startswith('f'):
                grid[ny, nx] = 'k0'

    add_outline()

    return grid

def render_to_canvas(grid):
    c = new_canvas(64, 64)
    for y in range(64):
        for x in range(64):
            tok = grid[y, x]
            if tok != '..' and tok in P and P[tok] is not None:
                c.set(x, y, P[tok])
    return c

grid = create_dragon_grid()
c = render_to_canvas(grid)
view(c)
