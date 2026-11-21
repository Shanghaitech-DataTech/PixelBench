# The first frame preserves every input pixel on a larger shared canvas.
f1 = new_canvas(44, 34, name='rest')
f1.blit(input_canvas, 4, 5)
f2 = new_canvas(44, 34, name='leap')
ink='#3a3737'; shade='#827c7c'; mid='#b7b3b2'; fur='#efe9e7'
def shape(points, color):
    f2.poly(points,color)
    f2.poly(points,ink,fill=False)
# Far hind leg trails behind the lifted rump.
shape([(13,18),(18,20),(13,24),(8,25),(4,24),(5,22),(9,22)],mid)
f2.line(6,23,10,23,fur)
# Far front leg, visible beyond the chest.
shape([(27,16),(31,16),(34,19),(38,19),(39,20),(39,22),(34,22),(29,20)],mid)
f2.line(35,20,37,20,fur)
# Airborne torso, elongated horizontally.
shape([(7,18),(9,15),(13,13),(18,12),(24,12),(28,13),(31,16),(32,19),(29,22),(24,23),(18,23),(13,22),(9,22),(7,20)],fur)
f2.poly([(8,18),(10,16),(14,14),(19,13),(24,13),(22,14),(15,15),(11,17),(9,20),(10,21),(8,20)],mid)
f2.line(9,17,11,15,shade)
f2.poly([(15,21),(19,22),(25,22),(29,20),(30,18),(31,19),(29,22),(24,22),(18,22)],mid)
# Near hind leg extends back, with the long rabbit foot trailing.
shape([(14,18),(18,19),(18,22),(14,25),(11,27),(4,27),(3,26),(4,24),(9,24),(11,21)],fur)
f2.poly([(14,20),(16,20),(16,22),(12,25),(10,26),(5,26),(5,25),(10,25)],mid)
f2.line(11,23,13,21,shade)
f2.line(5,25,8,25,fur)
# Near foreleg reaches forward and folds at the wrist.
shape([(27,17),(30,17),(32,20),(35,22),(39,22),(40,23),(40,25),(34,25),(30,23),(27,21)],fur)
f2.poly([(28,19),(30,20),(32,23),(35,24),(39,24),(39,23),(35,23),(31,21)],mid)
f2.set(39,24,shade)
# Preserve the original head, face and ears, shifted up and forward.
# The stepped boundary removes the old shoulder while retaining the cheek.
lefts={10:13,11:14,12:15,13:15,14:16,15:17,16:18,17:19,18:20}
for y in range(19):
    for x in range(lefts.get(y,10),26):
        p=input_canvas.get(x,y)
        if p != 0:
            f2.set(x+13,y+1,p)
view(f1,scale=10)
view(f2,scale=10)
finish([f1,f2])
