result = new_canvas(32,32,name='ancient_compass')
c=result
ink='#241e2b'
shadow='#694131'
gold='#b97936'
mid='#dda749'
light='#f6d77a'
glint='#fff0b0'
# Suspension loop, tucked behind the compass body
c.rect(13,1,6,2,ink).rect(11,3,10,5,ink)
c.rect(13,3,6,3,gold).rect(14,3,4,2,light)
c.rect(14,4,4,2,ink)
# Stepped heavy silhouette
c.poly([(11,5),(20,5),(20,6),(24,6),(24,8),(27,8),(27,11),(29,11),(29,22),(27,22),(27,25),(24,25),(24,27),(20,27),(20,29),(11,29),(11,28),(7,28),(7,26),(4,26),(4,23),(2,23),(2,12),(4,12),(4,9),(7,9),(7,7),(11,7)],ink)
# Coin-like bezel and shaded lower thickness
c.ellipse(15,17,12,11,shadow)
c.ellipse(15,16,12,11,gold)
c.ellipse(15,16,11,10,mid)
c.path('M 5 16 L 5 12 L 8 9 L 12 7 L 19 7 L 23 9 L 25 12',light,fill=False)
c.path('M 5 19 L 7 23 L 11 26 L 19 26 L 24 23 L 26 19',shadow,fill=False)
c.line(11,27,19,27,gold)
# Recessed compass face
c.ellipse(15,16,9,9,shadow)
c.ellipse(15,16,8,8,ink)
c.ellipse(15,16,7,7,'#37434c')
c.ellipse(15,15,6,6,'#46545a')
# Gold cardinal markers and fine ancient dial engravings
c.poly([(15,7),(13,10),(17,10)],light)
c.rect(15,9,1,3,gold)
c.poly([(15,25),(13,22),(17,22)],gold)
c.rect(15,21,1,2,light)
c.poly([(6,16),(9,14),(9,18)],light)
c.poly([(24,16),(21,14),(21,18)],gold)
for x,y in [(10,10),(20,10),(9,21),(21,21)]:
    c.set(x,y,gold)
for x,y in [(11,12),(19,12),(11,20),(19,20)]:
    c.set(x,y,'#91a1a0')
# Compass rose pointing northeast, warm counterweight southwest
c.poly([(19,10),(18,16),(12,22),(12,17)],ink)
c.poly([(18,11),(17,16),(14,18)],light)
c.poly([(12,21),(13,17),(16,16)],gold)
# Dark rim around the large inset sapphire
c.poly([(14,11),(17,11),(20,14),(20,18),(17,21),(14,21),(11,18),(11,14)],ink)
c.poly([(14,12),(17,12),(19,14),(19,17),(17,20),(14,20),(12,17),(12,14)],'#155887')
c.poly([(14,12),(17,12),(18,14),(15,16),(12,14)],'#58d7ec')
c.poly([(12,14),(15,16),(14,19),(12,17)],'#229bc4')
c.poly([(15,16),(18,14),(19,14),(19,17),(17,20),(14,20)],'#2269ae')
c.poly([(15,14),(17,14),(18,16),(16,18),(14,17)],'#38bde4')
c.line(14,12,16,12,'#d7fcff').set(13,13,'#a1f5f4')
c.line(17,18,16,19,'#113d70')
# Bezel wear and catches of light
c.line(8,9,10,8,glint).line(5,13,5,15,glint)
c.set(22,9,glint).set(25,15,light).set(23,23,mid)
c.set(8,24,light).set(10,25,light)
c.set(20,7,shadow).set(4,18,shadow).set(24,21,shadow)
view(result)
finish(result)
