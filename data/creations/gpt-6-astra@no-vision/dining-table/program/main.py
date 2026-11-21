# A compact, warmly lit dining set, seen from above at a slight angle.
result = new_canvas(64, 64, name="family_dining_table")
c = result
O = '#30252b'
D = '#50312c'
W = '#794732'
M = '#a7653c'
T = '#c48a50'
L = '#e4ad68'
H = '#f5cc84'
G = '#596d55'
S = '#89986b'
SH = '#b4bb83'

def rect(x,y,w,h,col): c.rect(x,y,w,h,col)
def line(x,y,x2,y2,col): c.line(x,y,x2,y2,col)
def poly(p,col): c.poly(p,col)

# Top chair: feet, seat and open spindle back.
rect(24,13,3,10,O); rect(38,13,3,10,O)
rect(25,14,1,7,M); rect(39,14,1,7,W)
rect(24,11,17,11,O)
rect(25,12,15,8,W)
rect(26,12,13,6,G)
rect(27,12,11,1,SH); rect(26,13,1,3,S)
rect(27,17,11,1,S)
# Exposed space separates the uprights and the three slats.
rect(23,4,4,11,O); rect(38,4,4,11,O)
rect(24,5,2,9,M); rect(39,5,2,9,T)
for x in (28,32,36):
    rect(x,7,2,6,O); rect(x,8,1,4,T)
rect(24,2,17,6,O)
rect(25,3,15,3,T); rect(26,3,13,1,L)
rect(25,6,15,1,W)

# Left chair, pointing inward.
rect(6,25,11,3,O); rect(7,26,9,1,T)
rect(6,39,11,3,O); rect(7,40,9,1,W)
poly([(6,26),(14,26),(17,29),(17,37),(14,40),(6,40)],O)
rect(7,28,8,10,W)
rect(8,28,7,9,G); rect(9,28,5,1,SH)
rect(8,29,1,6,S); rect(9,36,5,1,S)
rect(2,24,5,18,O)
rect(3,25,2,16,M); rect(3,25,1,15,L)
rect(6,25,1,16,W)
# Horizontal back rails, with dark gaps visible between.
for y in (27,32,37):
    rect(5,y,4,2,O); rect(5,y,3,1,T)
rect(2,24,5,2,O); rect(3,25,3,1,L)
rect(2,40,5,2,O)

# Right chair mirrors the construction, with the outer edge in shade.
rect(47,25,11,3,O); rect(48,26,9,1,T)
rect(47,39,11,3,O); rect(48,40,9,1,W)
poly([(49,26),(57,26),(57,40),(49,40),(46,37),(46,29)],O)
rect(48,28,8,10,W)
rect(48,28,7,9,G); rect(49,28,5,1,SH)
rect(48,29,1,6,S); rect(49,36,5,1,S)
for y in (27,32,37):
    rect(55,y,4,2,O); rect(56,y,2,1,T)
rect(57,24,5,18,O)
rect(58,25,3,15,W); rect(58,25,1,15,T)
rect(58,25,2,1,L)

# Rear structure and four short square table legs.
for x in (16,45):
    rect(x,39,4,12,O); rect(x+1,41,2,8,W)
    rect(x+1,41,1,6,T)
