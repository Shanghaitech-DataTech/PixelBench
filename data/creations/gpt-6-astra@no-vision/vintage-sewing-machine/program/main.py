result = new_canvas(48, 48, name='vintage_sewing_machine')
c=result
ink='#17212b'
deep='#243440'
body='#344c53'
light='#547175'
shine='#79918b'
gold='#b78a48'
bright='#e1bd73'
shade='#765935'
steel='#a9bdbe'
white='#e1e2c6'
# Cast-iron base, with an angled front and right edge.
c.poly([(5,33),(35,30),(44,34),(44,39),(39,43),(5,41),(3,38)],ink)
c.poly([(5,33),(35,31),(43,34),(38,39),(5,38)],body)
c.poly([(5,38),(38,39),(43,35),(43,39),(38,42),(5,40)],deep)
c.line(6,40,37,42,shade)
c.line(38,41,42,38,gold)
c.line(7,34,34,32,gold)
c.line(6,36,6,37,bright)
c.line(8,37,36,38,gold)
c.line(36,38,41,34,shade)
# Feet at the corners.
c.rect(7,41,5,2,ink)
c.rect(35,42,5,2,ink)
# Steel work plate.
c.poly([(8,32),(19,31),(24,34),(18,37),(7,36)],ink)
c.poly([(9,32),(18,32),(22,34),(17,36),(8,35)],steel)
c.line(10,34,17,34,light)
c.set(10,33,white)
# Crimson fabric fed under the presser foot and draped over the table edge.
c.poly([(15,32),(23,31),(30,33),(28,36),(29,39),(34,43),(29,45),(19,44),(15,41),(14,37)],'#662e3d')
c.poly([(15,32),(23,32),(28,33),(25,36),(27,40),(31,43),(28,44),(20,43),(16,40),(15,37)],'#bd404c')
c.poly([(17,33),(21,33),(21,37),(24,41),(28,43),(21,42),(18,39)],'#e26460')
c.line(24,34,23,37,'#8d303e')
c.line(23,37,26,41,'#8d303e')
c.line(16,39,19,42,'#f18b71')
c.line(20,43,28,44,'#e26460')
# The handwheel sits behind the pillar, seen as a narrow ellipse.
c.ellipse(39,18,6,9,ink)
c.ellipse(40,18,5,8,steel)
c.ellipse(40,18,3,6,deep)
c.line(40,12,40,24,light)
c.line(37,15,43,21,steel)
c.line(37,21,43,15,steel)
c.ellipse(39,18,2,3,ink)
c.ellipse(40,18,1,2,gold)
c.set(40,17,bright)
c.line(43,12,44,14,white)
c.line(44,15,44,19,white)
c.line(42,25,44,23,light)
# Sweeping head and curved upright: stepped cast-metal silhouette.
c.poly([(9,12),(11,9),(17,8),(29,9),(33,10),(36,14),(36,29),(39,32),(37,35),(27,35),(25,33),(28,30),(29,22),(28,18),(24,16),(16,16),(16,23),(13,26),(9,24),(8,20),(8,15)],ink)
c.poly([(10,12),(13,10),(19,10),(29,11),(33,12),(34,16),(34,29),(36,32),(34,33),(28,33),(30,29),(31,21),(29,17),(25,14),(16,14),(14,16),(14,23),(11,23),(10,20)],body)
c.poly([(13,10),(19,9),(29,10),(32,11),(33,13),(28,12),(18,11),(12,13),(10,16),(10,13)],light)
c.line(15,10,24,11,shine)
c.poly([(33,15),(35,16),(35,29),(37,32),(34,32),(33,27)],deep)
c.line(30,21,30,28,light)
c.line(29,30,28,32,shine)
# Fine gold pinstriping on the arm and pedestal.
c.line(17,13,25,13,gold)
c.line(25,13,29,15,gold)
c.line(29,15,31,18,gold)
c.line(31,18,32,24,shade)
c.line(28,33,35,33,gold)
c.set(29,32,bright)
c.set(34,31,gold)
# Small decorative medallion in the arm.
c.rect(21,12,3,3,shade)
c.line(21,12,23,12,bright)
c.set(22,13,gold)
c.set(22,14,bright)
# Brushed metal faceplate and its screws.
c.poly([(9,14),(12,12),(14,13),(14,22),(12,24),(9,22)],deep)
c.poly([(10,14),(12,13),(13,14),(13,21),(11,23),(10,21)],steel)
c.line(10,15,10,20,white)
c.set(12,15,light)
c.set(11,21,ink)
# Tension knob on the front edge.
c.rect(7,17,3,3,ink)
c.rect(7,17,2,2,gold)
c.set(7,17,bright)
# Thread spool and spindle.
c.line(24,3,24,9,steel)
c.rect(21,4,6,1,shade)
c.rect(22,5,4,3,'#c9a779')
c.line(22,5,25,5,white)
c.line(22,7,25,7,gold)
c.rect(21,8,6,1,bright)
c.set(24,2,white)
# Fine thread, routed along the upper arm.
c.line(22,9,16,11,'#cfb98d')
c.set(14,12,bright)
# Needle bar, needle, and separate presser-foot lever.
c.rect(10,24,2,5,ink)
c.line(11,24,11,28,steel)
c.line(11,29,11,32,white)
c.line(14,24,14,31,ink)
c.line(14,25,14,30,steel)
c.line(14,31,17,32,steel)
c.line(12,33,17,33,ink)
c.line(12,32,16,32,white)
c.set(11,33,ink)
# Oil port and bed fasteners.
c.set(30,11,ink)
c.set(33,29,gold)
c.set(39,35,bright)
c.set(7,37,shine)
print(c.stats_text())
print(c.matrix_text(region=(7,8,44,35)))
save('vintage_sewing_machine',result)
finish(result)
