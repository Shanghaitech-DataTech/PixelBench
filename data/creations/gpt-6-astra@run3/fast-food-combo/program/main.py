result = new_canvas(64,64, '#293440', name='fast_food_combo')
c=result
O='#241e29'; shadow='#1c2631'; rim='#667c85'; light='#a7bab5'; paper='#eeddb6'; pshade='#cbbd98'
# background and tray cast shadow
c.ellipse(33,49,29,10,shadow)
c.poly([(3,22),(46,15),(62,31),(59,52),(17,60),(2,42)],O)
c.poly([(3,24),(46,18),(61,32),(57,51),(17,57),(3,41)],rim)
c.poly([(5,25),(45,20),(58,33),(54,49),(18,54),(6,40)],'#344c58')
c.line(4,24,16,40,light); c.line(17,56,57,50,light); c.line(58,49,61,34,'#879d9e')
# liner
c.poly([(7,26),(44,22),(56,33),(52,47),(19,51),(8,39)],pshade)
c.poly([(7,26),(44,22),(56,33),(51,44),(20,48),(8,38)],paper)
# subtle paper print/checks
for x,y in [(11,28),(19,27),(33,25),(48,31),(17,43),(31,46),(45,43)]:
 c.line(x,y,x+2,y+2,'#d9b397')
# cola rear right silhouette
c.poly([(41,14),(57,13),(55,33),(52,36),(46,36),(43,32)],O)
c.poly([(43,16),(55,16),(53,32),(51,34),(47,34),(45,31)],'#a83039')
c.poly([(44,18),(48,19),(49,33),(47,33),(45,30)],'#ed6250')
c.poly([(49,20),(55,18),(54,25),(46,28),(45,23)],'#f9e2b8')
c.line(48,29,52,28,'#dd5043')
# cup rim and cola
c.ellipse(49,14,9,5,O);c.ellipse(49,13,8,4,'#e5d6b6');c.ellipse(49,13,6,3,'#492628')
c.line(46,15,51,16,'#8b4530')
# ice cubes
c.poly([(44,12),(47,10),(49,12),(47,14)],'#a7c4bd');c.set(46,11,'#edf3d8')
c.poly([(50,12),(53,11),(54,13),(51,15)],'#7ea5a7');c.line(51,12,53,12,'#d2e5d8')
# bent straw
c.line(50,12,51,5,O);c.line(51,5,55,2,O);c.line(51,12,52,5,'#fff1cc');c.line(52,5,56,2,'#fff1cc');c.set(52,8,'#e45147');c.set(54,3,'#e45147')
# fries rear left shadows and sticks
c = new_canvas(64,64,name='fries')
fries=[(9,12,2,14),(12,9,3,16),(16,11,3,13),(20,8,3,17),(24,12,2,13),(27,14,3,13)]
for x,y,w,h in fries:
 c.rect(x-1,y-1,w+2,h+2,O);c.rect(x,y,w,h,'#d78b32');c.line(x,y,x,y+h-2,'#ffdb73');c.set(x+1,y,'#ffe9a0')
c.poly([(7,21),(14,23),(21,22),(30,20),(28,34),(24,38),(13,37),(9,32)],O)
c.poly([(9,23),(15,26),(23,25),(28,23),(26,33),(23,36),(14,35),(11,31)],'#bc303d')
c.poly([(10,24),(15,27),(21,27),(20,35),(14,34),(12,30)],'#ee5249')
c.line(16,27,23,26,'#f87858')
# little carton emblem
c.line(16,32,17,29,'#ffe099');c.line(17,29,19,32,'#ffe099');c.line(19,32,21,29,'#ffe099');c.line(21,29,22,31,'#ffe099')
c.shift(-2,-6)
result.blit(c,0,0)
c=result
# nuggets right foreground
for x,y in [(43,35),(50,39),(41,43)]:
 c.poly([(x-4,y-2),(x-2,y-4),(x+2,y-4),(x+4,y-2),(x+4,y+1),(x+2,y+3),(x-2,y+3),(x-5,y+1)],O)
 c.poly([(x-3,y-2),(x-1,y-3),(x+2,y-3),(x+3,y-1),(x+2,y+2),(x-2,y+2),(x-4,y)],'#b96728')
 c.poly([(x-3,y-2),(x,y-3),(x+2,y-2),(x+2,y),(x-1,y+1),(x-3,y)],'#efa744')
 c.line(x-2,y-2,x,y-2,'#ffcf68');c.set(x+1,y,'#d0832e');c.set(x-2,y+1,'#8e4929');c.set(x+2,y-1,'#ffe08b')
