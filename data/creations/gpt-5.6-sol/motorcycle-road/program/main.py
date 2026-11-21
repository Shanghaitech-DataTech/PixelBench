from pixelbench_api import *

# Preserve the supplied motorcycle while removing its connected white backdrop.
sprite = input_canvas.copy(name="motorcycle")
sprite.fill_at(0, 0, None)

output = new_canvas(64, 64, "#86c9e8", name="output")

# Palette: clear country daylight and strong, readable terrain bands.
sky = "#86c9e8"
sky_hi = "#b7e2f2"
cloud = "#eef7f5"
cloud_shadow = "#c9e4e7"
hill_far = "#78ad58"
hill_light = "#8fc665"
field = "#5e9f42"
field_light = "#76ba48"
hedge_dark = "#245d38"
hedge = "#337746"
hedge_hi = "#4d9250"
trunk = "#76563b"
fence = "#d7c39a"
fence_shadow = "#a88f69"
road_edge = "#cbb991"
road = "#55565a"
road_dark = "#46474b"
road_light = "#67686c"
mark = "#f3df9b"
grass_dark = "#32713b"
grass = "#4f9642"
grass_hi = "#70b94a"
shadow = "#343438"

# Small blocky clouds.
output.rect(5, 7, 12, 3, cloud)
output.rect(8, 4, 6, 6, cloud)
output.rect(15, 8, 8, 3, cloud)
output.rect(6, 10, 15, 2, cloud_shadow)
output.rect(42, 6, 11, 3, cloud)
output.rect(45, 4, 5, 6, cloud)
output.rect(39, 8, 17, 3, cloud)
output.rect(42, 10, 11, 2, cloud_shadow)

# Layered rolling hills.
output.poly([(0, 25), (7, 20), (14, 22), (22, 16), (31, 22), (39, 18), (47, 22), (55, 17), (63, 21), (63, 38), (0, 38)], hill_far)
output.poly([(0, 28), (10, 24), (19, 28), (28, 23), (38, 27), (48, 22), (57, 27), (63, 25), (63, 39), (0, 39)], hill_light)
output.poly([(0, 32), (9, 28), (18, 31), (27, 27), (37, 32), (47, 28), (56, 31), (63, 29), (63, 41), (0, 41)], field)
# Crop rows suggest furrows in the fields.
output.line(0, 34, 22, 28, field_light)
output.line(42, 32, 63, 27, field_light)
output.rect(1, 35, 21, 2, field_light)

# Distant trees and hedge along the road.
for x, y, r in [(2,29,4),(7,27,5),(13,30,4),(50,28,5),(57,26,5),(63,29,4)]:
    output.circle(x, y, r, hedge_dark)
    output.rect(x-2, y, 4, 7, hedge_dark)
for x, y, r in [(2,28,3),(8,26,4),(14,29,3),(49,27,4),(57,25,4),(63,28,3)]:
    output.circle(x, y, r, hedge)
output.rect(0, 34, 64, 5, hedge_dark)
output.rect(0, 34, 64, 2, hedge)
for x in range(1, 64, 7):
    output.rect(x, 34, 3, 2, hedge_hi)

# A pale wooden fence peeking through behind the motorcycle.
for x in (3, 18, 46, 59):
    output.rect(x, 29, 2, 9, fence_shadow)
    output.rect(x, 29, 1, 8, fence)
output.rect(0, 31, 64, 2, fence_shadow)
output.rect(0, 31, 64, 1, fence)
output.rect(0, 36, 64, 2, fence_shadow)
output.rect(0, 36, 64, 1, fence)

# Road, aggregate edge, and foreground verge.
output.rect(0, 39, 64, 25, road)
output.rect(0, 39, 64, 2, road_edge)
output.rect(0, 42, 64, 2, road_light)
output.rect(0, 60, 64, 4, grass_dark)
output.rect(0, 61, 64, 3, grass)
for x in range(0, 64, 4):
    output.set(x, 60, grass_hi)
    if x % 8 == 0:
        output.set(x+1, 59, grass_dark)
# Broken center line remains visible around the vehicle.
output.rect(1, 54, 10, 2, mark)
output.rect(17, 54, 10, 2, mark)
output.rect(35, 54, 11, 2, mark)
output.rect(53, 54, 10, 2, mark)
# Sparse road texture.
for x, y in [(4,46),(14,50),(23,59),(31,48),(42,58),(51,49),(60,44)]:
    output.rect(x, y, 2, 1, road_dark)

# Ground the wheels, then restore the original motorcycle pixels exactly.
output.ellipse(32, 48, 24, 2, shadow)
output.blit(sprite, 0, 0)

view(output, scale=8, margin=0)
finish(output)
