# Both frames share the same origin and transparent canvas.
f1 = new_canvas(36, 46, name='frame_1_original')
f1.blit(input_canvas, 2, 1)
p = input_canvas.copy(name='punch_work')
# Remove the raised forearm and hand, preserving the face and torso.
for y, x in [(8,13),(9,13),(10,13),(11,14),(12,15),(13,15),(14,15),(15,16)]:
    p.clear(x,y,29-x,1)
f2 = new_canvas(36,46,name='frame_2_light_punch')
f2.blit(p,2,1)
# Draw the extended left arm in original sprite coordinates.
ink='#222034'; skin='#eec39a'; orange='#df7126'; shade='#8f563b'
def poly(points,color):
    f2.poly([(x+2,y+1) for x,y in points],color)
def line(x,y,xx,yy,color):
    f2.line(x+2,y+1,xx+2,yy+1,color)
def pixel(x,y,color):
    f2.set(x+2,y+1,color)
poly([(12,10),(15,9),(18,10),(25,10),(26,8),(29,8),(31,9),(31,13),(29,14),(26,14),(25,13),(21,15),(17,15),(15,14),(13,13)],ink)
poly([(13,11),(15,10),(18,11),(25,11),(26,10),(29,9),(30,10),(30,12),(29,13),(26,13),(25,12),(21,14),(17,14),(15,13),(13,13)],orange)
poly([(13,11),(15,10),(18,11),(25,11),(25,12),(21,13),(17,13),(15,12),(13,12)],skin)
# Fist highlights and curled thumb.
f2.rect(28,10,4,2,skin)
line(26,11,28,11,skin)
pixel(29,12,shade)
pixel(28,12,skin)
line(17,14,21,14,shade)
pixel(16,13,shade)
view(f1,scale=10)
view(f2,scale=10)
finish([f1,f2])
