from pixelbench_api import *

# Preserve the original fountain and give the top jet room to rise.
result = new_canvas(64, 88, name='running_fountain')
result.blit(input_canvas, 0, 12)

water_dark = '#1d8baa'
water = '#2ec7dc'
water_light = '#8eeaf0'
foam = '#ffffff'

# Central upward jet, tapering into droplets above the finial.
result.rect(31, 1, 2, 11, water_dark)
result.rect(30, 4, 1, 7, water)
result.rect(33, 5, 1, 6, water)
result.set(31, 0, water_light)
result.set(32, 1, foam)
result.set(30, 2, water_light)
result.set(29, 2, water_light)
result.set(34, 3, water_light)
result.set(28, 5, water)
result.set(35, 6, water)
result.set(27, 8, water_light)
result.set(36, 9, water_light)

# Small spray arcs returning into the top bowl.
for pts, col in [
    ([(30,5),(28,5),(27,6),(26,7),(25,8),(24,9),(23,11),(22,13),(22,15)], water),
    ([(33,6),(35,6),(36,7),(37,8),(38,9),(39,11),(40,13),(40,15)], water),
    ([(29,6),(27,7),(26,9),(25,11),(24,14)], water_light),
    ([(34,7),(36,8),(37,10),(38,12),(39,15)], water_light),
]:
    for x, y in pts:
        result.set(x, y, col)

# Water spilling from the top tier into the middle tier.
def stream(points):
    for x, y, w, col in points:
        result.rect(x, y, w, 1, col)

stream([
    (17,29,3,water_light),(16,30,4,water),(16,31,4,water),(17,32,4,water),
    (18,33,4,water),(18,34,4,water_light),(19,35,4,water),(20,36,3,water),
    (20,37,3,water_dark),(21,38,2,water_light),
])
stream([
    (45,29,3,water_light),(44,30,4,water),(44,31,4,water),(43,32,4,water),
    (42,33,4,water),(42,34,4,water_light),(41,35,4,water),(41,36,3,water),
    (41,37,3,water_dark),(41,38,2,water_light),
])

# Broken side falls from the middle bowl to the lower pool.
stream([
    (12,45,3,foam),(12,46,4,water_light),(12,47,4,water),(13,48,3,water),
    (13,49,3,water_light),(13,50,4,water),(14,51,3,water),(14,52,3,water_dark),
    (15,53,2,water_light),(15,54,2,foam),(16,55,1,water),
])
stream([
    (49,45,3,foam),(48,46,4,water_light),(48,47,4,water),(48,48,3,water),
    (48,49,3,water_light),(47,50,4,water),(47,51,3,water),(47,52,3,water_dark),
    (47,53,2,water_light),(47,54,2,foam),(47,55,1,water),
])

# Bright broken highlights and splash pixels emphasize moving water.
for x, y in [(14,39),(15,40),(23,40),(40,40),(48,39),(49,40),
             (8,50),(16,51),(47,51),(55,50),(13,57),(17,58),
             (46,58),(50,57),(22,65),(25,67),(38,67),(42,65)]:
    result.set(x, y, water_light)
for x, y in [(15,41),(22,39),(41,39),(48,41),(8,52),(17,53),
             (46,53),(55,52),(18,59),(45,59)]:
    result.set(x, y, foam)

view(result, scale=6, margin=0)
finish(result)
