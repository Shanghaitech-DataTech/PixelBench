result = new_canvas(32, 32, name='farm_sheep')
c=result
# Warm wool tones, with coloured edges rather than dark outlines.
shade='#c9c4b2'
mid='#ded9c8'
base='#eeeada'
light='#faf6e8'
face='#e9dfcc'
face_light='#f5ecdb'
pink='#dfb8ad'
pink_light='#f0cec0'
hoof='#a79a8c'
# Far legs.
c.rect(12,22,3,5,shade)
c.rect(12,26,3,2,hoof)
c.rect(22,22,3,5,shade)
c.rect(22,26,3,2,hoof)
# Small rounded tail.
c.ellipse(5,17,3,3,mid)
c.ellipse(4,16,2,2,base)
c.set(3,15,light)
# Scalloped fleece silhouette.
c.ellipse(14,16,9,8,mid)
c.ellipse(9,12,4,4,mid)
c.ellipse(14,10,4,4,mid)
c.ellipse(19,11,4,4,mid)
c.ellipse(22,15,4,4,mid)
c.ellipse(21,20,4,4,mid)
c.ellipse(16,22,4,3,mid)
c.ellipse(10,20,4,4,mid)
c.ellipse(7,16,3,4,mid)
# Broad, flat-lit wool masses.
c.ellipse(14,15,8,7,base)
c.ellipse(9,12,3,3,light)
c.ellipse(14,10,3,3,light)
c.ellipse(19,11,3,3,base)
c.ellipse(8,16,3,3,base)
c.ellipse(12,14,4,4,light)
c.ellipse(17,14,4,4,light)
c.ellipse(21,15,3,3,base)
c.ellipse(12,19,4,3,base)
c.ellipse(18,19,4,3,base)
# Quiet fleece curls, kept sparse at this scale.
c.line(7,18,8,19,mid)
c.line(8,19,10,19,mid)
c.line(13,19,14,20,mid)
c.line(14,20,16,20,mid)
c.set(16,19,mid)
c.line(18,9,19,9,light)
c.line(10,9,11,8,light)
# Near legs and tiny soft taupe hooves.
c.rect(9,23,3,5,base)
c.rect(9,27,3,2,hoof)
c.set(9,27,'#b7aa99')
c.rect(19,23,3,5,base)
c.rect(19,27,3,2,hoof)
c.set(19,27,'#b7aa99')
# Far ear, peeking above the head.
c.poly([(24,10),(25,6),(27,5),(28,6),(27,10)],mid)
c.line(26,7,26,9,pink)
# Side-facing rounded face and muzzle.
c.ellipse(25,14,4,5,mid)
c.ellipse(25,14,3,4,face)
c.ellipse(27,17,3,3,face)
c.ellipse(27,16,2,2,face_light)
c.line(25,19,28,19,'#d6cbb9')
# Visible floppy pink ear.
c.poly([(23,11),(20,10),(18,11),(19,14),(21,15),(23,13)],mid)
c.poly([(22,11),(19,11),(20,13),(21,14),(23,12)],pink)
c.line(20,11,21,12,pink_light)
# Wool cap overlapping the crown.
c.ellipse(24,10,3,2,base)
c.ellipse(23,9,2,2,light)
c.ellipse(26,10,2,2,base)
c.set(24,11,light)
# Kind dark eye and a discreet nose.
c.set(27,14,'#695e56')
c.set(27,13,'#8c7a69')
c.set(29,17,'#ad9285')
c.set(28,18,'#d3b6a4')
view(result)
finish(result)
