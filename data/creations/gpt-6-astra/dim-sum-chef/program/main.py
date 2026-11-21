result = new_canvas(32,32, name='dim_sum_chef')
c=result
ink='#302b35'
shadow='#62677b'
cloth='#dce3df'
white='#fff5de'
skin='#e8a06c'
light='#ffd29a'
skindark='#b96650'
wood='#bc733f'
gold='#e5ad5b'
# shoes and trousers
c.rect(10,25,5,5,ink); c.rect(17,25,5,5,ink)
c.rect(11,26,3,2,shadow); c.rect(18,26,3,2,shadow)
c.rect(9,29,6,2,ink); c.rect(17,29,6,2,ink)
c.line(10,29,12,29,'#777584'); c.line(18,29,20,29,'#777584')
# jacket silhouette and shoulders
c.poly([(9,13),(12,12),(20,12),(23,13),(25,17),(24,23),(21,25),(10,25),(7,23),(6,17)],ink)
c.poly([(9,14),(12,13),(20,13),(23,14),(24,18),(22,22),(9,22),(7,18)],cloth)
c.line(8,16,8,18,white); c.line(23,16,23,18,white)
# apron straps and bib
c.rect(11,14,10,12,shadow)
c.rect(12,15,8,10,'#a2b8b5')
c.line(12,13,14,16,white); c.line(19,13,17,16,white)
c.rect(10,23,12,4,ink)
c.rect(11,23,10,3,'#a2b8b5')
c.line(11,26,20,26,'#dce3df')
c.rect(12,23,2,2,'#eaf0e5'); c.set(15,25,white); c.set(18,24,'#eaf0e5'); c.set(19,25,'#dce3df'); c.set(12,16,white)
# ears and face
c.rect(9,8,14,4,ink)
c.rect(10,9,2,2,skin); c.rect(21,9,1,2,skin)
c.rect(11,5,10,8,ink)
c.rect(12,6,8,7,skin)
c.rect(12,7,7,4,light)
c.line(13,13,18,13,ink)
c.set(12,11,skindark); c.set(19,11,skindark)
c.set(13,9,ink); c.set(18,9,ink)
c.set(16,10,skin)
c.line(14,11,17,11,skindark); c.line(15,12,16,12,light)
# tall chef toque
c.poly([(10,7),(10,5),(8,5),(8,3),(10,1),(14,1),(15,2),(17,1),(21,1),(23,3),(23,5),(21,6),(21,8),(10,8)],ink)
c.poly([(10,5),(9,4),(10,2),(13,2),(15,3),(17,2),(20,2),(22,3),(22,4),(20,5),(20,7),(11,7),(11,5)],cloth)
c.line(11,2,13,2,white); c.line(10,3,13,3,white); c.line(17,2,20,2,white); c.line(16,3,21,3,white)
c.line(11,6,20,6,white)
c.set(14,4,'#a2b8b5'); c.set(19,4,'#a2b8b5')
# back rim of bamboo steamer
c.ellipse(16,19,9,3,ink)
c.ellipse(16,19,8,2,wood)
c.line(11,17,20,17,gold)
# buns individually inked
for x,y in [(11,18),(16,17),(21,18)]:
    c.poly([(x-3,y),(x-2,y-2),(x,y-3),(x+2,y-2),(x+3,y),(x+2,y+2),(x-2,y+2)],ink)
    c.poly([(x-2,y),(x-1,y-2),(x+1,y-2),(x+2,y),(x+1,y+1),(x-1,y+1)],white)
    c.set(x,y-1,'#d6b88b'); c.set(x+1,y,'#ecd6b0')
# front bamboo basket wall, clear rim
c.poly([(7,20),(9,19),(12,20),(20,20),(23,19),(25,20),(24,23),(21,24),(11,24),(8,23)],ink)
c.poly([(9,20),(12,21),(20,21),(23,20),(23,22),(20,23),(12,23),(9,22)],wood)
c.line(11,21,21,21,gold)
c.line(12,23,20,23,gold)
for x in [11,14,18,21]: c.set(x,22,'#f3c778')
# supporting hands over ends, outlined against both sleeve and basket
c.poly([(6,19),(8,18),(10,19),(10,22),(8,23),(6,22)],ink)
c.rect(7,19,2,3,skin); c.set(7,19,light); c.set(9,20,light); c.set(8,22,skindark)
c.poly([(24,18),(26,19),(26,22),(24,23),(22,22),(22,19)],ink)
c.rect(23,19,2,3,skin); c.set(24,19,light); c.set(22,20,light); c.set(23,22,skindark)
view(result,scale=12)
finish(result)
