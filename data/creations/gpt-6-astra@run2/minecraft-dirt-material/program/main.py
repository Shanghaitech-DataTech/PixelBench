import random
result = new_canvas(16, 16, background='#80583b', name='dirt')
# All grain clusters wrap around the tile, including the boundary clusters.
rng = random.Random(37)
colors = ['#80583b', '#926747', '#6c482f', '#a27852', '#593d2c', '#b18a61', '#777269', '#969084']
def grain(x,y,shape,color):
    for dx,dy in shape:
        result.set((x+dx)%16,(y+dy)%16,color)
shapes = [[(0,0),(1,0),(0,1)], [(0,0),(1,0)], [(0,0),(0,1),(1,1)], [(0,0),(1,0),(2,0),(1,1)], [(0,0),(0,1)]]
for i in range(49):
    x,y=rng.randrange(16),rng.randrange(16)
    grain(x,y,rng.choice(shapes),rng.choice([colors[1],colors[1],colors[2],colors[3]]))
for x,y,shape in [(2,3,[(0,0),(1,0),(1,1)]),(11,1,[(0,0),(1,0)]),(7,7,[(0,0),(0,1),(1,1)]),(13,10,[(0,0),(1,0)]),(2,12,[(0,0),(0,1)]),(9,14,[(0,0),(1,0)])]:
    grain(x,y,shape,colors[4])
for x,y in [(5,1),(0,7),(11,6),(6,11),(14,14)]:
    grain(x,y,[(0,0),(1,0)],colors[3])
    result.set(x,y,colors[5])
# Sparse mineral fragments, subordinate to the warm soil.
for x,y in [(14,3),(4,8),(10,12)]:
    grain(x,y,[(0,0),(1,0),(1,1)],colors[6])
    result.set(x,y,colors[7])
view(result)
save('dirt', result)
finish(result)
