from pixelbench_api import new_canvas, finish
import math

c = new_canvas(128, 128, name="motorcycle")

# Palette
black = c.color((18, 18, 22))      # main body black
darkgray = c.color((52, 52, 60))   # fairing dark gray
darkgray2 = c.color((76, 76, 86))  # lighter dark gray
silver = c.color((168, 168, 180))  # metal parts
silver2 = c.color((210, 210, 220)) # bright silver
metal = c.color((132, 132, 144))   # darker metal
red = c.color((220, 40, 42))       # red accent
tire = c.color((26, 26, 30))       # tire
tire_dark = c.color((14, 14, 16))  # tire inner
white = c.color((238, 238, 242))   # spokes/white
chrome = c.color((226, 226, 233))  # chrome bright
midgray = c.color((100, 100, 110)) # mid gray

# ======= REAR WHEEL (left) =======
# large tire
c.circle(32, 88, 26, tire, fill=True)
c.circle(32, 88, 21, tire_dark, fill=True)
c.circle(32, 88, 16, black, fill=True)
# hub
c.circle(32, 88, 7, silver2, fill=True)
c.circle(32, 88, 4, chrome, fill=True)
# spokes - white, 12 spokes
for ang_deg in range(0, 360, 30):
    a = math.radians(ang_deg)
    for r in range(8, 15):
        x = int(32 + r * math.cos(a))
        y = int(88 + r * math.sin(a))
        if 0 <= x < 128 and 0 <= y < 128:
            c.set(x, y, white)

# ======= FRONT WHEEL (right) =======
c.circle(103, 84, 23, tire, fill=True)
c.circle(103, 84, 18, tire_dark, fill=True)
c.circle(103, 84, 13, black, fill=True)
c.circle(103, 84, 6, silver2, fill=True)
c.circle(103, 84, 3, chrome, fill=True)
for ang_deg in range(0, 360, 40):
    a = math.radians(ang_deg)
    for r in range(7, 12):
        x = int(103 + r * math.cos(a))
        y = int(84 + r * math.sin(a))
        if 0 <= x < 128 and 0 <= y < 128:
            c.set(x, y, white)

# ======= REAR SWINGARM =======
c.line(38, 78, 60, 68, darkgray2)
c.line(38, 80, 60, 72, darkgray2)

# ======= MAIN BODY / SPORT BIKE =======
# Lower body / belly pan
c.poly([(26, 62), (30, 52), (52, 46), (76, 44), (84, 50), (82, 62), (60, 70), (30, 72)], black, fill=True)

# Mid body top / fuel tank area
c.poly([(34, 46), (44, 34), (60, 30), (76, 36), (72, 46), (50, 48)], black, fill=True)
# Tank highlight (dark gray)
c.poly([(40, 40), (48, 33), (60, 32), (66, 38), (56, 44)], darkgray2, fill=True)

# Seat section (from tank rear to tail)
c.poly([(40, 44), (52, 36), (46, 34), (32, 40)], black2 := darkgray, fill=True)

# ======= TAIL (upswept) =======
# upswept tail - long swept upward
c.poly([(30, 40), (26, 30), (20, 34), (12, 44), (8, 52), (12, 56), (24, 50), (32, 44)], black, fill=True)
# tail tip cowl
c.poly([(26, 30), (30, 22), (24, 20), (18, 26), (19, 34), (24, 32)], black2, fill=True)
# seat on tail
c.poly([(12, 46), (18, 40), (26, 38), (30, 42), (24, 48), (16, 50)], darkgray2, fill=True)

# tail light - red
c.poly([(30, 22), (24, 20), (20, 24), (24, 28), (30, 26)], red, fill=True)
# small tail light strip
c.rect(16, 42, 3, 4, red, fill=True)

# ======= FRONT FAIRING =======
# Upper fairing / nose
c.poly([(70, 44), (85, 30), (101, 26), (111, 34), (107, 50), (92, 58), (78, 54), (72, 48)], darkgray, fill=True)
# lower fairing extension
c.poly([(72, 48), (86, 54), (102, 56), (108, 50), (102, 62), (84, 64), (72, 56)], black, fill=True)

# ======= WINSCREEN (tilted small black) =======
c.poly([(92, 26), (97, 18), (101, 20), (97, 30)], black2, fill=True)

# ======= FRONT COWL OPENING / headlight =======
c.poly([(99, 34), (109, 36), (108, 44), (99, 42)], silver2, fill=True)

# ======= RED ACCENTS =======
# red stripe along lower body
c.poly([(34, 60), (56, 56), (72, 58), (70, 64), (50, 66), (36, 66)], red, fill=True)
# red accent on fairing edge
c.line(82, 54, 98, 56, red)
# red stripe high on tail
c.line(28, 34, 44, 30, red)

# ======= FRAME (silver tubular) =======
# front frame tube to steering head
c.line(76, 56, 89, 48, silver)
c.line(74, 58, 87, 50, silver)
# main frame spine
c.line(60, 44, 76, 50, silver)
# frame to engine
c.line(66, 50, 66, 62, silver)
# swingarm pivot / frame welds
c.circle(60, 68, 3, silver2, fill=True)

# ======= FRONT FORK (silver) =======
# silver fork lowers
c.line(93, 52, 101, 80, silver)
c.line(91, 50, 99, 80, silver)
# fork uppers (chrome)
c.line(89, 44, 95, 56, chrome)
# triple clamp / handlebar area
c.rect(87, 42, 8, 3, chrome, fill=True)
# brake disc hint
c.rect(101, 82, 3, 3, silver2, fill=True)

# ======= HANDLEBAR =======
c.line(85, 40, 91, 44, darkgray2)
c.rect(91, 40, 5, 2, silver2, fill=True)

# ======= ENGINE (round silver gray cover) =======
# main engine cover - round
c.circle(72, 74, 16, metal, fill=True)
c.circle(72, 74, 13, silver, fill=True)
c.circle(72, 74, 8, silver2, fill=True)
c.circle(72, 74, 4, chrome, fill=True)
# cylinder head detail
c.rect(78, 58, 10, 8, metal, fill=True)
# crankcase below
c.poly([(64, 82), (72, 88), (84, 86), (82, 78)], metal, fill=True)

# ======= EXHAUST =======
# exhaust pipe from engine rear
c.poly([(58, 82), (50, 88), (40, 88), (30, 88), (30, 84), (48, 80), (58, 80)], darkgray2, fill=True)
# exhaust tip
c.rect(24, 84, 6, 4, metal, fill=True)
# red hot pipe hint
c.rect(48, 80, 6, 3, red, fill=True)

# ======= FOOTPEG hints =======
c.rect(46, 74, 5, 2, silver2, fill=True)

# ======= PEEPS through wheels - brake disc silver lines =======
# front brake disc
for ang_deg in range(0, 360, 60):
    a = math.radians(ang_deg)
    for r in range(13, 17):
        x = int(103 + r * math.cos(a))
        y = int(84 + r * math.sin(a))
        if 0 <= x < 128 and 0 <= y < 128:
            c.set(x, y, silver)

print(c.stats_text())
finish(c)
