f1=new_canvas(42,36,name='original')
f1.blit(input_canvas,4,8)
f2=new_canvas(42,36,name='mid_leap')
a='#3a3737'; b='#b7b3b2'; c='#827c7c'; d='#efe9e7'
def shape(points,col):
    f2.poly(points,col)
    f2.poly(points,a,fill=False)
# hind leg trailing behind the raised body
shape([(13,19),(18,21),(13,26),(7,28),(1,28),(0,26),(2,24),(7,24),(10,20)],b)
f2.line(2,26,7,26,d)
f2.line(8,25,12,23,d)
# far foreleg reaches in direction of travel
shape([(24,19),(29,19),(32,23),(37,23),(39,25),(38,27),(33,27),(28,24)],c)
f2.line(33,25,37,25,b)
# stretched torso
shape([(6,17),(8,14),(13,12),(20,12),(26,13),(30,16),(30,21),(27,24),(20,24),(16,23),(12,24),(8,23),(6,21)],d)
f2.line(7,18,7,21,b)
f2.line(8,22,12,23,b)
f2.line(17,22,22,23,b)
f2.line(23,23,27,22,c)
# near hind foot kicked rearward
shape([(12,20),(16,22),(13,25),(8,26),(4,30),(1,30),(1,28),(5,24),(9,23)],d)
f2.line(2,29,5,26,b)
f2.line(6,25,10,24,b)
f2.line(11,23,13,22,b)
# extended near forepaw
shape([(25,19),(29,19),(30,22),(34,25),(39,25),(40,27),(39,29),(34,29),(30,27),(26,24)],d)
f2.line(28,23,31,26,b)
f2.line(32,27,35,28,b)
f2.line(36,28,39,28,c)
# Preserve the face and ear pixel work from the input.
input_canvas.select(10,0,16,18).copy_to(24,1,f2,mode='over')
view(f1,scale=10)
view(f2,scale=10)
finish([f1,f2])
