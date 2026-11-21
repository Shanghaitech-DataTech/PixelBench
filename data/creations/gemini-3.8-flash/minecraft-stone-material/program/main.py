import numpy as np

# 9 colors (<= 10 colors limit)
PALETTE = [
    "#1e1e24",  # 0: deep fissure core
    "#30303a",  # 1: crack shadow / fissure interior
    "#444450",  # 2: crevice edge / deep stone pit
    "#585865",  # 3: dark stone shadow fleck
    "#6c6c7a",  # 4: mid-dark stone cluster
    "#80808f",  # 5: base stone midtone
    "#9494a3",  # 6: light-mid stone cluster
    "#a9a9b8",  # 7: stone highlight / chipped rim
    "#c3c3d3",  # 8: sharpest chipped edge / glint
]

# Authentic Minecraft stone noise background (seamless modulo 16)
base_rows = [
    "5565544556655445",
    "5665443456765455",
    "6554455556655556",
    "5543455665445566",
    "4455566654456655",
    "4556655445566544",
    "5567654455665434",
    "6655544566765445",
    "6554455556554456",
    "5544345665544566",
    "4455556655445665",
    "4556655445556654",
    "5567654455665445",
    "5665543456765445",
    "6554455556554456",
    "5544556655445545",
]

grid = np.zeros((16, 16), dtype=int)
for y in range(16):
    for x in range(16):
        grid[y, x] = int(base_rows[y][x], 16)

def put(x, y, val):
    grid[y % 16, x % 16] = val

# Main jagged vertical fracture:
# Coordinates: (7,0)-(7,1)-(6,2)-(6,3)-(7,4)-(8,5)-(8,6)-(9,7)-(8,8)-(8,9)-(7,10)-(7,11)-(8,12)-(8,13)-(7,14)-(7,15)
put(7, 0, 0); put(8, 0, 7)
put(7, 1, 0); put(8, 1, 8); put(6, 1, 1)
put(6, 2, 0); put(7, 2, 7)
put(6, 3, 0); put(7, 3, 8); put(5, 3, 1)
put(7, 4, 0); put(8, 4, 7)
put(8, 5, 0); put(9, 5, 8); put(7, 5, 1)
put(8, 6, 0); put(9, 6, 7)

# Impact node at (9, 7) with 3D chipped rim:
put(9, 7, 0); put(10, 7, 0); put(11, 7, 8); put(9, 8, 7)
put(8, 7, 1)

# Vein continues down, oscillating left:
put(8, 8, 0); put(8, 9, 8); put(7, 8, 1)
put(8, 9, 0); put(9, 9, 7)
put(7, 10, 0); put(8, 10, 8); put(6, 10, 1)
put(7, 11, 0); put(8, 11, 7)
put(8, 12, 0); put(9, 12, 8); put(7, 12, 1)
put(8, 13, 0); put(9, 13, 7)
put(7, 14, 0); put(8, 14, 8); put(6, 14, 1)
put(7, 15, 0); put(8, 15, 7) # connects to (7, 0)!

# Branch 1 (shoots right-down from impact at 9, 7):
put(11, 7, 1); put(12, 8, 0); put(13, 8, 8)
put(13, 9, 0); put(14, 9, 7); put(12, 9, 1)
put(14, 10, 2); put(15, 10, 7) # tapers out before border!

# Branch 2 (shoots left-down from 6, 3):
put(5, 3, 1); put(4, 4, 0); put(5, 4, 8)
put(3, 4, 0); put(3, 5, 7)
put(2, 5, 0); put(2, 6, 8); put(1, 5, 1)
put(1, 6, 0); put(1, 7, 7)
put(0, 6, 0); put(0, 7, 8) # exits left at (0, 6)

# Connects on the right at (15, 6):
put(15, 6, 0); put(15, 7, 8) # enters right at (15, 6)
put(14, 6, 0); put(14, 7, 7)
put(13, 5, 1); put(13, 6, 7)
put(12, 5, 2) # tapers out!

# Secondary small rock spalls / stress fractures:
# In bottom-left (around 3, 12):
put(2, 12, 2); put(3, 12, 7)
put(3, 13, 1); put(4, 13, 0); put(5, 13, 8)
put(4, 14, 2); put(5, 14, 7)

# In top-right (around 13, 2):
put(12, 1, 2); put(13, 1, 7)
put(13, 2, 0); put(14, 2, 8); put(12, 2, 1)
put(14, 3, 1); put(14, 4, 7)

# Create final output canvas
c = new_canvas(16, 16, name="minecraft_cracked_stone")
for y in range(16):
    for x in range(16):
        c.set(x, y, PALETTE[grid[y, x]])

view(c)
finish(c)
