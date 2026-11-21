result = new_canvas(32,32, name='forest_slime')
c=result
# Restrained woodland palette, with warm luminous eyes.
o='#172f2c'; dark='#234735'; shade='#326046'; green='#4b8050'; mid='#689a58'; light='#92b86c'; moss='#b3ca78'; gleam='#d5df93'
wood='#765b40'; wh='#b49861'; wd='#453e32'
# Tiny forked antlers, behind the soft body.
c.poly([(8,13),(7,8),(5,6),(5,3),(7,3),(7,5),(9,7),(9,2),(11,2),(11,8),(13,10),(12,14)],o)
c.line(8,11,8,8,wood).line(8,8,6,5,wood).line(6,4,6,5,wh)
c.line(10,3,10,8,wh).line(10,8,12,11,wood)
c.poly([(20,13),(20,10),(22,8),(22,2),(24,2),(24,6),(26,4),(26,3),(28,3),(28,6),(25,9),(24,13)],o)
c.line(22,11,23,8,wood).line(23,3,23,8,wh)
c.line(24,8,27,5,wood).set(27,4,wh)
# Mushroom on the right of its back, with a creamy little stem.
c.rect(23,8,3,8,o).rect(24,9,1,6,'#d5c69b').set(24,12,'#a69972')
c.poly([(20,8),(21,5),(23,4),(26,4),(28,6),(29,9),(28,10),(20,10)],o)
c.poly([(21,8),(22,6),(24,5),(26,5),(27,6),(28,8),(28,9),(21,9)],'#a73942')
c.line(22,6,26,6,'#df5960').line(21,8,28,8,'#c44749')
c.set(23,6,'#ffe0b4').set(26,7,'#ffe0b4').set(22,8,'#ffe0b4').set(27,8,'#edbc98')
c.line(22,10,27,10,'#794340')
# Rounded jelly silhouette: wide at its base, no stray single-pixel noise.
body=[(13,9),(18,9),(18,10),(21,10),(21,11),(23,11),(23,13),(25,13),(25,16),(27,16),(27,21),(28,21),(28,25),(27,25),(27,27),(24,27),(24,28),(19,28),(19,27),(13,27),(13,28),(8,28),(8,27),(5,27),(5,26),(3,26),(3,22),(4,22),(4,18),(5,18),(5,15),(7,15),(7,12),(10,12),(10,10),(13,10)]
c.poly(body,o)
c.poly([(13,10),(18,10),(18,11),(21,11),(21,12),(22,12),(22,14),(24,14),(24,17),(26,17),(26,22),(27,22),(27,25),(25,25),(25,26),(23,26),(23,27),(20,27),(20,26),(12,26),(12,27),(8,27),(8,26),(5,26),(5,25),(4,25),(4,22),(5,22),(5,18),(6,18),(6,15),(8,15),(8,13),(11,13),(11,11),(13,11)],green)
# Underside and rounded right flank.
c.poly([(24,16),(25,18),(25,23),(26,23),(26,25),(23,26),(20,26),(20,25),(11,25),(11,26),(7,26),(5,24),(7,24),(9,23),(22,23),(23,21)],shade)
c.line(10,26,12,26,dark).line(20,26,23,26,dark).set(26,24,dark)
# Moss carpet cascades down the forehead in little stepped clumps.
c.poly([(12,11),(18,11),(18,12),(21,12),(21,13),(22,13),(22,16),(20,16),(20,15),(18,15),(18,17),(16,17),(16,15),(13,15),(13,16),(10,16),(10,18),(8,18),(8,16),(7,16),(8,14),(11,14),(11,12)],mid)
c.line(13,11,17,11,light).line(11,12,14,12,light).line(9,14,11,14,light)
c.rect(14,12,4,2,light).rect(18,13,3,2,light)
c.line(12,11,14,11,moss).line(15,12,17,12,moss).set(19,13,moss)
c.set(10,15,moss).set(12,14,light).set(17,15,green).set(20,15,green)
# Small moss tufts and jelly highlight down the left side.
c.line(6,18,6,21,mid).set(7,17,light).set(5,22,mid)
c.line(8,24,10,24,mid).line(12,25,15,25,mid)
c.line(23,23,24,22,green)
# Dark sockets surround the gold-green luminous eyes.
c.rect(9,18,5,5,dark).rect(18,18,5,5,dark)
c.rect(10,18,3,1,o).rect(19,18,3,1,o)
c.rect(10,19,3,3,'#b7ce69').rect(19,19,3,3,'#b7ce69')
c.rect(10,19,2,2,'#f5ecab').rect(19,19,2,2,'#f5ecab')
c.set(10,19,'#fff6d1').set(19,19,'#fff6d1')
c.line(10,22,12,22,green).line(19,22,21,22,green)
# A tiny friendly, slightly mischievous mouth and warm cheeks.
c.set(15,22,o).set(17,22,o).set(16,23,o)
c.line(7,22,8,22,'#87945b').line(23,21,24,21,'#87945b')
# A couple of deliberate moss flecks, kept in clusters.
c.set(14,17,light).set(15,17,mid).set(22,15,mid)
print(c.stats_text())
print(c.matrix_text())
save('forest-slime-monster',result)
finish(result)
