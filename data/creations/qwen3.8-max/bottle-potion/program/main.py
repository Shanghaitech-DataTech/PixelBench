from pixelbench_api import *

output = input_canvas.copy(name='output')

# palette indices (0 = transparent): 1 white, 2 black, 3 cork, 4 cork shadow,
# 5 water surface, 6 water body, 7/8 body shades, 9 shadow band, 10 body shade
RECOLOR = {
    5: '#5e2b91',   # deep surface band  (was #2f7598)
    6: '#9d64d4',   # liquid body        (was #74b8cf)
    7: '#9a5fd0',   # body shade
    8: '#9a5fd0',   # body shade
    9: '#38145c',   # dark shadow band   (was #31121d)
    10: '#a26ad8',  # body shade
}
water = set(RECOLOR)

mask = [[output.get(x, y) in water for x in range(64)] for y in range(64)]

for y in range(64):
    for x in range(64):
        i = output.get(x, y)
        if i in RECOLOR:
            output.set(x, y, RECOLOR[i])

BUBBLE = '#c9a1f0'
HILITE = '#efe3ff'
RING = '#8a4fc8'
AIR_TINT = '#e8d8fa'

def disc(cx, cy, r):
    pts = []
    for dy in range(-r, r + 1):
        for dx in range(-r, r + 1):
            if dx * dx + dy * dy <= r * r:
                pts.append((cx + dx, cy + dy))
    return pts

def liquid_bubble(cx, cy, r):
    for (x, y) in disc(cx, cy, r):
        if 0 <= x < 64 and 0 <= y < 64 and mask[y][x]:
            output.set(x, y, BUBBLE)
    if r >= 2:
        x, y = cx - 1, cy - 1
        if mask[y][x]:
            output.set(x, y, HILITE)

def air_white(x, y):
    return 0 <= x < 64 and 0 <= y < 64 and output.get(x, y) == 1 and 12 <= x <= 54 and 14 <= y <= 25

def air_bubble(cx, cy, r):
    inner = set(disc(cx, cy, max(r - 1, 0)))
    for (x, y) in disc(cx, cy, r):
        if not air_white(x, y):
            continue
        output.set(x, y, AIR_TINT if (x, y) in inner else RING)

# bubbles rising inside the liquid
liquid_bubble(14, 34, 2)
liquid_bubble(24, 31, 1)
liquid_bubble(34, 33, 2)
liquid_bubble(44, 30, 1)
liquid_bubble(18, 44, 2)
liquid_bubble(28, 48, 3)
liquid_bubble(40, 44, 2)
liquid_bubble(46, 40, 1)
liquid_bubble(22, 54, 2)
liquid_bubble(34, 57, 2)
liquid_bubble(40, 54, 1)
liquid_bubble(16, 48, 1)
liquid_bubble(30, 41, 1)
liquid_bubble(50, 40, 1)
liquid_bubble(5, 38, 1)

# fizz just under the surface
for (x, y) in [(20, 28), (30, 27), (40, 29), (12, 31), (48, 33)]:
    if mask[y][x]:
        output.set(x, y, BUBBLE)

# floating bubbles in the air space of the bottle
air_bubble(30, 20, 2)
air_bubble(23, 17, 1)
air_bubble(42, 19, 1)
air_bubble(35, 22, 1)

print(output.stats_text())
print(view(output, scale=8, margin=0))
save('bottle-potion', output)
finish(output)
