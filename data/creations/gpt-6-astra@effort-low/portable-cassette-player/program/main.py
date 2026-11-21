result = new_canvas(32,32)
c=result
ink='#172536'
shadow='#34485c'
metal='#7794a5'
light='#c4dce0'
cream='#edf1db'
orange='#ee9b48'
# headphone cable, curling around the right side
c.path('M 24 7 L 27 7 Q 30 7 30 11 L 30 25 Q 30 29 27 29 Q 25 29 25 27 L 25 23',ink,fill=False)
c.line(31,11,31,24,metal)
# plug
c.rect(24,20,3,5,ink)
c.rect(25,20,1,3,metal)
c.line(25,18,25,19,cream)
# chassis
c.rect(4,4,20,25,ink)
c.rect(3,6,22,21,ink)
c.rect(5,5,18,23,metal)
c.rect(4,7,20,19,metal)
c.rect(5,6,17,1,light)
c.rect(4,8,1,17,light)
c.rect(22,7,2,19,shadow)
c.rect(6,27,16,1,shadow)
# top transport keys
c.rect(6,2,5,3,ink)
c.rect(7,2,3,2,orange)
c.rect(12,3,4,2,ink)
c.rect(13,3,2,1,light)
c.rect(17,3,4,2,ink)
c.rect(18,3,2,1,light)
# window bezel and dark translucent glass
c.rect(6,8,15,12,ink)
c.rect(7,9,13,10,'#304f61')
c.rect(7,9,13,1,'#52798a')
# visible cassette silhouette
c.rect(8,11,11,7,'#6b8d96')
c.rect(9,10,9,1,'#a3bdba')
c.rect(9,17,9,1,light)
# tape connecting reels
c.rect(10,13,7,3,ink)
for x in (10,17):
    c.circle(x,13,3,ink)
    c.circle(x,13,2,cream)
    c.set(x,13,shadow)
    c.set(x,11,metal)
    c.set(x,15,metal)
c.rect(12,16,4,2,shadow)
c.rect(13,16,2,1,light)
# glass glints
c.line(7,10,9,8,light)
c.set(19,18,'#a3bdba')
# control row
c.rect(6,22,10,4,ink)
c.poly([(8,23),(8,25),(10,24)],cream)
c.rect(12,23,2,2,orange)
# volume wheel
c.circle(19,23,3,ink)
c.circle(19,23,2,light)
c.circle(19,23,1,metal)
c.line(19,21,19,22,cream)
# tiny labels and screws
c.line(7,21,11,21,light)
c.line(17,19,19,19,metal)
c.set(5,7,ink)
c.set(21,26,ink)
view(result)
finish(result)
