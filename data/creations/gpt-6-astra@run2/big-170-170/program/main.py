import random
import math

result = input_canvas.copy(name='output')

# Restore the sky beside the cabinet, where the raised arm was.
for y in range(68,93):
    for x in range(73,83):
        result.set(x,y,input_canvas.get(x-17,y))

# Reconstruct the cabinet's front. Its original right side is retained.
result.poly([(82,58),(115,56),(118,60),(118,144),(111,146),(79,132),(79,105),(80,74),(80,61)], 'c33')
result.line(81,61,80,126,'c41')
result.line(82,62,81,122,'c43')
result.line(116,60,116,141,'c41')
result.line(117,63,117,140,'c36')
# A softly lit, stepped glass surround.
result.poly([(87,60),(107,59),(107,58),(113,58),(115,60),(115,99),(112,102),(85,104),(83,102),(83,64),(84,62),(87,62)],'c245')
result.poly([(87,61),(112,60),(114,62),(114,98),(112,101),(86,103),(84,101),(84,64)],'c254')
result.line(85,64,85,99,'c242')
result.line(86,63,111,61,'c255')

# Rows of drinks, with glass and shelving matching the surviving products.
def bottle(x,y,h,body,shade,light,cap):
    result.rect(x+1,y,2,2,cap)
    result.rect(x,y+2,4,h-2,body)
    result.line(x+3,y+3,x+3,y+h-1,shade)
    result.line(x,y+3,x,y+h-3,light)
    result.rect(x+1,y+4,2,2,'c242')
    result.set(x+1,y+2,light)

for yy,hh in [(61,6),(68,10),(80,10),(92,9)]:
    result.rect(86,yy,27,hh,'c241')
    result.line(86,yy,112,yy,'c212')

for xx,col,sh,hi in [(87,'c164','c120','c238'),(93,'c223','c70','c237'),(100,'c221','c68','c222'),(107,'c214','c178','c245')]:
    bottle(xx,61,6,col,sh,hi,sh)
bottle(87,68,10,'c164','c120','c238','c142')
bottle(94,68,10,'c224','c69','c237','c223')
bottle(101,68,10,'c87','c83','c236','c85')
bottle(108,68,10,'c87','c83','c236','c85')
bottle(87,80,10,'c165','c142','c249','c163')
bottle(94,80,10,'c221','c68','c222','c157')
bottle(101,80,10,'c214','c191','c245','c192')
bottle(108,80,10,'c214','c191','c245','c192')
for xx in (87,94,101,108):
    bottle(xx,92,9,'c153','c104','c239','c123')
    result.rect(xx,94,4,1,'c249')
    result.set(xx+1,97,'c238')
for yy in (66,78,90):
    result.line(84,yy,114,yy,'c185')
    result.line(84,yy+1,114,yy+1,'c240')
    result.set(85,yy,'c197')
result.line(86,101,112,100,'c244')
# Keep exposed original glass, products and frame on the right side.
for x0,y0,x1,y1 in [(108,58,115,102),(104,59,107,66),(107,67,107,89),(101,91,107,101)]:
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            result.set(x,y,input_canvas.get(x,y))
# Slightly irregular glass glints and bottle labels keep the new shelves textured.
for x,y,col in [(88,69,'c249'),(89,73,'c239'),(95,72,'c223'),(95,75,'c237'),(101,72,'c236'),(102,76,'c85'),(88,82,'c249'),(89,87,'c142'),(95,84,'c222'),(96,88,'c68'),(102,82,'c245'),(102,87,'c191'),(88,96,'c242'),(95,95,'c239'),(96,98,'c104')]:
    result.set(x,y,col)
# Reflections on the display and the lower painted fascia.
result.line(85,65,85,72,'c255')
result.line(85,80,85,85,'c255')
result.line(85,93,85,98,'c255')
result.poly([(83,105),(113,103),(113,109),(83,112)],'c36')
result.line(85,105,110,104,'c43')
result.poly([(97,108),(112,107),(112,113),(96,115)],'c9')
result.line(98,108,111,107,'c43')
result.line(98,113,110,112,'c42')
result.line(100,110,109,109,'c64')
result.line(101,109,110,108,'c54')
result.rect(113,104,2,2,'c185')
result.set(113,104,'c237')
result.poly([(82,116),(94,115),(94,118),(81,123)],'c36')
for xx in range(83,92,2):
    result.line(xx,118,xx,120,'c9')

