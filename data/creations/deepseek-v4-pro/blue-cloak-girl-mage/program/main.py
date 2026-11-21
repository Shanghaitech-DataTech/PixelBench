from pixelbench_api import *

# 64x64 RPG mage sprite: girl mage, dark blue cloak, white boots, glowing amber staff.

c = new_canvas(64, 64, background=None, name="result")

# ---- palette ----
outline = c.color("#171126", "outline")
hair = c.color("#f6d282", "hair")
hair_hi = c.color("#ffe9a8", "hair_hi")
skin = c.color("#f4c8a0", "skin")
skin_shade = c.color("#dda077", "skin_shade")
cloak = c.color("#26376f", "cloak")
cloak_mid = c.color("#31448c", "cloak_mid")
cloak_hi = c.color("#465fae", "cloak_hi")
lining = c.color("#7e97d9", "lining")
boot = c.color("#eef1f6", "boot")
boot_shade = c.color("#b9bfd4", "boot_shade")
staff = c.color("#5f4228", "staff")
staff_hi = c.color("#7d5a3a", "staff_hi")
orb = c.color("#ffc04a", "orb")
orb_core = c.color("#fff3b0", "orb_core")
glow = c.color("#c4781f", "glow")
eye = c.color("#ff9e1a", "eye")
eye_dark = c.color("#8a4210", "eye_dark")
mouth = c.color("#c07a5a", "mouth")

# ---- symmetric body, left half (24 cols), mirrored to 48 cols ----
half_rows = [
    "...................HHHHH",   # 0  hair top
    ".................HHHHHHH",   # 1
    "...............HHHHHHHHH",   # 2
    ".............HHHHHHHHHHH",   # 3
    "...........HHHHHHHHHHHHH",   # 4
    "...........HHHHHHHSSSSSS",   # 5  forehead
    "...........HHHHHHSSSSSSS",   # 6
    "...........HHHHHSSSSSSSS",   # 7  eyes row
    "............HHHHSSSSSSSS",   # 8  eyes row
    "............HHHHHSSSSSSS",   # 9  eyes row
    ".............HHHHSSSSSSS",   # 10
    ".............HHHHHSSSSSS",   # 11 chin / mouth
    ".............HHHHHHSSSSS",   # 12
    "............HHHBBBBSSSSS",   # 13 shoulders / neck + hair over cloak
    "..........HHHBBBBBBBSSSS",   # 14
    "........HHBBBBBBBBBBSSSS",   # 15
    ".......HBBBBBBBBBBBBBLLL",   # 16 cloak + lining
    "......BBBBBBBBBBBBBBBLLL",   # 17
    "......BBBBBBBBBBBBBBBBLL",   # 18
    "......BBBBBBBBBBBBBBBBBL",   # 19
    "......BBBBBBBBBBBBBBBBBB",   # 20
    "......BBBBBBBBBBBBBBBBBB",   # 21
    ".....BBBBBBBBBBBBBBBBBBB",   # 22
    ".....BBBBBBBBBBBBBBBBBBB",   # 23
    "....BBBBBBBBBBBBBBBBBBBB",   # 24
    "....BBBBBBBBBBBBBBBBBBBB",   # 25
    "...BBBBBBBBBBBBBBBBBBBBB",   # 26
    "...BBBBBBBBBBBBBBBBBBBBB",   # 27
    "..BBBBBBBBBBBBBBBBBBBBBB",   # 28
    "..BBBBBBBBBBBBBBBBBBBBBB",   # 29
    ".BBBBBBBBBBBBBBBBBBBBBBB",   # 30
    ".BBBBBBBBBBBBBBBBBBBBBBB",   # 31
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 32
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 33
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 34
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 35
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 36
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 37
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 38
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 39
    "BBBBBBBBBBBBBBBBBBBBBBBB",   # 40 hem bottom
    "...............WWWWWWW..",   # 41 boots
    "...............WWWWWWW..",   # 42
    "...............WWWWWWW..",   # 43
    "...............WWWWWWW..",   # 44
    "...............WWWWWWW..",   # 45
    "...............WWWWWWW..",   # 46
    "...............WWWWWWW..",   # 47
    "...............WWWWWWW..",   # 48
    "...............WWWWWWW..",   # 49
    "...............WWWWWWW..",   # 50
    "...............WWWWWWW..",   # 51
    "...............wwwwwww..",   # 52 sole
    "...............wwwwwww..",   # 53 sole
]

