import random
import math

result = input_canvas.copy(name='output')
W, H, raw = input_canvas.to_rgba()
def rgb_at(x,y):
    i=(y*W+x)*4
    return tuple(raw[i:i+4])

# Remove the raised arm outside the cabinet with nearby unobstructed sky.
for y in range(69,92):
    for x in range(72,84):
        result.set(x,y,input_canvas.get(x-13,y))

# Reconstruct the cabinet face behind the person. The side panel is retained.
result.poly([(81,59),(114,57),(116,122),(79,125),(80,91)], '#1c184b')
result.line(81,60,80,117,'#19153f')
result.line(82,60,81,118,'#302155')
# Clear the final strip of coat along the cabinet's outside edge.
for y in range(100,124):
    for x in range(78,80):
        result.set(x,y,input_canvas.get(75,y))
result.line(80,100,80,122,'#16133d')
result.poly([(84,61),(112,59),(115,61),(115,99),(112,103),(84,104)], '#b591bd')
result.poly([(85,62),(112,60),(114,62),(114,98),(111,101),(85,102)], '#f1ded8')
result.line(85,61,112,59,'#ffeae3')
result.line(84,63,84,100,'#dcb2ea')
# Three illuminated shelves, each containing a varied row of drinks.
for y in (69,79,90):
    result.line(85,y,114,y-1,'#849288')
    result.line(85,y+1,114,y,'#b8bdaf')

def can(x,y,w,h,base,shade,light,cap):
    result.rect(x,y,w,h,base)
    result.rect(x+w-1,y+1,1,h-1,shade)
    result.line(x,y+1,x,y+h-2,light)
    result.rect(x,y,w,1,cap)
    result.line(x+1,y+h-1,x+w-1,y+h-1,shade)
    if h>=7:
        result.rect(x+1,y+3,max(1,w-2),2,'#d5e4d5')

for x,y,col,shade,hi in [(87,63,'#d99665','#a56c51','#efb998'),(94,62,'#78aeb6','#517b94','#c4ece5'),(102,62,'#76c472','#517653','#b1dfa0'),(108,61,'#a570db','#785690','#dcb2ea')]:
    can(x,y,4,7,col,shade,hi,'#e7d7d1')
for x,y,col,shade,hi in [(87,73,'#8fc6c3','#618f9f','#c4f2f0'),(94,72,'#75bfd0','#6e7774','#c4f2f0'),(101,72,'#6c54e6','#51509b','#b0b1eb'),(108,71,'#7ec0d4','#5f9097','#c4f2f0')]:
    can(x,y,4,7,col,shade,hi,'#f1e2d9')
for x,y,col,shade,hi in [(87,83,'#b889aa','#785690','#e7c2de'),(94,82,'#76c472','#517653','#b0dfa5'),(101,82,'#83b4c7','#618f9f','#c4f2f0'),(108,81,'#a570db','#785690','#dcb2ea')]:
    can(x,y,4,8,col,shade,hi,'#e8e5d3')
for x,y in [(87,94),(94,93),(101,93),(108,92)]:
    can(x,y,4,7,'#785b4a','#4f3b41','#b78c74','#d97454')
    result.rect(x,y,4,1,'#c6321a')
    result.rect(x+1,y-1,2,1,'#ffeae3')
# Window surround and coin controls, above the original motorcycle.
result.line(84,104,112,103,'#322455')
result.line(85,105,111,104,'#78578c')
result.poly([(83,106),(105,105),(105,115),(82,116)],'#211a4e')
result.poly([(86,109),(101,108),(101,112),(86,113)],'#0a1b2b')
result.line(87,109,99,108,'#3b4860')
result.line(87,114,100,113,'#473565')
result.poly([(108,107),(113,105),(115,110),(108,114)],'#283346')
result.line(109,108,112,107,'#778487')
result.line(110,110,112,109,'#06141e')
result.set(113,111,'#75bfd0')
# Preserve the untouched motorcycle silhouette where it crosses the repairs.
bike_poly=[(78,124),(83,122),(89,120),(94,118),(100,116),(101,115),(104,115),(106,117),(107,120),(112,120),(114,123),(114,129),(103,135),(88,131)]
bike_mask=new_canvas(170,170)
bike_mask.poly(bike_poly,'#ffffff')
for y in range(114,136):
    for x in range(78,115):
        if bike_mask.get(x,y) != bike_mask.get(0,0):
            result.set(x,y,input_canvas.get(x,y))

# Cool the pavement into wet asphalt, retaining the existing reflected shapes.
_,_,base=result.to_rgba()
for y in range(149,170):
    for x in range(170):
        i=(y*170+x)*4
        r,g,b,a=base[i:i+4]
        if r>g*1.12:
            result.set(x,y,(int(r*.65),int(g*.84),min(255,int(b*1.09)+7),a))

# Rain-filled puddles and broken reflections on the ground.
result.poly([(0,157),(10,155),(21,155),(25,157),(20,159),(31,160),(29,163),(11,164),(0,163)],'#173943')
result.poly([(0,159),(9,157),(17,158),(14,160),(27,161),(20,162),(0,161)],'#284856')
result.line(1,158,10,157,'#406374')
result.line(3,162,16,162,'#345967')
result.poly([(127,155),(139,153),(150,154),(153,157),(169,158),(169,169),(129,169),(134,165),(124,161)],'#163643')
result.poly([(132,157),(143,156),(148,158),(162,159),(165,162),(157,163),(145,162),(135,164),(127,161)],'#244758')
result.line(135,156,143,155,'#4d6979')
result.line(139,164,152,164,'#3c6173')
result.line(153,166,165,166,'#254f63')
# The pink window glimmers in broken strips between the bike and the puddles.
for x,y,w,c in [(120,150,6,'#574562'),(123,153,4,'#80627e'),(122,156,7,'#a084a1'),(117,159,5,'#655672'),(123,161,6,'#4e4a69'),(116,164,8,'#7b687e'),(117,166,6,'#45485e')]:
    result.rect(x,y,w,1,c)
