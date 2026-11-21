# Work on the character's original 28 x 50 logical pixel grid.
S=new_canvas(28,50,name='source_grid')
for y in range(50):
 for x in range(28): S.set(x,y,input_canvas.get(min(65,int((x+.5)*66/28)),min(118,int((y+.5)*119/50))))
C={chr(96+i):i for i in range(1,24)}
C['.']=0

def rows(c,x,y,text):
 for j,row in enumerate(text.strip('\n').splitlines()):
  for i,ch in enumerate(row): c.set(x+i,y+j,C[ch])
def patch(c,src,x,y,w,h,dx,dy,flip=False):
 for j in range(h):
  for i in range(w):
   p=src.get(x+(w-1-i if flip else i),y+j)
   if p: c.set(dx+i,dy+j,p)
def skirt(c,direction=0):
 for y in range(36,50):
  for x in range(28):
   sx=round(13.5+(x-13.5)/.93)
   if 0<=sx<28:
    p=S.get(sx,y)
    if p in (16,17,18,19,20):c.set(x,y,p)
 # shift the front pleats toward the turned centre
 if direction:
  for y in range(37,49):
   for x in range(9,21):
    sx=max(7,min(22,x-direction*2))
    c.set(x,y,S.get(sx,y))

head='''
.......aaaaaa..aaaaa........
......abcccbbaabbccbaa......
.....abcdcccccbbccdcba......
....abcdeccddcccdedcbaa.....
...abcdeedccddcddedcbca.....
...acdedfeddddddeedcddca....
..abdedcfedcccddeffcddca....
..acdecbdedcabbcdeecbedca...
..acdfdaedcbaccbaedcadfca...
..acdbdacfeaaaaaaefcadbca...
..acfacafccaggggggafccaca...
...adfaadabagg gggacbada....
...abdcaabaaggggggaabaca....
....acdacaacggggggccahaa....
....iaaaccchhgggggghhcai...
....iggahajhggggggghjahi...
.....igaaakiikgggggkikai...
.....ihjhg limlggggglmi....
......iijggnnlgggggglni....
.......ihgggggggggggggi....
........ijohgggggggghji....
.........jjohggggghojj.....
'''.replace(' ','g')
# Near side has a full eye; the far eye is compressed against the contour.
R=new_canvas(28,50,name='rightward_grid')
skirt(R,1)
# Continuous side planes join the bodice, sleeves and waist.
R.poly([(7,23),(22,23),(23,29),(22,34),(24,38),(8,38),(9,32)],16)
R.poly([(17,25),(22,25),(21,33),(23,37),(18,37)],20)
# far arm and sleeve
rows(R,21,23,'''
.pppp.
pqqqp.
pssqp.
pstpp.
.pji..
.ihhi.
.ighhi
.iughi
.igugi
.iggji
.ighji
..iji.
''')
# Torso turned toward screen right
rows(R,7,21,'''
..ppppjjjjj...
.pqqqqphhojp..
pqsssqpthhqp.
pqsrssqthtsp.
pqsqsssqtsrp.
pqssqqsssrsp.
.pppqqsssssp.
...pqqssssp..
...ptqqssqp..
...ptqssqtp..
...ptqssqtp..
..pttqssqtp..
..ptpqqqtpqp.
.pttpqtqtqqp.
.ptqpqqtqqqp.
pqtqstqssqtp.
''')
# near arm has original skin clusters and cuff
patch(R,S,0,27,7,11,3,27)
# fill upper shoulder, preserving original puff-sleeve facets
rows(R,4,22,'''
..ppppp.
.pqqqqqp
pqrrsqsq
ptrsrsqs
pqsqssqs
.pqsstqp
..ppppp.
''')
rows(R,0,0,head)
# braid as seen on far side, most of it occluded by the shoulder
rows(R,23,20,'''
aa..
bca.
dcaa
cfca
abfa
bcaa
daba
fca.
daa.
aa..
''')
# Close the side seam under the receding arm, with shaded fabric folds.
for y in range(27,37):
 for x in range(19,24):
  if R.get(x,y)==0: R.set(x,y,16 if x>21 else 20)
