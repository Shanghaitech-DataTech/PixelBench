import math, random

# An orthographic forge tile. All three axes keep a constant pixel step.
result = new_canvas(128, 128, name='Red roof forge')
c = result
P = {
'ink':'#252431', 'deep':'#332b38', 'shadow':'#333a42', 'ground':'#606567',
'pave':'#858880', 'pavelight':'#a4a291', 'pavedark':'#6a7170', 'edge':'#4a5055',
'mortar':'#595255', 'stone':'#9d9282', 'stonelight':'#c2b29a', 'stoneshade':'#786f69',
'cream':'#d4bb91', 'ivory':'#ead0a0', 'ochre':'#b69976', 'wallshade':'#9a826b',
'wooddark':'#4a3333', 'wood':'#74503c', 'woodmid':'#956342', 'woodlight':'#bc8652', 'woodhi':'#d5a367',
'roofdark':'#662e3b', 'roofseam':'#83333d', 'red':'#ba493f', 'red2':'#c95342', 'red3':'#ac3e3c',
'redlight':'#de6b4c', 'redhi':'#f18c5d', 'redshade':'#96353b',
'iron':'#414752', 'ironmid':'#64717a', 'ironlight':'#929e9f', 'ironhi':'#c5cebf',
'coal':'#3d2731', 'ember':'#a23c2e', 'orange':'#f0782f', 'gold':'#ffb641', 'flame':'#ffe58d', 'hot':'#fff5c4',
'brick':'#a65e4b', 'bricklight':'#c17b59', 'brickshade':'#79453e', 'glowstone':'#dc985c',
'moss':'#536957', 'mosslight':'#788166'
}
for k,v in P.items(): c.color(v,k)

def poly(pts,col): c.poly([(round(x),round(y)) for x,y in pts],col)
def line(a,b,col): c.line(round(a[0]),round(a[1]),round(b[0]),round(b[1]),col)

# Shallow diamond foundation, with a handful of broad paving stones.
poly([(63,64),(122,93),(122,97),(65,125),(5,96),(5,92)],'ink')
poly([(5,92),(64,121),(122,93),(122,97),(65,125),(5,96)],'edge')
poly([(5,92),(63,63),(122,93),(64,122)],'pavedark')
poly([(9,92),(63,65),(118,93),(64,120)],'ground')
random.seed(8)
def ground(x,y): return (64+2*x-2*y, 72+x+y)
for a in range(7):
    for b in range(7):
        u,v=a*4,b*4
        pts=[ground(u+.25,v+.25),ground(u+3.75,v+.25),ground(u+3.75,v+3.75),ground(u+.25,v+3.75)]
        # The perimeter is a clipped, stepped cobblestone apron.
        if all(7 <= x <= 120 and y <= 120 for x,y in pts):
            poly(pts, random.choice(['pave','pavedark','pave','ground']))
            if a+b>8:
                line(pts[0],pts[1],'pavelight' if (a+b)%3==0 else 'stone')
line((7,94),(64,122),'stone')
line((65,123),(120,96),'pavedark')
# Weight of the building and props on the stone.
poly([(18,84),(67,68),(111,84),(116,98),(70,119),(20,96),(13,92)],'shadow')
poly([(74,104),(103,87),(117,91),(113,103),(87,116),(74,112)],'edge')

