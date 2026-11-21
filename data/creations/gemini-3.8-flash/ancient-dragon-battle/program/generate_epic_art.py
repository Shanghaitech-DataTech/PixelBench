import math
import random

W, H = 256, 256

PALETTE = {
    # Sunset Sky Gradient (11)
    "sky_0": "#0a0412",
    "sky_1": "#150822",
    "sky_2": "#2c0a34",
    "sky_3": "#4c0f3e",
    "sky_4": "#78163c",
    "sky_5": "#a32230",
    "sky_6": "#cf3a22",
    "sky_7": "#e85e1c",
    "sky_8": "#fca429",
    "sky_9": "#fed852",
    "sky_10": "#fff29a",

    # Mountains & Horizon (5)
    "mtn_dark": "#120a1c",
    "mtn_mid": "#22122d",
    "mtn_light": "#381c42",
    "mtn_rim": "#8f283c",
    "mtn_gold": "#e85e1c",

    # Volumetric Smoke & Dust (7)
    "smk_black": "#0c0810",
    "smk_dark": "#18111c",
    "smk_mid": "#2a1e2e",
    "smk_light": "#423246",
    "smk_pale": "#644e66",
    "smk_warm": "#8e4434",
    "smk_fire": "#cc5e2e",

    # Dragon (17)
    "drg_out": "#060308",
    "drg_dark": "#120812",
    "drg_s1": "#200a18",
    "drg_s2": "#360e1e",
    "drg_s3": "#541222",
    "drg_s4": "#7c1624",
    "drg_s5": "#a61e26",
    "drg_s6": "#d43424",
    "drg_b1": "#260c0a",
    "drg_b2": "#4a1410",
    "drg_b3": "#7a2416",
    "drg_b4": "#b23e1a",
    "drg_w1": "#180812",
    "drg_w2": "#2c0e1a",
    "drg_w3": "#4a1422",
    "drg_w4": "#741e26",
    "drg_horn1": "#161a22",
    "drg_horn2": "#363e4e",
    "drg_horn3": "#6e7c90",

    # Fire, Dragon Breath & Explosions (8)
    "f_white": "#ffffff",
    "f_pale": "#fff7a4",
    "f_yellow": "#fed852",
    "f_orange": "#fa821c",
    "f_red": "#e03b18",
    "f_crimson": "#a61919",
    "f_dark": "#5a0c14",
    "f_char": "#21050a",

    # Castle Stone & Masonry (10)
    "st_deep": "#0a0c12",
    "st_shadow": "#12151e",
    "st_dark": "#1c222c",
    "st_mid": "#2a3240",
    "st_light": "#3e485a",
    "st_pale": "#5a667c",
    "st_hi": "#7e8ba2",
    "st_warm1": "#50281e",
    "st_warm2": "#824024",
    "st_glow": "#c26230",

    # Wood, Siege Engines (7)
    "wd_darkest": "#0b0704",
    "wd_dark": "#160e08",
    "wd_mid": "#28180e",
    "wd_light": "#402616",
    "wd_pale": "#5e3a22",
    "wd_hi": "#845434",
    "wd_iron": "#222730",

    # Soldiers, Knights, Armor & Banners (10)
    "st_iron": "#0e1218",
    "st_armor": "#1e2632",
    "st_metal": "#344254",
    "st_plate": "#546682",
    "st_glint": "#869ab5",
    "st_white": "#d0deee",
    "b_dark": "#520c12",
    "b_red": "#94141a",
    "b_bright": "#cc2222",
    "b_gold": "#b58016",
    "b_yellow": "#f0bc26",

    # Battlefield Ground & Mud (8)
    "g_deep": "#090604",
    "g_shadow": "#110c08",
    "g_dark": "#1c140e",
    "g_mid": "#2c1e14",
    "g_light": "#422e1e",
    "g_rock": "#20222a",
    "g_rockhi": "#363a46",
    "g_ember": "#46160e",
}

