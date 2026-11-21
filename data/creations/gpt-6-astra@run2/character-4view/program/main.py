# Four-view cheerleader sprite sheet, drawn at native resolution.
result = new_canvas(64,64,name='cheerleader_four_views')
O='#292435'
HA='#77452f'; HM='#ad683b'; HL='#db9850'; HX='#f1bd69'
SK='#efb58b'; SH='#c98267'; SL='#ffdab0'
R='#c83750'; RH='#f16268'; RD='#8c2944'
N='#343f60'; NH='#59617c'; W='#fff1d2'; WS='#c8c2bc'
G='#efb94f'; GH='#ffe18a'

def poly(c,p,col): c.poly(p,col)
def pom(c,x,y):
    # Spiky silhouette and clustered ribbons.
    poly(c,[(x-4,y-1),(x-3,y-3),(x-1,y-3),(x,y-4),(x+1,y-3),(x+3,y-3),(x+3,y-1),(x+4,y),(x+3,y+2),(x+1,y+3),(x-1,y+3),(x-3,y+2),(x-4,y+1)],O)
    poly(c,[(x-3,y-1),(x-2,y-2),(x,y-2),(x,y-3),(x+1,y-2),(x+2,y-2),(x+2,y),(x+3,y),(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1),(x-3,y+1)],G)
    c.line(x-2,y-1,x-1,y,RH); c.line(x,y-2,x,y,GH)
    c.line(x+2,y-1,x+1,y,R); c.set(x-2,y+1,GH)
    c.line(x,y+1,x+1,y+2,R); c.set(x+2,y+1,GH)

def bow(c,x,y):
    poly(c,[(x-3,y-1),(x-1,y-1),(x,y),(x+2,y-1),(x+3,y),(x+2,y+2),(x,y+1),(x-2,y+2),(x-3,y+1)],O)
    c.line(x-2,y,x-1,y+1,RH); c.line(x+1,y,x+2,y,R)
    c.set(x,y+1,RD)

def legs(c,back=False):
    c.rect(11,22,4,7,O); c.rect(17,22,4,7,O)
    c.rect(12,23,2,4,SK); c.set(13,23,SH)
    c.rect(18,23,2,4,SK); c.set(19,23,SH)
    c.rect(12,26,2,2,W); c.rect(18,26,2,2,W)
    poly(c,[(11,27),(14,27),(14,29),(10,29),(10,28)],O)
    poly(c,[(17,27),(20,27),(21,28),(21,29),(17,29)],O)
    c.rect(11,28,3,1,W); c.rect(18,28,3,1,W)
    if back:
        c.set(12,28,R); c.set(19,28,R)

def body(c,back=False):
    # Bent arms hold a pair of gold pom-poms at hip level.
    poly(c,[(10,12),(8,13),(6,17),(7,20),(10,18),(12,15),(19,15),(22,19),(24,19),(25,17),(22,13),(20,12)],O)
    c.line(9,14,7,17,SK); c.line(7,17,8,18,SH)
    c.line(21,14,23,17,SK); c.set(23,18,SH)
    poly(c,[(11,11),(20,11),(21,15),(20,18),(22,22),(9,22),(11,18),(10,15)],O)
    poly(c,[(12,12),(19,12),(20,15),(19,18),(12,18),(11,15)],R)
    c.line(12,12,15,15,W); c.line(15,15,19,12,W)
    if not back:
        c.set(15,14,R); c.set(16,16,G)
    else:
        c.line(13,13,18,13,RH)
    c.rect(11,17,10,2,N); c.line(12,17,19,17,W)
    poly(c,[(12,19),(19,19),(21,22),(10,22)],R)
    c.line(12,19,11,21,RH); c.line(15,19,15,21,W); c.line(18,19,19,21,RD)
    c.line(10,22,21,22,O)
    pom(c,5,19); pom(c,26,19)

front=new_canvas(32,31,name='front')
legs(front); body(front)
# Ponytail on the character's left, consistent in the rear view.
poly(front,[(20,3),(23,3),(25,5),(24,8),(25,11),(23,13),(20,11),(21,7)],O)
poly(front,[(22,4),(23,5),(23,8),(24,10),(22,11),(21,10)],HM)
front.line(23,6,22,9,HL)
# Neck and face.
front.rect(14,9,4,4,O); front.rect(15,10,2,3,SK)
poly(front,[(11,2),(18,2),(21,4),(21,8),(19,11),(13,11),(10,8),(10,4)],O)
poly(front,[(12,4),(19,4),(20,6),(19,9),(18,10),(14,10),(12,8)],SK)
front.line(13,6,13,8,SL); front.set(19,8,SH)
# Hair cap with swept fringe.
poly(front,[(11,3),(13,1),(18,1),(20,3),(20,6),(17,5),(15,3),(13,6),(11,6)],HA)
front.line(12,3,14,2,HL); front.line(14,2,18,2,HM)
front.line(17,3,19,4,HL); front.set(12,4,HM)
front.set(14,7,O); front.set(18,7,O)
front.set(13,8,SH); front.set(19,8,SH); front.line(15,9,16,9,RD)
bow(front,22,3)
result.blit(front,0,0)

