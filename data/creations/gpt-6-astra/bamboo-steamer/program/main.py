result = new_canvas(32, 32, name='bamboo_steamer')
c=result
edge='#65432e'
shadow='#946039'
mid='#bf884a'
gold='#dda75d'
light='#f4ca7d'
# small rising steam, separated from the lid
c.line(23,2,23,3,'#bfd5d4')
c.line(23,3,22,4,'#bfd5d4')
c.line(22,4,22,5,'#e4eeE5')
c.line(27,5,27,6,'#bfd5d4')
c.set(26,7,'#e4eee5')
# tilted lid behind the open basket
c.poly([(3,11),(4,8),(8,5),(15,3),(19,4),(22,7),(21,10),(17,12),(8,15),(4,14)],edge)
c.poly([(4,10),(8,7),(15,4),(18,5),(20,7),(17,9),(8,12),(4,12)],gold)
c.line(6,9,15,5,light)
c.line(6,11,18,6,shadow)
c.line(9,11,19,7,light)
c.line(10,7,13,10,mid)
c.line(14,5,17,8,mid)
# substantial lower lid lip
c.line(5,13,9,13,mid)
c.line(9,13,20,9,gold)
c.line(7,14,18,11,shadow)
# lid knob
c.poly([(10,5),(10,3),(13,2),(15,3),(15,4),(12,6)],edge)
c.line(11,3,13,3,light)
c.line(11,4,14,4,mid)
# basket body silhouette
c.poly([(2,18),(4,15),(9,13),(22,13),(27,15),(29,18),(28,26),(25,29),(20,30),(10,30),(5,28),(3,25)],edge)
c.poly([(3,19),(28,19),(27,26),(24,28),(19,29),(10,29),(6,27),(4,25)],mid)
c.poly([(4,20),(10,23),(21,23),(27,20),(26,25),(23,27),(11,28),(6,25)],gold)
# vertical bamboo staves
for x,y in [(6,22),(10,24),(15,24),(20,24),(25,22)]:
    c.line(x,y,x,y+3,shadow)
    c.line(x+1,y,x+1,y+2,light)
c.line(9,28,20,28,shadow)
c.line(11,29,19,29,gold)
# dark open interior and back rim
c.ellipse(15,18,13,5,shadow)
c.ellipse(15,17,12,4,light)
c.ellipse(15,18,11,4,'#795338')
c.ellipse(15,19,10,3,'#a27847')
# three individually outlined dumplings
def dumpling(cx,cy):
    c.poly([(cx-4,cy+2),(cx-4,cy),(cx-2,cy-3),(cx,cy-4),(cx+2,cy-3),(cx+4,cy),(cx+4,cy+2),(cx+2,cy+3),(cx-2,cy+3)],'#88674a')
    c.poly([(cx-3,cy+1),(cx-3,cy),(cx-1,cy-3),(cx+1,cy-3),(cx+3,cy),(cx+3,cy+1),(cx+1,cy+2),(cx-2,cy+2)],'#f7e7ba')
    c.line(cx-2,cy+2,cx+2,cy+2,'#d8bd87')
    c.line(cx-1,cy-2,cx-1,cy,'#d8bd87')
    c.line(cx+1,cy-2,cx+2,cy,'#d8bd87')
    c.set(cx,cy-3,'#fff6da')
    c.line(cx-2,cy,cx-1,cy+1,'#fff6da')
dumpling(15,15)
dumpling(8,18)
dumpling(23,18)
# foreground rim embraces dumplings without obscuring their tops
c.path('M 3 19 L 5 21 L 10 23 L 21 23 L 26 21 L 28 19 L 28 21 L 25 23 L 21 25 L 10 25 L 5 23 L 3 21 Z',shadow)
c.line(4,20,7,22,light)
c.line(7,22,11,23,light)
c.line(11,23,20,23,light)
c.line(20,23,25,21,light)
c.line(25,21,27,19,gold)
c.line(11,25,20,25,mid)
view(result)
finish(result)