full_rows = []
for r in half_rows:
    assert len(r) == 24, (len(r), r)
    full_rows.append(r + r[::-1])

art_w = 48
art_h = 54
grid = [list(row) for row in full_rows]

def setg(x, y, ch):
    if 0 <= x < art_w and 0 <= y < art_h:
        grid[y][x] = ch

# staff shaft (left side, 2px), reaches the ground
for y in range(5, 53):
    setg(3, y, 't')
    setg(4, y, 'T')

# left hand gripping staff
for y in range(28, 31):
    for x in range(4, 7):
        setg(x, y, 'S')

# right hand resting at side
for y in range(33, 36):
    for x in range(39, 43):
        setg(x, y, 'S')

# ---- draw flat art onto canvas ----
ox, oy = 8, 5
charmap = {
    'H': hair, 'S': skin, 'B': cloak, 'L': lining,
    'W': boot, 'w': boot_shade, 'T': staff, 't': staff_hi,
}
for y in range(art_h):
    for x in range(art_w):
        ch = grid[y][x]
        if ch == '.':
            continue
        if ch in charmap:
            c.set(ox + x, oy + y, charmap[ch])

# strong dark silhouette outline around every region that touches transparency
c.outline(outline)

# keep the staff shaft wood-coloured (redraw after outline so it is not swallowed)
for y in range(5, 53):
    c.set(ox + 3, oy + y, staff_hi)
    c.set(ox + 4, oy + y, staff)

# left hand gripping staff (redraw over the shaft so it stays in front)
for y in range(28, 31):
    for x in range(4, 7):
        c.set(ox + x, oy + y, skin)

# ---- glowing amber orb (drawn after outline so it stays luminous) ----
glow_cells = []
for gx in range(2, 6):
    glow_cells.append((gx, 0))
for gy in range(1, 5):
    for gx in range(1, 7):
        glow_cells.append((gx, gy))
for gx in range(2, 6):
    glow_cells.append((gx, 5))

for (gx, gy) in glow_cells:
    c.set(ox + gx, oy + gy, glow)

for gy in range(1, 5):
    for gx in range(2, 6):
        c.set(ox + gx, oy + gy, orb)
for gy in range(2, 4):
    for gx in range(3, 5):
        c.set(ox + gx, oy + gy, orb_core)

# ---- face details (on top of outline, so no dark ring) ----
# big amber anime eyes
for x in (18, 19, 20, 21):
    c.set(ox + x, oy + 7, eye_dark)
for x in (26, 27, 28, 29):
    c.set(ox + x, oy + 7, eye_dark)
for y in (8, 9):
    for x in (18, 19, 20, 21):
        c.set(ox + x, oy + y, eye)
    for x in (26, 27, 28, 29):
        c.set(ox + x, oy + y, eye)

# eye sparkles
c.set(ox + 19, oy + 8, boot)
c.set(ox + 27, oy + 8, boot)

# mouth
c.set(ox + 23, oy + 11, mouth)
c.set(ox + 24, oy + 11, mouth)

# ---- subtle shading: bangs shadow on forehead ----
for x in range(18, 30):
    c.set(ox + x, oy + 5, skin_shade)

# neck shadow under chin
for x in range(19, 29):
    c.set(ox + x, oy + 13, skin_shade)

# ---- hair shine ----
for (hx, hy) in [(20, 2), (21, 2), (19, 3), (20, 3)]:
    c.set(ox + hx, oy + hy, hair_hi)

# ---- cloak folds/highlights ----
for y in range(20, 41):
    c.set(ox + 10, oy + y, cloak_hi)
    c.set(ox + 37, oy + y, cloak_hi)
for y in range(24, 41):
    c.set(ox + 15, oy + y, cloak_mid)
    c.set(ox + 32, oy + y, cloak_mid)

# ---- boot inner shading ----
for y in range(41, 52):
    c.set(ox + 20, oy + y, boot_shade)
    c.set(ox + 27, oy + y, boot_shade)

print(c.stats_text())
finish(c)