rows(R,20,32,'''
tpq
pqt
ptq
tqp
''')
# Small stepped profile and asymmetric fringe establish the head turn.
rows(R,12,10,'''
aagggg
aagggg
aaaggg
''')
R.set(23,18,7)
R.set(23,19,8)
# the opposite turn keeps the anatomical braid on the near side
L=new_canvas(28,50,name='leftward_grid')
for y in range(50):
 for x in range(28): L.set(x,y,R.get(27-x,y))
# Remove the far braid copied by reflection and restore sleeve behind it.
L.rect(0,21,5,9,0)
rows(L,3,22,'''
.ppp
pqqp
psqp
ptpp
pji.
ihhi
ighi
iugi
''')
# The original left-shoulder braid remains on the visible near shoulder.
for y in range(19,31):
 for x in range(16,27):
  if 1<=S.get(x,y)<=6: L.set(x+1,y,S.get(x,y))
# Rear torso and same full skirt, seen from behind.
B=new_canvas(28,50,name='rear_grid')
skirt(B)
patch(B,S,0,27,7,11,1,27)
patch(B,S,21,27,7,11,20,27)
rows(B,5,21,'''
..ppppjjjjpppp..
.pqqqqphhpqqqqp.
pqssqqqqqqqqssqp
pqsrssqqqqssrsqp
pqsqsssttsssqspq
pqssqqsttsqqssqp
.ppqqqsttsqqqpp.
..pqqssttssqqp..
..ptqssttssqtp..
..ptqssttssqtp..
..ptqqsttsqqtp..
..ptpqsttsqptp..
.pttpqqttqqpttp.
.ptqpqtqqtqpqtp.
ptqpqqqttqqqpqtp
pqtqsqqttqqsqtqp
''')
# Back of the same parted, waved hair, gathered to the character's left.
rows(B,0,0,'''
.......aaaaa....aaaaa.......
......abcabbaaaabbacba......
.....abcabccccbcccbacba.....
....aacdaccddccddccadcaa....
...abadedbccddcdccbdedaba...
...acaddedcddddddcdeddaca...
..abdbcefeddccccddefecbdba..
..acdeccbddccccccddbccedca..
.abdcfdaedddcddcdddeadfcdba.
.acdbdacfeeddccddeefcadbdca.
.acfacafccfddccddfccfacafca.
..adfaadabcdcddcdcbadaafda..
..abdcacbceddddddecbcacdba..
...acdadcfedccccdefcdadca...
...aaccdeccddccddecddccaa...
...abcdfdacddccddcadfdcba...
....acdbdacddccddcadbdca....
....acfacafddccddfacafca....
.....adfaadcdccdcdaafda.....
.....abdcacbccddcbcacaa.....
......acdedccbbccdecaa......
.......acfeddccdeeca........
........acfedcdeca.........
.........acccccaa..........
''')
# braid is still draped on the left side; visible along the back shoulder
for y in range(19,31):
 for x in range(16,27):
  if 1<=S.get(x,y)<=6: B.set(29-x,y+1,S.get(x,y))
# Narrow end of plait, retain dark outline and woven brown highlights
rows(B,5,29,'''
aafcaa
.acdaa
..aaa.
''')
# restore rear shoulder edge at the far side

# Export to the exact original physical pixel dimensions using nearest cells.
def full(c,name):
 o=new_canvas(66,119,name=name)
 for y in range(119):
  for x in range(66): o.set(x,y,c.get(min(27,int(x*28/66)),min(49,int(y*50/119))))
 return o
f1=full(R,'frame_1_left_45')
f2=full(L,'frame_2_right_45')
f3=full(B,'frame_3_rear')
view(f1,scale=4)
view(f2,scale=4)
view(f3,scale=4)
finish([f1,f2,f3])
