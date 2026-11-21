from pixelbench_api import *

W = H = 128
c = new_canvas(W, H, name="title")

# --- sky gradient (sunset): top deep purple -> mid magenta -> orange near horizon
sky_bands = [
    (0,  18, "#2a1a4a"),
    (18, 30, "#4a2260"),
    (30, 42, "#7a2e63"),
    (42, 52, "#b03f55"),
    (52, 60, "#d95b3a"),
    (60, 68, "#f07f33"),
]
for y0, y1, col in sky_bands:
    c.rect(0, y0, W, y1 - y0, col)
# dither between bands for smoothness
for i in range(len(sky_bands) - 1):
    y1 = sky_bands[i][1]
    c.dither(0, y1, W, 2, [sky_bands[i][2], sky_bands[i + 1][2]], pattern="checker")

HORIZON = 68

# --- large orange sun, half set at horizon
c.circle(78, 66, 16, "#ffd23f", fill=True)
c.circle(78, 66, 16, "#ffb340", fill=False)
# sun reflection on sea
c.rect(70, HORIZON, 17, 20, "#f0a04a")
for yy in range(HORIZON, 100, 3):
    c.line(72 + (yy % 5), yy, 86 - (yy % 5), yy, "#ffd97a")

# --- sea
c.rect(0, HORIZON, W, 40, "#1c3a5e")
c.rect(0, HORIZON, W, 6, "#2e5a80")
for yy in range(HORIZON + 8, 108, 4):
    c.line(0, yy, W, yy, "#2a4f74")
# sparkle lines
for xx, yy in [(20, 80), (40, 92), (100, 84), (60, 100), (15, 100)]:
    c.line(xx, yy, xx + 6, yy, "#7fb2d9")

# --- layered clouds
def cloud(x, y, w, col):
    c.ellipse(x + w // 2, y, w // 2, 3, col, fill=True)
    c.ellipse(x + w // 4, y - 2, w // 5, 2, col, fill=True)
    c.ellipse(x + 3 * w // 4, y - 1, w // 5, 2, col, fill=True)

cloud(6, 22, 44, "#5a3a72")
cloud(60, 14, 56, "#4a2f63")
cloud(96, 30, 40, "#6b4478")
cloud(20, 38, 52, "#8a4f6e")
cloud(80, 44, 40, "#a85f5c")
cloud(0, 50, 34, "#c76b4e")
cloud(50, 56, 30, "#d97b45")

# --- distant headland
c.poly([(0, 70), (14, 62), (30, 68), (44, 66), (44, 74), (0, 74)], "#2f3a5c", fill=True)

# --- cliff (right side, castle sits on top)
c.poly([(64, 74), (78, 72), (96, 70), (118, 70), (128, 74), (128, 128),
        (108, 128), (100, 108), (90, 96), (80, 86), (70, 80)], "#3a3040", fill=True)
# cliff face shading
c.poly([(90, 96), (100, 108), (108, 128), (96, 128), (88, 104), (82, 90)], "#2a2230", fill=True)
c.line(78, 72, 74, 80, "#4a3f52")
c.line(96, 70, 94, 80, "#4a3f52")

# --- castle: keep + two towers with flags
STONE = "#b8a89a"
STONE_D = "#8a7a70"
STONE_L = "#d8ccc0"

# central keep
c.rect(84, 44, 22, 28, STONE)
c.rect(84, 44, 22, 3, STONE_L)
c.rect(84, 68, 22, 4, STONE_D)
# keep roof
c.poly([(82, 44), (95, 34), (108, 44)], "#7a3040", fill=True)
# keep windows
for wx in (88, 94, 100):
    c.rect(wx, 50, 2, 4, "#2a1a30")
    c.rect(wx, 58, 2, 4, "#ffcf6a")

# left tower (taller, on cliff edge)
c.rect(72, 40, 10, 34, STONE)
c.rect(72, 40, 10, 2, STONE_L)
c.rect(72, 70, 10, 4, STONE_D)
c.poly([(70, 40), (77, 30), (84, 40)], "#5a6a8a", fill=True)
c.rect(75, 48, 3, 5, "#2a1a30")
c.rect(75, 58, 3, 5, "#ffcf6a")
c.rect(75, 66, 3, 4, "#ffcf6a")

# right tower
c.rect(108, 48, 10, 26, STONE)
c.rect(108, 48, 10, 2, STONE_L)
c.rect(108, 70, 10, 4, STONE_D)
c.poly([(106, 48), (113, 38), (120, 48)], "#5a6a8a", fill=True)
c.rect(111, 56, 3, 5, "#2a1a30")
c.rect(111, 64, 3, 5, "#ffcf6a")

# battlements on keep
for bx in range(84, 106, 4):
    c.rect(bx, 41, 2, 3, STONE)

# --- flags
def flag(pole_x, pole_top_y, col):
    c.line(pole_x, pole_top_y, pole_x, pole_top_y - 9, "#3a2a20")
    c.poly([(pole_x + 1, pole_top_y - 9), (pole_x + 8, pole_top_y - 7), (pole_x + 1, pole_top_y - 5)], col, fill=True)

flag(77, 30, "#d84040")   # left tower, red pennant
flag(113, 38, "#e8a020")  # right tower, gold pennant
flag(95, 34, "#d84040")   # keep roof

# --- wall between towers
c.rect(82, 66, 26, 6, STONE_D)
for bx in range(83, 107, 4):
    c.rect(bx, 64, 2, 2, STONE)

# --- gate
c.rect(90, 66, 8, 6, "#2a1a30")

# --- dark rocks foreground (bottom, silhouetted)
c.poly([(0, 128), (0, 112), (10, 106), (22, 112), (34, 104), (48, 112),
        (60, 106), (72, 114), (86, 108), (100, 116), (114, 110), (128, 116),
        (128, 128)], "#1a1420", fill=True)
# rock highlights
c.line(10, 106, 22, 112, "#2e2438")
c.line(34, 104, 48, 112, "#2e2438")
c.line(86, 108, 100, 116, "#2e2438")

# --- birds
for bx, by in [(30, 30), (38, 26), (50, 34)]:
    c.line(bx, by, bx + 2, by - 1, "#1a1420")
    c.line(bx + 2, by - 1, bx + 4, by, "#1a1420")

# --- title text
c.text(14, 6, "DRAGONCOAST", "#ffe9b0", font="5x7")
c.text(28, 116, "PRESS START", "#e8c080", font="5x7")

print(c.stats_text())
finish(c)
