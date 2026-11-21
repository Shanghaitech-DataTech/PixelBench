import random

output = input_canvas.copy(name='restored_scene')
# Reconstruct the obscured machine on an independent layer.
machine = new_canvas(170,170,name='restored_machine')
machine.poly([(82,60),(117,55),(118,145),(82,149)], '#201b50')
machine.line(82,62,82,141,'#35305f')
machine.line(83,62,83,139,'#514273')
machine.line(116,57,117,144,'#403568')
# Recessed illuminated display, with a gentle rise in perspective to the right.
machine.poly([(85,62),(112,59),(115,61),(115,101),(112,104),(85,107)], '#b98bb5')
machine.poly([(86,63),(112,60),(114,62),(114,100),(112,102),(86,105)], '#f1d6d1')
machine.poly([(86,64),(111,61),(113,62),(113,99),(110,101),(86,104)], '#ddc9bd')
# Shelf lighting and back panels follow the original machine's perspective.
for y in [66,78,90]:
    machine.poly([(86,y),(113,y-3),(113,y+7),(86,y+10)], '#c7b4b0')
    machine.line(86,y,112,y-3,'#fceadc')
    machine.line(86,y+10,113,y+7,'#7a8791')
    machine.line(86,y+11,113,y+8,'#f2d9d5')
# Small drinks with shaded sides, paper labels, lids, and glass highlights.
for row,y in enumerate([66,78,90]):
    for j,x in enumerate([88,94,100,106]):
        yy=y-(x-86)//9
        body,shade,light=[('#bd734d','#875b49','#e9a777'),('#72aaa1','#527a85','#b6d8c2'),('#7f82b5','#5b6196','#b8b7da'),('#b27aa6','#80658f','#e4bdd4')][(j+row)%4]
        if row==0:
            machine.rect(x+1,yy,2,1,'#d3d7d1')
            machine.rect(x,yy+1,4,7,shade)
            machine.rect(x,yy+1,3,6,body)
            machine.line(x,yy+2,x,yy+5,light)
            machine.rect(x+1,yy+4,2,2,'#dfd7ca')
        elif row==1:
            machine.rect(x+1,yy,2,2,shade)
            machine.rect(x+1,yy,2,1,'#d8e2d5')
            machine.rect(x,yy+2,4,6,shade)
            machine.rect(x,yy+2,3,5,body)
            machine.set(x,yy+3,light)
            machine.rect(x+1,yy+4,2,2,'#e4dace')
        else:
            machine.rect(x,yy+1,4,7,shade)
            machine.rect(x,yy+1,3,6,body)
            machine.line(x,yy+1,x+2,yy+1,'#e8d9cd')
            machine.rect(x,yy+3,3,2,'#e8c8b8')
            machine.set(x,yy+6,light)
# Display frame, subtle reflected bands, price tabs.
machine.line(85,63,85,105,'#f9e6db')
machine.line(114,63,114,100,'#f3d7dd')
for y in [77,89,101]:
    for x in [88,94,100,106]:
        yy=y-(x-86)//9
        machine.line(x,yy,x+2,yy,'#a09ba6')
        machine.set(x+1,yy,'#efe3d7')
# Lower steel fascia, payment panel and collection recess.
machine.poly([(85,109),(114,105),(115,129),(85,133)], '#292748')
machine.line(86,109,112,105,'#655775')
machine.poly([(104,108),(112,107),(112,116),(104,117)], '#171c32')
machine.line(105,109,110,108,'#809997')
machine.line(106,111,110,110,'#0c152a')
machine.rect(108,113,2,2,'#8caf9c')
machine.set(108,113,'#c0dfc3')
machine.poly([(87,120),(103,118),(103,125),(87,127)], '#111a2b')
machine.line(88,120,102,118,'#554663')
machine.line(88,126,102,124,'#4e5267')

# Exact character silhouette; keep the parked bike and the rest of the scene.
removal = new_canvas(170,170,name='character_mask')
removal.poly([(89,61),(99,60),(105,63),(108,68),(106,75),(104,78),(107,84),(108,90),(104,97),(102,102),(105,109),(105,116),(98,117),(94,120),(88,123),(86,125),(79,124),(79,108),(79,99),(81,92),(81,90),(77,90),(75,87),(74,83),(73,78),(74,75),(77,71),(80,70),(84,71),(85,66)], '#ffffff')
for y in range(60,126):
    for x in range(73,118):
        in_machine = (82 <= x <= 115 and 63 <= y <= 114)
        if removal.get(x,y) != 0 or in_machine:
            if x >= 82:
                output.set(x,y,machine.get(x,y))
            else:
                output.set(x,y,input_canvas.get(x-22,y))
# Finish the upper border and clear the narrow background strip at the left.
for y in range(58,64):
    for x in range(82,116):
        if machine.get(x,y) != 0:
            output.set(x,y,machine.get(x,y))
for y in range(108,125):
    for x in range(79,82):
        output.set(x,y,'#14283a')
output.line(79,124,81,124,'#0e222c')