# Recover the scooter foreground along the cabinet's occlusion boundary.
def inside(x,y,pts):
    odd=False
    j=len(pts)-1
    for i in range(len(pts)):
        xi,yi=pts[i]; xj,yj=pts[j]
        if ((yi>y)!=(yj>y)) and x < (xj-xi)*(y-yi)/(yj-yi)+xi:
            odd=not odd
        j=i
    return odd
scooter=[(75,128),(80,126),(83,123),(90,121),(98,117),(100,115),(104,115),(107,117),(110,120),(113,121),(115,124),(116,133),(118,143),(118,162),(75,162)]
for y in range(114,163):
    for x in range(75,119):
        if inside(x+0.5,y+0.5,scooter):
            result.set(x,y,input_canvas.get(x,y))

# Cool the pavement without changing the scooter or roadside vegetation.
road_colours={'c16':'#242c38','c18':'#28313d','c19':'#30353f','c20':'#26313d','c21':'#2b3542','c22':'#313b49','c23':'#343b49','c24':'#21303d','c49':'#3e434e','c51':'#414652'}
road_indices={result.color(k):v for k,v in road_colours.items()}
for y in range(150,170):
    for x in range(170):
        p=result.get(x,y)
        if p in road_indices:
            result.set(x,y,road_indices[p])

# A restrained cool cast ties the reconstruction into the storm lighting.
shade=new_canvas(170,170,name='storm_shade')
shade.rect(0,0,170,170,'#13203520')
shade.rect(0,0,170,53,'#151a2e28')
result=flatten([result,shade],name='storm_base')

# Broad, broken pools on the road, with horizontal specular reflections.
result.poly([(0,159),(13,157),(30,158),(36,161),(44,161),(43,165),(32,166),(25,169),(0,169)],'#173a4b')
result.poly([(0,162),(14,160),(28,161),(23,163),(34,164),(21,166),(7,165),(0,166)],'#254e60')
result.line(2,162,13,162,'#4e7987')
result.line(15,164,23,164,'#547c87')
result.line(1,168,12,168,'#376575')
result.poly([(117,155),(132,153),(145,154),(153,158),(169,158),(169,169),(119,169),(113,165),(126,160)],'#1c3b4b')
result.poly([(130,158),(145,157),(152,161),(166,161),(169,164),(159,166),(140,165),(145,162),(128,161)],'#34596c')
result.line(139,158,147,158,'#65808f')
result.line(155,164,167,164,'#52788a')
result.line(131,161,139,161,'#74939f')
result.line(145,168,158,168,'#315362')
result.poly([(56,161),(65,159),(71,160),(72,162),(77,164),(73,166),(62,165),(56,167),(52,166)],'#263e4c')
result.line(57,163,65,163,'#64808a')
result.line(65,165,70,165,'#77929a')

