import math, random
random.seed(17)
W=H=256
result = new_canvas(W,H,background='#090e19',name='The Astral Engine')
c=result
# A tightly controlled palette: blue-black stone, aged brass, and emissive gems.
ink='#0a101b'; deep='#151924'
bg=['#090e19','#0d1421','#111d2b','#172737','#203343','#2b4350','#38545c']
stone=['#121e2a','#1b2b38','#293e49','#3b5158','#52666a','#71817e']
gold=['#211b25','#38262a','#58372b','#79502e','#a16f39','#c5944c','#dfb768','#f5d68a','#fff0b7']
cyan=['#112c3b','#174554','#246575','#338c98','#59bbc2','#8ce5e0','#d4fff1']
violet=['#272338','#433754','#645079','#927ca9','#c4abd1','#f3e1ef']

def ln(x0,y0,x1,y1,col):
    c.line(round(x0),round(y0),round(x1),round(y1),col)
def dot(x,y,r,col):
    c.circle(round(x),round(y),r,col)
def poly(points,col):
    c.poly([(round(x),round(y)) for x,y in points],col)
def xy(cx,cy,rx,ry,rot,t):
    a=math.radians(rot); t=math.radians(t)
    return (cx+rx*math.cos(t)*math.cos(a)-ry*math.sin(t)*math.sin(a),cy+rx*math.cos(t)*math.sin(a)+ry*math.sin(t)*math.cos(a))