# The approaching flash lights the existing cloud texture in cool blue tiers.
import math
pal={p['index']:p['rgba'] for p in output.palette()}
for y in range(111):
    for x in range(170):
        r,g,b,a=pal[output.get(x,y)]
        if b > r+15 and g > r+10 and (x<80 or y<51 or x>135):
            d=((x-85)/65)**2+((y-26)/62)**2
            glow=max(0, 4-int(d*4))
            # Discrete tones retain the original pixel clusters.
            output.set(x,y,(max(0,r-1)+glow*4,max(0,g-5)+glow*5,max(0,b-4)+glow*8))

# Forked bolts are behind every foreground object.
bolts=[[(91,2),(87,11),(92,17),(81,29),(85,29),(76,40),(79,39),(69,57),(73,55),(65,72)],
       [(89,14),(100,20),(98,26),(108,33),(106,38),(114,45)],
       [(80,34),(68,37),(65,44),(57,48),(55,55)],
       [(154,16),(150,25),(155,32),(145,44),(149,43),(143,57),(147,55),(139,75),(142,73),(138,87)],
       [(151,27),(162,36),(159,42),(166,50)]]
light = new_canvas(170,170,name='lightning_halo')
for n,pts in enumerate(bolts):
    for a,b in zip(pts,pts[1:]):
        for dx,dy in [(-2,0),(2,0),(0,-2),(0,2)]:
            light.line(a[0]+dx,a[1]+dy,b[0]+dx,b[1]+dy,(117,156,240,18 if n else 30))
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            light.line(a[0]+dx,a[1]+dy,b[0]+dx,b[1]+dy,(127,180,243,42 if n else 75))
        light.line(*a,*b,(185,224,250,150 if n in [1,2,4] else 220))
output = flatten([output,light],name='storm_lighting')
for n,pts in enumerate(bolts):
    if n in [0,3]:
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            output.line(*a,*b,'#e4f4f5' if n==0 else '#bfdfe7')
output.set(90,3,'#ffffff')
output.line(82,26,80,29,'#effcff')

# Wet tarmac preserves the bike, pole, vegetation and existing warm reflections.
ground = new_canvas(170,170,name='wet_pavement_mask')
ground.poly([(0,153),(6,150),(34,149),(44,148),(49,153),(61,155),(68,153),(74,151),(81,152),(88,156),(98,161),(110,161),(117,156),(119,150),(134,151),(145,154),(158,154),(169,158),(169,169),(0,169)], '#ffffff')
pal={p['index']:p['rgba'] for p in output.palette()}
for y in range(148,170):
    for x in range(170):
        if ground.get(x,y) != 0:
            r,g,b,a=pal[output.get(x,y)]
            output.set(x,y,(int(r*.67+5),int(g*.7+11),int(b*.79+16)))
water=new_canvas(170,170,name='puddles')
# Shallow broken pools; sharp horizontal glints flatten them onto the road.
water.poly([(0,158),(5,156),(23,156),(28,158),(39,159),(37,161),(24,162),(29,164),(9,163),(4,161),(0,161)], '#173441')
water.poly([(119,154),(131,153),(140,154),(141,156),(153,157),(163,157),(169,160),(169,163),(156,163),(151,165),(129,164),(116,166),(109,164),(119,161),(127,159)], '#254654')
water.poly([(2,167),(24,166),(31,168),(38,168),(38,169),(0,169)], '#214756')
water.poly([(48,159),(57,158),(65,157),(69,159),(66,160),(61,160),(57,162),(45,163),(39,162)], '#585967')
water.poly([(78,159),(85,157),(93,160),(95,161),(91,164),(84,164),(77,162)], '#85828d')
water.poly([(120,157),(132,156),(139,157),(135,158),(126,158),(122,160),(115,160)], '#554f73')
water.line(129,154,136,154,'#63748b')
water.line(124,155,130,155,'#9b8aab')
water.line(131,159,141,159,'#6b658a')
water.line(114,162,127,162,'#56566f')
water.line(133,163,143,163,'#394f69')
water.line(150,159,164,159,'#416477')
water.line(159,160,168,160,'#547c8a')
water.line(4,157,21,157,'#355665')
water.line(14,159,30,159,'#39596b')
water.line(3,161,12,161,'#638292')
water.line(6,167,24,167,'#527989')
water.line(47,160,60,160,'#9a8c98')
water.line(53,159,67,159,'#d2bbbc')
water.line(78,160,85,160,'#dfc9c5')
water.line(83,162,90,162,'#b0a8b2')
water.line(86,163,92,163,'#5f657b')
# A faint, fragmented reflection of the flash at the left edge.
for x,y,w,col in [(14,152,3,'#557986'),(12,154,6,'#6e8e9b'),(17,156,3,'#90b1bd'),(14,160,7,'#6b91a3'),(18,162,4,'#abd0d3'),(11,165,6,'#61899d'),(14,168,10,'#7595ab')]:
    water.line(x,y,x+w,y,col)
# Composite water only where pavement is exposed.
for y in range(148,170):
    for x in range(170):
        if ground.get(x,y) != 0 and water.get(x,y) != 0:
            output.set(x,y,water.get(x,y))

