# The unchanged first pose and the attack share one spacious animation canvas.
W,H=88,78
f1=new_canvas(W,H,name='01_original')
f1.blit(input_canvas,12,8)
f2=new_canvas(W,H,name='02_heavy_attack')
ink='c0'
# Keep the source's ground shadow, split to follow the two new foot positions.
for y in range(51,61):
    for x in range(43):
        if input_canvas.get(x,y)==41:
            if x<23: f2.set(x+12,y+8,'c40')
            else: f2.set(x+19,y+13,'c40')
# White sweep: a tapered arc from the raised position into the hammer head.
f2.path('M 32 6 C 52 1 73 11 81 28 C 89 44 81 60 68 66 L 63 60 C 74 51 78 40 74 28 C 68 15 51 7 32 6 Z','c30')
f2.path('M 73 24 C 82 40 76 53 64 61 L 68 64 C 78 54 83 40 76 28 Z','#e1dfeb')
f2.path('M 64 7 C 73 11 80 18 83 25','c30',fill=False)
f2.line(85,30,86,35,'c30')
# Exclude the raised hammer and hand while keeping original head/body pixels.
weapon_min={0:17,1:17,2:17,3:17,4:17,5:17,6:17,7:17,8:21,9:22,10:23,11:25,12:27,13:28,14:29,15:29,16:30,17:30,18:30,19:29,20:29,21:29,22:29}
def is_weapon(x,y):
    return y in weapon_min and x>=weapon_min[y]
# The far leg stays planted. Retain the original pixels along its silhouette.
rear_ranges={43:(15,19),44:(15,19),45:(14,21),46:(12,20),47:(12,19),48:(11,18),49:(11,18),50:(10,18),51:(10,18),52:(10,18),53:(9,18),54:(10,16),55:(10,16),56:(10,17),57:(10,16),58:(11,15)}
for y,(a,b) in rear_ranges.items():
    for x in range(a,b+1):
        p=input_canvas.get(x,y)
        if p not in (0,41): f2.set(x+12,y+8,p)
# Advance the paladin's left (screen-right) lower leg by seven pixels and down five.
front_ranges={45:(27,31),46:(27,32),47:(27,32),48:(27,32),49:(27,32),50:(27,33),51:(28,34),52:(28,36),53:(29,37),54:(29,38),55:(30,38),56:(31,37)}
for y,(a,b) in front_ranges.items():
    for x in range(a,b+1):
        p=input_canvas.get(x,y)
        if p not in (0,41): f2.set(x+19,y+13,p)
# Shear the torso toward the attack; preserve all its intricate source shading.
for y in range(8,51):
    dx=12+round((46-y)*0.14)
    for x in range(43):
        p=input_canvas.get(x,y)
        if p in (0,41) or is_weapon(x,y): continue
        # Raised arm is replaced by the extended attacking arm below.
        if 23<=y<=28 and x>=29: continue
        # Old leg silhouettes are drawn independently in their new poses.
        if y>=43 and x>=13 and x<=32: continue
        if y>=47 and x>=30: continue
        f2.set(x+dx,y+10,p)
# Shield's pointed lower tip, unaltered except for the torso's forward lean.
for y in range(51,53):
    for x in range(5,11):
        p=input_canvas.get(x,y)
        if p not in (0,41): f2.set(x+12,y+10,p)
# Dark tabard between the two legs, trimmed in the source's gold tones.
f2.poly([(33,50),(40,50),(42,58),(38,61),(32,60),(30,58)],ink)
f2.poly([(34,51),(38,52),(40,58),(37,59),(32,58)],'c7')
f2.line(34,52,32,57,'c16')
f2.line(37,53,38,57,'c8')
f2.line(32,59,38,60,'c9')
f2.line(33,59,36,59,'c21')
# Upper thigh and hip plate over the top of the tabard.
f2.poly([(32,49),(37,49),(39,52),(37,56),(32,55),(30,52)],ink)
f2.poly([(33,50),(36,50),(37,52),(36,54),(32,53)],'c15')
f2.line(33,50,36,51,'c17')
f2.set(32,51,'c30')
# Restore the engraved gold tassets so the source's armour design remains clear.
for y in range(36,46):
    for x in range(18,25):
        p=input_canvas.get(x,y)
        if p not in (0,41): f2.set(x+13,y+10,p)
# The forward thigh now lies above the cloak: its highlights turn around a bent knee.
f2.poly([(38,50),(42,50),(47,53),(50,57),(49,60),(45,61),(42,58),(40,55),(37,54)],ink)
f2.poly([(39,51),(42,51),(46,54),(48,57),(47,59),(44,58),(41,54),(38,53)],'c15')
f2.poly([(40,51),(42,52),(45,54),(46,56),(44,57),(41,54),(39,53)],'c4')
f2.line(40,51,43,53,'c17')
f2.line(40,52,42,53,'c30')
f2.line(43,55,45,57,'c34')
f2.poly([(46,56),(49,57),(48,60),(45,60),(43,58)],'c20')
f2.line(45,57,48,58,'c21')
f2.line(45,57,47,58,'c19')
f2.set(48,59,'c9')
# Arm thrust down and forward. A gold pauldron, steel elbow and vambrace.
f2.poly([(41,34),(46,34),(49,37),(50,40),(54,42),(57,45),(56,49),(52,49),(49,46),(46,43),(42,41),(40,38)],ink)
f2.poly([(42,35),(46,35),(48,38),(46,41),(42,40),(41,38)],'c21')
f2.line(43,35,46,36,'c19')
f2.line(42,36,41,38,'c24')
f2.poly([(43,38),(46,37),(48,39),(46,41),(43,40)],'c9')
f2.poly([(47,40),(49,40),(52,43),(51,46),(48,44),(46,42)],'c20')
f2.line(48,41,51,44,'c16')
f2.poly([(51,42),(54,43),(56,46),(54,48),(51,46),(50,44)],'c15')
f2.line(51,42,54,44,'c17')
f2.line(51,43,53,45,'c30')
f2.line(53,47,55,47,'c14')
# Plate facets and trim use the same silver/gold treatment as the idle pose.
f2.poly([(42,36),(45,36),(47,38),(46,39),(43,39),(42,38)],'c15')
f2.line(43,36,45,37,'c30')
f2.line(42,37,44,38,'c17')
f2.set(45,38,'c4')
f2.line(43,40,46,41,'c24')
f2.set(42,39,'c19')
f2.set(47,38,'c21')
f2.set(47,39,'c9')
f2.line(46,42,48,43,'c7')
f2.set(49,43,'c13')
f2.line(51,45,52,46,'c4')
f2.set(52,47,'c20')
# Turn the original weapon and its gauntleted grip through a half turn.
for y in range(23):
    for x in range(43):
        if not is_weapon(x,y): continue
        p=input_canvas.get(x,y)
        if p not in (0,41): f2.set(89-x,65-y,p)
# A short pair of white speed accents at the trailing edge.
f2.line(78,57,75,60,'c30')
f2.set(73,62,'c30')
# Verify frame one preserves every source pixel, including its transparent shadow.
for y in range(61):
    for x in range(43):
        assert f1.get(x+12,y+8)==input_canvas.get(x,y)
assert f1.stats()['size']==f2.stats()['size']
save('paladin_attack_01',f1)
save('paladin_attack_02',f2)
view(f1,scale=6,margin=0)
view(f2,scale=6,margin=0)
finish([f1,f2])
