result = new_canvas(32,32,name='chainmail')
o='#171e2b'; dark='#303d50'; mid='#596e80'; light='#9fb8c7'; hi='#d8e6e8'
# short sleeved mail hauberk silhouette
pts=[(10,3),(12,3),(13,5),(18,5),(19,3),(21,3),(25,5),(27,8),(29,13),(29,15),(24,18),(22,17),(22,27),(20,29),(11,29),(9,27),(9,17),(7,18),(2,15),(2,13),(4,8),(6,5)]
result.poly(pts,o)
result.poly([(10,4),(12,5),(13,7),(18,7),(20,4),(24,6),(26,9),(28,14),(24,16),(21,14),(21,26),(19,28),(12,28),(10,26),(10,14),(7,16),(3,14),(5,9),(7,6)],mid)
# Ring mesh: staggered loops, shared links, preserved silhouette
base=result.copy(name='mesh mask')
for y in range(6,28,3):
    for x in range(3+(1 if (y//3)%2 else 0),29,3):
        ring=[(0,0,dark),(1,0,light),(-1,1,light),(0,1,dark),(1,1,o),(2,1,mid),(0,2,mid),(1,2,light)]
        for dx,dy,col in ring:
            xx,yy=x+dx,y+dy
            if 0<=xx<32 and 0<=yy<32 and base.get(xx,yy)==base.color(mid):
                # darker rings on right and under sleeve
                if xx>=19 or yy>=25:
                    col={light:mid,mid:dark}.get(col,col)
                result.set(xx,yy,col)
# shoulder highlights and reinforced seams
result.line(7,6,10,4,light)
result.line(21,4,24,6,mid)
result.line(5,10,3,14,dark)
result.line(3,15,7,17,o)
result.line(4,14,7,16,light)
result.line(25,15,28,13,mid)
result.line(24,17,28,15,o)
result.line(9,12,9,16,dark)
result.line(22,11,22,16,o)
# dark neck opening, rim
result.poly([(11,3),(13,4),(14,5),(17,5),(19,3),(21,3),(20,7),(18,9),(13,9),(11,7)],o)
result.line(11,4,12,7,light)
result.line(12,7,14,8,mid)
result.line(14,9,17,9,light)
result.line(18,8,20,5,mid)
# tiny bright catches on links
for x,y in [(7,8),(10,10),(13,11),(12,14),(15,17),(12,20)]:
    result.set(x,y,hi)
# weighted hem and center vent
result.line(11,28,14,28,mid)
result.line(17,28,20,28,dark)
result.line(15,27,15,29,o)
result.set(15,29,None)
result.set(16,29,None)
view(result)
finish(result)
