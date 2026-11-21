from pixelbench_api import new_canvas, finish, input_canvas

c = new_canvas(32, 32, name="rts-factory-icon")

# ---- palette ----
OUT     = c.color("#171126")
ROOF_D  = c.color("#312947")
ROOF_L  = c.color("#4a3e66")
BRICK   = c.color("#b4492a")
BRICK_L = c.color("#d05e35")
BRICK_D = c.color("#8e3a1f")
MORTAR  = c.color("#e0b078")
DOOR    = c.color("#241c36")
DOOR_L  = c.color("#3b2f55")
VENT    = c.color("#231d33")
VENT_M  = c.color("#5b5372")
VENT_D  = c.color("#181329")
CHIM    = c.color("#7d3522")
CHIM_L  = c.color("#c15a30")
CHIM_D  = c.color("#4c2417")
SMOKE    = c.color("#cfd2de")
SMOKE_D  = c.color("#a6aabc")
SMOKE_HI = c.color("#eceef4")
WARM    = c.color("#ffcf6e")
SHADOW   = c.color((10, 6, 20, 150))
SHADOW_D = c.color((10, 6, 20, 105))

for x in range(5, 27):
    c.set(x, 27, SHADOW)
for x in range(8, 25):
    c.set(x, 28, SHADOW_D)

# ---- chimney (centered) ----
c.rect(13, 4, 4, 2, OUT)
c.rect(13, 4, 4, 1, CHIM_L)
c.rect(14, 5, 2, 6, OUT)
c.rect(14, 6, 2, 4, CHIM)
c.rect(15, 6, 1, 4, CHIM_D)

# ---- smoke ----
for x in range(13, 17):
    c.set(x, 3, SMOKE_D)
for x in range(12, 18):
    c.set(x, 2, SMOKE)
for x in range(13, 17):
    c.set(x, 1, SMOKE_HI)

# ---- building ----
c.rect(4, 10, 24, 17, OUT)
c.rect(5, 11, 22, 1, ROOF_L)
c.rect(5, 12, 22, 1, ROOF_D)
c.rect(5, 13, 22, 13, BRICK)
c.rect(5, 13, 22, 1, BRICK_L)

bricks = [
    (13, [(5, 10), (11, 16), (17, 22), (23, 26)]),
    (16, [(5, 7),  (8, 13),  (14, 19), (20, 26)]),
    (19, [(5, 10), (11, 16), (17, 22), (23, 26)]),
    (22, [(5, 7),  (8, 13),  (14, 19), (20, 26)]),
    (25, [(5, 10), (11, 16), (17, 22), (23, 26)]),
]
for y0, bl in bricks:
    y1 = min(y0 + 1, 25)
    joints = [b for (a, b) in bl[:-1]]
    for a, b in bl:
        for x in range(a, b + 1):
            c.set(x, y1, BRICK_D)
        for y in range(y0, y1 + 1):
            c.set(b, y, BRICK_D)
    for xj in joints:
        for y in range(y0, y1 + 1):
            c.set(xj, y, MORTAR)
c.rect(5, 13, 1, 13, BRICK_D)

# ---- vents ----
for vx in (9, 14, 19):
    c.rect(vx, 14, 4, 4, OUT)
    c.rect(vx + 1, 15, 2, 2, VENT)
    c.rect(vx + 1, 15, 2, 1, VENT_M)
    c.rect(vx + 2, 16, 1, 1, VENT_M)
    c.rect(vx + 2, 16, 1, 1, VENT_D)

# ---- door ----
c.rect(13, 21, 6, 6, OUT)
c.rect(14, 22, 4, 4, DOOR)
c.rect(14, 22, 4, 1, DOOR_L)
c.rect(15, 23, 2, 1, WARM)

# ---- compact ASCII preview ----
sym = {
    OUT: 'O', ROOF_D: 'r', ROOF_L: 'R', BRICK: 'B', BRICK_L: 'b',
    BRICK_D: 'd', MORTAR: 'm', DOOR: 'D', DOOR_L: 'l', VENT: 'v',
    VENT_M: 's', VENT_D: 'k', CHIM: 'C', CHIM_L: 'c', CHIM_D: 'h',
    SMOKE: 'S', SMOKE_D: 's', SMOKE_HI: 'W', WARM: 'w',
}
def ch(x, y):
    i = c.get(x, y)
    if i is None:
        return '.'
    return sym.get(i, '#')
for y in range(32):
    print(''.join(ch(x, y) for x in range(32)))
print(c.stats_text())

finish(c)