# Thick foundation and the two parallel wall planes.
poly([(19,53),(63,75),(63,112),(19,90)],'ink')
poly([(63,75),(107,53),(107,90),(63,112)],'ink')
poly([(21,55),(62,75),(62,105),(21,85)],'ochre')
poly([(23,58),(59,76),(59,99),(23,81)],'cream')
poly([(22,60),(27,63),(27,84),(22,82)],'wallshade')
poly([(64,74),(105,54),(105,88),(64,108)],'cream')
poly([(67,73),(104,55),(104,85),(67,103)],'ivory')
# Front gable under the roof.
poly([(63,74),(86,40),(106,53),(106,62),(64,83)],'wooddark')
poly([(67,72),(86,44),(103,54),(103,61),(67,79)],'ochre')
poly([(70,70),(85,47),(99,55),(99,60),(70,75)],'cream')
# Structural timber follows the same wall axes.
poly([(20,55),(24,57),(24,86),(20,85)],'wood')
poly([(59,73),(64,75),(64,108),(59,106)],'wooddark')
line((60,76),(60,103),'woodlight')
poly([(102,56),(106,54),(106,88),(102,90)],'wood')
line((103,59),(103,85),'woodlight')
poly([(64,76),(106,55),(106,59),(64,80)],'wooddark')
line((66,77),(101,60),'woodmid')
poly([(84,45),(88,46),(88,64),(84,66)],'wood')
line((85,48),(85,63),'woodlight')
# A small iron grille high in the gable.
poly([(92,53),(98,56),(98,62),(91,65),(89,63),(89,57)],'wooddark')
poly([(92,56),(96,57),(96,61),(92,63)],'coal')
line((92,56),(92,62),'ironmid')
line((95,57),(95,61),'iron')

# Dressed stone along the foot of each wall.
poly([(20,83),(62,104),(62,111),(20,90)],'mortar')
poly([(64,104),(106,83),(106,90),(64,111)],'mortar')
for i in range(6):
    x=21+i*7
    y=84+(x-20)*.5
    poly([(x,y),(x+5,y+2.5),(x+5,y+7),(x,y+4.5)],'stone' if i%2 else 'stoneshade')
    line((x,y),(x+5,y+2.5),'stonelight')
for i in range(6):
    x=65+i*7
    y=104-(x-64)*.5
    poly([(x,y),(x+5,y-2.5),(x+5,y+3),(x,y+5.5)],'stone' if i%2 else 'ochre')
    line((x,y),(x+5,y-2.5),'stonelight')

# Side door: iron straps, inset planks and a stone step.
poly([(27,68),(43,76),(43,100),(27,92)],'wooddark')
poly([(29,71),(41,77),(41,97),(29,91)],'wood')
for x in [30,34,38]:
    y=72+(x-29)*.5
    line((x,y),(x,y+18),'woodmid')
    line((x+2,y+1),(x+2,y+19),'wooddark')
poly([(29,78),(41,84),(41,86),(29,80)],'iron')
poly([(29,87),(41,93),(41,95),(29,89)],'iron')
for x,y in [(30,79),(39,84),(30,88),(39,93)]: c.set(x,y,'ironlight')
c.set(38,87,'woodhi'); c.set(39,88,'ink'); c.set(38,89,'wooddark')
poly([(26,92),(43,100),(47,98),(47,101),(42,104),(25,96)],'edge')
poly([(26,91),(43,99),(47,97),(30,89)],'stonelight')
line((26,92),(43,100),'stone')
# Patches in the old render, kept in small clusters.
for pts in [[(24,63),(27,64),(27,66),(24,65)],[(47,90),(55,94),(55,97),(47,93)],[(49,73),(54,76),(54,78),(49,75)]]:
    poly(pts,'ochre')
line((46,94),(52,97),'wallshade')
line((49,98),(56,101),'wallshade')

# Large arched forge mouth, defined in coordinates on the right wall.
def wall(u,h): return (63+u,110-.5*u-h)
def wp(points,col): poly([wall(u,h) for u,h in points],col)
def wl(a,b,col): line(wall(*a),wall(*b),col)
wp([(6,1),(35,1),(35,21),(32,30),(25,35),(17,34),(8,27),(6,20)],'mortar')
# Rough stone jambs.
for side in [6,31]:
    for j in range(4):
        lo=2+j*5
        wp([(side,lo),(side+5,lo),(side+5,lo+4),(side,lo+4)],'stone' if side==6 else 'ochre')
        wl((side,lo+4),(side+4,lo+4),'stonelight' if side==6 else 'glowstone')