def polar(cx,cy,r,t): return xy(cx,cy,r,r,0,t)
def stroke_arc(cx,cy,rx,ry,rot,start,end,col,thick=1):
    pts=[xy(cx,cy,rx,ry,rot,start+(end-start)*i/max(1,int(abs(end-start)*1.5))) for i in range(max(1,int(abs(end-start)*1.5))+1)]
    for a,b in zip(pts[:-1],pts[1:]):
        if thick==1: ln(*a,*b,col)
        else: dot(*a,thick//2,col)

def ring(cx,cy,rx,ry,rot,width,start=0,end=360,dim=0):
    # Pixel-rasterized annular plate, with a dark thickness underneath.
    a=math.radians(rot); co=math.cos(a); si=math.sin(a)
    ex=int(abs(rx*co)+abs(ry*si))+3; ey=int(abs(rx*si)+abs(ry*co))+4
    def draw(shift,shadow):
        for y in range(max(0,int(cy-ey)), min(256,int(cy+ey+shift+1))):
            for x in range(max(0,int(cx-ex)), min(256,int(cx+ex+1))):
                dx=x-cx; dy=y-cy-shift
                u=dx*co+dy*si; v=-dx*si+dy*co
                q=(u/rx)**2+(v/ry)**2
                qi=(u/(rx-width))**2+(v/(ry-width))**2
                if q>1 or qi<1: continue
                t=math.degrees(math.atan2(v/ry,u/rx))%360
                if not start<=t<=end: continue
                if shadow:
                    c.set(x,y,ink if shift==3 else gold[1]); continue
                outer=(u/max(1,rx-1.0))**2+(v/max(1,ry-1.0))**2>1
                inner=(u/max(1,rx-width+1))**2+(v/max(1,ry-width+1))**2<1
                if outer or inner: col=gold[0]
                else:
                    f=(1-math.sqrt(q))/(1-math.sqrt(q/qi))
                    light=(-dx*.65-dy*.8)/max(1,math.hypot(dx,dy))
                    val=5 if light>0.38 else 4 if light>-.30 else 3
                    if f<.29: val+=2
                    elif f>.73: val-=1
                    if .43<f<.57 and width>=7: val-=1
                    val=max(1,min(8,val-dim))
                    col=gold[val]
                c.set(x,y,col)
    draw(3,True); draw(0,False)

def bolt(x,y,r=2):
    dot(x,y,r,ink);dot(x,y,max(0,r-1),gold[5]);c.set(round(x)-1,round(y)-1,gold[8]);c.set(round(x),round(y),gold[2])

# Dark, monumental chamber: recessed arches and paired stone piers.
c.rect(0,0,256,206,bg[1])
c.path('M 25 206 V 94 Q 25 3 128 0 Q 231 3 231 94 V 206 Z',bg[2])
c.path('M 40 206 V 92 Q 40 17 128 13 Q 216 17 216 92 V 206 Z',bg[0])
for off,col in [(0,bg[3]),(5,bg[2]),(11,bg[3])]:
    c.path(f'M {26+off} 204 V 94 Q {26+off} {7+off} 128 {3+off} Q {230-off} {7+off} {230-off} 94 V 204',col,False)
for x in [12,229]:
    c.rect(x,58,15,151,bg[0]);c.rect(x+3,59,10,146,bg[2]);c.rect(x+4,64,2,136,bg[3]);c.rect(x+11,64,2,136,bg[1])
    for y in [55,61,94,132,170,202]:
        c.rect(x-3,y,21,4,bg[0]);c.rect(x-2,y,19,1,bg[3]);c.rect(x,y+1,15,2,bg[2])
# Quiet block joints behind the machine.
for y,xs in [(31,[45,205]),(63,[32,222]),(103,[29,222]),(145,[29,222]),(181,[28,223])]:
    for x in xs:
        ln(x,y,x+8,y,bg[3]);ln(x+5,y,x+5,y+19,bg[1])
# A restrained ambient aureole, in discrete colours.
halo=['#111d28','#17252f','#1c2d34','#24373b','#2d403e']
for y in range(10,207):
    for x in range(29,228):
        d=math.hypot((x-128)*1.02,(y-110)*.94)
        if d<98:
            v=0 if d>87 else 1 if d>72 else 2 if d>54 else 3 if d>35 else 4
            # Sparse ordered transitions preserve the pixel texture.
            if v>0 and abs(d-[0,87,72,54,35][v])<2 and (x+y)%3==0: v-=1
            c.set(x,y,halo[v])
# Fine celestial drafting on the wall, visible through empty spaces.
for r in [64,97]:
    stroke_arc(128,109,r,r,0,0,360,bg[3])
for t in range(0,360,30):
    a=polar(128,109,95,t);b=polar(128,109,100,t);ln(*a,*b,bg[4])
for x,y in [(38,46),(213,30),(45,177),(219,164),(105,14),(155,19),(28,120)]:
    c.set(x,y,bg[5]);ln(x-2,y,x+2,y,bg[3]);ln(x,y-2,x,y+2,bg[3])
# Floor, radial flagstones and pooled light.
c.rect(0,207,256,49,bg[1]);ln(0,207,255,207,bg[3])
for x in [-100,-35,35,84,170,224,292,355]:
    xx=max(0,min(255,x));ln(128,193,xx,255,bg[3])
for y in [216,231,252]:ln(0,y,255,y,bg[3])
c.ellipse(128,235,65,15,bg[2]);c.ellipse(128,235,54,11,bg[3]);c.ellipse(128,234,44,8,bg[4])
for x in range(74,183,6):
    c.set(x,244+(x%3),bg[4])

# The altar's cut-stone octagonal plinth.
poly([(80,238),(95,231),(161,231),(177,238),(177,246),(162,252),(94,252),(80,246)],ink)
poly([(82,238),(96,233),(159,233),(174,238),(160,244),(96,244)],stone[3])
poly([(82,240),(96,245),(160,245),(174,240),(174,245),(160,250),(96,250),(82,245)],stone[1])
ln(96,245,159,245,stone[4]);ln(96,249,159,249,stone[2])
poly([(95,213),(161,213),(160,238),(153,242),(103,242),(96,238)],ink)
poly([(98,215),(158,215),(157,237),(151,239),(105,239),(99,236)],stone[2])
poly([(98,215),(109,220),(109,238),(101,235)],stone[3])
poly([(148,219),(158,215),(156,236),(148,239)],stone[1])
c.rect(111,220,34,20,stone[1]);c.rect(113,222,30,15,stone[0])
ln(111,220,145,220,stone[4]);ln(112,238,144,238,stone[3])
for x in [102,108,148,154]:
    ln(x,221,x,234,stone[0]);ln(x+1,222,x+1,235,stone[4])
# Inlaid alchemical seal on the pedestal.
poly([(128,223),(135,233),(121,233)],gold[4]);poly([(128,225),(132,231),(124,231)],stone[0]);ln(119,229,137,229,gold[5]);c.set(128,235,cyan[4])
poly([(82,209),(99,200),(157,200),(174,209),(174,215),(157,224),(99,224),(82,215)],ink)
poly([(84,208),(100,202),(155,202),(171,208),(155,217),(100,217)],stone[4])
poly([(84,210),(100,219),(155,219),(171,210),(171,214),(155,222),(100,222),(84,214)],stone[2])
ln(100,219,155,219,stone[5]);ln(85,210,100,218,stone[3]);ln(157,217,170,210,stone[5])
c.ellipse(128,209,29,6,stone[2]);c.ellipse(128,208,27,5,gold[2]);c.ellipse(128,207,25,4,stone[0]);c.ellipse(128,207,19,3,cyan[1]);c.ellipse(128,207,12,2,cyan[3]);c.ellipse(128,207,7,1,cyan[5])
for x in [104,112,144,152]:
    ln(x,207,x+2,209,gold[6])
# Rising motes and broken levitation beams.
for x,y in [(122,198),(134,200),(125,194),(140,193),(115,201)]:
    c.set(x,y,cyan[4]);c.set(x,y+1,cyan[2])
ln(127,194,127,202,cyan[2]);ln(129,198,129,204,cyan[4])

# Toothed wheels behind the gimbals.
def gear(cx,cy,r,teeth,phase=0):
    pts=[]
    for i in range(teeth):
        for frac,rr in [(0,r-2),(.16,r-2),(.22,r),(.68,r),(.76,r-2)]:
            pts.append(polar(cx,cy,rr,phase+(i+frac)*360/teeth))
    poly([(x+1,y+2) for x,y in pts],ink);poly(pts,gold[3]);c.poly([(round(x),round(y)) for x,y in pts],ink,False)
    for i in range(teeth):
        t=phase+(i+.35)*360/teeth
        a=polar(cx,cy,r-1,t);b=polar(cx,cy,r-3,t);ln(*a,*b,gold[6] if math.sin(math.radians(t))<.3 else gold[4])
    dot(cx,cy,r-5,ink);dot(cx,cy,r-6,gold[2]);dot(cx,cy,r-8,bg[1])
    for t in range(0,360,60):
        a=polar(cx,cy,3,t+phase);b=polar(cx,cy,r-7,t+phase);ln(*a,*b,gold[4]);ln(a[0]+1,a[1],b[0]+1,b[1],gold[2])
    dot(cx,cy,4,ink);dot(cx,cy,3,gold[5]);dot(cx-1,cy-1,1,gold[7]);c.set(cx,cy,gold[1])

for args in [(62,77,19,15,5),(180,69,16,13,12),(199,121,19,16,4),(73,158,20,16,3),(156,170,20,18,0),(117,43,14,12,0)]:gear(*args)
# Rear radial braces, with riveted joints.
for t in [10,65,132,181,232,290]:
    a=polar(128,109,27,t);b=polar(128,109,73,t)
    ln(a[0]+1,a[1]+2,b[0]+1,b[1]+2,ink)
    ln(*a,*b,gold[2]);ln(a[0]-1,a[1]-1,b[0]-1,b[1]-1,gold[4]);bolt(*b)
# Meridian ring and its machined brass rim.
ring(128,108,78,86,-16,9)
# Subtle concentric inner engraved tracks.
stroke_arc(128,108,74,82,-16,0,360,gold[2])
stroke_arc(128,108,70,78,-16,180,325,gold[6])
for t in range(0,360,5):
    a=xy(128,108,77,85,-16,t);b=xy(128,108,74 if t%30 else 72,82 if t%30 else 80,-16,t)
    ln(*a,*b,gold[7] if 165<t<300 else gold[4])
for t in range(0,360,30):
    p=xy(128,108,74,82,-16,t);bolt(*p,2)

# Tiny angular runic characters engraved tangentially around the rim.
runes=[[(0,0),(0,5),(3,3),(0,2)],[(0,0),(3,0),(1,2),(1,5)],[(0,1),(3,4),(3,0),(0,4)],[(0,0),(3,2),(0,3),(3,5)],[(0,5),(0,0),(3,0),(3,2),(0,2)],[(0,0),(3,3),(0,5),(0,0)]]
def rune(x,y,angle,idx,col,scale=1):
    pts=runes[idx%len(runes)];a=math.radians(angle)
    tr=lambda p:(x+(p[0]-1.5)*math.cos(a)*scale-(p[1]-2.5)*math.sin(a)*scale,y+(p[0]-1.5)*math.sin(a)*scale+(p[1]-2.5)*math.cos(a)*scale)
    for p,q in zip(pts[:-1],pts[1:]):ln(*tr(p),*tr(q),col)
for i,t in enumerate(range(11,360,24)):
    p=xy(128,108,73,81,-16,t)
    rune(*p,t+74,i,cyan[4] if i%3 else gold[7],.8)
# Secondary concentric instrument plate, inset with a luminous zodiac scale.
ring(128,108,61,68,-16,6,0,360,1)
for t in range(0,360,6):
    a=xy(128,108,60,67,-16,t);b=xy(128,108,58.5,65.5,-16,t)
    ln(*a,*b,gold[5] if 130<t<300 else gold[3])
for i,t in enumerate(range(4,360,30)):
    p=xy(128,108,57.5,64.5,-16,t)
    rune(p[0]+1,p[1]+1,t+74,i,cyan[0],.85)
    rune(*p,t+74,i,cyan[5] if i%3==0 else cyan[3],.85)
# Precision gear train and eccentric bearings in the upper section.
gear(116,62,11,12,8)
gear(134,60,8,10,4)
gear(145,51,8,10,2)
gear(76,121,11,12,3)
for cx,cy,r in [(116,62,6),(134,60,4),(145,51,4)]:
    stroke_arc(cx,cy,r,r,0,190,330,gold[7])
# A fine split vernier, graduated and mounted on the inner meridian.
for j in range(16):
    t=192+j*3
    a=xy(128,108,51,57,-16,t);b=xy(128,108,48 if j%5==0 else 49.5,54 if j%5==0 else 55.5,-16,t)
    ln(*a,*b,gold[5])
stroke_arc(128,108,51,57,-16,190,239,gold[3])
# External index pointers.
for t in [252,342,72,162]:
    p=xy(128,108,80,88,-16,t);q=xy(128,108,88,96,-16,t)
    ln(*p,*q,ink);dot(*q,3,ink);dot(*q,2,gold[5]);dot(q[0]-1,q[1]-1,0,gold[8])
# Rear arcs of the two interlocking orbital tracks.
ring(128,108,92,43,-32,6,180,360,1)
ring(128,108,88,40,59,6,180,360,1)

# Alchemical clocks and armillary interior.
def dial(cx,cy,r,hand,kind=0):
    dot(cx+1,cy+2,r+2,ink);dot(cx,cy,r+1,gold[1]);dot(cx,cy,r,gold[5]);dot(cx-1,cy-1,r-1,gold[7]);dot(cx,cy,r-2,gold[2]);dot(cx,cy,r-3,ink);dot(cx,cy,r-4,bg[2])
    for t in range(0,360,30):
        a=polar(cx,cy,r-4,t);b=polar(cx,cy,r-6,t);ln(*a,*b,gold[6])
    for t in range(0,360,90):
        p=polar(cx,cy,r-1,t);c.set(round(p[0]),round(p[1]),gold[8])
    if kind==0:
        poly([polar(cx,cy,r-6,t) for t in [-90,30,150]],gold[3]);poly([polar(cx,cy,r-8,t) for t in [-90,30,150]],bg[2])
    else:
        dot(cx-3,cy-2,4,gold[6]);dot(cx-1,cy-3,4,bg[2]);ln(cx-4,cy+5,cx+4,cy+5,gold[3])
    q=polar(cx,cy,r-5,hand);ln(cx,cy,*q,cyan[5]);q=polar(cx,cy,5,hand+150);ln(cx,cy,*q,gold[7]);dot(cx,cy,2,gold[1]);c.set(cx,cy,gold[8])
    for t in [45,225]:bolt(*polar(cx,cy,r+2,t),1)

# Mechanical struts with visible collars and small shaft highlights.
for a,b in [((83,82),(117,101)),((139,119),(166,143)),((126,135),(124,161)),((145,99),(163,82))]:
    for dd,col in [(2,ink),(1,gold[3]),(0,gold[6])]:ln(a[0],a[1]+dd,b[0],b[1]+dd,col)
gear(106,139,12,11,10)
gear(155,83,13,12,9)
dial(85,86,16,305,1)
dial(168,140,17,225,0)
dial(124,162,12,278,0)
# Small copper pipes and soldered fittings.
c.path('M 84 105 L 84 122 L 94 132',ink,False);c.path('M 86 105 L 86 121 L 96 131',gold[5],False)
c.path('M 163 107 L 177 101 L 177 87',gold[2],False);c.path('M 164 106 L 179 100 L 179 87',gold[6],False)
for x,y in [(85,113),(90,126),(178,94)]:bolt(x,y,2)

# The core's cage: double bezel and radial calibration marks.
dot(129,111,31,ink)
dot(128,108,30,gold[3]);dot(127,107,29,gold[6]);dot(128,108,27,gold[1]);dot(128,108,25,bg[1])
for t in range(0,360,10):
    a=polar(128,108,26,t);b=polar(128,108,23 if t%30==0 else 25,t);ln(*a,*b,gold[7] if t%30==0 else gold[4])
for i,t in enumerate(range(0,360,60)):
    p=polar(128,108,27.5,t);bolt(*p,2)
    p=polar(128,108,21,t+30);rune(*p,t+120,i,cyan[4],.6)
# Faceted solar heart and sharp bloom rays.
dot(128,108,19,gold[2]);dot(128,108,17,'#a86f34');dot(128,108,15,'#e6a84d');dot(128,108,12,'#ffdb79')
for t in range(0,360,45):
    a=polar(128,108,9,t-12);b=polar(128,108,23 if t%90==0 else 18,t);d=polar(128,108,9,t+12)
    poly([a,b,d],'#f5c769')
poly([(128,88),(139,105),(135,118),(126,125),(116,110),(120,99)],'#fff0aa')
poly([(128,89),(127,108),(120,100)],'#fffbdc')
poly([(128,89),(139,105),(127,108)],'#ffe389')
poly([(139,105),(135,118),(127,108)],'#efba57')
poly([(127,108),(135,118),(126,124)],'#ffd675')
poly([(120,100),(127,108),(126,124),(116,110)],'#fff6c4')
poly([(127,99),(133,107),(127,115),(122,108)],'#ffffe6')
ln(128,83,128,95,'#ffeaa0');ln(128,121,128,132,gold[6]);ln(108,108,116,108,'#ffeaa0');ln(139,108,150,108,'#ffeaa0')
c.set(127,85,'#fffbdc');c.set(129,88,'#fffbdc')
# Four curved retaining claws.
for t in [45,135,225,315]:
    pts=[polar(128,108,30,t-6),polar(128,108,19,t-4),polar(128,108,17,t+2),polar(128,108,27,t+5)]
    poly(pts,ink);ln(*pts[0],*pts[1],gold[7]);ln(*pts[1],*pts[2],gold[4]);bolt(*polar(128,108,29,t),2)

# Front halves pass in front of the inner clocks to establish real depth.
ring(128,108,92,43,-32,6,0,180,0)
ring(128,108,88,40,59,6,0,180,0)
for rx,ry,rot in [(92,43,-32),(88,40,59)]:
    for t in range(5,179,8):
        a=xy(128,108,rx-1,ry-1,rot,t);b=xy(128,108,rx-3,ry-3,rot,t);ln(*a,*b,gold[7] if t%3 else gold[2])
    for i,t in enumerate([20,53,86,119,152]):
        p=xy(128,108,rx-3,ry-3,rot,t)
        if t in [20,86,152]:bolt(*p,2)
        else:rune(*p,t+rot+90,i,cyan[5],.7)

# A crystal is cut into deliberate pixel facets, with a brass orbital cradle.
def crystal(cx,cy,r,pal,angle=0):
    dot(cx+1,cy+2,r+2,ink)
    pts=[(cx-r*.48,cy-r*.9),(cx+r*.42,cy-r*.9),(cx+r*.92,cy-r*.3),(cx+r*.9,cy+r*.35),(cx+r*.3,cy+r*.94),(cx-r*.42,cy+r*.87),(cx-r*.94,cy+r*.23),(cx-r*.9,cy-r*.38)]
    poly(pts,ink)
    inn=[(cx+(x-cx)*.86,cy+(y-cy)*.86) for x,y in pts]
    poly(inn,pal[2])
    q=(cx-r*.12,cy-r*.05)
    colors=[pal[5],pal[4],pal[2],pal[1],pal[2],pal[3],pal[4],pal[5]]
    for i in range(8):poly([inn[i],inn[(i+1)%8],q],colors[i])
    poly([inn[0],inn[1],q,(cx-r*.52,cy-r*.1)],pal[5])
    poly([inn[1],inn[2],q],pal[3]);poly([q,inn[3],inn[4]],pal[1])
    ln(inn[0][0],inn[0][1],inn[1][0],inn[1][1],pal[-1]);ln(inn[7][0],inn[7][1],inn[0][0],inn[0][1],pal[-1]);ln(*q,*inn[4],pal[4])
    dot(cx-r*.35,cy-r*.4,1,pal[-1]);c.set(round(cx-r*.43)-1,round(cy-r*.4),pal[-1])
    # Equatorial brass clasp and two crescent prongs.
    stroke_arc(cx,cy,r+2,r*.45,angle,0,180,ink,3)
    stroke_arc(cx,cy,r+2,r*.45,angle,5,175,gold[5])
    for t in [4,176]:
        p=xy(cx,cy,r+2,r*.45,angle,t);bolt(*p,2)
    c.set(round(cx),round(cy+r*.45),gold[8])

crystal(82,32,9,[gold[1],gold[2],gold[4],gold[5],gold[6],gold[7],gold[8]],-18)
crystal(207,70,13,cyan,-24)
crystal(49,151,11,['#15233d','#203d5d','#2b5e81','#448ead','#73bdd2','#ace9ec','#e0fff5'],22)
crystal(158,182,10,[violet[0],violet[1],violet[2],violet[3],violet[4],violet[5], '#fff7ff'],-12)
# Small satellite bead with an orbit pin.
crystal(177,47,6,cyan,0)
# Specular pixels, free sparks and fine hanging measuring chains.
for x,y in [(204,54),(213,64),(46,139),(77,23),(156,169),(117,92),(142,109)]:
    ln(x-2,y,x+2,y,cyan[3] if x>190 or x<60 else gold[5]);ln(x,y-2,x,y+2,cyan[3] if x>190 or x<60 else gold[5]);c.set(x,y,cyan[6] if x>190 or x<60 else gold[8])
for x,y0,y1 in [(55,96,115),(197,143,165),(102,180,193)]:
    for y in range(y0,y1,3):
        c.set(x,y,gold[5]);c.set(x+1,y+1,gold[2])
    poly([(x,y1-1),(x+3,y1+3),(x,y1+7),(x-3,y1+3)],ink);ln(x,y1,x,y1+5,gold[6]);c.set(x+1,y1+3,cyan[4])
# Delicate luminous dust in the empty air, kept sparse.
for x,y in [(35,85),(222,97),(65,193),(188,187),(115,25),(144,15),(42,164),(217,128),(98,197),(174,199),(104,58),(145,66)]:
    c.set(x,y,gold[5]);c.set(x,y+1,gold[2])

# Final visible inscriptions, on the exposed upper and lower meridian.
for i,t in enumerate([248,262,276,290,65,82,99,116,133]):
    p=xy(128,108,73.5,81.5,-16,t)
    rune(p[0]+1,p[1]+1,t+74,i,ink,.8)
    rune(*p,t+74,i,cyan[5] if i%3==0 else cyan[4],.8)
# Worn edges and tiny mineral seams in the cut stone.
for x,y in [(92,211),(103,216),(149,218),(162,211),(100,239),(154,244),(94,247)]:
    ln(x,y,x+2,y,stone[4]);c.set(x+1,y+1,stone[1])
c.path('M 88 211 L 94 212 L 97 215 M 153 222 L 152 227 L 155 229 L 154 233',stone[0],False)
for x,y in [(116,215),(120,215),(139,214),(144,213),(104,204),(154,205)]:c.set(x,y,stone[5])
view(result,scale=3,margin=0)
assert result.stats()['size'] == (256,256) or list(result.stats()['size']) == [256,256]
assert result.stats()['colors_used'] <= 140
print(result.stats_text())
save('astral_engine',result)
finish(result)
