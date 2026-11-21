output=input_canvas.copy(name='output')
c=output
shadow='#147c99'
blue='#21aec7'
light='#69dbe3'
white='#c7f6ed'
# Jet around the existing finial.
c.line(31,1,31,8,blue)
c.line(32,2,32,9,light)
c.set(31,0,white)
c.poly([(30,2),(28,3),(26,6),(25,9),(26,10),(28,6),(30,4)],blue)
c.line(29,3,27,6,light)
c.poly([(33,3),(35,4),(37,7),(38,10),(36,10),(35,7),(33,5)],blue)
c.line(34,4,36,7,light)
c.set(26,4,light)
c.set(38,6,white)
# Short overflows from the small bowl to the middle tier.
for x,y,end in [(24,13,20),(38,13,20),(19,23,29),(43,23,29)]:
    c.rect(x,y,3,end-y,shadow)
    c.rect(x,y,2,end-y,blue)
    c.line(x,y,x,end-2,light)
    c.set(x,y,white)
    c.line(x-1,end,x+3,end,blue)
    c.line(x,end-1,x+2,end-1,light)
    c.set(x-2,end-2,light)
# Long falling ribbons from the largest upper basin into the reservoir.
for x,dx in [(16,-1),(46,1)]:
    c.poly([(x,31),(x+3,31),(x+3,36),(x+dx+3,43),(x+dx+3,49),(x+dx,50),(x+dx,43),(x,36)],shadow)
    c.poly([(x,31),(x+2,31),(x+2,37),(x+dx+2,44),(x+dx+2,49),(x+dx,49),(x+dx,43),(x,36)],blue)
    c.line(x,32,x,38,light)
    c.line(x+dx,40,x+dx,46,light)
    c.line(x+1,32,x+1,34,white)
    c.set(x+dx,48,white)
    c.line(x+dx-2,50,x+dx+4,50,light)
    c.line(x+dx-3,51,x+dx-1,51,blue)
    c.line(x+dx+3,51,x+dx+5,51,blue)
    c.line(x+dx-2,47,x+dx-1,48,light)
    c.set(x+dx+4,47,white)
    c.set(x+dx-3,45,light)
# Bright ripples and beads on the tier pools.
for x,y,w in [(28,11,3),(33,10,2),(28,21,5),(35,20,3),(22,30,4),(35,31,5),(23,54,5),(35,53,4)]:
    c.line(x,y,x+w-1,y,light)
c.set(14,39,light)
c.set(50,41,light)
view(output)
finish(output)
