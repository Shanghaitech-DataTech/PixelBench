from pixelbench_api import *
import random

W, H = 128, 128

bg = new_canvas(W, H, background='#0a0a18', name='bg')

def C(hexv, name=None):
    return bg.color(hexv, name)

# ---------- palette ----------
sky_top      = C('#0a0a18', 'sky_top')
sky_glow     = C('#15102c', 'sky_glow')
horizon_glow = C('#2a1a4a', 'horizon_glow')
buildingL    = C('#161224', 'buildingL')
buildingR    = C('#120e1c', 'buildingR')
edgeL        = C('#2a1f42', 'edgeL')
edgeR        = C('#251c3a', 'edgeR')
window_dark  = C('#231838', 'window_dark')
window_warm  = C('#ffd166', 'window_warm')
window_cool  = C('#5fd8ff', 'window_cool')

neon_pink   = C('#ff2fa0', 'neon_pink')
neon_cyan   = C('#2af5ff', 'neon_cyan')
neon_purple = C('#b56bff', 'neon_purple')
neon_green  = C('#3aff9e', 'neon_green')
neon_yellow = C('#ffe94a', 'neon_yellow')
neon_orange = C('#ff8a2a', 'neon_orange')

pink_ref   = C('#5a1040', 'pink_ref')
cyan_ref   = C('#0f4a52', 'cyan_ref')
purple_ref = C('#3a1a55', 'purple_ref')
green_ref  = C('#104a30', 'green_ref')
yellow_ref = C('#5a4a12', 'yellow_ref')

street      = C('#0d0b16', 'street')
street_line = C('#1d1830', 'street_line')
puddle_base = C('#07060f', 'puddle_base')
sign_bg     = C('#0d0916', 'sign_bg')
machine_bg  = C('#0b0a14', 'machine_bg')
silhouette  = C('#05050a', 'silhouette')
umbrella_light = C('#d8f6ff', 'umbrella_light')

# ---------- sky and distant glow ----------
for i, y0 in enumerate(range(0, 52, 8)):
    yy = 52 - y0
    pass

# soft glow near the vanishing point
bg.rect(40, 26, 48, 30, sky_glow, fill=True)
bg.rect(46, 20, 36, 34, horizon_glow, fill=True)

# distant skyline (dark towers with tiny lit windows)
for sx, sw, sh, top in [(50, 7, 22, 18), (60, 6, 30, 10), (68, 8, 26, 14), (78, 6, 18, 20)]:
    bg.rect(sx, top, sw, sh, buildingL, fill=True)
    for wx in range(sx + 1, sx + sw - 1, 3):
        for wy in range(top + 2, top + sh - 2, 4):
            if (wx * 7 + wy * 13) % 5 == 0:
                bg.set(wx, wy, window_warm)

# ---------- ground / street ----------
bg.poly([(40, 128), (62, 50), (66, 50), (88, 128)], street, fill=True)

# perspective seams
for t in [0.25, 0.45, 0.7]:
    y = 50 + (128 - 50) * t
    xl = 62 - (62 - 40) * t
    xr = 66 + (88 - 66) * t
    bg.line(int(62 + (64 - 62) * t), int(y), int(64), int(y), street_line)
bg.line(63, 50, 40, 128, street_line)
bg.line(65, 50, 88, 128, street_line)

# ---------- left building ----------
bg.poly([(0, 0), (0, 128), (40, 128), (62, 50), (50, 0)], buildingL, fill=True)
bg.line(50, 0, 62, 50, edgeL)
bg.line(62, 50, 40, 128, edgeL)

# left windows
for row, y in [(28, 26), (52, 40), (74, 56)]:
    for x in range(10, 44, 10):
        if (x + y) % 20 < 10:
            bg.rect(x, y, 6, 9, window_cool if (x + y) % 3 else window_warm, fill=True)
        else:
            bg.rect(x, y, 6, 9, window_dark, fill=True)

# ---------- right building ----------
bg.poly([(128, 0), (128, 128), (88, 128), (66, 50), (78, 0)], buildingR, fill=True)
bg.line(78, 0, 66, 50, edgeR)
bg.line(66, 50, 88, 128, edgeR)

# right windows
for row, y in [(26, 28), (48, 42), (70, 58)]:
    for x in range(84, 118, 10):
        if (x + y) % 20 < 10:
            bg.rect(x, y, 6, 9, window_warm if (x + y) % 3 else window_cool, fill=True)
        else:
            bg.rect(x, y, 6, 9, window_dark, fill=True)

# ---------- neon signs: left RAMEN ----------
bg.rect(6, 12, 40, 18, sign_bg, fill=True)
bg.rect(6, 12, 40, 18, neon_pink, fill=False)
bg.text(10, 16, "RAMEN", neon_pink, font="5x7")

# kanji accent under RAMEN (12px CJK)
bg.text(8, 34, "雨", neon_cyan, font="12px")

# neon bowl icon
bg.circle(24, 60, 9, neon_cyan, fill=False)
bg.line(16, 50, 22, 56, neon_cyan)
bg.line(32, 50, 26, 56, neon_cyan)

# ---------- neon signs: right BAR ----------
bg.rect(84, 10, 38, 16, sign_bg, fill=True)
bg.rect(84, 10, 38, 16, neon_cyan, fill=False)
bg.text(88, 14, "BAR", neon_cyan, font="5x7")

