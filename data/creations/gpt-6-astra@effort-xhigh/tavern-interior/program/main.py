# A small tavern after sundown. All clusters are painted on the native 64px grid.
result = new_canvas(64,64, '#211b23', name='The Amber Lantern')
c = result
P = {
'ink':'#211b23','deep':'#2c2027','shadow':'#38262c','wall':'#493033',
'wall2':'#563735','warmwall':'#644235','litwall':'#754c37','glowwall':'#875c3c',
'wooddark':'#3e292b','woodshade':'#59352e','wood':'#7c4734','woodlight':'#a56a40',
'goldwood':'#c38b4d','edge':'#dea65b','cream':'#f5d18a','light':'#ffe7ae',
'amber':'#db9a47','gold':'#b87535','floor':'#4a3030','floorlight':'#654032',
'floordark':'#35272c','metal':'#55504a','metalhi':'#8a7b61',
'green':'#426257','greenhi':'#7e9471','greendark':'#2d413f',
'red':'#824849','redhi':'#b87459','blue':'#344654','bluehi':'#587080',
'glass':'#798874','glasshi':'#c0bd89','haze':'#947353','hazedark':'#735742'
}
def r(x,y,w,h,k): c.rect(x,y,w,h,P.get(k,k))
def l(x,y,xx,yy,k): c.line(x,y,xx,yy,P.get(k,k))
def p(pts,k): c.poly(pts,P.get(k,k))
def dot(x,y,k): c.set(x,y,P.get(k,k))
# Plaster, timber and pools of lamplight.
r(1,4,62,35,'wall')
r(2,10,60,23,'wall2')
p([(9,13),(20,11),(28,29),(25,36),(5,36)],'warmwall')
p([(13,15),(19,15),(24,31),(10,31)],'litwall')
p([(38,12),(52,12),(61,32),(31,32)],'warmwall')
p([(42,14),(49,13),(56,30),(35,30)],'litwall')
r(1,32,62,8,'woodshade')
l(1,32,62,32,'woodlight')
l(1,34,62,34,'wooddark')
for x in (4,11,19,27,35,43,51,59):
    l(x,35,x,40,'wooddark')
# Floorboard perspective.
r(0,40,64,24,'floor')
p([(12,40),(48,40),(63,64),(0,64)],'floorlight')
p([(1,44),(18,42),(6,64),(0,64)],'floor')
p([(47,42),(60,42),(63,64),(61,64)],'floor')
for a,b in [(3,-15),(14,1),(25,20),(36,40),(47,60),(58,79)]:
    # endpoints kept in frame by short interpolation
    for y in range(41,64):
        x=round(a+(b-a)*(y-41)/23)
        if 0 <= x < 64: dot(x,y,'floordark')
for y in (45,51,58): l(0,y,63,y,'floordark')
for x,y,w in [(4,48,6),(15,54,9),(33,61,12),(47,55,10),(4,61,8),(53,47,6),(27,44,8)]:
    l(x,y,x+w,y,'woodlight')
# Small nighttime window at the left, with thick wooden mullions.
r(2,16,12,17,'ink')
r(3,15,10,17,'ink')
r(4,17,8,13,'blue')
r(5,18,6,5,'bluehi')
r(5,24,6,6,'blue')
dot(6,19,'cream'); dot(7,19,'cream'); dot(6,20,'cream')
p([(4,29),(4,27),(7,24),(10,27),(12,25),(12,30)],'greendark')
l(7,17,7,30,'wooddark'); l(8,17,8,30,'woodlight')
l(4,23,11,23,'wooddark')
l(3,16,3,31,'woodlight')
r(2,31,13,2,'ink'); r(3,31,11,1,'goldwood')
# Cabinet recess and framing.
r(21,13,39,19,'ink')
r(23,15,35,15,'wooddark')
r(23,15,35,6,'shadow')
r(23,23,35,6,'shadow')
r(21,13,39,2,'wood'); l(22,13,58,13,'woodlight')
r(21,15,2,15,'wood'); l(21,15,21,29,'woodlight')
r(58,15,2,15,'woodshade')
r(40,15,2,15,'woodshade'); l(40,16,40,29,'wood')
# Individual bottle silhouettes: shoulder, neck, liquid and one reflected pixel.
def bottle(x,b,h,body,hi,w=3):
    r(x,b-h+3,w,h-2,'ink')
    r(x+1,b-h,1,3,'ink')
    r(x,b-h+4,w,h-4,body)
    r(x+1,b-h+2,1,h-2,body)
    dot(x+1,b-h+3,hi)
    if h>6: l(x,b-h+5,x,b-1,hi)
    dot(x+1,b-h,'goldwood')
    l(x,b,x+w-1,b,'ink')
