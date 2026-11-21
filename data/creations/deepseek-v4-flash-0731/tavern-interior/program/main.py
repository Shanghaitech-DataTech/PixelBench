#!/usr/bin/env python3
# 64x64 cozy tavern interior — warm nighttime lighting, smoky air, dark outlines
from pixelbench_api import new_canvas, finish
import random

INK     = "#1e1610"
CEIL    = "#2b1d12"
WALL    = "#382419"
WALL2   = "#402a1c"
PLANK_D = "#452c1c"
SMOKE   = "#5d4633"
HAZE    = "#75604a"
HAZE2   = "#8c7559"
WOOD_D  = "#3c2614"
WOOD_M  = "#5a3b1e"
WOOD_H  = "#96602e"
WOOD_T  = "#b4733a"
BAND    = "#201610"
FLOOR1  = "#4a2f17"
FLOOR2  = "#3a2412"
BARREL  = "#6b4522"
BARREL_H = "#8a5a2d"
BARREL_D = "#462c15"
STOOL   = "#6e4522"
STOOL_H = "#8c5c2e"
STOOL_D = "#3c2413"
LAMP    = "#e8a72e"
LAMP_D  = "#9c6c1c"
GLOW_HI = "#ffe37f"
GLOW_M  = "#ffc94d"
GLOW_L  = "#d9992d"
GLOW_X  = "#a06a1e"
BOT_G   = "#2e6b31"; BOT_GH = "#4d8f47"
BOT_A   = "#b06e1a"; BOT_AH = "#d9a03a"
BOT_B   = "#31548f"; BOT_BH = "#5d86c4"
BOT_R   = "#8f2a1f"; BOT_RH = "#c2553a"
CORK    = "#9d6f3e"
GLASS   = "#d3e2e6"
GLASS_D = "#a0b8c4"
GLASS_W = "#f2f8fa"

c = new_canvas(64, 64, name="tavern")


def bottle(x, base_y, body, hi, tall=True):
    h = 6 if tall else 4
    y0 = base_y - h + 1
    c.rect(x, y0, 5, h, body)
    c.rect(x + 1, y0, 1, h, hi)
    nh = 3
    c.rect(x + 1, y0 - nh, 3, nh, body)
    c.rect(x + 2, y0 - nh, 1, nh, hi)
    c.rect(x + 1, y0 - nh - 1, 3, 1, CORK)
    c.rect(x, y0, 5, h, INK, fill=False)
    c.rect(x + 1, y0 - nh, 3, nh, INK, fill=False)


def sbottle(x, base_y, body, hi):
    y0 = base_y - 3
    c.rect(x, y0, 4, 4, body)
    c.rect(x + 1, y0, 1, 4, hi)
    c.rect(x + 1, y0 - 2, 2, 2, body)
    c.rect(x + 1, y0 - 2, 2, 2, INK, fill=False)
    c.rect(x, y0, 4, 4, INK, fill=False)


def glass(x, y):
    c.rect(x, y, 4, 5, GLASS_D)
    c.rect(x + 1, y, 2, 5, GLASS)
    c.rect(x + 1, y, 1, 2, GLASS_W)
    c.rect(x + 1, y + 2, 2, 3, GLASS)
    c.rect(x, y, 4, 5, INK, fill=False)


def barrel(x, y, w, h):
    c.rect(x, y, w, h, BARREL)
    c.rect(x + 1, y, 1, h, BARREL_H)
    c.rect(x + w - 2, y, 2, h, BARREL_D)
    c.rect(x, y + 2, w, 2, BAND)
    c.rect(x, y + h - 5, w, 2, BAND)
    c.rect(x + 2, y - 2, w - 4, 2, BARREL_H)
    c.rect(x, y, w, h, BAND, fill=False)


def lamp(cx):
    for i in range(14):
        c.set(cx, 4 + i, BAND)
    c.rect(cx - 2, 18, 5, 2, LAMP_D)
    c.rect(cx - 3, 20, 7, 3, LAMP)
    c.rect(cx - 4, 23, 9, 2, LAMP)
    c.rect(cx - 2, 18, 5, 7, INK, fill=False)
    c.rect(cx - 4, 23, 9, 2, INK, fill=False)
    c.rect(cx - 2, 20, 6, 4, GLOW_M)


def stool(cx):
    c.ellipse(cx, 29, 5, 2, STOOL)
    c.ellipse(cx, 28, 4, 1, STOOL_H)
    c.rect(cx - 5, 31, 11, 1, STOOL)
    c.line(cx - 5, 33, cx - 5, 57, STOOL_D)
    c.line(cx + 5, 33, cx + 5, 57, STOOL_D)
    c.rect(cx - 5, 41, 11, 1, STOOL)
    c.rect(cx - 5, 51, 11, 1, STOOL)
    c.rect(cx - 7, 57, 3, 1, STOOL_D)
    c.rect(cx + 5, 57, 3, 1, STOOL_D)


