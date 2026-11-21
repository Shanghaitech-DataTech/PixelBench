# A small, warm, cloud-fleeced farm sheep, facing right.
result = new_canvas(32, 32, name='farm-sheep')
c = result
cream = '#f7f2e5'
light = '#fffbef'
wool = '#e9e1d0'
shade = '#d5c9b5'
face = '#e9dcc6'
face_light = '#f4e7d0'
face_shadow = '#d3bfa5'
pink = '#e5afa9'
pink_light = '#f3cbc1'
hoof = '#9c8977'
hoof_light = '#b4a08a'
eye = '#665b52'

# Far legs sit behind the fleece, in a warmer shadow.
c.poly([(11,21),(14,21),(14,27),(13,29),(11,29)], face_shadow)
c.rect(11,27,3,2,hoof)
c.poly([(21,21),(24,21),(24,28),(23,29),(21,29)], face_shadow)
c.rect(21,27,3,2,hoof)

# Little woolly tail at the rump.
c.ellipse(4,17,2,3,wool)
c.ellipse(3,16,2,2,cream)
c.set(2,15,light)

# Joined scallops give a single cloud-shaped body.
c.ellipse(14,17,10,7,wool)
for x,y,r in [(7,14,3),(10,11,3),(15,11,4),(20,12,4),(23,16,3),(21,21,4),(16,23,3),(11,22,4),(7,20,3),(5,17,3)]:
    c.circle(x,y,r,wool)
# Softly shadowed lower scallops, with no dark border.
c.ellipse(14,19,9,5,wool)
c.line(9,24,12,24,shade)
c.line(16,25,18,25,shade)
c.line(21,24,23,23,shade)

# Near legs have cream fronts and short muted hooves.
c.poly([(8,22),(11,22),(11,28),(10,30),(8,30)],face)
c.line(8,24,8,27,face_light)
c.rect(8,28,3,2,hoof_light)
c.set(10,29,hoof)
c.poly([(19,22),(22,22),(22,28),(21,30),(19,30)],face)
c.line(19,24,19,27,face_light)
c.rect(19,28,3,2,hoof_light)
c.set(21,29,hoof)

# Broad fleece planes and rounded tufts, lit from upper left.
c.ellipse(13,16,9,6,cream)
for x,y,r in [(7,13,2),(10,11,3),(15,10,3),(19,12,3),(22,15,3),(7,18,3),(11,20,3),(16,21,3),(20,19,3)]:
    c.circle(x,y,r,cream)
c.ellipse(11,13,6,3,light)
c.circle(7,14,2,light)
c.circle(15,10,2,light)
c.ellipse(17,14,4,3,light)
c.ellipse(10,18,3,2,light)
# Just a few crescent-shaped wool separations.
c.line(5,19,6,20,wool)
c.line(12,21,14,21,wool)
c.set(15,20,wool)
c.line(19,17,20,17,wool)
c.set(21,16,wool)
c.line(9,10,10,9,light)

# The far ear peeks around the head on its left.
c.poly([(23,13),(20,11),(20,9),(23,10),(25,12),(24,14)],face_shadow)
c.line(21,10,23,12,pink)
c.set(21,10,pink_light)

# A long, soft face and rounded muzzle make the side view clear.
c.poly([(24,12),(27,12),(29,14),(29,18),(30,19),(30,21),(28,23),(25,22),(23,19),(23,15)],face_shadow)
c.poly([(24,13),(27,13),(28,15),(28,18),(30,19),(30,21),(28,22),(25,21),(24,18)],face)
c.line(25,15,25,19,face_light)
c.line(26,20,28,21,face_light)

# Long pink near ear, angled outward, with a cream rim.
c.poly([(26,12),(28,10),(31,10),(30,13),(28,15),(26,14)],face)
c.poly([(27,12),(30,11),(29,13),(28,14),(27,13)],pink)
c.line(28,12,29,11,pink_light)

# Small wool cap overlaps the ear roots and forehead.
c.circle(24,12,3,cream)
c.circle(26,12,2,cream)
c.circle(23,13,2,cream)
c.line(23,10,25,10,light)
c.line(22,11,22,12,light)
c.set(26,13,wool)

# Calm eye and the tiniest muzzle details.
c.set(28,16,eye)
c.set(27,16,face_light)
c.set(30,20,hoof)
c.set(29,22,face_shadow)

# Center the finished silhouette within its transparent tile.
c.shift(0, -2)
print(c.stats_text())
print(c.matrix_text(region=(19,7,31,21)))
save('farm-sheep', result)
finish(result)
