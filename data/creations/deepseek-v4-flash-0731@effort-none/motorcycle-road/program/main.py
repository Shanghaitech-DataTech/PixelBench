from pixelbench_api import *

# Create the output canvas - copy of input
out = input_canvas.copy(name="output")

w, h = 64, 64

# Define colors
SKY = (135, 206, 235)
CLOUD = (255, 255, 255)
GRASS_FAR = (124, 179, 66)
GRASS = (86, 185, 52)
GRASS_DARK = (54, 130, 36)
ROAD = (105, 105, 105)
ROAD_DARK = (80, 80, 80)
ROAD_EDGE = (130, 130, 130)
GRASS_BOTTOM = (60, 160, 40)
TREE_TRUNK = (101, 67, 33)
TREE_GREEN = (34, 100, 40)
ROAD_LINE = (255, 255, 255)
FLOWER_RED = (230, 80, 80)

# Create the scene
scene = new_canvas(w, h, name="scene")

# Sky (rows 0-13)
scene.rect(0, 0, w, 14, SKY)

# Distant hills (rows 14-19)
scene.rect(0, 14, w, 6, GRASS_FAR)

# Green grass field (rows 20-43)
scene.rect(0, 20, w, 24, GRASS)

# Road (rows 44-52)
road_y = 44
road_h = 9
scene.rect(0, road_y, w, road_h, ROAD)

# Grass below road (rows 53-63)
scene.rect(0, road_y + road_h, w, h - (road_y + road_h), GRASS_BOTTOM)

# Grass texture
for y in range(20, road_y):
    for x in range(w):
        if (x * 3 + y * 7) % 17 == 0:
            scene.set(x, y, GRASS_DARK)

for y in range(road_y + road_h, h):
    for x in range(w):
        if (x * 5 + y * 11) % 19 == 0:
            scene.set(x, y, GRASS_DARK)

# Clouds
scene.ellipse(8, 4, 5, 2, CLOUD)
scene.ellipse(16, 3, 3, 2, CLOUD)
scene.ellipse(24, 5, 4, 1, CLOUD)
scene.ellipse(42, 6, 5, 2, CLOUD)
scene.ellipse(52, 3, 3, 1, CLOUD)

# Trees in the distant hills
scene.rect(2, 12, 2, 6, TREE_TRUNK)
scene.circle(3, 10, 3, TREE_GREEN)
scene.rect(7, 13, 2, 5, TREE_TRUNK)
scene.circle(8, 11, 2, TREE_GREEN)
scene.rect(55, 12, 2, 6, TREE_TRUNK)
scene.circle(56, 10, 3, TREE_GREEN)
scene.rect(60, 14, 2, 4, TREE_TRUNK)
scene.circle(61, 12, 2, TREE_GREEN)

# A small bush in the far field
scene.circle(30, 14, 2, TREE_GREEN)
scene.rect(30, 16, 2, 1, TREE_TRUNK)

# A fence line in the middle distance
for fx in range(5, 60, 10):
    scene.rect(fx, 20, 1, 3, TREE_TRUNK)
    if fx + 5 < w:
        scene.rect(fx, 21, 5, 1, TREE_TRUNK)

# Small flowers in the grass
for fy in range(26, 43, 5):
    for fx in range(3, 30, 13):
        scene.set(fx, fy, FLOWER_RED)
for fy in range(28, 43, 6):
    for fx in range(38, 62, 15):
        scene.set(fx, fy, FLOWER_RED)

# Road shoulder lines
scene.rect(0, road_y, w, 1, ROAD_EDGE)
scene.rect(0, road_y + road_h - 1, w, 1, ROAD_EDGE)

# Center line dashes
for x in range(2, w-2, 12):
    scene.rect(x, road_y + 4, 5, 1, ROAD_LINE)

# Road texture
for y in range(road_y + 1, road_y + road_h - 1):
    for x in range(w):
        if (x * 7 + y * 3) % 31 == 0:
            scene.set(x, y, ROAD_DARK)

# Composite: replace white from input with scene, keep everything else
for y in range(h):
    for x in range(w):
        idx = input_canvas.get(x, y)
        rgba = tuple(input_canvas.palette()[idx]['rgba'])
        if rgba == (255, 255, 255, 255):
            s_idx = scene.get(x, y)
            s_rgba = tuple(scene.palette()[s_idx]['rgba'])
            out.set(x, y, s_rgba)
        else:
            out.set(x, y, rgba)

# Fill any remaining transparent pixels in the output
for y in range(h):
    for x in range(w):
        idx = out.get(x, y)
        rgba = tuple(out.palette()[idx]['rgba'])
        if rgba[3] == 0:
            s_idx = scene.get(x, y)
            s_rgba = tuple(scene.palette()[s_idx]['rgba'])
            out.set(x, y, s_rgba)

finish(out)