# ---------- build the scene ----------
c.rect(0, 0, 64, 64, CEIL)
c.rect(0, 0, 64, 1, INK)
c.rect(0, 3, 64, 1, BAND)

# back wall rows 4..45
c.rect(0, 4, 64, 42, WALL)
for x in range(8, 64, 8):
    c.rect(x, 4, 1, 42, PLANK_D)

# early smoky air on the wall
rng = random.Random(21)
for _ in range(90):
    c.set(rng.randrange(2, 62), rng.randrange(5, 26), rng.choice([SMOKE, WALL2, SMOKE]))
for (wx, wy, wl) in [(4, 6, 9), (13, 5, 10), (24, 7, 11), (36, 6, 10), (48, 8, 9), (56, 5, 8)]:
    for i in range(wl):
        c.set(wx + i, wy + (i // 2) % 3, SMOKE)

# main bottle shelf rows 10..12
c.rect(0, 10, 64, 3, WOOD_D)
c.rect(0, 10, 64, 1, WOOD_H)
c.rect(0, 12, 64, 1, BAND)
for (bx, bc, bh) in [(3, BOT_G, BOT_GH), (10, BOT_A, BOT_AH), (24, BOT_B, BOT_BH),
                   (38, BOT_G, BOT_GH), (51, BOT_R, BOT_RH), (57, BOT_B, BOT_BH)]:
    bottle(bx, 10, bc, bh)

# side shelves rows 19..21
c.rect(2, 19, 12, 3, WOOD_D)
c.rect(2, 19, 12, 1, WOOD_H)
c.rect(2, 21, 12, 1, BAND)
c.rect(50, 19, 12, 3, WOOD_D)
c.rect(50, 19, 12, 1, WOOD_H)
c.rect(50, 21, 12, 1, BAND)
for (bx, bc, bh) in [(4, BOT_A, BOT_AH), (8, BOT_B, BOT_BH), (11, BOT_G, BOT_GH),
                   (52, BOT_B, BOT_BH), (56, BOT_R, BOT_RH), (59, BOT_G, BOT_GH)]:
    sbottle(bx, 19, bc, bh)

# floor rows 46..63
c.rect(0, 46, 64, 18, FLOOR1)
for y in (49, 53, 57, 61):
    c.rect(0, y, 64, 1, FLOOR2)
for (jx, jy) in [(8, 47), (24, 47), (42, 47), (58, 47), (16, 51), (38, 51),
                (6, 55), (30, 55), (52, 55), (12, 59), (26, 59), (44, 59),
                (20, 61), (34, 61), (50, 61)]:
    c.rect(jx, jy, 3, 1, FLOOR2)

# barrels at the bar ends
barrel(0, 47, 14, 15)
barrel(48, 47, 14, 15)

# lamp halos — warm pools of light on the back wall behind the counter
for cx in (18, 32, 46):
    c.circle(cx, 32, 10, GLOW_X)
    c.circle(cx, 32, 7, GLOW_L)
    c.circle(cx, 32, 4, GLOW_M)
    c.circle(cx, 32, 2, GLOW_HI)

# wooden bar counter rows 30..46, x 9..54
c.rect(9, 30, 46, 5, WOOD_M)
c.rect(9, 30, 46, 2, WOOD_T)
c.rect(9, 34, 46, 1, WOOD_H)
c.rect(9, 35, 46, 11, WOOD_M)
for px in range(13, 56, 7):
    c.rect(px, 35, 1, 11, WOOD_D)
c.rect(9, 44, 46, 1, WOOD_D)
c.rect(9, 46, 46, 1, BAND)
c.rect(9, 30, 46, 17, INK, fill=False)

# bar stools in front of the bar
for cx in (18, 32):
    stool(cx)
    lamp(cx)
stool(44)
lamp(43)

# glasses on the bar counter
glass(14, 28)
glass(30, 29)
glass(47, 28)

# warm light reflected on the wood below each lamp (in front of stools)
for cx in (18, 32, 43):
    c.ellipse(cx, 31, 4, 1, GLOW_M)
    c.rect(cx - 2, 31, 5, 1, GLOW_HI)

# curling smoke drifting near the lamps
rng2 = random.Random(7)
for _ in range(70):
    c.set(rng2.randrange(4, 60), rng2.randrange(7, 24),
          rng2.choice([HAZE, HAZE, HAZE2]) if rng2.random() < 0.6 else rng2.choice([SMOKE, WALL2]))

print(c.stats_text())
finish(c)
