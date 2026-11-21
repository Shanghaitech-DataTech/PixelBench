# Frame one retains every input pixel on a shared, expanded canvas.
f1 = new_canvas(49, 52, name='original')
f1.blit(input_canvas, 5, 2)
f2 = new_canvas(49, 52, name='full_draw')
P = {e['name']:e['index'] for e in input_canvas.palette() if e['name']}
# Explicit original palette, kept throughout the redraw.
ink='#121311'; brown='#422110'; edge='#7b4231'; skin='#c5956a'; light='#f6d39b'; pale='#faf3c9'
green='#529439'; lime='#9cde5a'; forest='#304915'; olive='#4f7229'
steel='#687862'; shine='#a4b496'; dark='#252a23'; gray='#3c3c3c'; cream='#e1d4c2'
gold='#ffe75a'; amber='#df9859'; pink='#ef5ba1'; wine='#55002a'; magenta='#9e005d'
# Ground contact shadow for the wider stance.
f2.ellipse(23,47,21,3,'#17003599')
# Preserve the head, hair, quiver, tunic and coat from the original.
for y in range(41):
    xmax = 24 if y < 19 else 22
    for x in range(xmax+1):
        col=input_canvas.get(x,y)
        if input_canvas.palette()[col]['rgba'][3] == 0: continue
        dx=3 if y<19 else 4
        f2.set(x+dx,y+2,col)
# Braced rear leg, boot facing left.
f2.poly([(13,35),(19,36),(17,41),(13,46),(9,48),(3,48),(3,45),(8,42)],ink)
f2.poly([(13,36),(17,37),(14,42),(10,45),(6,46),(6,44),(10,41)],'#5d422f')
f2.poly([(13,37),(15,38),(12,42),(9,44),(7,44),(10,40)],'#d1b6a2')
f2.line(5,46,10,46,skin)
f2.line(4,48,10,48,brown)
f2.set(4,47,'#faf3c9')
# Forward leg spreads right, weight planted beneath the bow.
f2.poly([(23,35),(28,36),(29,40),(32,44),(36,46),(36,48),(27,48),(25,44),(22,40)],ink)
f2.poly([(24,37),(27,37),(27,41),(31,46),(34,46),(34,47),(28,47),(25,43)],'#5d422f')
f2.poly([(26,38),(27,40),(29,43),(28,45),(26,43),(24,39)],'#d1b6a2')
f2.line(29,46,33,46,skin)
f2.line(29,48,35,48,brown)
# Coat panels spread with the hips.
f2.poly([(15,29),(23,29),(27,35),(28,40),(23,42),(19,38),(16,42),(12,40)],ink)
f2.poly([(16,30),(20,30),(19,36),(16,40),(14,39)],gray)
f2.poly([(17,30),(19,31),(17,37),(15,38)],steel)
f2.poly([(21,30),(23,30),(26,36),(26,39),(23,40),(20,36)],steel)
f2.line(22,32,24,36,shine)
f2.poly([(21,36),(24,38),(24,40),(22,39)],dark)
f2.line(19,32,19,38,'#534338')
f2.rect(16,29,8,2,brown)
f2.rect(17,29,6,1,'#bc6c0c')
f2.rect(20,29,2,2,gold)
# Fully flexed bow silhouette. Limbs sweep far forward from the tips.
bow=[(33,3),(36,4),(38,7),(39,10),(42,13),(44,17),(46,22),(46,27),(44,31),(42,35),(40,38),(37,42),(33,44),(32,43),(35,40),(37,36),(39,32),(41,28),(42,24),(42,21),(41,17),(39,14),(36,11),(35,7),(32,5)]
f2.poly(bow,brown)
f2.path('M 33 4 L 35 5 L 37 9 L 38 12 L 41 15 L 43 19 L 44 23 L 44 27 L 42 31 L 40 35 L 38 39 L 35 42 L 33 43',amber,False)
f2.path('M 34 4 L 36 7 L 37 11 L 40 14 L 42 18 L 43 22 L 43 27 L 41 31 L 39 35 L 37 39 L 34 42',gold,False)
# Magenta bindings retain the original bow's ornament.
for x,y in [(40,14),(43,18),(41,30),(38,36)]:
    f2.line(x,y,x+1,y+2,wine)
    f2.line(x+1,y,x+2,y+1,pink)
f2.set(33,4,pale); f2.set(33,43,pale)
# Taut string reaches the anchor hand beside the jaw. No arrow.
f2.line(33,5,24,20,light)
f2.line(24,20,33,42,light)
# Straight bow arm: shoulder, sleeve, forearm and gripping hand.
f2.poly([(22,20),(26,20),(30,21),(40,21),(42,20),(45,21),(45,25),(41,26),(29,25),(26,26),(22,25)],ink)
f2.poly([(23,21),(26,21),(29,22),(29,24),(26,25),(23,24)],steel)
f2.line(24,21,27,22,shine)
f2.line(23,22,23,24,gray)
f2.poly([(29,22),(39,22),(40,24),(30,24)],skin)
f2.line(30,22,39,22,light)
# Bracer with small metallic edges.
f2.rect(34,21,6,4,gray)
f2.rect(35,21,4,2,steel)
f2.line(35,21,38,21,shine)
f2.line(39,22,39,24,cream)
f2.line(34,22,34,24,brown)
f2.rect(42,20,2,7,brown)
f2.poly([(40,22),(41,21),(43,21),(44,22),(44,24),(42,25),(40,24)],skin)
f2.line(41,21,43,21,pale)
f2.line(41,22,43,22,light)
f2.set(44,23,edge)
f2.line(41,24,42,24,edge)
# Drawing arm: elbow pulled behind the torso, hand anchored at the cheek.
f2.poly([(18,21),(21,22),(18,25),(13,27),(9,25),(10,22),(15,20)],ink)
f2.poly([(17,21),(20,22),(17,24),(13,25),(11,24),(12,22)],steel)
f2.line(12,22,15,21,shine)
f2.line(11,24,13,25,gray)
# Raised forearm runs back up from the rear elbow to the string hand.
f2.poly([(10,23),(12,26),(16,24),(22,21),(25,21),(26,19),(24,17),(22,17),(20,19),(15,21)],brown)
f2.poly([(12,23),(13,24),(17,22),(21,20),(22,18),(24,18),(24,20),(21,21),(17,23),(13,25)],skin)
f2.line(13,23,21,19,light)
f2.poly([(13,22),(15,21),(18,23),(15,25),(13,25)],gray)
f2.line(14,22,16,21,shine)
f2.line(15,23,17,22,steel)
f2.set(15,24,steel)
f2.line(22,18,24,18,pale)
f2.line(22,19,24,19,light)
f2.set(24,20,edge)
# Small armor facets and boot seams echo the source's pixel texture.
f2.line(15,32,16,31,shine)
f2.set(16,34,shine)
f2.line(14,36,14,38,'#313b31')
f2.line(18,35,17,38,'#534338')
f2.set(15,40,'#48382f')
f2.line(23,33,24,35,shine)
f2.set(25,36,'#a4b496')
f2.line(24,37,25,38,'#3c3c3c')
f2.set(22,38,'#313b31')
f2.set(23,40,'#534338')
f2.line(11,42,13,40,skin)
f2.line(9,44,11,43,'#5d422f')
f2.set(7,46,'#d1b6a2')
f2.line(27,43,28,44,skin)
f2.set(31,46,'#d1b6a2')
f2.set(33,47,'#7b4231')
view(f1,scale=8)
view(f2,scale=8)
finish([f1,f2])
