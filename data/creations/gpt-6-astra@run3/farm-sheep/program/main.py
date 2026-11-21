result = new_canvas(32, 32, name='farm_sheep')
c = result
# A small warm palette: wool shadows, cream highlights, and rosy skin.
shade = '#d4cbb9'
mid = '#e8e1d1'
wool = '#f6f1e5'
light = '#fffaf0'
leg = '#c9bda9'
hoof = '#a69787'
face = '#eee3d1'
pink = '#dcaeaa'
pinklight = '#edc7be'
eye = '#665d55'
# Far legs remain visible behind the rounded fleece.
c.rect(11, 22, 3, 5, leg)
c.rect(21, 22, 3, 5, leg)
c.rect(11, 26, 3, 2, hoof)
c.rect(21, 26, 3, 2, hoof)
# A little woolly tail at the left.
c.ellipse(5, 16, 3, 3, mid)
c.ellipse(4, 15, 2, 2, wool)
c.set(3,14,light)
# Scalloped body silhouette.
c.ellipse(14, 17, 10, 7, shade)
for x,y,r in [(7,13,3),(10,10,3),(15,10,4),(19,11,4),(22,14,3),(22,19,3),(18,22,3),(12,22,3),(7,20,3)]:
    c.circle(x,y,r,mid)
c.ellipse(14,16,9,6,wool)
for x,y,r in [(7,13,2),(10,10,2),(15,9,3),(19,11,3),(22,14,2),(7,18,2)]:
    c.circle(x,y,r,wool)
# Soft, small wool clusters, mostly defined by lit upper edges.
c.line(8,11,10,11,light)
c.line(12,8,15,8,light)
c.line(18,10,19,10,light)
c.line(6,15,6,16,light)
c.line(10,15,12,15,light)
c.set(10,16,light)
c.line(16,13,18,13,light)
c.line(14,19,16,19,mid)
c.set(13,18,mid)
c.line(7,21,9,21,shade)
c.line(13,23,15,23,shade)
c.line(19,21,21,21,shade)
# Near legs and soft brown hooves.
c.rect(8,23,3,5,face)
c.rect(8,27,3,2,hoof)
c.rect(9,24,1,3,wool)
c.rect(18,23,3,5,face)
c.rect(18,27,3,2,hoof)
c.rect(19,24,1,3,wool)
# Far ear peeks out over the profile.
c.poly([(24,11),(25,7),(28,7),(27,12)],mid)
c.line(26,8,26,10,pinklight)
# Rounded face, looking right.
c.ellipse(25,17,4,5,leg)
c.ellipse(25,16,4,5,face)
c.ellipse(27,18,3,3,face)
c.line(24,13,26,13,wool)
c.line(29,18,29,19,mid)
c.line(25,21,28,21,leg)
# Near ear, drooping gently to the left.
c.poly([(24,12),(21,11),(18,12),(19,15),(22,16),(24,14)],mid)
c.poly([(22,12),(19,12),(20,14),(22,15),(23,13)],pinklight)
c.line(20,14,22,14,pink)
# Puffy forehead cap.
c.circle(24,11,3,wool)
c.circle(27,12,2,wool)
c.circle(22,11,2,wool)
c.line(23,9,25,9,light)
c.set(27,11,light)
# Quiet expression and a tiny rosy muzzle.
c.rect(27,15,1,2,eye)
c.set(28,19,pink)
c.set(29,19,pink)
c.set(28,20,leg)
view(result)
finish(result)
