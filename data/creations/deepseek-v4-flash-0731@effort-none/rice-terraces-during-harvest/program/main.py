from pixelbench_api import *
import math

c = new_canvas(64, 64, background=None, name="terraces")

# --- Palette ---
WATER_DEEP = c.color((14, 30, 50), "water_deep")
WATER2 = c.color((60, 45, 30), "water2")
RICE_FAR1 = c.color((120, 105, 40), "rice_far1")
RICE_FAR2 = c.color((150, 130, 50), "rice_far2")
RICE_MID1 = c.color((180, 150, 60), "rice_mid1")
RICE_MID2 = c.color((205, 170, 65), "rice_mid2")
RICE_NEAR1 = c.color((225, 190, 70), "rice_near1")
RICE_NEAR2 = c.color((240, 210, 90), "rice_near2")
RICE_BRIGHT = c.color((250, 225, 110), "rice_bright")
SOIL = c.color((75, 55, 30), "soil")
SOIL_DARK = c.color((50, 38, 22), "soil_dark")
HOUSE_WALL = c.color((160, 145, 120), "house_wall")
HOUSE_ROOF = c.color((110, 70, 50), "house_roof")
SKIN = c.color((224, 178, 130), "skin")
HAT = c.color((200, 170, 90), "hat")
HAT2 = c.color((170, 140, 80), "hat2")
SHIRT = c.color((210, 80, 70), "shirt")
SHIRT2 = c.color((70, 90, 160), "shirt2")
TREE_DARK = c.color((40, 70, 40), "tree_dark")
TREE_LIGHT = c.color((70, 100, 50), "tree_light")
WATERLIGHT = c.color((100, 88, 60), "waterlight")

def contour(x, base, amp, freq, phase=0):
    return base + amp * math.sin((x / 64.0) * freq * math.pi * 2 + phase)

def draw_band(y0f, y1f, amp0, amp1, fr0, fr1, ph0, ph1, col):
    for x in range(64):
        y0 = int(round(contour(x, y0f, amp0, fr0, ph0)))
        y1 = int(round(contour(x, y1f, amp1, fr1, ph1)))
        if y0 > y1:
            y0, y1 = y1, y0
        if y0 < 0: y0 = 0
        if y1 > 63: y1 = 63
        for y in range(y0, y1 + 1):
            c.set(x, y, col)

# Base: fill whole with bright near rice; then paint progressively darker toward bottom.
c.rect(0, 0, 64, 64, RICE_NEAR2)

band_specs = [
    # (y_top, y_bottom, amp, freq, phase, color)  -- near (top) to far (bottom)
    (5, 11, 1.6, 1.4, 0.4, RICE_NEAR2),
    (11, 17, 2.0, 1.7, 0.9, RICE_NEAR1),
    (17, 23, 2.3, 2.0, 1.4, RICE_MID2),
    (23, 29, 2.6, 2.2, 1.9, RICE_MID1),
    (29, 34, 2.8, 2.4, 2.4, RICE_MID1),
    (34, 39, 3.0, 2.6, 2.9, RICE_FAR2),
    (39, 44, 3.1, 2.8, 3.3, RICE_FAR1),
    (44, 49, 3.2, 2.9, 3.7, RICE_FAR2),
    (49, 54, 3.3, 3.0, 1.2, WATER2),
    (54, 63, 3.4, 3.1, 1.6, WATER_DEEP),
]

# Draw far -> near so near overlaps.
for b in reversed(band_specs):
    y_top, y_bot, amp, freq, ph, col = b
    draw_band(y_top, y_bot, amp/2, amp, freq, freq*1.1, ph, ph+0.3, col)

# Ridge banks between bands
for idx in range(len(band_specs)):
    y_top, y_bot, amp, freq, ph, col = band_specs[idx]
    # edge at bottom of this band = bank facing viewer (above next terrace)
    for x in range(64):
        yy = int(round(contour(x, y_bot, amp, freq, ph)))
        if idx == len(band_specs)-1:
            continue
        if 0 <= yy < 64:
            c.set(x, yy, SOIL)
            if yy + 1 <= 63:
                c.set(x, yy + 1, SOIL_DARK)
            if yy - 1 >= 0:
                c.set(x, yy - 1, SOIL_DARK)
# top edge of nearest band
y_top, y_bot, amp, freq, ph, col = band_specs[0]
for x in range(64):
    yy = int(round(contour(x, y_top, amp, freq, ph)))
    if 0 <= yy < 64:
        c.set(x, yy, SOIL_DARK)

