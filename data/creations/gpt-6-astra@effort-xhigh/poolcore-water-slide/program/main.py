import math, random

# A quiet pool hall in a deliberately small, cool palette.
C = {
 'ceil':'#dce9e5','ceilshade':'#c9deda','ceilline':'#bfd6d3','light':'#f7fff0',
 'lightedge':'#e5f7eb','fixture':'#9abbbb','wall':'#d6e9e5','white':'#eaf3e9',
 'wallblue':'#c3e0de','wallalt':'#cee5e1','grout':'#a9cece','left':'#bad8d9',
 'leftalt':'#c3dfde','leftline':'#95bec4','right':'#cee4df','rightline':'#accfce',
 'dark':'#406e79','door':'#6b9aa3','doorlight':'#83b5ba','doorblack':'#517f8b',
 'deck':'#d6e7e0','deckalt':'#c4dfdb','deckline':'#a2c7c7','deckshadow':'#92b9bd',
 'coping':'#f0f5e9','copingshade':'#b8d8d5','poolrim':'#6faeb9',
 'water0':'#8ccbd3','water1':'#95d2d7','water2':'#9bd8dc','water3':'#a3dce0',
 'water4':'#ace1e2','waterline':'#80bdc8','waterline2':'#96cdd2','waterlight':'#bde9e6',
 'foam':'#d6f3e9','reflection':'#c3e7df','reflshade':'#8bc4cc','wave':'#b1e4e2',
 'colfront':'#dcebe3','colside':'#afcfce','colline':'#b6d3d0','colsideline':'#90b8bd',
 'slideoutline':'#719fa9','slideunder':'#a4c4c8','slideinner':'#c3dcdd',
 'slideinnerdark':'#9fbfc7','slidewhite':'#f2f5eb','slidehi':'#ffffef',
 'skin':'#dda98e','skinhi':'#f5c5a0','skinshade':'#bb8478','hair':'#4e4443',
 'hairhi':'#756054','hairshade':'#393f43','suit':'#4c8594','suitlight':'#73a5ac',
 'goldshade':'#c9a845','gold':'#efc74b','yellow':'#ffe36b','yellowhi':'#fff19b',
 'floatshadow':'#6bb6c1','skinwater':'#8ac5c8',
}
r = new_canvas(128,128,C['ceil'],name='poolcore')

def poly(points,key): r.poly(points,C.get(key,key))
def line(x0,y0,x1,y1,key): r.line(x0,y0,x1,y1,C.get(key,key))
def rect(x,y,w,h,key): r.rect(x,y,w,h,C.get(key,key))

# Ceiling, with ribs and flush fluorescent fixtures.
poly([(0,0),(127,0),(104,31),(29,31)],'ceil')
poly([(0,0),(13,0),(39,31),(29,31)],'ceilshade')
for x in [18,53,88,123]:
    line(x,0,65+(x-65)*0.28,31,'ceilline')
for y in [10,21,30]: line(0,y,127,y,'ceilline')
# Narrow beams tie the room together.
poly([(0,20),(127,20),(118,24),(10,24)],'ceilshade')
line(11,24,117,24,'lightedge')
for points in [ [(19,5),(42,5),(48,11),(30,11)], [(81,5),(107,5),(98,11),(78,11)],
                [(46,25),(58,25),(59,28),(49,28)], [(76,25),(88,25),(84,28),(75,28)]]:
    poly(points,'fixture')
    inner=[(x,y-1) for x,y in points]
    poly(inner,'light')

# Back wall: alternate pale ceramic squares, with individual seams.
rect(29,31,76,32,'wall')
for j,y in enumerate(range(32,62,4)):
    for i,x in enumerate(range(30,104,4)):
        key='wallalt' if (i+2*j)%5==0 else ('wallblue' if (i+3*j)%11==0 else 'white')
        rect(x,y,3,3,key)
for y in range(31,62,4): line(29,y,104,y,'grout')
for x in range(29,105,4): line(x,31,x,61,'grout')
# A dim, unoccupied continuation of the hall.
rect(49,39,13,23,'grout')
rect(50,40,11,22,'doorblack')
rect(51,41,9,20,'door')
rect(51,41,3,20,'dark')
rect(55,43,5,14,'doorlight')
line(55,43,55,57,'grout')
line(54,57,60,57,'grout')
poly([(54,58),(60,58),(60,61),(51,61)],'deckshadow')
# Small grid-tiled inset on the far wall.
rect(71,39,15,15,'copingshade')
rect(73,41,11,11,'wallalt')
for x in [76,80]: line(x,41,x,51,'grout')
for y in [44,48]: line(73,y,83,y,'grout')
line(29,61,104,61,'deckshadow')

