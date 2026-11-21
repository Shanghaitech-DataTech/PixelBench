from pixelbench_api import *

inp = input_canvas
W, H = 128, 64

# ---------- palette colours ----------
sky    = (173, 216, 247)
cloud  = (245, 248, 252)
sun    = (255, 222, 84)
hill   = (150, 205, 138)
grass  = (104, 182, 84)
grass2 = (84, 158, 68)
tree   = (50, 120, 50)
trunk  = (121, 74, 40)
road   = (112, 112, 116)
roadedge = (238, 238, 238)
dash   = (255, 226, 92)
shadow = (74, 74, 78)

bg = new_canvas(W, H, name='scene')

# ---------- sky (rows 0..16) ----------
bg.rect(0, 0, W, 17, sky)
bg.circle(112, 8, 3, sun)
bg.rect(16, 6, 12, 3, cloud)
bg.rect(21, 4, 7, 2, cloud)
bg.rect(66, 12, 11, 3, cloud)
bg.rect(71, 10, 7, 2, cloud)
bg.rect(40, 3, 9, 2, cloud)

# rolling hills peeking above the grass
bg.ellipse(40, 29, 40, 14, hill)
bg.ellipse(88, 30, 44, 14, hill)
bg.ellipse(118, 29, 40, 14, hill)

# ---------- grass (rows 17..43) ----------
bg.rect(0, 17, W, 27, grass)
import random
random.seed(7)
tufts = [(x, y) for x in range(W) for y in range(19, 43)]
random.shuffle(tufts)
for (x, y) in tufts[:150]:
    bg.set(x, y, grass2)

# ---------- trees framing the scene ----------
def draw_tree(cx, cy):
    bg.rect(cx - 1, cy, 3, 7, trunk)
    bg.circle(cx, cy - 4, 5, tree)
draw_tree(8, 33)
draw_tree(121, 29)
draw_tree(2, 36)

# ---------- road (rows 44..59) ----------
bg.rect(0, 44, W, 16, road)
bg.rect(0, 44, W, 1, roadedge)
bg.rect(0, 59, W, 1, roadedge)
for x in range(0, W, 10):
    bg.rect(x, 51, 5, 2, dash)
bg.rect(0, 60, W, 4, grass)
for x in range(0, W, 12):
    bg.set(x + 3, 61, grass2)

# shadows under the wheels
bg.ellipse(48, 52, 8, 2, shadow)
bg.ellipse(97, 52, 8, 2, shadow)

# ---------- place the motorcycle on the road ----------
bw, bh, data = inp.to_rgba()
bike = inp.copy(name='bike')
for y in range(bh):
    for x in range(bw):
        i = (y * bw + x) * 4
        if data[i] == 255 and data[i+1] == 255 and data[i+2] == 255 and data[i+3] == 255:
            bike.set(x, y, None)

bg.blit(bike, 32, 3)

result = bg
finish(result)
