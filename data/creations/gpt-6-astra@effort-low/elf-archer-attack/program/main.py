f1=new_canvas(48,51,name='original')
f1.blit(input_canvas,6,2)
f2=new_canvas(48,51,name='full_draw')
# Repose the existing body, preserving its textured costume and face.
for y in range(47):
    for x in range(35):
        keep = (y<16 and x<24) or (16<=y<28 and x<=21) or (28<=y<40 and x<=21) or y>=40
        if not keep: continue
        if 18<=y<=24 and x<13: continue
        p=input_canvas.get(x,y)
        if p==0: continue
        dx=5
        if y>=40:
            dx=3 if x<14 else 8
        elif y>=30:
            dx=5 + (1 if x>=15 else -1)
        f2.set(x+dx,y+2,p)
# Drawn bow: deeply flexed limbs, pale inner edge, magenta bindings.
f2.path('M 34 3 L 35 7 L 40 10 L 43 15 L 44 20 L 43 26 L 40 33 L 36 37 L 34 43',1,False)
f2.path('M 35 3 L 36 7 L 41 10 L 44 15 L 45 20 L 44 26 L 41 33 L 37 38 L 35 43',2,False)
f2.path('M 34 3 L 35 8 L 40 11 L 42 15 L 43 20 L 42 26 L 39 32 L 35 37 L 34 43',7,False)
f2.path('M 34 4 L 34 8 L 39 12 L 41 16 M 41 26 L 38 32 L 34 37 L 34 42',9,False)
f2.line(34,3,22,17,13)
f2.line(22,17,34,43,13)
for x,y in [(41,13),(40,29)]:
    f2.line(x,y,x+3,y+1,10)
    f2.line(x,y+1,x+3,y+2,11)
    f2.line(x,y+2,x+2,y+3,21)
# Bow arm extended at shoulder height.
f2.poly([(23,19),(28,17),(34,17),(39,17),(42,18),(42,21),(37,22),(29,23),(24,24)],20)
f2.poly([(24,19),(29,18),(35,18),(35,21),(28,22),(24,23)],31)
f2.line(27,18,34,18,33)
f2.line(28,19,34,19,32)
f2.line(28,21,34,21,39)
f2.poly([(23,18),(27,18),(29,20),(27,24),(23,25),(21,22)],31)
f2.poly([(23,18),(26,18),(28,20),(26,22),(23,23),(22,21)],32)
f2.line(23,19,26,19,33)
f2.set(23,20,34)
f2.rect(35,17,3,5,2)
f2.rect(35,18,2,3,12)
f2.line(35,18,36,18,14)
f2.poly([(38,17),(41,17),(42,18),(42,22),(38,22)],1)
f2.rect(38,18,3,3,3)
f2.line(39,18,41,18,14)
f2.line(39,20,41,20,12)
f2.rect(43,18,2,5,10)
f2.line(43,19,43,21,23)
# Rear elbow lifted and pulled back; forearm leads to face anchor.
f2.poly([(17,19),(12,18),(8,20),(8,23),(11,25),(16,24),(22,19),(24,17),(23,15),(20,15)],20)
f2.poly([(16,19),(12,19),(9,21),(10,23),(13,24),(17,22),(21,18),(20,17)],32)
f2.line(10,21,12,20,33)
f2.line(11,23,14,23,31)
f2.poly([(13,20),(18,17),(20,18),(16,22)],3)
f2.line(14,20,18,18,12)
f2.poly([(18,16),(20,14),(23,15),(24,17),(22,19),(20,18)],2)
f2.line(20,15,22,15,14)
f2.line(19,16,22,17,12)
f2.set(22,18,3)
# Remove the isolated remnant of the original lowered hand.
f2.clear(5,26,7,2)
view(f1,scale=8)
view(f2,scale=8)
finish([f1,f2])
