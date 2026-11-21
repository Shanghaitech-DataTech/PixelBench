import random
result = new_canvas(16,16,background='#805638',name='dirt')
# Wrapped clusters ensure texture continues across every tile boundary.
rng=random.Random(41)
colors=['#68452f','#704a31','#94633f','#a37249','#593e2d','#895b3b']
shapes=[[(0,0),(1,0),(0,1)],[(0,0),(1,0),(1,1)],[(0,0),(0,1)],[(0,0),(1,0),(2,0),(1,1)],[(0,0),(1,0),(0,1),(1,1)]]
for i in range(63):
    x,y=rng.randrange(16),rng.randrange(16)
    col=colors[rng.randrange(len(colors))]
    for dx,dy in rng.choice(shapes):
        result.set((x+dx)%16,(y+dy)%16,col)
# Sparse desaturated mineral chips, set among the brown clods.
for x,y in [(3,2),(12,5),(6,11),(15,14)]:
    result.set(x,y,'#777164')
    result.set((x+1)%16,y,'#8b8070')
    result.set(x,(y+1)%16,'#68452f')
view(result)
finish(result)
