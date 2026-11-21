result = new_canvas(96,72,background='#a9d3d5',name='country-road')
# Soft clouds in a clear rural sky.
result.rect(7,8,17,3,'#edf0dc').rect(11,6,9,2,'#edf0dc').rect(20,9,8,2,'#edf0dc')
result.rect(60,5,19,3,'#edf0dc').rect(64,3,9,2,'#edf0dc').rect(76,7,10,2,'#edf0dc')
# Layered fields and distant hedges.
result.poly([(0,22),(9,19),(21,19),(34,24),(48,22),(60,17),(71,16),(83,19),(95,18),(95,44),(0,44)],'#86aaa0')
result.poly([(0,28),(12,25),(23,26),(38,30),(55,25),(72,25),(85,23),(95,24),(95,48),(0,48)],'#749361')
result.poly([(0,30),(17,28),(31,31),(49,33),(65,29),(81,28),(95,31),(95,48),(0,48)],'#a8b271')
result.poly([(0,35),(23,33),(45,36),(73,32),(95,33),(95,49),(0,49)],'#8d9d59')
# Planted strips follow the slope.
for pts in [[(0,31),(17,30),(29,32)],[(4,34),(22,32),(36,34)],[(65,31),(80,30),(94,32)]]:
    for a,b in zip(pts,pts[1:]): result.line(*a,*b,'#c0bf7d')
# A distant farmhouse among the fields.
result.rect(72,21,10,7,'#dfd0a1')
result.poly([(70,21),(76,17),(84,21)],'#775d50')
result.rect(75,24,2,4,'#716957').rect(79,23,2,2,'#7b9290')
# Trees framing the landscape.
def tree(x,y,s):
    result.rect(x,y,2,s+8,'#6b6950')
    result.line(x,y+s,x-3,y+3,'#6b6950')
    result.ellipse(x,y,s,s+2,'#536e51')
    result.ellipse(x-3,y-2,s-1,s-1,'#658456')
    result.ellipse(x+2,y-4,s-2,s-2,'#82965f')
tree(8,25,6)
tree(89,22,5)
# Fence on the far verge.
result.line(0,39,95,35,'#6e7253')
result.line(0,41,95,37,'#6e7253')
for x in range(2,96,9):
    y=39-(x*4//95)
    result.rect(x,y-2,2,7,'#82755a')
    result.set(x,y-2,'#c5b68a')
# Road shoulders and broad, gently angled asphalt.
result.poly([(0,44),(95,39),(95,64),(0,70)],'#c7b68b')
result.poly([(0,46),(95,41),(95,62),(0,68)],'#787d7b')
result.line(0,46,95,41,'#e0d3ad')
result.line(0,67,95,61,'#ded0a6')
# Broken centre stripe, visible ahead and below the motorcycle.
for x in [0,23,46,69,92]:
    y=62-(x*5//95)
    result.line(x,y,min(x+11,95),y,'#d9cfaa')
# Sparse aggregate, kept away from the subject's silhouette.
for x,y in [(5,49),(16,54),(6,59),(22,64),(39,65),(65,62),(86,47),(91,54),(80,59),(19,47),(3,65)]:
    result.rect(x,y,2,1,'#8d9188')
# Foreground meadow.
result.poly([(0,70),(95,64),(95,72),(0,72)],'#728a4c')
for x,y in [(7,70),(27,69),(49,68),(65,67),(84,66),(91,68)]:
    result.line(x,y,x+1,y-2,'#566e43')
    result.line(x+1,y,x+3,y-1,'#566e43')
# Contact shadows tie both tyres to the road.
result.ellipse(34,57,8,2,'#5d6661')
result.ellipse(70,57,8,2,'#5d6661')
result.line(36,56,69,56,'#626a64')
# Extract the original pixels, including open spaces within the wheels/frame.
bike=input_canvas.copy(name='motorcycle')
white=input_canvas.get(0,0)
for y in range(64):
    for x in range(64):
        if bike.get(x,y)==white:
            bike.set(x,y,None)
result.blit(bike,20,9)
view(result)
finish(result)
