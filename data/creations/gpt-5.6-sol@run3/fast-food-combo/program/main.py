from pixelbench_api import *

c = new_canvas(64,64, '#253c43', name='combo')
O='#211f29'
# Tray, with a raised lip and an inset paper liner.
c.ellipse(33,53,29,8,'#1b3038')
c.poly([(2,29),(39,18),(61,29),(61,47),(25,61),(2,46)],O)
c.poly([(3,29),(39,20),(60,30),(59,46),(25,59),(3,45)],'#687b83')
c.poly([(4,30),(39,22),(58,30),(57,43),(25,56),(5,43)],'#bac3b8')
c.poly([(6,31),(39,23),(56,31),(55,42),(25,54),(7,42)],'#eee0bd')
c.line(4,46,25,58,'#9aafb0'); c.line(26,58,59,46,'#82979e')
c.line(8,41,25,52,'#d2bd96')
c.line(32,48,51,41,'#d2bd96')
# Carton of fries at the back, each fry edged and lit.
for x,y,h in [(24,14,15),(28,10,18),(32,13,16),(36,9,19),(39,13,15),(43,14,14)]:
    c.poly([(x,y+1),(x+2,y),(x+4,y+2),(x+3,y+h),(x,y+h)],O)
    c.rect(x+1,y+2,2,h-2,'#df922e')
    c.line(x+1,y+2,x+1,y+h-2,'#ffe18b')
    c.set(x+2,y+2,'#fff0b4')
c.poly([(23,25),(28,24),(32,28),(37,28),(44,23),(43,37),(32,41),(25,36)],O)
c.poly([(25,27),(28,26),(32,30),(37,30),(42,26),(41,36),(32,39),(27,35)],'#c83c3a')
c.poly([(25,27),(28,28),(30,36),(32,39),(27,35)],'#f2634a')
c.poly([(38,30),(42,26),(41,36),(37,37)],'#952f3b')
c.line(28,29,29,34,'#ff8a62')
c.poly([(32,32),(35,31),(37,32),(36,35),(33,36),(31,34)],'#ffd879')
c.set(34,33,'#fff2ba')
# Cola cup, tapered body and visible open rim.
c.poly([(44,17),(57,17),(55,35),(51,38),(46,35)],O)
c.poly([(45,19),(56,19),(54,34),(51,36),(47,34)],'#d9e4da')
c.poly([(45,22),(48,24),(55,23),(54,31),(50,33),(46,30)],'#d94a43')
c.line(47,25,48,29,'#fa8060')
c.line(54,24,53,31,'#9b3440')
c.ellipse(50,17,8,4,O)
c.ellipse(50,17,7,3,'#f5eed8')
c.ellipse(50,17,5,2,'#4c292b')
c.line(47,18,50,19,'#8f4a30')
# Floating ice facets.
c.poly([(46,16),(49,15),(50,17),(47,18)],'#b9c8bd')
c.set(47,16,'#eff6de')
c.poly([(51,16),(54,16),(53,18),(51,18)],'#839d9c')
c.set(52,16,'#e6ebd4')
# Bent striped straw.
c.line(51,16,53,6,O); c.line(53,6,59,3,O)
c.line(52,16,54,7,'#f7e9cb'); c.line(54,7,59,4,'#f7e9cb')
for x,y in [(53,12),(54,8),(57,5)]: c.set(x,y,'#ed5b51')
# Burger shadow and bottom bun.
c.ellipse(18,44,14,5,'#c0a77c')
c.ellipse(18,41,14,7,O)
c.ellipse(18,41,12,5,'#b96c32')
c.ellipse(18,40,12,4,'#efb054')
c.line(10,44,20,45,'#f4c56e')
# Seared patty.
c.ellipse(18,38,14,5,O)
c.ellipse(18,38,12,3,'#66392e')
c.line(9,39,15,40,'#965031'); c.line(20,39,26,38,'#a85e35')
c.set(12,37,'#c27b42'); c.set(23,39,'#c27b42')
# Melted cheese corners.
c.poly([(6,35),(18,32),(30,35),(28,39),(23,38),(21,41),(16,38),(10,39)],O)
c.poly([(7,35),(18,33),(29,35),(27,38),(23,37),(21,39),(16,37),(10,38)],'#ffbf3f')
c.line(10,35,20,35,'#ffe184')
# Lettuce ruffle and a narrow tomato layer.
c.ellipse(18,33,13,4,'#8f3031')
c.line(9,34,16,35,'#ef6650')
c.poly([(4,31),(7,28),(12,29),(17,27),(22,29),(28,28),(32,31),(30,34),(26,33),(23,35),(19,33),(15,35),(11,33),(7,34)],O)
c.poly([(5,31),(8,29),(12,30),(17,28),(22,30),(28,29),(31,31),(29,33),(26,32),(23,34),(19,32),(15,34),(11,32),(7,33)],'#5c963b')
c.line(8,30,12,31,'#a7c956'); c.line(17,30,21,31,'#a7c956'); c.set(27,31,'#a7c956')
# Domed sesame crown.
c.poly([(5,29),(6,25),(9,21),(14,19),(22,19),(27,21),(30,25),(31,29),(28,32),(21,33),(12,32),(7,31)],O)
c.poly([(6,28),(8,24),(11,22),(15,20),(21,20),(26,22),(29,26),(30,29),(27,31),(21,32),(12,31),(8,30)],'#d68b3e')
c.poly([(7,27),(10,23),(15,21),(21,21),(26,23),(28,26),(26,28),(19,29),(12,29)],'#efb95f')
c.line(12,22,19,21,'#ffd58a')
c.line(11,30,21,31,'#ba7034')
for x,y in [(11,25),(16,23),(22,24),(26,27),(18,27),(8,28),(23,29)]:
    c.set(x,y,'#fff0b5'); c.set(x+1,y-1,'#fff0b5')