# Arch ring of separate wedge stones.
for i in range(7):
    a=math.pi*i/7+.035; b=math.pi*(i+1)/7-.035
    pts=[(20+15*math.cos(a),21+15*math.sin(a)),(20+15*math.cos(b),21+15*math.sin(b)),(20+10.5*math.cos(b),21+10.5*math.sin(b)),(20+10.5*math.cos(a),21+10.5*math.sin(a))]
    wp(pts,['stone','stonelight','cream','stonelight','stone','stonelight','stone'][i])
    wl(pts[0],pts[1],'ivory')
# Black inset arch.
arch=[(10,3),(30,3),(30,21)]+[(20+10*math.cos(a),21+10*math.sin(a)) for a in [i*math.pi/16 for i in range(17)]]
wp(arch,'wooddark')
arch2=[(12,4),(29,4),(29,20)]+[(20+9*math.cos(a),20+9*math.sin(a)) for a in [i*math.pi/16 for i in range(17)]]
wp(arch2,'coal')
wp([(12,4),(29,4),(29,15),(25,19),(20,17),(16,20),(12,13)],'ember')
wp([(12,5),(29,5),(29,10),(26,14),(23,13),(21,20),(18,15),(16,16),(13,11)],'orange')
# Distinct rising tongues, each with a pale heart.
wp([(14,6),(13,10),(17,15),(18,21),(21,16),(20,12),(23,15),(25,22),(27,17),(26,12),(28,9),(27,6)],'gold')
wp([(17,6),(16,9),(19,14),(19,18),(22,13),(21,10),(24,12),(25,16),(26,11),(25,7)],'flame')
wp([(20,6),(19,9),(21,12),(23,9),(24,6)],'hot')
# Coal bed and grate bars.
wp([(11,3),(30,3),(30,6),(11,6)],'ink')
for u,h in [(13,6),(17,5),(21,6),(25,5),(28,6)]:
    wp([(u,h),(u+2,h),(u+2,h+1),(u,h+1)],'orange')
for u in [13,18,23,28]: wl((u,3),(u,8),'iron')
wl((11,4),(29,4),'ironmid')
# Projecting hearth slab, illuminated along the inner edge.
poly([(69,106),(96,92),(101,95),(73,110)],'ink')
poly([(69,104),(96,90),(101,93),(73,108)],'stoneshade')
line((71,104),(96,92),'glowstone')
line((73,108),(99,95),'stone')
line((75,105),(91,97),'bricklight')

# A deep wooden eave supports the red tile surface.
poly([(14,50),(63,74),(63,80),(14,56)],'ink')
poly([(16,52),(61,74),(61,78),(16,56)],'wooddark')
line((17,53),(60,75),'woodmid')
for x in [23,36,50]:
    y=56+(x-16)*.5
    poly([(x,y),(x+3,y+1),(x+3,y+5),(x,y+3)],'wooddark')
    c.set(x+1,round(y+2),'woodlight')
# The single visible broad roof slope.
A=(39,15); B=(87,39); D=(15,51); C=(63,75)
def roof(u,v): return (39+48*u-24*v,15+24*u+36*v)
poly([(38,13),(89,38),(65,77),(12,52)],'ink')
poly([A,B,C,D],'roofdark')
random.seed(22)
rows=7; cols=8
for r in range(rows):
    for j in range(-1,cols+1):
        u0=max(0,(j+(r%2)*.5)/cols); u1=min(1,(j+1+(r%2)*.5)/cols)
        if u1<=u0: continue
        v0=r/rows; v1=(r+1)/rows
        tile=[roof(u0+.006,v0+.005),roof(u1-.006,v0+.005),roof(u1-.006,v1-.018),roof(u0+.006,v1-.018)]
        col=random.choice(['red','red','red2','red3'])
        poly(tile,col)
        line(roof(u0+.011,v1-.021),roof(u1-.011,v1-.021),'roofseam')
        line(roof(u0+.012,v0+.018),roof(u1-.018,v0+.018),'redlight' if (r+j)%4 else 'redhi')
        if u1-u0>.07:
            line(roof(u0+.015,v0+.046),roof(u0+.015,v1-.047),'redlight' if j%3==0 else 'red2')
