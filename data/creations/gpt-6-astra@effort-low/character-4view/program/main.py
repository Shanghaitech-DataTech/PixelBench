result = new_canvas(64,64,name='cheerleader_four_views')
O='#292137'; H='#71402f'; HL='#ae6540'; HS='#492c2c'; S='#f5bf91'; SS='#d98d75'; W='#fff4dc'; SH='#b8b7cd'; R='#dd385e'; RL='#ff7290'; RD='#972c51'; B='#f5c653'
def rect(c,x,y,w,h,col): c.rect(x,y,w,h,col)
def front(back=False):
 c=new_canvas(24,30)
 # ponytail behind shoulders
 c.poly([(14,3),(18,4),(19,7),(18,13),(15,15),(14,11)],O)
 c.rect(16,6,2,7,H);c.set(17,7,HL)
 # legs and shoes
 for x in (8,13):
  c.rect(x,21,4,7,O);c.rect(x+1,22,2,4,S);c.set(x+1,25,SS)
  c.rect(x,26,4,3,O);c.rect(x+1,26,2,2,W)
  c.rect(x-1,28,5,2,O);c.rect(x,28,3,1,W)
 # neck and arms
 c.rect(10,10,4,4,O);c.rect(11,10,2,3,S)
 c.poly([(7,12),(5,13),(4,18),(6,20),(8,16),(16,16),(18,20),(20,18),(19,13),(16,12)],O)
 c.line(6,14,5,17,S);c.line(17,14,18,17,S)
 # torso
 c.poly([(8,12),(10,12),(12,14),(14,12),(16,12),(15,19),(9,19)],O)
 c.poly([(9,13),(12,15),(15,13),(14,18),(10,18)],R)
 c.line(9,13,12,15,W);c.line(12,15,15,13,W)
 if not back: c.set(12,16,B)
 c.rect(9,18,7,2,O);c.rect(10,18,5,1,W)
 # pleated skirt
 c.poly([(9,19),(15,19),(18,23),(6,23)],O)
 c.poly([(10,19),(14,19),(16,22),(8,22)],R)
 c.line(10,20,9,22,RL);c.line(14,20,15,22,RD);c.line(7,23,17,23,W);c.line(7,24,17,24,O)
 # head
 c.rect(7,3,10,7,O);c.rect(8,2,8,10,O)
 c.rect(8,4,8,6,S);c.rect(9,10,6,1,SS)
 c.rect(8,3,8,3,H);c.rect(9,3,5,1,HL);c.set(8,6,H);c.set(15,6,H)
 if back:
  c.rect(8,4,8,7,H);c.rect(9,4,2,6,HL);c.rect(13,5,3,6,HS);c.rect(11,9,3,3,H)
 else:
  c.set(10,7,O);c.set(14,7,O);c.set(9,8,SS);c.set(15,8,SS);c.set(12,9,RD)
 # bow
 c.poly([(13,2),(16,1),(16,4),(13,3)],O);c.poly([(17,2),(20,1),(20,5),(17,4)],O)
 c.rect(14,2,2,2,RL);c.rect(18,2,2,2,R);c.set(17,3,B)
 # pom poms
 for x in (3,20):
  c.circle(x,19,3,O);c.circle(x,19,2,B);c.line(x-2,18,x+2,20,RL);c.line(x,17,x,21,W);c.set(x-2,20,R);c.set(x+2,18,R)
 return c

def side():
 c=new_canvas(24,30)
 # facing left, ponytail to right
 c.poly([(14,4),(18,4),(19,7),(18,12),(16,15),(14,12)],O)
 c.rect(16,6,2,6,H);c.line(17,6,17,10,HL)
 # legs
 c.rect(10,22,4,6,O);c.rect(11,23,2,4,SS)
 c.rect(13,22,4,6,O);c.rect(14,23,2,4,S)
 for x in (9,13):
  c.rect(x,26,4,3,O);c.rect(x+1,26,2,2,W);c.rect(x-1,28,5,2,O);c.rect(x,28,3,1,W)
 # torso
 c.rect(10,11,4,3,O);c.rect(11,11,2,2,S)
 c.poly([(10,12),(14,12),(16,18),(15,20),(9,20),(8,16)],O)
 c.poly([(10,13),(13,13),(14,18),(10,18),(9,16)],R)
 c.line(9,14,11,15,W);c.rect(10,18,5,1,W)
 c.poly([(10,19),(15,19),(18,24),(8,24)],O)
 c.poly([(11,19),(14,19),(16,22),(10,22)],R);c.line(13,20,14,22,RL);c.line(9,23,17,23,W)
 # arm
 c.poly([(13,13),(15,14),(15,17),(12,20),(10,18),(12,16)],O)
 c.line(13,14,13,17,S);c.set(12,18,S)
 # face and hair
 c.poly([(9,3),(14,2),(17,4),(17,9),(14,12),(10,11),(9,9),(7,8),(8,6),(8,4)],O)
 c.poly([(9,5),(14,5),(14,10),(11,11),(10,9),(8,8)],S)
 c.rect(9,3,6,2,H);c.rect(14,4,2,7,H);c.rect(10,3,4,1,HL);c.set(9,5,H);c.set(9,7,O);c.set(10,9,SS);c.set(13,7,SS)
 c.rect(15,2,3,3,O);c.rect(16,1,3,2,O);c.rect(16,2,2,2,RL);c.rect(17,4,3,3,O);c.rect(18,4,1,2,R);c.set(16,4,B)
 c.circle(10,20,3,O);c.circle(10,20,2,B);c.line(8,19,12,21,RL);c.line(10,18,10,22,W);c.set(8,21,R)
 return c
result.blit(front(),4,1)
result.blit(front(True),36,1)
a=side();result.blit(a,4,33)
a=a.copy();a.mirror('h');result.blit(a,36,33)
view(result)
finish(result)
