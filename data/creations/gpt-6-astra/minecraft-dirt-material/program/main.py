import random
result = new_canvas(16, 16, background='#805638', name='dirt')
# Wrapped clusters retain the same granular treatment at every tile edge.
rng = random.Random(52)
colors = ['#593c2b', '#69462f', '#734c32', '#926440', '#a3734d', '#b18459']
for i in range(84):
    x, y = rng.randrange(16), rng.randrange(16)
    shade = rng.choices(colors, weights=[8,15,14,20,12,4])[0]
    shape = rng.choice([[(0,0)], [(0,0),(1,0)], [(0,0),(0,1)], [(0,0),(1,0),(0,1)], [(0,0),(1,0),(1,1)]])
    for dx,dy in shape:
        result.set((x+dx)%16, (y+dy)%16, shade)
# Sparse embedded mineral fragments, with restrained cool grey-brown tones.
for x,y in [(2,3),(11,1),(7,10),(14,12)]:
    result.set(x,y,'#858078')
    result.set((x+1)%16,y,'#706c63')
result.set(2,4,'#706c63')
result.set(14,13,'#706c63')
view(result, scale=24, margin=0)
finish(result)
