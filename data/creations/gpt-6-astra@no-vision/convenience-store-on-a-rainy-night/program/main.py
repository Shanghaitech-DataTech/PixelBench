from pixelbench_api import *
import random
random.seed(17)
c = new_canvas(64,64, '#111b30', name='Rainy corner store')
# Night palette
ink='#111b30'; deep='#18273d'; wall='#30485b'; edge='#527080'; blue='#31536a'; wet='#233d53'; cyan='#63969d'; glint='#8dc4bd'
# Distant buildings and street
c.rect(0,9,8,36,'#17273a'); c.rect(2,5,5,5,'#17273a')
c.rect(1,15,3,8,'#2c3f51'); c.rect(0,29,5,2,'#30495a')
c.rect(61,6,3,40,'#203249')
c.rect(0,45,64,19,wet)
c.poly([(0,45),(62,42),(64,47),(0,51)],'#3b5361')
c.line(0,49,63,46,'#142b40')
c.line(0,50,63,47,'#4b6874')
# Building volume and roof
c.poly([(10,11),(57,11),(62,15),(62,45),(57,47),(10,46)],'#253b4d')
c.poly([(57,12),(62,16),(62,45),(57,46)],'#203345')
c.rect(9,10,49,3,'#496070'); c.line(9,10,57,10,'#769198')
c.rect(11,13,46,32,wall)
c.rect(8,13,51,1,'#121f32')
# Luminous fascia sign, in its metal casing
c.rect(11,14,46,10,'#18283a')
c.rect(12,14,44,9,'#bd9769')
c.rect(13,15,42,7,'#f7dd9c')
c.rect(14,16,4,5,'#d59762')
c.rect(51,16,3,5,'#d59762')
c.text(22,15,'OPEN','#5a665d',spacing=1)
c.line(13,23,56,23,'#6d6054')
# Awning: dark teal alternating panels with warm red tabs
c.poly([(10,24),(57,24),(60,28),(7,28)],'#4d7b7e')
for x in range(10,58,8):
    c.poly([(x,24),(x+3,24),(x+4,28),(x-1,28)],'#b66757')
c.rect(7,28,53,2,'#233c4b')
for x in range(8,59,8): c.rect(x,28,4,2,'#8e514c')
c.line(9,24,57,24,'#8caaa2')
# Recessed warm glazing
c.rect(11,30,29,15,'#152b39')
c.rect(13,30,25,12,'#f2bb71')
c.rect(14,30,23,3,'#ffe6a1')
c.rect(14,33,23,7,'#e6a467')
c.rect(14,40,23,2,'#b07851')
# Interior ceiling lamps
c.rect(16,31,7,1,'#fff2bf'); c.rect(28,31,7,1,'#fff2bf')
# Shelves and deliberately blocky merchandise
for y in [35,39]:
    for x,co,h in [(15,'#79937c',2),(18,'#d46e57',3),(21,'#fae1a0',2),(25,'#889c8c',3),(28,'#d16e57',2),(31,'#ffe4a4',3),(34,'#829481',2)]:
        c.rect(x,y-h,2,h,co)
    c.rect(14,y,23,1,'#956f54')
    c.line(14,y+1,37,y+1,'#f7cb86')
