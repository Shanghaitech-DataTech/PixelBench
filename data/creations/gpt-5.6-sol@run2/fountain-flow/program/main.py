result = new_canvas(64,84,name='running_fountain')
result.blit(input_canvas,0,8)
water = new_canvas(64,84,name='water')
shadow='#158bad'
blue='#2ec7dc'
light='#86e8ed'
foam='#e4ffff'
def line(x,y,xx,yy,c): water.line(x,y+8,xx,yy+8,c)
def rect(x,y,w,h,c): water.rect(x,y+8,w,h,c)
def path(d,c):
    # All path points are translated with a temporary water layer below.
    pass
# Rising jet and two short arcing sprays.
for x,y,xx,yy,c in [(31,6,31,-3,blue),(32,5,32,-4,light),(31,-4,32,-5,foam),(30,-3,29,-4,light),(29,-4,27,-4,blue),(27,-4,25,-2,blue),(25,-2,24,1,blue),(24,2,23,6,blue),(23,7,23,9,light),(33,-3,35,-4,blue),(35,-4,37,-3,light),(37,-3,39,0,blue),(39,1,40,5,blue),(40,6,40,8,light)]: line(x,y,xx,yy,c)
rect(31,0,1,5,foam)
rect(30,6,4,3,light)
line(29,9,34,9,foam)
# Short spills over the upper two bowls.
for x,y,h in [(23,12,6),(39,12,6),(18,22,7),(45,22,7)]:
    rect(x,y,3,h,shadow)
    rect(x,y,2,h-1,blue)
    rect(x,y,1,max(2,h-3),light)
    rect(x+1,y+h-2,1,2,foam)
    line(x-1,y+h,x+3,y+h,blue)
    line(x,y+h+1,x+2,y+h+1,light)
# Long side cascades falling from the lowest raised bowl into the pool.
for x,y,h in [(18,32,20),(44,32,20)]:
    rect(x,y,3,h,shadow)
    rect(x,y,2,h-2,blue)
    rect(x,y,1,6,light)
    rect(x+1,y+8,1,7,light)
    rect(x,y+16,1,3,foam)
    rect(x-1,y+h-1,5,2,blue)
    line(x-2,y+h,x+3,y+h,light)
    line(x-3,y+h+2,x+4,y+h+2,blue)
    water.set(x-2,y+h-2+8,foam)
    water.set(x+4,y+h-1+8,light)
# Front spill, split into slender ribbons so the stonework remains visible.
rect(29,34,6,2,blue)
line(29,34,34,34,light)
rect(30,36,3,7,blue)
rect(30,36,1,5,foam)
rect(31,43,2,10,blue)
rect(31,45,1,5,light)
rect(32,54,1,2,light)
line(28,56,35,56,blue)
line(30,57,34,57,foam)
# Scattered droplets and ripples around the landing points.
for x,y in [(16,48),(22,50),(42,49),(48,48),(28,53),(35,54),(21,17),(42,18),(16,27),(48,28)]:
    rect(x,y,1,2,light)
for x,y,w in [(13,54,4),(21,55,4),(39,55,5),(47,53,3),(25,11,3),(35,11,3)]:
    line(x,y,x+w-1,y,light)
result=flatten([result,water],name='output')
view(result,scale=6,margin=0)
finish(result)
