result = new_canvas(32,32)
c=result
ink='#182435'
shade='#304357'
mid='#53738a'
light='#9bbbc7'
cream='#e3e4cf'
# cable behind player, curling to the right
c.path('M 23 7 L 26 7 Q 29 7 29 10 L 29 23 Q 29 28 26 28 L 25 28',ink,fill=False)
c.line(30,11,30,22,mid)
c.rect(24,27,3,2,ink)
c.rect(23,27,2,2,light)
# top transport keys
c.rect(6,3,5,3,ink)
c.rect(7,3,3,1,cream)
c.rect(12,3,4,3,ink)
c.rect(13,3,2,1,light)
c.rect(17,3,4,3,ink)
c.rect(18,3,2,1,light)
# case stepped silhouette
c.rect(5,5,18,25,ink)
c.rect(4,7,20,21,ink)
c.rect(6,6,16,23,mid)
c.rect(5,8,18,19,mid)
c.rect(6,6,15,1,light)
c.line(5,8,5,26,light)
c.rect(21,8,2,19,shade)
c.rect(7,28,14,1,shade)
# upper label and headphone plug
c.rect(7,8,9,1,cream)
c.rect(18,8,2,1,'#efb75d')
c.rect(22,5,3,3,ink)
c.rect(23,5,1,2,light)
# glazed window bevel
c.rect(6,10,15,12,ink)
c.rect(7,11,13,10,light)
c.rect(8,12,11,8,'#243e50')
# cassette body visible through glass
c.rect(8,13,11,5,'#507c85')
c.rect(9,18,9,2,'#355665')
c.line(10,18,16,18,ink)
# two spools
for x in (10,16):
 c.circle(x,15,2,cream)
 c.set(x,15,ink)
 c.set(x,13,light)
 c.set(x+1,16,light)
c.line(11,17,15,17,'#b2b6a4')
# glass gleams
c.line(8,12,10,12,'#c1e3df')
c.set(8,13,'#c1e3df')
c.line(17,19,18,18,'#81acb6')
# lower control panel play stop and rewind
c.rect(7,23,10,4,shade)
c.line(8,24,8,26,cream)
c.set(9,25,cream)
c.rect(12,24,2,2,cream)
c.line(15,24,15,26,light)
# volume wheel at lower right
c.rect(18,23,3,5,ink)
c.rect(19,23,1,5,light)
for y in (23,25,27): c.set(20,y,mid)
# bottom trim and screw
c.set(7,28,light)
c.set(20,28,light)
view(c)
finish(result)