# burger shadow and bottom bun
c.ellipse(24,44,13,5,'#827454')
c.ellipse(23,40,13,7,O)
c.ellipse(23,41,11,5,'#bd6b32')
c.ellipse(23,40,11,4,'#efaa51')
c.line(17,44,25,45,'#ffcf77');c.line(29,43,32,41,'#d28139')
# beef patty
c.ellipse(23,38,13,5,O)
c.ellipse(23,38,11,3,'#65372b');c.line(15,39,19,40,'#a35b35');c.line(23,40,29,39,'#994a2e');c.set(31,37,'#b8773c')
# melted cheese hanging over patty
c.poly([(11,35),(22,32),(35,34),(33,37),(29,37),(27,41),(23,38),(18,38),(15,40),(14,37)],'#e98d22')
c.poly([(12,34),(24,32),(34,34),(31,36),(28,36),(27,39),(23,36),(18,37),(15,38),(15,36)],'#ffcf48')
c.line(19,35,24,34,'#ffe98b')
# lettuce ruffles
c.poly([(10,32),(13,30),(17,31),(20,29),(24,30),(28,29),(32,31),(36,32),(34,35),(30,34),(27,36),(23,34),(20,36),(17,34),(14,35),(11,34)],O)
c.poly([(11,32),(15,31),(18,32),(21,30),(24,32),(28,30),(32,32),(35,32),(33,34),(29,33),(27,35),(23,33),(20,34),(17,33),(14,34)],'#568b38')
c.line(12,32,16,32,'#a9cb50');c.line(20,32,23,32,'#b9d965');c.line(27,32,30,31,'#a9cb50')
# sesame bun dome
c.path('M 10 31 Q 10 22 20 20 Q 30 18 35 27 L 36 31 Q 25 38 10 31 Z',O)
c.path('M 12 30 Q 12 23 20 22 Q 29 20 33 27 L 34 30 Q 25 35 12 30 Z','#d88b3d')
c.path('M 13 28 Q 15 22 22 22 Q 29 22 32 27 L 32 29 Q 24 32 14 29 Z','#f3b85e')
c.path('M 16 25 Q 22 21 28 25 L 29 26 Q 22 24 16 27 Z','#ffcf7a')
c.line(15,31,20,32,'#edaa4b')
for x,y in [(16,26),(20,24),(25,23),(29,26),(23,28),(31,29),(18,29)]:
 c.set(x+1,y+1,'#bd7a37');c.line(x,y,x+1,y-1,'#fff1b3')
# sauce cups at front
for x,y,col,hi in [(48,48,'#a7352c','#e15b37'),(36,51,'#e5b65c','#ffe6a0')]:
 c.ellipse(x,y+2,5,3,O);c.rect(x-4,y,9,3,'#b6b9a5');c.line(x-2,y+4,x+2,y+4,'#e6dfbf')
 c.ellipse(x,y,6,3,O);c.ellipse(x,y,5,2,'#fff0cc');c.ellipse(x,y,3,1,col);c.line(x-2,y-1,x,y-1,hi)
assert result.stats()['colors_used'] <= 86
save('fast-food-combo', result)
view(result)
finish(result)
