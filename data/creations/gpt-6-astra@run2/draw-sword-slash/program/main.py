# Original sprite is preserved exactly in the first expanded frame.
W,H=112,104
ox,oy=23,27
f1=new_canvas(W,H,name='01_original')
f1.blit(input_canvas,ox,oy)
f2=new_canvas(W,H,name='02_completed_slash')
black='#020202'; edge='#120d1c'; dark='#231c2c'; cloth='#454463'; light='#69657d'; fold='#3d2c32'; skin='#f3a473'; shade='#71444c'; deep='#1b0202'; metal='#b2aeb1'; shine='#eedddd'; rust='#926e6b'
# A tapered black sweep traces the travel from the lower left to the upper right.
f2.path('M 6 85 Q 50 83 78 56 Q 96 36 104 6 Q 111 44 86 68 Q 53 91 6 85 Z',black)
f2.path('M 16 89 Q 55 94 83 76 Q 103 62 107 44 Q 100 67 82 79 Q 51 96 16 89 Z',black)
# Working sprite: the old sword hand and its handle are removed.
p=input_canvas.copy(name='pose')
p.clear(46,37,16,7)
p.clear(50,33,12,5)
# Retain the lowered right hand, scabbard, body, head and feet.
f2.blit(p,ox,oy)
# Rebuilt left sleeve rises from the character's far shoulder to a bent elbow.
f2.poly([(69,52),(74,52),(80,55),(84,53),(84,44),(90,43),(92,47),(91,59),(87,63),(81,64),(73,61)],edge)
f2.poly([(70,53),(75,54),(80,58),(85,57),(86,46),(89,46),(89,58),(86,61),(81,62),(75,59)],cloth)
f2.line(71,53,75,55,light)
f2.line(76,57,81,60,light)
f2.line(82,61,86,59,dark)
f2.line(88,50,88,56,light)
f2.poly([(69,58),(73,60),(76,64),(77,68),(72,68),(68,64)],cloth)
f2.line(73,62,75,66,dark)
# Cuff and left wrist, raised beside the face.
f2.poly([(83,45),(84,41),(89,40),(92,43),(91,47),(87,49)],edge)
f2.poly([(85,43),(88,42),(90,43),(89,47),(86,47)],skin)
f2.line(86,47,89,47,shade)
f2.line(84,46,88,48,light)
# Drawn blade: the point leads the completed up-right swing.
f2.poly([(85,41),(87,36),(104,7),(102,17),(90,40),(88,43)],edge)
f2.poly([(87,38),(102,11),(100,19),(89,40)],metal)
f2.line(88,37,103,9,shine)
f2.line(89,39,100,19,'#9b938d')
# Crossguard and hilt are aligned through the LEFT hand only.
f2.line(82,37,92,43,black)
f2.line(82,38,91,43,dark)
f2.line(83,37,92,42,metal)
f2.line(84,38,91,42,'#9b938d')
f2.poly([(86,40),(89,42),(84,51),(81,49)],black)
f2.line(87,42,83,49,fold)
f2.set(86,44,metal)
f2.set(84,47,metal)
f2.line(81,49,84,51,metal)
# Fingers wrap around the hilt; no sword is attached to the lowered right hand.
f2.poly([(84,40),(86,39),(88,40),(88,42),(86,43),(87,44),(86,46),(83,45),(82,43)],shade)
f2.poly([(84,40),(86,40),(87,41),(85,42),(86,43),(85,45),(83,44),(83,42)],skin)
f2.set(84,41,'#eedddd')
f2.set(86,43,fold)
view(f1,scale=4)
view(f2,scale=4)
# Neutral preview makes the black trail visible against transparency.
preview_bg=new_canvas(W,H,background='#b9bcc7',name='preview_background')
preview=flatten([preview_bg,f2],name='trail_check')
view(preview,scale=4)
finish([f1,f2])
