from pixelbench_api import *

out = input_canvas.copy(name='output')

BG = 1           # white background index
OUT = 2          # dark outline #2e1f12
WOOD_L = 3       # #96613a
WOOD_D = 22      # #5a3a20
GOLD = 18        # #c9a227

# ---- 1. erase the sword (grip, gold guard, blade) ----
sword_cols = (17, 18, 19, 20, 21)
for y in range(38, 57):
    for x in range(40, 47):
        if out.get(x, y) in sword_cols:
            out.set(x, y, BG)
# floating guard outline pixels
for (x, y) in [(40, 39), (46, 39), (40, 40), (46, 40)]:
    out.set(x, y, BG)
# restore the fist's bottom outline where the grip pixel sat
out.set(43, 38, OUT)

# ---- 2. staff pole: wood at x42-43, outline at x41 and x44 ----
for y in list(range(26, 34)) + list(range(39, 57)):
    out.set(41, y, OUT)
    out.set(42, y, WOOD_L)
    out.set(43, y, WOOD_D)
    out.set(44, y, OUT)
# bottom cap
out.set(42, 57, OUT)
out.set(43, 57, OUT)

# ---- 3. gold collar band under the orb ----
for y in (24, 25):
    out.set(41, y, OUT)
    out.set(42, y, GOLD)
    out.set(43, y, GOLD)
    out.set(44, y, OUT)

# ---- 4. magic orb on top ----
GEM_D = '#2b5f9e'
GEM = '#4a90d9'
GEM_L = '#bfe3f2'
out.circle(42, 19, 4, OUT, fill=True)
out.circle(42, 19, 3, GEM_D, fill=True)
out.circle(42, 19, 2, GEM, fill=True)
out.set(41, 18, GEM_L)
out.set(42, 17, GEM_L)

view(out, scale=8)
finish(out)
