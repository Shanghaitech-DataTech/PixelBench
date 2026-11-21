from pixelbench_api import *
import random

canvas = new_canvas(128, 128, background=(0, 0, 0))
c = canvas

def col(hex_str, name=None):
    return c.color(hex_str, name=name)

# ==============================
# REGISTER PALETTE
# ==============================
# Sky gradient
col("#080818", "sky_top")
sky_upper = col("#0d0d20")
sky_mid = col("#141430")
sky_low = col("#1a1a3a")

# Far buildings
far_1 = col("#0a0a14")
far_2 = col("#0f0f1c")

# Mid buildings
mid_1 = col("#151522")
mid_2 = col("#1a1a2c")
mid_3 = col("#20203a")

# Building details
window_dark = col("#0c0c16")
window_dim_w = col("#4a3520")
window_mid_w = col("#775a2e")
window_glow = col("#ddaa55")
pipe_col = col("#12122a")

# Ground / road
road = col("#232332")
sidewalk = col("#1a1a28")
road_line = col("#2e2e3e")
sheen = col("#3a3a55")

# Puddles
pd_a = col("#0e1c3a")
pd_b = col("#182a55")
pd_c = col("#2a4a6a")
pd_reflect = col("#2a5a7a")

# Neon colors
n_cyan = col("#00eeff")
n_cyan_d = col("#00aacc")
n_cyan_g = col("#00eeff22")
n_pink = col("#ff2d95")
n_pink_d = col("#d02080")
n_pink_g = col("#ff2d9522")
n_blue = col("#2277ff")
n_blue_g = col("#2277ff22")
n_purple = col("#9955ff")
n_yellow = col("#ffd700")
n_yellow_d = col("#ddaa00")
n_red = col("#ff3333")
n_green = col("#00ff88")
white = col("#ffffff")

# Warm interior
warm_bright = col("#ffddaa")
warm_med = col("#aa7744")
warm_dim = col("#553a28")

# Person
body = col("#06060b")
body_rim = col("#44eeff22")
body_rim_p = col("#ff2d9544")
umb = col("#88ddff55")
umb_edge = col("#bbeeff")
umb_hl = col("#ccffff66")

# Cables/structures
cable = col("#15151f")
pole = col("#1a1a28")

# Smoke/fog
fog1 = col("#1a1a3344")
fog2 = col("#20204033")
fog3 = col("#0e0e2255")

print(f"Colors registered: {len(c.palette())}")

# ==============================
# SKY BACKGROUND
# ==============================
for y in range(42):
    if y < 10:
        skyc = sky_upper if y < 6 else sky_mid
    elif y < 25:
        skyc = sky_low
    else:
        skyc = mid_1
    c.rect(0, y, 128, 1, skyc)

# ==============================
# FAR BUILDINGS (silhouette skyline)
# ==============================
buildings_far = [
    (0, 20, 32), (20, 14, 36), (34, 22, 28), (56, 18, 32),
    (74, 22, 28), (96, 16, 34), (112, 20, 30)
]
for bx, bw, bh in buildings_far:
    cy = 42 - bh
    c.rect(bx, cy, bw, bh, far_1)

random.seed(7)
for bx, bw, bh in buildings_far:
    cy = 42 - bh
    for wy in range(cy + 2, 40, 6):
        for wx in range(bx + 1, bx + bw - 2, 4):
            r = random.random()
            if r < 0.2:
                c.rect(wx, wy, 2, 2, window_dim_w)
            elif r < 0.3:
                c.rect(wx, wy, 2, 2, window_dark)

# Antenna on building
c.rect(24, 2, 1, 10, far_1)
c.set(24, 1, col("#ff3333"))

# ==============================
# MID BUILDINGS (visible structures)
# ==============================
# Left mid building - facade
c.rect(0, 12, 48, 68, mid_1)
c.rect(2, 14, 44, 64, mid_2)

# Windows on left building    
random.seed(8)
for wy in range(18, 70, 7):
    for wx in range(4, 42, 6):
        r = random.random()
        if r < 0.55:
            c.set(wx, wy, window_dark)
            c.set(wx+1, wy, window_dark)
            c.set(wx, wy+1, window_dark)
            c.set(wx+1, wy+1, window_dark)
            if r < 0.12:
                c.set(wx, wy, window_mid_w)
            elif r < 0.18:
                c.set(wx, wy, window_glow)

