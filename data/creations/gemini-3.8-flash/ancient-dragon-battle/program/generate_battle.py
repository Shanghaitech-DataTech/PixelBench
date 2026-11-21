import math
import random

W, H = 256, 256

PALETTE = {
    # Sunset Sky Gradient (12)
    "sky_0": "#0b0512",
    "sky_1": "#180a22",
    "sky_2": "#2d0e34",
    "sky_3": "#48123e",
    "sky_4": "#6e183e",
    "sky_5": "#992134",
    "sky_6": "#c43424",
    "sky_7": "#e4541e",
    "sky_8": "#f77d21",
    "sky_9": "#fcaa32",
    "sky_10": "#fde05b",
    "sky_11": "#fff59d",

    # Mountains & Horizon (5)
    "mtn_dark": "#130a1b",
    "mtn_mid": "#22132c",
    "mtn_light": "#3b1e42",
    "mtn_rim": "#8f3342",
    "mtn_gold": "#cf532e",

    # Smoke & Billows (7)
    "smk_black": "#0e0b12",
    "smk_dark": "#1a1420",
    "smk_mid": "#2e2434",
    "smk_light": "#483a4e",
    "smk_pale": "#6b586e",
    "smk_warm": "#914c38",
    "smk_fire": "#cf6836",

    # Dragon (17)
    "drg_out": "#080509",
    "drg_dark": "#140b15",
    "drg_s1": "#240e1b",
    "drg_s2": "#3b1222",
    "drg_s3": "#5e1627",
    "drg_s4": "#861c28",
    "drg_s5": "#b32729",
    "drg_s6": "#d9422a",
    "drg_b1": "#2c100e",
    "drg_b2": "#521a14",
    "drg_b3": "#852e1b",
    "drg_b4": "#bd4c22",
    "drg_w1": "#1c0b16",
    "drg_w2": "#331220",
    "drg_w3": "#521a28",
    "drg_w4": "#80272c",
    "drg_horn1": "#1c212a",
    "drg_horn2": "#414b5c",
    "drg_horn3": "#7e8b9e",

    # Fire & Explosions (8)
    "f_white": "#ffffff",
    "f_pale": "#fff7a4",
    "f_yellow": "#fed233",
    "f_orange": "#fa821c",
    "f_red": "#e03b18",
    "f_crimson": "#a61919",
    "f_dark": "#5a0c14",
    "f_char": "#21050a",

    # Castle Stone & Masonry (10)
    "st_deep": "#0b0d13",
    "st_shadow": "#131720",
    "st_dark": "#1d232e",
    "st_mid": "#2c3444",
    "st_light": "#424d62",
    "st_pale": "#5f6c86",
    "st_hi": "#8291ad",
    "st_warm1": "#542c22",
    "st_warm2": "#8a452a",
    "st_glow": "#c76734",

    # Wood, Siege Engines (7)
    "wd_darkest": "#0c0805",
    "wd_dark": "#181009",
    "wd_mid": "#2b1a10",
    "wd_light": "#442b1a",
    "wd_pale": "#633f27",
    "wd_hi": "#8a5c3a",
    "wd_iron": "#252b36",

    # Soldiers, Knights, Armor & Banners (10)
    "st_iron": "#10141b",
    "st_armor": "#212a38",
    "st_metal": "#38475c",
    "st_plate": "#5a6e8c",
    "st_glint": "#8ea3bf",
    "st_white": "#d4e2f2",
    "b_dark": "#5a0e14",
    "b_red": "#9c161d",
    "b_bright": "#d42525",
    "b_gold": "#bd881a",
    "b_yellow": "#f5c32c",

    # Ground & Mud (8)
    "g_deep": "#0a0705",
    "g_shadow": "#130e0a",
    "g_dark": "#1f1610",
    "g_mid": "#302218",
    "g_light": "#473323",
    "g_rock": "#242730",
    "g_rockhi": "#3c404e",
    "g_ember": "#4c1a11",
}

class PixelGrid:
    def __init__(self, w=256, h=256, default_color=None):
        self.w = w
        self.h = h
        self.grid = [[default_color for _ in range(w)] for _ in range(h)]

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
                dist2 = x * x + y * y
                if fill:
                    if dist2 <= r * r + r:
                        self.set(cx + x, cy + y, col)
                else:
                    if r * r - r <= dist2 <= r * r + r:
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