# Window mullions and sill
c.rect(24,30,2,13,'#3d5759'); c.line(24,31,24,41,'#8f9c84')
c.line(12,30,12,43,'#6c8985'); c.rect(12,42,27,2,'#4d686b')
c.line(13,42,37,42,'#bdbaa0')
c.line(15,31,15,32,'#fff2bf')
# Door and its glowing threshold
c.rect(40,30,13,16,'#162c39')
c.rect(42,30,9,14,'#e8b975')
c.rect(43,31,7,10,'#bba06e')
c.rect(44,31,6,3,'#fce2a1')
c.rect(44,35,6,6,'#907e5f')
c.rect(49,31,1,12,'#f8d693')
c.line(42,30,42,44,'#76928a')
c.rect(43,43,8,2,'#6e7967'); c.set(49,39,'#fef0b9')
c.rect(40,45,14,2,'#879084'); c.line(41,45,52,45,'#ead49a')
# Right-side masonry and small service panel
c.rect(54,31,3,9,'#3d5968'); c.rect(54,32,2,3,'#91a6a0')
c.set(54,33,'#e8d7a2'); c.rect(55,37,2,2,'#192e41')
c.line(58,30,58,43,'#54717d')
c.rect(10,44,29,2,'#223b4b')
# Wet pavement pools: long horizontal clusters of reflected light
c.poly([(14,47),(38,46),(35,50),(48,51),(51,55),(37,57),(13,55),(18,52),(9,51)],'#3d615f')
c.poly([(41,47),(52,47),(49,50),(53,52),(49,58),(41,58),(43,54),(39,51)],'#756f53')
for x,y,w,col in [(14,48,10,'#8e9471'),(28,48,8,'#bda66e'),(17,50,15,'#bc9c65'),(32,50,5,'#687e6a'),(28,52,12,'#e1b979'),(18,54,7,'#647e73'),(29,55,7,'#9d996e'),(38,56,7,'#7d8b75'),(43,48,7,'#e4bf7b'),(43,50,5,'#be9c62'),(44,53,8,'#c0a575'),(44,55,4,'#e0bd7c'),(42,58,7,'#808c78')]:
    c.rect(x,y,w,1,col)
# cool puddle contours
for x,y,w in [(1,58,10),(4,60,12),(21,61,13),(51,60,11),(53,55,9),(2,52,5),(31,59,7),(56,50,7)]:
    c.line(x,y,x+w-1,y,'#58838e')
    if y<60: c.line(x+2,y+1,x+w-2,y+1,'#345869')
c.line(5,57,14,57,'#86ada8'); c.line(23,62,29,62,'#6b9699')
# Umbrella rack beside entrance: visible hooked handles and gathered canopies
c.line(54,43,54,48,'#0e2132'); c.line(60,43,60,48,'#0e2132')
c.rect(54,44,7,4,'#192f40'); c.line(54,44,60,44,'#7d9c9f')
# furled umbrellas
c.line(55,39,55,46,'#96b7b4'); c.line(55,39,56,38,'#96b7b4'); c.set(57,39,'#96b7b4')
c.poly([(55,41),(54,46),(56,46)],'#b46e66')
c.line(59,38,59,46,'#708b99'); c.set(58,38,'#708b99')
c.poly([(59,40),(58,46),(60,46)],'#557f87')
c.line(54,48,60,48,'#4b6776')
# Bicycle silhouette, parked across left foreground
for cx in [7,24]:
    c.circle(cx,53,5,'#101f31',fill=False)
    c.circle(cx,53,4,'#637e8a',fill=False)
    c.set(cx,53,'#a0b4ad')
# spokes
for cx in [7,24]:
    c.line(cx-3,51,cx+3,55,'#385467'); c.line(cx-2,56,cx+2,50,'#385467')
# frame triangles
for p in [(7,53,12,46),(12,46,17,53),(17,53,7,53),(12,46,21,46),(21,46,17,53),(21,46,24,53)]: c.line(*p,'#b27765')
c.line(12,46,11,44,'#a8b5ae'); c.line(9,44,14,44,'#102334')
c.line(21,46,20,42,'#859d9e'); c.line(20,42,23,42,'#a8b5ae'); c.set(23,43,'#a8b5ae')
c.circle(17,53,1,'#183043'); c.line(17,53,19,55,'#9caaa4'); c.line(18,55,20,55,'#102334')
c.rect(3,46,7,1,'#536c79'); c.line(4,47,6,49,'#536c79')
# Person stepping into the open, lighted doorway, yellow raincoat
c.line(43,47,42,51,'#112538'); c.line(47,47,47,49,'#112538')
c.line(41,51,44,51,'#0c1d2e'); c.line(47,49,49,49,'#0c1d2e')
c.poly([(43,39),(47,39),(48,43),(49,47),(41,47),(42,43)],'#cd913e')
c.poly([(43,40),(44,41),(43,46),(41,47),(42,42)],'#efb94f')
c.line(46,41,47,45,'#9c713b'); c.set(46,46,'#f7ca6b')
# reaching hand
c.line(47,41,49,39,'#e7af4c'); c.set(49,38,'#eed1a0')
# hood and face in profile
c.poly([(42,38),(42,36),(43,35),(46,35),(47,37),(47,40),(43,40)],'#eeb64d')
c.rect(45,37,2,3,'#62533d'); c.set(47,38,'#edc792')
c.line(43,36,45,36,'#ffda7b'); c.set(43,37,'#ffda7b')
c.line(42,40,44,41,'#ffe096')
# Wind-driven rain, with controlled contrast in front of the shop
for x,y,l in [(4,1,3),(16,3,3),(27,0,3),(38,4,3),(50,1,4),(61,0,3),(9,6,2),(32,6,2),(59,8,3),(2,19,3),(5,33,3),(2,40,2),(61,29,3),(61,37,3),(35,3,1),(22,8,1),(6,13,2),(0,10,2)]:
    c.line(x,y,x-1,y+l,'#426174')
