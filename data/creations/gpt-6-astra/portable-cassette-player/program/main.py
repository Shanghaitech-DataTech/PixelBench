result = new_canvas(32, 32, name='portable_cassette_player')
c = result
ink='#192333'
shadow='#334354'
steel='#62788a'
light='#bbd0d5'
cream='#e9ead8'
body='#df9b46'
bright='#f6c66a'
darkgold='#ae6534'
# Headphone cord, with a loose loop to the right of the player.
c.path('M 23 5 L 26 5 Q 29 5 29 8 L 29 22 Q 29 26 27 27 L 26 27 Q 25 27 25 25 L 25 22', ink, fill=False)
c.line(30,9,30,20,steel)
c.line(29,22,28,24,steel)
# Top playback keys and volume wheel.
c.rect(6,3,5,3,ink)
c.rect(7,3,3,1,light)
c.rect(12,3,4,3,ink)
c.rect(13,3,2,1,'#e57057')
c.rect(17,3,4,3,ink)
c.rect(18,3,2,1,light)
c.rect(21,4,3,3,ink)
c.set(22,4,steel)
# Case silhouette and stepped corners.
c.rect(4,5,19,25,ink)
c.rect(3,7,21,21,ink)
c.rect(5,6,17,23,body)
c.rect(4,8,19,19,body)
c.rect(5,6,17,1,bright)
c.rect(4,8,1,18,bright)
c.rect(22,8,1,19,darkgold)
c.rect(5,27,17,2,darkgold)
c.rect(6,28,15,1,'#c27b39')
# Small headphone jack at shoulder.
c.rect(23,5,3,3,ink)
c.rect(24,5,1,2,light)
# Cassette door bezel.
c.rect(6,9,15,14,darkgold)
c.rect(5,10,17,12,darkgold)
c.rect(6,9,15,1,bright)
c.rect(6,10,15,12,ink)
c.rect(7,11,13,10,steel)
# Smoked transparent window, showing the cassette inside.
c.rect(7,11,13,9,'#749a9f')
c.rect(8,12,11,7,'#38555e')
c.rect(8,12,11,2,'#a4bec0')
# Tape span and two exposed spool hubs.
c.rect(9,15,9,2,ink)
for x in (10,17):
    c.circle(x,15,3,ink)
    c.circle(x,15,2,cream)
    c.set(x,15,shadow)
    c.set(x,13,light)
    c.set(x-2,15,steel)
    c.set(x+1,16,steel)
c.line(11,18,16,18,'#c19d6e')
c.rect(11,19,6,1,ink)
c.rect(12,19,4,1,light)
# Glass glints and lower frame.
c.line(7,11,10,11,'#d9ece5')
c.set(7,12,'#d9ece5')
c.line(18,20,19,19,'#a4bec0')
c.rect(7,21,13,1,shadow)
# Front transport symbols: play, stop, and rewind.
c.poly([(7,24),(7,27),(10,25)],ink)
c.rect(12,24,3,3,ink)
c.line(17,25,19,24,ink)
c.line(17,25,19,26,ink)
# Recessed volume thumbwheel on the right side.
c.rect(22,12,3,8,ink)
c.rect(23,13,1,6,steel)
for y in (13,15,17): c.set(23,y,light)
# Case screws and signal indicator.
c.set(6,7,cream)
c.set(20,7,ink)
c.set(20,8,'#9ecb8a')
c.set(6,27,light)
c.set(20,27,shadow)
view(result, scale=12)
finish(result)
