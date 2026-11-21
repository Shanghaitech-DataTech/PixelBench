W,H=120,104
ox,oy=20,22
f1=new_canvas(W,H,name='frame_1')
f1.blit(input_canvas,ox,oy)
f2=new_canvas(W,H,name='frame_2')
# Broad, tapered black ribbon records the completed rising sweep.
f2.path('M 9 83 Q 51 94 86 72 Q 108 55 110 13 Q 124 51 99 77 Q 61 106 9 83 Z','#020202')
f2.path('M 20 88 Q 61 98 88 81 Q 70 98 43 96 Z','#020202')
f2.line(100,70,107,61,'#020202')
s=input_canvas.copy(name='pose')
# Remove the sword arm and its old grip, leaving the low scabbard hand intact.
s.poly([(48,27),(56,28),(61,36),(61,43),(47,43),(45,38),(48,34)],None)
f2.blit(s,ox,oy)
ink='#120d1c'; dark='#231c2c'; cloth='#454463'; light='#69657d'; skin='#f3a473'; shade='#71444c'
# Left sleeve: shoulder, forward elbow, and raised forearm.
f2.poly([(65,46),(71,47),(77,54),(81,49),(85,39),(92,41),(90,54),(82,65),(76,65),(69,59)],ink)
f2.poly([(66,48),(70,49),(77,58),(80,56),(85,44),(89,45),(86,55),(80,62),(76,62),(70,57)],cloth)
f2.line(70,49,77,56,light)
f2.line(77,60,81,59,light)
f2.poly([(82,49),(86,40),(91,42),(88,51)],dark)
f2.line(84,44,89,46,light)
# Blade at the end of the draw, rising to the upper right.
f2.poly([(89,35),(108,7),(106,18),(93,38)],ink)
f2.poly([(90,34),(107,9),(104,19),(92,36)],'#b2aeb1')
f2.line(91,34,107,9,'#eedddd')
f2.line(93,34,104,19,'#69657d')
# Hilt and guard stay aligned with the blade, held only by the raised left hand.
f2.line(84,44,91,34,ink)
f2.line(85,44,92,34,ink)
f2.line(85,42,90,35,'#3d2c32')
f2.line(87,33,96,39,ink)
f2.line(88,33,96,38,'#9b938d')
# Closed fingers around the grip.
f2.poly([(84,38),(87,36),(91,38),(91,41),(88,45),(83,43)],ink)
f2.poly([(85,38),(87,37),(90,39),(89,42),(86,44),(84,42)],skin)
f2.line(87,40,89,41,'#71444c')
f2.set(85,43,'#71444c')
f2.line(83,44,88,46,ink)
preview=new_canvas(W,H,background='#aaa5b3',name='contrast_preview')
preview.blit(f2,0,0)
view(preview,scale=4)
finish([f1,f2])
