result = new_canvas(64,64, name='dining_table')
c=result
O='#30232b'; D='#653d32'; S='#89503a'; M='#b67245'; L='#d9985b'; H='#f2bc78'; SH='#493036'
# Four chairs, viewed from above with a slight front-facing tilt.
def chair(x,y,back=True):
    # legs beneath upholstered wooden seat
    leg_h = 8 if back else 5
    c.rect(x+2,y+14,3,leg_h,O); c.rect(x+13,y+14,3,leg_h,O)
    c.rect(x+3,y+15,1,leg_h-2,M); c.rect(x+14,y+15,1,leg_h-2,M)
    c.rect(x+1,y+7,16,11,O)
    c.rect(x+2,y+8,14,8,D)
    c.rect(x+3,y+8,12,6,M)
    c.line(x+4,y+8,x+13,y+8,H)
    c.line(x+3,y+14,x+14,y+14,S)
    if back:
        c.rect(x,y,18,10,O)
        c.rect(x+1,y+1,16,7,S)
        c.rect(x+2,y+1,14,2,L)
        c.rect(x+3,y+4,12,3,D)
        c.rect(x+4,y+4,10,1,M)
        c.rect(x+1,y+8,2,6,O);c.rect(x+15,y+8,2,6,O)
        c.set(x+2,y+2,H)
chair(9,3);chair(37,3)
# Table legs and lower apron.
c.rect(8,36,5,17,O);c.rect(10,39,2,12,S);c.set(10,51,L)
c.rect(51,36,5,17,O);c.rect(52,39,2,12,S);c.set(52,51,L)
c.rect(14,39,36,7,O);c.rect(15,40,34,4,D);c.line(16,40,48,40,M)
# Large bevelled table top
c.poly([(9,17),(54,17),(59,22),(59,39),(55,43),(8,43),(4,39),(4,22)],O)
c.poly([(9,18),(54,18),(58,22),(58,38),(54,41),(9,41),(5,38),(5,22)],S)
c.poly([(10,18),(53,18),(57,22),(57,36),(53,39),(10,39),(6,36),(6,22)],L)
c.poly([(10,19),(53,19),(56,22),(56,35),(53,38),(10,38),(7,35),(7,22)],M)
c.line(10,19,53,19,H);c.line(7,22,7,34,L)
c.line(10,38,53,38,D);c.line(54,38,57,35,D)
# Plank joints and restrained woodgrain.
for y in (24,31):
    c.line(8,y,55,y,S);c.line(9,y+1,54,y+1,L)
c.line(20,20,20,23,S);c.line(43,26,43,30,S);c.line(17,33,17,37,S)
c.line(11,21,16,21,L);c.line(45,21,51,21,L)
c.line(10,28,18,28,L);c.line(46,34,52,34,L)
c.line(22,35,26,35,S);c.line(23,36,28,36,L)
c.line(46,28,51,28,D);c.line(47,29,50,29,L)
# Woven runner beneath the bowl.
c.rect(26,19,13,18,S)
c.rect(27,19,11,18,'#bfc29a')
c.rect(29,19,7,18,'#daddad')
for x in (27,29,31,33,35,37):
    c.set(x,18,'#e9dfb4');c.set(x,37,'#e9dfb4')
c.line(27,34,37,34,'#8c9c83')
# Bowl shadow, dark outer rim and ceramic body.
c.ellipse(32,31,10,3,S)
c.ellipse(32,28,10,5,O)
c.ellipse(32,29,8,4,'#648c88')
c.line(27,32,36,32,'#a5c9b0')
c.ellipse(32,26,10,4,O)
c.ellipse(32,26,8,3,'#e8deb4')
c.ellipse(32,26,7,2,'#9c7851')
# Fruit nestled within the bowl.
c.circle(28,25,3,'#68342f');c.circle(28,24,3,'#ce5844');c.set(27,22,'#ffb46a');c.line(28,21,29,20,D)
c.circle(35,24,3,'#607642');c.circle(35,23,2,'#9db356');c.set(34,22,'#d6d87b');c.line(35,21,35,20,D)
c.circle(32,27,3,'#b46b30');c.circle(32,26,2,'#efa44e');c.set(31,25,'#ffda7c')
c.poly([(37,26),(39,24),(40,23),(40,26),(38,28),(35,29),(34,28)],'#edc365')
c.set(40,23,D);c.line(36,28,38,27,'#fff0a0')
c.line(25,29,27,30,'#fff0cf');c.line(28,31,35,31,'#c9e0c7')
# Near chairs overlap the front edge of the table; both remain distinct.
chair(9,43,False);chair(37,43,False)
for x in (9,37):
    c.rect(x,47,18,12,O)
    c.rect(x+1,48,16,9,S)
    c.rect(x+2,48,14,2,H)
    c.rect(x+2,50,14,6,M)
    c.rect(x+4,51,10,3,D)
    c.line(x+4,51,x+13,51,S)
    c.line(x+2,56,x+15,56,L)
    c.rect(x+1,57,3,5,O);c.rect(x+14,57,3,5,O)
    c.rect(x+2,58,1,3,M);c.rect(x+15,58,1,3,M)
view(result)
finish(result)
