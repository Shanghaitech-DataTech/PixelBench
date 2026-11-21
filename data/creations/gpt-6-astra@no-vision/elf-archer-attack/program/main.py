# Shared canvas leaves room for the fully drawn bow and wider stance.
f1 = new_canvas(55, 51, name='original')
f1.blit(input_canvas, 5, 2)
f2 = new_canvas(55, 51, name='full_draw')
# Build the body from the original pixels, preserving its palette and detailing.
# Local coordinates use the original 35 x 47 sprite grid.
def put(x, y, color):
    f2.set(x+5, y+2, color)
def line(x0,y0,x1,y1,color):
    f2.line(x0+5,y0+2,x1+5,y1+2,color)
def poly(points,color):
    f2.poly([(x+5,y+2) for x,y in points],color)
def rect(x,y,w,h,color):
    f2.rect(x+5,y+2,w,h,color)
def stamp(x0,y0,x1,y1,dx=0,dy=0,cond=None):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            p=input_canvas.get(x,y)
            if p and (cond is None or cond(x,y,p)):
                put(x+dx,y+dy,p)
# Ground shadow, wider under the braced feet.
for y in range(42,47):
    for x in range(35):
        if input_canvas.get(x,y)==42:
            put(x,y,42)
line(1,45,34,45,42)
line(3,46,33,46,42)
# Cape streams behind the drawn shoulder.
stamp(0,9,12,40,dx=-1,cond=lambda x,y,p: x < (9 if y<20 else 11))
# Lower tunic and armor: hips shift back as the archer braces.
body_edge={25:20,26:21,27:21,28:21,29:20,30:21,31:21,32:21}
for y in range(25,33):
    stamp(8,y,body_edge[y],y,dx=-1)
# Back leg angles to the left; front leg plants well forward.
for y in range(33,44):
    shift=-1-(y-33)//3
    stamp(9,y,16,y,dx=shift)
for y in range(33,44):
    shift=1+(y-33)//3
    right=22 if y<=35 else (21 if y<=39 else 26)
    stamp(17,y,right,y,dx=shift)
stamp(1,40,12,44,dx=-1)
stamp(19,40,28,44,dx=5)
# Connect the splayed legs with angular armor folds.
poly([(13,32),(18,32),(17,36),(13,41),(11,40)],'c27')
line(15,33,15,37,'c31')
line(15,37,12,41,'c30')
line(18,34,21,37,'c31')
# Torso pulled back slightly beneath the aiming head.
stamp(9,16,24,23,dx=-1)
stamp(9,24,21,24,dx=-1)
# Head with hair, pointed ear, eye, and original expression.
stamp(7,0,23,17,dx=-1,dy=-1)
# Draw arm: elbow is back and level with the shoulder; hand anchors at cheek.
poly([(15,19),(12,16),(7,17),(4,20),(6,23),(11,24),(17,22),(20,20)],'c19')
poly([(14,19),(11,17),(8,18),(6,20),(8,22),(12,22),(17,21)],'c31')
line(7,19,10,18,'c32')
line(7,20,10,21,'c30')
line(10,22,14,21,'c27')
# Extended forearm runs from the rear elbow to the cheek.
poly([(8,17),(10,15),(18,13),(21,14),(22,17),(19,19),(13,19),(10,21)],'c0')
poly([(10,16),(18,14),(20,15),(20,17),(15,18),(11,19),(9,19)],'c2')
line(11,16,18,15,'c11')
line(10,18,15,17,'c14')
line(14,19,19,18,'c1')
# Bracer at the wrist.
poly([(14,15),(16,14),(18,18),(16,19)],'c30')
line(15,15,17,18,'c32')
# Bow arm is fully straight, shoulder to grip, with plated upper arm.
poly([(19,18),(23,17),(28,18),(32,18),(33,22),(27,23),(22,23),(19,22)],'c19')
poly([(20,19),(23,18),(28,19),(29,22),(23,22),(21,21)],'c31')
line(22,18,26,19,'c32')
line(22,19,25,20,'c33')
line(23,22,28,22,'c30')
# Bare arm between elbow guard and bow hand.
poly([(29,18),(34,18),(40,18),(43,19),(43,22),(39,23),(34,22),(29,22)],'c0')
poly([(30,19),(35,19),(40,19),(42,20),(41,22),(35,21),(30,21)],'c2')
line(32,19,40,19,'c11')
line(33,21,40,22,'c1')
poly([(28,18),(31,18),(32,22),(29,23),(28,21)],'c30')
line(29,18,30,21,'c32')
line(30,18,31,21,'c28')
# Full-flex bow: tips pulled back toward the archer, grip pushed forward.
bow=[(33,0),(33,3),(35,5),(38,7),(40,10),(42,14),(43,18),(43,22),(42,27),(40,31),(37,34),(34,36),(33,39)]
for (x0,y0),(x1,y1) in zip(bow,bow[1:]):
    line(x0,y0,x1,y1,'c0')
    line(x0+1,y0,x1+1,y1,'c0')
    line(x0,y0+1,x1,y1+1,'c8')
# Gold facing and small original-style magenta inlays.
for a,b in [((34,4),(37,6)),((38,8),(40,11)),((41,13),(42,17)),((42,24),(41,28)),((40,30),(37,33)),((36,35),(34,37))]:
    line(*a,*b,'c6')
line(38,7,39,8,'c16')
line(42,13,42,15,'c9')
put(42,14,'c22')
line(40,30,39,31,'c9')
put(40,30,'c22')
# Taut bowstring forms a deep V to the drawing fingers, with no arrow.
line(33,1,20,15,'c2')
line(20,15,33,39,'c2')
line(33,1,28,6,'c11')
line(25,24,31,35,'c11')
# Grip and fingers cover the string/bow junctions naturally.
rect(42,18,2,6,'c19')
line(43,18,43,23,'c35')
poly([(40,18),(42,18),(43,19),(42,22),(40,22),(39,21)],'c1')
line(40,19,42,19,'c11')
line(40,20,42,20,'c2')
put(41,21,'c11')
# Fingers anchored alongside the mouth; do not cover the eye above.
poly([(19,13),(21,13),(22,15),(21,18),(19,18),(18,16)],'c1')
line(19,14,20,14,'c11')
line(19,15,21,15,'c14')
line(19,16,20,16,'c11')
put(19,17,'c2')
# Verify that frame one retains every source pixel at its shared offset.
assert all(f1.get(x+5,y+2)==input_canvas.get(x,y) for y in range(47) for x in range(35))
assert f1.stats()['size']==f2.stats()['size']
save('elf-archer-attack-frame-1',f1)
save('elf-archer-attack-frame-2',f2)
print(f1.stats_text())
print(f2.stats_text())
finish([f1,f2])
