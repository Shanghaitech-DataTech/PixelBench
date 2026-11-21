result = new_canvas(64,64,name='cheerleader_four_views')
O='#292438'; HA='#653b35'; HS='#422b32'; HL='#aa6045'; HH='#d88a59'
SK='#f4b184'; SL='#d9826d'; SH='#ffdab0'; R='#e84960'; RS='#a92c50'; RH='#ff7a79'; W='#fff2dd'; WS='#b8c6d1'; B='#477985'; BS='#30515f'; G='#ffc85b'; GS='#df883f'; GH='#fff0a0'

def shape(c,pts,col):
    c.poly(pts,col)
    c.poly(pts,O,fill=False)
def pom(c,x,y):
    pts=[(x+2,y),(x+5,y),(x+5,y+1),(x+7,y+1),(x+7,y+3),(x+8,y+3),(x+8,y+6),(x+6,y+6),(x+6,y+8),(x+2,y+8),(x+2,y+7),(x,y+7),(x,y+2),(x+2,y+2)]
    shape(c,pts,GS)
    c.rect(x+2,y+2,4,4,G)
    c.line(x+1,y+3,x+3,y+4,GH); c.line(x+4,y+1,x+4,y+3,GH)
    c.line(x+6,y+3,x+5,y+5,GH);c.line(x+2,y+5,x+1,y+6,G)
    c.line(x+4,y+5,x+4,y+7,G);c.set(x+6,y+6,G)
def bow(c,x,y):
    shape(c,[(x,y),(x+3,y+1),(x+6,y),(x+6,y+4),(x+3,y+3),(x,y+4)],R)
    c.set(x+1,y+1,RH);c.set(x+5,y+1,RH);c.set(x+3,y+2,W)

def full(back=False):
    c=new_canvas(32,32)
    # ponytail tucked behind the right shoulder
    shape(c,[(20,5),(23,6),(24,10),(23,13),(24,15),(20,14),(19,10)],HA)
    c.line(22,8,22,12,HL)
    # legs and white trainers
    for x in [12,18]:
        c.rect(x,23,4,7,O);c.rect(x+1,24,2,4,SK);c.set(x+2,24,SL)
        c.rect(x+1,27,2,2,W)
        c.rect(x-1,29,5,2,O);c.rect(x,29,3,1,W)
    # arms, angling outward to pom-poms
    shape(c,[(11,14),(13,16),(10,21),(7,21),(7,18)],SK)
    shape(c,[(20,14),(23,17),(25,19),(23,22),(20,19),(18,16)],SK)
    c.set(10,17,SH);c.set(22,18,SH)
    # sleeveless top
    shape(c,[(12,13),(19,13),(21,16),(20,20),(12,20),(10,16)],R)
    c.line(12,14,15,17,W);c.line(15,17,19,14,W)
    c.line(12,18,12,19,RH);c.line(19,17,19,19,RS)
    if not back:
        c.set(15,18,W);c.set(16,18,W);c.set(15,19,W)
    else:
        c.line(14,18,17,18,RS)
    c.rect(12,20,9,1,W)
    # flared pleated skirt
    shape(c,[(12,21),(20,21),(23,25),(9,25)],R)
    c.line(12,22,11,24,RH);c.line(15,22,14,24,RS);c.line(19,22,20,24,RS)
    c.line(10,24,22,24,W)
    # neck
    c.rect(14,12,4,3,O);c.rect(15,12,2,3,SL)
    # head
    shape(c,[(12,4),(19,4),(21,6),(21,11),(19,14),(13,14),(10,11),(10,7)],HA if back else SK)
    if not back:
        c.line(12,8,12,11,SH);c.set(20,10,SL);c.set(18,12,SL)
        # hair cap with swept fringe
        c.poly([(11,5),(13,3),(18,3),(21,5),(21,9),(19,8),(18,6),(15,8),(12,8),(11,10)],HA)
        c.line(13,4,18,4,HL);c.line(12,5,15,5,HL);c.set(12,6,HH)
        c.rect(13,9,2,2,O);c.rect(18,9,2,2,O)
        c.set(13,9,W);c.set(18,9,W)
        c.set(12,11,RH);c.set(20,11,RH);c.line(15,12,16,12,HS)
    else:
        c.poly([(12,4),(19,4),(20,6),(20,11),(18,13),(13,13),(11,10),(11,7)],HA)
        c.line(12,6,12,10,HL);c.line(13,5,18,5,HL);c.line(14,5,14,8,HL)
        c.line(18,8,18,12,HS);c.line(13,12,17,12,HS)
    bow(c,17,2)
    pom(c,3,17);pom(c,23,17)
    return c

def side():
    c=new_canvas(32,32)
    # ponytail falling behind the head
    shape(c,[(19,5),(23,5),(25,8),(24,13),(25,16),(22,16),(20,12)],HA)
    c.line(23,7,23,12,HL);c.set(24,14,HL)
    # far leg and shoe
    c.rect(17,24,4,6,O);c.rect(18,25,2,4,SL)
    c.rect(16,29,5,2,O);c.rect(17,29,3,1,WS)
    # near leg
    c.rect(13,24,4,6,O);c.rect(14,25,2,3,SK);c.rect(14,28,2,1,W)
    c.rect(11,29,6,2,O);c.rect(12,29,4,1,W)
    shape(c,[(14,14),(18,13),(20,16),(19,21),(13,21),(12,17)],R)
    c.line(13,15,14,17,W);c.line(18,15,18,19,RS)
    c.line(13,20,19,20,W)
    shape(c,[(13,21),(19,21),(22,25),(11,25)],R)
    c.line(14,22,13,24,RH);c.line(18,22,19,24,RS);c.line(12,24,21,24,W)
    c.rect(14,12,4,3,O);c.rect(15,12,2,3,SL)
    # face projects left at the nose
    shape(c,[(12,4),(18,4),(21,7),(20,11),(17,14),(12,13),(12,11),(10,10),(11,8),(11,6)],SK)
    c.set(12,10,SH);c.set(13,12,SL)
    # hair cap and back edge
    c.poly([(12,4),(15,3),(19,4),(21,6),(21,11),(18,13),(17,10),(18,8),(15,7),(12,7)],HA)
    c.line(14,4,18,5,HL);c.line(18,5,19,7,HL);c.set(13,5,HH)
    c.rect(12,8,2,2,O);c.set(12,8,W);c.set(12,11,RH)
    c.set(17,10,SL);c.set(17,9,SH)
    bow(c,19,2)
    # visible arm reaches forward
    shape(c,[(16,15),(18,16),(17,20),(13,22),(10,21),(10,19),(14,18)],SK)
    c.line(16,16,16,18,SH);c.line(12,20,14,20,SL)
    pom(c,5,18)
    return c
front=full();back=full(True);left=side();right=left.copy();right.mirror('h')
result.blit(front,0,0);result.blit(back,32,0);result.blit(left,0,32);result.blit(right,32,32)
view(result,scale=8,margin=0)
finish(result)
