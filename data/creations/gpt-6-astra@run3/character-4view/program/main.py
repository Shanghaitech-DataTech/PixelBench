# Four views of one cheerleader, on a transparent 64px sheet.
result = new_canvas(64, 64, name='cheerleader_four_views')
P = {
 'o':'#252334', 'h':'#62394a', 'm':'#965345', 'l':'#c47950',
 's':'#f4b48d', 'a':'#d98678', 'k':'#ffcfaa',
 't':'#237d91', 'u':'#39b5be', 'v':'#73d9ce', 'n':'#24465f',
 'w':'#fff1db', 'g':'#a4c4ce', 'r':'#d64461', 'p':'#ff8290',
 'y':'#eaa746', 'z':'#ffe58a', 'd':'#a76839'
}
def rect(c,x,y,w,h,k): c.rect(x,y,w,h,P[k])
def line(c,x,y,xx,yy,k): c.line(x,y,xx,yy,P[k])
def poly(c,pts,k): c.poly(pts,P[k])
def pix(c,x,y,k): c.set(x,y,P[k])
def pattern(c,x,y,rows):
 for j,row in enumerate(rows):
  for i,ch in enumerate(row):
   if ch!='.': pix(c,x+i,y+j,ch)

def pom(c,x,y):
 pattern(c,x,y,[
 '..o.o..',
 '.oyoy o'.replace(' ',''),
 'oyzyzyo',
 '.zyzyd.',
 'oyzdyzo',
 '.oyzyo.',
 '..o.o..'])

def front(c,back=False):
 # Ponytail is on the girl's left, changing screen side in the back view.
 if not back:
  poly(c,[(20,5),(23,6),(24,11),(23,14),(20,13),(21,10)],'o')
  poly(c,[(21,6),(22,7),(23,11),(22,13),(21,12)],'m')
  line(c,22,8,22,11,'l')
 else:
  poly(c,[(10,5),(7,6),(6,11),(7,14),(10,13),(9,10)],'o')
  poly(c,[(9,6),(8,7),(7,11),(8,13),(9,12)],'m')
  line(c,8,8,8,11,'l')
 # Legs, socks, and matching sneakers.
 pattern(c,10,22,[
 'oooo.oooo',
 'okso.okso',
 'okso.okso',
 'osao.osao',
 'owwo.owwo',
 'owgo.owgo',
 'owwo.owwo',
 'owwwoowwwo',
 'oooo.ooooo'])
 # Outstretched arms.
 poly(c,[(10,13),(8,13),(6,16),(4,16),(4,19),(7,19),(11,16)],'o')
 poly(c,[(20,13),(22,13),(24,16),(26,16),(26,19),(23,19),(19,16)],'o')
 line(c,9,14,6,17,'k'); line(c,6,17,5,17,'s')
 line(c,21,14,24,17,'s'); pix(c,25,17,'k')
 # Uniform top.
 poly(c,[(12,12),(18,12),(21,14),(19,18),(20,20),(10,20),(11,18),(9,14)],'o')
 poly(c,[(12,13),(18,13),(20,14),(18,18),(19,20),(11,20),(12,18),(10,14)],'t')
 rect(c,12,14,6,4,'u'); line(c,12,14,12,17,'v')
 # Neck
 rect(c,14,11,3,3,'o'); rect(c,14,11,3,2,'s')
 if not back:
  # V-shaped white yoke and small red center star/crest.
  line(c,11,13,15,16,'w'); line(c,19,13,15,16,'w')
  pix(c,15,17,'r'); pix(c,14,17,'w'); pix(c,16,17,'w')
 else:
  line(c,11,14,19,14,'w'); line(c,13,16,17,16,'n')
  pix(c,14,16,'w'); pix(c,16,16,'w')
 rect(c,11,19,9,1,'w'); rect(c,11,20,9,1,'r')
 # Pleated skirt, identical from all angles.
 poly(c,[(11,21),(19,21),(22,24),(8,24)],'o')
 line(c,11,21,9,23,'t'); line(c,12,21,11,23,'u')
 rect(c,13,21,2,3,'t'); rect(c,16,21,2,3,'u')
 line(c,18,21,20,23,'t'); pix(c,18,23,'v')
 line(c,9,24,21,24,'o')
 line(c,10,23,20,23,'w')
 # Head silhouette.
 poly(c,[(12,3),(18,3),(20,5),(20,9),(18,12),(13,12),(10,9),(10,5)],'o')
 poly(c,[(12,4),(18,4),(19,5),(19,9),(17,11),(13,11),(11,9),(11,5)],'m')
 if not back:
  rect(c,12,6,7,4,'s'); rect(c,13,9,5,2,'k')
  pix(c,11,8,'s'); pix(c,19,8,'a')
  line(c,12,6,14,5,'h'); line(c,14,5,16,6,'h'); line(c,16,6,18,5,'h')
  pix(c,12,5,'l'); pix(c,13,4,'l'); pix(c,14,4,'l')
  pix(c,13,8,'o'); pix(c,17,8,'o')
  pix(c,12,9,'a'); pix(c,18,9,'a'); pix(c,15,10,'a')
 else:
  rect(c,12,5,6,5,'m'); line(c,12,5,12,8,'l'); line(c,13,4,17,4,'l')
  line(c,14,6,14,10,'h'); line(c,17,6,17,10,'h')
  line(c,12,10,13,11,'h'); line(c,18,8,18,10,'l')
 # Red hair bow above left temple (mirrored in back).
 bx=18 if not back else 7
 pattern(c,bx,2,['oo.oo','ororo','oprr o'.replace(' ',''),'.oro.'])
 pom(c,1,15); pom(c,23,15)
 return c

