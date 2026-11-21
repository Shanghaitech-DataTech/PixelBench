from pixelbench_api import *

# 8-color palette for authentic Minecraft dirt material
PALETTE = [
    "#402c1b", # 0: deepest fissure / pit
    "#4f3722", # 1: dark crevice / pebble shadow
    "#5e432a", # 2: dark midtone
    "#6f4f32", # 3: midtone brown
    "#7f5b3a", # 4: base dirt tone
    "#8f6742", # 5: light clod body
    "#a1754c", # 6: pebble highlight
    "#b58558", # 7: bright grit speckle
]

# 16x16 seamless dirt texture map
GRID = [
    "3232124433300214",
    "2212223344312233",
    "3433233132424323",
    "4423333332323333",
    "7325542122234324",
    "2144335433132533",
    "1313336332232333",
    "2202344443343233",
    "1223313355142333",
    "2212432434424432",
    "5325334455444233",
    "4476644455434442",
    "4554354364533144",
    "5766453345443364",
    "4433553334322035",
    "4211143424330034",
]

c = new_canvas(16, 16, name="dirt_block")
for y in range(16):
    for x in range(16):
        c.set(x, y, PALETTE[int(GRID[y][x])])

view(c)
finish(c)
