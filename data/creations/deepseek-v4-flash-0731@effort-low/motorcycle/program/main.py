import math
from pixelbench_api import *

c = new_canvas(128, 128)

black    = c.color('#121216', 'black')
darkgray = c.color('#383a3f', 'darkgray')
midgray  = c.color('#6a6c72', 'midgray')
silver   = c.color('#babcc4', 'silver')
light    = c.color('#d6d8de', 'light')
red      = c.color('#e0222c', 'red')
white    = c.color('#e8e8ee', 'white')
grayhub  = c.color('#989aa2', 'grayhub')


def wheel(cx, cy, r):
    c.circle(cx, cy, r, black)                      # tire
    c.circle(cx, cy, r - 6, 'transparent')          # clear inner tire
    c.circle(cx, cy, r - 7, silver)                 # silver rim fill
    c.circle(cx, cy, r - 11, 'transparent')         # rim inner
    inner = r - 11
    for k in range(8):
        a = math.radians(k * 45 + 22.5)
        x = cx + int(round(math.cos(a) * inner))
        y = cy + int(round(math.sin(a) * inner))
        c.line(cx, cy, x, y, white)
    c.circle(cx, cy, 5, grayhub)


# --- wheels ---
wheel(32, 84, 25)
wheel(98, 84, 25)

# --- front fender (black arc over front tire) ---
c.path("M 14 84 A 26 26 0 0 1 50 84", black, fill=False)
c.path("M 15 84 A 25 25 0 0 1 49 84", black, fill=False)

# --- main black body silhouette (tank, seat, upswept tail) ---
body = [
    (20, 58), (24, 46), (30, 44), (46, 40), (60, 42), (68, 48),
    (74, 52), (84, 52), (94, 46), (102, 36), (110, 30), (113, 33),
    (108, 38), (100, 44), (94, 54), (84, 62), (70, 68), (56, 70),
    (40, 66), (28, 62),
]
c.poly(body, black)

# --- dark gray fairing over front ---
fairing = [
    (21, 60), (25, 48), (34, 42), (50, 42), (56, 48), (54, 58),
    (46, 64), (30, 62),
]
c.poly(fairing, darkgray)

# --- small tilted black windscreen ---
c.poly([(24, 44), (32, 34), (37, 36), (30, 45)], black)

# --- red accent stripe on fairing ---
c.poly([(27, 58), (32, 50), (46, 50), (50, 55), (40, 58), (30, 59)], red)

# --- silver front fork ---
c.poly([(27, 57), (33, 56), (35, 84), (31, 84)], silver)

# --- round silver gray engine cover ---
c.circle(60, 74, 11, midgray)
c.circle(60, 74, 7, light)
c.circle(60, 74, 3, silver)

# --- silver tubular frame (front down to swingarm pivot) ---
c.line(30, 52, 72, 72, silver)
c.line(33, 49, 60, 57, silver)
c.line(60, 57, 74, 68, silver)

# --- swingarm to rear axle ---
c.line(74, 71, 97, 85, silver)

# --- red tail light at tail tip ---
c.rect(107, 31, 4, 4, red)

# final submission
print(c.stats_text())
finish(c)
