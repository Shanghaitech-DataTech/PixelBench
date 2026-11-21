import random, math
random.seed(19)
result = new_canvas(128,128,name='red_roofed_forge')
c=result
P={
'ink':'#252731','deep':'#34303a','ground':'#4b5351','ground2':'#60665c','groundhi':'#7b7d6b','edge':'#363f40','moss':'#58624c',
'stone':'#706c69','stonesh':'#514e55','stoneli':'#989080','stonehi':'#b5a58b',
'wall':'#b9a487','wallhi':'#d2bd95','wallsh':'#8e7a64','side':'#8c806d','sidesh':'#6f665b',
'wood':'#654238','woodsh':'#432f30','woodhi':'#9c6545','woodlight':'#bb8452',
'roofdark':'#652d36','roofsh':'#8c3440','roof':'#b44543','roof2':'#c65447','roofhi':'#df7052','rooflight':'#ee9163',
'iron':'#41464c','ironhi':'#7c8585','irondark':'#292c35','black':'#30232b','coal':'#5a292c',
'ember':'#b13d2c','orange':'#f2772f','gold':'#ffb947','fire':'#ffe88a','white':'#fff3bd'}
def poly(points,col): c.poly([(round(x),round(y)) for x,y in points],P.get(col,col))
def line(a,b,col): c.line(round(a[0]),round(a[1]),round(b[0]),round(b[1]),P.get(col,col))
def F(u,z): return (23+u,89+u*.5-z)
def fp(points,col): poly([F(u,z) for u,z in points],col)
def fl(a,b,col): line(F(*a),F(*b),col)
# Low, cut-stone tile foundation and silhouette
poly([(8,90),(59,64),(120,94),(120,100),(70,125),(8,96)],'edge')
poly([(8,89),(58,64),(121,95),(70,121)],'ground')
line((10,95),(70,124),'ground2'); line((70,123),(119,99),'ground2')
# restrained paving patches
for x,y,w in [(17,89,10),(22,96,10),(38,102,9),(53,112,10),(70,114,11),(87,107,9),(108,98,7),(14,92,4),(101,91,10),(43,92,8),(57,104,9),(75,105,8)]:
    poly([(x,y),(x+w,y-w*.5),(x+w+7,y-w*.5+3),(x+7,y+3)],random.choice(['ground2','ground2','groundhi']))
    line((x,y+1),(x+6,y+4),'edge')
for x,y in [(15,86),(20,99),(66,119),(91,112),(115,100),(48,108)]:
    c.rect(x,y,3,1,P['moss']);c.set(x+2,y-1,P['moss'])
# building cast shadow
poly([(25,89),(65,70),(117,94),(82,113),(62,113)],'edge')
# walls: gabled front and long side
poly([(69,75),(106,56),(106,91),(69,111)],'side')
poly([(23,55),(43,36),(70,78),(70,111),(23,88)],'wall')
poly([(24,60),(40,42),(43,39),(66,78),(66,103),(25,83)],'wallhi')
poly([(23,81),(70,104),(70,112),(23,89)],'stonesh')
poly([(70,104),(106,86),(106,93),(70,112)],'stonesh')
# wall sill stones
for u in range(0,46,9):
    fp([(u,1),(u+8,1),(u+8,7),(u,7)],random.choice(['stone','stoneli']))
for i in range(4):
    x=71+i*9;y=110-i*4.5
    poly([(x,y-1),(x+8,y-5),(x+8,y-11),(x,y-7)],'stone')
    line((x,y-7),(x+7,y-10.5),'stoneli')
