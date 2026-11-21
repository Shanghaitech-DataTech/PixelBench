result = new_canvas(16, 16, name='wooden_key')
O='#35231e'
D='#69402a'
M='#a46838'
L='#d79a53'
H='#f0c780'
# Carved bow and sturdy diagonal stem.
result.poly([(3,1),(6,1),(8,3),(8,6),(14,12),(14,14),(12,14),(10,12),(8,14),(6,12),(8,10),(6,8),(3,8),(1,6),(1,3)],O)
result.line(12,14,14,14,O)
result.poly([(3,2),(6,2),(7,3),(7,6),(13,12),(13,13),(12,13),(10,11),(8,13),(7,12),(9,10),(6,7),(3,7),(2,6),(2,3)],M)
# Directional light on the rim, with end-grain shadows.
result.line(3,2,6,2,H)
result.line(2,3,2,5,L)
result.set(3,6,L)
result.line(4,7,6,7,D)
result.line(7,3,7,5,L)
# Open centre of the key's wooden bow.
result.rect(3,3,3,3,O)
result.rect(4,4,2,2,None)
result.set(3,4,None)
result.set(4,3,None)
result.line(3,6,5,6,D)
result.set(6,4,D)
# Long grain follows the shaft; square-cut teeth remain distinct.
result.line(7,7,12,12,L)
result.line(7,8,12,13,D)
result.set(8,8,H)
result.set(10,10,M)
result.set(13,12,L)
result.set(13,13,M)
result.set(8,11,L)
result.set(7,12,L)
result.set(8,12,M)
view(result, scale=24)
finish(result)
