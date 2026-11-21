# Two transparent animation frames; the first contains an exact copy of the input.
W,H = 120,104
OX,OY = 18,26
f1 = new_canvas(W,H,name='01_original')
f1.blit(input_canvas, OX, OY)

# Source-palette constants.
ink = '#020202'
edge = '#120d1c'
hair = '#69657d'
cloth = '#454463'
shade = '#231c2c'
crease = '#3d2c32'
pants = '#926e6b'
steelshade = '#8a8385'
red = '#71444c'
redblack = '#1b0202'
skin = '#f3a473'
shine = '#eedddd'
steelmid = '#9b938d'
steel = '#b2aeb1'

# Sweep builds from a fine lower-left tail to the raised upper-right blade.
trail = new_canvas(W,H,name='black_slash_trail')
trail.path('M 9 86 Q 40 86 73 63 Q 98 44 110 9 Q 113 42 92 64 Q 62 88 9 86 Z', ink)
trail.path('M 16 91 Q 40 92 60 84 Q 42 94 16 91 Z', ink)
trail.path('M 97 61 Q 111 43 114 27', ink, fill=False)
trail.line(7,87,12,87, ink)

# Retain the face, hair, legs, right arm and scabbard from the supplied sprite.
body = input_canvas.copy(name='pose_edit')
# Remove only the original left sleeve, sword hand, guard and hilt.
body.poly([(50,27),(61,27),(61,43),(48,43),(48,37),(50,34)], None)
body.rect(41,39,21,5,None)
# Restore the tunic edge and waist behind the old sword guard.
body.poly([(47,27),(51,28),(51,34),(49,38),(49,43),(46,44),(40,42),(40,39),(44,39)],cloth)
body.poly([(48,31),(51,32),(49,38),(49,43),(46,44),(46,40)],shade)
body.poly([(41,42),(45,43),(48,43),(48,46),(41,46)],crease)
body.line(44,43,47,44,red)
# Small dark scabbard mouth beside the right hand, with no sword in that hand.
body.poly([(39,41),(42,40),(45,42),(43,44),(40,44)],edge)
body.line(40,41,42,41,steelshade)
body.line(42,42,44,42,steelmid)
body.set(42,43,ink)

f2 = new_canvas(W,H,name='02_completed_slash')
f2.blit(trail,0,0)
f2.blit(body,OX,OY)

# Raised LEFT arm. Coordinates below are relative to the original sprite.
def poly(points,col):
    f2.poly([(x+OX,y+OY) for x,y in points],col)
def line(x0,y0,x1,y1,col):
    f2.line(x0+OX,y0+OY,x1+OX,y1+OY,col)
def rect(x,y,w,h,col):
    f2.rect(x+OX,y+OY,w,h,col)

# A single continuous sleeve from left shoulder to the raised wrist.
poly([(49,27),(52,25),(57,25),(61,22),(65,17),(68,14),(73,17),(73,21),(68,28),(62,33),(57,34),(52,32)],edge)
poly([(51,27),(56,27),(61,25),(66,18),(68,16),(71,18),(70,22),(65,28),(60,31),(56,31)],cloth)
poly([(53,26),(57,26),(61,23),(65,18),(67,17),(67,20),(62,26),(58,28)],hair)
poly([(57,31),(62,28),(67,24),(70,20),(71,21),(68,27),(62,32)],shade)
line(57,28,58,30,edge)
line(64,24,66,24,edge)
poly([(66,17),(68,14),(73,17),(72,20),(69,19)],shade)
line(67,16,71,18,steelshade)

# Drawn katana: bright blade rises from the raised left fist to the upper right.
# Blade outline and two crisp steel planes.
poly([(75,12),(77,9),(91,-15),(92,-17),(92,-12),(81,12),(78,15)],edge)
poly([(77,11),(79,8),(91,-14),(90,-9),(80,12),(78,13)],steel)
poly([(77,11),(79,8),(91,-14),(89,-8),(78,12)],shine)
line(79,12,89,-8,steelshade)
# Hilt extends down-left from the guard, and is gripped ONLY by the left hand.
poly([(70,23),(68,21),(75,11),(78,13)],edge)
poly([(70,20),(75,13),(76,14),(71,22)],red)
line(70,19,72,20,steelshade)
line(72,16,74,17,steelshade)
# Metal guard, transverse to the blade.
poly([(73,9),(80,13),(80,15),(72,11)],edge)
line(73,10,79,13,steel)
line(74,10,76,11,shine)
# Fist overlaps and wraps the hilt, emerging directly from the sleeve cuff.
poly([(68,14),(70,12),(73,12),(76,14),(75,17),(72,20),(68,18)],redblack)
poly([(69,14),(71,13),(73,13),(75,14),(74,17),(72,19),(69,17)],skin)
line(70,13,72,13,shine)
line(72,16,74,17,red)
line(69,17,71,18,red)
f2.set(OX+74,OY+14,skin)

# Verify the unchanged original inside the expanded first frame.
for y in range(72):
    for x in range(62):
        assert f1.get(x+OX,y+OY) == input_canvas.get(x,y)

save('01_original',f1)
save('02_completed_slash',f2)
# Neutral inspection background is separate from the transparent output frames.
proof = new_canvas(W,H,'#a8b1b8',name='pose_preview')
proof.blit(f2,0,0)
view(proof,scale=5,margin=0)
finish([f1,f2])
