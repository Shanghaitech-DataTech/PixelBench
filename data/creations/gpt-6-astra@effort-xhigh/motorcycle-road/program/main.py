# A country lane, painted behind the original motorcycle.
result = new_canvas(96,80,background='#b8dfe0',name='output')
c = result
sky='#b8dfe0'; cloud='#f5f0d7'; cloudshade='#d8e6d8'
far='#86aaa0'; farlight='#a4bcb0'; hill='#6d9876'; hilllight='#86ad7a'
grass='#8caa54'; grasslight='#b3bf65'; grassdark='#688a49'
road='#737477'; roadlight='#898983'; roadshadow='#62666c'; verge='#c7bc83'; line='#eee0af'
# Quiet sky and stepped clouds.
c.poly([(0,8),(9,8),(9,6),(17,6),(17,7),(22,7),(22,10),(29,10),(29,12),(0,12)],cloudshade)
c.poly([(0,7),(9,7),(9,5),(16,5),(16,6),(21,6),(21,9),(27,9),(27,10),(0,10)],cloud)
c.poly([(54,11),(59,11),(59,9),(64,9),(64,7),(71,7),(71,8),(75,8),(75,10),(83,10),(83,12),(89,12),(89,14),(54,14)],cloudshade)
c.poly([(55,10),(60,10),(60,8),(65,8),(65,6),(70,6),(70,7),(74,7),(74,9),(82,9),(82,11),(87,11),(87,12),(55,12)],cloud)
# Distant hills and a nearer, patchwork slope.
c.poly([(0,26),(6,24),(14,24),(25,20),(32,20),(43,24),(50,24),(60,20),(67,19),(74,21),(84,20),(95,23),(95,41),(0,41)],farlight)
c.poly([(0,28),(8,27),(16,24),(24,24),(33,27),(43,29),(53,28),(63,25),(73,25),(84,28),(95,28),(95,43),(0,43)],far)
c.poly([(0,34),(9,30),(20,29),(30,31),(40,34),(51,35),(60,33),(68,30),(78,29),(87,30),(95,32),(95,53),(0,53)],hill)
c.poly([(0,37),(12,33),(24,33),(39,36),(48,38),(58,36),(68,32),(80,31),(95,34),(95,56),(0,56)],hilllight)
# Fields separated by a soft diagonal harvested strip.
c.poly([(0,40),(19,36),(35,36),(51,40),(66,36),(80,33),(95,36),(95,79),(0,79)],grass)
c.poly([(0,40),(18,37),(30,37),(48,41),(27,43),(0,47)],grasslight)
c.line(0,48,45,42,grassdark)
c.line(0,50,41,44,'#9caf58')
# A small farmhouse and adjoining barn on the remote hillside.
c.rect(40,29,9,6,'#d4c99a')
c.rect(47,30,4,5,'#b4aa83')
c.poly([(38,29),(44,24),(51,29)],'#715c51')
c.line(41,27,46,27,'#94705a')
c.rect(46,24,2,3,'#715c51')
c.rect(43,31,2,4,'#6c7162')
c.set(47,31,'#eff0c9')
c.line(38,35,52,35,grassdark)
# Remote hedges and cypress-like poplars.
for x,y,h in [(55,29,6),(59,30,8),(89,29,6),(93,30,8)]:
    c.line(x,y,x,y+h,'#637952')
    c.poly([(x,y-3),(x-2,y),(x-2,y+3),(x,y+5),(x+2,y+3),(x+1,y-1)],'#52795b')
    c.line(x-1,y,x-1,y+2,'#77945f')
