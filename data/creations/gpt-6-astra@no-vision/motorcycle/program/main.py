import math
c = new_canvas(128,128,name='Midnight sport motorcycle')
P = {'ink':'#0b0e14','rubber':'#141820','tread':'#242a33','edge':'#353d49','dark':'#202630','body':'#303946','mid':'#455160','hi':'#626f7d','metalDark':'#505e6a','steel':'#8998a4','silver':'#bdc9d0','white':'#edf3f4','redDark':'#7f172c','red':'#d82d3e','redHi':'#ff6170','black':'#11151c'}
def poly(pts,fill,outline=None):
    c.poly(pts,P.get(fill,fill))
    if outline: c.poly(pts,P.get(outline,outline),fill=False)
def line(x1,y1,x2,y2,color): c.line(x1,y1,x2,y2,P.get(color,color))
def tube(a,b,width=3):
    # parallel vertical offsets form a crisp metallic tube
    for d in range(-width//2,width//2+1): line(a[0],a[1]+d,b[0],b[1]+d,'ink')
    line(a[0],a[1],b[0],b[1],'steel')
    line(a[0],a[1]-1,b[0],b[1]-1,'silver')
# Two thick tires, machined rims, and pale radial spokes.
for cx,cy in [(28,92),(102,92)]:
    c.circle(cx,cy,20,P['ink'])
    c.circle(cx,cy,18,P['rubber'])
    c.path(f'M {cx-17} {cy+3} Q {cx-20} {cy-12} {cx-6} {cy-17} Q {cx+7} {cy-22} {cx+16} {cy-9}',P['tread'],fill=False)
    c.path(f'M {cx-13} {cy+13} Q {cx} {cy+22} {cx+14} {cy+11}',P['tread'],fill=False)
    c.circle(cx,cy,14,P['edge'])
    c.circle(cx,cy,13,P['steel'])
    c.circle(cx,cy,11,P['ink'])
    for ang in [-90,-30,30,90,150,210]:
        a=math.radians(ang)
        x=cx+round(10*math.cos(a));y=cy+round(10*math.sin(a))
        line(cx,cy,x,y,'silver')
        line(cx+1,cy,x+1,y,'white')
    c.circle(cx,cy,5,P['metalDark'])
    c.circle(cx,cy,4,P['steel'])
    c.circle(cx,cy,2,P['edge'])
    c.set(cx,cy,P['silver'])
    # short patterned shoulder grooves
    for ang in [25,48,125,150,197,222,253,291,324]:
        a=math.radians(ang)
        x=cx+round(17*math.cos(a));y=cy+round(17*math.sin(a))
        line(x,y,x+round(math.cos(a)),y+round(math.sin(a)),'tread')
# Rear brake and chain run, behind the swing arm.
line(29,88,58,84,'metalDark');line(28,98,61,94,'edge')
for x in range(32,58,3): c.set(x,97-(x-32)//9,P['steel'])
poly([(26,89),(59,82),(67,86),(62,91),(28,96)],'edge','ink')
line(29,91,57,85,'steel');line(31,93,58,88,'hi')
c.circle(29,92,3,P['silver']);c.circle(29,92,1,P['metalDark'])
# Hidden chassis and rear suspension.
poly([(35,52),(59,50),(88,57),(79,89),(49,91),(38,73)],'black','ink')
line(43,60,52,82,'metalDark')
for y in range(62,78,3): line(42+(y-62)//3,y,48+(y-62)//3,y-1,'red')
# Triangulated silver tubular frame.
tube((40,57),(69,62));tube((40,57),(52,84));tube((52,84),(78,65));tube((40,57),(78,65));tube((52,84),(72,88))
# Engine block and cooling ribs.
poly([(52,62),(71,62),(78,72),(72,86),(53,90),(43,81),(45,70)],'metalDark','ink')
poly([(53,62),(69,63),(72,72),(51,71)],'edge','ink')
for y in [64,67,70]: line(54,y,68,y+1,'steel')
c.circle(57,79,11,P['ink']);c.circle(57,79,9,P['steel']);c.circle(57,79,7,P['silver']);c.circle(58,80,6,P['hi'])
c.path('M 51 81 Q 48 73 56 72 Q 61 71 64 76',P['white'],fill=False)
c.circle(58,80,3,P['metalDark']);line(55,80,60,80,'steel')
for x,y in [(50,74),(63,73),(65,83),(52,86)]: c.set(x,y,P['white'])
# Header pipes and low exhaust sweeping back toward the tail.
c.path('M 73 74 Q 81 88 73 93 L 49 95',P['ink'],fill=False)
c.path('M 72 75 Q 78 88 72 91 L 46 93',P['steel'],fill=False)
c.path('M 74 75 Q 80 88 73 92 L 46 94',P['metalDark'],fill=False)
poly([(22,79),(27,78),(49,87),(52,92),(48,96),(24,85)],'ink','ink')
poly([(25,80),(46,88),(48,93),(42,92),(25,84)],'hi')
line(27,80,46,88,'silver');line(28,84,44,90,'steel')
poly([(22,79),(25,80),(25,85),(21,83)],'metalDark','ink')
# Tail, tail lamp, and stepped saddle.
poly([(12,42),(30,43),(45,49),(53,53),(45,59),(28,54),(16,49)],'body','ink')
poly([(13,43),(29,44),(38,47),(21,47)],'hi')
poly([(16,46),(32,49),(34,52),(19,49)],'red','redDark')
line(17,46,27,48,'redHi')
poly([(25,42),(35,43),(48,48),(61,48),(63,52),(47,54),(36,49),(26,47)],'black','ink')
line(28,42,35,43,'hi');line(47,48,59,48,'edge')
# Fuel tank: compact raised crown flowing into the broad front fairing.
poly([(46,48),(53,41),(63,39),(75,41),(85,48),(87,58),(74,65),(59,59),(48,55)],'body','ink')
poly([(50,47),(55,43),(64,41),(75,43),(79,46),(64,44),(56,45)],'hi')
poly([(50,51),(59,52),(70,57),(83,51),(84,57),(74,62),(60,57)],'dark')
line(54,43,63,41,'steel')
poly([(62,40),(68,40),(70,42),(63,43)],'edge','ink');line(64,41,67,41,'silver')
# Fork bridge and silver fork legs, in front of the front wheel.
poly([(87,53),(92,52),(104,91),(100,94),(95,80)],'metalDark','ink')
line(91,60,101,88,'silver');line(90,60,99,88,'white')
line(94,73,99,88,'steel')
poly([(99,87),(104,87),(105,93),(100,95),(98,92)],'hi','ink')
c.circle(102,92,2,P['silver']);c.set(102,92,P['edge'])
# Front fender rides closely over the tire.
poly([(84,79),(88,73),(98,70),(108,72),(116,79),(109,77),(100,75),(93,77),(88,81)],'body','ink')
line(90,74,98,72,'hi');line(98,72,106,73,'hi');line(109,75,113,78,'red')
# Tilted black windscreen and cockpit details.
poly([(82,47),(80,34),(85,35),(95,43),(100,51),(88,52)],'black','ink')
line(81,35,85,36,'hi');line(85,36,94,44,'edge')
line(84,39,87,45,'tread')
line(80,49,76,45,'steel');line(72,45,79,45,'ink');line(72,44,77,44,'hi')
line(94,46,98,38,'metalDark')
poly([(94,34),(101,34),(104,36),(101,39),(96,38)],'dark','ink');line(96,35,101,35,'hi')
# Broad angular nose and side fairing.
poly([(84,48),(98,48),(110,54),(116,60),(111,66),(99,70),(89,83),(80,95),(67,96),(69,86),(76,70),(73,62)],'body','ink')
poly([(86,49),(97,50),(108,55),(111,58),(99,55),(89,54),(79,60)],'hi')
poly([(76,64),(85,60),(105,62),(94,70),(86,85),(76,91),(72,90),(78,74)],'dark')
poly([(80,65),(96,61),(106,61),(100,65),(85,69),(78,79)],'edge')
# Air inlet with stepped louvres.
poly([(84,66),(94,64),(89,70),(81,75)],'ink')
line(84,68,91,66,'metalDark');line(82,71,88,69,'hi')
# Front lamp, red racing slash, and belly pan.
poly([(105,55),(113,59),(110,61),(102,58)],'ink','ink')
line(106,56,112,59,'white');line(104,57,109,59,'silver')
poly([(79,58),(93,55),(103,56),(94,59),(80,62),(76,66)],'red')
line(81,58,92,56,'redHi')
poly([(72,88),(78,91),(85,86),(80,96),(66,97),(63,93)],'dark','ink')
poly([(68,93),(78,93),(82,90),(79,95),(69,95)],'red')
line(70,93,77,93,'redHi')
# Panel fasteners, rider peg, and compact controls.
for x,y in [(77,64),(94,54),(76,88)]:
    c.set(x,y,P['steel'])
line(47,84,44,90,'ink');line(44,90,53,90,'silver');line(44,91,51,91,'metalDark')
c.circle(48,84,2,P['metalDark']);c.set(48,84,P['silver'])
print(c.stats_text())
print(c.matrix_text(region=(72,48,113,70)))
save('motorcycle',c)
finish(c)
