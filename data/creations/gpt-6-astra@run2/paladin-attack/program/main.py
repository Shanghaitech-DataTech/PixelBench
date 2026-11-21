# Both animation frames use the same expanded stage.
f1 = new_canvas(80, 76, name='paladin_ready')
f1.blit(input_canvas, 9, 8)
f2 = new_canvas(80, 76, name='paladin_heavy_attack')
# A tapered sweep follows the head of the mace, behind the figure.
trail = new_canvas(80,76,name='weapon_sweep')
trail.path('M 30 8 C 53 0 73 15 76 34 C 79 46 73 56 65 61 L 61 53 C 72 43 72 30 63 20 C 55 11 42 7 30 8 Z', '#c9cedb')
trail.path('M 33 8 C 55 3 71 17 74 34 C 77 46 70 54 64 58 L 63 53 C 72 41 69 28 61 20 C 53 12 42 9 33 8 Z', '#ffffff')
trail.path('M 46 4 C 63 7 75 20 78 34', '#ffffff', fill=False)
trail.path('M 41 13 C 54 14 63 22 66 30', '#ffffff', fill=False)
trail.line(76,43,74,48,'#ffffff')
f2.blit(trail,0,0)
# Retain the original cape, shield and armour texture, removing the raised
# weapon and raised forearm. The upper body leans into the strike.
body = input_canvas.copy(name='body_work')
for y in range(0,11):
    for x in range(43):
        if y < 8 or x >= [20,21,25][y-8]:
            body.set(x,y,None)
for y in range(11,24):
    for x in range(28,43):
        body.set(x,y,None)
# Legs will be placed separately to create a new, wider stance.
for y in range(40,61):
    for x in range(43):
        if body.get(x,y)==41:
            body.set(x,y,None)
body.clear(10,47,22,14)
body.clear(31,51,12,10)
# Shift each scanline: head and chest lead, hips stay planted.
for y in range(8,53):
    dx = 3 if y<30 else (2 if y<39 else 0)
    for x in range(43):
        idx=body.get(x,y)
        if idx:
            f2.set(x+9+dx,y+10,idx)
# Shadow follows the widened stance.
shadow=new_canvas(80,76,name='ground_shadow')
shadow.ellipse(33,66,23,4,'c40')
shadow.ellipse(47,68,17,3,'c40')
# Isolate the boots and greaves from the original image.
back=new_canvas(13,15,name='back_leg')
for y in range(44,59):
    for x in range(10,23):
        idx=input_canvas.get(x,y)
        if idx and idx!=41: back.set(x-10,y-44,idx)
# Plant the rear foot back and low.
f2.blit(back,17,53)
# Bent leading thigh and knee, in the existing armour palette.
f2.poly([(34,49),(41,49),(49,56),(48,61),(42,63),(36,58),(33,55)],'c0')
f2.poly([(35,50),(40,50),(47,56),(45,59),(40,58),(36,55)],'c20')
f2.poly([(36,51),(39,51),(45,56),(43,58),(39,55)],'c14')
f2.line(37,51,44,56,'c17')
f2.poly([(43,56),(48,56),(51,60),(48,64),(42,62),(41,59)],'c0')
f2.poly([(43,57),(47,57),(49,60),(46,62),(43,61)],'c21')
f2.line(43,57,47,58,'c19')
f2.line(43,58,46,59,'c24')
# The paladin's left boot advances to the right, carrying the impact.
front=new_canvas(12,15,name='left_leg')
for y in range(42,57):
    for x in range(25,37):
        idx=input_canvas.get(x,y)
        if idx and idx!=41: front.set(x-25,y-42,idx)
f2.blit(front,43,55)
# Weapon arm extends down and out from the shoulder.
f2.poly([(37,32),(42,30),(47,34),(48,39),(53,43),(51,48),(46,48),(42,43),(40,39),(37,38)],'c0')
f2.poly([(38,33),(42,32),(45,35),(44,39),(40,38)],'c20')
f2.poly([(39,33),(42,33),(44,35),(43,37),(40,37)],'c14')
f2.line(39,33,42,34,'c17')
f2.poly([(42,38),(45,37),(49,41),(47,44),(44,43)],'c6')
f2.line(43,38,47,41,'c24')
f2.poly([(45,42),(49,40),(53,43),(52,47),(49,49),(45,46)],'c0')
f2.poly([(46,42),(49,41),(52,43),(50,46),(48,47),(46,45)],'c14')
f2.line(47,42,50,43,'c17')
f2.line(46,44,49,45,'c4')
# Long gold-brown mace haft, now driven down toward the ground.
f2.poly([(43,34),(46,33),(66,54),(64,57),(60,55),(42,37)],'c0')
f2.poly([(44,34),(46,35),(65,54),(63,55),(44,37)],'c6')
f2.line(45,35,64,54,'c9')
f2.line(47,36,64,53,'c24')
f2.set(44,35,'c25')
# Fingers visibly wrap around the handle.
f2.poly([(48,41),(51,40),(54,43),(53,46),(50,47),(48,45)],'c0')
f2.poly([(49,41),(51,41),(53,43),(51,45),(49,44)],'c14')
f2.line(49,41,52,43,'c17')
f2.line(49,43,51,45,'c4')
# Copy the distinctive original mace head and turn it into the strike.
head=new_canvas(13,11,name='mace_head')
for y in range(11):
    for x in range(17,30):
        if y<8 or (y==8 and 22<=x<=26) or (y==9 and 23<=x<=26):
            idx=input_canvas.get(x,y)
            if idx:head.set(x-17,y,idx)
head.select(0,0,13,11).rotate(180).copy_to(60,51,f2,mode='over')
# Ground layer goes underneath the posed character and white arc.
f2=flatten([shadow,f2],name='paladin_heavy_attack_final')
view(f1,scale=6)
view(f2,scale=6)
finish([f1,f2])
