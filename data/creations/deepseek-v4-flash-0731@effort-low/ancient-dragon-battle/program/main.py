from pixelbench_api import *
import random

W = H = 256
c = new_canvas(W, H)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

# ---- Sky: dramatic sunset, banded to limit colors ----
sky_bands = [
    (0,    (24,14,52)),
    (30,   (50,22,66)),
    (55,   (88,34,62)),
    (78,   (138,50,52)),
    (100,  (196,74,44)),
    (122,  (242,118,44)),
    (142,  (255,178,72)),
    (158,  (255,228,150)),
]
for i in range(len(sky_bands) - 1):
    y0, col0 = sky_bands[i]
    y1, col1 = sky_bands[i+1]
    mid = (y0 + y1)//2
    for y in range(y0, y1):
        c.rect(0, y, W, 1, col0 if y < mid else col1)

# ---- Sun ----
c.circle(168, 150, 24, (255, 218, 138))
c.circle(168, 150, 17, (255, 236, 178))
c.circle(168, 150, 10, (255, 250, 222))
c.circle(168, 150, 5, (255, 255, 244))

# ---- strip clouds ----
random.seed(2)
cloud_c = [(120,74,116),(160,94,110),(205,120,100),(240,170,120)]
for _ in range(34):
    x = random.randint(0, 250)
    y = random.randint(30, 120)
    w = random.randint(10, 30)
    c.rect(x, y, w, 2, random.choice(cloud_c))

# ---- Distant mountains ----
c.poly([(0,178),(20,156),(38,168),(58,148),(80,166),(104,152),
        (128,168),(150,158),(180,170),(205,154),(232,168),(255,162),(255,180),(0,180)], (26,17,36))

# ---- Ground: banded progression ----
ground_bands = [(178,(104,80,60)),(200,(84,64,48)),(222,(62,48,38)),(246,(44,34,28))]
for i in range(len(ground_bands)-1):
    y0, col0 = ground_bands[i]
    y1, col1 = ground_bands[i+1]
    mid = (y0+y1)//2
    for y in range(y0, y1):
        c.rect(0, y, W, 1, col0 if y < mid else col1)
for y in range(ground_bands[-1][0], 256):
    c.rect(0, y, W, 1, ground_bands[-1][1])

# ---- Siege towers ----
def siege_tower(tx, tw, top, bot):
    wood = (100, 72, 46)
    dark = (60, 40, 28)
    c.rect(tx, top, tw, bot-top, (14,10,16))
    c.rect(tx+1, top+1, tw-2, bot-top-2, wood)
    c.rect(tx+2, top+2, 1, bot-top-4, dark)
    c.rect(tx+tw-3, top+2, 1, bot-top-4, dark)
    c.rect(tx-1, top-6, tw+2, 7, (14,10,16))
    c.rect(tx, top-6, tw, 5, (126,96,62))
    c.line(tx+1, top+8, tx+tw-2, bot-4, dark)
    c.line(tx+tw-2, top+8, tx+1, bot-4, dark)
siege_tower(78, 26, 118, 188)
siege_tower(16, 24, 138, 196)

# ---- Castle ----
def castle_tower(x, y, w, h, body):
    c.rect(x, y, w, h, (14,10,16))
    c.rect(x+1, y+1, w-2, h-2, body)
    sy = y
    mx = x
    while mx < x+w:
        ml = min(5, x+w-mx)
        c.rect(mx, sy-5, ml, 5, (14,10,16))
        if ml-2 > 0:
            c.rect(mx+1, sy-4, max(ml-2,1), min(3, ml), body)
        mx += 6

keep_body = (52, 44, 60)
castle_tower(166, 112, 58, 70, keep_body)
castle_tower(182, 96, 26, 26, keep_body)
castle_tower(138, 118, 30, 64, keep_body)
castle_tower(224, 112, 28, 70, keep_body)
castle_tower(246, 126, 10, 56, keep_body)