# timber wall frame
fp([(0,6),(4,6),(4,33),(0,35)],'woodsh');fl((1,8),(1,33),'woodhi')
fp([(43,0),(47,0),(47,34),(43,35)],'woodsh');fl((44,6),(44,34),'woodhi')
fp([(0,31),(46,31),(46,35),(0,35)],'wood');fl((3,32),(43,32),'woodhi')
# gable's central post and diagonal braces
poly([(41,41),(44,41),(47,64),(43,63)],'wood')
line((28,59),(41,49),'wood');line((48,59),(61,73),'wood')
# side structure and plaster variation
poly([(72,80),(76,78),(76,102),(72,104)],'woodsh')
poly([(101,63),(105,61),(105,89),(101,91)],'woodsh')
line((102,65),(102,87),'woodhi')
poly([(76,94),(100,82),(100,86),(76,98)],'sidesh')
line((77,96),(99,85),'woodhi')
# little side shutter
poly([(79,79),(91,73),(91,87),(79,93)],'woodsh')
poly([(81,80),(89,76),(89,86),(81,90)],'iron')
for i in range(3): line((82+i*3,80-i*1.5),(82+i*3,87-i*1.5),'ironhi')
line((79,92),(92,85),'woodhi')
# front stone furnace: thick arched masonry in front-face coordinates
arch=[(8,4),(8,22),(10,27),(14,31),(20,33),(27,32),(33,28),(36,22),(36,4)]
fp(arch,'stonesh')
fp([(9,5),(9,22),(12,27),(16,30),(22,31),(28,29),(33,25),(35,21),(35,5)],'stoneli')
# separate voussoir joints
for a,b in [((9,18),(14,18)),((9,24),(15,22)),((12,28),(17,25)),((17,31),(19,26)),((24,31),(24,27)),((30,28),(27,25)),((34,24),(29,22)),((30,17),(35,17)),((9,11),(14,11)),((30,10),(35,10))]: fl(a,b,'stonesh')
fp([(14,4),(14,21),(16,25),(20,27),(25,26),(29,22),(30,4)],'black')
# furnace hot inner walls
fp([(15,5),(15,20),(17,24),(20,25),(19,20),(18,6)],'ember')
fp([(27,6),(27,22),(29,20),(29,5)],'ember')
fp([(16,5),(16,12),(19,14),(23,12),(28,13),(28,5)],'orange')
fp([(17,6),(17,13),(20,16),(21,22),(24,17),(24,11),(26,16),(28,11),(28,6)],'gold')
fp([(19,6),(19,11),(21,14),(22,18),(24,12),(25,9),(25,6)],'fire')
fp([(21,6),(22,12),(24,9),(24,6)],'white')
# coals / iron lip and hearth slab
for u,z in [(16,6),(19,7),(26,7),(28,6)]: fp([(u,z),(u+2,z),(u+2,z+1),(u,z+1)],'coal')
fl((14,5),(30,5),'irondark')
fp([(7,0),(37,0),(37,5),(7,5)],'stonesh')
fp([(7,5),(37,5),(35,7),(9,7)],'stonehi')
fl((10,6),(33,6),'orange')
# small metal anchor details
for u in [2,45]:
    for z in [11,29]:
        x,y=F(u,z);c.set(round(x),round(y),P['ironhi'])
# roof dark solid underhang, left slope
poly([(42,32),(83,12),(113,59),(113,63),(70,85)],'woodsh')
poly([(17,54),(43,32),(83,12),(58,37),(17,59)],'woodsh')
line((20,57),(42,37),'woodhi')
line((44,39),(68,78),'woodhi')
poly([(18,54),(57,34),(82,13),(43,33)],'roofsh')
for i in range(1,6):
    a=(18+25*i/6,54-21*i/6);b=(57+25*i/6,34-21*i/6)
    line(a,b,'roofdark');line((a[0],a[1]-1),(b[0],b[1]-1),'roof2')
# tiled main roof, a precise oblique parallelogram
R=(43,33); U=(39,-20); V=(28,46)
def roof(s,t): return (R[0]+U[0]*s+V[0]*t,R[1]+U[1]*s+V[1]*t)
poly([roof(0,0),roof(1,0),roof(1,1),roof(0,1)],'roofdark')
for row in range(7):
    t0=row/7;t1=(row+1)/7
    shift=.5 if row%2 else 0
    for j in range(-1,9):
        s0=max(0,(j+shift)/8);s1=min(1,(j+1+shift)/8)
        if s1<=s0: continue
        col=random.choice(['roof','roof2','roof2','roofhi'])
        poly([roof(s0,t0),roof(s1,t0),roof(s1,t1),roof(s0,t1)],col)
        line(roof(s0,t0),roof(s0,t1),'roofsh')
        line(roof(s0,t1),roof(s1,t1),'roofdark')
        p=roof(s0,t1);q=roof(s1,t1)
        line((p[0]+1,p[1]-1),(q[0]-1,q[1]-1),'roofhi')
# gable bargeboards: sharp rim and sunlit terracotta edge
line((18,55),(43,33),'rooflight');line((18,56),(43,34),'roofdark')
line((43,33),(71,79),'rooflight');line((43,35),(70,80),'roofhi')
line((71,80),(110,60),'rooflight');line((71,82),(111,62),'roofdark')
# ridge cap, individual overlapping curved tiles
for i in range(8):
    s=i/8;e=(i+1)/8
    a=roof(s,0);b=roof(e,0)
    poly([(a[0]-2,a[1]),(a[0],a[1]-3),(b[0],b[1]-3),(b[0]+1,b[1]),(a[0]+1,a[1]+2)],'roofhi')
    line((a[0],a[1]-3),(b[0],b[1]-3),'rooflight')
    line((a[0]+1,a[1]+1),(b[0]+1,b[1]-1),'roofdark')