# CJK vertical-ish sign
bg.rect(92, 30, 26, 28, sign_bg, fill=True)
bg.rect(92, 30, 26, 28, neon_purple, fill=False)
bg.text(94, 34, "喫", neon_purple, font="12px")
bg.text(94, 46, "茶", neon_purple, font="12px")

# circular sign on right wall
bg.ellipse(103, 70, 14, 10, sign_bg, fill=True)
bg.ellipse(103, 70, 14, 10, neon_orange, fill=False)
bg.ellipse(103, 70, 9, 6, neon_yellow, fill=False)

# ---------- power cables ----------
cable_col = C('#241c3c', 'cable')
cable_hi  = C('#3d2f5e', 'cable_hi')
bg.path("M 50 6 Q 64 22 78 8", cable_col, fill=False)
bg.path("M 47 26 Q 64 42 81 24", cable_hi, fill=False)
bg.path("M 45 46 Q 64 62 83 44", cable_col, fill=False)
bg.path("M 42 66 Q 64 82 86 64", cable_hi, fill=False)

# ---------- vending machines (left) ----------
def vending(x, y, w, h, sign_col, accent_col):
    bg.rect(x, y, w, h, machine_bg, fill=True)
    bg.rect(x, y, w, h, sign_col, fill=False)
    bg.rect(x + 2, y + 2, w - 4, 10, sign_col, fill=False)
    bg.text(x + 4, y + 3, "24H", sign_col, font="5x7")
    # glowing front panel
    bg.rect(x + 3, y + 15, w - 6, 10, accent_col, fill=False)
    bg.rect(x + 5, y + 17, w - 10, 6, sign_col, fill=False)
    # drink rows
    for i in range(3):
        cy = y + 30 + i * 8
        for j in range(3):
            bg.rect(x + 3 + j * 6, cy, 4, 6, [neon_pink, neon_cyan, neon_yellow, neon_green][(i + j) % 4], fill=True)

vending(6, 92, 20, 32, neon_pink, neon_cyan)
vending(26, 94, 20, 30, neon_cyan, neon_purple)

# ---------- puddles and reflections ----------
bg.ellipse(58, 112, 15, 6, puddle_base, fill=True)
bg.line(46, 110, 70, 109, pink_ref)
bg.line(48, 114, 70, 113, cyan_ref)
bg.line(50, 118, 68, 117, neon_pink)

bg.ellipse(86, 119, 13, 5, puddle_base, fill=True)
bg.line(75, 117, 97, 118, purple_ref)
bg.line(77, 121, 97, 122, neon_cyan)

bg.ellipse(44, 125, 18, 5, puddle_base, fill=True)
bg.line(28, 123, 60, 124, yellow_ref)
bg.line(30, 126, 60, 127, neon_yellow)

# vertical neon reflections on wet street
for x, col, y0 in [(42, neon_pink, 98), (48, neon_cyan, 98), (98, neon_purple, 96), (104, neon_orange, 96)]:
    for i in range(6):
        bg.line(x + (i % 2), y0 + i * 5, x + 2 + (i % 2), y0 + i * 5 + 3, col)

# ---------- person layer ----------
person = new_canvas(W, H, background=None, name='person')
umbrella_tint = person.color((185, 235, 255, 90), 'umbrella_tint')

# transparent umbrella canopy (tint, then structure)
person.path("M 50 80 Q 64 54 78 80 L 50 80 Z", umbrella_tint, fill=True)
person.line(64, 68, 64, 96, silhouette)
person.path("M 50 80 Q 64 54 78 80", silhouette, fill=False)
person.line(50, 80, 78, 80, silhouette)
person.line(64, 68, 52, 80, silhouette)
person.line(64, 68, 64, 80, silhouette)
person.line(64, 68, 76, 80, silhouette)
person.path("M 52 78 Q 64 58 76 78", umbrella_light, fill=False)

# head
person.circle(64, 89, 4, silhouette, fill=True)

# coat / body
person.poly([(52, 97), (76, 97), (78, 116), (50, 116)], silhouette, fill=True)

# separated legs
person.rect(55, 116, 6, 10, silhouette, fill=True)
person.rect(68, 116, 6, 10, silhouette, fill=True)

# arms
person.line(56, 101, 64, 95, silhouette)
person.line(72, 101, 75, 113, silhouette)

# neon rim light on the silhouette for strong contrast
person.line(52, 98, 50, 116, neon_pink)
person.line(76, 98, 78, 116, neon_cyan)
person.line(55, 116, 55, 126, neon_pink)
person.line(73, 116, 73, 126, neon_cyan)

# ---------- rain layer ----------
rain = new_canvas(W, H, background=None, name='rain')
rain_alpha = rain.color((150, 180, 255, 80), 'rain_alpha')
random.seed(7)
for _ in range(150):
    x = random.randint(3, 127)
    y = random.randint(0, 118)
    length = random.randint(4, 10)
    dx = random.choice([-3, -2, -2, -1])
    rain.line(x, y, x + dx, y + length, rain_alpha)

# ---------- composite ----------
final = flatten([bg, rain, person], name='final')

print(bg.stats_text())
print(rain.stats_text())
print(person.stats_text())
print(final.stats_text())

finish(final)