# --- Rice texture / stubble dots & harvest highlights (only on rice bands, before houses) ---
import random
random.seed(11)
for idx in range(8):
    y_top, y_bot, amp, freq, ph, col = band_specs[idx]
    for _ in range(12):
        x = random.randint(1, 62)
        y = random.randint(max(0,y_top+1), min(63,y_bot-1))
        c.set(x, y, RICE_BRIGHT)
for idx in range(8):
    y_top, y_bot, amp, freq, ph, col = band_specs[idx]
    for _ in range(5):
        x0 = random.randint(1, 58)
        for i in range(random.randint(6, 14)):
            x = x0 + i
            yy = int(round(contour(x, y_top + (y_bot-y_top)*0.7, amp, freq, ph)))
            if 0 <= yy < 64:
                c.set(x, yy, SOIL)

# --- Village houses in the distance ---
def house(cx, cy):
    for dx in range(-1, 2):
        c.set(cx+dx, cy, HOUSE_WALL)
        c.set(cx+dx, cy+1, HOUSE_WALL)
    c.set(cx, cy+2, SOIL)
    for dx in range(-1, 2):
        c.set(cx+dx, cy-1, HOUSE_ROOF)
    c.set(cx, cy-2, HAT)
    c.set(cx-1, cy-1, HOUSE_ROOF)
    c.set(cx+1, cy-1, HOUSE_ROOF)

for (hx, hy) in [(22,45),(26,46),(30,44),(34,45),(24,48),(28,49),(32,48)]:
    house(hx, hy)

# House shade
for (hx, hy) in [(22,45),(26,46),(30,44),(34,45),(24,48),(28,49),(32,48)]:
    c.set(hx, hy+2, SOIL)
    c.set(hx-1, hy+2, SOIL)
    c.set(hx+1, hy+2, SOIL)

# tiny trees near village
def tree(cx, cy, col, size=2):
    for dx in range(-size, size+1):
        for dy in range(-size, size+1):
            if abs(dx)+abs(dy) <= size:
                c.set(cx+dx, cy+dy, col)

tree(19, 43, TREE_DARK, 1)
tree(37, 43, TREE_DARK, 1)
tree(18, 49, TREE_LIGHT, 1)
tree(39, 50, TREE_LIGHT, 1)
tree(20, 52, TREE_DARK, 1)
tree(36, 52, TREE_DARK, 1)

# Water shimmer on distant terraces (bottom)
import random as _r
_r.seed(5)
for _ in range(26):
    x = _r.randint(2, 61)
    y = _r.randint(50, 62)
    c.set(x, y, WATERLIGHT)
# a light ridge contour in the deep water
for x in range(2, 62):
    yy = 58 + int(round(1.5 * math.sin((x / 64.0) * 3.0 * math.pi * 2)))
    if 0 <= yy < 64:
        c.set(x, yy, WATER2)

# --- Farmers on narrow ridges (foreground) ---
# Farmer figure drawn as a small person standing on a ridge bank.

def farmer(cx, cy, skin_t, hat_t, shirt_t):
    # head with hat
    c.set(cx, cy, hat_t)
    c.set(cx+1, cy, hat_t)
    c.set(cx+2, cy, hat_t)
    c.set(cx+1, cy+1, skin_t)
    c.set(cx+2, cy+1, skin_t)
    c.set(cx, cy+1, hat_t)
    c.set(cx+3, cy+1, hat_t)
    # shoulders / shirt
    c.set(cx, cy+2, shirt_t)
    c.set(cx+1, cy+2, shirt_t)
    c.set(cx+2, cy+2, shirt_t)
    c.set(cx+3, cy+2, shirt_t)
    # body narrowing
    c.set(cx+1, cy+3, shirt_t)
    c.set(cx+2, cy+3, shirt_t)
    # shadow
    c.set(cx+1, cy+4, SOIL_DARK)
    c.set(cx+2, cy+4, SOIL_DARK)

# Farmer 1 on the ridge near y~12 (near band boundary)
farmer(22, 11, SKIN, HAT, SHIRT)   # standing on ridge of band0/boundary housing? Place on visible ridge

# Farmer 2 further along on another ridge
farmer(38, 19, SKIN, HAT2, SHIRT2)

print(c.stats_text())
finish([c])
