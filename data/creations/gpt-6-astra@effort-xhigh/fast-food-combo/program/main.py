# 64px fast food still life, built from a deliberately small palette.
result = new_canvas(64, 64, background='#304c51', name='fast_food_combo')
c = result
P = {
 'ink':'#252b30', 'deep':'#213b40', 'bg2':'#3b595d',
 'rimdark':'#743b39', 'rim':'#b85148', 'rimlight':'#e68162',
 'paper':'#e7d9b8', 'paperlit':'#f7e9c9', 'papersh':'#c6b798', 'cast':'#a7987b',
 'bunshade':'#a7542e','bun':'#df8e3d','bunlit':'#efb253','bunhi':'#ffce70',
 'seed':'#fff0bd', 'seedsh':'#bd7433',
 'meat':'#65382d','meatlit':'#8b4d32','meathi':'#b86b3b',
 'green':'#57974a','greensh':'#356343','greenhi':'#9ec65c',
 'cheese':'#ffc947','cheesehi':'#ffe481','cheesesh':'#d58a28',
 'redsh':'#9b3638','red':'#db4e43','redhi':'#f67b59',
 'white':'#fff1d4','whitesh':'#b6b6a6','gray':'#798c89',
 'cola':'#422e2c','colahi':'#815038','ice':'#b3c7bb','icehi':'#e2e3c9',
 'sauce':'#a8382c','saucelit':'#e46035', 'mustard':'#e6a53c'
}
def poly(points, color, edge=None):
 c.poly(points, P.get(color,color))
 if edge: c.poly(points, P.get(edge,edge), fill=False)
def rect(x,y,w,h,col): c.rect(x,y,w,h,P.get(col,col))
def line(x0,y0,x1,y1,col): c.line(x0,y0,x1,y1,P.get(col,col))
def dot(x,y,col): c.set(x,y,P.get(col,col))
def ellipse(x,y,rx,ry,col): c.ellipse(x,y,rx,ry,P.get(col,col))

# Quiet surface and the solid shadow beneath the tray.
line(4,16,11,16,'bg2'); line(3,17,7,17,'bg2')
line(54,57,60,57,'deep')
poly([(9,30),(52,25),(63,46),(63,55),(57,61),(12,63),(3,57),(1,49)],'deep')
# Thick coral tray, seen from above at a three-quarter angle.
poly([(9,24),(51,21),(61,44),(62,52),(56,59),(10,61),(2,54),(1,47)],'ink')
poly([(3,46),(59,44),(60,52),(55,57),(10,59),(3,53)],'rimdark')
line(11,59,54,57,'rim'); line(4,53,9,57,'rim')
poly([(9,22),(51,20),(60,43),(61,49),(55,56),(10,58),(2,51),(2,46)],'rim','ink')
line(10,23,49,21,'rimlight'); line(3,46,3,50,'rimlight')
line(4,51,10,56,'rimlight'); line(11,56,54,54,'rimlight')
poly([(11,26),(48,24),(56,43),(57,48),(52,52),(12,54),(7,49),(7,44)],'rimdark','ink')
poly([(12,27),(48,25),(55,43),(55,48),(51,51),(12,53),(8,49),(8,43)],'paper')
poly([(12,27),(47,25),(54,44),(51,48),(13,50),(9,47),(9,43)],'paperlit')
# Folded liner corners and a sparse printed border.
line(13,28,28,27,'papersh'); line(38,26,47,26,'papersh')
line(13,51,23,51,'papersh'); line(15,52,27,52,'papersh')
line(10,46,11,48,'rimlight'); line(13,50,15,50,'rimlight')
line(44,50,48,50,'rimlight')
# Cast shadows lock every item onto the same plane.
ellipse(32,35,9,4,'cast')
ellipse(48,37,9,4,'cast')
ellipse(20,47,14,5,'cast')
ellipse(40,48,9,4,'cast')
ellipse(51,48,6,4,'cast')

# Fries, drawn individually with dark ochre skins and luminous edges.
def fry(points, lightline):
 poly(points,'cheese','bunshade')
 line(*lightline,'cheesehi')
fry([(21,13),(24,12),(29,27),(25,28)],(22,14,26,25))
fry([(25,8),(28,8),(30,26),(27,27)],(26,9,28,24))
fry([(29,13),(32,12),(34,28),(30,28)],(30,14,32,25))
fry([(34,9),(37,10),(35,28),(32,28)],(35,11,33,25))
fry([(38,14),(40,15),(36,29),(33,28)],(38,16,35,25))
fry([(20,18),(22,17),(27,29),(24,30)],(21,19,25,27))
fry([(28,17),(30,17),(31,29),(28,29)],(29,18,29,25))
# Red carton: slanted side, dipped opening and a small gold emblem.
poly([(22,23),(26,24),(30,26),(35,24),(39,22),(37,33),(34,37),(26,36)],'red','ink')
poly([(35,25),(39,23),(37,33),(34,36),(33,28)],'redsh')
line(23,24,27,26,'redhi'); line(27,26,31,27,'redhi')
line(25,27,27,34,'redhi')
poly([(31,28),(34,28),(35,30),(34,32),(31,32),(30,30)],'cheese')
line(32,29,32,31,'white')

