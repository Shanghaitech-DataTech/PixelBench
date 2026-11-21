# Preserve every non-white pixel of the supplied motorcycle.
bike = input_canvas.copy(name='motorcycle')
white = input_canvas.get(0, 0)
for y in range(64):
    for x in range(64):
        if input_canvas.get(x,y) == white:
            bike.set(x,y,None)

c = new_canvas(64,64,background='#a8d9e5',name='output')
sky='#a8d9e5'; cloud='#edf4dd'; distant='#7ca590'; hill='#7fa85a'; light='#a6bc62'; grass='#739849'; deep='#4c7843'; hedge='#375b3e'; sand='#c2b682'; asphalt='#777b78'; roadlight='#858883'; roadshadow='#666e6b'; stripe='#ebd99e'
# Quiet sky, stepped clouds, and overlapping distant pastures.
c.rect(4,7,14,3,cloud).rect(7,5,7,2,cloud).rect(16,8,5,2,cloud)
c.rect(40,4,13,3,cloud).rect(44,2,6,2,cloud).rect(52,5,7,2,cloud)
c.poly([(0,20),(7,17),(14,17),(23,21),(34,18),(43,16),(51,18),(63,15),(63,31),(0,31)],distant)
c.poly([(0,23),(12,21),(23,23),(35,27),(47,22),(57,21),(63,23),(63,39),(0,39)],hill)
c.poly([(0,29),(13,27),(26,28),(39,31),(50,29),(63,27),(63,47),(0,47)],light)
c.poly([(0,35),(16,32),(31,34),(46,36),(63,31),(63,63),(0,63)],grass)
# A distant red barn and a pair of trees give the fields a rural scale.
c.rect(7,22,10,7,'#b96b4c')
c.poly([(5,22),(11,17),(13,17),(19,22)],'#655951')
c.line(7,22,17,22,'#e3c690')
c.rect(11,24,4,5,'#66544a').line(12,24,12,28,'#d3ac79')
c.rect(8,24,2,2,'#e3c690')
c.rect(23,23,2,8,'#6d684b')
c.rect(20,21,8,5,deep).rect(22,18,5,3,deep).rect(21,20,4,3,hill)
c.rect(2,25,1,6,'#6d684b').rect(0,21,6,5,deep).rect(0,20,4,2,deep)
# Field boundaries and a short wooden fence.
c.line(29,27,43,25,'#91ae5d')
c.line(0,33,22,31,'#c2bf83')
c.line(0,36,22,34,'#8b8159')
for x,y in [(2,34),(10,33),(18,32)]:
    c.rect(x,y,1,6,'#786d50').set(x,y,'#d6c18a')
# Road shoulder: narrow in the distance, opening into the foreground.
c.poly([(54,23),(58,23),(60,28),(58,33),(53,38),(63,40),(63,63),(0,63),(0,44),(28,38),(44,33),(51,28)],sand)
c.poly([(55,23),(57,23),(58,28),(56,32),(50,37),(44,40),(63,43),(63,63),(0,63),(0,47),(30,40),(46,34),(53,28)],asphalt)
c.poly([(0,57),(28,46),(47,39),(63,46),(63,63),(0,63)],roadlight)
c.line(55,24,55,27,roadshadow).line(54,29,51,32,roadshadow)
# Broken warm centre markings follow the bend, away from the wheels.
c.line(56,25,56,26,stripe)
c.line(55,29,54,30,stripe)
c.line(51,33,49,35,stripe)
c.poly([(34,44),(39,42),(41,43),(36,45)],stripe)
c.poly([(9,57),(20,52),(23,53),(12,59)],stripe)
# Small clusters on the verges, with denser green beside the near edge.
c.poly([(0,40),(4,39),(7,40),(10,39),(16,40),(0,44)],deep)
for x,y in [(1,39),(5,40),(12,39),(60,34),(62,36),(61,40)]:
    c.line(x,y,x,y-2,deep)
    c.set(x+1,y-1,light)
c.set(3,38,'#e6d58a').set(14,39,'#e6d58a').set(62,33,'#e6d58a')
# Softly stepped contact shadow, then the unaltered motorcycle pixels.
c.ellipse(31,54,25,2,roadshadow)
c.line(10,54,21,54,'#4f5954').line(45,54,55,54,'#4f5954')
c.blit(bike,0,6)
print(c.stats_text())
print(c.matrix_text(region=(0,16,63,35)))
save('motorcycle_country_road',c)
finish(c)
