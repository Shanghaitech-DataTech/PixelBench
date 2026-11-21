# Both frames use the same transparent canvas; the first preserves every source pixel.
f1 = new_canvas(55,55,name='original')
f1.blit(input_canvas,7,4)
f2 = new_canvas(55,55,name='full_draw')
# Original head, hair, quiver and cloak, with the torso set back for the draw.
f2.ellipse(22,49,20,2,42)
limits = [22]*19 + [21]*6 + [22]*10 + [21]*6
for y in range(28):
    for x in range(limits[y]+1):
        idx=input_canvas.get(x,y)
        if idx and idx!=42:
            f2.set(x+6,y+4,idx)
# Spread the weight over two planted boots. Preserve the original pixel texture.
for y in range(28,45):
    for x in range(12,25):
        idx=input_canvas.get(x,y)
        if idx and idx!=42:
            # progressively shift the forward leg away from the rear leg
            shift=max(0,(y-28)//4)
            f2.set(x+6+shift,y+4,idx)
# Rear leg and trailing cloak angle back toward the planted heel.
for y in range(28,45):
    for x in range(0,12):
        idx=input_canvas.get(x,y)
        if idx and idx!=42:
            shift=min(3,(y-28)//4)
            f2.set(x+6-shift,y+4,idx)
# Clear remnants of the narrow original boot placement.
# Bow: recurve limbs bend back under a full draw.
dark=1; gold=7; ochre=27; pale=6; pink=8; lightpink=11
f2.path('M 37 7 L 37 10 L 40 12 L 43 15 L 45 19 L 47 24 L 46 30 L 44 35 L 41 39 L 38 41 L 37 44',dark,fill=False)
f2.path('M 38 7 L 38 10 L 41 12 L 44 15 L 46 19 L 48 24 L 47 30 L 45 35 L 42 39 L 39 41 L 38 44',ochre,fill=False)
f2.path('M 37 7 L 38 10 L 40 12 L 43 15 L 45 19 L 47 24 L 46 30 L 44 35 L 41 39 L 38 41 L 37 44',gold,fill=False)
f2.line(37,7,38,9,pale)
f2.line(37,42,37,44,pale)
# String pulled all the way back to the cheek; no arrow.
f2.line(37,7,27,22,17)
f2.line(27,22,37,44,17)
f2.line(37,8,28,21,12)
f2.line(28,24,36,42,12)
# Limb bindings retain the pink accents of the original weapon.
for x,y in [(44,16),(44,33)]:
    f2.line(x,y,x+2,y+3,10)
    f2.line(x+1,y,x+2,y+2,8)
    f2.set(x+1,y+1,23)
# Clean and turn the chest into the new shoulder line.
f2.poly([(18,22),(25,21),(29,24),(29,29),(26,32),(19,31),(17,27)],20)
f2.poly([(19,23),(25,22),(28,25),(27,29),(24,31),(19,29)],24)
f2.poly([(20,23),(25,23),(27,25),(25,27),(20,26)],22)
f2.line(20,23,24,23,26)
f2.line(20,27,25,28,30)
f2.line(20,30,25,31,27)
f2.set(23,30,19)
# Bow arm: shoulder to wrist forms a nearly horizontal line.
f2.poly([(26,22),(30,22),(33,23),(43,23),(44,22),(47,23),(47,27),(43,27),(42,26),(31,27),(27,28),(25,26)],20)
f2.poly([(27,23),(30,23),(32,24),(32,26),(28,27),(26,25)],32)
f2.line(27,23,30,23,33)
f2.set(26,24,33)
f2.line(28,26,31,26,31)
# forearm, bracer, and the hand wrapped around the grip
f2.rect(32,24,11,2,12)
f2.line(32,26,42,26,16)
f2.rect(35,23,7,4,31)
f2.line(35,23,40,23,33)
f2.line(36,24,40,24,32)
f2.line(36,26,41,26,28)
f2.line(35,23,35,26,19)
f2.line(41,24,41,26,17)
f2.rect(43,23,4,3,12)
f2.line(43,23,45,23,14)
f2.line(44,26,46,26,2)
f2.set(46,24,3)
f2.set(47,24,1)
f2.set(46,25,16)
# Drawing arm: elbow driven behind the shoulder; forearm returns to the face.
f2.poly([(21,24),(17,22),(13,21),(11,23),(12,26),(18,29),(21,28),(23,26)],20)
f2.poly([(20,25),(16,23),(13,22),(12,24),(14,26),(18,28),(20,27)],32)
f2.line(13,22,17,24,33)
f2.line(14,26,18,28,31)
# Drawn forearm rises from rear elbow to anchor hand below the jaw.
f2.poly([(13,22),(17,21),(23,21),(25,20),(28,21),(28,23),(25,24),(18,25),(14,25)],1)
f2.poly([(14,22),(18,22),(23,22),(25,21),(27,21),(27,23),(23,23),(18,24),(14,24)],12)
f2.line(15,22,22,22,14)
f2.line(18,24,23,23,3)
f2.poly([(14,22),(18,21),(20,22),(19,25),(15,25)],31)
f2.line(15,22,18,22,33)
f2.line(15,23,18,23,32)
f2.line(15,25,18,25,28)
f2.line(19,22,19,24,19)
f2.set(26,21,14)
f2.set(27,22,3)
view(f1,scale=7)
view(f2,scale=7)
finish([f1,f2])
