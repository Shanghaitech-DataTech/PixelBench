# Offshore maintenance, a 64-pixel scene
result = new_canvas(64,64,background='#b8d7df',name='offshore_maintenance')
c=result
sky='#b8d7df'; pale='#dce8e5'; haze='#c9dee0'
# Broad quiet sky and horizontal haze
c.rect(0,26,64,15,haze)
c.rect(0,37,64,6,'#dbe6df')
c.rect(2,10,15,2,'#cee2e5'); c.rect(6,8,8,2,'#cee2e5')
c.rect(19,17,10,1,'#dce8e5')
# Distant turbine towers and their three individual blades
for x,y,base in [(12,23,43),(25,29,43)]:
    c.line(x,y+1,x,base,'#7f9fa9')
    c.line(x+1,y+2,x+1,base,'#edf1e7')
    if x==12:
        c.line(x,y,x+2,10,'#eff3e9')
        c.line(x,y,x-10,y+6,'#eff3e9')
        c.line(x,y,x+9,y+8,'#eff3e9')
        c.set(13,12,'#eff3e9')
    else:
        c.line(x,y,x+1,20,'#edf1e7')
        c.line(x,y,x-7,y+4,'#edf1e7')
        c.line(x,y,x+6,y+5,'#edf1e7')
    c.rect(x,y,2,2,'#f6f4df')
    c.rect(x,base-2,2,3,'#8f9f92')
# Distinct ocean plane
c.rect(0,43,64,21,'#367a91')
c.rect(0,43,64,2,'#6d9fa9')
c.line(0,47,17,47,'#5495a5'); c.line(19,45,28,45,'#9bbfc0')
c.line(2,44,9,44,'#d5e2d7');c.line(10,45,14,45,'#9bbfc0')
c.rect(0,54,64,10,'#286077')
c.poly([(0,51),(8,51),(11,52),(23,52),(25,50),(37,50),(39,52),(50,52),(54,50),(63,50),(63,56),(0,56)],'#32758a')
# Massive near tower continues out of frame, preserving human scale
c.poly([(42,0),(49,0),(51,37),(39,37)],'#668390')
c.poly([(42,0),(47,0),(48,36),(40,36)],'#dce4df')
c.poly([(42,0),(44,0),(43,35),(40,35)],'#f0eee0')
c.line(48,0,50,35,'#9db4b8')
# Yellow transition piece, submerged foundation and shaded side
c.rect(39,34,13,21,'#344d59')
c.rect(40,34,10,20,'#c68e35')
c.rect(40,34,3,19,'#edbd50')
c.rect(48,34,2,20,'#977337')
c.rect(39,51,13,4,'#344d59')
# Under-deck steel brackets
c.line(29,42,40,48,'#263f50'); c.line(54,42,49,48,'#263f50')
c.line(31,42,40,46,'#6e888b'); c.line(53,42,49,46,'#718788')
# Maintenance platform: back rail and grated deck
c.line(29,34,54,34,'#465e66')
for x in [29,35,53]:
    c.line(x,34,x,39,'#526c71')
c.line(29,35,54,35,'#e8bd59')
c.rect(27,39,29,4,'#263e4c')
c.rect(28,39,27,1,'#afb9a8')
c.rect(28,40,27,1,'#e4ac43')
for x in range(30,54,4): c.set(x,41,'#788b89')
# Front railing interrupted at ladder entrance
c.line(35,35,55,35,'#f1c85f')
c.line(35,38,55,38,'#c99137')
for x in [35,43,55]:
    c.line(x,35,x,39,'#e8b54f')
c.line(27,35,27,39,'#e8b54f');c.line(27,35,30,35,'#e8b54f')
# Ladder with dark silhouette, silver rails and separate rungs
c.line(29,39,29,56,'#243e4e');c.line(34,39,34,55,'#243e4e')
c.line(30,38,30,55,'#bac5bc');c.line(34,38,34,55,'#839b9c')
for y in range(40,56,3): c.line(30,y,34,y,'#a6b5ad')
# Technician climbing: helmet, face, high-viz jacket, harness, gloves, boots
c.rect(30,44,3,2,'#263747')
c.rect(30,43,3,1,'#ffdb64');c.set(31,42,'#ffe28b');c.set(33,44,'#ffd25a')
c.set(31,45,'#e7b08a')
c.rect(30,46,3,3,'#ed763b')
c.set(31,46,'#ffb452');c.line(30,47,32,47,'#ffe28b')
c.line(29,46,29,48,'#ed763b');c.set(29,45,'#d8c5a0')
c.line(33,46,34,45,'#f49042');c.set(34,44,'#d8c5a0')
c.set(31,46,'#394958');c.set(31,48,'#394958')
c.set(30,49,'#273b50');c.line(30,49,29,51,'#273b50');c.set(28,51,'#172e40')
c.line(32,49,33,50,'#273b50');c.set(33,51,'#172e40')
# Ripples wrap around the foundation and foreground wave crests
c.line(39,55,51,55,'#8ab8bc');c.line(42,56,54,56,'#5b96a3')
c.line(4,51,10,51,'#a7cccb');c.line(10,52,16,52,'#75acb5')
c.line(0,58,6,58,'#82b7be');c.line(3,57,9,57,'#b7d6d0');c.line(10,58,15,58,'#4d8c9d')
c.line(18,55,23,55,'#73a7b0');c.line(21,54,25,54,'#a7cccb')
c.line(20,61,29,61,'#6fa5b0');c.line(24,60,31,60,'#b7d6d0');c.set(32,61,'#82b7be')
c.line(44,61,53,61,'#4d8c9d');c.line(48,60,56,60,'#89b9bd')
c.line(57,48,63,48,'#9dc3c2');c.line(59,53,63,53,'#68a2ad')
view(result)
finish(result)
