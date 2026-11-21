import math

# A compact, right-facing supersport motorcycle. All marks are native pixels.
result = new_canvas(128, 128, name='midnight_sport')
c = result
P = {
 'ink':'#090c11', 'rubber':'#11151b', 'tire':'#20262e', 'tirehi':'#323b44',
 'deep':'#151a21', 'black':'#1c222b', 'body':'#2c333d', 'mid':'#3c4550',
 'edge':'#596572', 'steelDark':'#4c5963', 'steel':'#7e8e99',
 'silver':'#b4c2c9', 'light':'#dae2e5', 'white':'#f5f7f2',
 'redDark':'#771d2b', 'red':'#bf2838', 'redLight':'#f34d50', 'redHi':'#ff9390'
}
def col(k): return P.get(k,k)
def poly(pts,k): c.poly(pts,col(k))
def line(x1,y1,x2,y2,k): c.line(x1,y1,x2,y2,col(k))
def path(d,k,fill=True): c.path(d,col(k),fill=fill)
def stroke(a,b,w,k):
    x,y=a; u,v=b; dx=u-x; dy=v-y; length=math.hypot(dx,dy)
    nx=-dy/length*w/2; ny=dx/length*w/2
    poly([(round(x+nx),round(y+ny)),(round(u+nx),round(v+ny)),(round(u-nx),round(v-ny)),(round(x-nx),round(y-ny))],k)
    c.circle(x,y,max(0,int(w/2)),col(k)); c.circle(u,v,max(0,int(w/2)),col(k))

def wheel(cx,cy,r):
    c.circle(cx,cy,r,P['ink'])
    c.circle(cx,cy,r-1,P['rubber'])
    # Deliberate stepped shoulder highlights keep the tire dark and thick.
    c.path(f'M {cx-r+2} {cy+4} Q {cx-r-1} {cy-10} {cx-9} {cy-r+3} Q {cx} {cy-r-1} {cx+10} {cy-r+4}',P['tirehi'],fill=False)
    c.path(f'M {cx-r+3} {cy+8} Q {cx-10} {cy+r} {cx+2} {cy+r-2} Q {cx+13} {cy+r-2} {cx+r-2} {cy+5}',P['tire'],fill=False)
    for ang in (195,220,245,275,300,325,15,45,70,105,135,160):
        a=math.radians(ang)
        x=round(cx+(r-2)*math.cos(a)); y=round(cy+(r-2)*math.sin(a))
        xx=round(cx+(r-4)*math.cos(a+.055)); yy=round(cy+(r-4)*math.sin(a+.055))
        c.line(x,y,xx,yy,P['tire'])
    rr=r-6
    c.circle(cx,cy,rr+1,P['steelDark'])
    c.circle(cx,cy,rr,P['silver'])
    c.circle(cx,cy,rr-1,P['deep'])
    c.circle(cx,cy,rr-2,None)
    # Six swept silver-white alloy spokes, with darker trailing edges.
    for ang in range(-90,270,60):
        a=math.radians(ang)
        def pt(rad,off=0): return (round(cx+rad*math.cos(a+off)),round(cy+rad*math.sin(a+off)))
        poly([pt(3,-.38),pt(rr-1,-.05),pt(rr-1,.13),pt(7,.24),pt(3,.55)],'steel')
        line(*pt(4,.05),*pt(rr-1,.02),'white')
        line(*pt(5,.12),*pt(9,.16),'light')
    # Red valve mark on rim.
    c.set(cx+rr-2,cy+5,P['redLight'])
    c.circle(cx,cy,4,P['steelDark'])
    c.circle(cx,cy,3,P['silver'])
    c.circle(cx,cy,1,P['ink'])

