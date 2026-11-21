result = new_canvas(64,64,name='weapon_set')
c=result
ink='#202334'
shadow='#465369'
steel='#8099ab'
light='#c4e0df'
white='#eff6dd'
wood='#965438'
woodlight='#cc8750'
gold='#e5b65e'
darkgold='#976339'
red='#984b51'
# sword: upper left, diagonal point
c.poly([(7,22),(9,19),(9,17),(22,4),(27,3),(26,8),(13,21),(11,21),(9,24)],ink)
c.poly([(10,18),(23,5),(25,5),(24,8),(12,20)],steel)
c.line(11,18,24,5,light)
c.line(12,19,24,7,shadow)
c.set(24,5,white)
# leather handle
c.line(5,27,11,21,ink)
c.line(6,28,12,22,ink)
c.line(4,26,10,20,ink)
c.line(5,26,10,21,wood)
c.line(6,26,10,22,woodlight)
c.set(7,24,ink)
c.set(9,22,ink)
# guard
c.poly([(7,17),(9,17),(15,23),(15,25),(13,25),(6,18)],ink)
c.line(8,18,14,24,gold)
c.line(8,19,13,24,darkgold)
c.rect(3,26,4,4,ink)
c.rect(4,27,2,2,gold)
c.set(4,27,white)
# bow upper right: bowed stave left and taut string right
c.line(52,4,55,27,shadow)
c.line(53,6,55,25,light)
c.poly([(51,3),(54,4),(53,7),(49,9),(46,12),(45,16),(47,20),(51,23),(56,25),(56,28),(53,28),(52,26),(47,24),(43,20),(42,16),(43,11),(47,7),(50,6)],ink)
c.poly([(51,5),(52,5),(50,8),(47,10),(45,13),(44,16),(46,20),(49,23),(54,25),(54,26),(49,24),(45,21),(43,17),(44,12),(48,8)],wood)
c.path('M 50 7 L 46 10 L 44 14 L 44 17 L 46 20 L 50 23',woodlight,fill=False)
c.rect(42,13,4,6,ink)
c.rect(43,13,2,6,darkgold)
for y in (13,15,17): c.set(43,y,gold)
# arrow pointing right
c.line(39,16,58,16,ink)
c.line(39,15,58,15,woodlight)
c.poly([(57,12),(61,15),(57,19)],ink)
c.poly([(58,14),(60,15),(58,17)],light)
c.poly([(39,12),(43,14),(43,15),(40,15),(38,13)],ink)
c.line(40,13,42,14,red)
c.line(39,18,42,16,ink)
c.set(40,17,red)
# shield lower left
c.poly([(5,38),(10,36),(16,34),(22,36),(27,38),(26,49),(23,55),(16,61),(9,55),(6,49)],ink)
c.poly([(7,39),(16,36),(25,39),(24,49),(21,54),(16,58),(11,54),(8,49)],steel)
c.poly([(7,39),(16,36),(16,39),(10,41),(11,50),(16,55),(16,58),(10,53),(8,48)],light)
c.poly([(16,39),(23,41),(22,49),(20,53),(16,56),(12,52),(10,48),(9,41)],ink)
c.poly([(11,42),(16,40),(21,42),(20,49),(16,53),(13,50)],red)
c.poly([(16,40),(21,42),(20,49),(16,53)],'#6b3647')
c.line(16,42,16,51,gold)
c.line(13,45,19,45,gold)
c.set(16,43,white)
for x,y in [(8,40),(24,40),(9,49),(23,49),(16,57)]: c.set(x,y,white)
# battle axe lower right handle diagonal
c.poly([(39,57),(54,37),(57,39),(43,60),(40,61),(38,59)],ink)
c.line(41,58,55,39,wood)
c.line(42,57,55,40,woodlight)
# grip lower end
for x,y in [(41,56),(43,53),(45,50)]:
 c.line(x,y,x+2,y+1,ink)
 c.set(x+1,y,woodlight)
c.rect(38,58,4,3,ink)
c.rect(39,58,2,2,gold)
# axe blade broad crescent, right-facing opposing cutting lobes
c.poly([(45,34),(48,38),(51,39),(54,36),(55,33),(58,35),(61,40),(61,45),(59,49),(55,49),(54,45),(51,43),(48,44),(45,47),(41,46),(38,43),(37,39),(39,35),(41,34),(41,38),(43,39),(45,38)],ink)
c.poly([(39,38),(40,36),(40,39),(43,41),(47,40),(49,41),(46,44),(44,45),(41,44),(39,41)],steel)
c.poly([(55,36),(56,35),(59,40),(60,44),(58,47),(56,47),(56,44),(53,42),(52,41)],steel)
c.poly([(39,38),(40,41),(42,43),(45,44),(44,45),(41,44),(39,41)],light)
c.poly([(57,37),(59,40),(60,44),(58,47),(56,47),(57,45),(58,43),(58,40)],light)
c.line(40,41,41,42,white)
c.line(59,41,59,44,white)
# central socket
c.poly([(50,37),(53,38),(54,40),(50,46),(47,44),(47,42)],ink)
c.line(51,39,48,43,darkgold)
c.line(52,39,49,44,gold)
c.set(51,40,white)
view(result)
finish(result)
