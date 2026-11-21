import random
result = new_canvas(16, 16, background='#805438', name='dirt')
# Compact, opaque earth palette, with occasional cool mineral inclusions.
colors = ['#533923','#63432c','#704a30','#805438','#8d6040','#9c6c49','#ad7c54','#777263']
rng = random.Random(81)
# Toroidal clusters make the same grain distribution continue across each edge.
for i in range(155):
    x,y=rng.randrange(16),rng.randrange(16)
    col=rng.choices(colors, weights=[6,13,18,10,19,15,8,2])[0]
    shape=rng.choice([[(0,0)],[(0,0),(1,0)],[(0,0),(0,1)],[(0,0),(1,0),(0,1)],[(0,0),(1,0),(1,1)],[(0,0),(1,0),(0,1),(1,1)]])
    for dx,dy in shape:
        result.set((x+dx)%16,(y+dy)%16,col)
# A few embedded stone flecks, kept irregular and sparse.
for x,y in [(3,3),(11,7),(6,12)]:
    result.set(x,y,colors[7])
    result.set((x+1)%16,y,colors[2])
print(result.stats_text())
print(result.matrix_text())
finish(result)
