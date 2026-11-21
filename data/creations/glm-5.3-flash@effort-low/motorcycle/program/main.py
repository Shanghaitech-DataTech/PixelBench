from pixelbench_api import *

c = new_canvas(128, 128, name="moto")

BLACK = c.color("#141414", "black")
DGRAY = c.color("#3c3f44", "darkgray")
MGRAY = c.color("#5a5e64", "midgray")
SILVER = c.color("#b6bac0", "silver")
LSIL = c.color("#d9dce0", "lightsilver")
RED = c.color("#cc2222", "red")
WHITE = c.color("#f2f2f2", "white")

def wheel(cx, cy):
    c.circle(cx, cy, 17, BLACK)          # tire
    c.circle(cx, cy, 12, DGRAY)          # rim well
    c.circle(cx, cy, 10, MGRAY)          # rim
    # spokes
    for a in range(0, 360, 45):
        import math
        x2 = cx + int(round(9 * math.cos(math.radians(a))))
        y2 = cy + int(round(9 * math.sin(math.radians(a))))
        c.line(cx, cy, x2, y2, WHITE)
    c.circle(cx, cy, 3, SILVER)          # hub
    # tire highlights
    c.circle(cx, cy, 17, BLACK, fill=False)

wheel(34, 96)
wheel(100, 96)

# swingarm (silver) rear hub -> frame
c.line(34, 96, 60, 86, SILVER)
c.line(35, 99, 60, 89, MGRAY)

# front fork: silver, from front hub up to steering head
c.line(100, 96, 88, 60, SILVER)
c.line(97, 96, 85, 60, MGRAY)
# fork lower leg thicker
c.line(100, 96, 94, 76, LSIL)
c.line(99, 96, 93, 76, SILVER)
# handlebar
c.line(84, 58, 90, 54, BLACK)
c.line(86, 57, 91, 53, MGRAY)

# silver tubular frame
c.line(60, 86, 84, 60, SILVER)     # main spar
c.line(62, 84, 84, 58, LSIL)
c.line(58, 88, 62, 70, SILVER)     # down tube
c.line(60, 88, 66, 70, MGRAY)

# engine block + round silver cover
c.rect(56, 76, 18, 14, DGRAY)
c.circle(64, 83, 7, SILVER)
c.circle(64, 83, 4, MGRAY)
c.circle(63, 82, 1, LSIL)

# exhaust pipe (silver) sweeping back under tail
c.line(58, 92, 44, 94, SILVER)
c.line(44, 94, 36, 88, SILVER)
c.line(58, 94, 44, 96, MGRAY)
c.line(44, 96, 36, 90, MGRAY)
c.circle(36, 89, 2, LSIL)

# tail section (upswept) dark gray
c.poly([(52, 66), (30, 50), (24, 50), (22, 56), (30, 60), (48, 74)], DGRAY)
# tail light red
c.rect(22, 52, 3, 4, RED)
# seat black on top of tail
c.poly([(50, 64), (30, 49), (24, 49), (24, 51), (32, 53), (52, 68)], BLACK)

# main fairing: wide dark gray
c.poly([(50, 62), (58, 52), (72, 48), (84, 54), (88, 64), (86, 76), (78, 88), (64, 90), (54, 80), (48, 70)], DGRAY)
# red accent stripe on fairing
c.poly([(52, 66), (62, 56), (76, 54), (78, 58), (64, 60), (56, 70)], RED)
# lower cowl
c.poly([(56, 84), (70, 84), (78, 86), (76, 92), (62, 94), (56, 90)], DGRAY)
c.line(58, 90, 74, 88, RED)

# windscreen: tilted small black
c.poly([(74, 48), (84, 42), (88, 44), (86, 52), (78, 54)], BLACK)
c.line(76, 49, 85, 44, MGRAY)

# headlight hint
c.poly([(86, 58), (90, 56), (90, 62), (86, 64)], LSIL)

# front fender over front wheel
c.poly([(92, 82), (104, 84), (106, 88), (94, 86)], SILVER)

print(c.stats_text())
save("moto", c)
finish(c)