# Side walls mapped into trapezoids. Tiles become larger near the viewer.
for x in range(29):
    top=x*31/29
    bottom=104-x*43/29
    for y in range(math.ceil(top),math.ceil(bottom)):
        v=(y-top)/(bottom-top)
        row=int(v*8)
        z=1/(1.0+x*.055)
        col=int(8*math.log(1+x*.11))
        colprev=int(8*math.log(1+max(0,x-1)*.11))
        seam=(abs(v*8-round(v*8))<0.075) or col!=colprev
        key='leftline' if seam else ('leftalt' if (row+col)%4 else 'left')
        r.set(x,y,C[key])
for x in range(105,128):
    top=31-(x-104)*31/23
    bottom=61+(x-104)*44/23
    for y in range(max(0,math.ceil(top)),min(128,math.ceil(bottom))):
        v=(y-top)/(bottom-top)
        row=int(v*8)
        col=int(10*math.log(1+(127-x)*.12))
        colprev=int(10*math.log(1+(128-x)*.12))
        seam=abs(v*8-round(v*8))<.07 or col!=colprev
        r.set(x,y,C['rightline' if seam else ('white' if (row+col)%5==0 else 'right')])
# Left wall base course.
poly([(0,98),(29,59),(29,63),(0,108)],'deckshadow')

# Tiled floor, narrowing toward the rear of the room.
poly([(29,61),(104,61),(127,104),(127,127),(0,127),(0,104)],'deck')
for bx in range(-160,301,22):
    for y in range(61,128):
        xx=round(65+(bx-65)*(y-35)/(127-35))
        left=max(0,round(29-(y-61)*29/43)); right=min(127,round(104+(y-61)*23/43))
        if left<=xx<=right: r.set(xx,y,C['deckline'])
for y in [62,66,71,77,85,96,111,127]:
    left=max(0,round(29-(y-61)*29/43)); right=min(127,round(104+(y-61)*23/43))
    line(left,y,right,y,'deckline')
# The pool coping and the shadow just under its lip.
poly([(33,64),(96,64),(127,109),(127,127),(0,127),(0,109)],'coping')
poly([(35,67),(94,67),(127,115),(127,127),(0,127),(0,115)],'poolrim')

