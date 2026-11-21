# Green pear: seven opaque colours on a transparent 32 x 32 canvas.
result = new_canvas(32, 32, name='green_pear')
ink = '#293d25'
brown = '#805331'
shade = '#497b2e'
green = '#79a93e'
light = '#afd45b'
gleam = '#dce995'
leafgreen = '#426749'
# Small angled stem and the leaf behind the neck.
result.poly([(16,9),(15,7),(16,3),(18,2),(19,3),(18,5),(18,8)], ink)
result.line(17,3,16,7,brown)
result.set(17,4,brown)
result.poly([(18,6),(19,4),(22,2),(26,2),(25,5),(23,7),(20,7)], ink)
result.poly([(19,5),(22,3),(25,3),(23,5),(20,6)], shade)
result.line(21,4,24,3,green)
result.line(20,6,24,4,leafgreen)
# Deliberate stepped contour, broad and gently asymmetric at its base.
spans = {8:(14,18),9:(13,19),10:(13,20),11:(12,20),12:(12,20),13:(11,21),14:(10,22),15:(9,22),16:(8,23),17:(8,24),18:(7,24),19:(6,25),20:(6,25),21:(6,25),22:(6,25),23:(6,25),24:(7,25),25:(7,24),26:(8,23),27:(9,22),28:(11,20),29:(14,18)}
body = set((x,y) for y,(a,b) in spans.items() for x in range(a,b+1))
for x,y in body:
    result.set(x,y,green)
# Broad planes of reflected green, with the weight of the shadow at right.
result.poly([(18,9),(19,12),(19,15),(21,18),(22,21),(22,23),(20,26),(17,27),(12,27),(15,29),(23,29),(27,24),(27,17)], shade)
result.poly([(14,10),(17,9),(17,13),(15,16),(14,19),(13,23),(10,25),(8,23),(8,20),(10,16),(12,14)], light)
result.poly([(12,16),(14,15),(14,18),(12,20),(11,22),(9,22),(10,19)], gleam)
# Discrete highlight and a few skin flecks, all reusing the same palette.
result.line(14,11,14,12,gleam)
result.set(9,24,light)
result.set(12,25,light)
result.set(17,22,light)
result.set(19,25,green)
result.set(21,23,green)
result.set(18,17,shade)
# Clip planes to the fruit; restore its crisp one-pixel outer contour.
for y in range(8,32):
    for x in range(32):
        if (x,y) not in body:
            result.set(x,y,None)
for x,y in body:
    if any((x+dx,y+dy) not in body for dx,dy in ((-1,0),(1,0),(0,-1),(0,1))):
        result.set(x,y,ink)
# Tiny warm join where the stem enters the fruit.
result.set(16,8,brown)
print(result.stats_text())
print(result.matrix_text(region=(5,1,27,30)))
finish(result)
