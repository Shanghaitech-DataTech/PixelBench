W,H=50,51
f1=new_canvas(W,H,name='original')
f1.blit(input_canvas,7,2)
f2=new_canvas(W,H,name='full_draw')
# Source pixels keep the elf's detailed costume and face.
def patch(x,y,w,h,dx,dy):
    input_canvas.select(x,y,w,h).copy_to(dx,dy,f2,mode='over')
# Ground shadow widened for the braced feet.
f2.ellipse(22,47,20,2,42)
# Flowing skirt, torso and quiver, before the new arms.
patch(0,0,23,17,5,2)
patch(7,16,15,13,12,18)
patch(0,25,23,15,5,27)
# Spread both boots while preserving their original rendering.
patch(0,40,10,6,3,42)
patch(10,40,8,3,15,42)
patch(17,39,10,6,26,41)
# Extend hems into the planted legs.
f2.poly([(10,39),(15,40),(13,44),(8,44)],25)
f2.line(10,40,8,42,27)
f2.line(11,40,10,42,19)
f2.poly([(23,38),(27,39),(31,43),(27,44),(23,42)],25)
f2.line(25,40,28,43,36)
f2.line(26,40,29,42,32)
f2.line(28,43,30,43,27)
# New shoulder and chest silhouette.
f2.poly([(15,18),(21,17),(26,18),(29,22),(26,28),(18,28),(12,24)],20)
f2.poly([(17,19),(22,18),(26,20),(25,25),(19,27),(14,24)],24)
f2.poly([(17,19),(21,20),(25,19),(27,21),(24,23),(17,22)],22)
f2.line(18,19,21,20,26)
f2.line(22,20,25,19,26)
f2.line(17,23,24,24,30)
f2.poly([(17,25),(24,24),(25,27),(20,29),(15,27)],36)
f2.line(17,26,23,26,27)
f2.set(21,26,19)
f2.set(22,26,35)
# Rear drawing arm: elbow pulled back, forearm raised to the cheek.
body=f2
f2=new_canvas(W,H,name='drawing_arm')
f2.poly([(16,19),(12,19),(6,22),(6,25),(10,27),(15,25),(19,22),(23,20),(23,17),(20,16),(16,19)],20)
f2.poly([(15,20),(12,20),(8,22),(8,25),(11,25),(16,22)],2)
f2.poly([(14,20),(11,21),(8,23),(10,24),(15,22)],12)
f2.line(9,22,13,20,14)
# Magenta sleeve at rear shoulder.
f2.poly([(15,19),(18,19),(18,22),(14,24),(12,22)],10)
f2.poly([(15,19),(17,20),(16,22),(14,23),(13,22)],8)
f2.line(14,20,16,20,11)
f2.set(14,21,23)
# Arm across from rear elbow to anchor, dark bracer then fingers.
f2.poly([(9,23),(11,25),(19,21),(18,18),(15,19)],31)
f2.poly([(10,23),(11,24),(17,21),(17,19)],32)
f2.line(11,22,16,19,33)
f2.line(13,23,17,21,28)
f2.line(16,19,18,21,27)
f2.poly([(18,18),(20,16),(23,16),(24,18),(22,20),(19,21)],2)
f2.poly([(18,18),(21,17),(23,17),(22,19),(19,20)],12)
f2.line(20,17,22,17,14)
f2.set(22,19,3)
# Raise the drawing elbow and seat the fingers beside the cheek.
arm=f2
f2=body
f2.blit(arm,0,-3)
# Straight bow arm from shoulder to grip.
f2.poly([(25,19),(29,19),(33,20),(40,20),(42,19),(46,20),(46,23),(42,24),(39,23),(31,24),(27,23),(25,22)],20)
f2.poly([(27,20),(31,21),(35,21),(35,23),(29,23),(27,22)],3)
f2.line(29,20,34,21,14)
f2.line(29,21,34,22,12)
# Layered steel-green shoulder cap.
f2.poly([(24,18),(27,18),(30,20),(29,23),(26,24),(23,22)],31)
f2.poly([(25,19),(27,19),(29,20),(28,22),(26,23),(24,21)],32)
f2.line(25,19,27,19,34)
f2.line(25,20,28,20,33)
f2.set(25,21,33)
f2.line(26,23,28,22,28)
# Bow-arm bracer.
f2.poly([(34,20),(40,20),(41,23),(35,24),(33,23)],31)
f2.poly([(35,21),(39,21),(40,22),(35,23)],32)
f2.line(35,21,38,21,33)
f2.line(34,20,34,23,27)
f2.line(40,20,40,23,2)
# Fully flexed gold bow; swept tips bend back toward the archer.
bow=[(35,3),(37,4),(39,6),(39,8),(42,10),(44,13),(45,17),(45,20),(46,22),(45,25),(44,29),(42,33),(39,36),(37,39),(34,41)]
for a,b in zip(bow,bow[1:]):
    f2.line(a[0],a[1],b[0],b[1],1)
    f2.line(a[0]+1,a[1],b[0]+1,b[1],2)
    f2.line(a[0],a[1]-1,b[0],b[1]-1,7)
# Gold highlights and recurved ends.
f2.line(35,2,37,3,6)
f2.line(39,7,42,10,19)
f2.line(44,13,45,17,6)
f2.line(44,27,43,30,19)
f2.line(39,35,37,38,6)
f2.line(34,40,36,39,19)
# Magenta limb bindings.
for x,y in [(43,12),(44,16),(42,31),(38,36)]:
    f2.line(x,y,x+2,y,10)
    f2.line(x,y+1,x+2,y+1,8)
    f2.set(x,y+1,11)
# Taut string: two unobstructed segments meet at the drawing fingers.
f2.line(35,3,22,15,13)
f2.line(22,15,34,40,13)
f2.set(22,15,14)
# Grip and bow hand are in front of the bow and bracer.
f2.rect(44,20,3,4,1)
f2.line(45,20,45,23,10)
f2.poly([(41,20),(43,19),(45,20),(45,22),(43,24),(41,23)],2)
f2.poly([(41,20),(43,20),(44,21),(43,23),(41,22)],12)
f2.line(41,20,43,20,14)
f2.set(44,22,3)
# Finish the turned torso with the original armor palette.
f2.line(18,20,21,21,26)
f2.line(21,21,24,20,22)
f2.line(17,22,22,23,30)
f2.set(18,21,22)
f2.line(16,24,20,24,24)
f2.line(23,23,24,25,24)
f2.set(23,25,27)
f2.set(19,26,19)
f2.set(20,26,35)
# Remove an isolated remnant of the old relaxed arm.
f2.clear(8,26,2,1)
view(f1,scale=8)
view(f2,scale=8)
finish([f1,f2])
