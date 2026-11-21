result = new_canvas(32,32,name='skeleton_grunt')
c=result
ink='#25232d'; shade='#676573'; bone='#cbc7ac'; light='#f1e8c9'; mid='#96958b'
# bent legs and separated feet
c.poly([(14,20),(17,21),(16,24),(14,26),(14,28),(11,29),(9,28),(11,26),(12,23)],ink)
c.line(14,22,13,25,bone); c.set(14,22,light); c.set(12,26,shade)
c.line(12,27,12,28,bone); c.line(10,29,14,29,ink); c.line(10,28,13,28,light)
c.poly([(18,20),(21,20),(22,23),(21,26),(23,28),(23,30),(18,30),(17,28),(18,25),(18,23)],ink)
c.line(20,22,20,24,bone); c.set(20,25,shade); c.line(19,26,20,28,bone)
c.line(19,29,22,29,bone); c.set(19,28,light)
# curved spine and rib silhouette
c.poly([(14,10),(19,10),(22,13),(22,18),(20,21),(15,22),(12,19),(12,14)],ink)
c.line(18,12,19,19,shade)
c.line(17,12,17,19,bone)
# ribs curve around dark chest
for y in [13,16]:
 c.line(13,y,15,y+1,bone); c.line(15,y+1,17,y+1,light)
 c.line(19,y+1,21,y,bone)
c.set(13,15,shade); c.set(14,18,bone); c.line(15,19,20,19,bone)
# pelvis
c.line(14,20,16,22,bone); c.line(16,22,19,22,bone); c.line(19,22,21,20,mid); c.set(17,21,ink)
# sword arm, lowered elbow
c.poly([(12,12),(14,13),(12,16),(10,18),(8,18),(7,16),(9,14),(10,12)],ink)
c.line(11,13,10,15,light); c.set(9,16,shade); c.line(9,17,7,16,bone)
# sword angled out to left, short broad steel blade
c.poly([(3,6),(6,8),(9,15),(7,16),(4,10)],ink)
c.poly([(4,8),(5,9),(8,14),(7,14)],'#a4b8bf')
c.line(4,8,6,12,'#e4eeea'); c.line(6,12,7,14,'#e4eeea')
c.line(5,16,10,14,ink); c.line(5,15,9,14,'#a18a54')
c.line(8,16,9,19,ink); c.set(8,17,bone); c.set(9,18,'#a18a54')
# shield arm behind shield
c.line(21,13,24,16,ink); c.set(22,14,bone)
# skull, forward of the torso
c.poly([(11,3),(17,2),(20,4),(21,8),(19,11),(17,12),(12,11),(10,9),(9,6)],ink)
c.poly([(11,4),(17,3),(19,4),(20,7),(18,10),(12,10),(10,8),(10,6)],bone)
c.line(12,4,17,4,light); c.line(11,5,11,6,light); c.line(12,3,16,3,light)
c.line(19,5,19,7,mid); c.set(18,9,shade)
# heavy eye sockets, nasal cavity and teeth
c.rect(11,7,3,2,ink); c.rect(16,6,3,2,ink); c.set(16,8,shade)
c.set(14,9,ink); c.set(15,9,ink)
c.line(12,10,17,10,light); c.set(13,10,shade); c.set(16,10,shade)
c.line(13,11,16,11,bone)
# round wooden buckler, outlined metal rim
c.poly([(24,13),(28,14),(30,17),(30,21),(28,24),(24,25),(21,23),(20,19),(21,15)],ink)
c.poly([(24,14),(27,15),(29,17),(29,21),(27,23),(24,24),(22,22),(21,19),(22,16)],mid)
c.poly([(24,15),(27,16),(28,18),(28,21),(26,23),(24,23),(22,21),(22,18)],'#805239')
c.line(24,16,24,22,'#bd8650'); c.line(25,16,25,23,'#533a30'); c.line(27,17,27,21,'#aa7043')
c.set(23,17,'#d29a5b'); c.set(23,21,'#51392e')
c.rect(24,18,3,3,ink); c.rect(24,18,2,2,'#b4b7ad'); c.set(24,18,'#e4ddbc'); c.set(26,20,shade)
c.set(24,14,light); c.set(22,16,bone); c.set(28,22,shade)
view(result)
finish(result)
