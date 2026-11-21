# Preserve the supplied art exactly in the first frame.
f1 = new_canvas(44, 38, name='frame_1_original')
f1.blit(input_canvas, 5, 9)
f2 = new_canvas(44, 38, name='frame_2_mid_hop')
O='#3a3737'; S='#b7b3b2'; D='#827c7c'; W='#efe9e7'
def shape(points, fill=W):
    f2.poly(points, fill)
    f2.poly(points, O, fill=False)
# Far hind leg: tucked at the hock, with a long trailing foot.
shape([(19,21),(22,23),(19,26),(15,28),(10,28),(9,27),(10,26),(15,25),(17,22)], S)
f2.line(11,27,15,27,W)
# Far foreleg, folded under the chest.
shape([(28,19),(31,21),(31,23),(34,24),(35,26),(34,27),(30,26),(27,23)], S)
f2.line(31,25,33,25,W)
# Near hind leg is stretched out by the push-off.
shape([(17,21),(21,23),(19,26),(15,29),(10,30),(6,30),(6,28),(9,27),(12,27),(15,24)])
f2.line(7,29,12,29,S)
f2.line(13,28,16,27,S)
f2.line(16,26,18,24,D)
f2.set(7,28,S)
# Rounded tail on the trailing edge.
shape([(10,17),(12,17),(14,19),(14,21),(12,23),(9,22),(8,20),(8,19)])
f2.line(9,20,10,21,S)
f2.set(10,18,W)
# A lengthened, airborne torso.
shape([(25,14),(21,14),(17,15),(14,17),(12,20),(12,23),(14,25),(18,26),(23,26),(27,24),(30,22),(32,19),(31,16)])
f2.line(14,24,18,25,S)
f2.line(19,25,23,25,S)
f2.line(24,24,26,23,S)
f2.line(27,22,29,20,S)
# Haunch shading describes the thigh without cutting through the body.
f2.line(15,20,17,19,S)
f2.line(18,19,20,20,S)
f2.line(20,21,20,23,S)
f2.line(19,24,17,25,D)
# Extended near foreleg and small forward paw.
shape([(28,20),(31,20),(32,23),(35,25),(38,25),(40,27),(40,28),(35,28),(32,26),(29,24)])
f2.line(30,22,31,24,S)
f2.line(32,25,35,27,S)
f2.line(36,27,39,27,S)
f2.set(39,26,W)
# Keep the original head, expression and ears, relocating them as a unit.
for y in range(18):
    for x in range(10,26):
        p=input_canvas.get(x,y)
        if p != 0:
            f2.set(x+14,y+3,p)
print(f1.stats_text())
print(f2.stats_text())
print(f2.matrix_text())
save('bunny_hop_frame_1',f1)
save('bunny_hop_frame_2',f2)
finish([f1,f2])
