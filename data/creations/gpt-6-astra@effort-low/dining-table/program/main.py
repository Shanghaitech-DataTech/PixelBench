result = new_canvas(64,64,name='family_dining_table')
c=result
O='#382728'; D='#704235'; M='#a56842'; W='#c78c53'; H='#edb975'; S='#875039'
# four chairs, two along each side of the table
for x in (14,38):
    # back pair feet and seat
    c.rect(x+1,14,3,13,O); c.rect(x+12,14,3,13,O)
    c.rect(x+2,15,1,10,M); c.rect(x+13,15,1,10,M)
    c.rect(x,10,16,12,O); c.rect(x+1,11,14,9,M)
    c.rect(x+2,12,12,5,W); c.line(x+2,12,x+13,12,H)
    # tall backrest with spindles
    c.rect(x,3,3,14,O); c.rect(x+13,3,3,14,O)
    c.rect(x+1,4,1,11,W); c.rect(x+14,4,1,11,W)
    c.rect(x+5,5,2,7,D); c.rect(x+9,5,2,7,D)
    c.rect(x,2,16,5,O); c.rect(x+1,3,14,3,W); c.line(x+2,3,x+13,3,H)
# table legs below apron
for x in (9,49):
    c.rect(x,37,5,16,O); c.rect(x+1,38,3,13,D); c.line(x+1,40,x+1,50,W)
# thick tabletop, bevel and apron
c.poly([(7,17),(56,17),(59,20),(59,40),(56,44),(7,44),(4,40),(4,20)],O)
c.rect(7,37,49,6,D); c.line(8,42,55,42,M)
c.poly([(7,16),(56,16),(59,19),(59,37),(56,40),(7,40),(4,37),(4,19)],O)
c.poly([(8,17),(55,17),(58,20),(58,36),(55,39),(8,39),(5,36),(5,20)],M)
c.poly([(8,18),(55,18),(57,20),(57,34),(54,37),(9,37),(6,34),(6,20)],W)
c.line(9,18,54,18,H); c.line(6,21,6,33,H)
# boards and intentional wood grain
for y in (24,31):
    c.line(7,y,56,y,M); c.line(8,y+1,55,y+1,'#d89c5e')
for x,y,l in [(10,21,9),(42,21,10),(9,28,8),(45,28,8),(12,34,9),(40,34,10)]:
    c.line(x,y,x+l,y,'#ad7548'); c.line(x+2,y+1,x+l-2,y+1,'#e1a665')
c.line(50,35,53,35,M)
# bowl shadow and ceramic bowl
c.ellipse(32,30,11,3,S)
c.ellipse(31,28,10,6,O)
c.ellipse(31,28,9,5,'#639b92')
c.ellipse(30,27,8,4,'#a9c7ab')
c.line(25,31,28,32,'#d9dfbc'); c.line(29,33,34,33,'#85b4a3')
c.ellipse(31,25,10,4,O); c.ellipse(31,25,9,3,'#e9dfaf'); c.ellipse(31,25,7,2,'#876448')
# fruit: orange, apple, pear and banana
c.circle(26,24,4,O); c.circle(26,24,3,'#e79839'); c.set(25,22,'#ffd277'); c.set(27,26,'#bf642e')
c.circle(32,23,4,O); c.circle(32,23,3,'#c74c3e'); c.rect(30,21,2,2,'#f48459'); c.line(32,19,33,17,D); c.line(33,19,36,18,'#638147')
c.poly([(35,25),(35,22),(37,20),(37,18),(39,18),(40,22),(42,24),(40,27),(37,27)],O)
c.poly([(36,24),(38,21),(38,19),(39,22),(41,24),(39,26),(37,26)],'#a3ae4b'); c.set(38,22,'#d4d379')
c.path('M 27 26 L 29 28 L 34 28 L 37 26 L 36 29 L 33 31 L 29 30 L 26 28 Z',O)
c.line(28,27,30,29,'#f4cc63'); c.line(30,29,33,29,'#f4cc63'); c.line(33,29,36,27,'#f4cc63')
# front chairs, seats and legs, overlapping table edge
for x in (14,38):
    c.rect(x,45,3,15,O); c.rect(x+13,45,3,15,O)
    c.line(x+1,47,x+1,58,W); c.line(x+14,47,x+14,58,M)
    c.rect(x-1,42,18,10,O); c.rect(x,43,16,7,M)
    c.rect(x+1,43,14,4,W); c.line(x+2,43,x+13,43,H)
    c.line(x+1,49,x+14,49,D)
    # back posts and open slatted back
    c.rect(x,46,3,12,O); c.rect(x+13,46,3,12,O)
    c.line(x+1,47,x+1,56,W); c.line(x+14,47,x+14,56,W)
    for dx in (5,9):
        c.rect(x+dx,48,2,8,O); c.line(x+dx,49,x+dx,54,M)
    c.rect(x-1,53,18,5,O); c.rect(x,54,16,3,M); c.line(x+1,54,x+14,54,H)
view(result)
finish(result)
