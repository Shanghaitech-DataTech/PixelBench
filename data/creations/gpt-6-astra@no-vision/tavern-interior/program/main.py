# Cozy tavern interior, hand-placed pixel clusters.
c = new_canvas(64, 64, background='#211923', name='The Amber Lantern')
ink='#17131c'; deep='#2b1c25'; wall='#422831'; wooddark='#47282a'; wood='#714332'; mid='#925638'; goldwood='#b47545'; litwood='#d69a55'
# Back wall and timber ceiling
c.rect(1,1,62,38,wall)
c.poly([(1,1),(62,1),(53,8),(12,8)], '#30232b')
c.rect(0,0,64,3,ink)
c.line(4,3,13,9,'#614034'); c.line(59,3,52,9,'#614034')
c.rect(0,7,64,3,ink); c.rect(1,7,62,1,'#714532')
c.rect(0,3,4,35,ink); c.rect(1,3,2,34,'#674233')
c.rect(59,3,5,35,ink); c.rect(60,3,2,34,'#674233')
# Dim plaster blocks, sparse, grouped marks
for x,y,w in [(6,11,4),(30,10,7),(53,13,4),(7,31,5),(54,25,4)]:
    c.line(x,y,x+w,y,'#54333a')
# Warm pools on the wall behind the two lanterns
for x in [14,49]:
    c.ellipse(x,17,10,13,'#4d3030')
    c.ellipse(x,16,7,10,'#624031')
    c.ellipse(x,14,5,7,'#785135')
# Small blue nighttime window on the left
c.poly([(4,17),(5,14),(9,12),(12,14),(13,17),(13,30),(4,30)],ink)
c.poly([(6,17),(7,15),(9,14),(11,16),(11,28),(6,28)],'#26354b')
c.rect(7,19,4,8,'#32455a')
c.set(8,16,'#79909a'); c.set(10,22,'#607986')
c.line(8,15,8,28,wooddark); c.line(5,21,12,21,wooddark)
c.rect(3,29,11,2,ink); c.rect(4,29,9,1,'#805039')
# Recessed bottle cabinet
c.rect(19,10,27,21,ink)
c.rect(21,12,23,18,'#302329')
c.rect(22,13,21,8,'#38282b')
c.rect(22,23,21,7,'#3b282a')
c.rect(19,10,27,2,wooddark); c.line(20,10,44,10,'#97613d')
c.rect(19,12,2,18,'#65402f'); c.rect(44,12,2,19,'#65402f')
# Bottle silhouettes, bright single-pixel glass reflections
def bottle(x,y,base,hi,h=7):
    c.rect(x+1,y,2,2,ink)
    c.rect(x,y+2,4,h-2,ink)
    c.rect(x+1,y+1,1,2,hi)
    c.rect(x+1,y+3,2,h-4,base)
    c.set(x+1,y+3,hi)
    c.rect(x+1,y,2,1,'#c59860')
bottle(22,14,'#477367','#7ca88a',7)
bottle(28,13,'#9b583e','#dda75f',8)
bottle(34,15,'#687650','#a0ab6e',6)
bottle(39,13,'#446b68','#8baf92',8)
bottle(22,24,'#966240','#d39c59',6)
bottle(28,23,'#466e5d','#8caa74',7)
bottle(38,24,'#96504a','#d48c69',6)
# squat stoneware jug
c.rect(33,26,4,4,ink); c.rect(34,25,2,1,'#b18c67')
c.rect(34,26,2,3,'#b59a78'); c.set(34,26,'#dcc69b')
c.set(37,27,'#b59a78'); c.set(37,28,'#b59a78')
for y in [21,30]:
    c.rect(18,y,29,3,ink)
    c.rect(18,y,29,1,'#a86d42')
    c.rect(20,y+1,25,1,'#714331')
# Right wall small chalkboard
c.rect(51,20,8,11,ink); c.rect(52,21,6,9,'#855439')
c.rect(53,22,4,7,'#29332f')
c.line(54,23,56,23,'#b7ae83'); c.line(54,25,55,25,'#8c967b'); c.set(56,27,'#b7ae83')
# Floor, long perspective planks
c.poly([(0,34),(63,34),(63,63),(0,63)],'#513330')
c.poly([(0,49),(63,45),(63,63),(0,63)],'#654034')
for a,b in [(8,-12),(19,7),(30,28),(42,48),(53,72)]:
    # clipped manually to the floor frame
    bx=max(0,min(63,b))
    c.line(a,35,bx,63,'#38272a')
    if bx<63: c.line(a+1,36,bx+1,63,'#815039')