def render_scene():
    g = PixelGrid(W, H, PALETTE["sky_0"])

    # 1. Sky & Sunset Gradient with 4x4 Bayer Dithering
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
        (124, 134, "sky_9", "sky_10"),
        (134, 148, "sky_10", "sky_11"),
    ]

    for y0, y1, c1_k, c2_k in bands:
        col1 = PALETTE[c1_k]
        col2 = PALETTE[c2_k]
        for y in range(y0, min(H, y1)):
            t = (y - y0) / max(1, (y1 - y0))
            for x in range(W):
                thresh = BAYER4[y % 4][x % 4]
                g.set(x, y, col2 if t > thresh else col1)

    # Distant wispy sunset clouds
    cloud_layers = [
        (10, 48, 65, 3, "sky_3", "sky_8"),
        (135, 54, 85, 4, "sky_4", "sky_9"),
        (45, 68, 75, 3, "sky_5", "sky_10"),
        (165, 72, 70, 3, "sky_6", "sky_10"),
    ]
    for cx, cy, cw, ch, c_top, c_bot in cloud_layers:
        for y in range(cy, cy + ch):
            col = PALETTE[c_bot] if y == cy + ch - 1 else PALETTE[c_top]
            x0 = cx + (y - cy) * 2
            x1 = cx + cw - (y - cy) * 2
            for x in range(x0, x1):
                if (x + y) % 2 == 0 or y == cy + ch - 1:
                    g.set(x, y, col)

    # 2. Distant Mountains (y = 80 to 142)
    # Far craggy peaks
    far_mtn_pts = [
        (0, 112), (22, 102), (42, 86), (65, 100), (88, 110),
        (112, 92), (130, 82), (150, 98), (172, 106), (198, 84),
        (220, 94), (240, 86), (255, 100), (255, 148), (0, 148)
    ]
    g.poly(far_mtn_pts, PALETTE["mtn_mid"])

    # Ridge highlights on western slopes
    ridges = [
        ((42, 86), (22, 102)),
        ((42, 86), (65, 100)),
        ((130, 82), (112, 92)),
        ((130, 82), (150, 98)),
        ((198, 84), (172, 106)),
        ((198, 84), (220, 94)),
        ((240, 86), (220, 94)),
        ((240, 86), (255, 100)),
    ]
    for p0, p1 in ridges:
        g.line(p0[0], p0[1], p1[0], p1[1], PALETTE["mtn_rim"])
        g.set(p0[0], p0[1], PALETTE["mtn_gold"])
        g.set(p0[0] - 1, p0[1] + 1, PALETTE["mtn_gold"])

    # Mid mountain range (closer dark silhouette)
    mid_mtn_pts = [
        (0, 126), (32, 116), (58, 104), (82, 118), (108, 126),
        (132, 114), (158, 102), (184, 116), (212, 122), (236, 110), (255, 118),
        (255, 155), (0, 155)
    ]
    g.poly(mid_mtn_pts, PALETTE["mtn_dark"])
    for i in range(len(mid_mtn_pts) - 3):
        p0 = mid_mtn_pts[i]
        p1 = mid_mtn_pts[i+1]
        g.line(p0[0], p0[1], p1[0], p1[1], PALETTE["mtn_light"])

    # 3. Ground & Castle Cliff (y = 135 to 256)
    # Castle rock crag on right (x: 88 to 255, y: 135 to 215)
    cliff_pts = [
        (88, 185), (102, 164), (118, 152), (138, 142), (168, 138),
        (198, 136), (228, 136), (255, 136), (255, 215), (96, 215)
    ]
    g.poly(cliff_pts, PALETTE["g_shadow"])

    # Main battlefield terrain (y: 175 to 256)
    ground_pts = [
        (0, 182), (45, 178), (95, 182), (145, 186), (195, 192), (255, 195),
        (255, 256), (0, 256)
    ]
    g.poly(ground_pts, PALETTE["g_dark"])

    # Detailed ground mud, ruts, rock texture
    for y in range(208, 256):
        col = PALETTE["g_mid"] if y < 232 else PALETTE["g_shadow"]
        for x in range(W):
            if (x * 7 + y * 13) % 11 == 0:
                g.set(x, y, PALETTE["g_light"])
            elif (x * 3 + y * 5) % 17 == 0:
                g.set(x, y, PALETTE["g_deep"])

    # Cliff rock fissures and warm firelit rock ledges
    for cy in range(144, 200, 4):
        for cx in range(88 + (200 - cy) // 3, 252, 7):
            g.line(cx, cy, cx + 4, cy + 3, PALETTE["g_rock"])
            g.set(cx + 1, cy, PALETTE["g_rockhi"])
            if cx > 180: # firelight from tower above
                g.set(cx + 2, cy + 1, PALETTE["st_warm2"])

    # 4. Castle Stonework & Ramparts (x = 88 to 255, y = 92 to 185)
    # A. Left Curtain Wall & Ramparts (x: 88 to 134, y: 124 to 175)
    g.rect(88, 128, 46, 48, PALETTE["st_dark"])
    # Rampart corbel strip
    g.rect(86, 126, 48, 3, PALETTE["st_mid"])
    g.line(86, 126, 134, 126, PALETTE["st_light"])

    # Merlons / battlements on curtain wall
    for mx in range(88, 132, 8):
        g.rect(mx, 120, 5, 7, PALETTE["st_mid"])
        g.rect(mx, 120, 5, 1, PALETTE["st_light"])
        g.rect(mx, 121, 1, 6, PALETTE["st_light"])
        g.rect(mx + 4, 121, 1, 6, PALETTE["st_shadow"])

    # Masonry courses
    for row_y in range(132, 172, 4):
        g.line(88, row_y, 134, row_y, PALETTE["st_deep"])
        shift = (row_y // 4) % 2 * 4
        for bx in range(88 + shift, 134, 8):
            g.line(bx, row_y, bx, row_y + 3, PALETTE["st_deep"])
            g.set(bx + 1, row_y + 1, PALETTE["st_mid"])

    # B. Central Keep & Gatehouse (x: 134 to 184, y: 106 to 175)
    g.rect(134, 114, 50, 62, PALETTE["st_dark"])
    # Machicolations
    g.rect(132, 112, 54, 3, PALETTE["st_light"])
    for cx in range(134, 184, 6):
        g.rect(cx, 115, 3, 4, PALETTE["st_shadow"])
        g.set(cx + 1, 115, PALETTE["st_mid"])

    # Merlons on Central Keep
    for mx in range(134, 184, 8):
        g.rect(mx, 106, 5, 7, PALETTE["st_mid"])
        g.rect(mx, 106, 5, 1, PALETTE["st_light"])
        g.rect(mx, 107, 1, 6, PALETTE["st_light"])
        g.rect(mx + 4, 107, 1, 6, PALETTE["st_shadow"])

    # Central Keep arched windows blazing with internal fire
    c_windows = [(146, 126), (168, 126), (157, 144)]
    for wx, wy in c_windows:
        g.rect(wx, wy, 6, 9, PALETTE["f_char"])
        g.rect(wx + 1, wy + 1, 4, 7, PALETTE["f_red"])
        g.rect(wx + 2, wy + 2, 2, 5, PALETTE["f_orange"])
        g.set(wx + 2, wy + 3, PALETTE["f_yellow"])
        g.line(wx, wy, wx + 5, wy, PALETTE["st_deep"]) # arch top

    # Brick courses on keep
    for row_y in range(120, 172, 4):
        g.line(134, row_y, 184, row_y, PALETTE["st_deep"])
        shift = (row_y // 4) % 2 * 5
        for bx in range(134 + shift, 184, 10):
            g.line(bx, row_y, bx, row_y + 3, PALETTE["st_deep"])
            g.set(bx + 1, row_y + 1, PALETTE["st_mid"])

    # Flagpole & Burning Royal Banner on Keep
    g.line(156, 88, 156, 108, PALETTE["wd_dark"])
    g.set(156, 87, PALETTE["b_gold"])
    banner_pts = [(157, 89), (174, 92), (168, 98), (176, 104), (157, 102)]
    g.poly(banner_pts, PALETTE["b_red"])
    g.line(157, 89, 174, 92, PALETTE["b_gold"])
    g.line(157, 102, 176, 104, PALETTE["b_gold"])
    # Fire at banner tip
    g.set(174, 92, PALETTE["f_orange"])
    g.set(175, 93, PALETTE["f_yellow"])
    g.set(176, 104, PALETTE["f_orange"])
    g.set(177, 103, PALETTE["f_yellow"])

    # C. Great East Tower - Struck by Dragon Breath! (x: 184 to 244, y: 96 to 180)
    g.rect(184, 114, 60, 66, PALETTE["st_dark"])
    # Fiery highlights on west-facing wall
    for ty in range(112, 176):
        g.set(184, ty, PALETTE["st_glow"])
        g.set(185, ty, PALETTE["st_warm2"])
        g.set(186, ty, PALETTE["st_warm1"])

    # East Tower brick courses
    for row_y in range(118, 176, 4):
        g.line(184, row_y, 244, row_y, PALETTE["st_deep"])
        shift = (row_y // 4) % 2 * 5
        for bx in range(184 + shift, 244, 10):
            g.line(bx, row_y, bx, row_y + 3, PALETTE["st_deep"])
            if bx < 208:
                g.set(bx + 1, row_y + 1, PALETTE["st_warm2"])
            else:
                g.set(bx + 1, row_y + 1, PALETTE["st_mid"])

    # Blazing tower windows
    e_windows = [(198, 124), (224, 124), (211, 142)]
    for wx, wy in e_windows:
        g.rect(wx, wy, 6, 10, PALETTE["f_char"])
        g.rect(wx + 1, wy + 1, 4, 8, PALETTE["f_red"])
        g.rect(wx + 2, wy + 2, 2, 6, PALETTE["f_orange"])
        g.rect(wx + 2, wy + 3, 2, 3, PALETTE["f_yellow"])
        g.set(wx + 2, wy + 4, PALETTE["f_white"])

    # Shattered parapet & falling stone debris
    g.poly([(184, 114), (194, 102), (202, 108), (212, 114), (220, 108), (232, 104), (244, 114), (244, 120), (184, 120)], PALETTE["st_mid"])
    # Tumbling shattered blocks with fiery edges
    debris = [
        (180, 96, 4, 3, "st_mid"), (188, 86, 3, 4, "st_dark"),
        (228, 80, 4, 3, "st_warm2"), (240, 90, 4, 4, "st_mid"),
        (248, 104, 3, 3, "st_shadow"), (202, 82, 4, 3, "st_light")
    ]
    for dx, dy, dw, dh, dcol in debris:
        g.rect(dx, dy, dw, dh, PALETTE[dcol])
        g.set(dx, dy, PALETTE["f_orange"])
        g.set(dx + dw - 1, dy, PALETTE["f_yellow"])

    # Giant Roaring Inferno crowning East Tower (y: 68 to 114, x: 190 to 242)
    flame_outer = [
        (190, 114), (194, 94), (198, 102), (206, 72), (214, 92),
        (222, 68), (230, 88), (236, 78), (242, 114)
    ]
    g.poly(flame_outer, PALETTE["f_red"])
    flame_mid = [
        (194, 114), (198, 98), (206, 78), (214, 96), (221, 74), (228, 92), (236, 114)
    ]
    g.poly(flame_mid, PALETTE["f_orange"])
    flame_core = [
        (198, 114), (204, 100), (208, 84), (214, 100), (219, 82), (224, 98), (230, 114)
    ]
    g.poly(flame_core, PALETTE["f_yellow"])
    # White-hot core
    g.rect(206, 94, 6, 10, PALETTE["f_white"])
    g.rect(217, 90, 5, 12, PALETTE["f_white"])

    # 5. Knights & Defenders on Ramparts (y = 100 to 130)
    # A. Spearman bracing spear at x=98
    g.rect(98, 122, 3, 5, PALETTE["st_metal"])
    g.rect(97, 119, 5, 4, PALETTE["b_red"])
    g.rect(98, 116, 3, 3, PALETTE["st_plate"])
    g.set(98, 116, PALETTE["st_glint"])
    # Kite shield
    g.rect(96, 120, 2, 6, PALETTE["b_bright"])
    g.set(96, 122, PALETTE["b_gold"])
    # Angled spear pointing up at dragon
    g.line(99, 120, 106, 102, PALETTE["wd_mid"])
    g.set(106, 102, PALETTE["st_glint"])
    g.set(107, 101, PALETTE["st_white"])

    # B. Archer drawing bow at x=110
    g.rect(110, 122, 3, 5, PALETTE["st_armor"])
    g.rect(109, 119, 5, 4, PALETTE["b_red"])
    g.rect(110, 116, 3, 3, PALETTE["st_plate"])
    g.set(111, 116, PALETTE["st_glint"])
    # Longbow
    g.line(108, 112, 107, 124, PALETTE["wd_light"])
    g.line(108, 112, 113, 118, PALETTE["st_glint"])
    g.line(107, 124, 113, 118, PALETTE["st_glint"])
    g.line(113, 118, 106, 110, PALETTE["wd_hi"])
    g.set(105, 109, PALETTE["st_white"])

    # C. Knight Captain shouting orders at x=122
    g.rect(122, 122, 4, 5, PALETTE["st_metal"])
    g.rect(121, 119, 6, 4, PALETTE["st_plate"])
    g.set(122, 119, PALETTE["b_gold"])
    g.rect(122, 115, 4, 4, PALETTE["st_glint"])
    # Billowing red cape
    g.poly([(120, 119), (116, 123), (117, 128), (121, 124)], PALETTE["b_bright"])
    # Raised broadsword
    g.line(125, 119, 132, 108, PALETTE["st_white"])
    g.set(132, 108, PALETTE["st_glint"])
    g.set(125, 119, PALETTE["b_gold"])

    # D. Defenders on Central Keep (y: 102 to 116)
    # Spearman at x=142
    g.rect(142, 108, 3, 5, PALETTE["st_metal"])
    g.rect(141, 105, 5, 4, PALETTE["b_red"])
    g.rect(142, 102, 3, 3, PALETTE["st_plate"])
    g.set(142, 102, PALETTE["st_glint"])
    g.line(143, 106, 148, 90, PALETTE["wd_mid"])
    g.set(148, 90, PALETTE["st_white"])

    # Archer at x=152
    g.rect(152, 108, 3, 5, PALETTE["st_armor"])
    g.rect(151, 105, 5, 4, PALETTE["b_red"])
    g.rect(152, 102, 3, 3, PALETTE["st_plate"])
    g.line(150, 100, 149, 110, PALETTE["wd_light"])
    g.line(149, 104, 144, 96, PALETTE["wd_hi"])
    g.set(143, 95, PALETTE["st_white"])

    # Shield Knight guarding against embers at x=170
    g.rect(170, 108, 4, 5, PALETTE["st_metal"])
    g.rect(170, 103, 3, 4, PALETTE["st_plate"])
    g.line(168, 101, 174, 99, PALETTE["b_bright"])
    g.line(168, 102, 174, 100, PALETTE["b_gold"])

    # Reeling defender at x=186 near blast zone
    g.rect(186, 109, 4, 4, PALETTE["st_armor"])
    g.rect(187, 106, 3, 3, PALETTE["st_plate"])
    g.line(189, 107, 194, 104, PALETTE["st_metal"])

    # 6. Wooden Siege Tower (x = 16 to 68, y = 110 to 214)
    tower_pts = [(24, 112), (60, 112), (66, 204), (18, 204)]
    g.poly(tower_pts, PALETTE["wd_dark"])

    # Horizontal beams
    for dy in [112, 134, 158, 182, 202]:
        f = (dy - 112) / (202 - 112)
        xl = int(24 - f * 6)
        xr = int(60 + f * 6)
        g.rect(xl - 1, dy, (xr - xl) + 2, 4, PALETTE["wd_mid"])
        g.line(xl, dy, xr, dy, PALETTE["wd_hi"])

    # Vertical & corner beams
    g.line(24, 112, 18, 204, PALETTE["wd_light"])
    g.line(25, 112, 19, 204, PALETTE["wd_mid"])
    g.line(60, 112, 66, 204, PALETTE["wd_mid"])
    g.line(59, 112, 65, 204, PALETTE["wd_light"])
    g.line(42, 112, 42, 204, PALETTE["wd_light"])

    # X-bracing in panels
    for yt, yb in [(134, 158), (158, 182), (182, 202)]:
        ft, fb = (yt - 112) / 90.0, (yb - 112) / 90.0
        xlt, xrt = int(24 - ft * 6), int(60 + ft * 6)
        xlb, xrb = int(24 - fb * 6), int(60 + fb * 6)
        g.line(xlt + 2, yt + 4, 41, yb, PALETTE["wd_mid"])
        g.line(xlb + 2, yb, 41, yt + 4, PALETTE["wd_mid"])
        g.line(43, yt + 4, xrb - 2, yb, PALETTE["wd_mid"])
        g.line(43, yb, xrt - 2, yt + 4, PALETTE["wd_mid"])

    # Top platform mantlets (wooden teeth)
    for wx in range(22, 60, 7):
        g.rect(wx, 108, 5, 6, PALETTE["wd_light"])
        g.line(wx, 108, wx + 4, 108, PALETTE["wd_hi"])
        g.set(wx + 2, 111, PALETTE["wd_iron"])

    # Assault Bridge / Gangway extending toward castle
    bridge_pts = [(52, 118), (88, 126), (88, 130), (52, 122)]
    g.poly(bridge_pts, PALETTE["wd_pale"])
    g.line(52, 118, 88, 126, PALETTE["wd_hi"])
    g.line(56, 110, 86, 126, PALETTE["wd_iron"])
    g.line(56, 111, 86, 127, PALETTE["st_metal"])

    # Soldiers on Siege Tower Platform:
    # Archer at x=28
    g.rect(28, 103, 3, 5, PALETTE["st_armor"])
    g.rect(28, 100, 3, 3, PALETTE["st_plate"])
    g.line(26, 98, 25, 106, PALETTE["wd_hi"])
    g.line(25, 102, 33, 96, PALETTE["wd_light"])
    g.set(34, 95, PALETTE["st_white"])

    # Spearman stepping on assault bridge at x=48
    g.rect(48, 113, 3, 5, PALETTE["st_metal"])
    g.rect(48, 110, 3, 3, PALETTE["st_plate"])
    g.line(48, 112, 58, 108, PALETTE["wd_mid"])
    g.set(58, 108, PALETTE["st_glint"])
    g.set(59, 107, PALETTE["st_white"])
    g.circle(46, 114, 2, PALETTE["b_bright"])
    g.set(46, 114, PALETTE["b_gold"])

    # Tower War Banner
    g.rect(34, 140, 11, 18, PALETTE["b_dark"])
    g.rect(35, 141, 9, 16, PALETTE["b_red"])
    g.line(38, 146, 42, 152, PALETTE["b_yellow"])
    g.line(38, 152, 42, 146, PALETTE["b_yellow"])
    g.set(34, 158, PALETTE["wd_dark"])
    g.set(39, 156, PALETTE["wd_dark"])
    g.set(44, 158, PALETTE["wd_dark"])

    # Base Chassis & Heavy Iron-rimmed Wheels
    g.rect(14, 198, 56, 6, PALETTE["wd_darkest"])
    wheels = [(22, 206), (36, 206), (48, 206), (62, 206)]
    for wx, wy in wheels:
        g.circle(wx, wy, 6, PALETTE["wd_iron"], fill=True)
        g.circle(wx, wy, 4, PALETTE["wd_mid"], fill=True)
        g.circle(wx, wy, 2, PALETTE["wd_iron"], fill=True)
        g.set(wx, wy, PALETTE["st_glint"])

    # Trebuchet / Catapult (x = 74 to 98, y = 182 to 216)
    g.line(74, 212, 84, 192, PALETTE["wd_light"])
    g.line(94, 212, 84, 192, PALETTE["wd_light"])
    g.line(72, 212, 96, 212, PALETTE["wd_mid"])
    g.rect(76, 198, 7, 10, PALETTE["wd_darkest"])
    g.rect(77, 199, 5, 8, PALETTE["wd_mid"])
    g.line(78, 204, 91, 168, PALETTE["wd_pale"])
    g.line(79, 204, 92, 168, PALETTE["wd_light"])
    g.circle(84, 192, 2, PALETTE["wd_iron"])
    g.set(84, 192, PALETTE["st_plate"])
    # Flaming pitch ball launched into sky
    g.circle(96, 156, 3, PALETTE["f_red"])
    g.circle(96, 156, 2, PALETTE["f_orange"])
    g.set(96, 156, PALETTE["f_yellow"])
    g.set(94, 159, PALETTE["f_orange"])
    g.set(92, 163, PALETTE["f_yellow"])
    g.set(90, 167, PALETTE["f_crimson"])

    # 7. Battlefield & Armies in Formation (y = 195 to 254)
    # Rear ranks of spearmen (y = 198 to 216, x = 20 to 125)
    for ry in [198, 204, 210]:
        x_off = (ry // 6) % 2 * 4
        for sx in range(22 + x_off, 118, 6):
            g.rect(sx, ry, 3, 2, PALETTE["st_plate"])
            g.set(sx + 1, ry, PALETTE["st_glint"])
            g.rect(sx, ry + 2, 3, 3, PALETTE["st_armor"])
            # Pikes angled up at 55 degrees
            g.line(sx + 1, ry + 1, sx + 11, ry - 14, PALETTE["wd_mid"])
            g.set(sx + 11, ry - 14, PALETTE["st_glint"])
            g.set(sx + 12, ry - 15, PALETTE["st_white"])

    # War Banners in the ranks
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

    # Front Rank: Locked Shield Wall (y = 216 to 232, x = 20 to 120)
    for sx in range(20, 120, 5):
        g.rect(sx + 1, 214, 3, 3, PALETTE["st_plate"])
        g.set(sx + 2, 214, PALETTE["st_glint"])
        g.line(sx + 1, 216, sx + 3, 216, PALETTE["st_armor"])
        g.rect(sx, 217, 5, 11, PALETTE["b_red"])
        g.rect(sx + 1, 217, 3, 11, PALETTE["b_bright"])
        g.set(sx + 2, 220, PALETTE["b_gold"])
        g.set(sx + 2, 221, PALETTE["b_gold"])
        g.set(sx + 1, 220, PALETTE["b_gold"])
        g.set(sx + 3, 220, PALETTE["b_gold"])
        # Spear protruding over shield
        g.line(sx + 3, 218, sx + 12, 208, PALETTE["wd_hi"])
        g.set(sx + 12, 208, PALETTE["st_white"])

    # Mounted General / Knight Commander (x = 124 to 154, y = 206 to 242)
    # Warhorse
    horse_pts = [
        (128, 224), (134, 218), (144, 218), (150, 222), (147, 232), (130, 232)
    ]
    g.poly(horse_pts, PALETTE["b_dark"])
    g.rect(130, 222, 17, 8, PALETTE["b_red"])
    g.line(129, 230, 148, 230, PALETTE["b_gold"])

    # Horse neck & armored head
    g.line(144, 220, 151, 211, PALETTE["b_red"])
    g.line(145, 220, 152, 211, PALETTE["b_red"])
    g.rect(150, 210, 4, 5, PALETTE["st_metal"])
    g.set(152, 209, PALETTE["st_glint"])
    g.set(153, 212, PALETTE["st_white"])

    # Horse legs
    g.line(131, 232, 129, 242, PALETTE["g_shadow"])
    g.line(135, 232, 137, 242, PALETTE["g_shadow"])
    g.line(143, 232, 145, 242, PALETTE["g_shadow"])
    g.line(147, 232, 152, 240, PALETTE["g_shadow"])

    # Knight Commander in saddle
    g.rect(135, 213, 5, 6, PALETTE["st_plate"])
    g.rect(135, 207, 4, 6, PALETTE["st_glint"])
    g.set(136, 206, PALETTE["b_gold"])
    g.set(137, 205, PALETTE["b_gold"])
    # Broadsword raised high toward castle
    g.line(138, 211, 148, 196, PALETTE["st_white"])
    g.line(139, 211, 149, 196, PALETTE["st_glint"])
    g.set(138, 212, PALETTE["b_gold"])

    # Additional foot soldiers advancing behind general (x = 152 to 178, y = 216 to 238)
    for ax in [156, 164, 172]:
        g.rect(ax, 220, 3, 3, PALETTE["st_plate"])
        g.set(ax + 1, 220, PALETTE["st_glint"])
        g.rect(ax, 223, 3, 6, PALETTE["b_red"])
        g.line(ax + 1, 222, ax + 7, 214, PALETTE["wd_hi"])
        g.set(ax + 7, 214, PALETTE["st_white"])

    # Foreground stakes & barricades (y = 236 to 256)
    stakes = [(18, 246, -1), (28, 244, -1), (72, 248, -1), (82, 246, -1), (110, 248, 1), (170, 246, 1), (180, 248, 1)]
    for stx, sty, sdir in stakes:
        g.line(stx, sty, stx + sdir * 6, sty - 10, PALETTE["wd_dark"])
        g.line(stx + 1, sty, stx + sdir * 6 + 1, sty - 10, PALETTE["wd_light"])
        g.set(stx + sdir * 6, sty - 10, PALETTE["wd_hi"])

    # Burning iron brazier at x=162, y=242
    g.line(160, 248, 162, 244, PALETTE["wd_iron"])
    g.line(164, 248, 162, 244, PALETTE["wd_iron"])
    g.rect(160, 242, 5, 3, PALETTE["wd_iron"])
    g.set(161, 241, PALETTE["f_red"])
    g.set(162, 240, PALETTE["f_yellow"])
    g.set(163, 241, PALETTE["f_orange"])
    g.line(156, 249, 168, 249, PALETTE["g_ember"])

    # Discarded shield and broken spear in foreground (x: 104, y: 248)
    g.circle(104, 248, 4, PALETTE["b_red"])
    g.set(104, 248, PALETTE["b_gold"])
    g.line(98, 252, 112, 244, PALETTE["wd_mid"])

    # 8. The Ancient Dragon (Upper Sky, x = 40 to 240, y = 15 to 118)
    # A. Left Wing (x: 42 to 138, y: 15 to 68)
    # Wing membrane polygons
    mem1 = [(82, 18), (68, 21), (54, 24), (44, 28), (48, 38), (56, 48)]
    g.poly(mem1, PALETTE["drg_w2"])
    mem2 = [(82, 18), (56, 48), (64, 54), (74, 60)]
    g.poly(mem2, PALETTE["drg_w1"])
    mem3 = [(82, 18), (74, 60), (84, 64), (96, 66), (112, 58), (124, 46)]
    g.poly(mem3, PALETTE["drg_w2"])

    # Wing membrane translucent highlights & folds
    g.line(82, 18, 52, 40, PALETTE["drg_w3"])
    g.line(82, 18, 66, 54, PALETTE["drg_w3"])
    g.line(82, 18, 86, 62, PALETTE["drg_w3"])

    # Wing backlit rim glow along scalloped edges
    scallops = [
        ((44, 28), (48, 38)), ((48, 38), (56, 48)),
        ((56, 48), (64, 54)), ((64, 54), (74, 60)),
        ((74, 60), (84, 64)), ((84, 64), (96, 66))
    ]
    for p0, p1 in scallops:
        g.line(p0[0], p0[1], p1[0], p1[1], PALETTE["drg_w4"])

    # Dark outline along wing top edge
    g.line(82, 17, 44, 27, PALETTE["drg_out"])

    # Wing arm bone (Humerus & Forearm)
    g.line(124, 46, 102, 32, PALETTE["drg_s2"])
    g.line(124, 47, 102, 33, PALETTE["drg_s3"])
    g.line(102, 32, 82, 18, PALETTE["drg_s4"])
    g.line(102, 33, 82, 19, PALETTE["drg_s5"])
    # Thumb hook claw at wrist
    g.line(82, 18, 79, 15, PALETTE["drg_horn2"])
    g.set(78, 14, PALETTE["st_white"])

    # Wing finger struts
    g.line(82, 18, 44, 28, PALETTE["drg_s4"])
    g.line(82, 18, 56, 48, PALETTE["drg_s4"])
    g.line(82, 18, 74, 60, PALETTE["drg_s4"])
    g.line(82, 18, 96, 66, PALETTE["drg_s4"])
    for fx, fy in [(44, 28), (56, 48), (74, 60), (96, 66)]:
        g.set(fx, fy, PALETTE["st_white"])

    # B. Right Wing (x: 150 to 238, y: 12 to 62)
    r_mem1 = [(142, 44), (184, 15), (208, 18), (236, 24), (228, 36), (222, 44)]
    g.poly(r_mem1, PALETTE["drg_w2"])
    r_mem2 = [(142, 44), (222, 44), (214, 50), (204, 56), (172, 52)]
    g.poly(r_mem2, PALETTE["drg_w1"])

    # Underwing warm reflection from fire
    g.line(236, 24, 222, 44, PALETTE["f_orange"])
    g.line(222, 44, 204, 56, PALETTE["f_red"])
    g.line(184, 14, 236, 23, PALETTE["drg_out"])

    # Right wing bones
    g.line(142, 44, 184, 15, PALETTE["drg_s4"])
    g.line(184, 15, 236, 24, PALETTE["drg_s5"])
    g.line(184, 15, 222, 44, PALETTE["drg_s5"])
    g.line(184, 15, 204, 56, PALETTE["drg_s5"])
    g.set(184, 14, PALETTE["st_white"])

    # C. Dragon Body & Torso (x: 112 to 148, y: 44 to 72)
    body_pts = [
        (114, 52), (124, 46), (138, 44), (148, 50),
        (146, 64), (136, 72), (122, 70), (112, 62)
    ]
    g.poly(body_pts, PALETTE["drg_s2"])
    # Belly plates
    belly_pts = [(122, 70), (136, 72), (146, 64), (142, 60), (132, 66), (120, 64)]
    g.poly(belly_pts, PALETTE["drg_b2"])
    g.line(122, 70, 136, 72, PALETTE["drg_b4"])
    g.line(136, 72, 146, 64, PALETTE["drg_b3"])

    # Scales highlight on ribcage
    g.circle(130, 54, 4, PALETTE["drg_s4"])
    g.set(130, 53, PALETTE["drg_s5"])
    g.set(131, 52, PALETTE["drg_s6"])

    # D. Sinuous Neck (x: 126 to 174, y: 38 to 74)
    neck_pts = [
        (136, 46), (146, 40), (158, 44), (170, 56), (174, 68),
        (164, 72), (154, 62), (144, 54), (138, 50)
    ]
    g.poly(neck_pts, PALETTE["drg_s3"])
    g.line(136, 46, 146, 40, PALETTE["drg_s5"])
    g.line(146, 40, 158, 44, PALETTE["drg_s4"])
    g.line(158, 44, 170, 56, PALETTE["drg_s4"])
    # Spines along neck ridge
    neck_spines = [(142, 41), (148, 38), (154, 40), (162, 46), (168, 52)]
    for spx, spy in neck_spines:
        g.line(spx, spy, spx - 2, spy - 4, PALETTE["drg_horn2"])
        g.set(spx - 2, spy - 4, PALETTE["st_white"])

    # Underside fire reflection
    g.line(138, 50, 144, 54, PALETTE["drg_b3"])
    g.line(144, 54, 154, 62, PALETTE["drg_b4"])
    g.line(154, 62, 164, 72, PALETTE["f_orange"])

    # E. Dragon Head & Horns (x: 168 to 200, y: 58 to 84)
    skull_pts = [
        (170, 58), (180, 56), (192, 64), (198, 70), (194, 74), (184, 72), (174, 66)
    ]
    g.poly(skull_pts, PALETTE["drg_s4"])
    g.line(170, 58, 180, 56, PALETTE["drg_s5"])
    g.line(180, 56, 192, 64, PALETTE["drg_s6"])

    # Sweeping majestic horns
    # Horn 1
    g.line(174, 58, 165, 46, PALETTE["drg_horn1"])
    g.line(165, 46, 156, 40, PALETTE["drg_horn2"])
    g.set(155, 39, PALETTE["st_white"])
    # Horn 2
    g.line(172, 62, 161, 52, PALETTE["drg_horn1"])
    g.line(161, 52, 152, 48, PALETTE["drg_horn2"])
    g.set(151, 47, PALETTE["st_white"])

    # Eye & Brow
    g.line(180, 62, 186, 62, PALETTE["drg_out"])
    g.rect(182, 63, 3, 2, PALETTE["f_yellow"])
    g.set(183, 63, PALETTE["f_white"]) # pupil slit
    g.set(182, 64, PALETTE["f_orange"])

    # Fangs & Open Jaws
    g.line(184, 72, 196, 72, PALETTE["drg_out"])
    g.set(186, 73, PALETTE["f_white"])
    g.set(190, 73, PALETTE["f_white"])
    g.set(194, 73, PALETTE["f_white"])

    # Lower Jaw
    lower_jaw = [(176, 74), (184, 82), (194, 80), (184, 75)]
    g.poly(lower_jaw, PALETTE["drg_s3"])
    g.line(184, 82, 194, 80, PALETTE["drg_s5"])
    g.set(186, 79, PALETTE["f_white"])
    g.set(191, 78, PALETTE["f_white"])

    # Throat fire glow
    g.rect(180, 74, 6, 4, PALETTE["f_yellow"])
    g.set(182, 75, PALETTE["f_white"])

    # F. Apocalyptic Torrent of Dragon Breath (Blasting East Tower!)
    breath_outer = [
        (194, 74), (200, 78), (218, 98), (226, 114), (204, 112), (194, 82)
    ]
    g.poly(breath_outer, PALETTE["f_red"])

    breath_mid = [
        (195, 75), (202, 80), (215, 98), (222, 112), (206, 110), (195, 80)
    ]
    g.poly(breath_mid, PALETTE["f_orange"])

    breath_core = [
        (196, 76), (204, 82), (212, 98), (218, 110), (208, 108), (196, 79)
    ]
    g.poly(breath_core, PALETTE["f_yellow"])

    # Blinding white hot laser core
    g.line(196, 77, 214, 106, PALETTE["f_white"])
    g.line(197, 78, 215, 107, PALETTE["f_white"])
    g.line(196, 78, 214, 107, PALETTE["f_pale"])

    # Flame tendrils and swirls
    g.line(201, 84, 207, 82, PALETTE["f_yellow"])
    g.line(208, 92, 217, 90, PALETTE["f_orange"])
    g.line(212, 98, 223, 95, PALETTE["f_red"])

    # G. Hind Leg & Talons (x: 110 to 126, y: 64 to 84)
    thigh_pts = [(118, 64), (126, 68), (122, 76), (114, 72)]
    g.poly(thigh_pts, PALETTE["drg_s2"])
    g.line(116, 72, 112, 80, PALETTE["drg_s3"])
    g.line(112, 80, 108, 82, PALETTE["st_plate"])
    g.line(112, 80, 111, 84, PALETTE["st_plate"])
    g.line(112, 80, 115, 83, PALETTE["st_plate"])
    g.set(107, 82, PALETTE["st_white"])
    g.set(111, 85, PALETTE["st_white"])

    # H. Long Serpentine Tail (x: 52 to 116, y: 52 to 82)
    tail_pts = [
        (116, 62), (102, 68), (88, 70), (74, 68), (62, 72), (54, 78),
        (55, 82), (66, 76), (78, 72), (92, 74), (106, 72), (116, 66)
    ]
    g.poly(tail_pts, PALETTE["drg_s2"])
    g.line(116, 62, 54, 78, PALETTE["drg_s3"])
    tail_spines = [(108, 65), (98, 68), (86, 69), (76, 68), (64, 71)]
    for tx, ty in tail_spines:
        g.line(tx, ty, tx - 1, ty - 3, PALETTE["drg_horn2"])
        g.set(tx - 1, ty - 3, PALETTE["st_white"])
    tip_pts = [(54, 78), (48, 76), (46, 80), (48, 84), (54, 82)]
    g.poly(tip_pts, PALETTE["drg_s5"])
    g.set(45, 80, PALETTE["st_white"])

    # 9. Atmospheric Billowing Smoke Plumes
    smoke_puffs = [
        (216, 66, 14, "smk_dark"),
        (230, 52, 18, "smk_black"),
        (204, 46, 16, "smk_mid"),
        (188, 40, 14, "smk_dark"),
        (240, 36, 16, "smk_black"),
        (218, 28, 20, "smk_dark"),
        (178, 30, 15, "smk_mid"),
        (156, 24, 12, "smk_black"),
        (208, 62, 8, "smk_fire"),
        (218, 50, 9, "smk_warm"),
        (198, 46, 7, "smk_warm"),
    ]
    for smx, smy, smr, smcol in smoke_puffs:
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
        # Ramparts firing up at dragon & field
        (116, 108, 4, -3, False),
        (128, 102, 5, -2, False),
        (158, 92, 4, -4, False),
        (148, 86, 3, -5, True), # flaming arrow aimed at dragon
        (138, 78, 3, -4, False),
        # Army & siege tower firing up at castle
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

    # Arrows stuck in wood and stone
    stuck_arrows = [
        (48, 146, -3, -2), (56, 168, -4, -1), (112, 144, 3, -2), (124, 152, 4, -3)
    ]
    for sx, sy, sdx, sdy in stuck_arrows:
        g.line(sx, sy, sx + sdx, sy + sdy, PALETTE["wd_mid"])
        g.set(sx + sdx, sy + sdy, PALETTE["b_red"])

    # 11. Swirling Glowing Embers & Atmospheric Sparks
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