# top shelf
bottle(24,20,6,'green','greenhi')
bottle(29,20,7,'red','redhi')
bottle(34,20,5,'gold','amber',4)
bottle(43,20,6,'green','greenhi')
bottle(48,20,7,'green','greenhi')
bottle(53,20,5,'gold','cream',4)
# shelf ledges overlap the bottoms of bottles.
r(20,21,40,2,'ink'); l(21,21,59,21,'goldwood'); l(22,22,58,22,'wood')
bottle(24,29,6,'gold','amber',4)
bottle(31,29,6,'green','greenhi')
bottle(36,29,5,'red','redhi')
bottle(44,29,7,'green','greenhi',4)
bottle(51,29,6,'red','redhi')
bottle(55,29,5,'gold','amber')
# pale paper bottle labels
r(25,27,2,1,'cream'); dot(32,27,'cream'); r(45,26,2,2,'goldwood'); dot(52,27,'cream')
r(20,30,41,3,'ink'); l(21,30,59,30,'goldwood'); l(21,31,59,31,'wood')
# Rear keg, tucked into the left-hand nook.
def barrel(x,y,w,h):
    p([(x+2,y),(x+w-3,y),(x+w-1,y+3),(x+w-1,y+h-4),(x+w-3,y+h-1),(x+2,y+h-1),(x,y+h-4),(x,y+3)],'ink')
    p([(x+2,y+1),(x+w-3,y+1),(x+w-2,y+4),(x+w-2,y+h-4),(x+w-3,y+h-2),(x+2,y+h-2),(x+1,y+h-4),(x+1,y+4)],'wood')
    p([(x+3,y+2),(x+w//2,y+1),(x+w//2+1,y+h-2),(x+2,y+h-3),(x+1,y+5)],'woodlight')
    for xx in (x+3,x+6,x+9):
        if xx<x+w-2: l(xx,y+3,xx,y+h-3,'woodshade')
    l(x+2,y+1,x+w-3,y+1,'goldwood')
    for yy in (y+4,y+h-5):
        l(x+1,yy,x+w-2,yy,'ink'); l(x+1,yy+1,x+w-2,yy+1,'metal')
        l(x+2,yy+1,x+4,yy+1,'metalhi')
    l(x+3,y+h-2,x+w-4,y+h-2,'woodshade')
barrel(2,34,11,13)
# Cast shadows underneath the bar and furniture.
p([(12,46),(63,44),(63,54),(18,55),(9,51)],'floordark')
c.ellipse(9,57,8,3,P['floordark'])
c.ellipse(25,60,10,2,P['floordark'])
c.ellipse(46,61,10,2,P['floordark'])
# The substantial bar: side return, panelled face and a polished thick top.
p([(12,36),(17,38),(17,51),(12,47)],'ink')
p([(13,38),(16,40),(16,48),(13,46)],'woodshade')
r(17,37,46,14,'ink')
r(18,39,44,10,'wood')
r(18,39,44,2,'woodshade')
for x,w in [(19,12),(34,12),(49,12)]:
    r(x,41,w,7,'wooddark')
    r(x+1,42,w-2,5,'woodshade')
    l(x+1,42,x+w-2,42,'woodlight')
    l(x+1,42,x+1,46,'woodlight')
    l(x+3,45,x+w-3,45,'wood')
for x in (17,31,46,61):
    r(x,39,2,11,'woodlight'); l(x+1,41,x+1,48,'wood')
l(18,49,62,49,'goldwood'); l(18,50,62,50,'woodshade')
p([(16,32),(59,32),(63,35),(63,39),(14,39),(11,37)],'ink')
p([(17,33),(58,33),(62,35),(14,35)],'woodlight')
l(15,35,61,35,'goldwood')
l(13,36,62,36,'edge'); l(14,37,62,37,'wood')
l(18,33,57,33,'goldwood')
l(20,34,33,34,'wood'); l(44,34,56,34,'wood')
# Tankards and glassware on the counter.
def mug(x,y):
    r(x,y,5,6,'ink'); r(x+4,y+1,3,3,'ink')
    r(x+4,y+1,2,2,'glasshi'); dot(x+4,y+2,'woodshade')
    r(x+1,y+1,3,4,'amber'); l(x+1,y+2,x+1,y+4,'cream')
    r(x,y,5,2,'cream'); r(x+1,y,3,1,'light')
    l(x+1,y+5,x+3,y+5,'gold')
mug(18,29); mug(44,29)
# A clear stemmed glass and the last green bottle.
r(34,30,4,3,'ink'); dot(35,31,'glasshi'); dot(36,31,'glass')
dot(35,33,'glasshi'); l(34,34,37,34,'cream')
bottle(56,34,7,'green','greenhi')
# A foreground barrel with a visible elliptic head.
barrel(2,43,12,15)
c.ellipse(7,44,4,2,P['ink']); c.ellipse(7,44,3,1,P['woodlight'])
l(5,44,9,44,'woodshade'); dot(8,43,'goldwood')
# Two low bar stools, splayed legs with warm rimmed round seats.
def stool(x,y):
    # y is seat center
    l(x-3,y+2,x-5,y+11,'ink'); l(x-2,y+2,x-4,y+11,'ink')
    l(x+3,y+2,x+5,y+11,'ink'); l(x+2,y+2,x+4,y+11,'ink')
    l(x-2,y+3,x-4,y+10,'woodlight'); l(x+2,y+3,x+4,y+10,'wood')
    l(x,y+3,x,y+8,'woodshade')
    l(x-3,y+7,x+3,y+7,'ink'); l(x-3,y+6,x+3,y+6,'woodlight')
    c.ellipse(x,y+1,6,3,P['ink'])
    c.ellipse(x,y,5,2,P['wood'])
    l(x-4,y-1,x+4,y-1,'goldwood'); l(x-3,y-2,x+3,y-2,'edge')
    l(x-3,y,x+3,y,'woodlight')
    dot(x-4,y+1,'woodshade'); dot(x+4,y+1,'woodshade')
stool(25,48); stool(46,49)
# Small material marks, kept in clusters so that the room stays legible.
# Golden reflections in bottle shoulders and little parchment labels.
dot(25,17,'glasshi'); dot(30,17,'redhi'); dot(44,17,'glasshi')
dot(49,16,'greenhi'); l(54,18,55,18,'cream')
dot(26,19,'greenhi'); dot(35,19,'amber'); dot(49,19,'greenhi')
l(30,19,31,19,'goldwood'); dot(37,28,'goldwood')
# Shelves have thin bevels, iron pegs, and interrupted grain.
for xx in (22,41,58): dot(xx,22,'wooddark')
l(27,14,35,14,'woodshade'); l(47,14,55,14,'woodshade')
l(26,31,30,31,'woodshade'); l(46,31,52,31,'woodshade')
# Hand-worn panel grain and joinery.
l(21,44,25,44,'wood'); dot(27,43,'wood')
l(36,46,41,46,'wood'); l(38,43,43,43,'wood')
l(51,44,56,44,'wood'); dot(58,46,'wood')
for xx in (18,32,47,62):
    dot(xx,40,'goldwood'); dot(xx,48,'wooddark')
l(22,38,31,38,'woodshade'); l(40,38,51,38,'woodshade')
l(18,36,21,36,'cream'); l(45,36,48,36,'cream')
# A folded linen bar cloth drapes over the polished lip.
p([(28,34),(31,34),(32,36),(32,41),(29,41),(29,37),(27,36)],'ink')
p([(28,34),(30,34),(31,36),(31,40),(30,40),(30,36),(28,36)],'glass')
l(28,35,30,35,'glasshi'); l(30,36,30,39,'glasshi')
dot(31,40,'metal')
# The hollow rims and highlights distinguish glass from the foamy ale.
dot(34,30,'glasshi'); dot(37,30,'glasshi'); dot(36,32,'glasshi')
dot(36,31,'wooddark'); dot(19,31,'light'); dot(45,31,'light')
# Iron hoop rivets and a tap on the stacked cask.
dot(3,48,'metalhi'); dot(11,48,'metalhi'); dot(11,54,'metalhi')
r(7,38,2,2,'ink'); dot(8,38,'goldwood'); dot(8,39,'amber')
# Bar stool grain, feet, and knots in the floorboards.
dot(23,48,'woodshade'); l(26,48,28,48,'goldwood')
l(44,49,47,49,'goldwood'); dot(49,50,'woodshade')
l(20,59,22,59,'ink'); l(28,59,30,59,'ink')
l(41,60,43,60,'ink'); l(49,60,51,60,'ink')
l(31,55,34,55,'woodshade'); dot(32,54,'wooddark'); dot(33,54,'wood')
l(56,60,59,60,'woodshade'); dot(58,59,'wooddark')
l(16,61,18,61,'woodshade'); dot(17,60,'wooddark')
# Smoke in the lamplight: broad muted stepped wisps, with broken edges.
c.path('M 17 28 Q 13 25 17 23 Q 20 21 17 19 Q 12 17 14 14',P['hazedark'],fill=False)
l(17,23,18,22,'haze'); dot(15,25,'haze')
c.path('M 29 10 Q 23 8 28 6 Q 35 3 39 7 Q 42 10 51 7',P['hazedark'],fill=False)
l(31,5,36,5,'haze'); l(41,8,46,8,'haze')
# Ceiling framing, the dark silhouette closes in around the warm interior.
r(0,0,64,4,'ink'); r(1,2,62,2,'wooddark')
l(3,4,61,4,'wood')
p([(0,2),(3,2),(13,12),(11,14),(0,5)],'ink')
l(2,4,11,12,'woodshade')
p([(60,3),(63,3),(63,9),(57,14),(55,13)],'ink')
l(61,5,56,12,'woodshade')
r(0,5,2,35,'ink'); l(2,6,2,14,'woodshade')
r(62,6,2,28,'ink'); l(61,14,61,29,'woodshade')
# Pendants: thin chains, brass shades, and pale yellow glowing bellies.
def lamp(x,y):
    l(x,4,x,y-1,'ink'); dot(x,6,'metalhi')
    r(x-1,y-1,3,2,'ink'); dot(x,y-1,'goldwood')
    p([(x-2,y),(x+2,y),(x+4,y+3),(x+4,y+5),(x-4,y+5),(x-4,y+3)],'ink')
    p([(x-2,y+1),(x+2,y+1),(x+3,y+3),(x-3,y+3)],'gold')
    l(x-1,y+1,x+1,y+1,'edge'); l(x-2,y+2,x+2,y+2,'amber')
    l(x-3,y+3,x+3,y+3,'cream'); l(x-2,y+4,x+2,y+4,'light')
    l(x-1,y+5,x+1,y+5,'amber')
lamp(16,10); lamp(46,8)
# Deliberate flecks of reflected light and shadow at the scene edge.
dot(10,53,'goldwood'); dot(28,56,'goldwood'); l(0,62,12,62,'shadow')
l(0,63,63,63,'ink'); dot(63,62,'ink'); dot(0,61,'ink')
width, height, rgba = result.to_rgba()
assert (width, height) == (64, 64)
assert len({bytes(rgba[i:i+4]) for i in range(0,len(rgba),4) if rgba[i+3]}) <= 86
save('amber_lantern_tavern', result)
view(result, scale=8, margin=0)
finish(result)