# Warm light from the machine fractures into thin horizontal pool reflections.
rng=random.Random(207)
for y in range(151,170):
    if y in (153,156,160,164,167):
        continue
    center=98+rng.randint(-4,5)
    width=rng.randint(4,11)
    col=rng.choice(['#ad99ac','#8b839d','#71758e','#d6bdc2','#a9b0bd'])
    result.line(center-width//2,y,center+width//2,y,col)
    if y%3==0:
        result.line(center+width//2+2,y,center+width//2+5,y,'#565a75')
result.line(111,154,119,154,'#716c90')
result.line(116,156,126,156,'#55516f')
result.line(119,159,124,159,'#8f8cac')
result.line(42,161,49,161,'#cfbfbd')
result.line(48,158,55,158,'#bbb9bc')
result.line(51,157,58,157,'#e2d9cf')

# Forked lightning, with a narrow translucent halo, behind the street objects.
bolt=[(96,0),(89,12),(92,12),(80,29),(85,28),(68,49),(74,47),(61,67),(64,66),(57,79)]
branches=[[(82,26),(71,28),(67,35),(56,38),(51,47)],[(70,48),(79,57),(76,64)],[(90,10),(104,17),(102,23),(110,28)]]
lightning=new_canvas(170,170,name='lightning')
def stroke(points,col,dx=0,dy=0):
    for a,b in zip(points,points[1:]):
        lightning.line(a[0]+dx,max(0,a[1]+dy),b[0]+dx,max(0,b[1]+dy),col)
for off in (-2,2):
    stroke(bolt,'#73a5ee16',off,0)
    stroke(bolt,'#73a5ee16',0,off)
for off in (-1,1):
    stroke(bolt,'#88b9f356',off,0)
    stroke(bolt,'#88b9f356',0,off)
for branch in branches:
    stroke(branch,'#91b9e25f',1,0)
    stroke(branch,'#b8d7f4b8')
stroke(bolt,'#e6f4ffef')
lightning.set(89,12,'#ffffff')
lightning.set(80,29,'#ffffff')
lightning.set(68,49,'#ffffff')
result=flatten([result,lightning],name='lit_scene')

# Tiny pooled rivulets and clinging beads catch the flash on exposed surfaces.
water=new_canvas(170,170,name='surface_water')
water.line(35,22,35,39,'#567a8d70')
water.line(35,53,35,78,'#5578875c')
water.line(35,88,35,113,'#597a8a55')
water.line(35,120,35,143,'#5e7c8780')
water.line(118,62,118,81,'#6b88a676')
water.line(118,86,118,106,'#6b88a666')
water.line(132,90,132,112,'#6b88a64c')
water.line(132,117,132,137,'#6b88a650')
water.line(83,59,96,57,'#abc4dbb0')
water.line(103,56,112,56,'#e1e6f2c2')
water.line(120,145,131,144,'#7f9ab7b0')
for x,y in [(35,27),(35,55),(35,88),(35,122),(35,139),(117,68),(118,83),(118,111),(132,95),(132,119),(131,140),(85,61),(95,58),(107,57),(51,118),(60,116),(69,118),(50,128),(57,132),(84,128),(95,123),(104,119),(110,137),(113,146),(101,155)]:
    water.set(x,y,'#658ca693')
    water.set(x,y+1,'#bde2ecd5')
    if y%3==0:
        water.set(x+1,y+1,'#739ab59c')
        water.set(x,y+2,'#213a52b0')
# Fine wet edge highlights on the bike's body and wheels.
water.line(58,117,65,116,'#e5d4d5af')
water.line(87,125,94,122,'#a5cad7c0')
water.line(100,117,104,117,'#e1f0f3cc')
water.line(109,137,112,142,'#90bdccb0')
water.line(50,139,50,144,'#6ca3b9a0')
water.line(97,153,102,155,'#7099aab0')
water.set(106,156,'#c4e0e7bd')
for x,y in [(131,75),(120,95),(131,111),(119,126),(35,102),(35,132),(91,124),(59,119),(108,139)]:
    water.set(x,y-1,'#7b9db67b')
    water.set(x-1,y,'#b6d6e4ad')
    water.set(x,y,'#25495a85')
    water.set(x+1,y,'#8bacbe71')
    water.set(x,y+1,'#d5edf4d5')
result=flatten([result,water],name='wet_scene')

# Raindrops are painted with partial alpha and then composited over the scene.
rain=new_canvas(170,170,name='translucent_rain')
rng=random.Random(430)
for i in range(175):
    x=rng.randrange(2,168)
    y=rng.randrange(0,168)
    length=rng.choices([2,3,4,5,6],[3,5,5,2,1])[0]
    length=min(length,169-y)
    alpha=rng.choice([40,52,64,82,104])
    rain.line(x,y,x-1,y+length,(150,193,216,alpha))
    rain.set(x-1,y+length,(192,223,237,alpha+32))
# A few close droplets have a glassy body and a brighter lower edge.
for x,y in [(12,25),(47,10),(65,89),(153,53),(23,93),(143,121),(18,137),(69,146),(155,17),(122,35),(75,123),(59,52)]:
    rain.line(x,y,x-1,y+4,'#9cc8df6e')
    rain.rect(x-2,y+4,2,2,'#8ebbd277')
    rain.set(x-2,y+5,'#d1eff4bc')
result=flatten([result,rain],name='storm_rain')

# Rain striking standing water: low elliptical rings and small crown splashes.
splashes=new_canvas(170,170,name='rain_impacts')
for x,y,rx in [(13,161,4),(28,166,3),(40,154,2),(64,162,3),(81,167,4),(123,163,4),(146,160,3),(159,168,4),(8,153,2),(136,154,2)]:
    splashes.line(x-rx+1,y-1,x+rx-1,y-1,'#86adbd6c')
    splashes.set(x-rx,y,'#729fb57c')
    splashes.set(x+rx,y,'#729fb57c')
    splashes.line(x-rx+1,y+1,x+rx-1,y+1,'#a7d0dc9a')
for x,y in [(18,158),(38,166),(57,160),(76,156),(128,160),(150,164),(161,153)]:
    splashes.set(x,y-2,'#c3dfe7b2')
    splashes.set(x-2,y-1,'#9cbfcd91')
    splashes.set(x+2,y-1,'#9cbfcd91')
    splashes.line(x-1,y,x+1,y,'#89aabbb5')
result=flatten([result,splashes],name='output_final')
view(result,scale=4,margin=0)
finish(result)