# Bottom tile lips and lit ridge caps.
line((15,51),(63,75),'roofdark')
line((15,50),(62,73),'redlight')
line((13,52),(62,77),'ink')
# Right gable has two red rake edges; dark undersides anchor the geometry.
poly([(87,38),(113,51),(111,54),(86,42),(65,77),(62,75)],'roofdark')
line((88,39),(112,51),'redlight')
line((87,41),(65,74),'redlight')
line((88,42),(67,75),'redshade')
# The raised ridge is made of individual cap tiles.
for i in range(8):
    x=38+6*i; y=13+3*i
    poly([(x,y+1),(x+2,y),(x+8,y+3),(x+6,y+5),(x,y+2)],'redshade')
    line((x+1,y),(x+6,y+2),'redhi')
    line((x+1,y+2),(x+5,y+4),'redlight')
# Sparse cracks and chipped tile glints.
for x,y in [(29,39),(49,37),(55,58),(73,44)]:
    line((x,y),(x+1,y+2),'roofseam')
    c.set(x+2,y+2,'redhi')

# Squat brick chimney, with an open soot-black cap and roof flashing.
poly([(49,28),(61,24),(74,31),(63,39),(48,33)],'roofdark')
poly([(50,27),(62,22),(71,28),(61,35)],'iron')
poly([(51,17),(61,22),(61,33),(51,28)],'brick')
poly([(61,22),(69,18),(69,29),(61,33)],'brickshade')
line((51,17),(51,28),'wooddark')
line((61,23),(61,32),'bricklight')
for y in [23,28]:
    line((52,y),(60,y+4),'brickshade')
    line((62,y+4),(68,y+1),'wooddark')
    line((52,y-1),(59,y+2),'bricklight')
for x,y in [(55,21),(57,27),(65,23)]: line((x,y),(x,y+3),'brickshade' if x<61 else 'wooddark')
poly([(49,14),(58,10),(71,16),(62,21),(49,15)],'ink')
poly([(49,15),(62,21),(62,25),(49,19)],'stone')
poly([(62,21),(71,16),(71,20),(62,25)],'stoneshade')
poly([(49,14),(58,10),(71,16),(62,21)],'stonelight')
poly([(53,14),(58,12),(67,16),(62,18)],'ink')
line((54,15),(61,18),'coal')
line((49,14),(62,20),'ivory')
line((63,21),(70,17),'stone')

# Hanging wooden sign, suspended on two iron hooks from the eave.
line((46,72),(46,79),'ink')
line((56,77),(56,84),'ink')
c.set(46,75,'ironlight'); c.set(56,80,'ironlight')
poly([(43,77),(58,84),(58,95),(42,87)],'ink')
poly([(44,79),(56,85),(56,92),(44,86)],'woodmid')
line((44,79),(56,85),'woodhi')
line((44,86),(56,92),'wooddark')
line((45,85),(55,90),'wood')
# Cream anvil emblem, with a horn, narrow waist and flared base.
poly([(45,81),(49,83),(50,82),(55,85),(53,86),(49,85),(47,84)],'ivory')
line((50,85),(50,87),'ivory')
line((48,86),(53,89),'ivory')
c.set(44,80,'ironhi'); c.set(56,86,'ironhi')

