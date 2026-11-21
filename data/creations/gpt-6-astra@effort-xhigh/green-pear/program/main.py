# A small orchard pear, shaded in seven opaque colours.
result = new_canvas(32, 32, name='green_pear')
ink = '#30462b'
brown = '#795132'
shade = '#4e7a32'
green = '#7fac3e'
lime = '#b2d755'
light = '#e0ec93'
tan = '#b38a50'

# The leaf sits behind the bent wooden stem.
result.poly([(17,6),(19,3),(22,2),(27,2),(25,5),(22,7),(19,7)], ink)
result.poly([(19,5),(21,3),(25,3),(23,5),(20,6)], green)
result.line(20,4,24,3,lime)
result.line(18,7,23,4,shade)

# Stem: a one-pixel lit edge, and a darker cut end.
result.poly([(14,10),(14,7),(15,5),(16,2),(18,2),(18,5),(17,7),(17,10)], ink)
result.line(15,8,16,5,brown)
result.line(16,5,17,3,brown)
result.set(16,3,tan)
result.set(15,7,tan)

# Hand-stepped silhouette. The low, broad body narrows into a short neck.
rows = {
 8:(14,17), 9:(12,18), 10:(12,19), 11:(11,19),
 12:(11,19),13:(11,20),14:(10,20),15:(10,21),
 16:(9,22),17:(8,23),18:(7,24),19:(6,24),
 20:(6,25),21:(5,25),22:(5,25),23:(5,25),
 24:(6,25),25:(6,24),26:(7,24),27:(8,23),
 28:(10,21),29:(12,19)
}
body = {(x,y) for y,(a,b) in rows.items() for x in range(a,b+1)}
for x,y in sorted(body):
    boundary = any((x+dx,y+dy) not in body for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
    if boundary:
        col = ink
    elif y >= 27 or x >= 23 or (y >= 23 and x >= 21):
        col = shade
    elif x >= 19 or y >= 25 or (x >= 17 and y <= 16):
        col = green
    else:
        col = lime
    result.set(x,y,col)

# Broad highlight clusters follow the round left shoulder.
result.poly([(13,11),(15,10),(16,11),(15,14),(13,17),(11,19),(10,22),(8,22),(8,20),(10,17),(12,14)], light)
result.rect(8,23,2,2,lime)
# Soften the light's lower turn with a little green on the lower cheek.
result.line(9,25,12,27,green)
result.line(13,28,18,28,shade)
result.set(19,27,green)
# Tiny, deliberate lenticels rather than an overall noisy texture.
for x,y in [(16,18),(12,22),(17,24),(20,20)]:
    result.set(x,y,green)
result.set(11,25,light)
result.set(18,22,lime)
# Stem socket at the top of the fruit.
result.set(15,9,shade)
result.set(16,9,shade)
result.set(15,8,brown)

view(result, scale=12, margin=2, edges='all')
save('green-pear', result)
finish(result)
