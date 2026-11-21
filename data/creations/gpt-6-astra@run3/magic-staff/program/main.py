result = new_canvas(48,48,name='magic_staff')
c=result
# Dark edged, carved wood silhouette, tapering down to a brass ferrule.
outline='#251c32'
shadow='#503044'
wood='#92533e'
mid='#bd7b49'
light='#e6af67'
c.poly([(11,44),(12,38),(16,29),(20,20),(20,15),(18,12),(18,8),(21,4),(25,2),(30,2),(34,4),(36,8),(36,12),(34,16),(31,19),(27,20),(25,18),(25,15),(28,12),(30,11),(30,8),(27,7),(24,8),(23,11),(25,15),(25,20),(22,27),(18,35),(15,43),(14,46),(11,46)],outline)
c.poly([(12,44),(14,38),(18,29),(22,20),(22,15),(20,11),(20,8),(22,5),(26,3),(30,3),(33,5),(35,8),(35,12),(33,15),(30,18),(27,19),(26,17),(27,15),(30,13),(32,10),(31,7),(28,5),(25,6),(22,8),(22,11),(24,15),(24,20),(21,27),(17,36),(14,44)],wood)
# Continuous warm rim and ochre heartwood.
c.path('M 12 43 L 15 35 L 19 27 L 22 20 L 22 16 L 19 11 L 20 8 L 23 5 L 27 3 L 30 3',light,False)
c.path('M 14 41 L 17 34 L 20 28 L 23 20 L 23 15 L 21 11 L 21 8 L 24 6 L 28 4 L 31 5 L 34 8 L 34 12 L 31 16 L 28 17',mid,False)
c.path('M 15 40 L 19 31 L 23 22 L 24 18 M 24 14 L 23 11 L 24 8 L 27 7 L 30 8 L 30 10 M 32 6 L 33 10 L 31 13 L 27 16',shadow,False)
c.line(20,24,21,22,light)
c.line(17,33,18,30,shadow)
c.set(20,28,shadow)
c.set(23,6,'#f5cc83')
c.line(25,4,28,3,'#f5cc83')
# Purple leather binding just below the crook.
c.poly([(19,23),(21,19),(25,20),(23,25)],outline)
c.line(20,21,24,22,'#8053a0')
c.line(20,22,23,23,'#d59ce7')
c.line(19,24,22,25,'#8053a0')
c.set(20,23,'#f2c4f1')
# Golden collar and end cap.
c.line(20,19,24,20,'#e7b763')
c.set(24,21,'#9c633f')
c.line(12,42,14,43,'#f2c77c')
c.line(12,43,14,44,'#b57a4a')
c.line(12,44,13,44,'#e7b763')
# A suspended amethyst in the open hook.
c.poly([(26,9),(29,10),(30,13),(27,16),(25,13)],'#382343')
c.poly([(27,9),(29,11),(29,13),(27,15),(26,12)],'#9950d6')
c.line(27,10,27,13,'#eab1ff')
c.set(28,12,'#c576f2')
c.set(27,10,'#fff0ff')
# Sparse motes and four-point sparkles, all hard edged.
def sparkle(x,y,sz=2):
    c.line(x-sz,y,x+sz,y,'#ae65e7')
    c.line(x,y-sz,x,y+sz,'#ae65e7')
    c.set(x,y,'#fff0ff')
    if sz>1:
        c.set(x,y-1,'#e6b6ff')
        c.set(x,y+1,'#e6b6ff')
sparkle(39,7,2)
sparkle(33,23,2)
sparkle(13,13,2)
sparkle(39,17,1)
c.set(16,5,'#b36de6')
c.set(17,6,'#e9b6ff')
c.set(38,3,'#8351b8')
c.set(41,12,'#9b5bd4')
c.set(29,23,'#b36de6')
c.set(30,26,'#70408e')
c.set(16,19,'#b36de6')
c.set(11,19,'#734798')
view(result)
finish(result)
