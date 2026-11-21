import math

c = new_canvas(64, 64, background=None, name="weapon_set")

# ---- palette ----
K  = c.color('#2a2438', name='outline')
SL = c.color('#d7e2ec', name='steel_light')
SM = c.color('#8b9bb4', name='steel_mid')
SD = c.color('#5a6988', name='steel_dark')
WH = c.color('#ffffff', name='white')
GO = c.color('#feae34', name='gold')
GD = c.color('#c97a2b', name='gold_dark')
GY = c.color('#fee761', name='gold_light')
WD = c.color('#9a5b3c', name='wood')
WL = c.color('#c08254', name='wood_light')
WK = c.color('#6b3f2e', name='wood_dark')
RL = c.color('#e35b58', name='red_light')
RM = c.color('#ac3232', name='red')
RD = c.color('#7a2530', name='red_dark')
ST = c.color('#e8e8e8', name='string')


def px(ox, oy, x, y, col):
    c.set(ox + x, oy + y, col)


# ================= SWORD (top-left quadrant) =================
def sword(ox, oy):
    # blade outline: 45-deg diagonal, y = 30 - x, i = 10..25
    for i in range(10, 26):
        y0 = 30 - i
        for k in (-2, -1, 0, 1, 2):
            px(ox, oy, i, y0 + k, K)
    # blade steel (light top, mid, dark bottom)
    for i in range(11, 25):
        y0 = 30 - i
        px(ox, oy, i, y0 - 1, SL)
        px(ox, oy, i, y0, SM)
        px(ox, oy, i, y0 + 1, SD)
    # white shine near middle
    for i in range(15, 21):
        px(ox, oy, i, 30 - i - 1, WH)
    # tip
    px(ox, oy, 26, 3, K); px(ox, oy, 26, 4, SM); px(ox, oy, 26, 5, SD); px(ox, oy, 26, 6, K)
    px(ox, oy, 27, 3, K); px(ox, oy, 27, 4, K); px(ox, oy, 27, 5, K)
    px(ox, oy, 28, 3, K)
    # crossguard (perpendicular, direction (1,1)), through (10,20)
    for j in range(-5, 6):
        px(ox, oy, 10 + j, 20 + j, K)
        px(ox, oy, 10 + j, 21 + j, K)
    for j in range(-4, 5):
        px(ox, oy, 10 + j, 20 + j, GY)
        px(ox, oy, 10 + j, 21 + j, GO)
    # grip
    for j in range(1, 8):
        px(ox, oy, 10 - j, 20 + j, K)
        px(ox, oy, 10 - j, 21 + j, K)
    for j in range(1, 7):
        px(ox, oy, 10 - j, 20 + j, WL)
        px(ox, oy, 10 - j, 21 + j, WK)
    # pommel
    for x, y, col in [(2, 26, K), (3, 26, K), (4, 26, K),
                      (2, 27, K), (3, 27, GY), (4, 27, GO), (5, 27, K),
                      (2, 28, K), (3, 28, GY), (4, 28, GO), (5, 28, K),
                      (3, 29, K), (4, 29, K)]:
        px(ox, oy, x, y, col)


# ================= BOW (top-right quadrant) =================
def bow(ox, oy):
    # string
    for y in range(4, 29):
        px(ox, oy, 14, y, ST)
    # limbs
    for y in range(4, 29):
        x = 14 + round(8 * math.sin(math.pi * (y - 4) / 24))
        px(ox, oy, x - 1, y, K)
        px(ox, oy, x, y, WL)
        px(ox, oy, x + 1, y, WD)
        px(ox, oy, x + 2, y, K)
    # tip caps
    for x in range(13, 17):
        px(ox, oy, x, 3, K)
        px(ox, oy, x, 29, K)
    # grip wrap
    for y in range(14, 19):
        x = 14 + round(8 * math.sin(math.pi * (y - 4) / 24))
        px(ox, oy, x, y, WK)
        px(ox, oy, x + 1, y, WK)
    for y in (13, 19):
        x = 14 + round(8 * math.sin(math.pi * (y - 4) / 24))
        px(ox, oy, x, y, GO)
        px(ox, oy, x + 1, y, GO)
    # arrow shaft (drawn in front of the limb)
    for x in range(9, 26):
        px(ox, oy, x, 15, WL)
        px(ox, oy, x, 16, WK)
    # arrow head (points left)
    for x, y, col in [(5, 16, K), (6, 15, K), (6, 17, K),
                      (7, 14, K), (7, 18, K), (8, 14, K), (8, 18, K),
                      (6, 16, SM), (7, 15, SM), (7, 16, SL), (7, 17, SM),
                      (8, 15, SM), (8, 16, SM), (8, 17, SM)]:
        px(ox, oy, x, y, col)
    # fletching
    for x, y, col in [(24, 13, RM), (25, 13, RM), (26, 13, RL),
                      (25, 14, RM), (26, 14, RM),
                      (25, 18, RM), (26, 18, RM),
                      (24, 19, RM), (25, 19, RM), (26, 19, RL),
                      (26, 15, WK), (26, 16, WK)]:
        px(ox, oy, x, y, col)


