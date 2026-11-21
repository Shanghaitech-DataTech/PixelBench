import math, random
random.seed(8)
c = new_canvas(128,128,name='red_roofed_forge')
# Compact, shared palette.
P={'ink':'#242333','edge':'#34313a','earth':'#4c4444','soil':'#686057','stone':'#827b69','stonehi':'#a49b80','mortar':'#4e5352','wall':'#a49a7b','wallhi':'#bcb08b','wallshade':'#777864','beam':'#493b35','wood':'#79543a','woodhi':'#ad7b48','woodlight':'#d2a569','woodshadow':'#573d31','roofdark':'#662e35','roofshadow':'#89343a','red':'#ac423c','red2':'#bf4e40','red3':'#cc5a46','roofhi':'#e37c54','rooflight':'#f19962','metal':'#59636a','metalhi':'#94a3a0','metalshade':'#37434c','black':'#211f29','fireedge':'#a6402e','orange':'#ed762c','gold':'#ffb643','yellow':'#ffe58a','cream':'#fff5ca','grass':'#666d4c','grasshi':'#8c915d'}
def poly(pts,col,outline=None):
    c.poly(pts,P.get(col,col))
    if outline: c.poly(pts,P.get(outline,outline),fill=False)
def line(a,b,col): c.line(*a,*b,P.get(col,col))
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
# Raised diamond of worn stone, with a crisp silhouette.
poly([(5,94),(62,65),(123,95),(123,100),(66,127),(5,99)],'edge')
poly([(6,94),(62,66),(122,95),(66,123)],'soil')
poly([(6,95),(66,124),(66,126),(6,98)],'earth')
poly([(67,124),(122,97),(122,99),(67,126)],'mortar')
# Paving is laid on the same two axes as the house.
for i in range(9):
    for j in range(8):
        x=62+(i-j)*7; y=68+(i+j)*3.5
        if y>90 and 10<x<117 and y<118:
            poly([(round(x),round(y)),(round(x+6),round(y+3)),(round(x),round(y+6)),(round(x-6),round(y+3))],random.choice(['stone','soil','stone','mortar']))
for x,y in [(10,96),(15,98),(103,105),(107,102),(55,117),(91,112),(44,112)]:
    line((x,y),(x+3,y+1),'grass'); c.set(x+1,y-1,P['grasshi'])
# Foundation and plaster walls.
poly([(22,54),(64,75),(106,54),(106,87),(64,108),(22,87)],'ink','ink')
poly([(24,58),(64,78),(64,101),(24,82)],'wall')
poly([(65,76),(104,56),(104,83),(65,103)],'wallshade')
poly([(65,74),(85,41),(105,55),(104,83),(65,103)],'wallshade')
poly([(67,73),(85,46),(101,56),(67,73)],'wall')
# Limestone footings.
poly([(23,81),(64,101),(64,107),(23,87)],'stone','edge')
poly([(65,101),(105,81),(105,87),(65,107)],'mortar','edge')
for x in [28,39,51,61]:
    yy=81+(x-23)//2
    line((x,yy+1),(x,yy+5),'mortar')
for x in [71,81,93,102]:
    yy=101-(x-65)//2
    line((x,yy),(x,yy+4),'edge')
