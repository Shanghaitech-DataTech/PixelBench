from pixelbench_api import *

c = new_canvas(64, 64, background="#241a12", name="tavern")

# --- palette helpers (hex used directly) ---
WALL   = "#3a2a1c"
WALL2  = "#4a3624"
FLOOR  = "#2b1f14"
FLOOR2 = "#33261a"
WOOD   = "#6b4a2a"
WOODD  = "#4a3018"
WOODL  = "#8a6238"
STONE  = "#5a5048"

# back wall
c.rect(0, 0, 64, 40, WALL)
# wall planks
for x in range(0, 64, 8):
    c.line(x, 0, x, 39, WALL2)
# floor
c.rect(0, 40, 64, 24, FLOOR)
for y in range(42, 64, 5):
    c.line(0, y, 63, y, FLOOR2)

# --- shelf of bottles behind bar ---
c.rect(6, 10, 34, 3, WOODD)          # shelf board
# bottles on shelf
bottles = [(8,"#3f7a3a"), (11,"#7a3030"), (14,"#3a5a8a"), (17,"#8a6a2a"),
           (21,"#5a3a7a"), (24,"#3f7a3a"), (27,"#7a5030"), (30,"#3a6a5a"),
           (34,"#8a3a3a")]
for bx, col in bottles:
    c.rect(bx, 5, 2, 5, col)         # body
    c.set(bx, 4, col)
    c.rect(bx, 3, 2, 1, "#2a2018")   # neck/cork
# second small shelf
c.rect(44, 16, 16, 3, WOODD)
for bx, col in [(46,"#7a3030"), (49,"#3a5a8a"), (52,"#5a3a7a"), (55,"#3f7a3a"), (58,"#8a6a2a")]:
    c.rect(bx, 11, 2, 5, col)
    c.rect(bx, 9, 2, 2, "#2a2018")

# --- barrels left and right ---
def barrel(x, y, w, h):
    c.ellipse(x + w//2, y + h//2, w//2, h//2, WOOD)
    c.rect(x, y+1, w, h-2, WOOD)
    for i, hx in enumerate(range(x, x+w, 3)):
        c.line(hx, y+1, hx, y+h-2, WOODD if i%2 else WOODL)
    c.line(x, y+2, x+w-1, y+2, "#3a3a3a")   # metal hoops
    c.line(x, y+h-3, x+w-1, y+h-3, "#3a3a3a")

barrel(1, 30, 10, 12)
barrel(52, 32, 11, 13)
# barrel on its side on top of left barrel
c.ellipse(8, 26, 6, 4, WOOD)
c.rect(2, 22, 12, 8, WOOD)
c.line(2, 24, 13, 24, "#3a3a3a")
c.line(2, 28, 13, 28, "#3a3a3a")
c.ellipse(13, 26, 2, 4, WOODL)

# --- bar counter ---
c.rect(8, 40, 48, 8, WOOD)           # front panel
for x in range(8, 56, 6):
    c.line(x, 40, x, 47, WOODD)
c.rect(6, 38, 52, 3, WOODL)          # counter top
c.line(6, 38, 57, 38, "#a87c48")

# glasses on counter
def glass(x, y):
    c.rect(x, y, 3, 3, "#cfe3ea")
    c.rect(x, y+3, 1, 2, "#cfe3ea")
glass(14, 34)
glass(30, 34)
glass(40, 33)
# mug
c.rect(46, 33, 4, 4, "#a8783a")
c.rect(50, 34, 1, 2, "#a8783a")
c.rect(46, 32, 4, 1, "#e8d8a0")

# candle on counter
c.rect(24, 33, 2, 4, "#e8e0c8")
c.set(24, 32, "#ffd040"); c.set(25, 31, "#ffb020")

# --- bar stools in front of counter ---
def stool(x, y):
    c.rect(x, y, 7, 2, WOODL)
    c.line(x+1, y+2, x+1, y+6, WOODD)
    c.line(x+5, y+2, x+5, y+6, WOODD)
stool(14, 49)
stool(30, 50)
stool(44, 49)

# --- hanging lamps ---
def lamp(cx, cy):
    c.line(cx, 0, cx, cy-3, "#1a1410")       # chain
    c.rect(cx-1, cy-4, 2, 2, "#1a1410")      # shade top
    c.poly([(cx-4, cy+1), (cx+4, cy+1), (cx+2, cy-3), (cx-2, cy-3)], "#3a2a1c")
    c.rect(cx-2, cy+1, 4, 2, "#ffd050")      # glow
    c.set(cx-1, cy+1, "#fff0a0"); c.set(cx, cy+1, "#fff0a0")
lamp(16, 12)
lamp(40, 10)
# warm glow halos (semi-transparent)
for cx, cy, r in [(16,14,7), (40,12,7)]:
    c.circle(cx, cy, r, "#ffd05022")
    c.circle(cx, cy, r-3, "#ffd05033")

# --- dark outlines: darken silhouette edges ---
# outline around counter, barrels, stools via manual dark pixels
c.rect(6, 47, 52, 1, "#1a1008")
c.line(6, 38, 6, 47, "#1a1008")
c.line(57, 38, 57, 47, "#1a1008")
c.line(6, 38, 57, 38, "#1a1008")
c.rect(1, 29, 10, 1, "#1a1008")
c.rect(1, 41, 10, 1, "#1a1008")
c.set(0, 30, "#1a1008"); c.set(0, 40, "#1a1008")
c.line(0, 30, 0, 40, "#1a1008")
c.line(11, 30, 11, 40, "#1a1008")
c.rect(52, 31, 11, 1, "#1a1008")
c.rect(52, 44, 11, 1, "#1a1008")
c.line(52, 31, 52, 44, "#1a1008")
c.line(62, 31, 62, 44, "#1a1008")

# --- smoky atmosphere ---
import random
random.seed(7)
for _ in range(60):
    x = random.randint(0, 63); y = random.randint(0, 38)
    c.set(x, y, "#c8b8a055")
for _ in range(25):
    x = random.randint(0, 63); y = random.randint(0, 30)
    c.set(x, y, "#d8ccb833")

print(c.stats_text())
save("tavern", c)
finish(c)
