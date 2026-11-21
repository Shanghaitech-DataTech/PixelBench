src=input_canvas.select(0,0,66,119).resize(28,50).preview()
# Work on the source sprite's original coarse pixel grid.
def put(c,x,y,rows):
 for j,row in enumerate(rows):
  for i,ch in enumerate(row):
   c.set(x+i,y+j,None if ch=='.' else ord(ch)-96)
def patch(c,s,x,y,w,h,dx,dy):
 s.select(x,y,w,h).copy_to(dx,dy,c,mode='over')
# Recover the obscured shoulder and bodice from their matching visible side.
body=src.copy()
for y in range(22,32):
 for x in range(14,28): body.set(x,y,src.get(27-x,y))
# A turned torso is slightly narrower with the near shoulder offset.
def turnbody():
 c=new_canvas(28,50)
 for y in range(22,50):
  for x in range(3,26):
   sx=round((x-14)/0.85+13.5)
   if 0<=sx<28:c.set(x,y,body.get(sx,y))
 return c
right=turnbody()
# Rounded crown and curls retain the exact source texture.
src.select(1,0,26,15).resize(23,15).copy_to(3,0,right)
put(right,3,10,[
 'acfacafccfaggggafccfaca',
 '.adfaadabcagggggacbadaa',
 '.abdcaabaaaaggggaaaaba',
 '..acdagaaccgggggccaaha',
 '..iaaachhghgggggghhcaa',
 '..iggahaaajhgggghjaaha',
 '...igaakkiikhggkiikaag',
 '...ihjhlimmlggglmilhgi',
 '....iijgnnnlggglnnggi',
 '.....ihhggggggggggggi',
 '......ijohgggggggghji',
 '.......jjohggggghoji.',
 '.........jjjjjjjjji..'])
# Profile nose and cheek, small far eye, larger near eye.
right.rect(23,18,2,2,7).set(25,19,8).set(24,20,8)
# Near ear and temple curls.
put(right,5,13,['acdaa','iaach','iggah','ijgha','.ijji'])
# Far side braid lies along the outer shoulder.
src.select(19,19,8,12).resize(5,12).copy_to(22,20,right,mode='over')
# Opposite angle: keep the side braid on the character's anatomical left.
left=turnbody().mirror()
head=right.select(0,0,28,23).flip().preview()
left.blit(head,0,0)
# Replace the far braid fragment with the visible shoulder before placing near braid.
for y in range(23,32):
 for x in range(0,8):left.set(x,y,body.get(x,y))
# Remove stray far-side hair from the mirrored face margin.
left.rect(1,20,3,3,None)
patch(left,src,19,19,8,12,18,20)
# Rear: same sleeves, skirt, hands and waist; no face or front neckline.
back=body.copy()
back.rect(0,0,28,22,None)
patch(back,src,0,0,28,14,0,0)
put(back,2,10,[
 'acfacafccfaccbccafccfacafca'[:24],
 'adfaadabccddccddccbadaafda',
 'abdcaabccdeeddddeccbaacdba',
 '.acddccddeffddffeddccddca.',
 '.abccddddeeddddeeddddcbba.',
 '..acddccddddccddddccddca..',
 '..abceeddccdbbdccddeecba..',
 '...acffeddcddcdddeffcaa...',
 '...abdeedccddccddeedba....',
 '....acddbccddccbddcaa....',
 '.....abccddddddccba......',
 '......aabccccccbaa.......'])
# Back collar closes high under the hair.
put(back,9,22,['pqqttttqqp','qsqqqqqqsq','qssqqqqssq','qssssssssq','tqssssssqt','ptqssssqtp'])
# The braid falls from the left side of the nape (viewer right from behind).
braid=src.select(19,19,8,12).flip().preview()
# Erase face pixels captured at the braid's root.
for yy in range(3):
 for xx in range(8):
  if braid.get(xx,yy) in [7,8,9,10,15]: braid.set(xx,yy,3)
back.blit(braid,2,19)
# Rear bodice seam and subtle folds.
back.line(13,30,13,36,20)
back.line(14,30,14,36,17)
back.set(14,32,19).set(14,35,19)
# Retain the same skirt palette with folds continuous from the back waist.
for c in [right,left,back]:
 pass
f1=new_canvas(66,119,name='left_45')
f2=new_canvas(66,119,name='right_45')
f3=new_canvas(66,119,name='rear')
for small,large in [(right,f1),(left,f2),(back,f3)]:
 small.select(0,0,28,50).resize(66,119).copy_to(0,0,large)
 view(large,scale=4)
finish([f1,f2,f3])
