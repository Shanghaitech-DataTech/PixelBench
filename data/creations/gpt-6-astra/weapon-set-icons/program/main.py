result = new_canvas(64,64,name='weapon_set')
c=result
ink='#182034'
shadow='#35465b'
steel='#718b9c'
light='#b7d2d6'
white='#edf4dd'
gold='#dca552'
ghi='#f5d481'
gdark='#865334'
wood='#a0653d'
wdark='#593b34'
leather='#704039'
red='#b95548'
# Sword: pointed silver blade, brass crossguard, leather grip
c.poly([(16,2),(19,7),(18,20),(20,21),(20,23),(17,24),(18,28),(16,30),(13,29),(13,24),(10,23),(10,21),(13,20),(13,7)],ink)
c.poly([(16,4),(17,7),(17,19),(14,19),(14,8)],steel)
c.line(15,6,15,19,white)
c.line(16,7,16,19,light)
c.line(17,7,17,18,steel)
c.rect(11,21,9,2,gdark)
c.line(11,21,19,21,gold)
c.set(11,20,ghi);c.set(19,20,ghi)
c.rect(14,22,3,2,gold);c.set(15,22,ghi)
c.rect(14,24,3,4,leather)
c.set(14,24,red);c.set(15,26,gold);c.set(16,25,gold)
c.rect(14,28,3,1,gold);c.set(15,29,gdark)
# Bow: crescent wood limbs, taut string, nocked arrow
c.line(54,5,54,27,ink)
c.line(53,7,53,25,light)
c.poly([(44,3),(48,4),(51,7),(53,11),(53,21),(51,25),(48,28),(44,29),(43,27),(47,25),(49,21),(50,17),(49,11),(47,7),(43,5)],ink)
c.poly([(44,4),(48,5),(50,8),(52,12),(52,20),(50,24),(48,27),(44,28),(44,27),(47,25),(49,22),(50,18),(50,13),(48,8),(46,6),(44,5)],wood)
c.line(45,5,47,6,ghi);c.line(48,7,50,11,gold)
c.line(51,12,51,15,gold);c.line(50,21,48,25,gold)
c.set(46,27,gold)
c.rect(50,14,3,6,ink);c.rect(50,15,2,4,leather)
c.line(50,15,51,16,gold);c.line(50,18,51,19,gold)
# arrow points left
c.line(38,16,59,16,ink)
c.line(39,15,59,15,gold)
c.poly([(35,16),(40,12),(40,14),(43,14),(43,17),(40,17),(40,19)],ink)
c.poly([(36,16),(39,13),(39,15),(41,15),(41,16)],light)
c.line(38,16,40,16,steel)
c.poly([(56,14),(58,12),(60,12),(59,15),(60,18),(58,18),(56,16)],ink)
c.line(57,14,59,13,red);c.line(57,16,59,17,red)
# shield silhouette and metal rim
c.poly([(5,37),(11,35),(17,34),(23,36),(27,38),(26,49),(23,55),(16,61),(9,56),(6,50)],ink)
c.poly([(7,38),(16,36),(25,39),(24,49),(21,54),(16,58),(11,54),(8,49)],steel)
c.line(7,38,16,36,white);c.line(8,39,9,48,light)
c.line(16,36,25,39,light)
c.line(10,53,16,58,light)
c.poly([(10,40),(16,38),(23,40),(22,48),(20,52),(16,56),(12,52),(10,48)],ink)
c.poly([(11,41),(16,39),(22,41),(21,48),(19,52),(16,54),(13,51),(11,47)],'#36566b')
c.poly([(11,41),(16,39),(16,54),(13,51),(11,47)],'#497a8b')
# heraldic gold chevron and boss
c.poly([(12,44),(16,41),(20,44),(20,47),(16,44),(12,47)],gold)
c.line(12,44,16,41,ghi)
c.poly([(16,46),(18,48),(16,51),(14,48)],ink)
c.poly([(16,47),(17,48),(16,50),(15,48)],gold);c.set(16,47,ghi)
for x,y in [(8,39),(24,40),(9,49),(23,49),(16,57)]:
 c.set(x,y,white)
# Battle axe: tall wood haft and a double steel head
c.poly([(47,35),(51,35),(51,55),(53,57),(52,60),(48,61),(46,58),(47,55)],ink)
c.rect(48,36,2,20,wood);c.line(48,37,48,54,gold)
c.rect(47,54,4,5,leather)
c.line(47,54,50,55,gdark);c.line(47,56,50,57,gold)
c.rect(48,59,3,1,gold)
# blades, sculpted concave inner sides
c.poly([(38,35),(42,38),(47,39),(51,39),(55,37),(59,35),(58,40),(57,44),(59,48),(55,48),(51,45),(47,45),(43,48),(38,49),(40,44),(40,40)],ink)
c.poly([(39,37),(43,40),(47,40),(47,44),(43,46),(40,47),(42,43),(41,40)],steel)
c.poly([(39,37),(41,39),(43,42),(42,45),(40,47),(42,43),(41,40)],light)
c.line(40,38,41,40,white);c.line(40,47,43,46,white)
c.poly([(51,40),(55,39),(58,37),(56,42),(56,44),(57,46),(55,46),(51,44)],steel)
c.poly([(58,37),(56,42),(56,44),(57,46),(55,46),(54,43),(55,40)],light)
c.set(57,38,white);c.line(56,45,57,46,white)
# central socket
c.rect(47,38,5,9,ink)
c.rect(48,39,3,7,gdark);c.line(48,39,48,45,gold)
c.rect(48,40,3,2,gold);c.set(49,40,ghi)
c.rect(48,44,3,1,gold)
view(result)
finish(result)
