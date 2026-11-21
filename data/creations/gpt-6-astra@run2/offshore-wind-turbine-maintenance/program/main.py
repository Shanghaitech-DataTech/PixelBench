result = new_canvas(64,64,background='#a9d5df',name='offshore_maintenance')
c=result
# Air: spare, stepped cloud banks.
c.rect(0,27,64,10,'#bedfe4')
c.poly([(0,10),(7,10),(7,8),(16,8),(16,9),(22,9),(22,12),(29,12),(29,14),(0,14)],'#d9ebea')
c.rect(1,14,20,1,'#c9e4e6')
c.poly([(50,20),(54,20),(54,18),(61,18),(61,19),(63,19),(63,23),(50,23)],'#d9ebea')
# Distant ocean and the two complete wind turbines.
c.rect(0,36,64,28,'#488c9e')
c.line(0,36,63,36,'#739faa')
def distant_turbine(x,y,r):
    c.line(x,y+1,x,36,'#7195a1')
    c.line(x-1,y+2,x-1,35,'#e3eeee')
    c.line(x,y,x-2,y-r,'#f1f3e9')
    c.line(x,y,x-r,y+int(r*.55),'#edf2e9')
    c.line(x,y,x+r,y+int(r*.4),'#edf2e9')
    c.rect(x-1,y-1,3,2,'#f1f3e9')
    c.set(x,y,'#7e9eaa')
distant_turbine(12,22,10)
distant_turbine(25,28,6)
# Sea bands and individual broken wave crests.
c.rect(0,43,64,21,'#28748b')
c.poly([(0,52),(9,52),(9,50),(20,50),(20,52),(32,52),(32,55),(51,55),(51,53),(63,53),(63,64),(0,64)],'#20586e')
for x,y,w in [(1,39,6),(17,39,5),(26,37,7),(53,38,6),(8,42,7),(0,46,9),(19,45,5),(51,45,10),(4,49,7),(14,48,5),(54,50,7),(0,56,6),(10,54,8),(22,59,6),(51,58,10),(3,61,11)]:
    c.rect(x,y,w,1,'#579eaa')
for x,y,w in [(3,45,5),(15,48,3),(55,49,5),(8,54,7),(0,55,3),(54,57,5),(22,58,4),(5,60,5)]:
    c.rect(x,y,w,1,'#a3d2d2')
# Main tower continues above the frame, establishing the immense turbine scale.
c.poly([(39,0),(47,0),(49,36),(37,36)],'#607f8c')
c.poly([(40,0),(46,0),(47,35),(38,35)],'#d8e5df')
c.poly([(40,0),(42,0),(41,34),(38,34)],'#f3f1de')
c.poly([(46,0),(47,0),(49,35),(46,35)],'#a1b9bc')
c.line(39,20,47,20,'#b5c9c8')
c.set(40,21,'#f3f1de')
# Massive steel transition pile and its shaded foot.
c.rect(39,40,10,23,'#183e52')
c.rect(40,42,7,21,'#446573')
c.rect(40,42,2,20,'#69828a')
c.rect(40,45,7,2,'#264b60')
c.rect(40,58,7,3,'#2a4e5e')
# Diagonal platform supports.
for a,b,d,e in [(29,43,39,51),(54,43,48,51)]:
    c.line(a,b,d,e,'#183e52')
    c.line(a,b-1,d,e-1,'#718b91')
# Rear guardrail, golden safety paint.
c.line(29,33,55,33,'#765437')
c.line(29,32,55,32,'#f4c75d')
for x in [29,35,51,55]:
    c.line(x,33,x,39,'#c58d38')
c.line(29,36,55,36,'#e1ad48')
# Tower's yellow transition section and service hatch.
c.rect(37,34,13,7,'#c38c38')
c.rect(38,34,9,7,'#e7b64e')
c.rect(39,34,2,7,'#ffda72')
c.rect(42,33,4,7,'#57727a')
c.rect(43,34,2,5,'#264859')
c.set(44,36,'#eee3a5')
# Platform deck, front edge, and front rail.
c.poly([(29,38),(53,38),(57,40),(54,43),(27,43),(26,41)],'#263e50')
c.poly([(29,38),(53,38),(55,40),(28,40)],'#8c9e9a')
c.line(27,41,55,41,'#efbd51')
c.line(28,43,54,43,'#142f43')
for x in [27,35,45,55]:
    c.line(x,35,x,40,'#e5af47')
    c.set(x,34,'#ffe08b')
c.line(27,34,55,34,'#f7cb66')
c.line(27,37,55,37,'#d89a3b')
# Ladder mounted away from the pile: visible rungs, standoffs and curved handholds.
c.line(29,43,29,62,'#152f43')
c.line(34,43,34,62,'#152f43')
c.line(30,42,30,61,'#b8c7bf')
c.line(33,42,33,61,'#839d9f')
for y in range(44,63,3):
    c.line(30,y,33,y,'#d0d3bb')
for y in [46,57]:
    c.line(34,y,39,y,'#182f42')
c.line(30,38,30,42,'#f4c75d')
c.line(33,38,33,42,'#f4c75d')
c.line(30,38,31,37,'#f4c75d')
# Technician climbing: helmet, orange flotation suit, harness and staggered boots.
c.line(34,42,36,49,'#d9c482')
c.rect(31,48,3,5,'#172d40')
c.set(30,54,'#102c3b')
c.line(31,52,30,53,'#e78c3c')
c.line(33,52,33,55,'#bc5b33')
c.line(33,55,34,55,'#152d3e')
c.rect(31,48,3,4,'#f28f3b')
c.line(31,48,29,47,'#f1a54d')
c.set(29,46,'#d9c1a0')
c.line(34,49,35,47,'#e77736')
c.set(35,46,'#e3c7a3')
c.rect(31,46,3,2,'#af7956')
c.set(31,46,'#edc29a')
c.rect(31,44,3,2,'#ffda57')
c.line(30,46,34,46,'#ffe68c')
c.set(31,44,'#fff0a0')
c.line(32,48,32,51,'#fff0a0')
c.line(31,51,34,51,'#443c3a')
c.set(33,50,'#eff0bb')
# Foam wraps around the pile; near water remains visibly separate from steel.
c.line(37,62,49,62,'#80bdc2')
c.line(40,63,47,63,'#bedcda')
c.line(49,61,52,61,'#80bdc2')
c.line(17,63,22,63,'#41889a')
view(result,scale=8,margin=0)
finish(result)
