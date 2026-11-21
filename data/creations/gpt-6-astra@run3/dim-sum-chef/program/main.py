result = new_canvas(32, 32, name='dim_sum_chef')
c=result
ink='#302b35'
shadow='#5c626d'
white='#fff5dc'
cloth='#d9e5df'
shade='#97b6b4'
skin='#e8a477'
light='#ffd09b'
skindark='#ad6454'
wood='#ce8d47'
woodlight='#f3c877'
wooddark='#87532e'
# shoes, trouser legs
c.rect(10,26,5,4,ink).rect(17,26,5,4,ink)
c.rect(11,26,3,2,shadow).rect(18,26,3,2,shadow)
c.rect(9,29,6,2,ink).rect(17,29,6,2,ink)
c.line(10,29,12,29,shadow).line(18,29,20,29,shadow)
# coat silhouette and sleeves
c.poly([(10,12),(21,12),(24,14),(26,19),(24,22),(22,22),(22,27),(9,27),(9,22),(7,22),(5,19),(7,14)],ink)
c.poly([(10,13),(21,13),(23,15),(24,18),(22,20),(21,25),(10,25),(9,20),(7,18),(8,15)],cloth)
c.poly([(8,15),(10,14),(10,18),(8,20),(6,19)],white)
c.poly([(22,14),(24,16),(25,19),(23,20),(21,18)],shade)
# neck and collar
c.rect(13,11,6,4,ink).rect(14,12,4,3,skin)
c.poly([(10,13),(13,12),(15,15),(13,17)],white)
c.poly([(18,12),(21,13),(18,17),(16,15)],white)
c.set(15,15,skindark).set(16,15,skindark)
# apron shoulder straps and lower apron
c.line(11,14,11,18,wooddark).line(20,14,20,18,wooddark)
c.rect(11,16,10,10,shade)
c.rect(12,16,8,9,'#699a98')
c.line(11,26,20,26,cloth)
# flour dust clearly visible below basket
c.rect(12,24,2,2,cloth).set(14,24,white).set(15,25,cloth)
c.set(18,24,cloth).set(19,25,white).set(11,23,white)
# head ears
c.rect(9,7,3,4,ink).rect(20,7,3,4,ink)
c.rect(10,8,2,2,skin).rect(20,8,2,2,skin)
c.poly([(11,5),(20,5),(21,7),(21,11),(19,13),(13,13),(10,10),(10,7)],ink)
c.poly([(12,6),(19,6),(20,8),(20,11),(18,12),(13,12),(11,10),(11,7)],skin)
c.rect(12,6,7,4,light)
c.set(12,8,ink).set(18,8,ink)
c.set(11,10,'#d77c67').set(19,10,'#d77c67')
c.set(15,10,skindark)
c.line(14,11,17,11,ink)
# puffed chef toque
c.poly([(10,7),(10,5),(8,5),(8,3),(9,2),(12,2),(13,1),(18,1),(19,2),(22,2),(23,3),(23,5),(21,6),(21,7)],ink)
c.poly([(10,5),(9,4),(10,3),(13,3),(14,2),(17,2),(19,3),(21,3),(22,4),(20,5),(20,6),(11,6),(11,5)],cloth)
c.rect(11,3,3,2,white).rect(14,2,4,3,white).rect(19,3,2,2,white)
c.line(11,6,20,6,white)
# steamer dark back rim behind food
c.ellipse(15,19,10,3,ink)
c.ellipse(15,18,9,2,wooddark)
c.line(9,17,22,17,woodlight)
# three plump buns, individually outlined
for x,y in [(10,17),(15,16),(20,17)]:
    c.poly([(x-3,y+2),(x-3,y),(x-2,y-2),(x,y-3),(x+2,y-2),(x+3,y),(x+3,y+2)],wooddark)
    c.poly([(x-2,y+1),(x-2,y-1),(x,y-2),(x+2,y-1),(x+2,y+1)],white)
    c.set(x,y-2,'#d8b985').set(x-1,y-1,'#e7d1a1').set(x+1,y,'#e7d1a1')
# rounded bun bases sit above the rim
c.line(8,18,12,18,'#e7d1a1')
c.line(13,17,17,17,'#e7d1a1')
c.line(18,18,22,18,'#e7d1a1')
# bamboo basket front, strong boundary below buns
c.line(6,19,24,19,ink)
c.poly([(6,20),(24,20),(23,23),(21,24),(9,24),(7,23)],wooddark)
c.rect(8,20,15,3,wood)
c.line(8,20,22,20,woodlight)
c.line(9,23,21,23,woodlight)
for x in (10,14,18,22):
    c.line(x,21,x,22,wooddark)
    c.set(x+1,21,woodlight)
# hands wrap around the sides without merging into basket
c.poly([(5,18),(7,18),(8,19),(8,22),(6,23),(4,21),(4,19)],ink)
c.rect(5,19,2,3,skin).set(5,19,light).set(7,20,light)
c.poly([(24,18),(26,18),(27,19),(27,21),(25,23),(23,22),(23,19)],ink)
c.rect(24,19,2,3,skin).set(24,19,light).set(24,20,light)
view(c, scale=12)
finish(result)
