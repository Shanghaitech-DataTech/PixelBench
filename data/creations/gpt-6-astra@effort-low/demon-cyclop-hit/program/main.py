f1 = new_canvas(49,39,name='original')
f1.blit(input_canvas,4,4)
p = input_canvas.copy(name='recoil_parts')
ink='#141b1b'; green='#adbc3a'; shade='#74a334'; cream='#fce2ca'; gold='#ffe18d'
# Roll the pupil up within the original eye.
p.rect(17,16,3,3,cream)
p.rect(17,15,3,3,ink)
p.set(17,15,'#ffffff')
# Open the mouth under the eye, with a dark cavity, teeth and tongue.
p.poly([(15,22),(21,22),(23,24),(22,27),(19,28),(16,27),(14,25)],ink)
p.line(16,22,20,22,cream)
p.line(17,23,20,23,cream)
p.line(17,26,21,26,'#b65853')
p.line(18,27,20,27,'#e68b78')
# Lift and bend the monster's right leg (on the viewer's left).
p.clear(6,27,9,6)
p.clear(7,26,4,1)
p.poly([(10,25),(14,26),(14,28),(10,30),(6,29),(3,27),(4,24),(7,24),(8,26)],ink)
p.poly([(10,26),(13,27),(10,29),(7,28),(4,26),(5,25),(7,26)],shade)
p.line(5,25,6,26,gold)
p.set(10,27,green)
# A row-wise lean pushes the horns and torso back while the supporting foot stays planted.
f2=new_canvas(49,39,name='recoil')
w,h,rgba=p.to_rgba()
for y in range(h):
    shift=round(max(0,31-y)*0.19)
    for x in range(w):
        i=(y*w+x)*4
        r,g,b,a=rgba[i:i+4]
        if a: f2.set(x+4+shift,y+4,(r,g,b,a))
f3=new_canvas(49,39,name='impact_red')
w,h,rgba=f2.to_rgba()
for y in range(h):
    for x in range(w):
        i=(y*w+x)*4
        r,g,b,a=rgba[i:i+4]
        if a:
            f3.set(x,y,(round(r*0.48+255*0.52),round(g*0.48+22*0.52),round(b*0.48+28*0.52),a))
view(f1)
view(f2)
view(f3)
finish([f1,f2,f3])
