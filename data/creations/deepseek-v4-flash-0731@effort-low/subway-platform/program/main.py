from pixelbench_api import *

c = new_canvas(64, 64)

def k(rgb):
    return c.color(rgb)

# ---- base tunnel background ----
tunnel = k((12, 14, 22))
c.rect(0, 0, 64, 64, tunnel)

# ---- ceiling ----
ceiling = k((56, 52, 64))
c.rect(0, 0, 64, 9, ceiling)
tileline = k((42, 40, 50))
c.line(10, 0, 10, 9, tileline)
c.line(21, 0, 21, 9, tileline)
c.line(31, 0, 31, 9, tileline)
c.line(42, 0, 42, 9, tileline)
c.line(53, 0, 53, 9, tileline)

# ---- hanging station sign (no brand names) ----
rod = k((74, 76, 84))
c.rect(24, 0, 2, 5, rod)
c.rect(36, 0, 2, 5, rod)
signbox = k((30, 48, 74))
c.rect(21, 5, 22, 5, signbox)
st_band = k((224, 232, 246))
c.rect(22, 6, 20, 1, st_band)
# abstract rail-waymark marks (not a brand): ticks
c.rect(24, 8, 3, 2, st_band)
c.rect(30, 8, 3, 2, st_band)
c.rect(36, 8, 3, 2, st_band)

# ---- upper wall (between ceiling and doors) ----
wall = k((58, 56, 66))
c.rect(0, 10, 64, 4, wall)
c.rect(0, 13, 64, 1, k((44, 42, 52)))

# ---- arriving train (farthest object, behind screen doors) ----
train = k((40, 50, 64))
c.rect(0, 14, 64, 24, train)          # body y14..37
roof = k((66, 78, 98))
c.rect(0, 14, 64, 2, roof)
stripe = k((204, 70, 58))
c.rect(0, 17, 64, 2, stripe)
win = k((176, 206, 236))
c.rect(0, 21, 64, 12, win)            # windows
# window dividers -> train cars
for x in range(0, 64, 6):
    c.rect(x, 21, 2, 12, train)
# interior light / heads light on left, brighter at right (front arriving)
inter = k((120, 150, 180))
for x in range(2, 64, 6):
    c.rect(x, 24, 1, 5, inter)
# motion streaks on train body lower half (speed)
streak = k((196, 206, 220))
for i in range(0, 62, 12):
    c.rect(i, 34, 11, 1, streak)
for i in range(4, 62, 12):
    c.rect(i, 36, 7, 1, streak)
# headlight (right end = train arriving)
glow = k((255, 252, 214))
c.rect(55, 30, 9, 6, glow)
c.rect(55, 29, 9, 1, glow)
c.rect(55, 36, 6, 1, k((255, 238, 170)))

# ---- platform screen doors ----
door = k((84, 90, 100))
c.rect(0, 14, 64, 2, door)            # top rail
c.rect(0, 38, 64, 2, door)            # bottom rail
for x in range(0, 64, 8):
    c.rect(x, 14, 2, 26, door)
c.rect(62, 14, 2, 26, door)
# faint glass reflections (vertical light streaks over train)
refl = k((150, 168, 190))
c.rect(4, 16, 1, 22, refl)
c.rect(13, 16, 1, 22, refl)
c.rect(38, 18, 1, 20, refl)
c.rect(52, 16, 1, 22, refl)

# ---- platform ----
caution = k((238, 194, 68))
c.rect(0, 40, 64, 2, caution)
c.rect(30, 40, 8, 2, tunnel)          # gap in caution line
edge = k((74, 72, 80))
c.rect(0, 42, 64, 1, edge)
floorc = k((102, 100, 110))
c.rect(0, 43, 64, 21, floorc)
# floor tile joints (depth)
joint = k((90, 88, 98))
c.line(0, 49, 63, 49, joint)
for x in range(8, 64, 16):
    c.rect(x, 43, 1, 21, joint)
# motion dashes on floor (inbound train rushing)
mdash = k((150, 152, 164))
for x in range(2, 60, 14):
    c.rect(x, 46, 9, 1, mdash)

# ---- bench (right) ----
wood = k((84, 62, 36))
wood_d = k((54, 40, 22))
# legs
c.rect(45, 56, 2, 7, wood_d)
c.rect(57, 56, 2, 7, wood_d)
# seat
c.rect(44, 53, 16, 3, wood)
# backrest
c.rect(44, 47, 2, 8, wood)
# armrest
c.rect(44, 50, 4, 2, wood)

# ---- seated passenger C (on bench, facing right) ----
sil = k((16, 18, 24))
# head
c.circle(52, 45, 4, sil)
# torso
c.rect(50, 48, 7, 6, sil)
# thigh forward
c.rect(55, 52, 7, 3, sil)
# shin down to floor
c.rect(60, 54, 2, 7, sil)
# forearm
c.rect(53, 50, 4, 2, sil)
# feet
c.rect(59, 60, 4, 2, sil)

# ---- passenger B (standing, medium, phone at ear) ----
# head
c.circle(30, 47, 3, sil)
# torso (slightly hunched)
c.rect(28, 49, 6, 7, sil)
# bag on far side
c.rect(27, 50, 2, 6, k((40, 26, 40)))
# arm holding phone up
c.rect(32, 48, 2, 3, sil)
phone = k((120, 140, 180))
c.rect(33, 45, 2, 3, phone)
# legs
c.rect(28, 56, 3, 5, sil)
c.rect(32, 56, 3, 5, sil)
# hat
c.rect(28, 44, 6, 2, sil)

# ---- passenger A (foreground, standing tall, left, largest) ----
# head
c.circle(8, 43, 4, sil)
# torso
c.rect(4, 46, 9, 9, sil)
# coat accent panel
scar = k((150, 70, 60))
c.rect(5, 48, 2, 4, scar)
# arms
c.rect(3, 47, 2, 7, sil)
c.rect(12, 47, 2, 7, sil)
# tote bag
c.rect(11, 48, 2, 6, k((66, 58, 90)))
# legs
c.rect(5, 55, 3, 7, sil)
c.rect(9, 55, 3, 7, sil)
# feet
c.rect(4, 61, 6, 2, sil)
c.rect(11, 61, 6, 2, sil)

# ---- light shaft from approaching train across platform ----
beam = k((150, 150, 150))
for step in range(0, 14):
    y = 43 + step
    c.rect(2, y, 4, 1, beam)

print(c.stats_text())
finish(c)
