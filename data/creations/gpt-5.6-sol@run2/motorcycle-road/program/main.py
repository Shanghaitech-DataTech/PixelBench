from pixelbench_api import *

# Preserve the supplied motorcycle exactly, removing only its connected outer white field.
sprite = input_canvas.copy(name="motorcycle")
sprite.fill_at(0, 0, None)

out = new_canvas(96, 64, "#8ed8efff", name="output")

# Palette.
sky_hi = out.color("#8ed8ef", "sky")
sky_lo = out.color("#bde9ef", "horizon_sky")
cloud = out.color("#f8f4de", "cloud")
cloud_shade = out.color("#dce6d8", "cloud_shade")
hill_far = out.color("#729b68", "far_hill")
hill = out.color("#477d4d", "hill")
field_light = out.color("#9fbd49", "sunlit_field")
field = out.color("#638f35", "field")
grass_dark = out.color("#315c32", "dark_grass")
grass_bright = out.color("#b5cf4e", "bright_grass")
road = out.color("#55565a", "road")
road_dark = out.color("#3f4245", "road_dark")
road_light = out.color("#6a6968", "road_light")
shoulder = out.color("#84785f", "gravel")
stripe = out.color("#e8d98b", "road_marking")
fence = out.color("#79583c", "fence")
fence_hi = out.color("#ad8050", "fence_highlight")
trunk = out.color("#553e2b", "tree_trunk")
leaf_dark = out.color("#28592f", "leaf_dark")
leaf = out.color("#3e8138", "leaf")
leaf_hi = out.color("#67a83d", "leaf_highlight")
shadow = out.color("#303236b8", "bike_shadow")

# Subtle sky banding near the horizon.
out.rect(0, 13, 96, 15, sky_lo)
out.rect(0, 13, 96, 5, "#a7e1efff")

# Blocky summer clouds.
out.rect(7, 7, 17, 4, cloud)
out.rect(11, 4, 9, 8, cloud)
out.rect(15, 2, 5, 10, cloud)
out.rect(20, 6, 9, 6, cloud)
out.rect(8, 11, 19, 2, cloud_shade)
out.rect(62, 8, 18, 4, cloud)
out.rect(66, 5, 6, 8, cloud)
out.rect(72, 3, 5, 10, cloud)
out.rect(79, 9, 7, 4, cloud)
out.rect(64, 12, 20, 2, cloud_shade)

# Layered countryside and patchwork fields.
out.poly([(0, 27), (0, 21), (10, 18), (19, 22), (30, 16), (42, 23), (53, 19), (66, 23), (78, 17), (96, 22), (96, 31)], hill_far)
out.poly([(0, 32), (0, 27), (12, 23), (23, 28), (37, 21), (48, 28), (61, 24), (73, 29), (87, 22), (96, 25), (96, 35)], hill)
out.poly([(0, 30), (18, 27), (35, 32), (52, 27), (72, 31), (96, 27), (96, 43), (0, 43)], field_light)
out.poly([(0, 34), (22, 29), (43, 36), (63, 30), (96, 35), (96, 43), (0, 43)], field)
out.line(1, 37, 28, 31, grass_bright)
out.line(64, 34, 94, 29, grass_bright)
out.line(3, 40, 32, 35, grass_dark)
out.line(69, 39, 95, 35, grass_dark)

# Road and rough grassy shoulders.
out.rect(0, 42, 96, 4, grass_dark)
out.rect(0, 46, 96, 3, shoulder)
out.rect(0, 49, 96, 15, road)
out.rect(0, 60, 96, 4, road_dark)
out.line(0, 49, 95, 49, road_light)
out.dither(0, 46, 96, 3, [shoulder, grass_dark], pattern="checker")
# Small road texture, kept sparse and away from the subject.
for x, y in [(3,54),(12,58),(81,53),(89,57),(6,62),(76,61),(92,51),(18,52)]:
    out.set(x, y, road_light)
for x, y in [(1,59),(14,55),(79,58),(87,62),(94,55)]:
    out.set(x, y, road_dark)
# Broken center line visible to either side of the motorcycle.
out.rect(2, 57, 13, 2, stripe)
out.rect(78, 57, 15, 2, stripe)

# Fence in the middle distance.
out.line(0, 38, 18, 38, fence)
out.line(0, 41, 18, 40, fence)
out.line(76, 38, 95, 37, fence)
out.line(76, 41, 95, 40, fence)
for x, top in [(3,34),(16,35),(79,34),(92,33)]:
    out.rect(x, top, 3, 11, fence)
    out.set(x, top, fence_hi)
    out.set(x + 1, top, fence_hi)

# Roadside trees frame the scene without obscuring the motorcycle.
out.rect(2, 21, 4, 23, trunk)
out.rect(89, 20, 4, 24, trunk)
for cx, cy, r, col in [
    (4,18,7,leaf_dark),(1,23,6,leaf),(8,22,6,leaf),(5,13,6,leaf),(10,16,4,leaf_hi),
    (91,17,7,leaf_dark),(95,22,6,leaf),(87,22,6,leaf),(92,12,6,leaf),(86,16,4,leaf_hi)
]:
    out.circle(cx, cy, r, col)
# Restore trunks where foliage naturally opens near ground.
out.rect(3, 30, 3, 14, trunk)
out.rect(90, 29, 3, 15, trunk)

# Ground the wheels, then composite the original sprite over the scene.
out.ellipse(48, 52, 28, 3, shadow)
out.blit(sprite, 16, 4)

view(out, scale=8, margin=0)
finish(out)
