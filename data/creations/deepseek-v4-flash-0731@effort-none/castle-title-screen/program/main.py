from pixelbench_api import *

c = new_canvas(128, 128)

HORIZON = 80

# =========================================
# 1. SKY GRADIENT
# =========================================
sky_bands = [
    (14, 12, 46), (28, 16, 56), (48, 22, 62),
    (75, 30, 70), (108, 38, 72), (145, 46, 70),
    (185, 58, 66), (218, 82, 62), (240, 112, 60),
    (250, 146, 62),
]
for y in range(HORIZON):
    c.rect(0, y, 128, 1, sky_bands[y // 8])

# =========================================
# 2. LARGE ORANGE SUN
# =========================================
sx, sy = 94, 58
for dy in range(-24, 25):
    for dx in range(-24, 25):
        d2 = dx*dx + dy*dy
        if d2 <= 24*24:
            x, y = sx+dx, sy+dy
            if x < 0 or x >= 128 or y < 0 or y >= HORIZON:
                continue
            if d2 <= 12*12:
                col = (255, 222, 92)
            elif d2 <= 15*15:
                col = (255, 192, 73)
            elif d2 <= 18*18:
                col = (250, 158, 62)
            else:
                col = (238, 126, 60)
            c.set(x, y, col)

# =========================================
# 3. CLOUDS - layered sunset clouds
# =========================================
cld = [
    (3, 9, 5, 80, (45, 22, 62), 4),
    (6, 12, 65, 120, (35, 18, 60), 4),
    (14, 20, 25, 70, (48, 24, 62), 4),
    (18, 24, 75, 115, (60, 27, 64), 4),
    (28, 34, 10, 58, (85, 33, 68), 4),
    (33, 39, 50, 100, (105, 36, 70), 4),
    (42, 48, 20, 68, (145, 46, 68), 4),
    (48, 54, 60, 110, (175, 55, 66), 4),
    (56, 62, 30, 85, (210, 82, 62), 4),
    (64, 72, 50, 100, (235, 110, 62), 4),
    (70, 78, 20, 75, (245, 135, 62), 4),
    (72, HORIZON, 55, 100, (248, 148, 62), 4),
]
for ys, ye, xs, xe, col, gap in cld:
    for y in range(ys, min(ye, HORIZON)):
        for x in range(xs, min(xe, 128)):
            if x % gap < gap - 1:
                c.set(x, y, col)

# =========================================
# 4. SEA
# =========================================
for y in range(HORIZON, 128):
    if y < HORIZON + 8:
        col = (32, 44, 68)
    elif y < HORIZON + 18:
        col = (26, 36, 60)
    elif y < HORIZON + 30:
        col = (20, 30, 52)
    elif y < HORIZON + 42:
        col = (15, 24, 45)
    else:
        col = (12, 20, 40)
    c.rect(0, y, 128, 1, col)

# =========================================
# 5. SUN REFLECTION ON SEA
# =========================================
for y in range(HORIZON, 128):
    w = max(1, 10 - (y - HORIZON) * 6 // 10)
    if y < HORIZON + 8:
        rc = (250, 185, 80)
    elif y < HORIZON + 18:
        rc = (220, 142, 62)
    elif y < HORIZON + 34:
        rc = (175, 105, 55)
    elif y < HORIZON + 46:
        rc = (130, 75, 48)
    else:
        rc = (85, 55, 42)
    for dx in range(-w, w+1):
        x = sx + dx
        if (x + y) % 3 < 2 and 0 <= x < 128:
            c.set(x, y, rc)

# =========================================
# 6. CLIFF LANDSMASS
# =========================================
CLF_T = (50, 40, 52)
CLF_M = (34, 28, 44)
CLF_D = (22, 22, 34)
CLF_V = (16, 16, 26)

for x in range(90):
    if x < 16:
        top_y = 56
    elif x < 45:
        top_y = 55
    elif x < 72:
        top_y = 56
    else:
        top_y = 60 + (x - 70) // 4

    for y in range(top_y, 128):
        if y < top_y + 2:
            col = CLF_T
        elif y < top_y + 8:
            col = CLF_M
        elif y < top_y + 18:
            col = CLF_D
        else:
            col = CLF_V
        c.set(x, y, col)

# =========================================
# 7. CASTLE
# =========================================
CAST = (16, 12, 36)
CAST_H = (28, 22, 46)
CAST_L = (34, 27, 52)
WIN = (255, 200, 95)
WIN_D = (215, 170, 90)
FLG_R = (185, 52, 50)
FLG_L = (215, 75, 60)

# *** MAIN KEEP ***
# Grand central tower
c.rect(54, 36, 22, 22, CAST)   # main keep walls
c.rect(58, 26, 14, 10, CAST)   # upper level
c.rect(60, 18, 10, 8, CAST)    # tower top
c.poly([(60, 18), (69, 18), (64, 10)], CAST)  # spire

# Keep crenellations 
c.rect(55, 33, 4, 3, CAST)
c.rect(63, 33, 4, 3, CAST)
c.rect(55, 32, 4, 4, CAST)
c.rect(63, 32, 4, 4, CAST)
c.rect(68, 33, 3, 3, CAST)

# Keep windows
c.rect(58, 44, 2, 3, WIN)
c.rect(62, 44, 2, 3, WIN)
c.rect(60, 50, 2, 3, WIN_D)
c.rect(65, 50, 2, 3, WIN)

# Keep flag on spire
c.rect(64, 3, 2, 15, CAST)
c.rect(64, 4, 7, 4, FLG_R)
c.rect(65, 5, 5, 2, FLG_L)

# *** LEFT TOWER ***
c.rect(42, 40, 12, 18, CAST)
c.poly([(42, 40), (53, 40), (47, 28)], CAST)
c.rect(43, 36, 4, 4, CAST)
c.rect(50, 36, 4, 4, CAST)
c.rect(46, 45, 2, 3, WIN)
c.rect(48, 50, 2, 3, WIN_D)

# Left tower flag
c.rect(47, 22, 2, 8, CAST)
c.rect(47, 22, 6, 3, FLG_R)

# *** RIGHT TOWER ***
c.rect(76, 40, 12, 18, CAST)
c.poly([(76, 40), (87, 40), (81, 28)], CAST)
c.rect(77, 36, 4, 4, CAST)
c.rect(84, 36, 4, 4, CAST)
c.rect(80, 45, 2, 3, WIN)
c.rect(78, 50, 2, 3, WIN_D)

# Right tower flag
c.rect(81, 22, 2, 8, CAST)
c.rect(78, 22, 6, 3, FLG_R)

# *** Connecting walls and structures ***
# Wall between left tower and keep
c.rect(54, 46, 22, 12, CAST)

# Castle rim light (sunset facing edge)
for y in range(10, 58):
    c.set(76, y, CAST_H)
    c.set(77, y, CAST_H)
    c.set(75, y, CAST_L)
    c.set(86, y, CAST_H)

# =========================================
# 8. FOREGROUND ROCKS
# =========================================
FR1 = (14, 14, 22)
FR2 = (11, 12, 19)
FR3 = (18, 17, 25)
FR4 = (9, 10, 16)

rocks = [
    [(0, 88), (14, 84), (28, 90), (22, 98), (14, 94), (6, 102), (0, 100)],
    [(35, 100), (48, 96), (58, 103)],
    [(82, 90), (95, 87), (105, 94), (98, 100)],
    [(60, 108), (75, 102), (85, 110)],
    [(0, 100), (20, 96), (30, 103), (15, 110)],
    [(95, 102), (110, 106)],
]
for pts in rocks:
    c.poly(pts, FR1)

for y in range(100, 128):
    for x in range(0, 128):
        v = ((x * 7 + y * 5) % 7) % 5
        c.set(x, y, FR2 if v < 4 else FR3)

for y in range(108, 128):
    for x in range(0, 128):
        v = ((x * 11 + y * 7) % 9) % 6
        c.set(x, y, FR1 if v < 5 else FR4)

# =========================================
# 9. SEA shimmer
# =========================================
for y in range(HORIZON + 2, 115, 2):
    for dx in range(-15, 16):
        x = sx + dx
        if (x + y*5) % 9 < 3:
            if 0 <= x < 128:
                if y < HORIZON + 8:
                    c.set(x, y, (245, 170, 75))
                elif y < HORIZON + 20:
                    c.set(x, y, (190, 120, 56))

# Birds flying
for bx, by in [(72, 28), (78, 32), (84, 26)]:
    c.set(bx, by, (22, 15, 38))
    c.set(bx+2, by+1, (22, 15, 38))
    c.set(bx+1, by+2, (22, 15, 38))

# Cliff detail highlights
c.poly([(55, 58), (70, 56), (80, 62)], CAST)
c.poly([(80, 55), (92, 62)], CAST)

# More cliff surface texture
for x in range(0, 90):
    for y in range(65, 85):
        if x < 85 and (x * 13 + y * 9) % 11 == 0:
            c.set(x, y, CLF_D)

print(c.stats_text())
finish(c)