# Three coopered barrels, two below and one resting on top.
def barrel(cx, by, r=6, h=17):
    ty=by-h
    c.ellipse(cx,by,r,3,'ink')
    poly([(cx-r+1,ty),(cx+r-1,ty),(cx+r,ty+4),(cx+r,by-3),(cx+r-2,by),(cx-r+2,by),(cx-r,by-3),(cx-r,ty+4)],'wooddark')
    poly([(cx-r+2,ty+2),(cx+r-2,ty+2),(cx+r-1,ty+5),(cx+r-1,by-3),(cx+r-2,by-1),(cx-r+2,by-1),(cx-r+1,by-3),(cx-r+1,ty+5)],'woodmid')
    poly([(cx+1,ty+2),(cx+r-2,ty+2),(cx+r-1,ty+5),(cx+r-1,by-3),(cx+1,by)],'wood')
    line((cx-3,ty+3),(cx-3,by-2),'woodlight')
    line((cx,ty+3),(cx,by-1),'wooddark')
    line((cx+3,ty+3),(cx+3,by-2),'wooddark')
    for y in [ty+5,by-4]:
        poly([(cx-r,y-1),(cx-2,y+1),(cx+2,y+1),(cx+r,y-1),(cx+r,y+1),(cx+2,y+3),(cx-2,y+3),(cx-r,y+1)],'iron')
        line((cx-r+1,y),(cx-2,y+2),'ironlight')
        line((cx-2,y+2),(cx+1,y+2),'ironmid')
        c.set(cx+3,y+1,'ironlight')
    c.ellipse(cx,ty,r-1,3,'wooddark')
    c.ellipse(cx,ty,r-2,2,'woodlight')
    line((cx-r+2,ty),(cx+r-2,ty+2),'wood')
    line((cx-1,ty-1),(cx+3,ty+1),'woodmid')
    c.set(cx-1,ty,'woodhi')
    line((cx-r+2,ty+2),(cx-1,ty+3),'woodhi')
barrel(118,99,6,17)
barrel(105,105,7,18)
barrel(110,86,6,16)

# Anvil on a short oak block on the open left edge of the apron.
c.ellipse(45,109,11,4,'shadow')
poly([(39,100),(47,97),(53,101),(53,109),(46,113),(39,109)],'wooddark')
poly([(40,102),(46,105),(46,111),(40,108)],'woodmid')
poly([(47,105),(52,102),(52,108),(47,111)],'wood')
line((42,104),(42,108),'woodlight')
line((49,105),(49,109),'wooddark')
# Silhouette of horn, heel, narrow waist and flared foot.
poly([(31,96),(39,95),(43,92),(57,98),(57,101),(51,104),(49,104),(49,107),(53,108),(46,111),(36,106),(41,104),(41,102),(35,100)],'ink')
poly([(32,96),(39,96),(43,93),(55,98),(47,102),(39,99)],'ironlight')
poly([(38,99),(47,103),(55,99),(55,101),(49,104),(47,105),(47,108),(51,108),(46,110),(39,106),(43,105),(43,102)],'iron')
line((33,96),(40,97),'ironhi')
line((43,93),(54,98),'ironhi')
line((41,100),(47,103),'ironmid')
line((46,105),(46,108),'ironmid')
line((40,107),(46,110),'ironlight')
# A smith's hammer lies beside the glowing hearth.
line((83,112),(91,107),'wooddark')
line((83,111),(91,106),'woodlight')
poly([(89,104),(93,102),(97,105),(93,108),(89,106)],'ink')
poly([(89,104),(93,102),(96,104),(92,106)],'ironlight')
line((92,107),(96,105),'iron')
# Coal fragments and a few warmth-colored stones in front of the forge.
for x,y in [(76,112),(79,110),(80,115),(97,101)]:
    c.rect(x,y,2,2,'coal')
c.set(79,110,'ember'); c.set(96,101,'orange')
for x,y in [(15,94),(23,100),(67,119),(114,104),(11,91)]:
    line((x,y),(x+3,y+1),'moss')
    c.set(x+1,y-1,'mosslight')

# Validate the required native size and visible palette before export.
w, h, raw = result.to_rgba()
visible_colours = {bytes(raw[i:i+4]) for i in range(0, len(raw), 4) if raw[i+3] > 0}
assert (w, h) == (128, 128)
assert len(visible_colours) <= 86
print(f'Validated {w}x{h}; {len(visible_colours)} visible colours; transparent background.')
view(result, scale=4, margin=0)
save('red-roofed-forge-house', result)
finish(result)
