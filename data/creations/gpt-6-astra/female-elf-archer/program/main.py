# 64px woodland elf archer
result = new_canvas(64,64,background='#182b30',name='elf_archer')
c=result
ink='#14232a'; deep='#20483b'; dark='#2c6246'; green='#40845a'; mid='#65a463'; light='#91c777'; pale='#c3e49b'
skin='#edbd8b'; skinlight='#ffe0ac'; shade='#bc7e68'; skindark='#87594f'
wood='#955f41'; gold='#cba263'; bright='#f3d598'; metal='#b4d2bf'
# discreet woodland backdrop
c.poly([(3,0),(10,0),(9,44),(5,54),(2,54)],'#1d3538')
c.poly([(53,0),(58,0),(57,48),(53,50)],'#1d3538')
c.line(8,17,19,6,'#1d3538');c.line(54,25,44,13,'#1d3538')
c.ellipse(32,59,21,3,'#12242a');c.ellipse(32,59,15,2,'#203b38')
# bow behind right shoulder: bent stave with taut string
c.path('M 45 8 Q 58 24 49 43',ink,fill=False)
c.path('M 46 8 Q 59 25 50 43',gold,fill=False)
c.path('M 47 9 Q 60 25 51 42',wood,fill=False)
c.line(45,8,49,43,'#a5ae88');c.rect(54,23,2,6,ink);c.rect(54,24,1,4,wood)
# arrows and fletching above left shoulder
for x,y in [(17,11),(21,8),(24,12)]:
    c.line(x,y,x+6,33,ink);c.line(x+1,y,x+7,33,gold)
    c.poly([(x-2,y-3),(x+1,y-1),(x+2,y+5),(x-1,y+2)],metal)
    c.line(x,y-2,x+2,y+4,'#638d87')
