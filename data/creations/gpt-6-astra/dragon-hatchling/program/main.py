result = new_canvas(64,64,name='dragon_hatchling')
c=result
ink='#202235'; dark='#343950'; shade='#38636b'; green='#528b85'; light='#79b49b'; hi='#a3ceb0'; memdark='#604c67'; mem='#93667b'; memlight='#bd8690'; bellydark='#aa947d'; belly='#d9c5a0'; cream='#f3e1b7'; horn='#ead8b7'; mouth='#452b43'; tongue='#c46b7f'
# rear wing, lifted and half unfurled
c.poly([(35,30),(39,20),(45,12),(51,9),(53,10),(52,17),(56,22),(59,30),(55,28),(51,28),(48,30),(44,27),(39,33)],ink)
c.poly([(39,28),(43,20),(50,12),(49,20),(54,23),(56,27),(51,25),(48,27),(44,25)],memdark)
c.poly([(43,22),(50,13),(48,21),(52,24),(48,25)],mem)
c.line(40,28,50,12,green);c.line(50,12,50,20,light);c.line(50,20,56,27,shade)
c.line(49,20,47,26,memlight)
# curled spiny tail behind body
c.path('M 39 43 Q 49 49 54 43 Q 58 39 56 35 L 59 31 Q 64 40 59 48 Q 53 57 40 52 L 34 48 Z',ink)
c.path('M 39 45 Q 51 51 56 43 L 58 37 Q 61 43 56 48 Q 49 54 40 50 Z',shade)
c.path('M 43 49 Q 55 53 59 41 Q 59 49 52 51 L 44 52 Z',green)
c.poly([(53,39),(54,34),(59,30),(59,36),(57,40)],ink)
c.poly([(55,36),(58,33),(57,38)],light)
c.poly([(58,46),(62,44),(61,49),(57,49)],ink)
c.poly([(59,46),(61,46),(59,48)],horn)
c.poly([(51,52),(55,51),(55,55),(52,54)],ink)
c.set(53,53,horn)
# rear leg
c.poly([(37,41),(44,43),(47,48),(45,52),(48,55),(47,58),(35,58),(33,54)],ink)
c.poly([(38,44),(43,45),(44,49),(41,53),(45,55),(36,55)],shade)
c.rect(36,55,9,2,green)
c.poly([(43,54),(46,56),(43,56)],horn)
# rounded body
c.path('M 27 27 Q 36 24 41 32 Q 47 40 43 48 Q 40 55 31 54 Q 22 52 21 44 L 22 33 Z',ink)
c.path('M 27 28 Q 35 26 39 32 Q 44 40 41 48 Q 36 53 30 51 Q 23 49 23 41 L 24 33 Z',green)
c.path('M 37 31 Q 46 42 40 49 Q 36 53 31 51 L 35 45 L 35 35 Z',shade)
# pale chest
c.path('M 24 30 Q 28 29 31 33 Q 36 37 35 45 L 32 50 Q 25 49 24 43 Q 22 36 24 30 Z',bellydark)
c.path('M 24 31 L 28 32 Q 31 36 32 42 L 30 48 Q 25 46 24 41 Z',belly)
c.line(25,35,29,36,cream);c.line(25,39,31,40,bellydark);c.line(26,44,31,45,bellydark)
# near half-spread wing: strong articulated outline
c.poly([(31,34),(24,30),(18,30),(13,33),(8,29),(2,32),(3,24),(6,15),(12,7),(15,6),(15,11),(20,17),(25,24),(32,29),(35,32)],ink)
c.poly([(4,28),(5,23),(8,16),(13,9),(11,20),(12,29),(8,26)],memdark)
c.poly([(5,25),(8,17),(12,12),(10,21),(9,26),(7,26)],mem)
c.poly([(13,12),(18,18),(23,25),(18,27),(14,29),(12,21)],memlight)
c.poly([(14,18),(18,22),(20,26),(15,28)],mem)
c.line(4,27,7,18,green);c.line(7,18,13,9,light)
c.line(13,9,11,21,light);c.line(11,21,13,30,memlight)
c.poly([(14,9),(16,14),(21,20),(25,25),(30,29),(33,31),(32,33),(26,28),(22,25),(19,20),(14,15)],shade)
c.line(15,13,21,20,green);c.line(24,23,30,29,light)
c.set(13,8,hi)
# neck and head silhouette with short muzzle and open growl
c.path('M 19 15 L 23 12 L 31 12 L 37 16 L 39 23 L 36 28 L 32 31 L 27 34 L 21 32 L 17 28 L 12 27 L 9 23 L 10 19 L 15 18 Z',ink)
c.path('M 20 16 L 24 14 L 30 14 L 35 17 L 36 23 L 33 28 L 28 31 L 23 30 L 19 26 L 13 25 L 11 22 L 12 20 L 17 20 Z',green)
c.poly([(22,16),(25,14),(30,15),(33,17),(29,18),(23,19),(19,22),(12,22),(12,20),(18,19)],light)
c.poly([(33,18),(36,20),(35,25),(31,29),(27,29),(29,24)],shade)
# horns rise beyond round skull
c.poly([(21,15),(18,11),(18,6),(20,7),(22,10),(26,13)],ink)
c.poly([(22,13),(20,10),(19,8),(20,12),(23,14)],horn)
c.poly([(29,13),(30,8),(33,5),(34,5),(33,11),(35,15)],ink)
c.poly([(31,12),(32,8),(33,7),(32,12),(33,14)],horn)
c.set(31,12,bellydark)
# cheek frill
c.poly([(35,22),(40,19),(39,24),(37,26),(40,26),(36,30),(32,30)],ink)
c.poly([(35,24),(38,22),(36,26),(37,27),(33,29)],green)
# open mouth dark cavity and lower jaw
c.poly([(11,24),(16,24),(20,23),(23,24),(22,28),(18,30),(13,29)],ink)
c.poly([(13,25),(19,25),(21,24),(21,27),(18,28),(14,27)],mouth)
c.line(16,27,19,27,tongue)
c.poly([(12,24),(15,25),(14,27)],cream)
c.poly([(19,24),(21,24),(20,26)],cream)
c.line(14,29,18,30,belly);c.line(18,30,22,28,light)
# eye and scowling brow
c.poly([(22,20),(25,19),(28,20),(27,23),(23,23)],ink)
c.line(23,20,26,20,'#f4c46b');c.line(23,21,26,21,'#e89a4d');c.set(25,20,ink);c.set(25,21,ink);c.set(23,20,cream)
c.line(21,18,25,18,light);c.line(25,18,29,20,light)
c.rect(13,21,2,1,ink);c.set(16,20,hi)
c.line(27,25,29,25,light)
# near forearm, bent and clawed
c.poly([(30,33),(34,34),(35,39),(32,43),(28,43),(26,40),(28,38)],ink)
c.poly([(30,35),(32,35),(33,38),(30,40),(28,40)],light)
c.line(31,40,33,39,shade)
c.set(28,41,horn);c.set(30,42,horn);c.set(32,41,horn)
# near haunch and planted foot
c.path('M 27 43 Q 33 40 36 45 L 36 50 L 33 54 L 34 57 L 31 59 L 21 59 L 18 57 L 19 54 L 24 52 Q 21 47 27 43 Z',ink)
c.path('M 28 44 Q 33 43 34 46 L 33 50 L 29 54 L 31 56 L 21 56 L 21 55 L 27 53 Q 24 47 28 44 Z',green)
c.path('M 29 45 L 32 45 L 33 48 L 29 51 L 26 51 L 26 47 Z',light)
c.line(22,57,30,57,shade)
for x in (20,24,28):
 c.poly([(x,55),(x+2,57),(x,57)],horn)
# deliberately sparse scale clusters
for x,y in [(36,32),(38,35),(38,40),(40,43),(35,47),(31,16),(29,46)]:
 c.line(x,y,x+1,y,light)
 c.set(x+1,y+1,shade)
c.set(24,16,hi);c.set(11,21,hi)
view(result)
finish(result)
