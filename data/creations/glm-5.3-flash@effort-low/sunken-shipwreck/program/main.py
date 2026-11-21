from pixelbench_api import *

c = new_canvas(64, 64, background="#1a4a6e", name="wreck")

# water gradient bands
for y in range(0, 16):
    c.rect(0, y, 64, 1, "#1f567e")
for y in range(16, 34):
    c.rect(0, y, 64, 1, "#1a4a6e")
for y in range(34, 50):
    c.rect(0, y, 64, 1, "#163f5e")
for y in range(50, 64):
    c.rect(0, y, 64, 1, "#123452")

# light shafts
for x in range(6, 12):
    c.line(x, 0, x + 14, 30, "#2e6f96")
for x in range(30, 34):
    c.line(x, 0, x + 10, 24, "#2e6f96")

# sand floor
c.rect(0, 52, 64, 12, "#c9b47c")
c.rect(0, 52, 64, 2, "#d8c68f")
# sand dunes
c.line(0, 53, 20, 51, "#d8c68f")
c.line(40, 53, 63, 51, "#d8c68f")
# sand speckles
for (x, y) in [(8,56),(15,58),(23,55),(31,59),(38,56),(46,58),(53,55),(58,60),(4,60),(28,62)]:
    c.set(x, y, "#b39d66")

# --- shipwreck hull (half-buried, tilted) ---
HULL = "#6b4a2a"
HULL_D = "#4a3118"
HULL_L = "#8a6538"
# hull body: tilted arc, buried at bottom
c.poly([(14,52),(12,44),(13,38),(18,32),(26,28),(36,27),(45,30),(51,36),(54,44),(54,52),(46,52),(46,44),(44,38),(38,33),(30,32),(24,35),(20,40),(20,52)], HULL)
# deck edge highlight
c.line(18,32,26,28, HULL_L)
c.line(26,28,36,27, HULL_L)
c.line(36,27,45,30, HULL_L)
# planks
c.line(14,44,20,44, HULL_D)
c.line(13,40,19,39, HULL_D)
c.line(16,36,22,33, HULL_D)
c.line(44,34,48,38, HULL_D)
c.line(46,40,50,44, HULL_D)
c.line(47,47,51,50, HULL_D)
# ribs (corroded dark lines)
c.line(22,52,23,36, HULL_D)
c.line(28,52,29,31, HULL_D)
c.line(34,52,34,31, HULL_D)
c.line(40,52,41,33, HULL_D)

# broken mast
c.line(30,28,33,12, "#5a3d20")
c.line(31,28,34,12, "#6b4a2a")
# crossbeam remnant
c.line(26,18,36,16, "#5a3d20")
# tattered sail
c.poly([(27,17),(33,16),(32,23),(29,22)], "#b8c4c0")
c.set(30,20, "#8fa09c")

# crow's nest stub
c.rect(32,10,3,2, HULL_D)

# rust / corrosion patches on hull
for (x,y) in [(17,42),(18,43),(24,38),(25,39),(31,36),(38,34),(39,35),(43,40),(44,41),(48,46),(21,48),(35,49)]:
    c.set(x, y, "#7a4a2e")
for (x,y) in [(18,42),(25,38),(39,34),(44,40)]:
    c.set(x, y, "#9c5a30")

# portholes
c.circle(27,42,1, "#2a3f4a")
c.circle(36,40,1, "#2a3f4a")

# --- coral (left) ---
c.poly([(4,52),(3,46),(5,44),(6,47),(7,42),(8,46),(9,44),(10,48),(10,52)], "#e0705a")
c.poly([(2,52),(2,49),(3,50),(3,52)], "#e0705a")
c.set(5,45, "#f2937a")
c.set(7,43, "#f2937a")

# small coral right
c.poly([(58,52),(57,48),(59,46),(60,49),(61,47),(62,52)], "#d88a5a")
c.set(59,47, "#f0a878")

# --- seaweed ---
def weed(x, base, h, col):
    for i in range(h):
        y = base - i
        xx = x + (i // 3 if (i // 3) % 2 == 0 else -(i // 3) % 1)
        c.set(x + (1 if (i//4)%2 else 0) - (1 if (i//4)%3==2 else 0), y, col)
for (x, h) in [(12,9),(14,12),(16,7),(50,8),(52,11),(54,6),(22,5)]:
    weed(x, 52, h, "#3f8a4a")
for (x, h) in [(13,10),(51,9),(15,8),(53,7)]:
    weed(x, 52, h, "#5aa85f")

# --- school of fish ---
FISH = "#7ec8e8"
FISH_D = "#4a90b8"
def fish(x, y, flip=False):
    d = -1 if flip else 1
    c.set(x, y, FISH)
    c.set(x+d, y-1, FISH)
    c.set(x+d, y, FISH)
    c.set(x+d, y+1, FISH)
    c.set(x+2*d, y, FISH)
    c.set(x+2*d, y-1, FISH_D if not flip else FISH)
    c.set(x+3*d, y, FISH)
    # tail
    c.set(x-d, y, FISH_D)
    c.set(x-2*d, y-1, FISH_D)
    c.set(x-2*d, y+1, FISH_D)
    # eye
    c.set(x+2*d, y-0, "#12303e")

# arc of fish swimming right, above hull
pts = [(8,20),(14,17),(20,15),(26,14),(32,15),(38,17),(44,20)]
for i,(x,y) in enumerate(pts):
    fish(x, y)
# second smaller group lower-left
for (x,y) in [(6,30),(12,28),(18,27)]:
    fish(x, y, flip=False)

# bubbles
for (x,y) in [(24,8),(27,5),(40,10),(43,6),(10,12),(13,9),(55,14),(58,11),(20,38),(50,30)]:
    c.set(x, y, "#a8d8ec")
c.set(27,4, "#a8d8ec")
c.set(43,5, "#a8d8ec")

print(c.stats_text())
save("sunken-shipwreck", c)
finish(c)
