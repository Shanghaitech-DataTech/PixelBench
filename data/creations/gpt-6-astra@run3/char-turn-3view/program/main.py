chars='.123456saohtuivgABCDEFGHI'
src=new_canvas(28,50,name='source_grid')
for y in range(50):
 for x in range(28):
  src.set(x,y,input_canvas.get(min(65,round((x+.5)*66/28-.5)),min(118,round((y+.5)*119/50-.5))))
def row(c,y,x,s):
 for i,ch in enumerate(s):
  if 0<=x+i<28:c.set(x+i,y,chars.index(ch))
def rows(c,y,seq):
 for j,(x,s) in enumerate(seq):row(c,y+j,x,s)
def patch(c,coords,col):c.poly(coords,chars.index(col))
# Build the underlying outfit without the front braid, using its unobscured half.
body=src.copy(name='outfit_template')
for y in range(21,31):
 for x in range(14,28):body.set(x,y,src.get(27-x,y))
# A three-quarter torso: narrower far shoulder, broad near sleeve, displaced neckline.
def base_right():
 c=new_canvas(28,50,name='quarter_base')
 for y in range(21,50):
  # preserve the vertical scale and the original folds, but project their positions
  for x in range(3,26):
   sx=round((x-3)*27/22)
   c.set(x,y,body.get(sx,y))
 # sculpt neckline and breastplate oriented towards the right
 rows(c,21,[(8,'AAAAhhgassaghh'),(6,'ABBBBBAAhhhhhhA'),(5,'ABCCDBBDAaggggaA'),(4,'AECDCDBBDEaggaEBA'),(4,'ABDBDDBDDBEaaEBDA'),(5,'ABDDEBDDDDEssEDBA'),(6,'AAABBDCDDDEEDDBA'),(7,'ABBDCCDDDDDDDDA'),(7,'AABBDDDDDDDDDBA'),(8,'AAEEEBDDDBEEBA'),(9,'ABEBDDDDDBEBA'),(9,'AEBEDDDDDEBA'),(9,'EABEBDDDBEBA'),(9,'AAEBBBBEEBA'),(8,'BABAEBBEEABA'),(8,'ABBEBBBBEBBA')])
 # near arm is larger and one pixel lower
 rows(c,27,[(4,'ohAAA'),(4,'ogagA'),(4,'osahA'),(3,'ogFgho'),(3,'oFFhoG'),(2,'ogFsghH'),(2,'osFssgH'),(2,'ossshGA'),(2,'ohsshAE'),(3,'ogsaAE'),(4,'ooAEB')])
 # far arm, partially hidden by torso
 rows(c,27,[(23,'Ah1'),(23,'Aao'),(23,'haso'),(23,'hgFo'),(23,'ohFo'),(23,'hgsFo'),(23,'gssFo'),(23,'hssso'),(23,'hs ho'.replace(' ','')),(23,'asgo'),(23,'Aoo')])
 # back and side mass of the curly hair
 rows(c,9,[(2,'134241365511111155631'),(2,'136131633611111163361'),(3,'14611412313333132141'),(3,'1243112113444431211'),(4,'13413314345543121'),(4,'111334155433311'),(4,'1341433655111'),(4,'o14314543111'),(5,'o1341634311'),(5,'o131345311'),(6,'o1134311'),(7,'113411'),(8,'1111')])
 # face, offset toward the turning direction; near ear remains visible
 rows(c,13,[(11,'assssssssss'),(11,'assssssssssa'),(8,'oss1aassssssa'),(8,'osah11hassah1'),(9,'oahutootasato'),(10,'oasuoiusssuio'),(11,'oasvvussssuv'),(12,'oassssssssa'),(13,'ohgassssagh'),(14,'hhgassagh'),(15,'hhhhhhh')])
 # upper hair sweeps towards the face; project the part to screen right
 for y in range(0,14):
  for x in range(1,27):
   # redistribute left and right lobes around displaced part
   if x<=17:sx=round(x*13/17)
   else:sx=round(13+(x-17)*14/9)
   sx=max(0,min(27,sx))
   p=src.get(sx,y)
   if p:c.set(x,y,p)
 # Align the two eyes on the same brow, with the far eye foreshortened.
 rows(c,14,[(11,'assssssssssssa'),(12,'assssssssssssa'),(12,'assssssssssssa'),(12,'asssssssssssssa'),(12,'asssssssssssssa'),(13,'assssssssssa'),(14,'hgassssagh'),(15,'hgassagh'),(16,'hhhhhh')])
 for yy,near,far in [(15,'111h','111'),(16,'toot','tot'),(17,'uoiu','uoi'),(18,'svvu','uvv')]:
  row(c,yy,13,near)
  row(c,yy,22,far)
 row(c,18,25,'s')
 return c