# Right mid building
c.rect(48, 16, 64, 72, mid_2)
# Right building small roof structure
c.rect(48, 12, 14, 4, mid_3)
c.rect(110, 8, 18, 10, mid_3)

# Windows on right building
random.seed(9)
for wy in range(22, 70, 8):
    for wx in range(50, 90, 7):
        r = random.random()
        if r < 0.5:
            c.rect(wx, wy, 3, 3, window_dark)
            if r < 0.12:
                c.rect(wx, wy, 3, 1, window_glow)

random.seed(10)
for wy in range(18, 70, 6):
    for wx in range(112, 124, 5):
        r = random.random()
        if r < 0.5:
            c.rect(wx, wy, 3, 3, window_dark)
            if r < 0.1:
                c.rect(wx, wy, 3, 1, window_mid_w)

# <- Left side cyan sign on building
# Large cyan sign board
c.rect(6, 16, 30, 42, col("#0a0a18"))
# Cyan frame
c.rect(7, 17, 28, 1, n_cyan)
c.rect(7, 56, 28, 1, n_cyan)
c.rect(7, 17, 1, 40, n_cyan)
c.rect(34, 17, 1, 40, n_cyan)
# Blue glow behind
c.rect(6, 16, 1, 44, n_blue_g)
c.rect(35, 16, 1, 44, n_blue_g)
# Random flickering text/shape inside sign
c.text(11, 24, "GAME", n_cyan, font="8px")
c.text(12, 40, "AIA", n_cyan_d, font="8px")

# Right side pink sign
c.rect(100, 22, 26, 50, col("#10081c"))
c.rect(101, 23, 24, 48, col("#160a24"))
# Neon frame
c.rect(101, 23, 24, 1, n_pink)
c.rect(101, 70, 24, 1, n_pink)
c.rect(101, 23, 1, 48, n_pink)
c.rect(124, 23, 1, 48, n_pink)
# Pink glow
c.rect(100, 22, 1, 50, n_pink_g)
c.rect(125, 22, 1, 50, n_pink_g)
# Text
c.text(104, 32, "BAR", n_pink, font="8px")
c.text(105, 46, "24h", n_pink, font="8px")
# Small heart decoration
c.set(108, 58, n_pink)
c.set(112, 58, n_pink)
c.set(109, 60, n_pink)
c.set(111, 60, n_pink)
c.set(110, 61, n_pink)

# Horizontal neon strips  
c.rect(52, 20, 16, 3, n_purple)
c.rect(56, 34, 12, 2, n_blue)
c.rect(76, 28, 5, 12, n_pink)
c.rect(82, 64, 14, 2, n_red)
c.rect(56, 72, 24, 2, n_yellow)

# Green neon on right building
c.rect(110, 30, 6, 3, n_green)

# ==============================
# STRUCTURAL LINES / GUTTERS
# ==============================
c.rect(48, 40, 1, 48, pipe_col)
c.rect(100, 72, 1, 16, pipe_col)
c.rect(0, 30, 48, 1, far_1)

# ==============================
# POWER CABLES (overhead)
# ==============================
c.path("M 0 8 Q 30 20 62 16 Q 94 12 127 22", cable)
c.path("M 0 16 Q 36 30 64 24 Q 96 18 127 28", cable)
c.path("M 0 4 Q 22 12 44 8", cable)
c.path("M 64 10 Q 88 20 120 14", cable)

# Utility poles
c.rect(10, 6, 2, 46, pole)
c.rect(62, 6, 2, 50, pole)
c.rect(118, 10, 2, 48, pole)
c.rect(96, 20, 2, 44, pole)

# ==============================
# DOORS / SHOP FRONTS
# ==============================
# Door on left building
c.rect(22, 60, 14, 28, col("#08080e"))
c.rect(24, 62, 10, 24, col("#04040a"))
c.rect(26, 64, 4, 3, warm_bright)
c.rect(24, 60, 1, 2, warm_med)

