from pixelbench_api import *

c = input_canvas
W = H = 64
white_idx = c.color('#ffffffff')  # the input background

# ---- background country scene ----
bg = new_canvas(W, H, background=None)
def col(hexv, name=None):
    return bg.color(hexv, name)

skyT   = col('#8ecdf0', 'sky_top')
skyB   = col('#b8e2f5', 'sky_bottom')
sunC   = col('#ffd93d', 'sun')
cloudC = col('#ffffff', 'cloud')
hillC  = col('#79b56e', 'hill')
hillD  = col('#6aa75f', 'hill_shade')
fieldC = col('#9fd24a', 'field')
fieldD = col('#8cc43c', 'field_shade')
roadC  = col('#6b6b72', 'road')
roadD  = col('#5f5f66', 'road_wear')
lineC  = col('#ececec', 'edge_line')
dashC  = col('#f5cf3f', 'center_dash')
grassC = col('#66a63c', 'grass')
grassD = col('#57972f', 'grass_shade')
trunkC = col('#6b4a2b', 'tree_trunk')
folC   = col('#4fa04a', 'tree_foliage')
folD   = col('#3f8f3f', 'tree_foliage_dark')
shadowC = col('#3f3f46', 'shadow')
flwR   = col('#e23b3b', 'flower_red')

# --- sky ---
bg.rect(0, 0, W, 13, skyT)
bg.rect(0, 13, W, 13, skyB)          # rows 13..25

# sun + clouds
bg.circle(52, 5, 4, sunC)
def cloud(x, y):
    bg.rect(x+1, y,   8, 1, cloudC)
    bg.rect(x,   y+1, 10, 1, cloudC)
    bg.rect(x+1, y+2,  7, 1, cloudC)
    bg.rect(x+2, y+3,  4, 1, cloudC)
cloud(6, 5)
cloud(28, 9)
cloud(44, 16)

# --- distant hills ---
bg.rect(0, 25, W, 7, hillC)
bg.circle(15, 25, 9, hillC)
bg.circle(42, 25, 11, hillC)
bg.circle(58, 25, 8, hillC)
bg.circle(8, 25, 4, hillD)
bg.circle(50, 25, 5, hillD)

# --- field ---
bg.rect(0, 32, W, 6, fieldC)
for x in range(0, W, 4):
    bg.rect(x,   33, 2, 1, fieldD)
    bg.rect(x+2, 36, 2, 1, fieldD)

# --- road (rows 38..56) ---
bg.rect(0, 38, W, 19, roadC)
bg.rect(0, 38, W, 1, lineC)          # edge line
bg.rect(0, 55, W, 1, lineC)          # edge line
for x in range(0, W, 10):
    bg.rect(x, 47, 6, 1, dashC)      # dashed center line
for (px, py) in [(2, 42), (20, 44), (40, 52), (12, 52), (33, 40), (26, 54)]:
    bg.rect(px, py, 6, 2, roadD)     # worn patches
bg.rect(0, 46, W, 1, roadD)          # wheel-worn lane

# shadow beneath the motorcycle
bg.ellipse(31, 46, 27, 2, shadowC)

# --- grass verge ---
bg.rect(0, 57, W, 7, grassC)
for x in range(0, W, 3):
    bg.set(x,   58, grassD)
    bg.set(x+1, 61, grassD)
for (fx, fy) in [(3, 59), (9, 62), (24, 60), (38, 62), (46, 59), (55, 61)]:
    bg.set(fx, fy, sunC)
for (fx, fy) in [(15, 58), (31, 61), (50, 58)]:
    bg.set(fx, fy, flwR)

# --- roadside tree (right) ---
bg.rect(58, 29, 3, 12, trunkC)
bg.circle(58, 26, 5, folC)
bg.circle(56, 28, 3, folD)
bg.circle(60, 29, 3, folD)
bg.circle(42, 24, 5, folD)            # a second small tree in the field
bg.rect(43, 29, 2, 8, trunkC)

# --- bush at left of the road ---
bg.circle(2, 33, 4, folC)
bg.circle(1, 36, 3, folD)

# ---- motorcycle on top (everything except white pixels) ----
mc = new_canvas(W, H, background=None)
for y in range(H):
    for x in range(W):
        idx = c.get(x, y)
        if idx != white_idx:
            mc.set(x, y, idx)

result = flatten([bg, mc], name='output')
print(result.stats_text())
finish(result)