# Nuggets on the paper, irregular crisp silhouettes.
def nugget(x,y,flip=False):
    c.poly([(x,y+2),(x+2,y),(x+6,y),(x+9,y+3),(x+9,y+6),(x+6,y+8),(x+2,y+7),(x,y+5)],O)
    c.poly([(x+1,y+2),(x+3,y+1),(x+6,y+1),(x+8,y+3),(x+8,y+5),(x+6,y+7),(x+2,y+6),(x+1,y+4)],'#bf7835')
    c.poly([(x+2,y+2),(x+5,y+1),(x+7,y+3),(x+6,y+5),(x+2,y+5)],'#efb64f')
    for dx,dy in [(3,2),(6,3),(2,4)]: c.set(x+dx,y+dy,'#ffdb7d')
    c.set(x+4,y+5,'#c68b37'); c.set(x+7,y+5,'#92502f')
nugget(43,38); nugget(35,42); nugget(45,46)
# Two shallow dipping cups with glossy sauce.
def dip(x,y,sauce,light):
    c.ellipse(x,y+2,5,4,O)
    c.ellipse(x,y+2,4,3,'#a5b5b3')
    c.ellipse(x,y,5,3,O)
    c.ellipse(x,y,4,2,'#f7eed8')
    c.ellipse(x,y,3,1,sauce)
    c.line(x-2,y-1,x,y-1,light)
    c.set(x-3,y+2,'#f1e6ce')
dip(25,50,'#a53432','#f27751')
dip(35,53,'#bd8b41','#ffe4a0')

# Keep the final palette within the requested visible-colour budget.
from collections import Counter
counts = Counter(c.get(x,y) for y in range(64) for x in range(64))
rgba = {p['index']: p['rgba'] for p in c.palette()}
while len(counts) > 86:
    a,b = min(((a,b) for a in counts for b in counts if a < b), key=lambda pair: sum((rgba[pair[0]][k]-rgba[pair[1]][k])**2 for k in range(3)))
    if counts[a] > counts[b]: a,b = b,a
    for y in range(64):
        for x in range(64):
            if c.get(x,y) == a: c.set(x,y,b)
    counts[b] += counts.pop(a)
view(c, scale=8)
finish(c)