# ================= SHIELD (bottom-left quadrant) =================
def shield(ox, oy):
    outer = [(6, 5), (25, 5), (25, 16), (23, 20), (19, 24), (16, 26),
             (15, 26), (12, 24), (8, 20), (6, 16)]
    rim = [(7, 6), (24, 6), (24, 16), (22, 19), (19, 23), (16, 25),
           (15, 25), (12, 23), (9, 19), (7, 16)]
    field = [(8, 7), (23, 7), (23, 15), (21, 18), (18, 22), (16, 24),
             (15, 24), (12, 22), (9, 18), (8, 15)]
    c.poly([(ox + x, oy + y) for x, y in outer], K)
    c.poly([(ox + x, oy + y) for x, y in rim], GO)
    c.poly([(ox + x, oy + y) for x, y in field], RM)
    # shading: darker low, highlight left
    for y in range(oy, oy + 32):
        for x in range(ox, ox + 32):
            v = c.get(x, y)
            yy = y - oy
            xx = x - ox
            if v == RM:
                if yy >= 18:
                    c.set(x, y, RD)
                elif xx <= 10:
                    c.set(x, y, RL)
            elif v == GO and yy >= 21:
                c.set(x, y, GD)
    # boss
    c.circle(ox + 15, oy + 11, 2, K)
    c.circle(ox + 15, oy + 11, 1, SM)
    px(ox, oy, 14, 10, WH)


# ================= BATTLE AXE (bottom-right quadrant) =================
def axe(ox, oy):
    # handle: diagonal y = 34 - x; top end disappears under the head
    for i in range(6, 22):
        y0 = 34 - i
        for k in (-2, -1, 0, 1, 2):
            px(ox, oy, i, y0 + k, K)
    for i in range(7, 21):
        y0 = 34 - i
        px(ox, oy, i, y0 - 1, WL)
        px(ox, oy, i, y0, WD)
        px(ox, oy, i, y0 + 1, WK)
    # wrap straps
    for i in (12, 17):
        y0 = 34 - i
        for k in (-1, 0, 1):
            px(ox, oy, i, y0 + k, WK)
    # blade: long curved cutting edge, short back mounted on the haft
    outer = [(20, 13), (22, 11), (27, 9), (30, 12), (31, 16), (29, 19), (25, 20), (21, 16)]
    inner = [(21, 13), (22, 12), (26, 10), (29, 12), (30, 16), (28, 18), (25, 19), (22, 16)]
    c.poly([(ox + x, oy + y) for x, y in outer], K)
    c.poly([(ox + x, oy + y) for x, y in inner], SM)
    # steel shading: dark back up-left, bright cutting edge down-right
    for y in range(8, 23):
        for x in range(19, 32):
            v = c.get(ox + x, oy + y)
            if v != SM:
                continue
            near = (c.get(ox + x + 1, oy + y), c.get(ox + x, oy + y + 1),
                    c.get(ox + x + 1, oy + y + 1), c.get(ox + x - 1, oy + y),
                    c.get(ox + x, oy + y - 1), c.get(ox + x - 1, oy + y - 1))
            if K in (near[0], near[1], near[2]) or near[0] == SD or near[1] == SD:
                px(ox, oy, x, y, SL)
            elif K in (near[3], near[4], near[5]):
                px(ox, oy, x, y, SD)
    # edge shine
    for x, y in [(28, 18), (29, 17), (29, 16)]:
        if c.get(ox + x, oy + y) in (SL, SM):
            px(ox, oy, x, y, WH)


sword(0, 0)
bow(32, 0)
shield(0, 32)
axe(32, 32)

view(c)
finish(c)