line((24,81),(63,100),'stonehi')
# Framing, corner posts, and gable braces.
poly([(23,56),(27,58),(27,83),(23,81)],'beam')
line((25,59),(25,80),'woodhi')
poly([(60,75),(65,77),(65,103),(61,101)],'beam')
line((61,78),(61,98),'woodhi')
poly([(102,57),(105,55),(105,82),(102,84)],'beam')
poly([(26,59),(60,76),(60,79),(26,62)],'woodshadow')
line((29,64),(57,94),'beam'); line((29,65),(57,95),'wood')
line((67,75),(101,58),'beam'); line((68,77),(101,60),'beam')
line((85,47),(85,65),'beam'); line((76,68),(84,53),'woodshadow')
# Small gable ventilation slit.
poly([(87,53),(94,57),(94,61),(87,65)],'beam')
for x in [89,92]: line((x,56),(x,62),'black')
# Furnace surround, following the right-hand wall plane.
poly([(72,97),(72,79),(75,72),(91,64),(97,67),(99,72),(99,85)],'edge','ink')
poly([(74,96),(74,80),(78,73),(91,67),(95,69),(97,73),(97,85)],'stone')
poly([(79,93),(78,81),(80,76),(90,71),(93,73),(94,77),(94,87)],'fireedge','beam')
poly([(80,91),(80,81),(82,77),(90,73),(92,76),(92,86)],'black')
# Individually cut arch stones.
line((73,82),(78,81),'mortar'); line((74,88),(79,87),'mortar')
line((75,76),(79,78),'mortar'); line((79,71),(82,75),'mortar')
line((85,68),(86,73),'mortar'); line((91,66),(91,71),'mortar')
line((94,69),(92,73),'mortar'); line((97,75),(94,77),'mortar')
line((97,81),(94,83),'mortar')
line((75,80),(75,84),'stonehi'); line((79,73),(83,71),'stonehi')
# Fire tongues and molten coals.
poly([(80,90),(80,85),(83,83),(83,78),(86,82),(88,79),(89,75),(91,80),(93,80),(93,86)],'orange')
poly([(81,89),(83,85),(85,85),(86,80),(88,84),(90,81),(91,85),(92,86)],'gold')
poly([(84,88),(86,84),(88,86),(89,84),(90,87)],'yellow')
line((82,90),(92,85),'cream')
poly([(72,97),(97,84),(102,87),(77,100)],'beam','ink')
poly([(73,96),(96,85),(100,87),(77,98)],'stonehi')
line((80,94),(94,87),'orange')
# Roof silhouette and far slope.
poly([(17,53),(41,15),(88,38),(112,53),(112,57),(64,81),(17,58)],'ink','ink')
# Exposed triangular gable beneath the rake boards.
poly([(65,77),(87,41),(109,54)],'wallshade')
poly([(70,71),(87,45),(103,54)],'wall')
line((87,45),(87,64),'beam')
line((74,69),(86,50),'woodshadow')
line((70,74),(105,56),'beam')
line((71,75),(104,58),'wood')
poly([(90,51),(97,55),(97,58),(90,62)],'beam')
line((92,54),(92,59),'black'); line((95,55),(95,58),'black')
poly([(42,17),(65,30),(110,53),(87,40)],'roofshadow')
for t in range(1,8):
    x=42+t*5.6; y=17+t*2.85
    line((round(x),round(y)),(round(x+23),round(y+13)),'roofdark')
line((54,24),(99,47),'red3')
# Broad tiled roof: staggered terracotta courses.
def roofpt(u,v): return (round(42+45*u-24*v),round(17+23*u+38*v))
poly([roofpt(0,0),roofpt(1,0),roofpt(1,1),roofpt(0,1)],'roofdark')
for row in range(7):
    v0=row/7; v1=(row+1)/7
    shift=.5 if row%2 else 0
    for col in range(-1,9):
        u0=max(0,(col+shift)/8); u1=min(1,(col+1+shift)/8)
        if u1<=u0: continue
        a,b,d,e=roofpt(u0,v0),roofpt(u1,v0),roofpt(u1,v1),roofpt(u0,v1)
        shade=random.choice(['red','red2','red2','red3'])
        poly([a,b,d,e],shade)
        line(e,d,'roofdark'); line(b,d,'roofshadow')
        if col%3!=1: line((a[0],a[1]+1),(b[0]-1,b[1]),'roofhi')
# Eave fascia and ridge cap, each perfectly parallel to its roof axis.
poly([(18,55),(63,78),(63,81),(18,58)],'beam','ink')
line((20,55),(62,76),'roofhi')
line((20,58),(61,79),'wood')
poly([(63,77),(87,39),(111,53),(111,57),(88,44),(65,81)],'roofdark','ink')
line((65,76),(87,41),'roofhi'); line((88,41),(109,53),'red3')
poly([(40,16),(43,14),(90,38),(87,41)],'red3','roofdark')
line((43,15),(88,38),'rooflight')
for i in range(1,9):
    x=43+i*5; y=15+i*2.5
    line((round(x),round(y)),(round(x-2),round(y+3)),'roofshadow')
# Chimney emerges from the far roof slope.
poly([(64,30),(64,10),(73,6),(82,11),(82,34),(73,39)],'ink','ink')
poly([(65,12),(73,16),(73,36),(65,32)],'stone')
poly([(74,16),(80,13),(80,32),(74,36)],'mortar')
for y in [18,24,30]:
    line((65,y),(72,y+3),'edge'); line((74,y+3),(80,y),'edge')
    line((68,y+2),(68,y+5),'mortar')
