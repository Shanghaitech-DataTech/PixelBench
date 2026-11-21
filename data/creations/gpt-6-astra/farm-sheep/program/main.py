result = new_canvas(32,32,name='farm-sheep')
c = result
# Warm, low-contrast wool shades.
wool = '#f6f1e5'
light = '#fffaf0'
shade = '#e4ddce'
deep = '#cec5b6'
face = '#eee5d5'
pink = '#e5b6b0'
pinklight = '#f2cfbf'
hoof = '#9d8b7c'
# Little tail, behind the fleece.
c.ellipse(5,17,3,2,shade)
c.ellipse(4,16,2,2,wool)
# Four short legs, with the far pair subdued.
c.rect(10,22,3,5,deep)
c.rect(21,22,3,5,deep)
c.rect(10,26,3,2,hoof)
c.rect(21,26,3,2,hoof)
# Scalloped silhouette assembled from rounded wool lobes.
c.ellipse(15,17,10,7,shade)
for x,y,r in [(7,16,3),(9,12,3),(13,10,3),(17,10,3),(21,12,3),(23,16,3),(22,20,3),(18,22,3),(13,22,3),(9,21,3)]:
    c.circle(x,y,r,shade)
c.ellipse(14,15,9,6,wool)
for x,y,r in [(7,15,2),(9,12,3),(13,10,3),(17,10,3),(20,12,3),(22,15,2),(9,19,3),(13,20,3),(17,20,3),(20,18,3)]:
    c.circle(x,y,r,wool)
# Softly lit, discrete fleece clusters.
c.line(8,11,10,10,light)
c.line(12,8,14,8,light)
c.line(16,8,18,9,light)
c.line(6,14,6,16,light)
c.line(10,15,11,14,light)
c.line(11,14,13,14,light)
c.line(16,12,18,12,light)
c.line(15,17,16,16,light)
c.line(16,16,18,16,light)
c.line(9,20,11,21,shade)
c.line(14,21,16,21,shade)
c.line(18,19,19,18,shade)
# Near legs and tiny rounded hooves.
c.rect(8,23,3,4,face)
c.rect(18,23,3,4,face)
c.rect(8,27,3,2,hoof)
c.rect(18,27,3,2,hoof)
c.set(8,26,shade)
c.set(18,26,shade)
# Right-facing head, a gentle blunt muzzle.
c.ellipse(24,16,4,5,deep)
c.ellipse(24,15,4,5,face)
c.ellipse(26,18,3,3,face)
c.line(24,21,27,21,shade)
# The far ear and the longer near ear have warm pink inner folds.
c.poly([(26,11),(27,8),(29,8),(29,11),(27,13)],shade)
c.line(28,9,28,11,pink)
c.poly([(22,12),(18,10),(17,11),(18,14),(21,15),(23,14)],wool)
c.poly([(21,12),(18,11),(19,13),(21,14)],pink)
c.line(19,12,20,13,pinklight)
# Fluffy forelock wraps the brow, avoiding a heavy contour.
c.circle(23,10,3,wool)
c.circle(26,11,2,wool)
c.line(22,8,24,8,light)
c.line(24,9,26,9,light)
c.set(22,13,shade)
# Calm dark eye, blush, and a small nose.
c.set(26,15,'#685c53')
c.set(26,14,'#867566')
c.line(27,17,28,17,pinklight)
c.set(29,19,'#ad9383')
c.line(27,21,28,20,deep)
view(result,scale=12)
finish(result)
