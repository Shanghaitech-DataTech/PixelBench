result = new_canvas(32,32,name='skeleton_grunt')
c=result
O='#25232d'; D='#4e4b50'; S='#8e8c7e'; B='#c6c5aa'; H='#eee8c9'; W='#fff4d7'
# Bent legs and heavily shaded articulations
c.poly([(12,20),(16,20),(17,24),(15,27),(15,29),(11,29),(11,27),(13,24)],O)
c.poly([(18,20),(21,20),(21,24),(23,27),(23,29),(19,29),(18,26),(18,24)],O)
c.line(14,22,15,24,B); c.set(14,23,H)
c.rect(13,25,2,2,S); c.line(12,27,12,28,H)
c.line(19,22,19,24,B); c.line(20,25,21,27,B); c.set(20,25,H)
c.rect(10,28,6,3,O); c.rect(10,29,5,1,B); c.set(11,28,H)
c.rect(19,28,6,3,O); c.rect(20,29,4,1,B); c.set(20,28,H)
# Recessed torso, forward leaning shoulders
c.poly([(11,11),(15,10),(20,12),(22,16),(20,20),(20,23),(16,24),(12,22),(12,19),(10,16)],O)
c.line(16,13,17,20,S); c.set(16,14,H); c.set(17,16,B); c.set(17,18,B)
# Collar and rib cage, open dark gaps
c.line(12,12,15,12,H); c.line(17,12,19,13,B)
c.line(12,14,15,15,B); c.set(12,14,H)
c.line(18,14,20,14,B); c.set(20,15,S)
c.line(12,16,15,17,B); c.set(12,16,H)
c.line(18,16,20,16,B)
c.line(13,18,16,19,B); c.line(18,18,19,18,S)
# Pelvic crest
c.line(13,20,15,21,H); c.line(18,21,20,20,B)
c.line(14,22,16,22,S); c.set(18,22,S)
# Sword arm, crooked elbow
c.poly([(10,12),(12,13),(11,16),(9,18),(7,17),(8,14)],O)
c.line(10,13,9,15,H); c.set(10,14,B)
c.set(8,16,S); c.line(7,17,6,15,B)
# Short sword raised diagonally outward
c.poly([(2,5),(5,7),(8,13),(6,15),(3,10)],O)
c.poly([(3,7),(4,8),(7,13),(6,13),(4,10)],'#9baeb1')
c.line(3,7,6,12,'#e0eeDF'); c.line(5,10,7,13,'#667f8a')
c.line(4,14,9,12,O); c.line(5,14,8,13,'#b2a075')
c.line(7,14,8,17,O); c.set(7,15,B); c.set(8,16,H)
# Shield-side upper arm visible at shoulder
c.poly([(20,12),(23,13),(25,17),(22,19),(20,16)],O)
c.line(21,13,23,15,B); c.set(21,13,H)
# Small round wooden shield, dark metal rim
c.poly([(24,15),(28,16),(30,19),(30,23),(28,26),(24,27),(21,25),(20,22),(21,18)],O)
c.poly([(24,16),(27,17),(29,19),(29,23),(27,25),(24,26),(22,24),(21,21),(22,18)],'#777b76')
c.poly([(24,17),(27,18),(28,20),(28,23),(26,25),(24,25),(22,23),(22,20)],'#855332')
c.line(23,19,23,23,'#bc8750'); c.line(24,18,24,24,'#ad7444')
c.line(25,18,25,25,'#553d2e'); c.line(26,19,26,24,'#a56c3d')
c.line(27,20,27,23,'#6a442c'); c.set(23,18,'#d29c5d')
c.rect(24,20,3,3,O); c.rect(24,20,2,2,'#adb0a0'); c.set(24,20,H); c.set(26,22,D)
c.set(24,16,'#b8bca7'); c.set(22,18,'#b8bca7'); c.set(28,24,D)
# Large lowered skull, neck disappearing behind the jaw
c.rect(13,10,3,3,O); c.set(14,11,S)
c.poly([(11,2),(16,2),(19,4),(20,7),(19,10),(17,12),(12,12),(10,10),(9,7),(9,4)],O)
c.poly([(11,3),(16,3),(18,4),(19,7),(18,10),(16,11),(12,11),(11,9),(10,7),(10,5)],B)
c.line(12,3,16,3,H); c.line(11,4,11,6,H); c.rect(12,4,5,2,H); c.set(12,4,W)
c.line(18,5,18,7,S); c.set(19,7,S)
# Eye sockets angled into a dour stare
c.rect(11,7,3,2,O); c.set(11,6,S); c.set(13,7,D)
c.rect(16,7,3,2,O); c.set(18,6,S); c.set(16,8,D)
c.set(15,9,O); c.set(14,9,S)
c.set(11,9,S); c.set(18,9,S)
# Jagged teeth and jaw
c.line(12,10,17,10,H); c.set(13,10,O); c.set(16,10,O)
c.line(13,11,16,11,B); c.set(14,11,H)
view(result,scale=12)
save('skeleton-grunt',result)
finish(result)
