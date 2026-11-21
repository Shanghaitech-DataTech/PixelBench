result = new_canvas(32,32,name='bamboo_steamer')
c=result
edge='#65402d'
dark='#8b5734'
mid='#bc8046'
tan='#dfa35c'
light='#f3c980'
cream='#fff0c5'
# Back wall and dark interior
c.ellipse(16,21,14,6,edge)
c.ellipse(16,20,13,5,tan)
c.ellipse(16,20,11,4,dark)
c.ellipse(16,20,10,3,'#754c33')
# Lower basket silhouette
c.path('M 2 21 L 3 26 Q 6 30 16 30 Q 25 30 29 26 L 30 21 Z',edge)
c.path('M 3 22 L 4 26 Q 8 29 16 29 Q 25 29 28 26 L 29 22 Z',mid)
c.path('M 4 23 Q 16 28 28 23 L 28 25 Q 16 31 4 25 Z',tan)
# Woven bamboo vertical seams
for x,y in [(5,25),(9,27),(14,28),(19,28),(24,27),(27,25)]:
    c.line(x,y-1,x,y+1,dark)
    c.set(x+1,y-1,light)
c.path('M 4 26 Q 16 32 28 26',dark,fill=False)
c.path('M 5 26 Q 16 30 27 26',light,fill=False)
# Dumplings, individually scalloped and pleated
# rear dumpling
c.poly([(11,19),(11,17),(12,15),(14,14),(15,13),(17,14),(20,17),(20,19),(18,21),(13,21)],edge)
c.poly([(12,18),(13,16),(15,14),(17,15),(19,18),(19,19),(17,20),(13,20)],'#e6c797')
c.poly([(12,18),(14,15),(15,14),(17,16),(18,18),(16,19),(13,19)],cream)
c.line(15,15,14,18,'#c49e73')
c.line(17,16,17,18,'#c49e73')
c.set(15,15,'#ffffff')
# Left dumpling
c.poly([(5,21),(6,19),(8,18),(9,17),(11,18),(14,21),(13,23),(10,24),(7,23)],edge)
c.poly([(6,21),(7,19),(9,18),(11,19),(13,21),(12,22),(9,23),(7,22)],'#e6c797')
c.poly([(6,21),(8,19),(9,18),(11,20),(11,21),(9,22),(7,22)],cream)
c.line(9,19,8,21,'#c49e73')
c.line(11,20,11,21,'#c49e73')
c.set(9,18,'#ffffff')
# Right dumpling
c.poly([(18,22),(18,20),(20,18),(22,17),(24,18),(26,20),(26,22),(24,24),(20,24)],edge)
c.poly([(19,21),(20,19),(22,18),(24,19),(25,21),(24,23),(20,23)],'#e6c797')
c.poly([(19,21),(21,19),(22,18),(24,20),(24,21),(22,22),(20,22)],cream)
c.line(22,19,21,21,'#c49e73')
c.line(24,20,24,21,'#c49e73')
c.set(22,18,'#ffffff')
# Front rolled rim, below visible dumplings
c.path('M 2 21 Q 4 25 16 25 Q 27 25 30 21 L 29 24 Q 25 27 16 27 Q 6 27 3 24 Z',edge)
c.path('M 3 22 Q 7 26 16 26 Q 26 26 29 22',light,fill=False)
c.path('M 5 24 Q 16 28 27 24',tan,fill=False)
# Tilted lid, lifted toward upper left
c.poly([(2,11),(4,8),(10,5),(16,4),(21,5),(24,7),(24,10),(19,13),(11,16),(6,16),(2,14)],edge)
c.poly([(3,11),(9,8),(17,5),(22,6),(23,8),(21,10),(14,13),(7,15),(3,13)],dark)
c.poly([(3,10),(5,8),(11,5),(17,4),(21,5),(23,7),(21,9),(15,12),(8,14),(4,13)],tan)
c.poly([(5,10),(6,8),(12,6),(17,5),(20,6),(21,7),(18,9),(11,12),(7,13),(5,12)],light)
# diagonal bamboo strips and inset lip
c.line(6,10,17,6,mid)
c.line(8,12,20,7,mid)
c.line(7,9,17,5,cream)
c.line(9,12,20,8,tan)
c.line(4,12,7,13,cream)
c.line(8,14,20,10,mid)
c.line(12,14,22,10,light)
# lid loop handle
c.poly([(11,7),(11,5),(13,3),(16,3),(18,5),(17,7),(15,8),(13,8)],edge)
c.poly([(12,6),(13,4),(16,4),(17,5),(16,7),(14,7)],mid)
c.line(13,5,15,4,light)
c.line(14,6,15,5,edge)
# delicate little steam curls in open space
steam='#d3e3df'
c.path('M 26 15 L 27 14 L 27 12 L 26 11 L 26 9 L 27 8',steam,fill=False)
c.set(27,7,'#edf3e8')
c.path('M 29 11 L 30 10 L 30 8 L 29 7 L 29 5', '#aabfbb',fill=False)
c.set(29,4,steam)
view(result,scale=12)
finish(result)
