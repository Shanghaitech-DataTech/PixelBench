# Two 32px RPG animation cels, arranged left to right.
result = new_canvas(64, 32, name="swordsman_walk")
P = {
 'ink':'#171c32', 'deep':'#222d4c',
 'cape0':'#172c53', 'cape1':'#234577', 'cape2':'#32649a', 'cape3':'#5688b6',
 'hair0':'#652b37', 'hair1':'#ad3d35', 'hair2':'#e4683d', 'hair3':'#ffad59',
 'skin0':'#aa6055', 'skin1':'#e79a70', 'skin2':'#ffd09a',
 'steel0':'#425569', 'steel1':'#788d9b', 'steel2':'#b3c9ce', 'steel3':'#ecf4dc',
 'cloth0':'#303647', 'cloth1':'#50536a', 'cloth2':'#77798a',
 'boot0':'#3d2b36', 'boot1':'#70453f', 'boot2':'#a37053',
 'gold0':'#975337', 'gold1':'#d79c50', 'gold2':'#ffe19a'
}
for k,v in P.items(): result.color(v,k)
def poly(c, pts, col): c.poly(pts, P[col])
def line(c, a,b,col): c.line(*a,*b,P[col])
def rect(c,x,y,w,h,col): c.rect(x,y,w,h,P[col])
def dot(c,x,y,col): c.set(x,y,P[col])

