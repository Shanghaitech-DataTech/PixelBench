result = new_canvas(32,32)
c=result
ink='#332b35'; white='#fff2d5'; shade='#c9c8bb'; skin='#e9ac79'; light='#ffd3a0'; dark='#a76048'; coat='#ede4cb'; blue='#63858a'; apron='#9eb8ad'
# shoes and trousers
c.rect(10,26,5,4,ink); c.rect(17,26,5,4,ink)
c.rect(10,27,4,2,'#52616c'); c.rect(18,27,3,2,'#52616c')
c.rect(8,29,7,2,ink); c.rect(17,29,7,2,ink)
c.line(9,29,12,29,'#7b8385'); c.line(18,29,21,29,'#7b8385')
# body and sleeves
c.poly([(10,13),(21,13),(25,16),(26,22),(23,25),(22,28),(9,28),(8,25),(5,22),(6,16)],ink)
c.poly([(10,14),(21,14),(24,17),(24,22),(21,25),(10,25),(7,22),(7,17)],coat)
c.line(8,17,7,21,shade); c.line(23,17,24,21,shade)
# apron straps and skirt
c.rect(11,14,2,7,blue); c.rect(19,14,2,7,blue)
c.poly([(12,17),(19,17),(21,22),(22,27),(9,27),(10,22)],blue)
c.poly([(13,18),(18,18),(20,24),(20,27),(10,27),(11,23)],apron)
c.line(11,26,19,26,'#bfd0bb')
# flour on exposed apron
for x,y in [(12,24),(13,25),(16,24),(17,25),(18,24),(11,26)]: c.set(x,y,white)
c.set(12,25,'#dbe1cd')
# neck and head
c.rect(13,11,6,5,ink); c.rect(14,12,4,3,skin)
c.rect(9,7,14,5,ink); c.rect(10,8,12,4,skin)
c.rect(11,6,10,8,ink); c.rect(12,6,8,7,skin)
c.rect(12,7,7,4,light)
c.set(10,9,light); c.set(21,9,light)
# facial features
c.set(13,9,ink); c.set(18,9,ink)
c.set(16,10,skin); c.line(14,12,17,12,dark)
c.set(12,11,'#d78a69'); c.set(19,11,'#d78a69')
# tall chef toque
c.poly([(10,7),(9,5),(8,5),(8,2),(10,1),(13,1),(14,0),(18,0),(19,1),(22,1),(23,3),(22,6),(21,8)],ink)
c.rect(10,2,12,3,white); c.rect(9,3,13,2,white); c.rect(14,1,4,4,white)
c.line(11,4,11,6,shade); c.line(20,4,20,6,shade)
c.rect(11,6,10,2,ink); c.rect(12,6,8,1,white); c.line(12,7,19,7,shade)
# bamboo steamer dark silhouette
c.ellipse(16,20,10,3,ink)
c.rect(6,20,21,4,ink)
c.ellipse(16,23,10,2,ink)
c.rect(7,20,19,3,'#b47741')
c.ellipse(16,23,9,1,'#c58c4b')
c.ellipse(16,19,9,3,'#e8b76a')
c.ellipse(16,19,7,2,'#805334')
# three distinct buns
for x,y in [(11,18),(16,17),(21,18)]:
 c.ellipse(x,y,3,2,ink)
 c.ellipse(x,y,2,2,white)
 c.line(x-1,y+1,x+1,y+1,'#d7c7a5')
 c.set(x,y-1,'#c39d77')
# front rim and bamboo slats
c.line(8,21,24,21,'#f1c77c')
c.line(8,22,24,22,'#c18a49')
for x in [10,14,18,22]: c.line(x,22,x,23,'#8f603a')
c.line(10,24,22,24,'#e4ae61')
# hands outside basket, with cuffs
c.rect(5,19,3,3,ink); c.rect(24,19,3,3,ink)
c.rect(5,19,2,2,white); c.rect(25,19,2,2,white)
c.rect(5,21,4,3,ink); c.rect(24,21,4,3,ink)
c.rect(6,21,3,2,skin); c.rect(24,21,3,2,skin)
c.set(7,21,light); c.set(25,21,light)
view(result)
finish(result)
