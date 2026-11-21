result = new_canvas(32,32,name='dim_sum_chef')
c=result
O='#302b35'; W='#fff1d5'; G='#bbbdb5'; S='#e7a16d'; H='#ffd09a'; D='#ac614a'; A='#607f82'; B='#d7a359'; L='#f1c67a'; R='#986238'
# shoes and trousers
c.rect(10,26,5,4,O);c.rect(18,26,5,4,O)
c.rect(9,29,6,2,O);c.rect(18,29,6,2,O)
c.rect(11,27,3,2,'#697079');c.rect(19,27,3,2,'#697079')
# chef jacket silhouette, sleeves
c.poly([(10,13),(21,13),(25,16),(26,21),(23,24),(21,28),(10,28),(8,24),(5,21),(6,16)],O)
c.poly([(10,14),(21,14),(24,17),(24,21),(21,23),(10,23),(7,21),(7,17)],W)
c.rect(7,18,3,3,G);c.rect(22,18,3,3,G)
# apron straps and skirt
c.rect(11,14,2,5,A);c.rect(19,14,2,5,A)
c.poly([(12,17),(19,17),(21,26),(20,28),(11,28),(10,26)],A)
c.line(12,18,12,25,'#91a7a2');c.line(11,27,20,27,'#3e606a')
# flour dust on apron, deliberately visible beneath basket
for x,y in [(12,24),(13,25),(15,26),(18,25),(19,26),(12,26)]: c.set(x,y,'#e3e4cf')
c.set(14,25,'#aebeb4')
# neck and ears
c.rect(13,11,6,4,O);c.rect(14,12,4,3,S)
c.rect(8,8,3,4,O);c.rect(9,9,2,2,S)
c.rect(21,8,3,4,O);c.rect(21,9,2,2,S)
# rounded face
c.poly([(11,5),(20,5),(22,7),(22,11),(19,14),(13,14),(10,11),(10,7)],O)
c.poly([(11,6),(20,6),(21,8),(21,11),(18,13),(13,13),(11,11)],S)
c.rect(12,7,8,4,H)
c.line(12,8,14,8,O);c.line(18,8,19,8,O)
c.set(13,9,O);c.set(19,9,O)
c.set(16,10,D);c.line(15,12,18,12,D)
c.set(12,11,'#e48b68');c.set(20,11,'#e48b68')
# toque silhouette and folds
c.poly([(10,6),(8,4),(9,2),(12,1),(14,2),(16,0),(19,1),(20,2),(23,2),(24,4),(22,6),(22,7),(10,7)],O)
c.poly([(10,5),(9,4),(10,2),(12,2),(14,3),(16,1),(18,2),(19,4),(21,3),(23,3),(23,4),(21,6),(11,6)],W)
c.line(13,3,13,5,G);c.line(18,4,18,5,G)
c.rect(11,6,10,2,W);c.line(11,7,20,7,G)
# steamer rear rim
c.ellipse(16,19,9,3,O)
c.ellipse(16,19,8,2,R)
# individual buns above the rim, dark borders separate food from bamboo
for x,y in [(12,17),(19,17),(16,19)]:
 c.ellipse(x,y,3,2,O)
 c.ellipse(x,y,2,2,W)
 c.set(x,y-1,'#d9ba87');c.set(x-1,y,'#ead4a6');c.set(x+1,y-1,'#ffffff')
# basket front with thick raised rim and woven side
c.poly([(7,20),(10,21),(22,21),(25,20),(24,24),(21,25),(11,25),(8,24)],O)
c.poly([(8,21),(11,22),(21,22),(24,21),(23,24),(10,24)],B)
c.line(10,24,22,24,R)
for x in [11,14,18,21]: c.set(x,23,R)
c.line(9,21,11,22,L);c.line(11,22,21,22,L);c.line(21,22,23,21,L)
# hands wrap around outer edges; outlines keep them distinct
c.rect(5,20,4,4,O);c.rect(24,20,3,4,O)
c.rect(6,20,2,3,H);c.set(8,21,S);c.set(7,23,D)
c.rect(24,20,2,3,H);c.set(23,21,S);c.set(24,23,D)
view(c)
finish(result)