# Substantial bevel and apron under the tabletop.
poly([(16,19),(47,19),(50,22),(50,43),(47,47),(16,47),(13,44),(13,22)],O)
rect(15,38,34,6,W)
rect(17,43,30,3,M)
line(18,45,46,45,D)
# Rounded rectangular tabletop.
poly([(17,17),(46,17),(50,21),(50,40),(46,44),(17,44),(13,40),(13,21)],O)
poly([(17,18),(46,18),(49,21),(49,40),(46,43),(17,43),(14,40),(14,21)],T)
# Planks across the warm golden surface.
poly([(17,19),(46,19),(48,21),(48,24),(15,24),(15,21)],L)
rect(15,25,34,7,T)
rect(15,33,34,6,T)
poly([(15,40),(48,40),(46,42),(17,42)],M)
line(17,19,45,19,H)
line(15,24,48,24,M); line(15,25,48,25,L)
line(15,32,48,32,M); line(15,33,48,33,L)
line(15,39,48,39,M); line(17,40,46,40,L)
# Restrained grain, in short, deliberately stepped clusters.
line(19,21,25,21,T); line(20,22,23,22,T)
line(40,21,44,21,T)
line(17,28,22,28,M); line(19,29,24,29,L)
line(41,28,46,28,M)
line(18,35,22,35,M); line(19,36,24,36,L)
line(40,36,46,36,M); line(43,37,46,37,L)
line(22,41,25,41,T)
# A narrow oatmeal linen runner hanging over the near edge.
rect(28,19,9,24,'#ad8056')
rect(29,19,7,25,'#ded0a4')
rect(30,19,1,25,'#f4e3b6'); rect(35,19,1,25,'#b6ab85')
rect(29,43,7,3,'#c3b58d')
for x in (29,31,33,35): rect(x,46,1,1,'#e8d8ad')
line(30,21,34,21,'#b6ab85'); line(30,41,34,41,'#b6ab85')

# Near chair overlaps the apron: seat, turned posts and open back.
rect(24,48,3,13,O); rect(38,48,3,13,O)
rect(25,49,1,10,T); rect(39,49,1,10,W)
poly([(27,46),(38,46),(41,49),(41,55),(24,55),(24,49)],O)
rect(26,48,13,6,W)
rect(27,48,11,5,G)
line(28,48,37,48,SH); line(27,49,27,51,S)
line(28,52,37,52,S)
# Posts and visible open spindle work above the broad near back rail.
rect(23,51,4,10,O); rect(38,51,4,10,O)
rect(24,52,2,8,T); rect(39,52,2,8,M)
for x in (28,32,36):
    rect(x,53,2,5,O); rect(x,53,1,4,T)
rect(24,57,17,5,O)
rect(25,58,15,2,M); rect(25,58,15,1,L)
rect(26,60,13,1,W)

# Ceramic bowl on the table, with a tiny cast shadow.
c.ellipse(33,35,10,3,'#95613f')
poly([(23,30),(41,30),(40,35),(37,38),(28,38),(24,35)],O)
poly([(24,31),(40,31),(39,35),(36,37),(29,37),(26,35)],'#3e777b')
poly([(25,32),(29,34),(38,34),(36,36),(29,36),(26,34)],'#75a4a0')
line(28,36,35,36,'#b0cec0')
c.ellipse(32,30,9,4,O)
c.ellipse(32,30,8,3,'#bad0b6')
c.ellipse(32,30,7,2,'#4c6760')
# Fruit silhouettes: red apple, golden pear and green apple.
c.circle(28,28,4,O)
c.circle(28,28,3,'#bd4b3c')
rect(26,26,2,2,'#ee8960'); rect(29,29,2,2,'#923d38')
line(28,23,28,25,D); line(29,24,31,23,G)
poly([(33,23),(36,23),(36,26),(38,28),(38,31),(36,33),(32,32),(31,29),(33,26)],O)
poly([(34,24),(35,24),(35,27),(37,29),(36,31),(33,31),(32,29),(34,26)],'#e1ac46')
line(34,27,33,29,'#ffe08a'); c.set(34,25,'#ffe08a')
line(34,22,35,21,D)
c.circle(38,28,3,O); c.circle(38,28,2,'#88a14d')
c.set(37,27,'#c4cc73'); line(38,24,39,23,D)
# Small bunch of purple grapes peeks over the near rim.
for x,y in [(29,31),(32,31),(30,33),(33,33),(32,35)]:
    c.circle(x,y,1,'#654064'); c.set(x,y,'#aa7190')
# The bowl's bright front lip ties the fruit together.
line(24,32,26,33,'#d4ddc0')
line(35,33,39,32,'#d4ddc0')

print(c.stats_text())
print(c.matrix_text(region=(20,20,43,39)))
finish(result)
