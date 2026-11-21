result = new_canvas(96,80, '#a3d5de', name='country_road')
# A clear morning over rolling farmland.
result.rect(0,20,96,13,'#c2e1db')
result.rect(9,8,16,3,'#f1f1dc').rect(13,6,8,2,'#f1f1dc').rect(23,10,9,2,'#f1f1dc')
result.rect(59,12,18,3,'#f1f1dc').rect(63,10,8,2,'#f1f1dc')
result.poly([(0,29),(0,23),(9,20),(18,21),(27,25),(38,21),(48,19),(57,21),(68,26),(82,21),(95,22),(95,35)],'#81aaa0')
result.poly([(0,29),(12,26),(23,26),(36,31),(49,27),(63,26),(75,29),(88,25),(95,26),(95,45),(0,45)],'#678d65')
result.poly([(0,32),(18,29),(33,31),(49,35),(70,31),(95,31),(95,79),(0,79)],'#9aaa59')
result.poly([(0,37),(18,33),(33,35),(53,42),(39,47),(0,44)],'#c5ba6c')
result.poly([(0,43),(22,40),(46,45),(22,52),(0,52)],'#b4b663')
# Fine field furrows, kept behind the road and motorcycle.
for y in [37,40,43]:
    result.line(0,y,27,y-3,'#a6a45a')
result.poly([(88,30),(95,30),(95,53),(76,49),(76,39)],'#7f9b50')
# Pale gravel shoulders surrounding the winding asphalt.
road='M 81 28 L 85 28 C 77 35 80 38 91 42 L 95 43 L 95 70 C 65 68 32 79 0 79 L 0 53 C 22 48 47 48 66 44 C 83 40 70 36 81 28 Z'
result.path(road,'#d7cf9d')
road_inner='M 82 28 L 84 28 C 75 36 82 39 94 43 L 95 44 L 95 67 C 66 65 32 76 0 76 L 0 56 C 25 50 48 51 69 46 C 88 40 73 36 82 28 Z'
result.path(road_inner,'#737b7d')
result.path('M 0 72 C 35 71 65 61 95 63 L 95 67 C 66 65 32 76 0 76 Z','#626f72')
# Centre markings follow the bend.
result.line(81,30,80,32,'#e2d8a5')
result.line(80,36,82,38,'#e2d8a5')
result.poly([(83,43),(87,44),(83,46),(79,45)],'#e2d8a5')
result.poly([(4,65),(19,62),(20,64),(4,67)],'#e2d8a5')
result.poly([(34,60),(49,57),(51,59),(35,62)],'#e2d8a5')
result.poly([(68,54),(80,53),(84,55),(69,56)],'#e2d8a5')
# Fence follows the edge of the pasture.
result.line(0,43,42,39,'#786951')
result.line(0,46,42,42,'#786951')
for x,y in [(3,42),(15,41),(26,40),(36,39),(44,38)]:
    result.rect(x,y,2,8,'#675c49')
    result.set(x,y,'#e1d2a0')
# A pair of roadside trees, with clustered pixel foliage.
def tree(x,y,s):
    result.rect(x,y,2,s+5,'#6c6550')
    result.poly([(x-6,y+2),(x-8,y-2),(x-5,y-6),(x-2,y-7),(x,y-11),(x+5,y-10),(x+7,y-6),(x+9,y-3),(x+7,y+2),(x+2,y+4)],'#486f53')
    result.poly([(x-6,y-3),(x-3,y-6),(x,y-7),(x+1,y-10),(x+5,y-9),(x+6,y-5),(x+2,y-2),(x-1,y-1)],'#658b59')
    result.rect(x-3,y-5,3,2,'#87a665')
tree(9,28,5)
tree(86,30,5)
# Sparse grass clusters frame the foreground.
for x,y in [(4,52),(21,48),(50,47),(92,73),(74,75),(55,77),(12,78),(89,39)]:
    result.line(x,y,x-1,y-2,'#6f894a')
    result.line(x,y,x+2,y-2,'#6f894a')
# Keep every non-background pixel of the original motorcycle.
bike = input_canvas.copy(name='motorcycle')
white = input_canvas.get(0,0)
for y in range(64):
    for x in range(64):
        if input_canvas.get(x,y)==white:
            bike.set(x,y,None)
result.ellipse(48,64,27,2,'#586666')
result.ellipse(34,64,8,1,'#465354')
result.ellipse(69,64,7,1,'#465354')
result.blit(bike,16,16)
view(result)
finish(result)
