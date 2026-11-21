result = new_canvas(32,32,name='retro_film_camera')
c=result
O='#181a25'; DS='#30313a'; S='#555761'; M='#90999b'; L='#c5cdc6'; H='#eef0d6'; B='#473c3b'; BL='#655048'; BH='#886452'; BD='#302c32'
# stepped silhouette, top controls and prism
c.rect(5,7,6,4,O)
c.rect(6,7,4,2,M); c.rect(7,7,2,1,H)
c.rect(24,7,4,4,O); c.rect(25,7,2,2,'#ad7354'); c.set(25,7,'#e5b07a')
c.poly([(12,10),(14,5),(20,5),(23,10)],O)
c.poly([(14,9),(15,6),(19,6),(21,9)],M)
c.line(15,6,19,6,H); c.rect(15,8,5,2,DS); c.rect(16,8,3,1,'#557f88')
# camera body outline
c.rect(3,10,26,16,O); c.rect(2,12,28,12,O); c.rect(4,25,24,2,O)
# metal upper and lower housing
c.rect(4,11,24,5,M); c.rect(3,12,1,10,S)
c.line(5,11,26,11,H); c.rect(5,12,22,2,L)
c.rect(27,12,2,12,S)
c.rect(4,23,23,2,S); c.line(5,25,26,25,M); c.line(5,24,13,24,L)
# leather panels
c.rect(4,16,24,7,BD); c.rect(5,16,21,7,B)
c.rect(5,17,7,5,BL); c.rect(24,17,2,5,BL)
# restrained leather grain
for x,y in [(5,17),(8,17),(10,18),(6,19),(9,20),(5,21),(11,21),(25,18),(24,20),(26,22)]:
 c.set(x,y,BH)
for x,y in [(7,18),(9,18),(5,20),(7,21),(10,22),(24,18),(25,21)]:
 c.set(x,y,BD)
# finder and badge
c.rect(5,12,6,3,O); c.rect(6,12,4,2,'#36525f'); c.line(6,12,8,12,'#8cb7b8'); c.set(6,13,'#c6ded1')
c.rect(24,13,2,1,'#e0bd7e')
# circular lens assembly with offset dimensional shadow
c.ellipse(18,20,8,6,O)
c.circle(17,19,7,O)
c.circle(17,19,6,S)
c.path('M 12 18 L 12 16 L 14 14 L 19 14 L 22 17',L,fill=False)
c.path('M 13 23 L 15 25 L 19 25 L 22 22 L 23 19',DS,fill=False)
c.circle(17,19,5,O)
c.circle(17,19,4,'#46616b')
c.circle(17,19,3,'#223845')
c.poly([(17,16),(19,17),(20,20),(18,22),(15,21),(14,18)],'#172735')
c.poly([(14,18),(16,16),(18,16),(16,19),(14,20)],'#699a9e')
c.line(15,17,17,17,'#c1ded1'); c.set(14,18,'#8fc3be')
c.line(18,22,20,20,'#417c8b'); c.set(19,21,'#6aabb3')
# tiny physical details
c.set(12,19,H); c.set(17,13,H); c.set(22,16,M)
c.rect(6,23,3,1,DS); c.set(26,24,O)
view(result)
finish(result)