# Door on right building
c.rect(86, 62, 14, 26, col("#08080e"))
c.rect(88, 64, 10, 22, col("#04040a"))
c.rect(90, 66, 4, 3, warm_bright)
c.rect(88, 62, 1, 2, warm_med)

# ==============================
# VENDING MACHINES
# ==============================
# Left vending machine
c.rect(34, 76, 14, 12, col("#0e0e1a"))
c.rect(35, 77, 12, 9, col("#1a1a2a"))
# Products behind glass
c.rect(36, 78, 3, 3, n_cyan)
c.rect(40, 78, 3, 3, n_pink)
c.rect(36, 82, 3, 2, n_blue)
c.rect(40, 82, 3, 2, n_yellow)
# Glow line
c.rect(36, 84, 10, 1, n_cyan_d)
# Machine base
c.rect(34, 88, 14, 4, col("#101018"))

# Right vending machine
c.rect(78, 82, 12, 8, col("#12121c"))
c.rect(79, 83, 10, 6, col("#1e1e30"))
c.rect(80, 84, 3, 2, n_cyan)
c.rect(85, 84, 3, 2, n_pink)
c.rect(80, 87, 8, 1, n_pink_d)
c.rect(78, 90, 12, 4, col("#151520"))

# ==============================
# ROAD / GROUND
# ==============================
c.rect(0, 88, 128, 40, road)
# Sidewalk
c.rect(0, 108, 128, 20, sidewalk)

# Dashed lane markings
for lx in range(0, 132, 14):
    c.rect(lx, 92, 7, 2, road_line)
    c.rect(lx + 3, 101, 8, 2, road_line)

# ==============================
# PUDDLES & REFLECTIONS
# ==============================
# Big central puddle
c.ellipse(62, 100, 40, 6, pd_a)
c.ellipse(60, 100, 28, 4, pd_b)
c.ellipse(64, 101, 16, 3, pd_c)

# Puddles at edges
c.ellipse(16, 104, 9, 3, pd_a)
c.ellipse(108, 102, 7, 2, pd_b)
c.ellipse(2, 98, 6, 2, pd_a)

# Neon reflections on puddles
# Pink sign reflection
c.rect(80, 97, 4, 6, n_pink_d)
c.rect(83, 98, 5, 3, n_pink)
c.line(78, 100, 90, 100, n_pink)
c.line(76, 102, 93, 102, n_pink_d)

# Cyan reflection
c.rect(18, 98, 3, 5, n_cyan_d)
c.rect(14, 100, 8, 3, n_cyan)
c.line(12, 102, 24, 102, n_cyan_d)

# Yellow reflection
c.line(50, 100, 62, 100, n_yellow)
c.line(48, 102, 60, 102, n_yellow_d)

# Purple reflection
c.rect(52, 103, 3, 4, n_purple)

# Red reflection
c.line(88, 99, 94, 99, n_red)

# Reflection highlights / broken glass look
c.line(40, 99, 100, 99, pd_reflect)
c.line(35, 103, 105, 103, pd_reflect)

# Wet road sheen
for i in range(4):
    c.line(0, 90 + i * 5, 128, 90 + i * 5, sheen)

# ==============================
# PERSON (center) with transparent umbrella
# ==============================
# Position at approximately x=57-74, y=42-89
# The person is dark against neon-lit background

# Deep shadow / grounding
c.ellipse(65, 89, 11, 2, col("#08080f"))

# TRANSPARENT UMBRELLA (drawn first so body overlaps handle area)
# Umbrella as transparent dome
c.path("M 55 57 Q 65 41 75 57 Q 65 61 55 57", umb)
# Dome outline - clear visible edge
c.path("M 55 57 Q 65 41 75 57", umb_edge)
# Ribs showing through the transparent material
c.line(59, 46, 61, 59, umb_edge)
c.line(63, 43, 64, 59, umb_edge)
c.line(67, 43, 67, 59, umb_edge)
c.line(71, 47, 70, 59, umb_edge)
# Curved highlight reflecting neon lights
c.path("M 59 52 Q 65 48 71 52 Q 65 54 59 52", umb_hl)

# Handle
c.rect(64, 55, 1, 5, col("#666688"))

