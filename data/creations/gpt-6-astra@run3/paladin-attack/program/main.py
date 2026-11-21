W,H=80,76
f1=new_canvas(W,H,name='ready')
f1.blit(input_canvas,12,8)
f2=new_canvas(W,H,name='heavy_attack')
# Ground shadow moves with the wider stance.
f2.ellipse(37,67,23,4,41)
f2.ellipse(54,68,13,3,41)
# White sweep: a tapered arc following the descending mace.
f2.path('M 35 7 Q 61 4 72 24 Q 80 42 66 62 L 60 57 Q 72 40 66 26 Q 59 12 35 7 Z','#ccd8e1')
f2.path('M 36 7 Q 62 6 72 27 Q 78 43 65 60 L 62 57 Q 72 39 65 24 Q 55 11 36 7 Z',31)
f2.path('M 48 7 Q 68 11 75 28',31,fill=False)
f2.line(75,32,76,38,31)
# Cape behind the body, pulled back by the lunge.
f2.poly([(39,32),(47,34),(47,47),(50,60),(46,63),(30,59),(29,40)],1)
f2.poly([(40,34),(45,35),(44,48),(48,60),(43,61),(32,58),(32,40)],8)
f2.poly([(41,36),(43,37),(41,48),(45,60),(41,60),(37,49)],17)
f2.line(43,43,46,59,9)
f2.line(33,58,44,61,22)
f2.line(36,58,45,60,25)
# Rear leg: keep the original engraved plate and greave pixels.
for y in range(41,59):
    for x in range(9,20):
        i=input_canvas.get(x,y)
        if i not in (0,41):
            f2.set(x+10,y+7,i)
# Left leg steps forward on screen-right, bending out from the hip.
f2.poly([(35,48),(42,48),(49,55),(48,61),(40,60),(35,54)],1)
f2.poly([(37,49),(41,50),(46,55),(44,58),(39,56)],16)
f2.poly([(38,49),(41,51),(44,54),(42,55),(38,53)],5)
f2.line(40,50,44,54,18)
for y in range(44,57):
    for x in range(25,36):
        i=input_canvas.get(x,y)
        if i not in (0,41):
            f2.set(x+20,y+12,i)
# Original torso, helm and shield, compressed into a forward lean.
for y in range(8,52):
    for x in range(0,30):
        i=input_canvas.get(x,y)
        if i in (0,41): continue
        if y<11 and x>=22: continue
        if 11<=y<=23 and x>=27: continue
        if 24<=y<=29 and x>=27: continue
        if y>=41 and x>=15: continue
        if y>=49 and x>=11: continue
        # upper body travels forward more than the hips
        dx=15 if y<30 else (14 if y<38 else 12)
        if x<15 and y>=23: dx=11
        f2.set(x+dx,y+11,i)
# Hip plates bridge the widened stance.
for y in range(39,47):
    for x in range(15,28):
        i=input_canvas.get(x,y)
        if i not in (0,41): f2.set(x+12,y+11,i)
# Lowered striking arm, articulated shoulder / elbow / gauntlet.
f2.poly([(40,34),(44,32),(49,35),(49,39),(53,43),(52,48),(47,48),(43,43),(40,41)],1)
f2.poly([(41,35),(44,33),(48,35),(47,39),(43,40),(41,38)],16)
f2.poly([(42,35),(44,34),(47,36),(46,38),(43,38)],5)
f2.line(43,34,46,35,18)
f2.line(42,39,46,40,22)
f2.line(43,39,46,39,25)
f2.poly([(44,41),(47,40),(50,43),(48,46),(45,44)],21)
f2.line(47,41,49,43,15)
# Wooden shaft, tilted into the impact. Dark silhouette and gold binding.
f2.poly([(46,39),(48,37),(67,57),(65,60)],1)
f2.line(48,39,66,58,7)
f2.line(49,39,67,57,10)
f2.line(54,44,55,43,26)
f2.line(59,50,60,49,26)
# Fist closes visibly over the shaft.
f2.poly([(47,41),(50,40),(54,43),(54,46),(51,49),(47,46)],1)
f2.poly([(48,42),(50,41),(53,43),(52,46),(50,47),(48,45)],16)
f2.line(49,42,52,44,18)
f2.line(48,44,51,46,5)
f2.set(52,45,15)
# Reuse the original mace head, rotated to follow through downwards.
head=new_canvas(13,12,name='mace_head')
for y in range(11):
    for x in range(17,30):
        i=input_canvas.get(x,y)
        if i not in (0,7,10,8,9,11,12,13,14,17):
            head.set(x-17,y,i)
head.select(0,0,13,12).rotate(180).copy_to(60,53,f2,mode='over')
view(f1,scale=6)
view(f2,scale=6)
finish([f1,f2])
