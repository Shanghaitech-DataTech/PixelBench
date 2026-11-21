result = new_canvas(32,32,name='skeleton_grunt')
c=result
O='#242332'; J='#48434a'; S='#827d73'; B='#c8c2a2'; H='#eee6c4'; W='#fff3d3'
# legs, offset to establish a bent, shambling stance
c.poly([(13,20),(17,20),(17,23),(14,25),(14,28),(16,29),(16,30),(10,30),(10,28),(11,24),(13,23)],O)
c.poly([(19,20),(22,20),(22,24),(24,26),(24,28),(27,28),(28,30),(21,30),(21,27),(19,25),(18,23)],O)
c.line(14,22,12,25,B); c.set(13,23,H)
c.rect(11,26,2,3,B); c.set(11,26,H); c.line(11,29,14,29,S)
c.rect(19,22,2,3,S); c.set(20,23,B)
c.line(21,25,23,27,B); c.set(22,26,H); c.line(22,29,26,29,B)
# sword behind left hand: angled short blade
c.poly([(2,11),(5,13),(10,21),(8,23),(3,16)],O)
c.poly([(3,13),(5,15),(9,21),(8,21),(4,16)],'#91a8b0')
c.line(3,13,7,19,'#d4e1d9'); c.line(5,17,8,21,'#667b91')
c.line(6,22,10,20,O); c.line(6,21,10,19,'#8a8170')
c.line(8,22,10,25,O); c.line(8,22,9,24,'#90634b')
# hunched torso silhouette, shoulders raised behind skull
c.poly([(15,11),(20,10),(23,12),(24,16),(22,19),(22,22),(19,24),(14,23),(12,20),(13,16),(11,15)],O)
c.line(19,12,21,13,B); c.set(22,14,S)
# shadowed spine and ribs
c.line(17,13,17,20,S)
c.line(14,13,16,14,H); c.line(18,14,20,13,B)
c.line(13,15,15,16,B); c.line(16,16,20,15,H)
c.line(14,18,16,19,B); c.line(17,18,20,17,B)
c.set(17,15,J); c.set(17,17,J); c.set(17,19,H)
# pelvis
c.line(14,20,16,21,S); c.line(17,21,20,20,H)
c.line(14,21,15,22,B); c.line(19,21,20,22,B)
# left dangling upper arm and crooked forearm
c.poly([(11,13),(14,13),(13,17),(11,20),(10,23),(7,23),(7,20),(9,18),(10,15)],O)
c.line(11,14,11,17,H); c.set(12,14,B)
c.set(10,18,J); c.line(10,19,9,21,B)
c.rect(8,21,2,2,H); c.set(9,23,S)
# skull pitched forward
c.poly([(12,3),(17,3),(20,5),(20,9),(18,12),(17,14),(12,14),(11,12),(9,11),(9,6)],O)
c.poly([(12,4),(17,4),(19,6),(19,9),(17,11),(17,13),(12,13),(12,11),(10,10),(10,6)],B)
c.line(12,4,16,4,H); c.line(11,5,17,5,H); c.rect(10,6,8,2,H)
c.set(11,6,W); c.line(18,6,18,9,S)
# deep sockets, asymmetrical brow and nasal opening
c.rect(10,8,3,3,O); c.set(10,8,J)
c.rect(15,8,3,3,O); c.set(17,10,S)
c.set(14,10,J); c.set(13,11,O)
c.line(12,12,16,12,H); c.set(13,12,J); c.set(15,12,J)
c.line(12,13,16,13,S); c.set(12,13,B); c.set(14,13,B); c.set(16,13,B)
# right arm partially visible around shield
c.line(22,13,24,15,O); c.set(22,13,H); c.set(23,14,B)
# compact wooden shield with iron edging
c.poly([(24,14),(28,15),(30,17),(29,23),(26,26),(22,24),(21,18)],O)
c.poly([(24,15),(28,16),(29,18),(28,23),(26,25),(23,23),(22,18)],'#777c78')
c.poly([(24,16),(27,17),(28,18),(27,23),(26,24),(24,22),(23,18)],'#9d6840')
c.line(24,17,25,22,'#ca9358'); c.line(26,17,27,22,'#b78049')
c.line(25,17,26,23,'#5e4233')
c.set(24,19,'#e0a564'); c.set(27,20,'#774a34')
c.line(23,16,22,18,'#bbc3af'); c.line(22,19,23,22,'#a5aa97')
c.set(26,24,'#b6baa4'); c.set(28,17,'#a5aa97')
# shield boss and rivets
c.rect(24,19,3,3,O); c.set(25,19,'#d0d2b5'); c.set(24,20,'#a5aa97'); c.set(25,20,'#878d85'); c.set(26,20,'#535b60'); c.set(25,21,'#535b60')
c.set(24,16,'#e0d9b6'); c.set(28,18,'#d0d2b5'); c.set(27,23,'#b6baa4')
view(result)
finish(result)