# PERSON BODY - dark silhouette for readability
# Head
c.circle(65, 57, 3, body)
# Torso
c.path("M 59 60 L 71 60 L 69 81 L 61 81 Z", body)
# Shoulders
c.line(58, 60, 72, 60, body)
# Left arm (up holding umbrella)
c.rect(58, 60, 3, 5, body)
c.rect(62, 57, 3, 5, body)
# Right arm  
c.line(71, 60, 73, 58, body)
c.rect(70, 57, 3, 4, body)
# Legs
c.rect(60, 81, 5, 6, body)
c.rect(65, 81, 5, 6, body)
# Feet
c.rect(58, 86, 6, 3, body)
c.rect(65, 86, 6, 3, body)

# RIM LIGHT on person from neon signs
# Left side (cyan from left sign) - brighter
for y in range(57, 67):
    c.set(57, y, col("#33eeff"))
# Right side (pink from right sign) - brighter
for y in range(58, 70):
    c.set(73, y, n_pink_d)
# Head top highlight (pink from above)
c.set(63, 56, body_rim_p)
c.set(64, 55, col("#ff2d9566"))
# Shoulder highlights
for i in range(3):
    c.set(57 + i, 60, col("#33eeff33"))
    c.set(72 - i, 60, n_pink_g)
# Leg rim light
c.set(59, 82, col("#33eeff22"))
c.set(60, 83, col("#33eeff22"))
c.set(70, 82, body_rim_p)
c.set(71, 83, body_rim_p)
# Umbrella outline catching neon - pink edge catch
for y in range(44, 50):
    c.set(55, y, col("#ff2d9544"))
# Umbrella top catching cyan  
for y in range(43, 50):
    c.set(60 + (y - 43), 43, col("#33eeff44"))
c.set(65, 42, col("#88ffee"))

# Person's reflection in puddle
c.rect(59, 92, 12, 7, col("#0a0a1a44"))
c.path("M 60 92 L 70 92 L 69 98 L 61 98 Z", col("#10102044"))

# ==============================
# LIGHT EFFECTS
# ==============================
# Glow pools
c.ellipse(60, 102, 30, 4, n_pink_g)
c.ellipse(28, 104, 16, 3, n_cyan_g)
c.ellipse(84, 100, 12, 2, fog2)

# Steam from vents
c.rect(4, 106, 3, 2, fog2)
c.rect(3, 108, 5, 2, fog1)

# ==============================
# TRASH / PROPS
# ==============================
# Trash bin
c.rect(76, 78, 4, 8, col("#14142a"))
c.rect(75, 78, 6, 1, col("#2a2a40"))

# Small crate
c.rect(52, 84, 3, 4, col("#161622"))

# Old tire
c.circle(95, 90, 3, col("#1a1a20"), fill=False)

# ==============================
# RAIN
# ==============================
random.seed(99)
# General rain
for _ in range(70):
    rx = random.randint(0, 127)
    ry = random.randint(0, 127)
    ln = 3
    c.line(rx, ry, rx, ry + ln, col("#33334e"))
    c.line(rx + 1, ry + 1, rx + 1, ry + ln + 1, col("#222240"))

# Pink-tinted rain near sign
for _ in range(18):
    rx = random.randint(100, 124)
    ry = random.randint(20, 87)
    c.line(rx, ry, rx, ry + 2, n_pink_g)

# Cyan-tinted rain near sign
for _ in range(14):
    rx = random.randint(4, 40)
    ry = random.randint(14, 87)
    c.line(rx, ry, rx, ry + 2, n_cyan_g)

# ==============================
# FINAL ATMOSPHERIC OVERLAY
# ==============================
# Thin bg haze at ground level
c.rect(0, 86, 128, 1, fog3)
c.rect(0, 106, 128, 2, fog2)

# District backdrop separation line
c.line(0, 88, 128, 88, col("#0a0a14"))

# Building base shadows
c.rect(0, 86, 22, 2, col("#0a0a12"))
c.rect(92, 86, 36, 2, col("#0a0a12"))

# Vertical building edges emphasized
c.line(48, 12, 48, 88, far_1)
c.line(100, 10, 100, 88, far_1)

# ==============================
# Output
# ==============================
print(c.stats_text())
stats = c.stats()
print(f"Colors: {stats['colors_used']}")
print(f"Coverage: {stats['coverage']}")

finish(c)
