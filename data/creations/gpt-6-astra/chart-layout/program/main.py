result = new_canvas(128, 64, '#142330', name='fruit_chart')
c = result
# A restrained grid: each interval is four units.
for x in (26, 50, 74, 98):
    c.line(x, 4, x, 59, '#243542')
c.line(25, 4, 25, 59, '#536471')
c.line(25, 59, 111, 59, '#536471')
for x in (26, 50, 74, 98):
    c.set(x, 60, '#536471')
# Bars use a common zero and exactly six pixels per fruit.
rows = [(10,10,'#ee5260','#ff8790','#b63349'),
        (21,5,'#f3c64f','#ffe68a','#bc8c30'),
        (32,7,'#f58b38','#ffb563','#c95c28'),
        (43,14,'#e4e95a','#f8fba2','#a8b43e'),
        (54,2,'#a67ade','#d1a4f5','#7252ae')]
for y, value, body, light, shadow in rows:
    width = value * 6
    c.rect(26,y-3,width,7,body)
    c.line(26,y-3,26+width-1,y-3,light)
    c.line(26,y+3,26+width-1,y+3,shadow)
    c.text(30+width,y-3,str(value),'#e9f0ec')
# Apple: stem, green leaf, two lobes and warm red shading.
c.line(12,3,12,6,'#a77a4d')
c.poly([(13,4),(15,2),(18,2),(16,4)],'#78c87b')
c.poly([(7,6),(10,5),(12,6),(15,5),(18,7),(18,11),(16,15),(13,16),(11,15),(9,16),(6,12),(6,8)],'#922f48')
c.poly([(7,7),(10,6),(12,7),(15,6),(17,8),(17,11),(15,14),(12,14),(10,15),(7,11)],'#ee5260')
c.line(8,8,8,10,'#ffc0ac')
c.set(9,7,'#ffc0ac')
c.line(15,11,14,13,'#bf354a')
# Banana: a curved golden crescent with its tips turned upward.
c.path('M 6 18 L 8 17 Q 8 24 13 24 Q 17 23 18 18 L 20 18 Q 20 27 13 28 Q 6 28 5 21 Z','#ad7c2d')
c.path('M 6 18 L 7 18 Q 8 25 13 25 Q 18 24 19 19 Q 19 26 13 27 Q 7 27 6 21 Z','#f3c64f')
c.path('M 7 20 Q 9 27 15 25 Q 18 24 19 21', '#ffe997',fill=False)
c.set(6,17,'#a27b50')
c.set(19,18,'#a27b50')
# Orange: round silhouette, leaf and clustered peel highlights.
c.circle(12,33,6,'#c95c28')
c.circle(12,32,5,'#f58b38')
c.line(9,29,11,29,'#ffcc7c')
c.line(8,30,8,32,'#ffb563')
c.set(15,34,'#df6d2e')
c.set(13,36,'#df6d2e')
c.line(12,26,12,28,'#8f8047')
c.poly([(12,27),(15,24),(18,25),(15,27)],'#6fba73')
# Lemon: pointed ends and a pale rind highlight.
c.poly([(5,43),(7,42),(9,39),(14,38),(17,40),(19,43),(18,45),(15,48),(10,48),(7,46),(5,46)],'#a8b43e')
c.poly([(6,43),(9,40),(14,39),(17,41),(18,44),(15,47),(10,47),(7,45)],'#e4e95a')
c.line(10,40,13,40,'#f8fba2')
c.line(8,42,9,41,'#f8fba2')
c.set(15,45,'#c5ce46')
# Grapes: overlapping berries form a tapered bunch.
c.line(12,48,12,51,'#a17b50')
c.poly([(13,49),(16,48),(18,49),(16,51),(13,51)],'#6fba73')
for x,y in [(9,52),(14,52),(7,55),(12,55),(16,55),(10,58),(14,58),(12,61)]:
    c.circle(x,y,2,'#7252ae')
    c.circle(x,y-1,1,'#a67ade')
    c.set(x-1,y-1,'#d1a4f5')
view(result)
finish(result)
