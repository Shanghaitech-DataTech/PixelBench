result = new_canvas(32,32)
c=result
ink='#181b28'; edge='#343747'; steel='#8c9aab'; light='#d3dedc'; shine='#f3efd8'; leather='#59433e'; mid='#76584a'; dark='#382e32'
# silhouette and top fittings
c.rect(23,6,5,3,ink).rect(24,6,3,1,light).rect(24,7,3,1,steel)
c.rect(5,7,5,2,ink).rect(6,7,3,1,steel)
c.poly([(11,9),(13,5),(20,5),(22,9)],ink)
c.poly([(13,8),(14,6),(19,6),(20,8)],steel)
c.rect(3,9,26,17,ink).rect(2,11,28,13,ink)
c.rect(4,10,24,14,steel)
c.line(5,10,26,10,light)
c.rect(4,14,24,10,dark)
c.rect(4,15,23,8,leather)
c.line(5,24,26,24,edge)
c.line(6,25,25,25,ink)
# leather pebbled texture
for y in range(15,23):
    for x in range(5,27):
        if (x*3+y*5)%7==0: c.set(x,y,mid)
        elif (x+y*3)%8==0: c.set(x,y,dark)
c.line(4,15,4,22,mid)
c.line(27,15,27,23,dark)
# top face finder and badge
c.rect(6,11,5,3,ink).rect(7,11,3,2,'#49737c').set(7,11,'#b6d9cf')
c.rect(23,11,3,2,ink).rect(24,11,2,1,shine)
c.set(5,12,light)
# lens cast shadow
c.ellipse(17,20,8,7,dark)
# lens stepped barrel
c.circle(16,18,8,ink)
c.circle(16,18,7,steel)
c.circle(16,18,6,edge)
c.line(12,12,15,11,light)
c.line(10,15,10,18,light)
c.line(21,21,19,23,'#627485')
c.circle(16,18,5,ink)
c.circle(16,18,4,'#24434f')
c.poly([(13,16),(15,14),(18,15),(19,17),(16,17),(14,20),(12,19)],'#397780')
c.poly([(17,17),(20,17),(19,21),(16,22),(14,20)],'#192c42')
c.line(14,15,16,14,'#a2e2d8')
c.set(13,16,'#d3f3e3')
c.line(17,21,19,19,'#488c99')
c.set(18,20,'#73b9b5')
# tiny body rivets and strap lugs
c.set(5,23,steel).set(26,23,steel)
c.rect(1,12,2,4,ink).set(1,13,steel)
c.rect(29,12,2,4,ink).set(30,13,steel)
view(result)
finish(result)