# Clear water. The underlying tile grid is lightly refracted.
water = new_canvas(128,128,name='water')
for y in range(69,128):
    xl=35-(y-67)*.74; xr=94+(y-67)*.71
    key=['water0','water1','water2','water3','water4'][min(4,(y-69)//12)]
    for x in range(max(0,math.ceil(xl)),min(128,math.floor(xr)+1)):
        water.set(x,y,C[key])
# A mask keeps all the reflection marks inside the water.
wi = {water.color(v) for k,v in C.items() if k.startswith('water')}
water_mask = [[water.get(x,y) in wi for x in range(128)] for y in range(128)]
def wset(x,y,key):
    if 0<=x<128 and 0<=y<128 and water_mask[y][x]: water.set(x,y,C[key])
def wline(x0,y0,x1,y1,key):
    n=max(abs(x1-x0),abs(y1-y0))
    for i in range(n+1):
        f=i/max(1,n); wset(round(x0+(x1-x0)*f),round(y0+(y1-y0)*f),key)
# Pool floor tiles converge to a vanishing point, displaced by the surface.
for bx in range(-100,231,17):
    last=None
    for y in range(70,128):
        xx=round(65+(bx-65)*(y-37)/90 + .8*math.sin(y*.34+bx*.1))
        if last: wline(last[0],last[1],xx,y,'waterline2')
        last=(xx,y)
for y in [71,75,80,86,94,104,117]:
    for x in range(128):
        yy=y+int(math.sin(x*.13+y)*.85)
        wset(x,yy,'waterline2')
# Long quiet reflections of the fluorescent ceiling.
for xx,yy,length in [(45,74,10),(43,76,14),(40,79,19),(42,83,14),(34,88,16),(36,91,12),
                     (77,72,9),(75,75,15),(77,79,19),(76,82,12),(80,86,15),
                     (28,109,13),(25,113,19),(28,119,15)]:
    wline(xx,yy,xx+length,yy,'reflection')
    if length>15: wline(xx+3,yy+1,xx+length-5,yy+1,'wave')
# Column reflections interrupt the empty water with broad broken vertical shapes.
for y in range(76,116):
    width=max(1,5-(y-76)//10)
    x=26-int((y-76)*.22)+int(2*math.sin(y*.9))
    if y%5 in (0,1,3): wline(x,y,x+width,y,'reflshade')
# Broad, broken images of the white flume and column in the surface.
for y in range(90,120):
    f=(y-90)/30
    x=round(100-9*f+2*math.sin(y*.62))
    width=round(8-5*f)
    if y%7 not in (0,4):
        wline(x,y,x+width,y,'reflection' if y<103 else 'wave')
        if y%3==1: wline(x-3,y,x-1,y,'wave')
for y in range(81,109):
    x=round(28-(y-81)*.38+math.sin(y*.75))
    if y%5 in (0,1): wline(x,y,x+3,y,'reflection')
# Small, connected caustic facets, kept low contrast.
rng=random.Random(15)
for _ in range(58):
    y=rng.randint(72,126); x=rng.randint(3,124)
    length=rng.randint(2,6) if y<95 else rng.randint(4,10)
    if water_mask[y][x]:
        wline(x,y,x+length,y,'wave')
        if rng.random()<.65:
            wline(x+length,y,x+length+2,y-1,'wave')
            wline(x+length+2,y-1,x+length+5,y-1,'wave')
# A few very pale, clipped ripple crests.
for x,y,l in [(14,121,8),(78,113,7),(92,102,10),(37,101,6),(68,121,10),(30,81,4),(72,89,6),(11,110,5),(110,117,5)]:
    wline(x,y,x+l,y,'waterlight')
r.blit(water,0,0)

# Fine coping seams and a drainage channel along the right deck.
for y in [68,75,84,95,109]:
    xl=round(33-(y-64)*.75); xr=round(96+(y-64)*.70)
    line(max(0,xl),y,max(0,xl+3),y+2,'copingshade')
    if xr<127: line(xr-2,y+2,xr,y,'copingshade')
line(100,66,126,103,'deckshadow')
for y in range(69,103,3):
    x=round(100+(y-66)*26/37)
    line(x,y,x+2,y,'copingshade')

# Square tiled columns with three-dimensional side faces.
def column(x,top,w,bottom,depth):
    poly([(x,top),(x+w,top),(x+w,bottom),(x,bottom+depth)],'colfront')
    poly([(x+w,top),(x+w+depth,top-1),(x+w+depth,bottom-depth),(x+w,bottom)],'colside')
    step=max(3,w//2)
    for y in range(top+step,bottom,step):
        line(x,y,x+w,y,'colline')
        line(x+w,y,x+w+depth,y-depth//2,'colsideline')
    for xx in range(x+step,x+w,step): line(xx,top,xx,bottom,'colline')
    line(x,top,x,bottom+depth,'white')
    line(x+w+depth,top,x+w+depth,bottom-depth,'colsideline')
    poly([(x,bottom),(x+w,bottom-1),(x+w+depth,bottom-depth),(x+w+depth,bottom-depth+2),(x+w,bottom+2),(x,bottom+depth)],'copingshade')
column(28,28,5,66,3)
column(99,29,5,62,3)
# The foreground piers frame the hall without crowding the water.
poly([(6,95),(19,91),(29,94),(17,101),(5,100)],'deckshadow')
column(6,8,10,94,4)
column(117,5,10,100,0)

# Stainless ladder and top landing, behind the slide.
line(96,34,102,62,'slideoutline'); line(100,33,107,61,'slideoutline')
line(95,34,101,61,'slidewhite'); line(99,33,106,61,'coping')
for yy in range(39,61,4):
    xx=round(96+(yy-34)*6/28)
    line(xx,yy,xx+5,yy-1,'slideunder')
poly([(91,35),(99,34),(101,38),(92,39)],'slideunder')
line(91,35,98,34,'slidewhite')
line(95,28,95,35,'slidewhite'); line(99,28,99,34,'slidewhite'); line(95,28,99,28,'slidewhite')
# A slender support under the lower bend.
line(111,70,112,86,'slideoutline'); line(112,70,113,86,'coping')
line(109,87,116,87,'slideunder')

# Curving open flume. A shaded side wall hangs below its white rim.
def bez(p0,p1,p2,p3,n):
    out=[]
    for k in range(n):
        t=k/n; u=1-t
        out.append((u*u*u*p0[0]+3*u*u*t*p1[0]+3*u*t*t*p2[0]+t*t*t*p3[0],u*u*u*p0[1]+3*u*u*t*p1[1]+3*u*t*t*p2[1]+t*t*t*p3[1]))
    return out
pts=bez((94,39),(80,39),(78,46),(87,50),16)+bez((87,50),(96,54),(114,55),(113,66),22)+bez((113,66),(113,74),(102,78),(96,82),18)+[(96,82)]
norm=[]
for i,p in enumerate(pts):
    before=pts[max(0,i-1)]; after=pts[min(len(pts)-1,i+1)]
    dx=after[0]-before[0];dy=after[1]-before[1];d=math.hypot(dx,dy)
    norm.append((-dy/d,dx/d))
def ribbon(width,offset=0,dy=0):
    left=[];right=[]
    for i,((x,y),(nx,ny)) in enumerate(zip(pts,norm)):
        w=width*(.58+.42*i/(len(pts)-1))
        left.append((round(x+nx*(w+offset)),round(y+ny*(w+offset)+dy)))
        right.append((round(x+nx*(-w+offset)),round(y+ny*(-w+offset)+dy)))
    return left+right[::-1]
poly(ribbon(6.0,dy=4),'slideoutline')
poly(ribbon(5.8,dy=3),'slideunder')
poly(ribbon(6.0),'slidewhite')
poly(ribbon(3.7,offset=.2),'slideinnerdark')
poly(ribbon(2.6,offset=-.45),'slideinner')
# A continuous light on the upper edge makes the S-shaped channel legible.
last=None
for i,((x,y),(nx,ny)) in enumerate(zip(pts,norm)):
    w=5.2*(.58+.42*i/(len(pts)-1))
    p=(round(x-nx*w),round(y-ny*w))
    if last: line(*last,*p,'slidehi')
    last=p
# Open flared mouth and pale spill into the pool.
line(91,80,100,85,'slidewhite')
line(91,81,99,86,'slidehi')
line(92,84,90,88,'foam'); line(96,86,94,89,'waterlight')
line(86,89,90,89,'waterlight');line(95,90,102,90,'waterlight')
line(88,92,96,92,'wave');line(104,87,107,87,'waterlight')

# Ripples and a softly refracted shadow beneath the solitary swimmer.
for x,y,l,key in [(48,101,20,'floatshadow'),(51,103,15,'reflshade'),(46,104,5,'waterlight'),(64,104,6,'waterlight'),(48,108,11,'wave'),(53,112,9,'wave'),(44,97,3,'foam'),(69,98,5,'waterlight')]:
    line(x,y,x+l,y,key)
# Legs visible faintly through the crystal water.
poly([(55,99),(58,99),(57,106),(55,109),(53,109),(55,104)],'skinwater')
poly([(59,99),(61,99),(63,106),(62,109),(60,107)],'skinwater')
line(55,106,56,108,'wave');line(61,105,62,107,'wave')
# The yellow ring has a dark inner opening and a warm shaded lower edge.
r.ellipse(58,98,10,5,C['goldshade'])
r.ellipse(58,97,10,4,C['gold'])
r.ellipse(58,96,9,3,C['yellow'])
r.ellipse(58,96,6,2,C['floatshadow'])
line(51,95,54,94,'yellowhi');line(62,94,65,95,'yellowhi')
# Back, shoulders and swimsuit, viewed from behind.
poly([(55,91),(61,91),(62,96),(60,98),(55,97),(54,94)],'skin')
poly([(55,94),(60,94),(61,97),(59,98),(55,97)],'suit')
line(55,92,55,94,'suitlight');line(60,92,60,94,'suitlight')
line(54,92,51,95,'skinhi');line(61,92,65,95,'skin')
line(51,95,51,97,'skin');line(65,95,65,97,'skinhi')
rect(57,89,3,3,'skinshade')
# A little dark bob, with a single cool highlight and loose hair at the nape.
poly([(56,83),(59,83),(61,85),(61,89),(59,92),(56,91),(54,88),(54,85)],'hairshade')
poly([(56,83),(59,83),(60,85),(60,89),(57,90),(55,88),(55,85)],'hair')
line(56,84,58,84,'hairhi');line(55,85,55,87,'hairhi')
r.set(61,88,C['skin'])
# Front edge of the ring catches the even ceiling light.
line(53,100,62,100,'yellow');line(55,101,60,101,'gold')
r.set(49,97,C['yellowhi']);r.set(67,97,C['yellow'])

result=r
w,h,rgba=result.to_rgba()
visible_colors={tuple(rgba[i:i+4]) for i in range(0,len(rgba),4) if rgba[i+3]>0}
assert (w,h)==(128,128)
assert len(visible_colors)<=86
print(f'Final: {w}x{h}, {len(visible_colors)} visible colors')
view(result,scale=4,margin=0)
save('poolcore-water-slide',result)
finish(result)