# squat brick chimney, rooted into upper roof
poly([(71,35),(79,31),(88,36),(80,41)],'roofdark')
poly([(72,15),(79,18),(79,37),(72,33)],'stone')
poly([(79,18),(86,14),(86,33),(79,37)],'stonesh')
for y in [22,28,33]:
    line((72,y-3),(79,y),'stonesh');line((79,y),(85,y-3),'deep')
line((75,20),(75,23),'stonesh');line((76,28),(76,31),'stonesh');line((82,23),(82,26),'deep')
poly([(70,12),(78,8),(88,12),(79,17)],'stonehi')
poly([(70,12),(79,17),(79,20),(70,15)],'stoneli')
poly([(79,17),(88,12),(88,15),(79,20)],'stone')
poly([(74,12),(78,10),(84,12),(79,15)],'black')
line((74,12),(79,14),'deep')
# hanging sign on side wall, bracket projects right
line((96,66),(96,73),'irondark');line((96,66),(112,66),'irondark');line((98,70),(104,66),'iron')
c.set(96,66,P['ironhi']);line((105,67),(105,71),'ironhi');line((112,67),(112,71),'ironhi')
poly([(101,73),(114,70),(114,80),(101,84)],'woodsh')
poly([(102,74),(113,71),(113,79),(102,82)],'woodhi')
line((103,75),(112,73),'woodlight');line((103,81),(112,78),'wood')
# golden anvil pictogram on wooden sign
poly([(104,76),(111,74),(110,77),(108,78),(108,79),(105,80),(106,78)],'gold')
c.set(103,75,P['stonehi']);c.set(112,78,P['stonehi'])
# barrels, oval heads and staves; stacked cluster along right side

def barrel(x,y,w=12,h=15):
    # x,y is upper-left at top rim
    r=w//2;cx=x+r
    poly([(x+2,y+1),(x+w-2,y+1),(x+w,y+5),(x+w,y+h-4),(x+w-2,y+h),(x+2,y+h),(x,y+h-4),(x,y+5)],'woodsh')
    poly([(x+2,y+3),(x+w-2,y+3),(x+w-1,y+6),(x+w-1,y+h-4),(x+w-3,y+h-1),(x+3,y+h-1),(x+1,y+h-4),(x+1,y+6)],'woodhi')
    for k in [3,6,9]:
        if k<w-1: line((x+k,y+5),(x+k,y+h-2),'wood')
    line((x+2,y+6),(x+2,y+h-4),'woodlight')
    c.ellipse(cx,y+3,r,3,P['woodsh']);c.ellipse(cx,y+2,r-1,2,P['woodlight'])
    line((x+2,y+2),(x+w-2,y+2),'woodhi');c.set(cx+1,y+2,P['wood'])
    for yy in [y+6,y+h-4]:
        line((x+1,yy-1),(x+3,yy),'iron');line((x+3,yy),(x+w-3,yy),'iron');line((x+w-3,yy),(x+w-1,yy-1),'iron')
        line((x+2,yy),(x+5,yy+1),'ironhi');c.set(x+w-3,yy,P['ironhi'])
    line((x+3,y+h),(x+w-3,y+h),'ink')
barrel(105,88,12,16)
barrel(94,94,13,16)
barrel(102,78,12,15)
# Anvil on a heavy stump in foreground left
c.ellipse(27,103,7,4,P['woodsh']);c.rect(20,99,15,5,P['woodsh']);c.ellipse(27,99,7,4,P['woodhi'])
for x in [22,25,29,32]:line((x,100),(x,104),'wood')
poly([(18,92),(26,88),(37,93),(31,96),(30,100),(23,99),(24,95)],'irondark')
poly([(18,91),(26,87),(38,92),(31,95),(22,94)],'ironhi')
poly([(18,91),(22,94),(31,95),(31,97),(21,96),(15,92)],'iron')
line((18,91),(26,87),'stonehi');line((26,88),(36,92),'stoneli')
poly([(25,96),(29,97),(29,100),(33,102),(29,104),(21,100),(24,99)],'iron')
line((22,100),(29,103),'ironhi')
# leaning smith's tongs and hammer, beside entrance
line((63,96),(58,107),'irondark');line((65,97),(60,108),'ironhi')
line((58,107),(60,109),'iron');line((60,108),(63,108),'iron')
line((18,100),(15,108),'woodhi')
poly([(12,105),(16,106),(18,109),(15,110),(12,108)],'iron')
# a few warm reflections close to the open hearth
line((41,104),(47,107),'woodhi');c.set(48,108,P['orange'])
view(result)
finish(result)