c.line(0,52,62,52,'#402c2c'); c.line(7,61,28,61,'#402c2c')
c.line(31,57,48,57,'#402c2c'); c.line(51,59,62,59,'#402c2c')
for x,y,w in [(3,57,4),(11,54,5),(26,61,3),(42,61,4),(55,55,5),(1,48,4)]:
    c.line(x,y,x+w,y,'#95603f')
# Rug laid under stools
c.poly([(17,49),(47,49),(57,61),(8,61)],'#34252b')
c.poly([(18,50),(46,50),(54,60),(11,60)],'#75403c')
c.poly([(20,52),(45,52),(50,58),(15,58)],'#563238')
c.line(14,59,52,59,'#b27750')
for x in range(12,54,3): c.set(x,61,'#b27750')
# Counter front: heavy wooden panels
c.poly([(9,35),(58,35),(58,46),(10,46)],ink)
c.rect(11,37,45,7,wood)
c.rect(12,38,12,5,'#885039'); c.rect(27,38,13,5,'#885039'); c.rect(43,38,12,5,'#885039')
for x in [11,25,41,55]:
    c.rect(x,37,2,8,wooddark); c.line(x,38,x,43,'#bc7e47')
c.line(12,37,54,37,'#c08549')
c.line(13,42,23,42,'#6a3e31'); c.line(29,40,38,40,'#a3653f'); c.line(45,42,53,42,'#6a3e31')
c.rect(10,44,48,2,wooddark); c.line(11,44,56,44,'#a66b40')
# The thick polished bar top
c.poly([(10,30),(55,30),(60,34),(60,37),(8,37),(6,34)],ink)
c.poly([(11,31),(54,31),(58,34),(8,34)],'#bb804a')
c.line(10,32,54,32,'#d7a464')
c.line(8,35,58,35,'#e0a25b'); c.line(9,36,58,36,'#805039')
c.line(18,33,35,33,'#a3683e'); c.line(42,34,54,34,'#8f5637')
# Glasses on the bar: beer and a stemmed glass
c.ellipse(17,32,4,1,'#805039')
c.rect(14,27,5,6,ink); c.rect(15,28,3,4,'#b97832')
c.rect(15,27,3,2,'#f0d997'); c.set(15,29,'#ffe9b2')
c.line(19,28,20,28,'#d6b276'); c.line(20,28,20,30,'#d6b276'); c.set(19,31,'#d6b276')
c.line(32,28,36,28,'#eee1b4'); c.line(33,29,35,29,'#a6aaa0')
c.set(34,30,'#ddd4a7'); c.set(34,31,'#ddd4a7'); c.line(33,32,35,32,'#b9b99d')
bottle(47,25,'#4d7260','#9cb37d',8)
# Small bar towel
c.poly([(38,32),(42,32),(44,35),(39,35)],'#ddd0a0'); c.line(40,33,42,34,'#9c8d76')
# Foreground barrel left, curved staves and iron hoops
c.ellipse(6,50,6,2,'#302127')
c.poly([(1,36),(9,36),(12,40),(12,49),(9,52),(1,52),(0,49),(0,40)],ink)
c.poly([(2,38),(8,38),(10,41),(10,48),(8,50),(1,50),(1,41)],'#9c643d')
c.line(3,39,2,49,'#c38b4c'); c.line(6,39,6,50,'#603a2d'); c.line(9,40,9,48,'#603a2d')
c.ellipse(5,37,5,2,ink); c.ellipse(5,37,4,1,'#bf8b4c'); c.line(3,37,8,37,'#885737')
for y in [41,48]:
    c.rect(1,y,10,2,'#393537'); c.line(2,y,9,y,'#7a7770'); c.set(2,y+1,'#b5a283')
