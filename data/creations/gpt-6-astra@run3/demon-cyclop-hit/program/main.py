import math
f1 = new_canvas(51,45,name='original')
f1.blit(input_canvas,5,9)
pose=input_canvas.copy(name='recoil_source')
ink='#141b1b'; skin='#adbc3a'; shade='#74a334'; cream='#fce2ca'; gold='#ffe18d'; lid='#c8966b'
# Roll the pupil to the upper edge of the original single eye.
pose.rect(17,16,3,3,cream)
pose.rect(17,15,3,3,ink)
# Open the mouth below the eye; retain a green gap between the two features.
pose.rect(14,22,9,4,skin)
pose.poly([(16,23),(20,23),(22,24),(22,26),(20,28),(16,28),(14,26),(14,24)],ink)
pose.rect(16,24,5,2,'#563639')
pose.rect(16,23,5,1,cream)
pose.rect(17,26,4,1,'#c86b64')
# Bend and raise the image-left foot.
pose.clear(6,27,10,6)
pose.poly([(10,26),(14,26),(15,28),(12,30),(7,31),(4,30),(4,28),(7,27)],ink)
pose.poly([(10,27),(13,27),(13,28),(10,29),(6,30),(5,29),(7,28)],shade)
pose.set(5,29,gold)
pose.set(7,29,gold)
pose.line(16,27,21,27,shade)
pose.line(17,28,20,28,shade)
# Rotate around the planted image-right toe, allowing extra space above the horns.
rot=pose.select(0,0,37,33).rotate(14,algorithm='rotsprite').preview()
print('rotated size',rot.stats()['size'])
f2=new_canvas(51,45,name='recoil')
f2.blit(rot,5,3)
# Apply a red impact palette to every visible pixel, preserving the pose's shading.
f3=new_canvas(51,45,name='impact')
palette={p['index']:p['rgba'] for p in f2.palette()}
for y in range(45):
    for x in range(51):
        rgba=palette[f2.get(x,y)]
        r,g,b,a=rgba
        if a:
            f3.set(x,y,(round(r*.47+255*.53),round(g*.38+18*.62),round(b*.38+27*.62),a))
view(f1,scale=8)
view(f2,scale=8)
view(f3,scale=8)
finish([f1,f2,f3])
