# Both frames use a shared expanded stage.
f1 = new_canvas(84,80,name='ready')
f1.blit(input_canvas,10,9)
f2 = new_canvas(84,80,name='heavy_attack')
ink='#101010'; dark='#332d32'; steel='#858086'; light='#dccaca'; gold='#c67b02'; yellow='#ffcc43'; pink='#d6007f'; wine='#3f0016'
# Ground contact shadows.
f2.ellipse(35,70,24,4,'#17003599')
f2.ellipse(51,72,13,3,'#17003599')
# Arc left behind the descending hammer: tapered, hard pixel edges.
f2.path('M 34 7 C 62 5 79 26 77 52 Q 76 61 69 66 L 64 58 C 76 37 65 17 34 7 Z','#a9a5ab')
f2.path('M 34 7 C 63 6 78 26 75 51 Q 74 57 69 62 L 67 57 C 75 34 61 15 34 7 Z','#ffffff')
f2.path('M 44 8 C 65 12 76 29 75 44', '#ffffff',fill=False)
f2.path('M 54 10 C 70 18 79 32 78 43', '#ffffd5',fill=False)
# Back of cape, visible in the widened stance.
f2.poly([(31,38),(46,34),(49,57),(53,65),(41,64),(32,59)],ink)
f2.poly([(35,40),(45,37),(46,57),(50,62),(41,61),(35,57)],wine)
f2.line(43,40,46,59,'#690039')
f2.line(44,43,47,58,pink)
f2.line(38,58,49,63,gold)
# Reuse the original pixel work, pitching the upper body into the blow.
# The hammer and raised forearm are removed; the advancing leg is redrawn below.
for y in range(8,59):
    for x in range(43):
        idx=input_canvas.get(x,y)
        if idx==0 or idx==41: continue
        if y==8 and x>=20: continue
        if y==9 and x>=22: continue
        if y==10 and x>=24: continue
        if y==11 and x>=25: continue
        if 12<=y<=23 and x>=29: continue
        if y>=39 and x>=25: continue
        lean=4 if y<25 else (3 if y<34 else 1)
        f2.set(x+10+lean,y+11,idx)
# Advancing anatomical left thigh and bent knee, broad silver plates.
f2.poly([(37,48),(43,48),(48,53),(49,59),(46,63),(39,60),(36,54)],ink)
f2.poly([(38,49),(42,49),(46,53),(46,58),(41,58),(38,54)],'#332d32')
f2.poly([(40,50),(43,51),(46,54),(45,58),(41,57),(39,54)],steel)
f2.line(40,50,44,53,light)
f2.poly([(40,57),(46,56),(49,59),(47,63),(41,62),(39,59)],'#c67b02')
f2.line(41,57,46,57,'#ffe38c')
f2.line(41,61,47,61,'#804018')
# Boot: original engraved metal pixels, carried forward and down.
for y in range(48,58):
    for x in range(26,38):
        idx=input_canvas.get(x,y)
        if idx in (0,41): continue
        # Trim background cape to retain only the boot silhouette.
        if y<50 and x>31: continue
        if y==50 and x>32: continue
        if y==51 and x>33: continue
        if y==52 and x>34: continue
        f2.set(x+20,y+16,idx)
# Low, driving weapon arm, shoulder to wrist.
f2.poly([(40,33),(46,32),(49,35),(49,39),(53,43),(51,48),(46,47),(43,42),(39,40)],ink)
f2.poly([(41,34),(45,33),(48,35),(47,39),(43,40),(40,38)],gold)
f2.line(42,34,46,34,'#ffffd5')
f2.poly([(42,36),(46,35),(47,37),(45,39),(42,39)],yellow)
f2.poly([(44,40),(48,39),(51,42),(49,45),(46,44)],steel)
f2.line(46,40,49,42,light)
f2.line(45,41,47,44,'#5a565a')
# Long hammer haft runs through the gauntlet toward the impact.
f2.line(46,37,66,60,ink)
f2.line(45,38,65,61,ink)
f2.line(46,38,66,61,'#512a13')
f2.line(47,38,67,61,'#af7a18')
f2.line(47,39,66,60,'#d1b563')
# Closed steel fist around the haft.
f2.poly([(48,42),(51,41),(54,44),(54,47),(51,49),(48,46)],ink)
f2.poly([(49,42),(51,42),(53,44),(52,47),(50,47),(48,45)],steel)
f2.line(49,42,52,44,light)
f2.set(50,45,'#ffffff')
f2.line(51,46,53,45,'#5a565a')
# Original hammer head, flipped to the end of the descending shaft.
head=new_canvas(14,12,name='hammer_head')
for y in range(12):
    for x in range(17,31):
        if y==8 and x<20: continue
        if y==9 and x<22: continue
        if y==10 and x<25: continue
        if y==11 and x<26: continue
        idx=input_canvas.get(x,y)
        if idx: head.set(x-17,y,idx)
head.select(0,0,14,12).rotate(180).copy_to(61,56,f2,mode='over')
# Faceted highlights and seams match the original armor's pixel clusters.
f2.line(42,51,45,54,'#a9a5ab')
f2.set(42,51,'#ffffff')
f2.line(39,54,41,56,'#5a565a')
f2.line(43,58,46,58,'#ffcc43')
f2.set(41,58,'#ffffd5')
f2.line(42,60,46,60,'#804018')
f2.set(47,59,'#ffe38c')
f2.line(43,62,46,62,'#332d32')
f2.line(41,36,41,38,'#804018')
f2.line(43,37,46,37,'#ffe38c')
f2.set(47,36,'#c67b02')
f2.line(48,40,50,42,'#a9a5ab')
f2.set(48,40,'#ffffff')
view(f1,scale=6)
view(f2,scale=6)
finish([f1,f2])