q=base_right()
# Hair braid uses the same interlocking dark brown clusters as the source.
def braid(c,x,y,near=True):
 seq=['..2311..','.122411.','1336311.','134212161','156412123','164123412','113414611','16554121.','14311341.','.142111..','..1311...','..111....']
 if not near:seq=['.2311.','12241.','336311','342161','564121','641341','134161','655121','431341','.4211.','.131..','.11...']
 for j,s in enumerate(seq):
  for i,ch in enumerate(s):
   if ch!='.' and 0<=x+i<28:c.set(x+i,y+j,chars.index(ch))
# Left turn: left-side braid is on the far shoulder.
f1small=q.copy(name='left_turn_grid')
braid(f1small,22,20,False)
# Right turn: the braid is now on the near shoulder, not mirrored to the wrong side.
f2small=q.copy(name='right_turn_grid').mirror('h')
braid(f2small,17,20,True)
# Rear outfit uses the same sleeves and pleated hem.
f3small=body.copy(name='rear_grid')
for y in range(21):
 for x in range(28):f3small.set(x,y,None)
# rear collar and uninterrupted back of bodice
rows(f3small,21,[(5,'AAAAAhhhhhhhhAAAAA'),(4,'ABBBBBAgggggABBBBBA'),(3,'ABCCDBBAAAAABBDCCBA'),(2,'AECDCDBBDDDDBBDCDCEA'),(2,'ABDBDDBBDDDDBBDDBDBA'),(3,'ABDDEBDDDDDDDDDBEDBA'),(4,'AAABBDDDDDDDDBBAAA'),(6,'ABBDDDDBBDDDDBBA'),(6,'AABBDDBEBDDDBBAA'),(7,'AAEEBDBEBDD EAA'.replace(' ','')),(8,'ABEBDBEBDDBA'),(8,'AEBEDBE BDEBA'.replace(' ','')),(8,'EABEBBE BBEBA'.replace(' ','')),(7,'AAEBBBBBBBB EAA'.replace(' ','')),(7,'BABAEBBBBEABAB'),(6,'ABBEBBBBBBEBBBA')])
# back hair silhouette: same curls and crown, no facial features
for y in range(0,10):
 for x in range(28):f3small.set(x,y,src.get(x,y))
rows(f3small,10,[(1,'1361316336444436336131631'),(2,'146114124355554321411641'),(2,'124331245344443542133421'),(3,'1341344534334345441341'),(3,'1143356342332436533411'),(3,'1341433454334543341431'),(4,'14316345434454361341'),(4,'11334563433436543311'),(5,'134453434443435441'),(6,'1133454333454331'),(7,'11334344343311'),(8,'111334443311'),(10,'11111111')])
# Braid remains on the anatomical left (screen left from behind).
braid(f3small,5,19,True)
# Expand on exactly the same coarse pixel grid as the input.
def output(small,name):
 c=new_canvas(66,119,name=name)
 for y in range(119):
  for x in range(66):c.set(x,y,small.get(min(27,int((x+.5)*28/66)),min(49,int((y+.5)*50/119))))
 return c
f1=output(f1small,'frame_1_left_45')
f2=output(f2small,'frame_2_right_45')
f3=output(f3small,'frame_3_rear')
view(f1,scale=4)
view(f2,scale=4)
view(f3,scale=4)
finish([f1,f2,f3])
