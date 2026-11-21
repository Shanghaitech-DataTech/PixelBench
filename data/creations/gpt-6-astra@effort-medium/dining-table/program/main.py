result = new_canvas(64,64,name='family_dining_table')
c=result
O='#30212a'; D='#623c36'; S='#89503b'; W='#b77749'; L='#dfa365'; H='#f3c583'; R='#a96140'
# Four chairs, two at each long side. Rear chair backs rise above table.
for x in (13,37):
    # rear legs and seat
    c.rect(x+2,17,3,13,O); c.rect(x+13,17,3,13,O)
    c.rect(x,13,18,13,O); c.rect(x+1,14,16,10,D)
    c.rect(x+2,15,14,7,W); c.line(x+3,15,x+14,15,L)
    # back silhouette, curved stepped top
    c.rect(x,5,18,13,O); c.rect(x+2,3,14,3,O)
    c.rect(x+1,6,16,10,S); c.rect(x+3,4,12,3,W)
    c.line(x+3,5,x+14,5,H)
    c.rect(x+3,8,12,5,O)
    c.rect(x+4,8,2,5,L); c.rect(x+8,8,2,5,W); c.rect(x+12,8,2,5,W)
    c.line(x+2,15,x+15,15,L)
# Table legs behind tabletop
for x in (8,50):
    c.rect(x,35,6,15,O); c.rect(x+1,36,3,12,S); c.line(x+1,38,x+1,46,L)
# deep apron
c.rect(5,21,54,19,O)
c.rect(7,27,50,12,D)
c.rect(8,35,48,3,S)
c.line(9,36,54,36,W)
# tabletop beveled corners
c.poly([(8,16),(55,16),(59,20),(59,33),(56,36),(7,36),(4,33),(4,20)],O)
c.poly([(8,17),(55,17),(58,20),(58,32),(55,34),(8,34),(5,32),(5,20)],W)
c.line(8,17,54,17,H); c.line(6,20,6,31,L)
c.line(8,33,55,33,S); c.line(56,21,56,31,L)
# plank edges and tidy wood grain
for y in (22,28):
    c.line(7,y,55,y,R); c.line(8,y+1,54,y+1,L)
for x,y,n in [(10,19,9),(40,19,9),(10,25,7),(43,25,9),(12,31,11),(38,31,12)]:
    c.line(x,y,x+n,y,W if y==19 else R)
c.line(15,19,22,19,L); c.line(43,20,50,20,H)
c.line(10,24,15,24,H); c.line(44,30,52,30,H)
# little central linen runner
c.poly([(25,18),(38,18),(41,33),(23,33)],'#af6660')
c.line(26,18,24,32,'#e5a37e'); c.line(37,18,40,32,'#e5a37e')
c.line(27,31,36,31,'#f0be93')
# fruit bowl shadow
c.ellipse(32,27,9,3,D)
# ceramic bowl silhouette
c.ellipse(32,24,9,4,O)
c.poly([(23,24),(41,24),(38,29),(35,31),(29,31),(26,29)],O)
c.poly([(24,24),(40,24),(37,29),(29,29),(26,27)],'#63958b')
c.line(28,28,36,28,'#a6c7ae'); c.line(30,30,35,30,'#46706e')
# fruit
c.circle(28,22,3,O); c.circle(28,21,2,'#d35b45'); c.set(27,20,'#ff9a68')
c.circle(34,21,3,O); c.circle(34,21,2,'#e6a140'); c.set(33,20,'#ffcf65')
c.circle(37,24,2,'#739448'); c.set(36,23,'#b2c66b')
c.line(29,18,29,19,D); c.line(34,17,34,18,D); c.line(30,18,32,17,'#698b48')
# banana cluster
c.line(25,23,27,25,'#f6ce69'); c.line(27,25,31,25,'#f6ce69'); c.line(31,25,32,23,'#f6ce69')
c.line(27,26,31,26,'#bd863c')
c.line(24,26,26,28,'#c6d7b7'); c.line(27,29,35,29,'#94b9a1')
# foreground chairs, separated from tabletop by seat and uprights
for x in (13,37):
    c.rect(x+1,43,4,16,O); c.rect(x+13,43,4,16,O)
    c.rect(x+2,48,2,9,W); c.rect(x+14,48,2,9,S)
    c.poly([(x,39),(x+3,35),(x+14,35),(x+18,39),(x+18,49),(x,49)],O)
    c.poly([(x+1,39),(x+4,36),(x+13,36),(x+16,39),(x+16,46),(x+1,46)],W)
    c.line(x+4,37,x+13,37,H)
    c.rect(x+2,40,14,7,'#c78c59')
    c.line(x+3,41,x+14,41,L)
    # back posts and cutout
    c.rect(x,42,3,13,O); c.rect(x+15,42,3,13,O)
    c.rect(x+1,43,1,10,L); c.rect(x+16,43,1,10,W)
    c.rect(x+5,45,3,8,O); c.rect(x+10,45,3,8,O)
    c.line(x+6,46,x+6,51,W); c.line(x+11,46,x+11,51,W)
    # broad back crest at front
    c.rect(x,51,18,5,O); c.rect(x+2,55,14,2,O)
    c.rect(x+1,52,16,3,S); c.line(x+2,52,x+15,52,L)
    c.line(x+4,54,x+13,54,W)
view(result)
finish(result)