line((66,14),(66,17),'stonehi'); line((66,25),(66,28),'stonehi')
poly([(62,10),(72,5),(83,10),(73,15)],'stonehi','ink')
poly([(62,10),(73,15),(83,10),(83,13),(73,18),(62,13)],'mortar','ink')
poly([(66,10),(72,7),(79,10),(73,13)],'black')
# A modest curl of soot.
poly([(71,8),(69,5),(70,3),(74,2),(77,3),(74,4),(73,7)],'#777877')
c.set(75,1,'#a0a298'); c.set(78,2,'#a0a298')
# Hanging smith's wooden sign on the left facade.
line((30,63),(30,70),'metalshade'); line((49,72),(49,78),'metalshade')
poly([(28,67),(52,79),(52,90),(28,78)],'ink','ink')
poly([(29,68),(51,79),(51,88),(29,77)],'wood')
line((30,69),(50,79),'woodlight'); line((30,76),(50,86),'woodshadow')
line((31,74),(49,83),'woodhi')
# Cream hammer emblem.
line((38,74),(43,84),'woodlight'); line((39,74),(44,84),'woodlight')
poly([(35,73),(38,71),(46,75),(43,78)],'cream')
c.set(30,72,P['metalhi']); c.set(50,83,P['metalhi'])
# Barrels, including one resting above the lower pair.
def barrel(x,y):
    # x,y is top centre
    poly([(x-6,y),(x-7,y+4),(x-7,y+11),(x-5,y+15),(x,y+17),(x+5,y+15),(x+7,y+11),(x+7,y+4),(x+6,y)],'ink','ink')
    poly([(x-5,y+2),(x-6,y+6),(x-5,y+13),(x,y+15),(x+5,y+13),(x+6,y+5),(x+5,y+2)],'wood')
    poly([(x-4,y+3),(x-3,y+13),(x,y+15),(x,y+4)],'woodhi')
    for dx in [-3,1,4]: line((x+dx,y+5),(x+dx,y+13),'woodshadow')
    for yy in [4,11]:
        line((x-6,y+yy),(x,y+yy+3),'metalshade'); line((x,y+yy+3),(x+6,y+yy),'metalshade')
        line((x-5,y+yy),(x,y+yy+2),'metalhi'); line((x+1,y+yy+2),(x+5,y+yy),'metal')
    c.ellipse(x,y+1,6,3,P['woodshadow']); c.ellipse(x,y,5,2,P['woodlight'])
    line((x-3,y),(x+3,y+1),'wood'); c.set(x+1,y,P['woodshadow'])
barrel(16,85); barrel(29,92); barrel(21,74)
# Fuel rack with cut timber by the furnace.
poly([(102,91),(113,85),(119,88),(119,97),(109,102),(102,98)],'woodshadow','ink')
for x,y in [(108,94),(114,91),(108,88)]:
    poly([(x-3,y-1),(x+3,y-4),(x+6,y-2),(x,y+1)],'wood')
    c.ellipse(x,y,3,3,P['woodlight']); c.ellipse(x,y,2,2,P['woodhi'],fill=False); c.set(x,y,P['woodshadow'])
# Anvil on a solid oak stump in the foreground.
c.ellipse(66,113,9,4,P['edge'])
poly([(59,105),(72,105),(73,113),(68,117),(59,113)],'woodshadow','ink')
line((61,107),(61,112),'woodhi'); line((68,108),(68,114),'wood')
c.ellipse(65,105,7,3,P['woodhi'])
poly([(62,101),(69,101),(68,106),(73,108),(65,112),(58,108),(63,105)],'metalshade','ink')
poly([(54,99),(62,99),(67,96),(76,100),(72,104),(64,106),(57,103)],'metal','ink')
poly([(54,98),(62,98),(67,95),(77,99),(70,102),(62,103)],'metalhi','ink')
line((56,99),(62,101),'#c3c6b0'); line((65,97),(73,100),'#c3c6b0')
line((64,104),(64,108),'metalhi')
# A hammer left on the paving.
line((84,110),(92,114),'woodshadow'); line((84,109),(92,113),'woodhi')
poly([(80,109),(84,107),(88,109),(84,112)],'metalshade','ink')
line((81,108),(84,107),'metalhi')
result=c
view(result)
finish(result)
