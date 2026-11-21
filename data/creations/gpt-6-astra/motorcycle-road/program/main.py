result = new_canvas(96,80, '#a9d8df', name='country_road')
# Open sky and small banks of cloud.
result.rect(0,24,96,10,'#c7e3dd')
result.poly([(7,13),(11,13),(11,10),(20,10),(20,12),(26,12),(26,15),(7,15)], '#edf0da')
result.poly([(55,8),(59,8),(59,6),(66,6),(66,8),(73,8),(73,10),(55,10)], '#edf0da')
# Distant hills and patchwork pasture.
result.poly([(0,29),(8,26),(16,24),(26,25),(39,29),(51,26),(62,21),(70,20),(81,23),(95,25),(95,43),(0,43)], '#799d84')
result.poly([(0,34),(13,29),(25,28),(37,31),(51,33),(69,29),(83,28),(95,30),(95,53),(0,53)], '#98b56d')
result.poly([(0,36),(23,32),(39,34),(60,40),(34,47),(0,48)], '#c5c17a')
result.poly([(0,40),(23,35),(38,37),(45,39),(0,46)], '#d7cd88')
result.poly([(0,46),(31,41),(55,42),(78,36),(95,34),(95,80),(0,80)], '#739b55')
result.poly([(0,67),(40,62),(72,57),(95,49),(95,80),(0,80)], '#9baf5e')
# A hedge following the far field.
result.line(0,35,22,30,'#668b57')
result.line(22,30,38,32,'#668b57')
for x,y in [(2,34),(8,32),(16,30),(25,29),(33,30)]:
    result.rect(x,y,4,3,'#668b57')
# Winding tarmac and light gravel shoulder.
road=[(0,51),(28,49),(53,48),(69,43),(79,37),(84,32),(86,29),(89,29),(87,36),(84,43),(79,49),(81,52),(95,54),(95,65),(76,68),(53,74),(26,77),(0,77)]
result.poly(road,'#ccbd93')
result.poly([(0,54),(29,52),(54,51),(71,46),(82,38),(86,32),(87,30),(88,30),(86,37),(82,45),(76,50),(80,55),(95,57),(95,62),(75,65),(53,71),(25,74),(0,74)], '#777b78')
# Sparse surface texture and dashed center line.
for x,y,w in [(1,65,10),(24,64,10),(49,61,9),(72,56,7)]:
    result.rect(x,y,w,2,'#ded4af')
result.line(77,47,80,44,'#ded4af')
result.line(84,39,85,37,'#ded4af')
for x,y,w in [(3,58,5),(18,71,5),(42,68,7),(57,66,4),(86,60,5),(61,53,3)]:
    result.rect(x,y,w,1,'#858983')
# Fence along the verge behind the motorcycle.
result.line(0,44,62,43,'#8e7951')
result.line(0,48,62,47,'#8e7951')
result.line(62,43,78,36,'#8e7951')
result.line(62,47,78,39,'#8e7951')
for x,y,h in [(3,42,10),(17,42,9),(32,42,9),(47,41,9),(62,41,8),(72,37,7),(78,35,6)]:
    result.rect(x,y,2,h,'#705f47')
    result.line(x,y,x,y+h-2,'#d3bc83')
# A small wayside tree on the left.
result.rect(8,27,3,13,'#76664b')
result.line(9,32,5,27,'#76664b')
result.poly([(1,25),(3,20),(8,18),(13,20),(17,25),(15,30),(4,31),(1,28)], '#4f805d')
result.poly([(2,24),(5,20),(9,19),(13,22),(12,25),(7,27),(2,26)], '#709b67')
result.rect(5,21,4,2,'#95b576')
# Verge grasses and small flowers.
for x,y in [(2,79),(9,77),(22,79),(38,77),(58,74),(66,72),(81,69),(90,68),(92,48),(86,46),(2,50)]:
    result.line(x,y,x-1,y-2,'#5f884d')
    result.line(x,y,x+2,y-3,'#5f884d')
for x,y in [(53,77),(56,76),(84,73),(89,71),(18,48)]:
    result.set(x,y,'#e4d798')
# Contact shadows anchor both tires to the road.
result.ellipse(49,61,28,3,'#666e65')
result.ellipse(30,61,7,1,'#50594f')
result.ellipse(69,61,7,1,'#50594f')
# Keep every original colored motorcycle pixel; white was the backdrop.
bike = input_canvas.copy(name='motorcycle')
for y in range(64):
    for x in range(64):
        if bike.get(x,y)==1:
            bike.set(x,y,None)
bike.set(54,28,'#fff7da')
result.blit(bike,16,14)
view(result)
finish(result)
