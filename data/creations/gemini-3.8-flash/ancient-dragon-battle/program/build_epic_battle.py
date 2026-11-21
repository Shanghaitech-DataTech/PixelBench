import math
import random

W, H = 256, 256

PALETTE = {
    # Sky & Sunset Gradient
    "sky_space": "#0a0512",
    "sky_twilight": "#160b22",
    "sky_purple": "#2b0f34",
    "sky_plum": "#46133f",
    "sky_crimson": "#6b193d",
    "sky_ruby": "#992233",
    "sky_blood_orange": "#c23825",
    "sky_deep_orange": "#e35920",
    "sky_bright_orange": "#f78223",
    "sky_amber": "#fcae33",
    "sky_gold": "#fde05c",
    "sky_pale_yellow": "#fff49e",

    # Mountains & Horizon
    "mtn_shadow": "#140c1c",
    "mtn_body": "#24162e",
    "mtn_mid": "#382242",
    "mtn_light": "#54304e",
    "mtn_rim": "#9e3e44",
    "mtn_goldrim": "#c75c36",

    # Smoke & Dust
    "smoke_darkest": "#100d14",
    "smoke_deep": "#1c1720",
    "smoke_mid": "#302633",
    "smoke_light": "#4a3c4f",
    "smoke_pale": "#6e5c70",
    "smoke_warm_glow": "#8a483b",
    "smoke_fire_glow": "#bf663b",

    # Dragon
    "drg_outline": "#08060a",
    "drg_dark": "#120c14",
    "drg_scale_dark": "#240f1a",
    "drg_scale_mid": "#3d1222",
    "drg_scale_red": "#631726",
    "drg_scale_crimson": "#8c1e28",
    "drg_scale_bright": "#b82b2b",
    "drg_scale_hi": "#dc482c",
    "drg_belly_shadow": "#2e120f",
    "drg_belly_mid": "#541e15",
    "drg_belly_glow": "#87321e",
    "drg_belly_bright": "#bf4f26",
    "drg_wing_dark": "#1e0d17",
    "drg_wing_mid": "#381421",
    "drg_wing_light": "#5c1e2b",
    "drg_wing_rim": "#8f302e",
    "drg_horn_dark": "#1e222a",
    "drg_horn_light": "#4c5566",

    # Fire, Dragon Breath & Explosions
    "fire_white": "#ffffff",
    "fire_pale": "#fff7a3",
    "fire_yellow": "#fed233",
    "fire_orange": "#fa821c",
    "fire_red": "#e03b18",
    "fire_crimson": "#a61919",
    "fire_dark": "#5e0e16",
    "fire_char": "#24060b",

    # Castle Stone & Masonry
    "stone_deep": "#0c0e14",
    "stone_shadow": "#141821",
    "stone_dark": "#1e2430",
    "stone_mid": "#2e3646",
    "stone_light": "#444f66",
    "stone_pale": "#62708c",
    "stone_highlight": "#8898b8",
    "stone_fire_warm": "#783b28",
    "stone_fire_glow": "#b35932",

    # Siege Tower, Wood & Iron
    "wood_darkest": "#0e0906",
    "wood_dark": "#1a110a",
    "wood_mid": "#2d1b11",
    "wood_light": "#472c1c",
    "wood_pale": "#69422a",
    "wood_hi": "#8f5e3d",
    "wood_iron": "#292e38",

    # Soldiers, Knights, Armor & Banners
    "steel_dark": "#10141c",
    "steel_mid": "#1f2837",
    "steel_light": "#364459",
    "steel_bright": "#586c8a",
    "steel_glint": "#93a8c4",
    "steel_white": "#dbe8f7",
    "herald_red_dark": "#611017",
    "herald_red": "#a1181f",
    "herald_red_bright": "#d62828",
    "herald_gold": "#a87718",
    "herald_yellow": "#f2bc29",

    # Battlefield Ground & Earth
    "ground_deep": "#0c0806",
    "ground_shadow": "#140f0a",
    "ground_dark": "#211710",
    "ground_mid": "#332318",
    "ground_light": "#4a3424",
    "ground_rock": "#22242c",
    "ground_rockhi": "#3a3e4c",
    "ground_ember": "#4d1b12",
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
        # Scanline polygon fill
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

print("PixelGrid ready")