for x,y,l in [(8,31,3),(30,29,2),(38,34,3),(58,19,3),(3,47,2),(32,44,3),(36,53,2),(58,52,2),(14,58,1),(54,58,2),(3,61,2)]:
    c.line(x,y,x-1,y+l,'#73969e')
# Dripping eaves and little rain ripples
for x,y in [(9,30),(19,30),(35,30),(58,30)]: c.set(x,y,'#acd1c3')
for x,y in [(33,57),(57,58),(7,60)]:
    c.line(x-2,y,x,y,'#7ca4a5'); c.set(x+2,y,'#7ca4a5')
c.set(41,53,'#8ab3ad'); c.set(50,57,'#9ab8a9')
# Consolidate related shades into a cohesive limited palette.
merges = {
'#17273a':'#18273d', '#203249':'#203345', '#2c3f51':'#30485b',
'#30495a':'#30485b', '#3b5361':'#4b6874', '#142b40':'#18273d',
'#253b4d':'#233d53', '#121f32':'#111b30', '#18283a':'#18273d',
'#6d6054':'#956f54', '#233c4b':'#233d53', '#152b39':'#18273d',
'#fae1a0':'#ffe4a4', '#79937c':'#829481', '#889c8c':'#829481',
'#d46e57':'#d16e57', '#f7cb86':'#f2bb71', '#3d5759':'#4d686b',
'#6c8985':'#76928a', '#162c39':'#18273d', '#fce2a1':'#ffe6a1',
'#f8d693':'#f7dd9c', '#6e7967':'#829481', '#3d5968':'#30485b',
'#91a6a0':'#96b7b4', '#e8d7a2':'#ead49a', '#192e41':'#18273d',
'#54717d':'#527080', '#223b4b':'#233d53', '#8e9471':'#9d996e',
'#687e6a':'#647e73', '#7d8b75':'#808c78', '#e4bf7b':'#e0bd7c',
'#c0a575':'#bda66e', '#86ada8':'#8ab3ad', '#0e2132':'#111b30',
'#192f40':'#18273d', '#7d9c9f':'#96b7b4', '#708b99':'#73969e',
'#4b6776':'#527080', '#101f31':'#111b30', '#a0b4ad':'#a8b5ae',
'#385467':'#345869', '#102334':'#111b30', '#859d9e':'#73969e',
'#183043':'#233d53', '#9caaa4':'#a8b5ae', '#536c79':'#527080',
'#112538':'#111b30', '#0c1d2e':'#111b30', '#e7af4c':'#eeb64d',
'#edc792':'#eed1a0', '#ffda7b':'#ffe096', '#acd1c3':'#96b7b4',
'#7ca4a5':'#73969e', '#9ab8a9':'#96b7b4'
}
remap = {c.color(a):c.color(b) for a,b in merges.items()}
for y in range(64):
    for x in range(64):
        p = c.get(x,y)
        if p in remap: c.set(x,y,remap[p])
print(c.stats_text())
print(c.matrix_text(region=(39,34,50,48)))
save('rainy_convenience_store',c)
finish(c)
