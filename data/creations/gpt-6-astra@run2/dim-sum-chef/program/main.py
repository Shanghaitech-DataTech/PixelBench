result = new_canvas(32,32,name='dim_sum_chef')
c=result
ink='#342c36'
cloth='#ece8da'
light='#fff7e4'
shade='#b6c3c3'
apron='#557b85'
apronlight='#779ba1'
skin='#e5a776'
skinlight='#ffd09a'
skinshade='#b96e50'
wood='#c98c49'
woodlight='#f0bd70'
woodshade='#935a34'
# shoes and trouser legs
c.rect(10,26,5,4,ink).rect(17,26,5,4,ink)
c.rect(11,26,3,2,'#677785').rect(18,26,3,2,'#677785')
c.rect(9,29,6,2,ink).rect(17,29,6,2,ink)
c.line(10,29,13,29,'#72717b').line(18,29,21,29,'#72717b')
# jacket silhouette and sleeves
c.poly([(10,13),(21,13),(24,15),(26,19),(25,23),(22,24),(22,28),(9,28),(9,24),(6,23),(5,19),(7,15)],ink)
c.poly([(9,15),(12,14),(19,14),(22,15),(24,18),(24,22),(21,23),(21,27),(10,27),(10,23),(7,22),(7,18)],cloth)
c.line(8,17,7,20,light).line(23,17,24,20,shade)
# apron straps and body, distinct from white jacket
c.line(12,14,13,18,apron).line(19,14,18,18,apron)
c.poly([(13,16),(18,16),(20,20),(21,27),(10,27),(11,20)],apron)
c.rect(12,18,7,8,apronlight)
c.rect(13,23,5,3,apron).line(13,23,17,23,'#aac0ba')
# scattered flour patches on apron below basket
for x,y in [(11,24),(12,25),(11,26),(18,25),(19,24),(18,26),(15,26)]: c.set(x,y,cloth)
c.set(12,24,light).set(19,26,shade)
# ears, head
c.rect(9,8,14,4,ink)
c.rect(10,9,12,2,skin)
c.poly([(11,6),(20,6),(21,8),(21,12),(19,15),(12,15),(10,12),(10,8)],ink)
c.poly([(12,7),(19,7),(20,9),(20,12),(18,14),(13,14),(11,12),(11,9)],skin)
c.rect(12,8,7,3,skinlight)
c.line(12,12,13,13,skinshade).line(18,13,19,12,skinshade)
# facial features
c.set(12,10,ink).set(18,10,ink)
c.set(15,11,skinshade).set(16,11,skinlight)
c.line(14,13,17,13,ink).line(15,14,16,14,skinlight)
# tall chef toque with stepped lobes
c.poly([(9,6),(7,4),(8,2),(11,1),(13,2),(14,0),(18,0),(19,2),(22,2),(24,4),(23,6),(21,7),(21,9),(10,9),(10,7)],ink)
c.poly([(9,5),(8,4),(9,3),(12,2),(14,3),(15,1),(17,1),(19,3),(21,3),(23,4),(22,6),(20,6),(20,8),(11,8),(11,6)],cloth)
c.line(10,3,12,3,light).rect(15,2,3,3,light).line(20,4,21,4,light)
c.line(11,7,20,7,shade).line(12,6,19,6,light)
# bamboo steamer: dark rim separating the buns and hands
c.ellipse(15,20,9,3,ink)
c.rect(7,20,17,4,ink)
c.rect(8,20,15,3,wood)
c.ellipse(15,19,8,3,woodshade)
c.ellipse(15,19,7,2,'#64452f')
# three steamed buns with folded tops
for x,y in [(11,18),(19,18),(15,17)]:
 c.poly([(x-3,y),(x-2,y-2),(x-1,y-3),(x+1,y-3),(x+2,y-2),(x+3,y),(x+2,y+1),(x-2,y+1)],woodshade)
 c.poly([(x-2,y),(x-2,y-1),(x-1,y-2),(x+1,y-2),(x+2,y-1),(x+2,y),(x+1,y+1),(x-1,y+1)],cloth)
 c.line(x-1,y-1,x+1,y-1,light)
 c.set(x,y-2,'#c7b69b')
# front rim and woven vertical bamboo bands
c.line(8,20,22,20,woodlight)
c.line(8,23,22,23,woodshade)
c.line(9,22,21,22,woodlight)
for x in [10,14,18,21]: c.set(x,21,woodshade)
# hands at sides of the steamer with clear outline and cuffs
c.rect(5,19,3,4,ink).rect(24,19,3,4,ink)
c.rect(5,19,2,2,cloth).rect(25,19,2,2,shade)
c.poly([(7,19),(9,19),(9,21),(8,23),(6,22),(6,20)],ink)
c.poly([(23,19),(25,20),(25,22),(23,23),(22,21),(22,19)],ink)
c.rect(7,20,2,2,skinlight).set(7,22,skinshade)
c.rect(23,20,2,2,skinlight).set(24,22,skinshade)
view(result,scale=12)
finish(result)
