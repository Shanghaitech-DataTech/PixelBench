result = new_canvas(64,64,name='void-eye')
c=result
# translucent hovering shadow
c.ellipse(32,57,19,4,'#17102410')
c.ellipse(32,57,15,3,'#17102418')
c.ellipse(32,57,10,2,'#20132f22')
ink='#100e20'; dark='#21162f'; shade='#35213f'; mid='#51304f'; light='#79516b'; rim='#a77b92'
# short fleshy, curled feelers behind the orb
c.path('M 15 32 Q 8 34 10 42 Q 11 45 7 44 Q 11 50 15 45 L 20 35 Z',ink)
c.path('M 14 35 Q 11 38 13 42 Q 14 45 11 46 Q 17 45 17 36 Z',mid)
c.line(12,36,11,39,light)
c.path('M 46 31 Q 54 32 53 39 Q 51 44 57 41 Q 56 47 51 46 Q 46 43 45 36 Z',ink)
c.path('M 48 34 Q 52 34 50 40 Q 49 44 54 44 Q 49 47 47 39 Z',shade)
c.line(50,35,51,37,light)
c.path('M 19 40 Q 17 46 20 50 Q 22 53 17 51 Q 20 57 24 52 Q 27 48 26 42 Z',ink)
c.path('M 21 43 Q 20 48 23 50 L 21 53 Q 26 52 24 44 Z',mid)
c.line(21,45,21,48,light)
c.path('M 29 43 Q 26 50 31 53 Q 34 55 31 58 Q 39 57 36 51 L 37 43 Z',ink)
c.path('M 31 45 Q 30 49 33 52 Q 35 55 33 56 Q 38 54 34 49 L 35 45 Z',shade)
c.line(31,47,32,50,light)
c.path('M 40 40 Q 45 44 43 49 Q 42 52 47 50 Q 46 55 41 53 Q 36 50 36 44 Z',ink)
c.path('M 41 44 Q 43 47 41 50 Q 42 52 44 52 Q 38 53 39 45 Z',mid)
# massive irregular orb silhouette
c.poly([(11,23),(13,17),(17,12),(23,8),(30,6),(38,7),(45,10),(50,15),(53,22),(53,30),(50,37),(46,43),(39,47),(29,48),(21,45),(15,40),(12,34)],ink)
c.path('M 13 24 Q 16 11 29 8 Q 42 7 49 17 Q 54 29 46 39 Q 39 47 28 45 Q 15 43 13 31 Z',shade)
c.path('M 14 23 Q 19 10 30 9 Q 43 9 48 18 L 44 25 L 19 29 L 14 30 Z',mid)
c.path('M 17 20 Q 23 10 33 10 Q 40 10 45 15 Q 33 10 25 17 L 20 22 Z',light)
c.line(25,11,31,9,rim)
c.line(33,9,37,10,light)
# eye socket and heavy lower lid
c.path('M 14 26 Q 19 16 32 15 Q 46 14 51 25 Q 47 38 35 42 Q 21 42 14 30 Z',ink)
c.path('M 16 31 Q 29 46 44 36 L 48 32 Q 46 43 32 45 Q 20 43 16 35 Z',mid)
c.path('M 18 34 Q 30 44 42 38 Q 32 46 22 39 Z',light)
# eerie pale sclera, cool shadows
c.path('M 16 26 Q 23 17 33 18 Q 43 17 49 25 Q 44 36 33 39 Q 22 38 16 29 Z','#655a7d')
c.path('M 17 26 Q 24 19 33 19 Q 43 18 48 25 Q 43 33 32 35 Q 22 34 17 29 Z','#aaa0ba')
c.path('M 18 25 Q 24 20 31 20 Q 40 18 46 24 Q 35 20 27 26 Q 22 30 18 28 Z','#d7cbd6')
c.path('M 20 31 Q 24 35 29 36 L 24 35 Z','#c3b4cc')
# large deep purple iris
c.ellipse(33,27,11,12,ink)
c.ellipse(33,27,10,11,'#33204e')
c.ellipse(33,27,8,10,'#4e276f')
c.path('M 25 25 Q 25 19 30 18 Q 25 28 30 35 Q 24 33 25 25 Z','#724096')
c.path('M 29 36 Q 38 39 42 29 L 40 34 L 36 38 L 30 38 Z','#8752ac')
# radial iris facets
for x0,y0,x1,y1,col in [(28,19,29,22,'#9762b7'),(34,17,34,21,'#754299'),(38,19,36,22,'#653581'),(41,22,38,24,'#824b9d'),(41,28,38,28,'#64317e'),(39,33,37,31,'#9a59b0'),(35,36,34,32,'#b06bc5'),(30,35,31,32,'#80429e'),(26,30,29,29,'#a562b6'),(25,25,28,25,'#a66bbf')]:
 c.line(x0,y0,x1,y1,col)
# glowing pupil: shaded halo enclosing luminous narrow center
c.ellipse(33,27,5,7,'#492665')
c.ellipse(33,27,3,6,'#774998')
c.ellipse(33,27,2,5,'#b497cf')
c.line(33,23,33,30,'#e8d9f5')
c.set(33,31,'#c4a8e3')
c.set(32,24,'#dbbfec')
# restrained wet glints
c.rect(27,20,2,2,'#eee1ed')
c.set(29,20,'#c6b3d6')
c.set(38,33,'#cc97d7')
# sculpted brow overlaps iris upper edge
c.path('M 13 25 Q 18 16 29 15 Q 41 12 49 22 Q 41 17 32 17 Q 21 18 13 27 Z',dark)
c.path('M 16 22 Q 24 13 36 15 Q 24 15 19 21 Z',rim)
c.line(39,16,44,18,light)
# subtle body creases and lower bounce light
c.line(15,31,17,36,dark)
c.line(18,38,22,41,shade)
c.line(26,44,31,45,'#815170')
c.line(33,45,38,44,light)
c.line(44,39,47,35,dark)
c.set(48,30,light)
c.set(19,16,rim)
view(result)
finish(result)