def draw_frame(phase):
 c=new_canvas(32,32,name='stride_'+str(phase+1))
 bob=phase
 # Rear leg, visible under the tunic. The other cel swaps the leading leg.
 if phase==0:
  poly(c,[(15,20),(19,21),(16,25),(12,28),(8,28),(8,26),(12,24)],'ink')
  poly(c,[(15,21),(18,22),(14,25),(12,26),(10,26),(13,23)],'cloth0')
  line(c,(14,23),(12,25),'cloth1')
  poly(c,[(10,25),(13,26),(12,28),(8,28),(8,27)],'boot0')
  line(c,(9,26),(11,26),'boot1')
 else:
  poly(c,[(17,21),(21,21),(22,24),(26,27),(26,29),(20,29),(19,26),(17,24)],'ink')
  poly(c,[(18,22),(20,22),(21,25),(24,27),(21,27),(19,25)],'cloth0')
  line(c,(20,23),(21,25),'cloth1')
  rect(c,21,27,4,1,'boot1')
  rect(c,21,28,5,1,'boot0')
 # Cape silhouette, stretched backward with asymmetric pixel folds.
 if phase==0:
  poly(c,[(15,10),(19,11),(17,16),(16,22),(13,25),(9,24),(5,25),(7,21),(8,16),(11,12)],'ink')
  poly(c,[(13,12),(17,12),(15,18),(14,23),(11,24),(9,22),(7,23),(9,17)],'cape0')
  poly(c,[(12,13),(15,12),(13,18),(11,22),(8,23),(10,18)],'cape1')
  line(c,(12,14),(10,19),'cape2')
  line(c,(10,20),(9,21),'cape2')
  line(c,(15,15),(14,20),'cape1')
 else:
  poly(c,[(15,11),(19,12),(17,17),(16,23),(13,26),(10,24),(6,24),(7,20),(9,16),(11,13)],'ink')
  poly(c,[(13,13),(17,13),(15,19),(14,24),(12,24),(10,22),(8,23),(9,18)],'cape0')
  poly(c,[(12,14),(15,13),(13,19),(10,23),(8,22),(10,18)],'cape1')
  line(c,(12,15),(10,19),'cape2')
  dot(c,10,20,'cape2')
  line(c,(15,17),(14,22),'cape1')
 # Near leg: opposite swing in the second frame.
 if phase==0:
  poly(c,[(17,20),(21,20),(22,23),(22,25),(25,27),(26,29),(20,29),(19,26),(17,24)],'ink')
  poly(c,[(18,21),(20,21),(21,24),(20,25),(18,23)],'cloth1')
  line(c,(19,22),(20,24),'cloth2')
  poly(c,[(20,25),(22,25),(24,27),(25,28),(21,28),(20,27)],'boot1')
  line(c,(21,26),(23,27),'boot2')
  line(c,(21,29),(26,29),'ink')
 else:
  poly(c,[(16,21),(20,22),(18,25),(15,27),(14,29),(9,29),(9,27),(13,25)],'ink')
  poly(c,[(16,22),(18,23),(16,25),(14,26),(12,27),(12,26)],'cloth1')
  line(c,(16,23),(14,25),'cloth2')
  poly(c,[(12,26),(15,27),(13,28),(10,28),(10,27)],'boot1')
  line(c,(11,27),(13,27),'boot2')
 # All upper body positions have a one-pixel walk bob.
 def R(x,y,w,h,k):rect(c,x,y+bob,w,h,k)
 def L(x0,y0,x1,y1,k):line(c,(x0,y0+bob),(x1,y1+bob),k)
 def D(x,y,k):dot(c,x,y+bob,k)
 def Q(points,k):poly(c,[(x,y+bob) for x,y in points],k)
 # Neck and fitted steel cuirass over dark clothing.
 R(17,10,4,4,'ink'); R(18,10,2,3,'skin0'); R(19,11,2,1,'skin1')
 Q([(16,12),(19,12),(22,14),(22,20),(20,22),(15,21),(14,17)],'ink')
 Q([(17,13),(20,13),(21,15),(21,19),(18,20),(16,19),(16,15)],'steel0')
 Q([(18,13),(20,14),(20,18),(18,19),(17,17),(17,14)],'steel1')
 L(18,14,19,14,'steel3'); L(18,15,18,17,'steel2')
 R(16,19,6,2,'boot0'); L(16,19,20,19,'boot1')
 R(19,19,2,2,'gold1'); D(20,19,'gold2'); D(20,20,'gold0')
 Q([(16,21),(21,21),(22,23),(18,23),(15,22)],'cloth0')
 L(17,21,20,21,'cloth1')
 # Sword: long forward-tilted steel blade, dark edge and two-tone bevel.
 Q([(25,19),(25,15),(28,7),(30,4),(30,10),(27,18)],'ink')
 Q([(26,17),(26,15),(29,6),(29,10),(27,17)],'steel1')
 L(26,16,29,7,'steel3')
 L(27,16,29,10,'steel2')
 # Crossguard and wrapped grip remain visible beyond the fist.
 L(23,17,28,19,'ink'); L(24,17,28,18,'gold1'); D(25,17,'gold2')
 L(25,19,24,22,'ink'); D(24,21,'boot1'); D(24,22,'gold1')
 # Shoulder and arm bent forward to hold the sword.
 Q([(20,13),(23,14),(23,17),(25,18),(25,21),(22,21),(20,18),(19,16)],'ink')
 Q([(20,14),(22,14),(23,16),(21,17),(20,16)],'steel1')
 L(20,14,21,14,'steel3'); L(21,15,22,15,'steel2')
 L(21,17,22,19,'cloth1')
 R(22,18,2,2,'steel0'); D(22,18,'steel2')
 R(24,19,2,2,'skin0'); R(24,18,2,1,'skin2'); D(25,19,'skin1')
 # Right-facing profile: nose and chin stand beyond the red hair.
 Q([(17,4),(21,4),(23,6),(23,8),(25,9),(24,10),(23,10),(23,12),(19,12),(17,10)],'ink')
 Q([(19,5),(21,5),(22,6),(22,8),(24,9),(22,10),(22,11),(20,11),(18,9)],'skin1')
 L(21,6,22,6,'skin2'); D(23,9,'skin2'); L(20,10,21,10,'skin2')
 D(22,7,'ink'); D(23,8,'skin0'); D(22,10,'skin0')
 # Layered copper hair: a windswept fringe, bright crown and shaded nape.
 Q([(13,3),(16,3),(17,2),(21,2),(23,4),(23,6),(21,6),(20,8),(19,7),(19,10),(16,11),(15,9),(14,7),(12,7),(13,5),(11,5)],'ink')
 Q([(14,3),(17,4),(17,3),(21,3),(22,4),(22,5),(20,5),(19,7),(18,7),(18,9),(16,9),(15,7),(13,6),(15,5),(13,4)],'hair1')
 Q([(15,3),(17,4),(18,3),(21,3),(21,4),(19,5),(17,5),(16,6),(14,5)],'hair2')
 L(18,3,20,3,'hair3'); D(15,4,'hair3')
 L(16,7,16,9,'hair0'); D(17,8,'hair2'); D(18,9,'hair0')
 # Ear in front of the long sideburn and a copper collar clasp.
 D(19,8,'skin2'); D(19,9,'skin0')
 D(16,12,'gold1'); D(17,12,'gold2')
 return c

f0=draw_frame(0)
f1=draw_frame(1)
result.blit(f0,0,0).blit(f1,32,0)
print(result.stats_text())
print(f0.matrix_text())
print(f1.matrix_text())
save('swordsman_walk', result)
finish(result)
