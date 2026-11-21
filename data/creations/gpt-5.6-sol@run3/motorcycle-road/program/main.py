from pixelbench_api import *
from collections import deque

src = input_canvas
W, H = 64, 64

# Identify only the white field connected to the canvas edge. Enclosed white
# details in the wheels remain part of the motorcycle.
white = src.get(0, 0)
outside = set()
q = deque()
for x in range(W):
    if src.get(x, 0) == white: q.append((x, 0))
    if src.get(x, H - 1) == white: q.append((x, H - 1))
for y in range(H):
    if src.get(0, y) == white: q.append((0, y))
    if src.get(W - 1, y) == white: q.append((W - 1, y))
while q:
    x, y = q.popleft()
    if (x, y) in outside or not (0 <= x < W and 0 <= y < H):
        continue
    if src.get(x, y) != white:
        continue
    outside.add((x, y))
    q.extend(((x-1,y), (x+1,y), (x,y-1), (x,y+1)))

out = new_canvas(W, H, '#9bd7e8', name='output')
# Palette
sky_hi = out.color('#c7edf0', 'sky_highlight')
sky = out.color('#9bd7e8', 'sky')
cloud = out.color('#f4f1df', 'cloud')
cloud_shade = out.color('#d9e5dc', 'cloud_shade')
hill_far = out.color('#78a95b', 'far_hills')
hill_light = out.color('#9fc867', 'sunlit_fields')
hill_dark = out.color('#4c7d45', 'hill_shadow')
hedge = out.color('#24543c', 'hedge')
hedge_hi = out.color('#3f7746', 'hedge_highlight')
grass = out.color('#5f963f', 'roadside_grass')
grass_light = out.color('#8fbd4a', 'grass_light')
grass_dark = out.color('#376b36', 'grass_dark')
road = out.color('#65686b', 'road')
road_light = out.color('#777b7c', 'road_light')
road_dark = out.color('#4e5355', 'road_dark')
line = out.color('#e9dfaa', 'road_marking')
fence = out.color('#e4d2a2', 'fence')
fence_dark = out.color('#8e7657', 'fence_shadow')
trunk = out.color('#745234', 'tree_trunk')
shadow = out.color('#34393a', 'bike_shadow')

# Sky bands and small fair-weather clouds.
out.rect(0, 0, 64, 12, sky_hi)
out.rect(0, 12, 64, 17, sky)
out.rect(7, 7, 11, 2, cloud)
out.rect(9, 5, 6, 4, cloud)
out.rect(11, 4, 3, 2, cloud)
out.rect(44, 9, 12, 2, cloud)
out.rect(47, 7, 6, 4, cloud)
out.rect(49, 6, 3, 2, cloud)
out.rect(47, 10, 8, 1, cloud_shade)

# Patchwork hills at the road's horizon.
out.poly([(0,25),(8,19),(17,22),(26,16),(36,23),(45,18),(55,22),(63,17),(63,35),(0,35)], hill_far)
out.poly([(0,27),(14,23),(26,26),(35,22),(47,25),(63,21),(63,35),(0,35)], hill_light)
out.poly([(0,31),(13,27),(27,31),(39,26),(53,29),(63,25),(63,36),(0,36)], hill_dark)
# Field furrows.
out.line(4, 28, 14, 24, '#d1d878')
out.line(17, 29, 26, 27, '#d1d878')
out.line(48, 27, 60, 24, '#d1d878')

# Dense hedgerows frame the road opening.
out.poly([(0,27),(8,25),(16,28),(22,27),(26,33),(22,38),(0,41)], hedge)
out.poly([(64,26),(57,25),(51,28),(46,27),(42,33),(45,38),(64,40)], hedge)
out.rect(0, 32, 23, 3, hedge_hi)
out.rect(47, 31, 17, 3, hedge_hi)
out.set(4,29,hedge_hi).set(12,28,hedge_hi).set(54,29,hedge_hi).set(60,28,hedge_hi)

# Perspective country road and grassy shoulders.
out.poly([(25,31),(40,31),(64,64),(0,64)], road)
out.poly([(29,31),(36,31),(50,64),(14,64)], road_light)
out.poly([(0,39),(25,31),(18,64),(0,64)], grass)
out.poly([(40,31),(64,39),(64,64),(48,64)], grass)
out.poly([(0,45),(18,37),(14,64),(0,64)], grass_dark)
out.poly([(47,36),(64,45),(64,64),(51,64)], grass_dark)
# Road edge stones and central broken marking.
out.line(24,33,14,63, road_dark)
out.line(40,33,51,63, road_dark)
out.poly([(31,34),(34,34),(35,39),(31,39)], line)
out.poly([(31,48),(36,48),(39,58),(29,58)], line)
# Grass pixel clusters along both verges.
for x,y in [(2,42),(6,39),(10,43),(4,51),(11,55),(2,59),(55,41),(59,46),(53,51),(61,56),(55,61)]:
    out.rect(x,y,2,1,grass_light)
    out.set(x+1,y-1,grass_light)

# A simple roadside fence receding toward the horizon.
out.line(48,35,63,49,fence_dark)
out.line(48,37,63,52,fence)
for x,y,h in [(48,34,6),(53,38,7),(59,43,9)]:
    out.rect(x,y,2,h,fence_dark)
    out.rect(x,y,1,h,fence)

# Ground the motorcycle with a narrow tire-level cast shadow.
out.ellipse(32, 53, 23, 2, road_dark)
out.rect(12,52,41,2,road_dark)

# Restore the original motorcycle exactly, including enclosed white highlights.
for y in range(H):
    for x in range(W):
        if (x, y) not in outside:
            out.set(x, y, src.get(x, y))

save('motorcycle-road', out, indexed=True)
view(out, scale=8, margin=0)
finish(out)
