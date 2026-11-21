result = new_canvas(32,32,name='chainmail_armor')
outline='#171d2b'
shadow='#303b50'
steel='#566b80'
mid='#7f98a8'
light='#b6cbd0'
glint='#e3eded'
# Short-sleeved hauberk silhouette and dark edge.
shape=[(10,3),(12,3),(13,5),(18,5),(19,3),(21,3),(22,4),(25,5),(26,7),(29,12),(29,15),(24,18),(22,16),(22,27),(21,29),(10,29),(9,27),(9,16),(7,18),(2,15),(2,12),(5,7),(6,5),(9,4)]
result.poly(shape,outline)
result.poly([(10,5),(12,6),(19,6),(21,5),(24,7),(27,12),(27,14),(24,16),(21,13),(20,27),(11,27),(10,13),(7,16),(4,14),(4,12),(7,7)],steel)
# Metal body: deep side folds and a brighter central plane.
result.poly([(10,9),(13,8),(19,8),(21,10),(20,27),(11,27)],mid)
result.poly([(10,12),(12,14),(12,27),(10,27)],shadow)
result.poly([(19,12),(21,10),(21,27),(18,27)],steel)
# Ring links follow staggered rows; holes and paired highlights imply woven loops.
fabric = result.copy(name='fabric_template')
for y in range(6,26,3):
    for x in range(4 + (1 if ((y-6)//3)%2 else 0),28,3):
        # Only place whole links within the steel fabric.
        pts=[(x,y),(x-1,y+1),(x+1,y+1),(x,y+2)]
        allowed=[steel,mid,shadow]
        ids=[result.color(v) for v in allowed]
        if all(fabric.get(px,py) in ids for px,py in pts):
            bright = light if 11<=x<=18 else mid
            base = steel if 12<=x<=18 else shadow
            result.set(x,y,bright)
            result.set(x-1,y+1,bright)
            result.set(x,y+1,shadow)
            result.set(x+1,y+1,base)
            result.set(x,y+2,base)
            if y<13 and 11<=x<=17: result.set(x,y,glint)
# Reinforced neck opening, dark interior, pale steel rim.
result.poly([(10,4),(12,3),(13,5),(18,5),(19,3),(21,4),(20,8),(18,10),(13,10),(11,8)],outline)
result.line(11,4,12,7,light)
result.line(12,7,14,9,mid)
result.line(14,9,17,9,light)
result.line(18,8,20,5,steel)
result.line(14,6,17,6,'#252e40')
# Bound sleeve cuffs and bottom hem.
result.line(3,14,7,17,outline)
result.line(4,13,7,15,light)
result.line(24,17,28,14,outline)
result.line(24,15,27,13,mid)
result.line(11,28,20,28,shadow)
result.line(11,27,20,27,mid)
for x in [12,15,18]: result.set(x,27,light)
view(result)
finish(result)
