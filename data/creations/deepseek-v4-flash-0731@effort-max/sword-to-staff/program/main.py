from pixelbench_api import *

c = input_canvas.copy(name="output")

WHITE = 1
GOLD = 18
OUT = 2      # dark brown outline
WOOD = 5     # #7a4a26
WOOD_L = 3   # #96613a highlight
ORB = c.color((63, 168, 232))
ORB_D = c.color((31, 111, 168))
ORB_H = c.color((160, 222, 250))

# ---- remove the old sword (blade + gold + tip), region x39..47, y33..56 ----
c.rect(39, 33, 9, 24, WHITE)

# ---- staff shaft: 4 px wide, x40..43, from y13 down to y54 ----
for y in range(13, 55):
    c.set(40, y, OUT)
    c.set(41, y, WOOD)
    c.set(42, y, WOOD_L)
    c.set(43, y, OUT)
# rounded wooden tip
c.set(41, 55, WOOD)
c.set(42, 55, WOOD_L)
c.set(41, 56, OUT)
c.set(42, 56, OUT)

# ---- crystal orb on top ----
c.set(41, 6, ORB)
c.set(42, 6, ORB)
c.set(43, 6, ORB)
for y in (7, 8):
    c.set(40, y, ORB)
    c.set(41, y, ORB)
    c.set(42, y, ORB)
    c.set(43, y, ORB)
    c.set(44, y, ORB)
c.set(40, 9, ORB)
c.set(41, 9, ORB)
c.set(42, 9, ORB)
c.set(43, 9, ORB)
c.set(44, 9, ORB)
c.set(40, 10, ORB)
c.set(41, 10, ORB)
c.set(42, 10, ORB)
c.set(43, 10, ORB)
c.set(41, 11, ORB)
c.set(42, 11, ORB)
c.set(43, 11, ORB)
# orb shading + shine
c.set(41, 7, ORB_H)
c.set(42, 6, ORB_H)
c.set(41, 10, ORB_D)
c.set(44, 10, ORB_D)

# ---- gold band under the orb ----
c.set(40, 12, OUT)
c.set(41, 12, GOLD)
c.set(42, 12, GOLD)
c.set(43, 12, OUT)

# ---- hand closes around the staff ----
c.set(39, 44, 13)
c.set(39, 45, 15)
c.set(39, 46, 25)
c.set(39, 47, 26)
c.set(39, 48, 26)
c.set(39, 49, 16)
c.set(39, 50, 16)
c.set(39, 51, 26)
c.set(39, 52, 26)
c.set(40, 46, 26)
c.set(40, 47, 25)

print(c.stats_text())
finish(c)
