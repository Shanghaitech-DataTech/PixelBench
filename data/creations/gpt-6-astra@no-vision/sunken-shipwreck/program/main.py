import math, random
random.seed(14)
c = new_canvas(64,64, background='#082d42', name='Sunken shipwreck')
# restrained deep-water palette
water=['#154d60','#12485b','#104356','#0d3b50','#0a3449','#082f44']
for y in range(52):
    c.rect(0,y,64,1,water[min(5,y//9)])
# shafts of filtered light, broken by water
c.poly([(6,0),(12,0),(29,45),(22,48)],'#195367')
c.poly([(20,0),(23,0),(41,44),(37,46)],'#14495c')
c.poly([(46,0),(48,0),(57,30),(54,32)],'#14495c')
for x,y,w in [(0,7,9),(25,5,12),(48,11,10),(8,16,8),(33,15,8),(0,26,7),(50,26,9),(21,22,6)]:
    c.line(x,y,x+w,y,'#1b5364')
# distant bottom shapes
c.poly([(0,44),(8,41),(17,45),(26,43),(38,47),(49,42),(63,43),(63,56),(0,56)],'#104455')
c.poly([(0,50),(11,48),(20,50),(32,49),(43,48),(54,46),(63,48),(63,64),(0,64)],'#426968')
c.poly([(0,54),(12,51),(22,53),(38,51),(50,50),(63,52),(63,64),(0,64)],'#8b9276')
c.poly([(0,59),(16,55),(29,57),(44,54),(56,55),(63,54),(63,64),(0,64)],'#b4ac82')
c.poly([(0,63),(17,60),(27,60),(36,58),(50,59),(63,57),(63,64),(0,64)],'#c6bc8f')
# sand ripples and stones
for x,y,w in [(2,56,5),(14,58,5),(28,55,5),(49,53,6),(52,61,8),(5,62,7),(34,61,7),(21,63,4)]:
    c.line(x,y,x+w,y,'#dbcc9b')
for x,y in [(9,57),(2,60),(29,61),(45,59),(60,55),(24,58),(50,63),(34,57)]:
    c.set(x,y,'#7f8d77')
# distant slender plants
for x,y,h in [(3,48,13),(59,48,15),(62,49,10)]:
    c.path(f'M{x} {y} Q{x-3} {y-h//2} {x} {y-h}', '#236466',fill=False)
# wreck's shadow
c.ellipse(33,53,24,4,'#677c6d')
c.ellipse(32,53,20,2,'#425d58')
# broken mast behind the wreck
c.poly([(31,38),(33,38),(29,12),(27,10),(27,15)],'#102d35')
c.line(28,14,32,37,'#7f7254')
c.line(29,16,32,32,'#aa9161')
c.line(21,21,39,18,'#283e3b')
c.line(21,20,38,17,'#887853')
# rigging and ragged remnant sail
c.line(28,15,16,37,'#3e6461')
c.line(29,15,47,35,'#3e6461')
c.poly([(30,21),(33,25),(37,28),(34,28),(36,31),(32,29)],'#71877a')
c.set(33,27,'#a8ac86')
# jagged hull silhouette: left stern and upturned pointed bow
hull=[(9,33),(15,34),(16,31),(19,33),(20,37),(25,38),(26,35),(28,38),(34,37),(35,34),(38,36),(45,33),(52,29),(55,29),(54,40),(50,48),(44,53),(23,54),(16,50),(12,43)]
c.poly(hull,'#132e32')
# deck cavity
c.poly([(11,35),(17,37),(26,40),(38,39),(49,34),(52,32),(50,40),(40,45),(23,45),(15,41)],'#253c37')
c.poly([(17,38),(26,41),(38,40),(47,37),(43,42),(26,46),(19,43)],'#0d2b31')
# remaining interior ribs, lit broken ends
for points in [[(16,36),(18,36),(21,45),(19,46)],[(25,37),(27,38),(29,47),(27,48)],[(35,36),(37,37),(36,47),(34,48)],[(44,35),(46,34),(44,44),(42,46)]]:
    c.poly(points,'#625c43')
c.line(17,36,19,41,'#9b8052')
c.line(26,38,27,42,'#ad8a54')
c.line(36,37,35,42,'#9b8052')
# foreground outer hull, visible sweeping planking
c.poly([(11,38),(16,40),(22,43),(32,45),(42,42),(50,37),(54,31),(53,41),(49,48),(43,52),(24,53),(17,49),(13,43)],'#694f38')
c.poly([(14,42),(23,46),(33,48),(44,45),(51,40),(49,46),(43,51),(24,52),(18,48)],'#8b6641')
c.poly([(18,47),(25,50),(36,50),(46,47),(43,51),(24,53)],'#4a4936')
# long curved plank seams
c.path('M12 39 L22 44 L32 46 L42 43 L51 37 L53 33', '#b08852',fill=False)
c.path('M14 43 L23 47 L33 49 L44 46 L51 41', '#382f29',fill=False)
c.path('M18 48 L25 51 L36 51 L45 48 L49 45', '#302f29',fill=False)
c.path('M15 44 L23 48 L33 50 L43 47', '#ad8050',fill=False)
# ribs and seams on outside, dark waterlogged foot
c.line(19,43,22,49,'#51452f')
c.line(29,46,30,50,'#51452f')
c.line(41,44,39,50,'#51452f')
c.line(48,40,45,46,'#51452f')
# exposed shattered gunwale and rusty nails
for x,y in [(12,39),(18,42),(24,45),(31,46),(39,44),(45,41),(50,37)]:
    c.set(x,y,'#d0a56a')
    c.set(x,y+2,'#253b33')
# gaping hole in the side
c.poly([(31,45),(35,44),(38,45),(38,48),(35,50),(31,49),(30,47)],'#263a33')
c.poly([(32,45),(35,45),(37,46),(36,48),(32,49)],'#0b2c33')
c.set(31,45,'#b38a54')
c.set(36,49,'#a48350')
# corrosion, algae patches, barnacles
for x,y,w in [(13,40,2),(17,44,2),(23,45,3),(26,49,2),(40,46,3),(46,42,2),(49,38,2),(20,49,2),(41,50,3)]:
    c.line(x,y,x+w,y,'#57715b')
    c.set(x+1,y+1,'#3c5949')
for x,y in [(15,41),(21,45),(25,47),(42,45),(47,41),(48,43),(28,50),(40,49)]:
    c.set(x,y,'#b3ac80')
    c.set(x+1,y,'#708c75')
# sand banks bury the lower hull
c.poly([(12,52),(18,51),(23,53),(29,53),(34,55),(42,52),(48,52),(53,54),(52,57),(10,57)],'#b4ac82')
c.line(15,53,20,53,'#d7c796')
c.line(25,55,32,55,'#dbcc9b')
c.line(40,54,47,53,'#dbcc9b')
# plank debris
c.poly([(5,52),(7,51),(14,54),(13,55)],'#494934')
c.line(6,52,12,54,'#9d8353')
c.line(37,59,45,57,'#6d6245')
c.line(38,59,44,58,'#b18f5b')
# foreground kelp with curled ribbon leaves
def kelp(x,y,h):
    c.path(f'M{x} {y} Q{x-2} {y-h//2} {x+1} {y-h}', '#1f5b4e',False)
    c.poly([(x,y-3),(x-4,y-8),(x-4,y-12),(x-2,y-10),(x,y-5)],'#36775b')
    c.poly([(x,y-7),(x+1,y-12),(x+4,y-15),(x+3,y-10)],'#408365')
    c.poly([(x,y-12),(x-2,y-16),(x-1,y-19),(x+1,y-16)],'#3b7b5e')
    c.line(x,y-2,x,y-9,'#599674')
kelp(6,56,22)
kelp(57,57,23)
# branching red coral
for pts in [[(52,58),(51,52),(48,49),(48,46)],[(51,53),(54,50),(54,46)],[(51,55),(47,54),(45,51)],[(53,51),(57,49),(57,46)]]:
    for a,b in zip(pts,pts[1:]):
        c.line(a[0],a[1],b[0],b[1],'#944b4d')
        c.line(a[0]+1,a[1],b[0]+1,b[1],'#d17966')
for x,y in [(48,46),(54,46),(57,46),(45,51)]:
    c.set(x,y,'#f0aa7f')
# little lavender fan coral at bottom left
for tx,ty in [(8,56),(10,55),(12,57),(15,56),(16,59)]:
    c.line(12,61,tx,ty,'#775e79')
    c.set(tx,ty,'#b18d9c')
c.rect(11,60,3,2,'#666e62')
# schooling fish in open water; consistently facing right
def fish(x,y,col,bright):
    c.poly([(x-4,y-2),(x-4,y+2),(x-2,y)],col)
    c.line(x-2,y,x+2,y,col)
    c.line(x-1,y-1,x+1,y-1,bright)
    c.line(x-1,y+1,x+1,y+1,col)
    c.set(x+2,y,'#092e42')
    c.set(x,y+2,col)
for x,y in [(40,9),(51,12),(45,17),(57,20),(36,24),(49,25)]:
    fish(x,y,'#6b9c9c','#bdd0b3')
# small golden fish nearer foreground
fish(17,26,'#d09659','#edc882')
fish(9,23,'#ab8b53','#d5bd7e')
# sparse particulates and ascending bubbles
for x,y in [(6,9),(17,6),(56,5),(3,30),(22,12),(60,34),(40,30),(20,31),(8,43),(45,6)]:
    c.set(x,y,'#397182')
for x,y in [(21,29),(23,24),(22,18)]:
    c.set(x,y,'#76a5a6'); c.set(x+1,y-1,'#76a5a6')
print(c.stats_text())
print(c.matrix_text(region=(9,31,54,54)))
save('sunken_shipwreck',c)
finish(c)
