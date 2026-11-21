f1=new_canvas(80,78,name='ready')
f1.blit(input_canvas,10,8)
f2=new_canvas(80,78,name='heavy_attack')
# Broad tapered swing ribbon, behind the attacking silhouette.
f2.path('M 36 8 Q 66 5 75 30 Q 80 48 67 65 L 63 58 Q 73 42 67 28 Q 60 12 36 8 Z',31)
f2.path('M 49 10 Q 72 17 73 36 Q 73 47 68 53 Q 71 35 64 24 Q 59 16 49 10 Z','#dccaca')
f2.path('M 41 4 Q 65 4 76 24',31,fill=False)
f2.line(76,28,77,34,31)
# Repose original richly detailed body. Remove raised weapon and forearm.
for y in range(8,61):
 for x in range(43):
  p=input_canvas.get(x,y)
  if p==0 or p==41: continue
  if y<15 and x>=22: continue
  if y<24 and x>=27: continue
  if y>=47 and 26<=x<=38: continue
  if y>=50 and x<19: continue
  lean=3 if y<32 else (2 if y<42 else 0)
  f2.set(x+10+lean,y+10,p)
# Rear boot anchors the weight, copied independently.
input_canvas.select(9,50,10,9).copy_to(18,60,f2,mode='over')
# Forward left leg: bent thigh and shin, outlined and plated.
f2.poly([(39,51),(46,51),(51,57),(53,63),(60,66),(60,70),(47,70),(44,65),(43,60),(38,57)],1)
f2.poly([(40,52),(45,52),(49,57),(46,61),(42,58)],16)
f2.line(41,52,46,57,18)
f2.poly([(47,58),(50,59),(52,65),(48,67),(45,63)],15)
f2.line(47,59,49,64,31)
f2.line(48,59,51,64,20)
f2.poly([(49,65),(53,65),(54,67),(58,67),(59,69),(48,69),(47,67)],16)
f2.line(49,66,53,66,20)
f2.line(49,68,57,68,5)
# Swinging arm, shoulder to lowered gauntlet.
f2.poly([(43,32),(48,33),(50,37),(54,40),(53,45),(49,47),(45,43),(43,39)],1)
f2.poly([(44,33),(47,34),(48,38),(46,40),(44,38)],15)
f2.line(44,33,47,35,18)
f2.poly([(47,38),(50,39),(53,42),(51,45),(48,44),(46,41)],21)
f2.line(48,39,51,42,5)
f2.line(47,40,50,43,18)
# Hammer haft extends from the clenched hand toward the impact.
f2.line(49,40,65,58,1)
f2.line(48,41,64,59,1)
f2.line(50,40,66,58,1)
f2.line(49,41,65,59,7)
f2.line(50,42,65,58,10)
f2.line(51,43,64,57,20)
for x,y in [(54,47),(57,50),(60,53)]:
 f2.line(x-1,y,x+1,y-1,7)
f2.poly([(48,40),(51,40),(54,43),(52,46),(49,45),(47,43)],1)
f2.poly([(49,41),(51,41),(53,43),(51,45),(49,44)],15)
f2.line(49,41,51,42,31)
f2.line(49,43,51,44,5)
# Original hammer head, turned end for end to land below the hand.
head=new_canvas(15,11,name='hammer_part')
for y in range(11):
 for x in range(16,31):
  if (y<8 or x>=21) and not (y>=9 and x>=26):
   head.set(x-16,y,input_canvas.get(x,y))
head.select(0,0,15,11).rotate(180).copy_to(59,55,f2,mode='over')
# Small trailing flecks at the end of the arc.
f2.line(73,60,71,64,31)
f2.line(75,65,73,67,31)
view(f1,scale=5)
view(f2,scale=5)
finish([f1,f2])
