# Frame one preserves every source pixel on an expanded canvas.
W,H=76,76
ox,oy=12,7
f1=new_canvas(W,H,name='ready')
f1.blit(input_canvas,ox,oy)
f2=new_canvas(W,H,name='heavy_attack')
# Broad white crescent follows the head of the descending hammer.
f2.path('M 35 6 Q 64 9 70 32 Q 74 47 63 58 L 58 51 Q 68 40 62 26 Q 55 13 35 6 Z','#d7dce8')
f2.path('M 39 8 Q 63 12 68 33 Q 71 44 63 54 L 60 50 Q 67 39 61 26 Q 54 15 39 8 Z','#ffffff')
f2.path('M 48 9 Q 68 17 72 36', '#ffffff',fill=False)
f2.line(70,42,69,46,'#ffffff')
# Rebuild the silhouette from the original pixels, excluding the raised weapon
# and arm. The torso pitches forward two pixels during the blow.
for y in range(8,61):
    for x in range(43):
        col=input_canvas.get(x,y)
        if col==0: continue
        if y==8 and x>=20: continue
        if 9<=y<15 and x>=22: continue
        if y<22 and x>=24: continue
        if 22<=y<28 and x>=28: continue
        if x>=25 and y>=43: continue # advancing left leg
        dx,dy=(1,2) if y<34 else (0,0)
        f2.set(x+ox+dx,y+oy+dy,col)
# Restored cape in the space vacated by the upraised forearm.
f2.poly([(42,32),(46,33),(47,42),(47,52),(44,54),(40,47)],'c7')
f2.line(46,35,46,49,'c13')
f2.line(45,41,45,48,'c8')
# Advancing left leg, original knee and boot retain their plate highlights.
for y in range(40,57):
    for x in range(25,39):
        col=input_canvas.get(x,y)
        if col!=0 and col!=41:
            f2.set(x+ox+7,y+oy+5,col)
# Thigh joins hip to the advanced knee.
f2.poly([(36,43),(42,44),(49,52),(46,56),(41,53),(36,48)],'c0')
f2.poly([(38,44),(41,45),(46,51),(43,53),(39,49)],'c15')
f2.line(40,45,46,50,'c4')
f2.line(39,45,43,48,'c30')
f2.line(43,51,46,53,'c21')
# New dropped shoulder, bent forearm and gauntlet.
f2.poly([(39,30),(44,30),(47,34),(47,37),(52,39),(51,44),(47,45),(42,40),(40,36),(37,34)],'c0')
f2.poly([(40,31),(43,31),(46,34),(45,37),(41,37),(39,34)],'c15')
f2.poly([(40,31),(43,31),(45,33),(42,34),(39,33)],'c17')
f2.line(41,31,43,31,'c30')
f2.poly([(42,36),(45,35),(46,38),(49,39),(47,42),(44,40)],'c14')
f2.line(43,36,46,39,'c4')
f2.line(43,39,46,42,'c21')
f2.line(44,40,47,43,'c24')
# Hammer haft: from a counterweight behind the fist to the dropped head.
f2.line(44,34,61,51,'c0')
f2.line(43,34,60,51,'c0')
f2.line(44,34,61,50,'c9')
f2.line(45,35,60,50,'c6')
f2.line(47,38,49,40,'c25')
# Plate gauntlet closes around the shaft.
f2.poly([(47,38),(50,39),(52,41),(50,44),(47,43),(46,41)],'c0')
f2.poly([(48,39),(50,40),(51,41),(49,43),(47,41)],'c14')
f2.line(48,39,50,41,'c17')
f2.set(48,40,'c30')
f2.line(48,42,49,43,'c15')
# Exact original hammer head, turned over to lead the impact.
head=new_canvas(14,11,name='hammer_head')
for y in range(9):
    for x in range(17,29):
        col=input_canvas.get(x,y)
        if col: head.set(x-16,y+1,col)
turned=head.select(0,0,14,11).rotate(170).preview()
f2.blit(turned,54,46)
# Small white accent at the leading edge of the heavy swing.
f2.line(65,59,68,61,'#ffffff')
f2.set(70,59,'#ffffff')
view(f1,scale=6)
view(f2,scale=6)
finish([f1,f2])