result.line(44,163,52,163,'#b7b6bd')
result.line(49,165,55,165,'#677a88')
result.line(80,166,88,166,'#c3c5cc')
result.line(77,168,85,168,'#687e91')

# Distant lightning: a narrow brilliant core and a restrained, pixel-stepped glow.
lightning=new_canvas(170,170,name='lightning')
bolt=[(79,2),(73,13),(77,13),(66,28),(71,27),(60,43),(64,42),(55,57)]
branch=[(66,28),(76,30),(79,37),(85,41)]
farbolt=[(154,4),(146,17),(150,17),(138,32),(144,31),(135,45),(129,51)]
def stroke_poly(c,pts,color):
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        c.line(x0,y0,x1,y1,color)
for pts in (bolt,branch,farbolt):
    for dx,dy in [(-2,0),(2,0),(0,-2),(0,2),(-1,-1),(1,1)]:
        stroke_poly(lightning,[(x+dx,y+dy) for x,y in pts],'#71b8da21')
    for dx in (-1,1):
        stroke_poly(lightning,[(x+dx,y) for x,y in pts],'#8ed2f16a')
    stroke_poly(lightning,pts,'#d7f5f2' if pts is bolt else '#acdbe8')
stroke_poly(lightning,[(146,17),(158,23),(156,29),(162,35)],'#83c5dda0')
result=flatten([result,lightning],name='storm_scene')

# Water adhering to the cabinet, pole, and motorcycle.
beads=new_canvas(170,170,name='surface_water')
for x,y,n in [(120,65,6),(128,75,8),(132,96,6),(122,111,8),(130,128,5),(117,83,4),(32,81,6),(35,108,5)]:
    beads.line(x,y,x,y+n,'#8ebbd447')
    beads.set(x,y+n,'#b4dbe4a0')
    beads.set(x,y+n+1,'#0a243d90')
for x,y in [(119,57),(126,59),(131,62),(120,89),(129,102),(133,120),(122,138),(115,100),(33,67),(31,123),(48,128),(52,125),(66,119),(80,129),(87,133),(99,121),(108,127),(91,137),(103,144),(109,148),(55,147)]:
    beads.set(x,y,'#dbf4edb0')
    beads.set(x,y+1,'#6c9aaf80')
for pts in [[(88,66),(88,69),(89,71)],[(110,74),(110,78),(109,80)],[(85,87),(85,92),(86,95)],[(113,94),(113,99)]]:
    stroke_poly(beads,pts,'#ffffff57')
# Broken highlights follow the bike's curved, wet fenders.
stroke_poly(beads,[(88,136),(94,136),(100,139),(104,143)],'#98bac46a')
stroke_poly(beads,[(46,137),(45,141),(47,146)],'#a3c7d078')
result=flatten([result,beads],name='wet_scene')

# Sparse background droplets and larger foreground drops retain transparency.
rng=random.Random(713)
rain=new_canvas(170,170,name='rain')
for i in range(160):
    x=rng.randrange(2,169)
    y=rng.randrange(0,164)
    length=rng.choice([2,3,3,4,5])
    alpha=rng.randrange(30,88)
    rain.line(x,y,x-1,y+length,(135,185,207,alpha))
    if i%4==0:
        rain.set(x-1,y+length,(192,224,235,alpha+25))
for x,y,l in [(9,27,7),(25,63,6),(46,11,8),(62,69,7),(14,112,8),(39,95,7),(71,99,7),(96,26,8),(115,14,6),(130,38,7),(151,67,9),(160,105,8),(139,123,7),(68,143,7),(29,136,7),(5,144,6),(155,144,7),(122,135,7),(56,117,5)]:
    rain.line(x,y,x-2,y+l,'#9bc6db78')
    rain.set(x-2,y+l,'#d0edf1ab')
    rain.set(x-1,y+l-1,'#b7dce777')
result=flatten([result,rain],name='result')

# Tiny impact crowns and broken ripples sit on top of the wet pavement.
for x,y,rx in [(13,159,4),(28,151,3),(40,166,4),(64,156,3),(74,165,3),(128,160,4),(146,157,4),(161,165,5),(6,167,3),(117,152,3)]:
    result.line(x-rx,y,x-2,y,'#557c8c')
    result.line(x+2,y,x+rx,y,'#365d70')
    result.set(x-rx+1,y+1,'#3b6275')
    result.set(x+rx-1,y+1,'#718f9c')
    result.set(x,y-1,'#a7c6cc')
    if rx>=4:
        result.set(x-1,y-3,'#8dabbc')
        result.set(x+2,y-2,'#6d93a7')
# Near droplets catch the flash with a translucent, rounded lower edge.
drops=new_canvas(170,170,name='near_droplets')
for x,y in [(18,47),(57,84),(103,13),(145,91),(8,130),(137,146),(76,54),(158,37)]:
    drops.set(x,y,'#a8d6e34a')
    drops.rect(x-1,y+1,2,2,'#abd6e877')
    drops.set(x-1,y+2,'#e0f5ef9a')
    drops.set(x-1,y+3,'#75a5bf40')
result=flatten([result,drops],name='thunderstorm')
view(result,scale=4,margin=0)
save('thunderstorm',result)
finish(result)