wheel(25,87,20)
wheel(104,87,19)
# Brake rotors are separate, so the perforations reveal the original spokes.
rotors = new_canvas(128,128,name='rotors')
for cx,cy,r in [(25,87,7),(104,87,9)]:
    rotors.circle(cx,cy,r,P['steelDark'])
    rotors.circle(cx,cy,r-1,P['silver'])
    rotors.circle(cx,cy,r-3,None)
    for ang in range(0,360,45):
        a=math.radians(ang)
        rotors.set(round(cx+(r-2)*math.cos(a)),round(cy+(r-2)*math.sin(a)),P['steelDark'])
    rotors.circle(cx,cy,3,P['steel'])
    rotors.circle(cx,cy,1,P['white'])
c.blit(rotors,0,0)

# Far-side chassis, chain drive and rear suspension.
poly([(18,46),(37,47),(62,58),(53,67),(31,55),(16,51)],'ink')
poly([(20,47),(36,49),(53,57),(49,60),(29,53)],'steelDark')
line(21,47,41,53,'silver')
poly([(24,85),(48,68),(62,75),(58,83),(28,92),(22,91)],'ink')
poly([(25,85),(49,72),(57,76),(54,80),(28,89)],'steel')
poly([(29,86),(49,75),(53,76),(49,79),(29,88)],'deep')
line(27,84,48,72,'light')
line(29,90,53,82,'steelDark')
line(24,93,58,85,'ink')
line(24,92,57,84,'steelDark')
for x in range(28,54,4): c.set(x,92-(x-24)//4,P['silver'])
stroke((39,54),(49,74),5,'ink')
stroke((40,55),(49,73),2,'silver')
for j in range(6):
    x=39+j; y=56+2*j
    line(x-2,y+1,x+4,y-1,'redDark')
    line(x-2,y,x+3,y-2,'redLight')

# Rear hugger and a very small tail support.
path('M 9 70 Q 16 62 29 64 L 36 68 L 33 71 Q 22 65 10 73 Z','ink')
path('M 12 69 Q 22 64 31 67','body',False)
poly([(16,46),(20,47),(14,59),(9,61),(8,58),(12,56)],'ink')
line(10,59,14,58,'steelDark')

# A tubular alloy frame, visible behind the engine and fairing.
for a,b in [((40,52),(64,57)),((64,57),(51,80)),((40,52),(51,80)),((51,80),(76,79)),((64,57),(76,79))]:
    stroke(a,b,5,'ink')
    stroke(a,b,3,'steel')
    line(a[0],a[1]-1,b[0],b[1]-1,'light')

# Engine block and cooling ribs.
poly([(54,58),(69,58),(77,68),(76,82),(66,87),(51,83),(46,75),(48,65)],'ink')
poly([(55,60),(67,60),(73,67),(71,76),(51,77),(50,67)],'steelDark')
poly([(55,59),(66,59),(70,65),(53,65)],'steel')
for y in (63,66,69):
    line(52,y,69,y,'deep')
    line(53,y+1,69,y+1,'silver')
c.circle(60,77,11,P['ink'])
c.circle(60,77,9,P['steelDark'])
c.circle(59,76,8,P['steel'])
c.circle(59,76,6,P['silver'])
path('M 53 77 Q 52 69 60 69 Q 65 70 66 74','light',False)
path('M 54 81 Q 61 86 66 79','steelDark',False)
c.circle(60,77,3,P['steel'])
line(58,76,62,76,'silver')
for x,y in [(52,73),(63,69),(67,79),(57,84)]:
    c.set(x,y,P['ink']); c.set(x,y-1,P['light'])

# Curved exhaust header and compact brushed-metal silencer.
path('M 72 72 Q 81 81 74 88 Q 70 93 59 88','ink',False)
path('M 73 74 Q 79 83 72 88 L 58 87','steel',False)
path('M 73 76 Q 77 83 71 87 L 61 86','light',False)
poly([(39,79),(43,78),(60,86),(64,91),(61,95),(41,88),(36,83)],'ink')
poly([(40,80),(44,80),(60,87),(61,91),(58,92),(41,86),(38,83)],'steel')
poly([(43,81),(57,87),(57,90),(42,85)],'light')
poly([(37,81),(40,80),(43,84),(41,87),(37,84)],'deep')
line(38,81,40,84,'steelDark')
line(45,85,55,89,'silver')
line(57,86,55,90,'steelDark')

# Swept tail shell, bright red tail lamp and inset saddle.
poly([(9,36),(23,35),(35,39),(46,44),(45,50),(34,52),(18,46),(10,42)],'ink')
poly([(10,37),(22,37),(37,42),(43,46),(34,48),(18,43)],'body')
poly([(13,36),(23,36),(36,41),(28,40),(16,39)],'edge')
poly([(13,41),(24,43),(34,48),(25,46),(14,44)],'redDark')
poly([(10,38),(18,39),(20,42),(11,41)],'red')
line(11,38,17,39,'redLight')
c.set(11,39,P['redHi'])
poly([(28,40),(37,41),(49,46),(51,50),(39,50),(29,45),(25,44)],'ink')
line(30,41,37,42,'mid')
line(37,42,47,46,'mid')
poly([(40,48),(49,49),(54,53),(48,56),(39,52)],'black')

# Sculpted fuel tank with a cool, narrow highlight.
path('M 43 46 L 48 40 Q 52 36 58 35 L 67 35 Q 74 37 78 44 L 81 52 L 71 58 L 52 53 L 45 50 Z','ink')
path('M 46 46 L 50 41 Q 55 37 60 37 L 66 37 Q 72 38 75 44 L 77 50 L 69 54 L 53 51 Z','body')
poly([(50,41),(57,38),(66,38),(71,40),(73,43),(65,41),(57,41),(48,46)],'mid')
line(54,38,64,37,'edge')
line(65,37,69,39,'edge')
poly([(49,47),(56,48),(68,50),(75,47),(76,51),(69,55),(53,52)],'black')
line(54,51,68,54,'redDark')
poly([(59,35),(65,35),(68,37),(63,38),(58,37)],'ink')
line(60,36,65,36,'steel')

# Steering head, clip-on bar and a small angled smoked windscreen.
stroke((81,46),(89,53),4,'steelDark')
line(79,43,89,42,'ink')
line(79,42,85,42,'steel')
poly([(80,42),(76,33),(77,30),(81,31),(94,41),(98,46),(88,48)],'ink')
poly([(78,33),(81,33),(91,41),(93,44),(83,42)],'black')
line(78,33,81,39,'mid')
line(82,34,88,39,'body')
poly([(83,41),(91,42),(94,46),(86,46)],'deep')
# Single compact stalk mirror.
line(88,40,91,35,'ink')
poly([(90,33),(96,33),(99,35),(96,37),(91,36),(89,35)],'ink')
line(91,34,96,34,'mid')

# Front fork: silver telescopic legs with a strong forward rake.
stroke((87,50),(103,85),6,'ink')
stroke((88,51),(103,84),4,'steelDark')
stroke((91,58),(102,82),3,'silver')
line(91,57,102,81,'white')
poly([(100,80),(105,82),(107,88),(102,91),(99,87)],'steelDark')
line(101,82,103,87,'silver')
c.circle(104,87,2,P['silver']); c.set(104,87,P['ink'])
# Brake caliper behind the front fork leg.
poly([(94,81),(97,80),(100,84),(100,90),(97,93),(93,90)],'ink')
poly([(95,82),(97,83),(98,87),(97,90),(95,89)],'steel')
line(95,84,96,87,'light')

# Broad aerodynamic nose and deep side fairing.
# The upper side panel wraps around the circular crankcase, leaving the
# silver trellis visible along its left edge.
poly([(56,54),(66,52),(76,56),(80,65),(78,76),(71,84),(67,81),(70,73),(65,66),(57,62)],'ink')
poly([(58,55),(66,54),(75,58),(77,65),(75,74),(71,78),(71,71),(65,64),(59,61)],'body')
poly([(59,55),(66,54),(73,57),(68,59),(61,58)],'mid')
line(59,55,65,54,'edge')
poly([(61,59),(71,60),(74,64),(65,63)],'ink')
line(63,60,70,61,'steelDark')
line(66,64,72,66,'black')
c.set(60,57,P['silver'])
path('M 76 44 L 88 43 L 97 44 L 106 48 L 111 54 L 109 60 L 98 64 L 93 76 L 87 88 L 83 93 L 65 93 L 59 88 L 67 85 L 72 77 L 73 63 L 68 58 Z','ink')
path('M 78 46 L 88 45 L 97 47 L 104 50 L 108 54 L 106 58 L 96 61 L 90 75 L 84 88 L 68 90 L 64 88 L 72 83 L 76 75 L 76 61 L 72 57 Z','body')
# Nose bevel, curved grey panel and small headlight.
poly([(79,46),(88,45),(97,47),(103,50),(94,49),(83,49),(75,54)],'mid')
line(81,46,89,46,'edge')
poly([(101,50),(106,52),(108,55),(102,55),(98,52)],'ink')
line(102,51,106,53,'light')
c.set(107,54,P['silver'])
poly([(79,53),(93,50),(99,53),(93,60),(88,70),(83,80),(76,82),(79,67)],'mid')
poly([(82,55),(92,52),(94,53),(88,61),(84,70),(82,75),(80,76)],'edge')
# Deep inset gill and sharp red sweep.
poly([(76,59),(88,57),(84,64),(79,70),(75,70)],'ink')
line(77,60,85,59,'steelDark')
line(77,64,81,63,'black')
poly([(74,73),(81,71),(93,60),(105,57),(102,61),(95,64),(83,78),(73,82)],'redDark')
poly([(75,73),(81,72),(94,60),(106,57),(102,60),(95,63),(82,76),(74,79)],'red')
line(83,71,94,61,'redLight')
line(95,61,103,58,'redLight')
# Belly pan steps around the engine.
poly([(72,83),(81,81),(88,76),(85,86),(81,91),(67,91),(63,88)],'deep')
line(69,91,80,91,'steelDark')
poly([(71,87),(81,85),(83,83),(81,88),(69,90),(66,88)],'red')
line(71,87,80,85,'redLight')
# Fairing fasteners and small race-panel slash.
for x,y in [(77,51),(96,56),(77,80),(82,88)]:
    c.set(x,y,P['ink']); c.set(x,y-1,P['silver'])
line(86,53,90,52,'silver')
line(85,55,88,54,'silver')

# Front fender sits closely over the tread, leaving the wheel leg readable.
path('M 86 75 Q 90 66 101 65 Q 112 64 119 74 L 116 76 Q 110 70 102 70 Q 93 70 88 78 Z','ink')
path('M 88 73 Q 94 66 102 67 Q 111 66 116 72 L 115 73 Q 103 67 91 74 Z','body')
path('M 92 69 Q 102 64 112 70','edge',False)
line(112,70,116,73,'red')
# The exposed lower fork continues over the fender.
stroke((98,74),(102,83),3,'steelDark')
line(98,74,102,83,'light')
c.circle(104,87,2,P['steel']); c.set(104,87,P['white'])

# Rearset, pivot bolts, and small mechanical highlights.
poly([(45,73),(49,70),(53,73),(49,81),(46,81)],'ink')
poly([(47,74),(49,72),(51,74),(48,79)],'silver')
line(44,79,51,80,'steelDark')
line(43,78,49,78,'light')
c.circle(25,87,3,P['steelDark']); c.circle(25,87,2,P['silver']); c.set(25,87,P['ink'])
c.circle(50,79,2,P['steelDark']); c.set(50,79,P['white'])

# Validate the requested output dimensions, limited palette, and alpha.
info = result.stats()
assert info['size'] == (128, 128) or info['size'] == [128, 128]
assert info['colors_used'] <= 86
assert info['visible_pixels'] < 128 * 128
print(result.stats_text())
view(result,scale=4,margin=0)
save('midnight_sport',result)
finish(result)
