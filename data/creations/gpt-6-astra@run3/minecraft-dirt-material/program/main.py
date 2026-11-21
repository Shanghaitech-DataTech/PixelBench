import random
result = new_canvas(16, 16, background='#81583b', name='dirt')
# Each grain wraps across the tile edge so the material repeats continuously.
rng = random.Random(41)
colors = ['#593d2b','#6b4931','#986b48','#ac7d54','#765139']
shapes = [[(0,0),(1,0),(0,1)],[(0,0),(1,0),(2,0),(1,1)],[(0,0),(0,1),(1,1)],[(0,0),(1,0)],[(0,0),(1,0),(0,1),(1,1)],[(0,0)]]
for i in range(67):
    x,y = rng.randrange(16),rng.randrange(16)
    col = rng.choices(colors, weights=[12,24,25,13,15])[0]
    for dx,dy in rng.choice(shapes):
        result.set((x+dx)%16,(y+dy)%16,col)
# Muted mineral grains, sparsely embedded in the earth.
for x,y in [(3,2),(11,5),(6,10),(14,13)]:
    result.set(x,y,'#8d8475')
    result.set((x+1)%16,y,'#756d60')
    result.set(x,(y+1)%16,'#756d60')
view(result, scale=24, margin=0)
finish(result)