# Water beads cling to metal lips, the seat, mudguards and glass.
surface=new_canvas(170,170,name='clinging_water')
surface.line(86,60,111,57,(185,217,236,110))
surface.line(118,57,131,61,(118,158,193,75))
surface.line(116,63,116,139,(151,177,214,65))
surface.line(134,67,134,143,(103,154,180,75))
surface.line(86,106,112,102,(222,228,239,100))
surface.line(88,116,103,113,(149,183,197,100))
surface.line(57,118,68,115,(204,217,220,100))
surface.line(85,125,103,117,(167,209,220,80))
surface.line(105,135,111,142,(153,204,220,100))
surface.line(36,14,36,143,(112,159,170,43))
# Glass rivulets with intermittent highlights.
for x,y,length in [(87,65,11),(110,80,12),(98,64,7),(113,90,7),(125,76,17),(130,111,13),(120,131,6)]:
    surface.line(x,y,x,y+length,(134,182,214,48))
    surface.set(x,y+length,(192,228,240,140))
    surface.set(x,y+length-1,(109,168,199,105))
for x,y in [(88,61),(97,60),(109,59),(116,69),(116,91),(116,110),(134,85),(134,124),(130,145),(124,144),(87,107),(102,105),(58,118),(65,117),(72,119),(86,125),(96,121),(104,118),(111,139),(115,149),(52,143),(33,64),(36,99)]:
    surface.set(x,y,(205,234,241,165))
    surface.set(x,y+1,(113,173,199,128))
# Ground droplets and small splash crowns sit on top of the standing water.
for x,y in [(7,153),(27,154),(39,159),(44,166),(59,165),(70,155),(75,168),(101,166),(119,153),(139,156),(151,168),(164,165),(32,166)]:
    surface.line(x-2,y,x+2,y,(102,156,181,95))
    surface.set(x-1,y-1,(183,219,230,155))
    surface.set(x+1,y-1,(153,205,223,125))
    surface.set(x,y,(211,232,238,190))
for x,y in [(20,160),(62,166),(135,161),(153,154),(8,168)]:
    surface.line(x-3,y,x-1,y,(120,174,193,110))
    surface.line(x+2,y,x+4,y,(120,174,193,110))
    surface.line(x-1,y+1,x+2,y+1,(147,191,204,130))
    surface.set(x,y-2,(210,232,237,190))
# Rounded, transparent beads with a bright upper lip and a darker meniscus.
for x,y in [(125,96),(132,132),(117,77),(36,121),(69,118),(108,137),(24,164),(51,155),(121,166),(145,158)]:
    surface.set(x,y-1,(169,213,227,65))
    surface.line(x-1,y,x+1,y,(138,188,209,95))
    surface.line(x-1,y+1,x+1,y+1,(73,132,166,112))
    surface.set(x-1,y,(223,240,242,200))
    surface.set(x,y+2,(128,182,201,95))
# Thin elliptical ripple fragments and torn reflection edges.
for x,y in [(28,157),(47,167),(123,158),(147,164)]:
    surface.line(x-3,y-1,x+2,y-1,(127,176,195,85))
    surface.set(x-4,y,(148,198,213,120))
    surface.set(x+4,y,(148,198,213,100))
    surface.line(x-2,y+1,x+2,y+1,(180,212,223,120))
for x,y,w in [(8,159,3),(27,160,4),(40,163,2),(62,162,3),(79,164,4),(114,165,3),(134,157,5),(155,162,4),(164,167,3)]:
    surface.line(x,y,x+w,y,(161,193,211,70))
output=flatten([output,surface],name='wet_scene')

# Actual alpha droplets: variable opacity and size give rain depth.
rain=new_canvas(170,170,name='translucent_rain')
rng=random.Random(822)
for i in range(235):
    x=rng.randrange(2,169); y=rng.randrange(0,168)
    length=rng.choice([2,3,3,4,5,6])
    dx=1 if length<5 else 2
    y2=min(169,y+length)
    opacity=rng.choice([24,35,45,58,72])
    if 84<x<115 and 60<y<104:
        opacity=int(opacity*.65)
    rain.line(x,y,max(0,x-dx),y2,(153,197,217,opacity))
    if i%4==0:
        rain.set(max(0,x-dx),y2,(190,222,234,opacity+36))
# Larger nearby droplets have a clear core and translucent shaded side.
for x,y in [(11,29),(21,85),(48,55),(62,14),(73,91),(124,29),(143,10),(160,70),(151,114),(15,131),(40,112),(66,135),(123,128),(158,145),(6,64),(107,47)]:
    rain.line(x+1,y,x,y+4,(158,204,228,90))
    rain.line(x,y+2,x-1,y+5,(172,214,232,128))
    rain.set(x-1,y+6,(215,238,243,175))
    rain.set(x,y+5,(111,170,204,80))
result=flatten([output,rain],name='thunderstorm')
save('thunderstorm_scene',result)
view(result,scale=4,margin=0)
finish(result)