# Cola cup: tapered paper body, a red wrap and cream lip.
poly([(40,15),(56,15),(54,34),(52,37),(45,37),(42,34)],'ink')
poly([(41,16),(55,16),(53,34),(51,36),(46,36),(43,33)],'white')
poly([(52,18),(55,17),(53,34),(51,36),(50,35)],'whitesh')
poly([(42,22),(54,22),(53,30),(51,32),(45,32),(43,30)],'red')
poly([(52,22),(54,22),(53,30),(51,32),(50,31)],'redsh')
line(43,23,44,29,'redhi')
# A clean, tiny cup badge.
poly([(48,23),(50,25),(50,28),(48,30),(46,28),(46,25)],'white')
line(47,27,49,25,'cheese')
line(46,35,50,35,'paper')
# Rim and dark, open cola surface.
ellipse(48,14,8,4,'ink')
ellipse(48,14,7,3,'white')
ellipse(48,14,6,2,'cola')
line(46,16,51,16,'colahi')
dot(43,14,'bunlit'); dot(53,14,'bunlit')
# Separate faceted ice cubes float in the cola.
poly([(44,13),(46,12),(48,13),(47,15),(45,15)],'#86a8a6')
line(45,13,46,13,'icehi'); line(45,14,47,14,'ice')
poly([(49,14),(51,13),(53,14),(52,16),(50,16)],'#86a8a6')
line(50,14,51,14,'icehi'); line(50,15,52,15,'ice')
dot(48,12,'colahi')
# Bent paper straw has an outline and red diagonal bands.
poly([(50,13),(50,7),(54,3),(56,3),(57,4),(53,8),(53,13)],'ink')
line(51,12,51,8,'white'); line(52,12,52,8,'white')
line(51,8,55,4,'white'); line(52,8,56,4,'white')
line(51,10,52,9,'red'); line(53,6,54,6,'red'); dot(56,4,'redhi')

# Burger on a folded napkin, front-left and larger than the other food.
poly([(8,43),(19,40),(33,48),(25,54),(11,50)],'papersh')
poly([(8,42),(19,40),(32,47),(24,52),(11,49)],'white')
line(12,48,23,51,'paper')
# Bottom bun, rounded with a visible toasted underside.
poly([(7,40),(10,37),(28,37),(32,41),(32,45),(29,48),(24,50),(14,50),(9,48),(6,45)],'ink')
poly([(8,41),(12,39),(27,39),(30,42),(30,45),(27,47),(23,48),(14,48),(9,46)],'bun')
poly([(9,43),(14,45),(25,45),(30,42),(29,45),(25,47),(15,47),(10,45)],'bunlit')
line(13,48,23,48,'bunshade'); dot(10,44,'bunhi'); line(15,46,21,46,'bunhi')
# Rough charred patty and small grill highlights.
poly([(7,38),(11,36),(27,36),(31,39),(32,42),(29,44),(25,45),(13,45),(8,43),(6,41)],'ink')
poly([(8,39),(13,38),(27,38),(30,40),(30,42),(26,43),(14,43),(9,42)],'meat')
line(11,41,15,42,'meatlit'); line(18,43,23,43,'meatlit')
line(25,41,29,40,'meathi'); dot(10,40,'meathi'); dot(17,42,'meathi'); dot(24,42,'meatlit')
# Melted cheese: bright edge and two drips over the patty.
poly([(7,37),(16,35),(30,37),(31,39),(26,40),(23,43),(20,40),(15,40),(11,42),(10,39)],'cheesesh','bunshade')
poly([(8,37),(17,36),(29,37),(30,38),(25,39),(23,41),(20,39),(15,39),(11,41),(11,38)],'cheese')
line(13,37,22,37,'cheesehi'); line(22,40,23,40,'cheesehi')
# Ruffled lettuce escaping under the crown.
poly([(6,34),(9,32),(28,32),(31,34),(33,36),(30,38),(28,37),(25,39),(22,37),(18,39),(15,37),(12,39),(10,37),(7,37)],'greensh','ink')
poly([(7,34),(11,34),(14,35),(18,34),(22,35),(27,34),(31,35),(29,37),(26,36),(24,38),(21,36),(17,37),(14,36),(11,37),(9,35)],'green')
line(8,34,11,35,'greenhi'); line(16,35,19,35,'greenhi'); line(25,35,29,35,'greenhi')
# Bun crown, its top ellipse and stepped, toasted lower edge.
poly([(6,32),(7,29),(10,26),(14,24),(22,24),(27,26),(30,29),(32,32),(31,34),(28,36),(23,37),(14,37),(9,35),(6,34)],'ink')
poly([(7,32),(8,29),(11,27),(15,25),(22,25),(26,27),(29,29),(30,32),(30,34),(26,35),(15,36),(10,34),(7,33)],'bun')
poly([(8,30),(11,27),(16,25),(21,25),(26,27),(28,29),(29,32),(25,34),(16,34),(11,33),(8,32)],'bunlit')
poly([(10,29),(13,27),(17,26),(21,26),(25,28),(26,30),(22,31),(14,31)],'bunhi')
line(8,33,12,35,'bunshade'); line(16,36,24,36,'bunshade'); line(28,34,30,33,'bunshade')
# Individually placed, directional sesame seeds.
for x,y,dx in [(12,29,1),(17,27,0),(22,28,1),(26,31,0),(19,31,1),(12,32,1),(24,33,1)]:
 dot(x,y+1,'seedsh'); line(x,y,x+dx,y if dx else y+1,'seed')