# Right foreground barrel
c.ellipse(59,58,4,1,'#302127')
c.poly([(56,44),(61,44),(63,47),(63,55),(61,58),(55,57),(53,54),(53,48)],ink)
c.poly([(56,46),(61,46),(62,48),(62,55),(60,56),(55,55),(55,48)],'#95603a')
c.line(57,47,56,55,'#c38b4c'); c.line(60,47,60,55,'#603a2d')
c.ellipse(58,44,4,2,ink); c.ellipse(58,44,3,1,'#c38b4c'); c.line(56,44,60,44,'#885737')
for y in [48,54]:
    c.rect(54,y,9,2,'#393537'); c.line(55,y,61,y,'#77716a'); c.set(55,y+1,'#b5a283')
# Bar stools, dark silhouettes, splayed legs, round leather seats
def stool(x,y):
    c.ellipse(x,y+11,6,2,'#35252a')
    c.line(x-3,y+2,x-5,y+11,ink); c.line(x+3,y+2,x+5,y+11,ink)
    c.line(x-2,y+3,x-3,y+10,'#bb7c47'); c.line(x+2,y+3,x+4,y+10,'#865035')
    c.line(x-3,y+7,x+3,y+7,ink); c.line(x-3,y+8,x+3,y+8,'#9c633b')
    c.ellipse(x,y+1,6,3,ink)
    c.ellipse(x,y,5,2,'#754237'); c.line(x-3,y-1,x+2,y-1,'#c08451')
    c.line(x-3,y+2,x+3,y+2,'#9b5d3b')
stool(20,47); stool(36,49); stool(48,46)
# Soft smoke, stair-stepped translucent-looking colours chosen from wall tones
c.path('M 29 27 Q 25 24 29 21 Q 32 18 28 16 Q 24 14 28 11', '#715352', fill=False)
c.path('M 30 27 Q 27 24 31 21 Q 34 18 30 16', '#5c4044', fill=False)
c.set(27,12,'#826155'); c.set(28,11,'#76584f')
# Pendant lanterns: chains, black cage, amber panes and pale flame
for x in [14,49]:
    c.line(x,3,x,8,ink); c.set(x,5,'#a87e45')
    c.line(x-1,8,x+1,8,'#b88943')
    c.poly([(x-2,9),(x+2,9),(x+4,11),(x+3,16),(x-3,16),(x-4,11)],ink)
    c.rect(x-2,11,5,4,'#e9a547')
    c.rect(x-1,11,3,4,'#ffdc79'); c.rect(x,11,1,3,'#fff0b0')
    c.line(x-3,10,x+3,10,'#a8773d'); c.set(x-2,11,'#ffe2a0')
    c.line(x-3,15,x+3,15,'#81502e'); c.line(x-2,16,x+2,16,ink)
    c.set(x,17,'#b58746')
# Frame anchors
c.rect(0,62,64,2,ink)
# Consolidate near-identical pigments into a deliberate shared palette.
merges = {
 '#302127':'#30232b', '#35252a':'#34252b', '#38272a':'#34252b',
 '#402c2c':'#47282a', '#3b282a':'#38282b', '#54333a':'#5c4044',
 '#714331':'#714332', '#674233':'#65402f', '#805039':'#885039',
 '#815039':'#885039', '#81502e':'#885039', '#865035':'#885039',
 '#8f5637':'#885737', '#95603a':'#9c643d', '#95603f':'#9c633b',
 '#a3683e':'#a3653f', '#a66b40':'#a86d42', '#a8773d':'#b88943',
 '#b58746':'#b88943', '#b18c67':'#b59a78', '#bb7c47':'#bc7e47',
 '#b27750':'#c08451', '#c38b4c':'#bf8b4c', '#d6b276':'#c59860',
 '#ddd4a7':'#ddd0a0', '#eee1b4':'#f0d997', '#ffe9b2':'#fff0b0',
 '#ffe2a0':'#ffdc79', '#77716a':'#7a7770', '#76584f':'#715352',
 '#826155':'#715352', '#9c8d76':'#b59a78'
}
lookup={c.color(a):c.color(b) for a,b in merges.items()}
for y in range(64):
    for x in range(64):
        old=c.get(x,y)
        if old in lookup: c.set(x,y,lookup[old])
print(c.stats_text())
print(c.matrix_text(region=(7,25,38,37)))
save('tavern-interior',c)
finish(c)
