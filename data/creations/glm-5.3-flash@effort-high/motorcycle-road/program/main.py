from pixelbench_api import *

# --- 1. isolate the motorcycle: remove the white background ---
bike = input_canvas.copy(name="output")
white = bike.color('#ffffff')
for y in range(64):
    for x in range(64):
        if bike.get(x, y) == white:
            bike.set(x, y, None)

# --- 2. country road scene ---
s = new_canvas(64, 64, name="scene")

sky      = s.color('#a9dcf5', name='sky')
sun      = s.color('#ffd94a', name='sun')
hill     = s.color('#7cb85c', name='hill')
hill_d   = s.color('#5f9c46', name='hill_dark')
grass    = s.color('#8fce62', name='grass')
grass_d  = s.color('#6fb04a', name='grass_dark')
road     = s.color('#7a7a80', name='road')
road_d   = s.color('#5c5c62', name='road_dark')
line_c   = s.color('#e8e6d0', name='road_line')
bush     = s.color('#3f8a3a', name='bush')
flower_r = s.color('#e05555', name='flower_red')
flower_y = s.color('#f0c040', name='flower_yellow')

# sky, sun, clouds
s.rect(0, 0, 64, 27, sky)
s.circle(53, 6, 4, sun)
s.circle(11, 8, 3, '#ffffff')
s.circle(15, 7, 2, '#ffffff')
s.circle(30, 12, 3, '#ffffff')
s.circle(34, 11, 2, '#ffffff')

# distant hills poking over the horizon
s.ellipse(14, 29, 14, 9, hill)
s.ellipse(46, 30, 20, 10, hill_d)

# grass fields
s.rect(0, 27, 64, 37, grass)

# the road: wheels of the bike rest at y=50
s.rect(0, 50, 64, 11, road)
s.rect(0, 50, 64, 1, road_d)
s.rect(0, 60, 64, 1, road_d)
for x in range(2, 64, 8):
    s.rect(x, 55, 4, 1, line_c)

# bushes at the roadside
s.ellipse(3, 48, 3, 2, bush)
s.ellipse(61, 48, 3, 2, bush)

# grass tufts and flowers
for x, y in [(6, 33), (18, 30), (28, 36), (40, 31), (52, 34), (58, 29),
             (10, 40), (24, 43), (36, 38), (48, 42), (56, 38), (14, 36)]:
    s.line(x, y, x, y + 2, grass_d)
for x, y in [(9, 32), (33, 33), (45, 30), (20, 41), (60, 36)]:
    s.set(x, y, flower_r)
for x, y in [(15, 30), (38, 41), (52, 44), (5, 44)]:
    s.set(x, y, flower_y)

# --- 3. motorcycle on top of the road ---
s.blit(bike, 0, 1)

print(s.stats_text())
print(s.matrix_text(region=(0, 18, 63, 52)))

finish(s)