for (wx, wy) in [(198,120),(156,130),(238,124),(174,118),(210,152),(148,142),(230,144),(192,100)]:
    c.rect(wx, wy, 3, 4, (255, 150, 60))
    c.rect(wx+1, wy+1, 1, 2, (255, 220, 140))

wall_body = (60, 64, 78)
c.rect(128, 148, 128, 32, (14,10,16))
c.rect(129, 149, 126, 30, wall_body)
c.rect(128, 148, 128, 5, (82, 86, 100))
c.rect(150, 156, 28, 24, (14,10,16))
c.rect(151, 157, 26, 22, (38, 32, 42))

# flames on towers
def flame(cx, cy):
    c.circle(cx, cy, 5, (255, 190, 70))
    c.circle(cx, cy-2, 3, (255, 120, 40))
    c.circle(cx, cy-4, 2, (255, 205, 95))
    c.circle(cx, cy-5, 1, (255, 240, 180))
flame(214, 90); flame(229, 100); flame(196, 88); flame(151, 92); flame(214, 88)
flame(140, 110); flame(250, 120); flame(245, 126)

# smoke
def smoke(cx, top, n):
    grays = [(70,66,70),(56,53,56),(44,42,44),(82,78,82),(66,62,64)]
    for i in range(n):
        cc = grays[i % 5]
        r = 3 + i*2
        x = cx - i + (i%3)
        y = top - i*4
        c.circle(x, y, r, cc)
smoke(214, 72, 9); smoke(230, 78, 7); smoke(196, 66, 4)
smoke(150, 82, 6); smoke(245, 94, 5)

# ---- Dragon ----
dragon_red = (112, 28, 32)
dragon_dark = (70, 16, 20)
dragon_light = (150, 50, 44)
c.ellipse(150, 54, 34, 12, (14,10,16))
c.ellipse(152, 53, 30, 8, dragon_red)
# tail
for (ax,ay,bx,by) in [(118,58,96,68),(96,68,78,74),(78,74,58,86)]:
    c.line(ax,ay,bx,by, dragon_red)
    c.line(ax+1,ay+1,bx+1,by+1, (14,10,16))
c.circle(52, 90, 4, dragon_dark); c.circle(52, 90, 2, dragon_red)
# neck + head
c.line(178, 50, 196, 42, dragon_red); c.line(178, 55, 196, 46, (14,10,16))
c.line(196, 42, 212, 36, dragon_red); c.line(197, 47, 213, 41, (14,10,16))
c.circle(214, 37, 6, (14,10,16)); c.circle(214, 37, 5, dragon_red)
c.circle(209, 35, 4, dragon_red)
c.line(214, 35, 224, 33, dragon_red); c.line(219, 39, 224, 38, (14,10,16))
c.set(212, 35, (255, 230, 120))
c.poly([(210,32),(214,22),(216,32)], dragon_dark)
c.poly([(218,31),(224,22),(222,31)], dragon_dark)
for sx, sy in [(160,43),(170,41),(180,45)]:
    c.poly([(sx,sy),(sx+3,sy-5),(sx+5,sy)], dragon_dark)
# wings
c.poly([(128,46),(90,12),(70,22),(58,8),(40,28),(80,36),(96,42),(118,50)], dragon_dark)
c.poly([(128,47),(94,17),(78,25),(70,15),(56,27),(84,37),(100,43),(118,50)], dragon_red)
c.poly([(128,45),(94,15),(76,23),(88,37),(118,50)], dragon_light)
c.line(94,17,118,50, dragon_dark); c.line(86,28,118,50, dragon_dark)
c.poly([(140,62),(108,42),(86,50),(70,64),(96,68),(122,64)], dragon_dark)
c.poly([(138,60),(110,45),(90,52),(78,62),(96,64),(122,62)], dragon_red)