back=new_canvas(32,31,name='back')
legs(back,True); body(back,True)
back.rect(14,9,4,4,O); back.rect(15,10,2,3,SH)
poly(back,[(12,1),(19,1),(21,3),(22,7),(20,11),(12,11),(10,8),(10,4)],O)
poly(back,[(13,2),(18,2),(20,4),(20,8),(19,10),(13,10),(11,7),(12,4)],HA)
back.line(13,3,18,3,HM); back.line(12,4,12,7,HL)
back.line(14,4,14,9,HM); back.line(18,4,19,8,HM)
# Tail sits on the opposite side in the rear view.
poly(back,[(10,3),(8,4),(7,7),(8,9),(7,12),(9,14),(12,12),(12,7)],O)
poly(back,[(9,5),(10,5),(11,8),(10,11),(9,12),(9,9),(8,7)],HM)
back.line(9,6,10,8,HL); back.set(9,11,HL)
bow(back,10,3)
result.blit(back,32,0)

# Left profile; the right profile is an exact horizontal counterpart.
side=new_canvas(32,31,name='left_profile')
# Rear arm and distant pom.
poly(side,[(18,12),(20,13),(23,17),(22,19),(20,18),(17,15)],O)
side.line(20,14,22,17,SH)
pom(side,23,19)
# Offset legs retain a clear profile silhouette.
poly(side,[(13,21),(20,21),(19,27),(20,28),(20,29),(15,29),(15,27),(16,23),(15,26),(14,28),(11,28),(11,26)],O)
side.rect(17,23,2,4,SH); side.rect(17,26,2,2,WS)
side.rect(16,28,3,1,W)
side.line(13,23,12,26,SK); side.set(13,24,SL)
side.line(12,26,13,26,W)
side.rect(10,27,4,3,O); side.rect(10,28,3,1,W)
# Top and pleated skirt.
poly(side,[(14,11),(18,11),(20,15),(19,18),(21,22),(11,22),(13,18),(12,14)],O)
poly(side,[(14,12),(17,12),(19,15),(18,18),(14,18),(13,14)],R)
side.line(13,13,14,15,W); side.line(17,12,18,13,RH)
side.line(13,17,19,17,W); side.line(13,18,19,18,N)
poly(side,[(14,19),(18,19),(20,22),(12,22)],R)
side.line(14,19,13,21,W); side.line(18,19,19,21,RD)
side.line(11,22,21,22,O)
# Ponytail behind the head.
poly(side,[(20,3),(23,4),(24,7),(23,9),(24,12),(22,14),(19,12),(20,9),(19,5)],O)
poly(side,[(21,5),(22,5),(23,7),(22,9),(23,11),(22,12),(21,11)],HM)
side.line(21,6,22,8,HL); side.set(22,11,HL)
side.rect(14,9,4,4,O); side.rect(15,10,2,3,SK)
# Projecting nose and single eye establish the direction.
poly(side,[(13,2),(19,2),(21,4),(21,8),(18,11),(13,11),(12,9),(10,8),(12,6),(12,4)],O)
poly(side,[(13,4),(18,4),(19,6),(18,9),(16,10),(13,9),(13,8),(11,8),(13,6)],SK)
side.line(13,5,13,6,SL); side.set(13,7,O); side.set(13,9,RD)
poly(side,[(13,2),(15,1),(19,2),(21,4),(20,8),(18,9),(17,7),(17,4),(14,5),(12,5)],HA)
side.line(14,3,17,2,HL); side.line(18,3,19,4,HM)
side.line(19,5,19,7,HL)
bow(side,21,3)
# Near arm extends toward the front pom.
poly(side,[(14,13),(16,14),(15,17),(11,19),(9,18),(11,16),(12,14)],O)
side.line(13,14,14,15,SK); side.line(14,16,11,18,SK)
pom(side,8,19)
result.blit(side,0,33)
right=side.copy(name='right_profile').mirror('h')
result.blit(right,32,33)
view(result,scale=8,margin=0)
save('cheerleader_four_views',result)
finish(result)
