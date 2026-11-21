import random
result = new_canvas(16,16,background='#805536',name='dirt')
rng=random.Random(173)
colors=['#593b29','#69452e','#744b31','#805536','#8d603d','#9c6c46','#ac7c53','#777369']
# Wrapped granular clusters keep all four edges tileable.
for i in range(100):
    x=rng.randrange(16); y=rng.randrange(16)
    col=rng.choices(colors[:7],[6,12,18,22,20,14,8])[0]
    shape=rng.choice([[(0,0)],[(0,0),(1,0)],[(0,0),(0,1)],[(0,0),(1,0),(0,1)],[(0,0),(1,0),(1,1)]])
    for dx,dy in shape: result.set((x+dx)%16,(y+dy)%16,col)
# Small muted mineral flecks amid the earth.
for x,y in [(3,2),(12,5),(7,11),(0,14)]:
    result.set(x,y,colors[7])
    result.set((x+1)%16,y,'#69452e')
view(result)
finish(result)
