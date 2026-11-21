# Original sprite is retained pixel-for-pixel in frame one.
f1 = new_canvas(112,74,name='01_ready')
f1.blit(input_canvas,10,5)
f2 = new_canvas(112,74,name='02_release')
P = {p['index']:p['rgba'] for p in input_canvas.palette()}
fire = {'#f27219','#f4a30c','#fed32c'}
fireids = {i for i,v in P.items() if tuple(v[:3]) in [(242,114,25),(244,163,12),(254,211,44)]}
def put(x,y,col):
    f2.set(x+10,y+5,col)
def original(x,y):
    if not (0<=x<47 and 0<=y<63): return None
    col=input_canvas.get(x,y)
    return col if P[col][3] and col not in fireids else None
# Lean the hood and shoulders into the cast, keeping the original texture.
for y in range(34):
    dx=round((34-y)*0.29)
    for x in range(47):
        if 20<=y<=25 and x>=29: continue
        col=original(x,y)
        if col is not None: put(x+dx,y+1,col)
# Stretch the coat along the stepping thigh; row sampling keeps solid clusters.
for y in range(34,55):
    advance=(y-34)*0.65
    for xx in range(47):
        if xx<=10: sx=xx
        elif xx<=16+advance: sx=10+(xx-10)*6/(6+advance)
        else: sx=xx-advance
        col=original(round(sx),y)
        if col is not None: put(xx,y,col)
# Back boot anchors the stance. The near (left) foot steps into the spell.
for y in range(54,63):
    for x in range(17):
        col=original(x,y)
        if col is not None: put(x,y,col)
for y in range(54,61):
    for x in range(17,32):
        col=original(x,y)
        if col is not None: put(x+13,y+2,col)
# Connect the forward ankle to the coat hem.
def poly(points,c): f2.poly([(x+10,y+5) for x,y in points],c)
def line(x,y,X,Y,c): f2.line(x+10,y+5,X+10,Y+5,c)
black='#010202'; dark='#0b0b13'; maroon='#4a222d'; red='#7d423a'; gray='#455363'; fold='#211d2c'
poly([(30,52),(36,52),(38,56),(34,58),(31,56)],dark)
line(32,53,34,56,maroon)
# Long sleeve and clenched casting hand.
poly([(30,20),(35,20),(38,21),(51,21),(54,22),(55,25),(51,27),(37,26),(30,25)],black)
poly([(32,21),(36,22),(49,22),(51,23),(50,25),(37,24),(32,24)],maroon)
line(36,22,49,22,red)
line(37,25,49,25,'#240b0c')
line(32,21,33,24,gray)
poly([(50,22),(53,21),(55,22),(56,24),(54,25),(50,25)],'#240b0c')
line(51,22,54,22,'#dfb2ac')
line(51,23,55,23,'#7d423a')
line(52,24,54,24,'#4a222d')
# Jagged flame stream, wind-torn wake and forward-moving fireball.
ember='#b83d1c'; orange='#f27219'; gold='#f4a30c'; yellow='#fed32c'; hot='#fff0a0'
poly([(54,23),(59,21),(64,21),(61,18),(68,20),(72,19),(68,15),(74,17),(77,14),(82,14),(81,12),(86,15),(87,17),(90,18),(88,19),(92,22),(89,25),(85,28),(79,28),(75,26),(70,27),(66,25),(61,25),(58,24)],ember)
poly([(55,23),(62,22),(68,23),(72,21),(69,19),(76,20),(75,17),(80,18),(79,15),(84,16),(85,18),(88,18),(87,21),(90,22),(87,25),(83,26),(78,26),(74,24),(70,25),(65,24),(59,24)],orange)
poly([(58,23),(65,23),(71,22),(75,23),(79,21),(77,19),(81,20),(82,17),(84,20),(87,21),(88,23),(84,25),(80,24),(77,25),(72,23),(66,24)],gold)
poly([(70,23),(76,22),(80,23),(82,21),(82,19),(85,22),(86,23),(83,24),(78,23),(74,24)],yellow)
line(81,22,84,22,hot)
put(83,23,hot)
# Detached sparks emphasize the direction and add air around the trail.
line(62,17,65,18,orange)
put(59,16,ember)
line(72,12,74,13,orange)
put(78,10,gold)
line(67,28,70,29,orange)
put(73,30,gold)
put(87,13,orange)
put(91,27,gold)
view(f1,scale=5)
view(f2,scale=5)
finish([f1,f2])
