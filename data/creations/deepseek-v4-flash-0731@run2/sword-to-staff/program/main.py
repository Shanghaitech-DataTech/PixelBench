from pixelbench_api import *

out = input_canvas.copy(name='output')

GOLD = 18      # sword blade gold
OUTLINE = 2    # dark outline
WHITE = 1      # sky/background
SKIN = 9       # hand skin
SLEEVE = 22    # tunic/sleeve colour under the sword tip
WOOD = 16      # brown wood
SKIN_B = 9

# --- locate the gold sword ---
gold = [(x, y) for y in range(64) for x in range(64) if out.get(x, y) == GOLD]

def replace_colour(x, y):
    # the lower gold cluster lies over the tunic/sleeve; the rest lies over sky
    return SLEEVE if y >= 42 else WHITE

# erase the blade: gold pixels, plus dark outline pixels touching them
for (x, y) in gold:
    out.set(x, y, replace_colour(x, y))
for y in range(64):
    for x in range(64):
        if out.get(x, y) == OUTLINE:
            if any(abs(x - gx) + abs(y - gy) == 1 for (gx, gy) in gold):
                out.set(x, y, replace_colour(x, y))

# --- draw the staff held in the right hand (hand skin sits at x40-43, rows 35-37) ---
# cap (knob) on top
for y in (12, 13):
    out.set(43, y, OUTLINE); out.set(44, y, OUTLINE)
for y in (14, 15):
    out.set(42, y, OUTLINE); out.set(43, y, WOOD); out.set(44, y, WOOD); out.set(45, y, OUTLINE)
# rod
for y in range(16, 49):
    out.set(42, y, OUTLINE); out.set(43, y, WOOD); out.set(44, y, WOOD); out.set(45, y, OUTLINE)
# the hand gripping the rod: redraw the hand skin over the rod
for y in range(35, 38):
    for x in range(40, 44):
        out.set(x, y, SKIN)

# small dark grip line below the hand keeps the hand reading as holding the staff
for y in (38, 39, 40):
    out.set(39, y, OUTLINE)
    out.set(46, y, OUTLINE)

print("gold removed:", len(gold))
print(out.stats_text())
save('sword_to_staff', out)
finish(out)