# leather quiver
c.poly([(15,23),(23,21),(32,42),(25,45),(22,42)],ink)
c.poly([(17,25),(23,24),(29,41),(25,42)],wood)
c.line(18,27,24,40,'#bb8351');c.line(16,24,23,22,gold)
# hair silhouette, including floating locks
c.poly([(24,8),(29,4),(36,4),(42,7),(45,13),(44,23),(47,31),(48,38),(44,43),(38,40),(24,42),(19,38),(19,29),(21,20),(21,12)],ink)
c.poly([(25,9),(30,5),(36,5),(41,8),(43,13),(42,24),(46,35),(43,40),(38,37),(24,40),(21,37),(21,29),(23,20),(22,13)],dark)
c.poly([(26,10),(28,8),(28,23),(25,31),(25,37),(22,36),(23,27)],green)
c.poly([(39,16),(42,15),(41,25),(45,35),(42,38),(39,32)],green)
c.line(24,25,22,34,mid)
# legs back then front
c.poly([(32,39),(41,39),(40,47),(43,55),(42,59),(35,59),(35,54),(33,48)],ink)
c.poly([(34,41),(39,41),(38,48),(41,54),(36,55),(35,48)],'#668b65')
c.poly([(25,40),(34,41),(32,49),(30,57),(23,58),(24,49)],ink)
c.poly([(27,42),(32,43),(30,49),(28,54),(25,54),(26,48)],'#b1c58b')
c.line(27,44,26,51,pale)
# boots
c.poly([(24,51),(30,52),(30,57),(29,60),(20,60),(20,58),(23,56)],ink)
c.poly([(25,53),(29,53),(28,58),(22,58),(25,56)],wood)
c.line(24,52,29,53,gold);c.line(21,59,28,59,'#654e3d')
c.poly([(35,52),(41,51),(42,57),(45,59),(44,60),(35,60)],ink)
c.poly([(36,54),(40,53),(40,57),(43,58),(36,58)],wood)
c.line(36,52,40,52,gold)
# torso and tunic, asymmetrical hem
c.poly([(27,23),(34,22),(40,25),(41,32),(39,35),(42,43),(35,44),(31,42),(26,45),(22,42),(25,33),(23,28)],ink)
c.poly([(28,24),(34,24),(38,26),(39,31),(36,35),(40,41),(35,42),(30,40),(26,43),(24,41),(27,33),(25,28)],light)
c.poly([(35,26),(38,27),(38,32),(35,35),(38,41),(34,40),(32,33)],green)
c.poly([(27,27),(30,27),(32,32),(27,32)],pale)
c.line(27,36,25,40,pale);c.line(30,36,29,39,mid)
# far arm at hip
c.poly([(39,26),(42,27),(46,35),(44,39),(40,39),(38,35)],ink)
c.poly([(40,28),(41,28),(44,34),(42,36),(40,34)],skin)
c.poly([(40,27),(42,28),(43,31),(39,33),(38,29)],mid)
c.line(40,28,41,29,pale)
c.poly([(43,34),(45,35),(43,38),(40,37)],wood)
c.rect(40,35,2,3,skinlight)
# near hanging arm
c.poly([(25,26),(28,29),(25,35),(24,40),(21,42),(19,40),(20,36),(20,31),(22,27)],ink)
c.poly([(22,30),(25,31),(23,36),(21,37),(21,33)],skin)
c.poly([(23,26),(26,27),(27,30),(24,33),(20,31)],light)
c.line(23,27,25,28,pale)
c.poly([(21,35),(24,36),(23,39),(20,39)],wood)
c.line(21,35,23,36,gold)
c.poly([(20,39),(23,39),(22,41),(20,40)],skinlight)
# belt and diagonal quiver strap
c.line(26,33,37,34,ink);c.line(26,34,37,35,wood)
c.rect(30,33,4,3,gold);c.rect(31,34,2,1,ink)
c.line(27,24,36,33,'#624a36');c.line(28,24,37,33,gold)
# neck
c.poly([(30,20),(37,20),(35,25),(32,27),(29,24)],ink)
c.poly([(31,21),(36,21),(34,25),(32,25),(30,24)],skin)
c.line(32,22,35,22,shade)
# head in three-quarter view, looking right
c.poly([(28,10),(35,8),(40,12),(40,16),(42,18),(39,19),(38,22),(34,24),(29,21),(26,17)],ink)
c.poly([(29,11),(35,10),(39,13),(39,17),(41,18),(38,19),(37,21),(34,22),(30,20),(28,17)],skin)
c.poly([(33,11),(36,11),(38,13),(38,18),(36,20),(33,20),(31,17)],skinlight)
c.line(30,18,32,21,shade)
# pointed ear extending to left
c.poly([(28,14),(19,11),(22,17),(27,19),(29,17)],ink)
c.poly([(27,15),(21,13),(24,17),(27,18)],skin)
c.line(23,14,26,16,shade)
c.set(27,18,gold);c.set(27,19,bright)
# swept crown and long front lock
c.poly([(23,13),(24,9),(29,5),(36,6),(40,9),(41,13),(37,13),(33,10),(30,13),(29,17),(30,25),(27,30),(25,29),(26,23),(25,19),(26,14)],dark)
c.poly([(25,11),(28,8),(33,7),(36,8),(31,9),(28,13),(27,18),(28,24),(26,27),(27,21),(26,17)],green)
c.line(26,11,30,8,light);c.line(30,8,34,8,mid)
c.poly([(33,8),(36,8),(39,10),(40,12),(37,11)],mid)
c.line(28,15,27,20,mid)
# brows, eye and mouth
c.line(35,14,38,14,dark)
c.line(35,16,38,16,ink);c.set(36,16,'#f8edcb');c.set(37,16,'#416f54');c.set(38,16,ink)
c.set(32,16,skindark)
c.line(36,20,37,20,shade)
# forehead circlet and green jewel
c.line(29,11,32,10,gold);c.line(33,10,37,12,gold)
c.set(33,10,bright);c.set(34,11,'#dbeab4')
# leaf clasp at collar
c.poly([(29,25),(31,27),(30,29),(28,28)],dark);c.set(29,26,bright)
view(result)
save('female_elf_archer',result)
finish(result)