# ---- Arrow trajectories ----
c.line(30,212,90,188, (74,56,40)); c.line(90,188,98,184, (185,165,145))
c.line(120,200,164,180, (66,50,38)); c.line(164,180,172,177, (175,155,135))
c.line(56,218,108,194, (74,56,40))
c.line(92,208,140,188, (66,50,38)); c.line(198,208,232,194, (84,66,48))
# arrows in flight (shaft + tip)
def arrow(x0,y0,x1,y1):
    c.line(x0,y0,x1,y1,(90,72,50)); c.set(x1,y1,(200,185,160))
arrow(56,214,96,196); arrow(120,198,158,182); arrow(200,210,226,200)

# flying arrows up near ramparts
arrow(170,120,200,112); arrow(204,116,230,108)

# ---- Sentries (knights on ramparts) ----
def sentry(cx, base, facing, bodyc, shieldc):
    top = base - 16
    c.line(cx+facing*4, top-6, cx+facing*4, base, (104,104,112))
    c.rect(cx-2, base-4, 5, 4, (14,10,16))
    c.rect(cx-1, base-4, 3, 3, bodyc)
    c.rect(cx-1, base-11, 3, 3, (14,10,16))
    c.rect(cx, base-10, 1, 2, (82,84,92))
    c.rect(cx-2, base-8, 3, 2, (14,10,16))
    c.rect(cx-3, base-7, 3, 5, (14,10,16))
    c.rect(cx-3, base-6, 2, 3, shieldc)
sentry(186, 164, -1, (150,152,160), (110,38,40))
sentry(176, 152, 1, (106,108,118), (68,88,128))
sentry(232, 160, 1, (150,152,160), (138,118,78))
sentry(180, 148, -1, (106,108,118), (110,38,40))
sentry(210, 154, 1, (150,152,160), (68,88,128))
sentry(168, 130, 1, (106,108,118), (110,38,40))
sentry(194, 130, -1, (150,152,160), (138,118,78))
sentry(206, 124, -1, (106,108,118), (68,88,128))
sentry(160, 146, -1, (150,152,160), (110,38,40))

# ---- Soldiers in formation on ground ----
random.seed(3)
for gx in range(16, 248, 12):
    gy = 240 + (gx % 2)*4
    shield_c = [(110,38,40),(68,88,128),(140,118,78)][gx % 3]
    rcolor = [(136,138,146),(150,152,160),(124,126,136)][gx % 3]
    top = gy - 14
    c.line(gx+4, top-6, gx+4, gy, (110,110,118))
    c.rect(gx-1, gy-4, 4, 4, (14,10,16))
    c.rect(gx, gy-4, 2, 3, rcolor)
    c.rect(gx-1, gy-9, 4, 3, (14,10,16))
    c.rect(gx, gy-8, 2, 2, (96,98,104))
    c.rect(gx-2, gy-6, 3, 2, (14,10,16))
    c.rect(gx-2, gy-6, 2, 1, shield_c)

# ---- Ground texture ----
random.seed(9)
for _ in range(900):
    x = random.randint(0, 255); y = random.randint(186, 255)
    r = random.random()
    if r < 0.45: c.set(x, y, (40, 30, 24))
    elif r < 0.8: c.set(x, y, (48, 36, 30))
# scorch near castle
for _ in range(250):
    x = random.randint(128, 255); y = random.randint(182, 210)
    c.set(x, y, (58, 44, 36))

# ---- Embers ----
random.seed(11)
for _ in range(230):
    x = random.randint(120, 255); y = random.randint(36, 205)
    c.set(x, y, random.choice([(255,200,90),(230,120,50),(180,80,40),(255,150,60)]))

# ---- Semi-transparent smoke veil ----
random.seed(5)
for _ in range(70):
    x = random.randint(10, 255); y = random.randint(58, 135)
    c.circle(x, y, random.randint(2, 6), (0,0,0,45))

print(c.stats_text())
finish(c)