class CanvasGrid:
    def __init__(self, w=256, h=256, bg="#0a0412"):
        self.w = w
        self.h = h
        self.grid = [[bg for _ in range(w)] for _ in range(h)]

    def set(self, x, y, col):
        if 0 <= x < self.w and 0 <= y < self.h and col is not None:
            self.grid[y][x] = col

    def get(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            return self.grid[y][x]
        return None

    def rect(self, x, y, w, h, col):
        for cy in range(y, y + h):
            if 0 <= cy < self.h:
                row = self.grid[cy]
                for cx in range(x, x + w):
                    if 0 <= cx < self.w:
                        row[cx] = col

    def line(self, x0, y0, x1, y1, col):
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            self.set(x0, y0, col)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def circle(self, cx, cy, r, col, fill=True):
        for y in range(-r, r + 1):
            for x in range(-r, r + 1):
                d2 = x * x + y * y
                if fill:
                    if d2 <= r * r + r:
                        self.set(cx + x, cy + y, col)
                else:
                    if r * r - r <= d2 <= r * r + r:
                        self.set(cx + x, cy + y, col)

    def poly(self, pts, col):
        if len(pts) < 3:
            return
        min_y = max(0, min(p[1] for p in pts))
        max_y = min(self.h - 1, max(p[1] for p in pts))
        n = len(pts)
        for y in range(min_y, max_y + 1):
            nodes = []
            for i in range(n):
                p1 = pts[i]
                p2 = pts[(i + 1) % n]
                if (p1[1] <= y < p2[1]) or (p2[1] <= y < p1[1]):
                    if p2[1] != p1[1]:
                        x_node = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                        nodes.append(x_node)
            nodes.sort()
            for i in range(0, len(nodes) - 1, 2):
                x_start = max(0, int(math.ceil(nodes[i])))
                x_end = min(self.w - 1, int(math.floor(nodes[i + 1])))
                for x in range(x_start, x_end + 1):
                    self.set(x, y, col)

def generate():
    g = CanvasGrid(W, H, PALETTE["sky_0"])

    # 1. Sunset Sky with 4x4 Bayer Dithering (Clean, pure sky gradient)
    BAYER4 = [
        [0/16,  8/16,  2/16, 10/16],
        [12/16, 4/16, 14/16,  6/16],
        [3/16, 11/16,  1/16,  9/16],
        [15/16, 7/16, 13/16,  5/16]
    ]

    bands = [
        (0, 14, "sky_0", "sky_1"),
        (14, 28, "sky_1", "sky_2"),
        (28, 44, "sky_2", "sky_3"),
        (44, 62, "sky_3", "sky_4"),
        (62, 78, "sky_4", "sky_5"),
        (78, 92, "sky_5", "sky_6"),
        (92, 104, "sky_6", "sky_7"),
        (104, 114, "sky_7", "sky_8"),
        (114, 124, "sky_8", "sky_9"),
        (124, 136, "sky_9", "sky_10"),
    ]

    for y0, y1, c1, c2 in bands:
        col1 = PALETTE[c1]
        col2 = PALETTE[c2]
        for y in range(y0, min(H, y1)):
            t = (y - y0) / max(1, (y1 - y0))
            for x in range(W):
                thresh = BAYER4[y % 4][x % 4]
                g.set(x, y, col2 if t > thresh else col1)

    # 2. Distant Mountains (y = 80 to 142)
    far_mtn_pts = [
        (0, 110), (22, 100), (42, 84), (65, 98), (88, 108),
        (112, 90), (130, 80), (150, 96), (172, 104), (198, 82),
        (220, 92), (240, 84), (255, 98), (255, 148), (0, 148)
    ]
    g.poly(far_mtn_pts, PALETTE["mtn_mid"])

    ridges = [
        ((42, 84), (22, 100)), ((42, 84), (65, 98)),
        ((130, 80), (112, 90)), ((130, 80), (150, 96)),
        ((198, 82), (172, 104)), ((198, 82), (220, 92)),
        ((240, 84), (220, 92)), ((240, 84), (255, 98))
    ]
    for p0, p1 in ridges:
        g.line(p0[0], p0[1], p1[0], p1[1], PALETTE["mtn_rim"])
        g.set(p0[0], p0[1], PALETTE["mtn_gold"])
        g.set(p0[0] - 1, p0[1] + 1, PALETTE["mtn_gold"])

    mid_mtn_pts = [
        (0, 124), (32, 114), (58, 102), (82, 116), (108, 124),
        (132, 112), (158, 100), (184, 114), (212, 120), (236, 108), (255, 116),
        (255, 155), (0, 155)
    ]
    g.poly(mid_mtn_pts, PALETTE["mtn_dark"])
    for i in range(len(mid_mtn_pts) - 3):
        p0 = mid_mtn_pts[i]
        p1 = mid_mtn_pts[i+1]
        g.line(p0[0], p0[1], p1[0], p1[1], PALETTE["mtn_light"])

    # 3. Ground & Castle Cliff (y = 135 to 256)
    # Castle rock crag on right (solid cliff base under castle, seamless connection)
    cliff_pts = [
        (86, 182), (100, 168), (120, 158), (140, 148), (170, 142),
        (200, 140), (230, 140), (255, 140), (255, 215), (92, 215)
    ]
    g.poly(cliff_pts, PALETTE["g_shadow"])

    # Battlefield earth
    ground_pts = [
        (0, 182), (45, 178), (95, 182), (145, 186), (195, 192), (255, 195),
        (255, 256), (0, 256)
    ]
    g.poly(ground_pts, PALETTE["g_dark"])

    # Mud ruts and soil texturing
    for y in range(208, 256):
        for x in range(W):
            if (x * 7 + y * 13) % 11 == 0:
                g.set(x, y, PALETTE["g_light"])
            elif (x * 3 + y * 5) % 17 == 0:
                g.set(x, y, PALETTE["g_deep"])

    # Rock ledges and fissures
    for cy in range(144, 202, 4):
        for cx in range(88 + (202 - cy) // 3, 252, 7):
            g.line(cx, cy, cx + 4, cy + 3, PALETTE["g_rock"])
            g.set(cx + 1, cy, PALETTE["g_rockhi"])
            if cx > 180:
                g.set(cx + 2, cy + 1, PALETTE["st_warm2"])

    # 4. Castle Architecture (x = 88 to 255, y = 92 to 184)
    # A. Left Curtain Wall & Ramparts (x: 88 to 134, y: 124 to 182)
    g.rect(88, 128, 46, 54, PALETTE["st_dark"])
    g.rect(86, 126, 48, 3, PALETTE["st_mid"])
    g.line(86, 126, 134, 126, PALETTE["st_light"])

    for mx in range(88, 132, 8):
        g.rect(mx, 120, 5, 7, PALETTE["st_mid"])
        g.rect(mx, 120, 5, 1, PALETTE["st_light"])
        g.rect(mx, 121, 1, 6, PALETTE["st_light"])
        g.rect(mx + 4, 121, 1, 6, PALETTE["st_shadow"])

    for row_y in range(132, 180, 4):
        g.line(88, row_y, 134, row_y, PALETTE["st_deep"])
        shift = (row_y // 4) % 2 * 4
        for bx in range(88 + shift, 134, 8):
            g.line(bx, row_y, bx, row_y + 3, PALETTE["st_deep"])
            g.set(bx + 1, row_y + 1, PALETTE["st_mid"])

    # B. Central Keep & Gatehouse (x: 134 to 184, y: 106 to 184)
    g.rect(134, 114, 50, 70, PALETTE["st_dark"])
    g.rect(132, 112, 54, 3, PALETTE["st_light"])
    for cx in range(134, 184, 6):
        g.rect(cx, 115, 3, 4, PALETTE["st_shadow"])
        g.set(cx + 1, 115, PALETTE["st_mid"])

    for mx in range(134, 184, 8):
        g.rect(mx, 106, 5, 7, PALETTE["st_mid"])
        g.rect(mx, 106, 5, 1, PALETTE["st_light"])
        g.rect(mx, 107, 1, 6, PALETTE["st_light"])
        g.rect(mx + 4, 107, 1, 6, PALETTE["st_shadow"])

    c_windows = [(146, 126), (168, 126), (157, 144)]
    for wx, wy in c_windows:
        g.rect(wx, wy, 6, 9, PALETTE["f_char"])
        g.rect(wx + 1, wy + 1, 4, 7, PALETTE["f_red"])
        g.rect(wx + 2, wy + 2, 2, 5, PALETTE["f_orange"])
        g.set(wx + 2, wy + 3, PALETTE["f_yellow"])
        g.line(wx, wy, wx + 5, wy, PALETTE["st_deep"])

    for row_y in range(120, 180, 4):
        g.line(134, row_y, 184, row_y, PALETTE["st_deep"])
        shift = (row_y // 4) % 2 * 5
        for bx in range(134 + shift, 184, 10):
            g.line(bx, row_y, bx, row_y + 3, PALETTE["st_deep"])
            g.set(bx + 1, row_y + 1, PALETTE["st_mid"])

    # Flagpole & Royal Banner on Keep
    g.line(156, 88, 156, 108, PALETTE["wd_dark"])
    g.set(156, 87, PALETTE["b_gold"])
    banner_pts = [(157, 89), (174, 92), (168, 98), (176, 104), (157, 102)]
    g.poly(banner_pts, PALETTE["b_red"])
    g.line(157, 89, 174, 92, PALETTE["b_gold"])
    g.line(157, 102, 176, 104, PALETTE["b_gold"])
    g.set(174, 92, PALETTE["f_orange"])
    g.set(175, 93, PALETTE["f_yellow"])
    g.set(176, 104, PALETTE["f_orange"])
    g.set(177, 103, PALETTE["f_yellow"])

    # C. East Tower - Struck by Dragon Fire (x: 184 to 244, y: 104 to 184)
    g.rect(184, 114, 60, 70, PALETTE["st_dark"])
    for ty in range(112, 180):
        g.set(184, ty, PALETTE["st_glow"])
        g.set(185, ty, PALETTE["st_warm2"])
        g.set(186, ty, PALETTE["st_warm1"])

    for row_y in range(118, 180, 4):
        g.line(184, row_y, 244, row_y, PALETTE["st_deep"])
        shift = (row_y // 4) % 2 * 5
        for bx in range(184 + shift, 244, 10):
            g.line(bx, row_y, bx, row_y + 3, PALETTE["st_deep"])
            if bx < 208:
                g.set(bx + 1, row_y + 1, PALETTE["st_warm2"])
            else:
                g.set(bx + 1, row_y + 1, PALETTE["st_mid"])

    e_windows = [(198, 124), (224, 124), (211, 142)]
    for wx, wy in e_windows:
        g.rect(wx, wy, 6, 10, PALETTE["f_char"])
        g.rect(wx + 1, wy + 1, 4, 8, PALETTE["f_red"])
        g.rect(wx + 2, wy + 2, 2, 6, PALETTE["f_orange"])
        g.rect(wx + 2, wy + 3, 2, 3, PALETTE["f_yellow"])
        g.set(wx + 2, wy + 4, PALETTE["f_white"])

    # Blasted shattered wall top
    g.poly([(184, 114), (194, 106), (202, 112), (212, 116), (220, 110), (232, 106), (244, 114), (244, 120), (184, 120)], PALETTE["st_mid"])
    debris = [
        (180, 96, 4, 3, "st_mid"), (188, 86, 3, 4, "st_dark"),
        (228, 80, 4, 3, "st_warm2"), (240, 90, 4, 4, "st_mid"),
        (248, 104, 3, 3, "st_shadow"), (202, 82, 4, 3, "st_light")
    ]
    for dx, dy, dw, dh, dcol in debris:
        g.rect(dx, dy, dw, dh, PALETTE[dcol])
        g.set(dx, dy, PALETTE["f_orange"])
        g.set(dx + dw - 1, dy, PALETTE["f_yellow"])

    # Tower Inferno
    flame_outer = [
        (190, 114), (196, 96), (202, 104), (210, 80), (218, 98),
        (224, 76), (232, 94), (238, 84), (242, 114)
    ]
    g.poly(flame_outer, PALETTE["f_red"])
    flame_mid = [
        (194, 114), (200, 100), (208, 86), (216, 100), (222, 82), (228, 98), (236, 114)
    ]
    g.poly(flame_mid, PALETTE["f_orange"])
    flame_core = [
        (198, 114), (204, 102), (210, 92), (216, 102), (220, 90), (225, 100), (230, 114)
    ]
    g.poly(flame_core, PALETTE["f_yellow"])
    g.rect(208, 98, 5, 10, PALETTE["f_white"])
    g.rect(218, 94, 4, 12, PALETTE["f_white"])

    # 5. Knights & Defenders on Ramparts
    # Spearman at x=98
    g.rect(98, 122, 3, 5, PALETTE["st_metal"])
    g.rect(97, 119, 5, 4, PALETTE["b_red"])
    g.rect(98, 116, 3, 3, PALETTE["st_plate"])
    g.set(98, 116, PALETTE["st_glint"])
    g.rect(96, 120, 2, 6, PALETTE["b_bright"])
    g.set(96, 122, PALETTE["b_gold"])
    g.line(99, 120, 106, 102, PALETTE["wd_mid"])
    g.set(106, 102, PALETTE["st_glint"])
    g.set(107, 101, PALETTE["st_white"])

    # Archer drawing bow at x=110
    g.rect(110, 122, 3, 5, PALETTE["st_armor"])
    g.rect(109, 119, 5, 4, PALETTE["b_red"])
    g.rect(110, 116, 3, 3, PALETTE["st_plate"])
    g.set(111, 116, PALETTE["st_glint"])
    g.line(108, 112, 107, 124, PALETTE["wd_light"])
    g.line(108, 112, 113, 118, PALETTE["st_glint"])
    g.line(107, 124, 113, 118, PALETTE["st_glint"])
    g.line(113, 118, 106, 110, PALETTE["wd_hi"])
    g.set(105, 109, PALETTE["st_white"])

    # Knight Captain at x=122
    g.rect(122, 122, 4, 5, PALETTE["st_metal"])
    g.rect(121, 119, 6, 4, PALETTE["st_plate"])
    g.set(122, 119, PALETTE["b_gold"])
    g.rect(122, 115, 4, 4, PALETTE["st_glint"])
    g.poly([(120, 119), (116, 123), (117, 128), (121, 124)], PALETTE["b_bright"])
    g.line(125, 119, 132, 108, PALETTE["st_white"])
    g.set(132, 108, PALETTE["st_glint"])
    g.set(125, 119, PALETTE["b_gold"])

    # Defenders on Central Keep
    g.rect(142, 108, 3, 5, PALETTE["st_metal"])
    g.rect(141, 105, 5, 4, PALETTE["b_red"])
    g.rect(142, 102, 3, 3, PALETTE["st_plate"])
    g.set(142, 102, PALETTE["st_glint"])
    g.line(143, 106, 148, 90, PALETTE["wd_mid"])
    g.set(148, 90, PALETTE["st_white"])

    g.rect(152, 108, 3, 5, PALETTE["st_armor"])
    g.rect(151, 105, 5, 4, PALETTE["b_red"])
    g.rect(152, 102, 3, 3, PALETTE["st_plate"])
    g.line(150, 100, 149, 110, PALETTE["wd_light"])
    g.line(149, 104, 144, 96, PALETTE["wd_hi"])
    g.set(143, 95, PALETTE["st_white"])

    g.rect(170, 108, 4, 5, PALETTE["st_metal"])
    g.rect(170, 103, 3, 4, PALETTE["st_plate"])
    g.line(168, 101, 174, 99, PALETTE["b_bright"])
    g.line(168, 102, 174, 100, PALETTE["b_gold"])

    g.rect(186, 109, 4, 4, PALETTE["st_armor"])
    g.rect(187, 106, 3, 3, PALETTE["st_plate"])
    g.line(189, 107, 194, 104, PALETTE["st_metal"])

    # 6. Wooden Siege Tower (x = 16 to 68, y = 110 to 214)
    tower_pts = [(24, 112), (60, 112), (66, 204), (18, 204)]
    g.poly(tower_pts, PALETTE["wd_dark"])

    for dy in [112, 134, 158, 182, 202]:
        f = (dy - 112) / (202 - 112)
        xl = int(24 - f * 6)
        xr = int(60 + f * 6)
        g.rect(xl - 1, dy, (xr - xl) + 2, 4, PALETTE["wd_mid"])
        g.line(xl, dy, xr, dy, PALETTE["wd_hi"])

    g.line(24, 112, 18, 204, PALETTE["wd_light"])
    g.line(25, 112, 19, 204, PALETTE["wd_mid"])
    g.line(60, 112, 66, 204, PALETTE["wd_mid"])
    g.line(59, 112, 65, 204, PALETTE["wd_light"])
    g.line(42, 112, 42, 204, PALETTE["wd_light"])

    for yt, yb in [(134, 158), (158, 182), (182, 202)]:
        ft, fb = (yt - 112) / 90.0, (yb - 112) / 90.0
        xlt, xrt = int(24 - ft * 6), int(60 + ft * 6)
        xlb, xrb = int(24 - fb * 6), int(60 + fb * 6)
        g.line(xlt + 2, yt + 4, 41, yb, PALETTE["wd_mid"])
        g.line(xlb + 2, yb, 41, yt + 4, PALETTE["wd_mid"])
        g.line(43, yt + 4, xrb - 2, yb, PALETTE["wd_mid"])
        g.line(43, yb, xrt - 2, yt + 4, PALETTE["wd_mid"])

    for wx in range(22, 60, 7):
        g.rect(wx, 108, 5, 6, PALETTE["wd_light"])
        g.line(wx, 108, wx + 4, 108, PALETTE["wd_hi"])
        g.set(wx + 2, 111, PALETTE["wd_iron"])

    bridge_pts = [(52, 118), (88, 126), (88, 130), (52, 122)]
    g.poly(bridge_pts, PALETTE["wd_pale"])
    g.line(52, 118, 88, 126, PALETTE["wd_hi"])
    g.line(56, 110, 86, 126, PALETTE["wd_iron"])
    g.line(56, 111, 86, 127, PALETTE["st_metal"])

    g.rect(28, 103, 3, 5, PALETTE["st_armor"])
    g.rect(28, 100, 3, 3, PALETTE["st_plate"])
    g.line(26, 98, 25, 106, PALETTE["wd_hi"])
    g.line(25, 102, 33, 96, PALETTE["wd_light"])
    g.set(34, 95, PALETTE["st_white"])

    g.rect(48, 113, 3, 5, PALETTE["st_metal"])
    g.rect(48, 110, 3, 3, PALETTE["st_plate"])
    g.line(48, 112, 58, 108, PALETTE["wd_mid"])
    g.set(58, 108, PALETTE["st_glint"])
    g.set(59, 107, PALETTE["st_white"])
    g.circle(46, 114, 2, PALETTE["b_bright"])
    g.set(46, 114, PALETTE["b_gold"])

    g.rect(34, 140, 11, 18, PALETTE["b_dark"])
    g.rect(35, 141, 9, 16, PALETTE["b_red"])
    g.line(38, 146, 42, 152, PALETTE["b_yellow"])
    g.line(38, 152, 42, 146, PALETTE["b_yellow"])
    g.set(34, 158, PALETTE["wd_dark"])
    g.set(39, 156, PALETTE["wd_dark"])
    g.set(44, 158, PALETTE["wd_dark"])

    g.rect(14, 198, 56, 6, PALETTE["wd_darkest"])
    wheels = [(22, 206), (36, 206), (48, 206), (62, 206)]
    for wx, wy in wheels:
        g.circle(wx, wy, 6, PALETTE["wd_iron"], fill=True)
        g.circle(wx, wy, 4, PALETTE["wd_mid"], fill=True)
        g.circle(wx, wy, 2, PALETTE["wd_iron"], fill=True)
        g.set(wx, wy, PALETTE["st_glint"])

    # Trebuchet
    g.line(74, 212, 84, 192, PALETTE["wd_light"])
    g.line(94, 212, 84, 192, PALETTE["wd_light"])
    g.line(72, 212, 96, 212, PALETTE["wd_mid"])
    g.rect(76, 198, 7, 10, PALETTE["wd_darkest"])
    g.rect(77, 199, 5, 8, PALETTE["wd_mid"])
    g.line(78, 204, 91, 168, PALETTE["wd_pale"])
    g.line(79, 204, 92, 168, PALETTE["wd_light"])
    g.circle(84, 192, 2, PALETTE["wd_iron"])
    g.set(84, 192, PALETTE["st_plate"])

    g.circle(96, 156, 3, PALETTE["f_red"])
    g.circle(96, 156, 2, PALETTE["f_orange"])
    g.set(96, 156, PALETTE["f_yellow"])
    g.set(94, 159, PALETTE["f_orange"])
    g.set(92, 163, PALETTE["f_yellow"])
    g.set(90, 167, PALETTE["f_crimson"])

    # 7. Battlefield & Armies in Formation (y = 195 to 254)
    for ry in [198, 204, 210]:
        x_off = (ry // 6) % 2 * 4
        for sx in range(22 + x_off, 118, 6):
            g.rect(sx, ry, 3, 2, PALETTE["st_plate"])
            g.set(sx + 1, ry, PALETTE["st_glint"])
            g.rect(sx, ry + 2, 3, 3, PALETTE["st_armor"])
            g.line(sx + 1, ry + 1, sx + 11, ry - 14, PALETTE["wd_mid"])
            g.set(sx + 11, ry - 14, PALETTE["st_glint"])
            g.set(sx + 12, ry - 15, PALETTE["st_white"])

    flag_poles = [(52, 168, 208), (98, 172, 212)]
    for fx, fyt, fyb in flag_poles:
        g.line(fx, fyt, fx, fyb, PALETTE["wd_mid"])
        g.set(fx, fyt - 1, PALETTE["b_gold"])
        b_pts = [(fx + 1, fyt + 2), (fx + 16, fyt + 5), (fx + 12, fyt + 10), (fx + 17, fyt + 15), (fx + 1, fyt + 14)]
        g.poly(b_pts, PALETTE["b_red"])
        g.line(fx + 1, fyt + 2, fx + 16, fyt + 5, PALETTE["b_yellow"])
        g.line(fx + 1, fyt + 14, fx + 17, fyt + 15, PALETTE["b_yellow"])
        g.rect(fx + 4, fyt + 6, 4, 4, PALETTE["b_gold"])
        g.set(fx + 5, fyt + 7, PALETTE["b_yellow"])

    # Shield Wall
    for sx in range(20, 120, 5):
        g.rect(sx + 1, 214, 3, 3, PALETTE["st_plate"])
        g.set(sx + 2, 214, PALETTE["st_glint"])
        g.line(sx + 1, 216, sx + 3, 216, PALETTE["st_armor"])
        g.rect(sx, 217, 5, 11, PALETTE["b_red"])
        g.rect(sx + 1, 217, 3, 11, PALETTE["b_bright"])
        g.line(sx, 217, sx, 227, PALETTE["b_dark"])
        g.line(sx + 4, 217, sx + 4, 227, PALETTE["b_dark"])
        g.set(sx + 2, 220, PALETTE["b_gold"])
        g.set(sx + 2, 221, PALETTE["b_gold"])
        g.set(sx + 1, 220, PALETTE["b_gold"])
        g.set(sx + 3, 220, PALETTE["b_gold"])
        g.line(sx + 3, 218, sx + 12, 208, PALETTE["wd_hi"])
        g.set(sx + 12, 208, PALETTE["st_white"])

    # Mounted Commander
    horse_pts = [
        (128, 224), (134, 218), (144, 218), (150, 222), (147, 232), (130, 232)
    ]
    g.poly(horse_pts, PALETTE["b_dark"])
    g.rect(130, 222, 17, 8, PALETTE["b_red"])
    g.line(129, 230, 148, 230, PALETTE["b_gold"])

    g.line(144, 220, 151, 211, PALETTE["b_red"])
    g.line(145, 220, 152, 211, PALETTE["b_red"])
    g.rect(150, 210, 4, 5, PALETTE["st_metal"])
    g.set(152, 209, PALETTE["st_glint"])
    g.set(153, 212, PALETTE["st_white"])

    g.line(131, 232, 129, 242, PALETTE["g_shadow"])
    g.line(135, 232, 137, 242, PALETTE["g_shadow"])
    g.line(143, 232, 145, 242, PALETTE["g_shadow"])
    g.line(147, 232, 152, 240, PALETTE["g_shadow"])

    g.rect(135, 213, 5, 6, PALETTE["st_plate"])
    g.rect(135, 207, 4, 6, PALETTE["st_glint"])
    g.set(136, 206, PALETTE["b_gold"])
    g.set(137, 205, PALETTE["b_gold"])
    g.line(138, 211, 148, 196, PALETTE["st_white"])
    g.line(139, 211, 149, 196, PALETTE["st_glint"])
    g.set(138, 212, PALETTE["b_gold"])

    # Advancing soldiers behind general
    for ax in [156, 164, 172]:
        g.rect(ax, 220, 3, 3, PALETTE["st_plate"])
        g.set(ax + 1, 220, PALETTE["st_glint"])
        g.rect(ax, 223, 3, 6, PALETTE["b_red"])
        g.line(ax + 1, 222, ax + 7, 214, PALETTE["wd_hi"])
        g.set(ax + 7, 214, PALETTE["st_white"])

    # Barricades
    stakes = [(18, 246, -1), (28, 244, -1), (72, 248, -1), (82, 246, -1), (110, 248, 1), (170, 246, 1), (180, 248, 1)]
    for stx, sty, sdir in stakes:
        g.line(stx, sty, stx + sdir * 6, sty - 10, PALETTE["wd_dark"])
        g.line(stx + 1, sty, stx + sdir * 6 + 1, sty - 10, PALETTE["wd_light"])
        g.set(stx + sdir * 6, sty - 10, PALETTE["wd_hi"])

    # Brazier
    g.line(160, 248, 162, 244, PALETTE["wd_iron"])
    g.line(164, 248, 162, 244, PALETTE["wd_iron"])
    g.rect(160, 242, 5, 3, PALETTE["wd_iron"])
    g.set(161, 241, PALETTE["f_red"])
    g.set(162, 240, PALETTE["f_yellow"])
    g.set(163, 241, PALETTE["f_orange"])
    g.line(156, 249, 168, 249, PALETTE["g_ember"])

    g.circle(104, 248, 4, PALETTE["b_red"])
    g.set(104, 248, PALETTE["b_gold"])
    g.line(98, 252, 112, 244, PALETTE["wd_mid"])

    # 8. THE ANCIENT DRAGON WITH CRISP DARK OUTLINE
    # A. Left Wing (x: 42 to 125, y: 8 to 58)
    w_pts1 = [(66, 12), (52, 14), (36, 18), (40, 26), (44, 34)]
    g.poly(w_pts1, PALETTE["drg_w2"])
    w_pts2 = [(66, 12), (44, 34), (52, 40), (62, 46)]
    g.poly(w_pts2, PALETTE["drg_w1"])
    w_pts3 = [(66, 12), (62, 46), (72, 50), (84, 52), (98, 46), (112, 36)]
    g.poly(w_pts3, PALETTE["drg_w2"])

    g.line(66, 12, 42, 30, PALETTE["drg_w3"])
    g.line(66, 12, 58, 42, PALETTE["drg_w3"])
    g.line(66, 12, 78, 48, PALETTE["drg_w3"])

    # Scalloped rim glow
    for p0, p1 in [((36, 18), (40, 26)), ((40, 26), (44, 34)), ((44, 34), (52, 40)), ((52, 40), (62, 46)), ((62, 46), (72, 50)), ((72, 50), (84, 52))]:
        g.line(p0[0], p0[1], p1[0], p1[1], PALETTE["drg_w4"])

    # Dark outlines on wing top and scallops
    g.line(66, 11, 36, 17, PALETTE["drg_out"])
    g.line(66, 11, 112, 35, PALETTE["drg_out"])

    # Wing arm bones & struts
    g.line(112, 36, 88, 22, PALETTE["drg_s2"])
    g.line(112, 37, 88, 23, PALETTE["drg_s3"])
    g.line(88, 22, 66, 12, PALETTE["drg_s4"])
    g.line(88, 23, 66, 13, PALETTE["drg_s5"])
    g.line(66, 12, 64, 9, PALETTE["drg_horn2"])
    g.set(63, 8, PALETTE["st_white"])

    g.line(66, 12, 36, 18, PALETTE["drg_s4"])
    g.line(66, 12, 44, 34, PALETTE["drg_s4"])
    g.line(66, 12, 62, 46, PALETTE["drg_s4"])
    g.line(66, 12, 84, 52, PALETTE["drg_s4"])
    for fx, fy in [(36, 18), (44, 34), (62, 46), (84, 52)]:
        g.set(fx, fy, PALETTE["st_white"])

    # B. Right Wing (far wing banking right, x: 130 to 205, y: 8 to 52)
    rw_pts1 = [(128, 34), (162, 10), (180, 14), (202, 20), (194, 30), (188, 38)]
    g.poly(rw_pts1, PALETTE["drg_w2"])
    rw_pts2 = [(128, 34), (188, 38), (180, 44), (170, 48), (145, 42)]
    g.poly(rw_pts2, PALETTE["drg_w1"])

    g.line(202, 20, 188, 38, PALETTE["f_orange"])
    g.line(188, 38, 170, 48, PALETTE["f_red"])
    g.line(162, 9, 202, 19, PALETTE["drg_out"])

    g.line(128, 34, 162, 10, PALETTE["drg_s4"])
    g.line(162, 10, 202, 20, PALETTE["drg_s5"])
    g.line(162, 10, 188, 38, PALETTE["drg_s5"])
    g.line(162, 10, 170, 48, PALETTE["drg_s5"])
    g.set(162, 9, PALETTE["st_white"])

    # C. Dragon Body & Torso (x: 104 to 138, y: 32 to 58)
    torso_pts = [
        (106, 40), (114, 34), (128, 32), (138, 38),
        (136, 50), (126, 56), (114, 54), (104, 48)
    ]
    g.poly(torso_pts, PALETTE["drg_s2"])
    belly = [(114, 54), (126, 56), (136, 50), (132, 46), (122, 50), (112, 48)]
    g.poly(belly, PALETTE["drg_b2"])
    g.line(114, 54, 126, 56, PALETTE["drg_b4"])
    g.line(126, 56, 136, 50, PALETTE["drg_b3"])

    g.circle(120, 42, 3, PALETTE["drg_s4"])
    g.set(120, 41, PALETTE["drg_s5"])
    g.set(121, 40, PALETTE["drg_s6"])

    # D. Sinuous Arching Neck (x: 124 to 166, y: 28 to 56)
    neck = [
        (126, 36), (136, 30), (148, 32), (160, 40), (166, 48),
        (158, 52), (148, 46), (138, 42), (130, 40)
    ]
    g.poly(neck, PALETTE["drg_s3"])
    g.line(126, 36, 136, 30, PALETTE["drg_s5"])
    g.line(136, 30, 148, 32, PALETTE["drg_s5"])
    g.line(148, 32, 160, 40, PALETTE["drg_s4"])

    g.line(126, 35, 136, 29, PALETTE["drg_out"])
    g.line(136, 29, 148, 31, PALETTE["drg_out"])
    g.line(148, 31, 160, 39, PALETTE["drg_out"])

    neck_spines = [(132, 31), (138, 28), (144, 29), (152, 34), (158, 38)]
    for spx, spy in neck_spines:
        g.line(spx, spy, spx - 2, spy - 4, PALETTE["drg_horn2"])
        g.set(spx - 2, spy - 4, PALETTE["st_white"])

    g.line(130, 40, 138, 42, PALETTE["drg_b3"])
    g.line(138, 42, 148, 46, PALETTE["drg_b4"])
    g.line(148, 46, 158, 52, PALETTE["f_orange"])

    # E. Dragon Head & Jaws (x: 160 to 186, y: 42 to 62)
    head_pts = [
        (160, 44), (170, 42), (180, 48), (186, 52), (182, 56), (174, 54), (164, 50)
    ]
    g.poly(head_pts, PALETTE["drg_s4"])
    g.line(160, 44, 170, 42, PALETTE["drg_s5"])
    g.line(170, 42, 180, 48, PALETTE["drg_s6"])

    g.line(160, 43, 170, 41, PALETTE["drg_out"])
    g.line(170, 41, 180, 47, PALETTE["drg_out"])
    g.line(180, 47, 186, 51, PALETTE["drg_out"])

    # Horns
    g.line(164, 44, 156, 34, PALETTE["drg_horn1"])
    g.line(156, 34, 148, 28, PALETTE["drg_horn2"])
    g.set(147, 27, PALETTE["st_white"])

    g.line(162, 48, 153, 40, PALETTE["drg_horn1"])
    g.line(153, 40, 145, 36, PALETTE["drg_horn2"])
    g.set(144, 35, PALETTE["st_white"])

    # Glowing Eye
    g.line(170, 46, 175, 46, PALETTE["drg_out"])
    g.rect(171, 47, 3, 2, PALETTE["f_yellow"])
    g.set(172, 47, PALETTE["f_white"])
    g.set(171, 48, PALETTE["f_orange"])

    # Fangs
    g.line(174, 54, 184, 54, PALETTE["drg_out"])
    g.set(176, 55, PALETTE["f_white"])
    g.set(180, 55, PALETTE["f_white"])

    # Lower Jaw
    jaw = [(166, 54), (174, 62), (182, 60), (174, 55)]
    g.poly(jaw, PALETTE["drg_s3"])
    g.line(174, 62, 182, 60, PALETTE["drg_s5"])
    g.line(166, 54, 174, 63, PALETTE["drg_out"])
    g.set(176, 59, PALETTE["f_white"])
    g.set(180, 58, PALETTE["f_white"])

    g.rect(170, 53, 5, 4, PALETTE["f_yellow"])
    g.set(172, 54, PALETTE["f_white"])

    # F. THE DRAGON BREATH TORRENT
    br_outer = [
        (180, 55), (188, 56), (220, 94), (226, 106), (206, 104), (180, 61)
    ]
    g.poly(br_outer, PALETTE["f_red"])

    br_mid = [
        (181, 56), (189, 58), (218, 96), (222, 104), (208, 102), (181, 60)
    ]
    g.poly(br_mid, PALETTE["f_orange"])

    br_core = [
        (182, 57), (188, 59), (215, 96), (218, 102), (210, 100), (182, 59)
    ]
    g.poly(br_core, PALETTE["f_yellow"])

    g.line(182, 58, 214, 100, PALETTE["f_white"])
    g.line(183, 58, 215, 100, PALETTE["f_white"])
    g.line(182, 59, 214, 101, PALETTE["f_pale"])

    g.line(190, 64, 196, 62, PALETTE["f_yellow"])
    g.line(198, 74, 206, 71, PALETTE["f_orange"])
    g.line(204, 82, 212, 79, PALETTE["f_red"])
    g.line(188, 68, 194, 72, PALETTE["f_orange"])
    g.line(196, 80, 202, 86, PALETTE["f_red"])

    # G. Hind Leg & Talons
    thigh = [(108, 48), (116, 52), (112, 60), (104, 56)]
    g.poly(thigh, PALETTE["drg_s2"])
    g.line(106, 56, 102, 64, PALETTE["drg_s3"])
    g.line(102, 64, 98, 66, PALETTE["st_plate"])
    g.line(102, 64, 101, 68, PALETTE["st_plate"])
    g.line(102, 64, 105, 67, PALETTE["st_plate"])
    g.set(97, 66, PALETTE["st_white"])
    g.set(101, 69, PALETTE["st_white"])

    # H. Long Serpentine Tail (x: 42 to 106, y: 44 to 72)
    tail_pts = [
        (106, 48), (94, 54), (80, 56), (68, 54), (56, 58), (48, 64),
        (49, 68), (60, 62), (72, 58), (84, 60), (96, 58), (106, 52)
    ]
    g.poly(tail_pts, PALETTE["drg_s2"])
    g.line(106, 48, 48, 64, PALETTE["drg_s3"])
    g.line(106, 47, 48, 63, PALETTE["drg_out"])
    g.line(106, 53, 49, 69, PALETTE["drg_out"])

    tail_spines = [(98, 51), (88, 54), (76, 55), (66, 54), (56, 57)]
    for tx, ty in tail_spines:
        g.line(tx, ty, tx - 1, ty - 3, PALETTE["drg_horn2"])
        g.set(tx - 1, ty - 3, PALETTE["st_white"])
    tip = [(48, 64), (42, 62), (40, 66), (42, 70), (48, 68)]
    g.poly(tip, PALETTE["drg_s5"])
    g.set(39, 66, PALETTE["st_white"])

    # 9. Natural Volumetric Smoke Rising from East Tower (away from dragon)
    tower_smoke = [
        (228, 65, 14, "smk_dark"),
        (242, 52, 16, "smk_black"),
        (234, 40, 18, "smk_dark"),
        (248, 28, 16, "smk_black"),
        (218, 56, 10, "smk_warm"),
        (224, 68, 8, "smk_fire"),
    ]
    for smx, smy, smr, smcol in tower_smoke:
        for sy in range(-smr, smr + 1):
            for sx in range(-smr, smr + 1):
                d2 = sx * sx + sy * sy
                if d2 <= smr * smr:
                    px, py = smx + sx, smy + sy
                    if 0 <= px < W and 0 <= py < H:
                        cur = g.get(px, py)
                        if cur not in [PALETTE["drg_s5"], PALETTE["drg_s6"], PALETTE["f_white"], PALETTE["f_yellow"], PALETTE["f_orange"]]:
                            if d2 > (smr - 2) * (smr - 2):
                                if (px + py) % 2 == 0:
                                    g.set(px, py, PALETTE[smcol])
                            else:
                                g.set(px, py, PALETTE[smcol])

    # 10. Flying Arrows in Ballistic Arcs
    arrows = [
        (116, 108, 4, -3, False),
        (128, 102, 5, -2, False),
        (158, 92, 4, -4, False),
        (148, 86, 3, -5, True),
        (138, 78, 3, -4, False),
        (38, 92, 5, -3, False),
        (54, 82, 5, -3, True),
        (72, 104, 4, -4, False),
        (88, 112, 5, -3, False),
        (104, 126, 4, -3, True),
        (68, 140, 4, -3, False),
        (82, 152, 4, -4, False),
        (132, 160, 4, -3, True),
        (146, 150, 4, -3, False),
    ]
    for ax, ay, adx, ady, is_fire in arrows:
        g.line(ax, ay, ax + adx, ay + ady, PALETTE["wd_hi"])
        tip_x, tip_y = ax + adx, ay + ady
        g.set(tip_x, tip_y, PALETTE["st_white"])
        g.set(ax, ay, PALETTE["b_bright"])
        if is_fire:
            g.set(tip_x, tip_y, PALETTE["f_yellow"])
            g.set(tip_x + 1, tip_y, PALETTE["f_orange"])
            g.set(ax - 1, ay + 1, PALETTE["smk_mid"])

    stuck_arrows = [
        (48, 146, -3, -2), (56, 168, -4, -1), (112, 144, 3, -2), (124, 152, 4, -3)
    ]
    for sx, sy, sdx, sdy in stuck_arrows:
        g.line(sx, sy, sx + sdx, sy + sdy, PALETTE["wd_mid"])
        g.set(sx + sdx, sy + sdy, PALETTE["b_red"])

    # 11. Swirling Glowing Embers
    rng = random.Random(42)
    for _ in range(95):
        ex = rng.randint(35, 250)
        ey = rng.randint(12, 165)
        cur = g.get(ex, ey)
        if cur not in [PALETTE["f_white"]]:
            ecol = rng.choice(["f_white", "f_yellow", "f_orange", "f_pale"])
            g.set(ex, ey, PALETTE[ecol])
            if rng.random() < 0.25:
                g.set(ex + 1, ey, PALETTE["f_red"])

    return g
