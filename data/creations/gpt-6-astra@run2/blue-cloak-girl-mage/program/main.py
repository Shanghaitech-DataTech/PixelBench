result = new_canvas(64,64,name='blue_cloak_mage')
c=result
ink='#151a32'; deep='#202b50'; blue='#2c4175'; mid='#3c5990'; light='#5877aa'; edge='#7f9ac0'
skin='#efbe9f'; shade='#ce8d80'; pale='#ffdbc0'; hair='#b4b5d1'; hs='#777d9f'; hl='#e2dfeb'; gold='#db9b4e'; bright='#ffe4a0'
# staff glow, kept in a compact halo
c.poly([(48,5),(54,5),(58,10),(58,17),(54,21),(48,21),(44,17),(44,10)], '#ee9e3820')
c.poly([(49,7),(53,7),(56,11),(56,16),(53,19),(49,19),(46,16),(46,11)], '#ffc65a38')
# long staff and carved terminal
c.line(51,18,51,57,ink); c.line(50,18,50,57,'#815439'); c.line(49,19,49,56,gold)
c.set(50,57,gold); c.rect(49,51,3,2,'#e6b66c')
# cloak silhouette: open falling bell with broad hood
c.poly([(23,19),(34,19),(39,24),(40,32),(43,46),(39,49),(33,50),(21,49),(14,47),(17,34),(18,25)],ink)
c.poly([(20,26),(26,23),(34,23),(38,27),(38,35),(41,45),(37,47),(21,47),(16,45),(20,32)],deep)
# legs behind tunic
c.rect(24,43,6,9,ink); c.rect(31,43,6,9,ink)
c.rect(25,44,4,7,shade); c.rect(32,44,4,7,skin)
# white boots with dark border and asymmetrical relaxed toes
c.poly([(24,48),(29,48),(30,57),(29,60),(22,60),(21,58),(23,55)],ink)
c.poly([(31,48),(37,48),(37,55),(40,57),(40,60),(32,60),(31,58)],ink)
c.poly([(24,49),(28,49),(29,56),(27,58),(22,58),(24,55)],'#b7c5db')
c.rect(25,50,3,6,'#f4f2ed'); c.line(23,57,27,57,'#f4f2ed'); c.line(24,49,28,49,hl)
c.poly([(32,49),(36,49),(36,56),(39,57),(39,58),(33,58)],'#b7c5db')
c.rect(32,50,3,6,'#f4f2ed'); c.line(34,57,38,57,'#f4f2ed'); c.line(32,49,36,49,hl)
# simple ivory dress
c.poly([(25,27),(32,27),(34,36),(36,45),(32,47),(23,46),(22,44),(25,35)],ink)
c.poly([(26,28),(31,28),(32,36),(34,44),(30,45),(24,44),(26,35)],'#bac5da')
c.poly([(27,29),(30,29),(30,37),(32,44),(26,44)],'#e5e4e9')
# belt
c.rect(25,35,8,3,deep); c.rect(28,35,3,3,gold); c.set(29,36,bright)
# left hanging cloak panel and sleeve
c.poly([(21,25),(26,25),(24,32),(23,39),(20,45),(16,44),(19,35),(17,33)],blue)
c.poly([(20,27),(23,26),(21,34),(18,40),(18,35)],mid)
c.line(18,44,20,44,light); c.line(23,38,21,44,mid)
# relaxed left hand
c.poly([(19,35),(22,36),(22,40),(20,42),(18,40),(18,37)],ink)
c.poly([(19,36),(21,37),(21,40),(20,41),(19,39)],skin); c.set(19,37,pale)
# right cloak sweep, arm bent gently to staff
c.poly([(32,25),(36,25),(39,30),(44,30),(46,34),(42,37),(38,34),(40,44),(37,46),(34,45),(32,36)],blue)
c.poly([(34,26),(36,27),(39,32),(43,32),(43,34),(38,32),(36,31)],mid)
c.poly([(34,35),(36,37),(38,44),(36,45),(35,41)],mid)
c.line(34,28,33,33,light)
# gold piping on open cloak
c.line(25,27,23,34,gold); c.line(32,27,33,34,gold)
c.line(17,45,20,46,light); c.line(36,47,39,46,light)
# hand around staff
c.rect(45,30,6,5,ink); c.rect(45,31,5,3,skin); c.line(46,31,49,31,pale); c.set(49,33,shade); c.set(50,32,skin)
# back of hood
c.poly([(19,20),(18,15),(20,9),(24,6),(31,5),(36,8),(39,14),(38,21),(35,26),(23,26)],ink)
c.poly([(20,19),(20,13),(23,9),(28,7),(32,7),(36,11),(37,16),(36,22),(33,25),(24,24)],blue)
c.poly([(21,14),(24,10),(29,8),(33,9),(35,12),(28,10),(24,13),(22,18)],mid)
c.line(25,9,29,8,light)
# hair and face opening
c.poly([(23,13),(27,10),(32,11),(35,14),(35,22),(32,26),(24,24),(21,21),(21,16)],ink)
c.poly([(23,14),(27,12),(32,12),(34,15),(34,22),(32,25),(24,23),(22,21),(22,17)],hs)
# neck
c.rect(27,23,4,4,shade); c.rect(28,24,3,3,skin)
# face
c.poly([(24,15),(31,14),(34,17),(33,22),(30,25),(27,24),(24,21)],skin)
c.poly([(25,16),(31,15),(33,17),(32,21),(30,23),(27,22),(25,20)],pale)
# fringe in distinct anime locks
c.poly([(23,14),(26,12),(31,12),(34,15),(34,18),(31,16),(29,14),(28,18),(26,16),(24,19),(23,22),(22,20)],hair)
c.line(24,14,27,13,hl); c.line(29,13,31,14,hl)
c.line(23,18,23,22,hl)
c.poly([(33,17),(34,18),(34,23),(32,25),(32,22)],hair)
# front-facing eyes, violet blue
c.line(25,19,27,19,ink); c.line(30,19,32,19,ink)
c.set(26,20,'#50658e'); c.set(31,20,'#50658e'); c.set(25,20,'#faf4ed'); c.set(30,20,'#faf4ed')
c.set(29,23,'#a76470'); c.set(24,21,'#e9a294'); c.set(33,21,'#e9a294')
# collar folded over shoulders and amber clasp
c.poly([(22,23),(26,25),(28,28),(24,28),(21,25)],mid)
c.poly([(33,23),(31,25),(29,28),(34,27),(36,24)],mid)
c.line(22,24,25,26,light); c.line(34,24,32,26,light)
c.rect(27,27,4,3,ink); c.rect(28,27,2,3,gold); c.set(28,27,bright)
# crescent metal cradle atop the staff
c.poly([(46,12),(47,17),(50,20),(53,19),(56,15),(55,12),(54,16),(51,18),(49,17),(48,13)],ink)
c.line(47,13,48,17,gold); c.line(48,17,51,19,gold); c.line(51,19,54,16,gold); c.line(54,16,55,13,bright)
c.rect(49,20,3,2,gold); c.set(50,20,bright)
# glowing amber crystal
c.poly([(51,6),(54,11),(53,15),(50,17),(48,13),(49,9)],'#ad5a31')
c.poly([(51,7),(53,11),(52,15),(50,16),(49,12)],'#ffae42')
c.poly([(51,8),(52,11),(51,14),(50,12)],'#fff0b4')
c.set(50,9,'#fff9dd'); c.set(48,22,'#ffd16c')
# sparse floating sparks
c.set(45,8,'#ffc363'); c.set(57,10,'#ffe5a1'); c.set(55,21,'#e9a44f'); c.set(47,4,'#e7b765')
view(result)
finish(result)
