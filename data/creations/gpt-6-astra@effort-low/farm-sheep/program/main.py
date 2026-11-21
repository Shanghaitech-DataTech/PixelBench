result = new_canvas(32,32)
c=result
# Muted wool, warm shadows and rosy details.
shadow='#c9c3b4'
mid='#e1ddce'
wool='#f3efdf'
light='#fff9e9'
face='#e9dfcd'
rose='#d7aaa5'
pink='#efc5bd'
hoof='#a59888'
# Four short legs, partially hidden under the fleece.
c.rect(9,21,3,6,shadow)
c.rect(20,21,3,6,shadow)
c.rect(9,26,3,2,hoof)
c.rect(20,26,3,2,hoof)
c.rect(6,21,3,7,face)
c.rect(17,22,3,6,face)
c.rect(6,27,3,2,hoof)
c.rect(17,27,3,2,hoof)
c.set(6,26,light)
c.set(17,26,light)
# Tail at the left, and the scalloped round body.
c.ellipse(4,17,2,3,mid)
c.ellipse(3,16,1,2,wool)
c.ellipse(13,17,10,7,mid)
for x,y,r in [(6,14,3),(8,11,3),(12,10,3),(16,10,3),(20,12,3),(22,15,3),(21,19,3),(18,22,3),(13,22,3),(8,21,3),(5,18,3)]:
 c.circle(x,y,r,mid)
c.ellipse(13,16,9,6,wool)
for x,y,r in [(6,13,2),(9,10,2),(13,9,2),(17,10,2),(20,12,2),(6,17,2),(9,20,2),(13,21,2),(18,20,2)]:
 c.circle(x,y,r,wool)
# Small clustered highlights suggest soft curls without outlines.
c.line(9,11,11,11,light)
c.set(8,12,light)
c.line(14,9,15,9,light)
c.line(13,14,15,14,light)
c.set(12,15,light)
c.line(6,16,7,16,light)
c.line(16,18,17,18,light)
c.line(10,21,11,21,mid)
c.set(8,19,mid)
# Far ear.
c.poly([(22,11),(24,7),(26,7),(26,11),(24,13)],rose)
c.line(24,9,24,11,pink)
# Side-facing head with a softly rounded muzzle.
c.ellipse(24,16,4,5,shadow)
c.ellipse(24,15,4,5,face)
c.ellipse(26,18,3,3,face)
c.line(25,21,27,21,shadow)
c.line(22,14,22,17,wool)
# Near ear droops gently to the left.
c.poly([(23,12),(20,11),(18,12),(19,15),(21,16),(23,14)],mid)
c.poly([(22,12),(19,12),(20,14),(21,15),(22,14)],pink)
c.set(20,13,rose)
# Wool cap sits over the forehead.
c.circle(24,10,3,wool)
c.circle(21,10,2,wool)
c.circle(26,11,2,wool)
c.line(23,8,25,8,light)
c.set(22,9,light)
# Gentle dark eye, tiny warm nose and cheek.
c.set(26,15,'#766f64')
c.set(26,16,'#766f64')
c.set(28,18,'#b3968c')
c.set(25,18,'#e2bfb0')
view(result)
finish(result)