# The road curls down from the farmhouse and opens into the foreground.
road_shape='M 67 33 C 73 33 84 37 86 41 C 90 48 66 49 40 54 C 24 57 9 61 0 64 L 0 80 L 96 80 L 96 50 C 96 44 90 36 72 32 L 68 32 Z'
c.path(road_shape,verge)
c.path('M 68 33 C 75 34 84 38 84 41 C 87 47 66 48 39 55 C 23 58 9 62 0 65 L 0 80 L 96 80 L 96 51 C 96 44 90 37 72 33 Z',road)
# Road edge, shoulder and faint sunlit tarmac patches.
c.path('M 69 34 C 76 35 83 38 82 41 C 82 45 62 48 39 55 C 23 59 9 63 0 66',line,fill=False)
c.path('M 0 78 C 21 71 42 69 61 65 C 77 61 88 59 95 57',roadshadow,fill=False)
c.path('M 0 68 C 23 62 39 59 56 55 C 73 52 87 48 88 44',roadlight,fill=False)
# Center dashes shrink toward the bend.
c.poly([(0,74),(12,70),(17,70),(5,75)],line)
c.poly([(26,68),(39,65),(43,65),(30,69)],line)
c.poly([(53,62),(63,59),(66,59),(57,63)],line)
c.poly([(77,55),(84,52),(86,52),(80,56)],line)
c.line(88,47,89,45,line)
c.line(84,39,82,38,line)
c.set(76,35,line)
# Fence beside the outside shoulder, with rails receding toward the bend.
fence='#8f7a50'; fence_light='#dfcd92'; fence_dark='#6e6847'
posts=[(1,55,8),(12,51,7),(24,47,6),(35,44,5),(45,42,4),(55,39,4),(64,37,3),(72,36,2)]
for (x,y,h),(xx,yy,hh) in zip(posts,posts[1:]):
    c.line(x,y-h+2,xx,yy-hh+1,fence)
    c.line(x,y-h+1,xx,yy-hh,fence_light)
    c.line(x,y-2,xx,yy-1,fence)
for x,y,h in posts:
    c.rect(x,y-h,2,h+1,fence_dark)
    c.line(x,y-h,x,y-1,fence_light)
    c.set(x+1,y-h,fence)
# A tree frames the scene to the left.
c.poly([(9,43),(11,32),(10,25),(13,26),(14,42),(16,44)],'#6a6546')
c.line(12,35,18,29,'#6a6546')
c.line(11,33,6,27,'#6a6546')
c.poly([(1,24),(3,21),(7,21),(8,17),(14,16),(17,18),(21,18),(24,22),(23,27),(20,30),(15,32),(9,31),(5,30),(1,28)],'#426f53')
c.poly([(1,23),(4,20),(8,20),(9,17),(14,17),(17,19),(20,19),(22,22),(20,25),(16,26),(13,29),(8,28),(6,26),(2,27)],'#5c8956')
c.poly([(4,21),(9,21),(10,18),(14,18),(16,20),(20,21),(18,23),(14,23),(12,25),(8,24),(5,25)],'#88a65c')
c.line(9,43,18,44,grassdark)
# Sparse grass tufts and tiny wildflowers on the near shoulder.
for x,y in [(3,58),(19,54),(31,50),(47,46),(59,43),(93,36),(87,33),(27,38),(6,46),(22,43)]:
    c.set(x,y-1,grassdark); c.line(x-1,y,x+2,y,grassdark)
for x,y in [(7,56),(16,52),(29,48),(49,44),(89,35)]:
    c.set(x,y,'#e6d68a')
# The near verge completes the road's width without crowding the motorcycle.
c.poly([(13,80),(33,76),(55,74),(77,72),(95,69),(95,80)],verge)
c.poly([(22,80),(39,77),(62,75),(79,74),(95,71),(95,80)],grassdark)
c.poly([(32,80),(47,78),(67,77),(85,74),(95,73),(95,80)],grass)
c.line(72,78,73,76,grassdark)
c.line(74,78,74,75,grassdark)
c.line(88,77,90,75,grassdark)
c.set(82,78,'#e6d68a')
# Low cast shadow anchors both tires to the tarmac.
c.ellipse(49,67,29,3,'#62666c')
c.ellipse(49,67,22,2,'#575d62')
c.ellipse(31,66,7,1,'#444d51')
c.ellipse(68,66,7,1,'#444d51')
# Remove only the original white backdrop, including the openings in the wheels.
bike = input_canvas.copy(name='motorcycle')
white = input_canvas.get(0,0)
for y in range(64):
    for x in range(64):
        if input_canvas.get(x,y) == white:
            bike.set(x,y,None)
result.blit(bike,18,19)
view(result,scale=6,margin=0)
save('motorcycle-country-road',result)
finish(result)
