result = new_canvas(32,32,name='farm_sheep')
c=result
# Warm, restrained wool tones and soft taupe hooves.
shade='#cec8b8'
mid='#e5dfce'
white='#f6f1e3'
light='#fff9ed'
face='#e4d9c7'
pink='#e4b6ad'
# Four short legs, partially hidden by the fleece.
c.rect(9,22,3,5,'#c2b5a2')
c.rect(21,22,3,5,'#c2b5a2')
c.rect(9,26,3,2,'#9c8b7b')
c.rect(21,26,3,2,'#9c8b7b')
c.rect(6,22,3,6,face)
c.rect(17,23,3,5,face)
c.rect(6,27,3,2,'#b09b88')
c.rect(17,27,3,2,'#b09b88')
# Rounded tail and scalloped fleece silhouette.
c.ellipse(4,17,2,3,mid)
c.set(2,16,white)
c.ellipse(14,17,11,8,mid)
for x,y,r in [(7,13,4),(11,10,4),(17,10,4),(21,13,4),(7,20,4),(12,22,3),(17,22,3),(21,20,4)]:
 c.circle(x,y,r,mid)
c.ellipse(14,15,10,6,white)
for x,y,r in [(7,13,3),(11,10,3),(17,10,3),(20,12,3),(7,18,3),(12,19,4),(17,19,4)]:
 c.circle(x,y,r,white)
# Subtle curls, highlights only on the upper-left edges.
c.line(9,8,12,8,light)
c.line(8,9,8,10,light)
c.line(16,8,18,8,light)
c.line(5,13,5,15,light)
c.line(10,15,12,15,mid)
c.set(9,14,mid)
c.line(15,12,17,12,mid)
c.set(14,11,mid)
c.line(13,21,15,21,mid)
c.set(12,20,mid)
c.line(6,23,8,23,shade)
c.line(19,23,21,23,shade)
# Far ear, face facing right, and a long near ear.
c.poly([(24,10),(27,8),(28,8),(28,11),(25,13)],'#cabaa8')
c.line(26,10,27,9,pink)
c.ellipse(25,16,4,6,face)
c.ellipse(27,19,3,3,face)
c.line(24,22,27,22,'#cbbca8')
c.rect(28,18,3,3,face)
c.set(30,20,'#b5a08f')
c.set(29,21,'#cbbca8')
c.poly([(23,12),(19,12),(19,14),(21,16),(23,15)],'#d5c4b3')
c.line(20,13,22,14,pink)
c.set(21,14,'#edc3b7')
# A soft wool cap overlaps the brow.
c.circle(23,11,3,white)
c.circle(26,11,2,white)
c.line(22,9,24,9,light)
c.set(26,13,mid)
# Small gentle eye and warm cheek.
c.rect(27,15,1,2,'#6b6056')
c.set(28,15,'#6b6056')
c.set(27,15,'#857363')
c.line(26,18,27,18,'#e3bfb0')
view(result)
finish(result)
