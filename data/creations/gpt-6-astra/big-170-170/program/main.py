import random
random.seed(31)
output = input_canvas.copy(name='output')
# Replace the silhouette beyond the machine with matching nearby sky.
for y in range(68,124):
    for x in range(73,83):
        if y < 112 or x>=78:
            output.set(x,y,input_canvas.get(x-18,y))
# Reconstruct the complete luminous front and its housing.
output.poly([(82,60),(91,57),(115,56),(119,60),(119,146),(82,146)], '#211b43')
output.line(82,62,82,120,'#363050')
output.poly([(85,61),(114,59),(116,61),(116,99),(112,105),(86,110),(84,106),(84,65)], '#b67ab3')
output.poly([(87,62),(113,60),(115,62),(115,98),(111,103),(86,107),(85,104),(85,65)], '#ffe4ce')
output.line(87,61,112,59,'#fbe3ec')
# Subdued warm glow behind merchandise.
output.poly([(88,64),(112,62),(113,97),(110,101),(87,104)], '#efd2b6')
for shelf in [76,88,100]:
    output.line(86,shelf,114,shelf-2,'#737c7a')
    output.line(87,shelf+1,113,shelf-1,'#afb8a2')
# Three orderly rows of cans/bottles, with pixel highlights and labels.
cols=[('#b75c38','#f5ab65'),('#609a84','#a3d6b1'),('#7653a0','#bc8fda'),('#517f9e','#9dd5d9')]
for row in range(3):
    for col in range(4):
        x=88+col*6; y=65+row*12-(col//2)
        dark,light=cols[(col+row)%4]
        output.rect(x+1,y,3,1,'#e1d0ad')
        output.rect(x,y+1,4,8,dark)
        output.line(x,y+2,x,y+7,light)
        output.rect(x+1,y+4,3,2,'#e9debd')
        output.set(x+2,y+1,light)
        output.line(x,y+9,x+3,y+9,'#8e776c')
# Front skirt, payment panel and collection hatch.
output.poly([(85,110),(111,104),(115,105),(115,140),(85,140)],'#252047')
output.poly([(108,108),(115,106),(115,116),(108,118)],'#273e50')
output.line(109,109,113,108,'#73979b')
output.line(109,111,112,110,'#0c1d30')
output.rect(112,113,2,2,'#b1d5ca')
output.poly([(88,124),(106,120),(106,128),(88,132)],'#101b2d')
output.line(89,124,105,121,'#544469')
output.line(118,62,118,141,'#3b2d5c')
# Remove the last coat pixels to the left of the cabinet.
for y in range(109,125):
    for x in range(77,82):
        output.set(x,y,input_canvas.get(x-15,94+(y-109)//2))
# Restore the scooter's unmodified foreground contour over the new cabinet.
tops={78:125,79:124,80:124,81:124,82:124,83:123,84:123,85:123,86:122,87:122,88:122,89:121,90:121,91:121,92:120,93:120,94:120,95:119,96:119,97:118,98:118,99:117,100:117,101:116,102:116,103:116,104:116,105:117,106:118,107:119,108:120,109:121,110:122,111:122,112:122,113:123,114:124,115:137,116:142,117:146,118:149}
for x,top in tops.items():
    for y in range(top,163):
        output.set(x,y,input_canvas.get(x,y))
# A cool storm grade retains the scene's original palette relationships.
original=output.copy(name='restored')
for y in range(170):
    for x in range(170):
        idx=original.get(x,y)
        rgba=original.palette()[idx]['rgba']
        r,g,b,a=rgba
        lit=(85<=x<=116 and 59<=y<=105)
        if lit:
            color=(int(r*.94),int(g*.94),min(255,int(b*.99)),a)
        else:
            color=(int(r*.76),int(g*.85),min(255,int(b*.94)+3),a)
        output.set(x,y,color)
# Lightning behind the architecture, with transparent blue halos.
lightning=new_canvas(170,170,name='lightning')
bolts=[[(101,0),(99,9),(104,16),(97,27),(104,25),(98,37),(94,45),(97,51)],[(98,28),(90,31),(86,39)],[(99,10),(109,14),(113,20)],[(153,29),(148,36),(151,42),(143,51),(147,50),(141,59),(144,66)]]
for pts in bolts:
    for (x1,y1),(x2,y2) in zip(pts,pts[1:]):
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            lightning.line(x1+dx,y1+dy,x2+dx,y2+dy,'#6baed640')
        lightning.line(x1,y1,x2,y2,'#c9edffd8')
output=flatten([output,lightning],name='storm')
# Pools and broken reflections on the foreground pavement.
water=new_canvas(170,170,name='water')
water.poly([(0,154),(15,152),(29,153),(39,156),(32,159),(17,160),(9,158),(0,159)],'#32647772')
water.poly([(120,150),(136,149),(148,152),(164,153),(169,156),(169,169),(132,169),(119,165),(123,161),(116,158)],'#36637588')
water.poly([(41,159),(53,157),(66,158),(70,161),(64,165),(48,166),(36,165)],'#a9bdc754')
water.poly([(75,161),(83,159),(89,160),(93,164),(88,167),(78,166)],'#f7c2b957')
for x,y,w in [(123,154,10),(141,157,18),(126,164,17),(152,167,12),(7,156,13),(20,158,12),(48,162,12),(40,165,8),(80,164,9)]:
    water.line(x,y,x+w,y,'#8dc5d17a')
for x,y,w in [(125,160,9),(130,161,15),(119,167,10),(134,168,17)]:
    water.line(x,y,x+w,y,'#c3a7bb65')
# Thin irregular reflected lightning.
for x,y,w in [(147,152,3),(144,154,6),(146,156,4),(141,159,6),(140,162,7),(143,165,4),(137,168,8)]:
    water.line(x,y,x+w,y,'#bdedee8a')
output=flatten([output,water],name='wet_scene')
# Rain: translucent droplets and short slanted streaks at several depths.
rain=new_canvas(170,170,name='rain')
for i in range(280):
    x=random.randrange(1,169); y=random.randrange(0,168)
    length=random.choices([1,2,3,4,6],[2,4,5,3,1])[0]
    if y+length>=170: continue
    alpha=random.choice(['36','48','62','7a'])
    rain.line(x,y,x-1,y+length,'#a4cbdc'+alpha)
    if length>=4:
        rain.set(x-1,y+length,'#d8edf894')
# Clinging beads on the machine lip, pole and scooter body.
for x,y in [(85,60),(93,58),(108,57),(117,65),(118,82),(118,102),(119,129),(133,78),(133,105),(134,144),(36,35),(36,72),(36,110),(36,146),(56,117),(63,116),(72,120),(89,122),(103,117),(110,124),(83,136),(107,140),(115,153),(50,141)]:
    rain.set(x,y,'#c2e4ecb0')
    rain.set(x,y+1,'#7cbdd68a')
    if random.random()<.35:
        rain.set(x,y+2,'#bce2e8a0')
# Small impact crowns and concentric, broken ripples.
for x,y in [(12,157),(30,163),(58,159),(66,168),(119,155),(135,159),(155,163),(147,151),(6,166),(112,167)]:
    rain.line(x-2,y,x+2,y,'#a6d7df72')
    rain.set(x-3,y-1,'#a6d7df52'); rain.set(x+3,y-1,'#a6d7df52')
    rain.set(x-1,y-2,'#cee9ed8a'); rain.set(x+1,y-3,'#cee9ed75')
    if x%2==0:
        rain.line(x-4,y+2,x-2,y+2,'#75afbf58')
        rain.line(x+1,y+2,x+4,y+2,'#75afbf58')
result=flatten([output,rain],name='result')
view(result,scale=4,margin=0)
finish(result)
