result = new_canvas(32, 32, name='portable_cassette_player')
c = result
ink='#182333'
shadow='#354455'
steel='#748899'
light='#c5d8d9'
cream='#f1e9cc'
# headphone lead, running from the top jack down the right side
c.path('M 22 5 L 22 3 Q 22 1 25 1 L 27 1 Q 30 1 30 4 L 30 23 Q 30 27 27 27 L 26 27',ink,fill=False)
c.line(29,4,29,22,steel)
c.rect(21,3,3,3,ink)
c.rect(22,3,1,2,light)
# top transport keys
c.rect(5,3,5,3,ink)
c.rect(6,3,3,2,light)
c.rect(11,3,4,3,ink)
c.rect(12,3,2,2,steel)
c.rect(16,3,4,3,ink)
c.rect(17,3,2,2,steel)
# rounded casing silhouette
c.rect(4,5,21,25,ink)
c.rect(3,7,23,21,ink)
c.rect(5,6,18,22,'#d18443')
c.rect(4,8,20,19,'#d18443')
c.rect(5,6,18,2,'#f2c273')
c.line(4,8,4,26,'#f2c273')
c.rect(23,7,2,21,'#8c5138')
c.rect(5,28,18,1,'#8c5138')
# cassette window bevel
c.rect(5,9,18,13,'#8c5138')
c.rect(6,9,16,1,ink)
c.rect(5,10,18,11,ink)
c.rect(6,10,16,10,'#597780')
c.rect(7,11,14,8,'#96b6b6')
# tape cassette inside the clear pane
c.rect(7,13,14,6,'#354455')
c.line(9,17,18,17,'#c5d8d9')
c.line(10,14,18,14,'#718f99')
for x in [10,18]:
    c.circle(x,15,3,ink)
    c.circle(x,15,2,cream)
    c.set(x,15,shadow)
    c.set(x,13,steel)
    c.set(x-2,16,steel)
    c.set(x+2,16,steel)
c.poly([(10,18),(18,18),(20,20),(8,20)],ink)
c.rect(11,19,6,1,steel)
# glass reflections over upper edge
c.line(7,11,12,11,'#e3f4e9')
c.set(7,12,'#e3f4e9')
c.line(16,11,20,11,'#bbd7d2')
c.line(6,21,21,21,'#f2c273')
# lower playback controls inset
c.rect(6,23,11,4,ink)
c.rect(7,24,4,2,shadow)
c.poly([(8,24),(10,25),(8,27)],cream)
c.rect(12,24,3,2,steel)
c.rect(13,24,2,2,light)
# exposed volume thumbwheel
c.rect(19,23,4,5,ink)
c.rect(20,23,2,4,steel)
c.set(20,23,light)
c.set(20,25,light)
c.line(18,24,18,26,'#8c5138')
# tiny power light and screw
c.set(7,28,'#fff0ba')
c.set(8,28,'#73b9a0')
c.set(22,28,shadow)
view(result, scale=12)
finish(result)
