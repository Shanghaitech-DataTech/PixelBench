# Keep the untouched source on a shared, roomier transparent canvas.
W, H = 104, 72
OX, OY = 7, 4
f1 = new_canvas(W, H, name='01_ready')
f1.blit(input_canvas, OX, OY)
f2 = new_canvas(W, H, name='02_release')

# Original palette: shadow, cloth, leather, metal, skin and the three fire tones.
P = {p['index']: tuple(p['rgba']) for p in input_canvas.palette()}
ink=P[6]; dark=P[3]; navy=P[9]; clothdark=P[7]; grey=P[4]
steel=P[8]; edge=P[1]; brown=P[5]; leather=P[10]; deep=P[2]; skin=P[12]
orange=P[13]; gold=P[14]; yellow=P[15]

def poly(points,col):
    f2.poly([(x+OX,y+OY) for x,y in points],col)
def line(x0,y0,x1,y1,col):
    f2.line(x0+OX,y0+OY,x1+OX,y1+OY,col)
def rect(x,y,w,h,col):
    f2.rect(x+OX,y+OY,w,h,col)
def dot(x,y,col):
    f2.set(x+OX,y+OY,col)

# Rear boot stays planted as the weight moves onto the forward left leg.
input_canvas.select(0,54,14,9).copy_to(OX,OY+54,f2,mode='over')

# The left leg takes a long step. Its boot is planted on the same ground line.
poly([(28,48),(34,48),(37,52),(37,56),(40,59),(45,60),(48,62),(48,63),(35,63),(32,60),(31,56),(29,53)],ink)
poly([(30,49),(34,50),(36,53),(35,56),(38,59),(43,61),(46,61),(46,62),(35,62),(33,59),(32,54)],leather)
poly([(30,50),(32,50),(34,54),(34,58),(36,61),(35,62),(33,59),(31,55)],deep)
poly([(34,53),(36,54),(36,57),(39,60),(43,61),(40,61),(36,59)],brown)
line(36,62,46,62,navy)
dot(44,60,grey)
dot(47,62,clothdark)

# The split coat spreads over the new stance; original cloth colours and folds survive.
for y in range(34,55):
    amount=(y-34)/20
    for x in range(0,32):
        idx=input_canvas.get(x,y)
        if idx == 0: continue
        nx=x+3+round((x-13)*amount*0.52)
        ny=y+round(2*(1-amount))
        f2.set(OX+nx,OY+ny,idx)
        # Keep the widened fabric in continuous pixel clusters.
        if x<31 and input_canvas.get(x+1,y)!=0:
            nx2=x+1+3+round((x+1-13)*amount*0.52)
            for xx in range(nx+1,nx2):
                f2.set(OX+xx,OY+ny,idx)

# A forward shear pivots the hood, cape and torso around the hips.
for y in range(34):
    dx=3+round((33-y)*0.30)
    for x in range(32):
        idx=input_canvas.get(x,y)
        if idx==0 or idx>=13: continue
        # The old casting arm is replaced by an extended, open-handed thrust.
        if 20<=y<=25 and x>=28: continue
        f2.set(OX+x+dx,OY+y+2,idx)

# Shoulder, sleeve and extended forearm.
poly([(32,21),(36,21),(39,23),(44,23),(48,22),(52,22),(54,23),(55,25),(54,28),(50,29),(46,28),(41,29),(37,28),(34,27),(32,25)],ink)
poly([(33,22),(36,22),(39,24),(43,24),(43,27),(39,28),(35,26),(33,25)],clothdark)
poly([(33,22),(36,22),(39,24),(38,25),(34,24)],steel)
line(34,22,36,22,grey)
poly([(39,24),(43,24),(47,23),(50,23),(51,26),(49,28),(45,27),(41,28),(39,27)],leather)
line(42,24,47,24,brown)
line(42,28,47,27,deep)
# Glove cuff and reaching fingers silhouette.
poly([(48,23),(50,22),(52,23),(53,25),(52,28),(49,28)],grey)
line(49,23,50,25,edge)
poly([(51,23),(55,22),(57,22),(57,23),(54,24),(58,24),(58,25),(55,26),(56,27),(55,28),(52,27),(51,26)],deep)
line(52,24,55,23,brown)
line(53,25,57,25,leather)
dot(55,26,brown)
dot(56,22,leather)

# The launched spell has a broad leading head and narrow, broken streamers.
ember='#b74625'
bright='#fff0a0'
poly([(57,25),(61,25),(64,23),(68,24),(71,22),(75,22),(75,19),(79,20),(81,18),(83,21),(86,21),(86,23),(89,25),(88,28),(90,29),(87,32),(85,33),(81,35),(77,34),(75,32),(70,32),(68,30),(65,30),(62,28),(59,28)],ember)
poly([(58,25),(63,26),(67,24),(72,25),(76,23),(76,21),(80,22),(82,20),(84,23),(87,24),(86,26),(89,28),(86,30),(85,32),(81,34),(78,32),(75,31),(71,30),(68,28),(65,29),(62,27)],orange)
# Backward whipping tongues above and below the main wake.
poly([(63,21),(67,22),(71,21),(75,22),(78,24),(74,25),(70,23),(67,23)],orange)
poly([(65,32),(68,32),(71,34),(75,33),(79,34),(82,33),(79,36),(75,35),(71,35),(69,33)],orange)
poly([(61,26),(65,26),(69,25),(72,26),(77,25),(79,23),(81,24),(82,22),(84,25),(86,26),(85,28),(87,29),(83,31),(80,32),(77,30),(74,29),(70,29),(67,27),(64,28)],gold)
poly([(67,26),(71,27),(74,26),(78,27),(80,25),(82,25),(82,24),(84,26),(84,28),(85,29),(81,30),(79,29),(76,29),(73,28),(70,28)],yellow)
poly([(76,27),(80,26),(82,26),(83,27),(82,29),(80,29),(79,28)],bright)
# Detached sparks follow the direction of travel.
rect(58,22,2,1,orange)
dot(61,20,gold)
rect(69,18,2,1,orange)
dot(72,19,yellow)
rect(65,35,2,1,ember)
dot(68,36,orange)
rect(83,16,2,1,orange)
dot(87,19,gold)
rect(85,36,2,1,orange)

# Verify that frame 1 retains every original pixel, including its transparency.
assert f1.select(OX, OY, 47, 63).preview().to_rgba()[2] == input_canvas.to_rgba()[2]
save('release-flames-01', f1)
save('release-flames-02', f2)
view(f1,scale=6,margin=0)
view(f2,scale=6,margin=0)
finish([f1,f2])
