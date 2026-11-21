result = new_canvas(64,64, name='family_dining_table')
c=result
O='#30252b'
D='#593731'
S='#80503b'
W='#aa6c45'
L='#d69759'
H='#efbc77'
# Chair silhouettes and warm inset backrests.
def chair_top(x,y):
    c.rect(x+1,y+1,13,18,O)
    c.rect(x,y+2,15,7,O)
    c.rect(x+2,y+2,11,5,W)
    c.line(x+3,y+2,x+11,y+2,H)
    c.rect(x+3,y+7,2,5,D)
    c.rect(x+10,y+7,2,5,D)
    c.rect(x+2,y+11,11,6,S)
    c.rect(x+3,y+11,9,3,L)
    c.line(x+3,y+14,x+11,y+14,W)
    c.rect(x+2,y+17,3,3,O)
    c.rect(x+10,y+17,3,3,O)
chair_top(17,3)
chair_top(35,3)
# Table legs visible below the apron.
for x in (12,46):
    c.rect(x,39,6,12,O)
    c.rect(x+1,40,3,9,S)
    c.line(x+1,43,x+1,48,L)
# Thick apron and rounded stepped tabletop.
c.rect(9,23,46,22,O)
c.rect(11,40,42,5,O)
c.rect(12,40,40,3,D)
c.line(13,41,50,41,S)
c.poly([(12,17),(51,17),(55,21),(55,38),(51,42),(12,42),(8,38),(8,21)],O)
c.poly([(12,18),(51,18),(54,21),(54,36),(50,40),(13,40),(9,36),(9,21)],W)
c.poly([(13,18),(50,18),(53,21),(53,34),(50,37),(13,37),(10,34),(10,21)],L)
c.line(14,19,49,19,H)
c.line(11,22,11,32,H)
c.line(14,37,49,37,S)
c.line(14,39,49,39,L)
# Individual boards and selected grain marks.
for y in (24,30):
    c.line(11,y,52,y,W)
    c.line(12,y+1,51,y+1,'#df9f60')
c.line(16,21,24,21,W)
c.line(18,22,22,22,H)
c.line(41,21,47,21,W)
c.line(14,28,19,28,W)
c.line(44,27,50,27,W)
c.line(16,34,23,34,W)
c.line(39,34,47,34,W)
c.line(42,35,46,35,H)
# Centerpiece bowl, with an outlined rim, fruit, and glazed front.
c.ellipse(32,29,10,5,D)
c.ellipse(32,28,10,5,O)
c.ellipse(32,27,9,4,'#f7dca0')
c.ellipse(32,27,7,3,'#956348')
# Bananas behind the apples.
c.path('M 30 23 Q 35 25 38 21 L 40 22 Q 37 29 30 26 Z','#6e502e')
c.path('M 31 23 Q 35 26 38 22 L 39 23 Q 36 28 31 25 Z','#f5cb55')
c.set(38,21,O)
# Pear.
c.poly([(27,22),(27,20),(29,19),(31,21),(31,23),(33,25),(32,28),(27,28),(25,26)],'#526139')
c.poly([(28,21),(29,21),(30,24),(31,25),(30,27),(27,26),(27,24)],'#a8b95b')
c.set(28,19,D)
c.set(28,23,'#d7d97b')
# Apples and orange.
c.circle(34,25,3,'#a53d3b')
c.circle(34,24,2,'#d95e48')
c.set(33,23,'#f69b68')
c.line(34,22,35,21,D)
c.line(36,22,38,21,'#6d8847')
c.circle(29,27,3,'#a93e3c')
c.circle(28,26,2,'#e76d51')
c.set(27,25,'#ffc18a')
c.set(29,23,D)
c.circle(38,27,2,'#dc873d')
c.set(38,26,'#ffd16b')
# The bowl's front overlaps the lower edges of the fruit.
c.poly([(23,28),(26,30),(38,30),(41,28),(39,33),(36,35),(28,35),(25,33)],O)
c.poly([(25,29),(28,31),(37,31),(39,29),(38,32),(35,34),(29,34),(26,32)],'#7b9d92')
c.line(27,30,37,30,'#d8e5b8')
c.line(28,32,35,33,'#acd0b3')
c.line(29,34,35,34,'#4e706a')
# Two foreground chairs. Back rails and open slats read clearly against the table.
def chair_front(x,y):
    c.rect(x+2,y+5,3,15,O)
    c.rect(x+11,y+5,3,15,O)
    c.rect(x+3,y+12,1,6,L)
    c.rect(x+12,y+12,1,6,S)
    c.rect(x+1,y+2,14,10,O)
    c.rect(x+2,y+3,12,7,W)
    c.rect(x+3,y+3,10,4,L)
    c.line(x+4,y+3,x+11,y+3,H)
    # Rear posts and floating back rail.
    c.rect(x+1,y-4,3,14,O)
    c.rect(x+12,y-4,3,14,O)
    c.line(x+2,y-2,x+2,y+8,L)
    c.line(x+13,y-2,x+13,y+8,S)
    c.rect(x,y-6,16,7,O)
    c.rect(x+1,y-5,14,4,W)
    c.line(x+2,y-5,x+13,y-5,H)
    c.line(x+3,y-3,x+11,y-3,L)
    c.rect(x+6,y,3,4,O)
    c.line(x+7,y,x+7,y+3,W)
chair_front(16,42)
chair_front(35,42)
view(result)
finish(result)