# Lettuce tips catch the light just below the crown.
line(8,36,10,36,'greenhi'); dot(11,37,'green')
line(15,37,17,37,'greenhi'); dot(18,38,'green')
line(23,37,25,37,'greenhi'); dot(28,37,'greenhi')
# Three irregular crispy nuggets, with compact crunchy pixel clusters.
def nugget(points, inner, details):
 poly(points,'bunshade','ink')
 poly(inner,'bunlit')
 for x,y,col in details: dot(x,y,col)
# Rear nugget.
nugget([(36,39),(39,38),(42,39),(44,42),(43,44),(39,46),(36,44),(35,42)],
 [(37,40),(40,39),(42,40),(42,42),(39,44),(37,43)],
 [(38,40,'cheesehi'),(39,40,'cheesehi'),(41,41,'bun'),(37,42,'bun'),(40,43,'bunhi'),(42,43,'bunshade')])
# Right nugget.
nugget([(43,44),(46,43),(49,45),(49,48),(47,50),(44,50),(41,48),(41,46)],
 [(44,45),(46,44),(48,46),(47,48),(44,48),(42,47)],
 [(44,45,'cheesehi'),(45,45,'cheesehi'),(47,46,'bun'),(43,47,'bun'),(46,48,'bunhi'),(48,48,'meathi')])
# Front nugget.
nugget([(34,45),(37,44),(40,46),(41,49),(39,51),(35,51),(32,49),(32,47)],
 [(34,46),(37,45),(39,47),(39,49),(35,49),(33,48)],
 [(35,46,'cheesehi'),(36,46,'cheesehi'),(38,47,'bun'),(34,48,'bun'),(37,49,'bunhi'),(39,50,'meathi')])

# Crisp little breading flecks and richer amber creases.
for x,y,col in [(36,41,'bunhi'),(38,42,'bunshade'),(40,40,'seed'),(41,43,'bun'),(37,44,'bun'),(43,46,'bunhi'),(45,47,'bunshade'),(47,45,'seed'),(46,49,'bun'),(33,47,'bunhi'),(36,48,'bunshade'),(38,46,'seed'),(34,49,'bunhi')]:
 dot(x,y,col)
# Two little dipping cups, with visible side walls and glossy sauces.
def dip(cx,cy, sauce, highlight):
 ellipse(cx,cy+3,5,3,'cast')
 poly([(cx-5,cy),(cx+5,cy),(cx+4,cy+4),(cx+2,cy+5),(cx-2,cy+5),(cx-4,cy+3)],'ink')
 poly([(cx-4,cy+1),(cx+4,cy+1),(cx+3,cy+3),(cx+1,cy+4),(cx-2,cy+3)],'whitesh')
 line(cx-3,cy+2,cx-2,cy+3,'white')
 ellipse(cx,cy,5,3,'ink')
 ellipse(cx,cy,4,2,'white')
 ellipse(cx,cy,3,1,sauce)
 line(cx-2,cy-1,cx,cy-1,highlight)
 dot(cx+3,cy+1,'paper')
dip(54,42,'sauce','saucelit')
dip(28,52,'mustard','cheesehi')
# A few crumbs on the paper, restrained and deliberate.
dot(34,39,'bunshade'); dot(33,40,'bunlit')
dot(44,53,'bunshade'); dot(45,53,'bunlit')
dot(48,39,'bunshade')

assert tuple(result.stats()['size']) == (64, 64)
assert result.stats()['colors_used'] <= 86
view(result, scale=8, margin=0)
save('fast_food_combo', result, indexed=True)
finish(result)
