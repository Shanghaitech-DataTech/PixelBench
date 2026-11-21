result = new_canvas(32,32)
c=result
outline='#171d2b'
shadow='#303d50'
base='#54667a'
light='#a9becb'
shine='#dce8e9'
# Short sleeves and long armored tunic
pts=[(10,3),(12,3),(13,5),(18,5),(19,3),(21,3),(25,5),(28,10),(28,14),(24,16),(22,14),(22,26),(20,29),(11,29),(9,27),(9,14),(7,16),(3,14),(3,10),(6,5)]
c.poly(pts,outline)
c.poly([(10,5),(11,5),(13,7),(18,7),(20,5),(21,5),(24,7),(26,11),(26,13),(24,14),(21,11),(20,17),(21,26),(19,27),(12,27),(11,26),(11,12),(8,12),(7,14),(5,13),(5,10),(7,7)],base)
# Cool steel shadow planes
c.poly([(19,8),(21,6),(24,8),(26,12),(24,14),(21,11),(20,18),(21,26),(18,27),(18,12)],shadow)
c.poly([(10,12),(12,13),(12,26),(15,27),(11,27)],shadow)
# Staggered tiny open rings; alternating rows overlap
allowed={c.color(base),c.color(shadow)}
eligible={(x,y) for y in range(32) for x in range(32) if c.get(x,y) in allowed}
for y in range(7,27,3):
    for x in range(5+( ((y-7)//3)%2)*2,27,4):
        coords=[(x,y),(x+1,y),(x-1,y+1),(x+2,y+1),(x,y+2),(x+1,y+2)]
        if all(0<=a<32 and 0<=b<32 and (a,b) in eligible for a,b in coords):
            darkside=x>=18 or x<8
            for a,b in coords: c.set(a,b,'#778d9f' if darkside else light)
            c.set(x,y+1,outline)
            c.set(x+1,y+1,shadow)
            c.set(x,y+2,'#45576c')
            c.set(x+1,y+2,'#72899c')
            if not darkside:c.set(x,y,shine)
# Reinforced collar and shoulder edging
c.line(10,4,12,6,'#8195a8')
c.line(12,6,14,8,outline)
c.line(14,8,17,8,outline)
c.line(17,8,20,5,outline)
c.line(13,6,18,6,'#0e1520')
c.line(13,7,18,7,'#8195a8')
c.line(7,6,9,5,light)
c.line(21,5,24,7,'#8195a8')
# Cuff rims
c.line(4,13,7,15,outline)
c.line(4,12,7,14,'#91a6b6')
c.line(24,15,27,13,outline)
c.line(24,14,27,12,'#8195a8')
# Hem with small central split
c.line(11,28,14,28,'#8195a8')
c.line(17,28,20,28,'#8195a8')
c.line(15,27,15,29,outline)
c.set(16,29,None)
c.set(15,29,None)
view(c)
finish(result)
