# Two frames share an expanded transparent stage.
W,H=46,38
f1=new_canvas(W,H,name='frame_1_original')
f1.blit(input_canvas,3,7)
f2=new_canvas(W,H,name='frame_2_mid_leap')
O='#3a3737'; L='#b7b3b2'; S='#827c7c'; F='#efe9e7'; E='#d6b39d'; T='#bc8b6d'; N='#cdae67'
def poly(points,fill,edge=O):
    f2.poly(points,fill)
    if edge: f2.poly(points,edge,fill=False)
def line(points,col):
    for p,q in zip(points,points[1:]): f2.line(*p,*q,col)
# Far hind leg trails backward, higher than the near leg.
poly([(16,17),(19,20),(15,22),(10,23),(6,23),(5,22),(6,20),(10,20),(13,18)],L)
line([(7,21),(11,21),(14,19)],F)
line([(10,22),(14,21),(16,19)],S)
# Far front paw extends forward.
poly([(29,17),(32,17),(35,19),(39,20),(41,21),(41,23),(37,23),(34,22),(30,21)],L)
line([(35,20),(38,21),(40,21)],F)
line([(35,22),(39,22)],S)
# The back is lengthened and held almost horizontal during flight.
poly([(11,17),(12,15),(15,13),(18,12),(22,11),(27,11),(31,12),(34,15),(34,18),(32,21),(29,22),(25,23),(20,24),(15,23),(12,21),(11,19)],F)
line([(12,18),(13,16),(16,14),(19,13),(23,12),(27,12)],L)
f2.set(13,16,S)
line([(13,21),(16,22),(20,23),(25,22),(29,21),(31,20)],L)
line([(17,23),(20,23),(24,23)],S)
# Near hind thigh flows into a long trailing foot.
poly([(17,18),(20,18),(21,20),(20,22),(17,24),(13,26),(9,28),(5,28),(4,27),(5,25),(8,25),(11,24),(13,22),(14,20)],F,None)
line([(17,18),(19,18),(20,19)],L)
line([(20,20),(19,22),(16,24),(12,26),(9,27),(5,27)],L)
line([(21,20),(21,22),(18,24),(14,26),(10,28),(5,28),(4,27),(5,25),(8,25),(11,24),(13,22)],O)
line([(5,26),(8,26),(11,25)],S)
f2.set(6,26,L)
# Near foreleg reaches ahead and downward, with a rounded paw.
poly([(29,18),(32,18),(33,20),(34,22),(37,24),(40,24),(41,25),(41,26),(36,26),(33,25),(30,22),(29,20)],F,None)
line([(29,20),(30,22),(33,25),(36,26),(41,26),(42,25),(41,24),(38,23),(35,21),(34,18)],O)
line([(30,20),(31,22),(34,24),(37,25),(40,25)],L)
f2.set(34,24,S)
# Preserve the distinctive original face, including its eye, gold nose, and jaw.
# The ears sweep gently backward as the rabbit advances.
for y in range(18):
    for x in range(26):
        if y>=10 and x<13: continue
        if y>=12 and x<15: continue
        idx=input_canvas.get(x,y)
        if idx==0: continue
        sweep = -((8-y+1)//2) if y<8 else 0
        f2.set(x+17+sweep,y+2,idx)
# Finish the neck under the reused jaw without a cut edge.
line([(30,16),(31,17),(32,18),(34,19)],L)
f2.set(30,16,F)
save('bunny_hop_frame_1',f1)
save('bunny_hop_frame_2',f2)
view(f1,scale=10)
view(f2,scale=10)
finish([f1,f2])
