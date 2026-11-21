f1=new_canvas(104,96,name='original')
f1.blit(input_canvas,14,18)
f2=f1.copy(name='completed_slash')
# Clear the drawn sword's original lower-left silhouette, preserving the body.
for y in range(43,54):
    for x in range(0,27):
        f2.set(x+14,y+18,None)
# Remove the old left forearm and gripping hand; rebuild the coat beneath.
f2.poly([(42,53),(49,52),(58,57),(61,64),(54,68),(44,65)],'#120d1c')
f2.poly([(44,53),(50,54),(55,58),(56,64),(48,65),(43,62)],'#454463')
f2.poly([(49,63),(56,62),(60,65),(58,69),(48,69)],'#926e6b')
# Sweeping black crescent: low-left origin, high-right terminal.
f2.path('M 16 80 Q 65 89 91 43 Q 100 27 97 10 Q 94 37 75 52 Q 51 73 16 80 Z','#020202')
f2.path('M 24 83 Q 71 82 89 55 Q 72 77 46 81 Z','#120d1c')
f2.line(19,79,28,77,'#020202')
f2.line(12,82,18,81,'#020202')
# Left arm swings across the front of the body, ending up and to the right.
f2.poly([(46,43),(51,44),(55,53),(62,49),(72,40),(78,44),(72,52),(56,63),(49,62),(44,55)],'#120d1c')
f2.poly([(46,45),(50,45),(53,55),(57,57),(71,44),(75,45),(69,52),(55,60),(50,59),(46,54)],'#454463')
f2.line(47,46,49,54,'#69657d')
f2.line(50,56,54,58,'#69657d')
f2.poly([(55,58),(69,47),(72,48),(57,61),(52,61)],'#231c2c')
# Cuff and left hand around the upward angled sword hilt.
f2.poly([(69,43),(72,39),(78,42),(76,47),(73,49),(68,46)],'#231c2c')
f2.poly([(72,40),(75,38),(79,39),(81,42),(77,46),(74,46),(71,43)],'#9b938d')
f2.poly([(73,40),(76,39),(79,40),(79,43),(76,45),(73,43)],'#f3a473')
# Blade points to the upper right at the end of the completed slash.
f2.poly([(79,36),(96,12),(92,26),(83,39)],'#020202')
f2.poly([(80,35),(95,14),(90,26),(82,37)],'#b2aeb1')
f2.line(80,35,94,16,'#eedddd')
f2.line(82,36,91,24,'#69657d')
# Guard, grip, and visible fingers establish which hand holds the sword.
f2.line(76,34,85,40,'#120d1c')
f2.line(77,34,85,39,'#9b938d')
f2.line(80,39,76,44,'#231c2c')
f2.set(78,40,'#f3a473')
f2.set(77,41,'#f3a473')
f2.set(76,42,'#f3a473')
f2.set(75,45,'#9b938d')
view(f1,scale=5)
view(f2,scale=5)
finish([f1,f2])