def side(c):
 # Girl looks left; the other profile is an exact mirrored view.
 # Rear ponytail, bow and fall of hair.
 poly(c,[(18,5),(22,6),(23,10),(22,14),(19,14),(20,10),(18,9)],'o')
 poly(c,[(20,6),(21,7),(22,10),(21,13),(20,12),(21,9)],'m')
 line(c,21,8,21,11,'l')
 # Far leg behind near leg, side sneakers.
 pattern(c,13,23,[
 'oooooo',
 'osaoao',
 'osaoao',
 'owgogo',
 'owgogo',
 'owwowo',
 'owwwwo',
 'oooooo'])
 # Near shoe projects forward.
 rect(c,11,29,5,2,'o'); rect(c,12,29,4,1,'w')
 # Far arm, visible behind waist.
 poly(c,[(17,13),(20,15),(20,19),(18,20),(17,18)],'o')
 line(c,18,15,19,17,'a'); pix(c,19,18,'s')
 # Torso and side of the pleated skirt.
 poly(c,[(13,12),(17,12),(19,15),(18,19),(20,24),(11,24),(12,20),(11,16)],'o')
 poly(c,[(14,13),(16,13),(18,15),(17,19),(13,19),(12,16)],'t')
 rect(c,13,14,3,4,'u'); line(c,13,14,13,16,'v')
 line(c,12,14,15,15,'w'); pix(c,13,16,'r')
 line(c,13,19,17,19,'w'); line(c,13,20,18,20,'r')
 poly(c,[(13,21),(17,21),(19,24),(12,24)],'t')
 line(c,14,21,13,23,'u'); line(c,16,21,17,23,'n')
 line(c,12,23,19,23,'w')
 # Neck.
 rect(c,14,10,3,3,'o'); rect(c,14,11,2,2,'s')
 # Side face, protruding nose, chin.
 poly(c,[(13,3),(18,3),(20,5),(20,9),(18,11),(13,11),(12,10),(11,9),(10,8),(11,7),(11,5)],'o')
 poly(c,[(13,4),(18,4),(19,5),(19,9),(17,10),(13,10),(12,9),(11,8),(12,7),(12,5)],'s')
 # Hair cap and side locks.
 poly(c,[(13,4),(18,4),(19,5),(19,9),(17,11),(16,10),(17,7),(14,6),(12,6),(12,5)],'h')
 line(c,13,4,17,4,'l'); line(c,17,5,18,6,'m')
 line(c,18,6,18,9,'m'); pix(c,17,10,'m')
 pix(c,12,7,'o'); pix(c,12,9,'a'); pix(c,15,8,'k'); pix(c,15,9,'a')
 # Bow at ponytail tie.
 pattern(c,18,2,['oo.oo','ororo','oprr o'.replace(' ',''),'.oro.'])
 # Near arm bends forward to carry both pom-poms.
 poly(c,[(13,14),(15,15),(14,19),(10,20),(8,18),(10,16),(12,17)],'o')
 line(c,13,15,13,18,'k'); line(c,10,18,12,18,'s')
 pom(c,6,16)
 return c

f=front(new_canvas(32,32,name='front'))
b=front(new_canvas(32,32,name='back'),True)
l=side(new_canvas(32,32,name='left'))
r=l.copy(name='right').mirror('h')
result.blit(f,0,0).blit(b,32,0).blit(l,0,32).blit(r,32,32)
assert result.stats()['colors_used'] <= 86
save('cheerleader_four_views',result)
view(result,scale=8,margin=0)
finish(result)
