# All frames use only colours sampled from the supplied sprite.
chars='.abcdefghijklmnopqrstuvw'
pal=[0]+[input_canvas.color('c'+str(i)) for i in range(23)]
source=[]
for y in range(50):
    source.append([chars[pal.index(input_canvas.get(int((x+.5)*66/28),int((y+.5)*119/50)))] for x in range(28)])
def make_grid(name,grid):
    c=new_canvas(28,50,name=name)
    for y,row in enumerate(grid):
        for x,ch in enumerate(row):
            if ch!='.': c.set(x,y,pal[chars.index(ch)])
    return c

def output(c,name):
    out=new_canvas(66,119,name=name)
    # Rebuild the exact original coarse grid at its supplied display size.
    for y in range(119):
        for x in range(66):
            out.set(x,y,c.get(int(x*28/66),int(y*50/119)))
    return out

def blank(): return [['.']*28 for _ in range(50)]
def setrow(g,y,x,text):
    for i,ch in enumerate(text):
        if 0<=x+i<28: g[y][x+i]=ch

def stamp(dst,src,dx=0,dy=0):
    for y,row in enumerate(src):
        for x,ch in enumerate(row):
            if ch!='.' and 0<=x+dx<28 and 0<=y+dy<50: dst[y+dy][x+dx]=ch

# Reconstruct the portion of the dress covered by the side ponytail from
# the matching sleeve and bodice on the other side.
clean=[r[:] for r in source]
for y in range(19,32):
    for x in range(14,28): clean[y][x]=source[y][27-x]

# Asymmetric projection: the visible near half remains broad, while the far
# half is foreshortened. Head, shoulders, waist and hem have separate profiles.
def quarter():
    g=blank()
    for y in range(50):
        if y<22: left,axis,right=2,19,27
        elif y<29: left,axis,right=3,18,26
        elif y<38: left,axis,right=3,17,26
        else: left,axis,right=2,17,26
        for x in range(left,right):
            if x<axis: sx=int((x-left+.5)*14/(axis-left))
            else: sx=14+int((x-axis+.5)*14/(right-axis))
            g[y][x]=clean[y][min(27,sx)]
    # Restore single-pixel contours lost in the projected far side.
    for y in range(19):
        xs=[x for x in range(28) if g[y][x]!='.']
        if xs:
            g[y][xs[-1]]='a' if y<14 else 'i'
    # A broad near eye and a narrower far eye, with the same blue irises.
    for y,near_eye,bridge,far_eye in [
        (16,'kiik','hgggh','kik'),
        (17,'liml','ggggg','mil'),
        (18,'gnnl','ggggh','nnl')]:
        setrow(g,y,12,near_eye+bridge+far_eye)
        g[y][24]='i'
    setrow(g,15,21,'haaa')
    g[19][23]='h'
    g[19][24]='i'
    g[20][23]='i'
    return g

# The same gathered curl is foreshortened over the far shoulder.
q1=quarter()
far=blank()
for y in range(19,31):
    for nx in range(20,27):
        sx=17+int((nx-20+.5)*11/7)
        ch=source[y][min(sx,27)]
        if ch in 'abcdef': far[y][nx]=ch
stamp(q1,far)

# The reverse three-quarter projection, keeping the ponytail on the
# character's anatomical left shoulder instead of mirroring the hairstyle.
q2=[r[::-1] for r in quarter()]
near=blank()
for y in range(19,31):
    for x in range(16,28):
        if source[y][x] in 'abcdef':
            # Compress the curl slightly to match the angled shoulder.
            nx=17+int((x-17)*.85)
            if 0<=nx<28: near[y+1][nx]=source[y][x]
stamp(q2,near)

# Back of the same dress. The skirt's panels and hem continue all the way
# around, with a higher back neckline and a simple central back seam.
rear=blank()
for y in range(22,50): rear[y]=clean[y][::-1]
back_rows={
22:'....pqqqqpijjjjjjipqqqqp....',
23:'...pqrrsqpihhooohipqsrqp...',
24:'..ptrsrsqpthhhhhtpqsrssrtp..',
25:'..pqsqssqsttttttssqssqsqp..',
26:'...pqsstqssssqssssqtssqp...',
27:'..ijpppqqsrssqssrsqqpppji..',
28:'..iohopqqsrrsqssrrsqqpohoi..',
29:'..ighjppqqsssqssssqqppjhgi..',
30:'.iouojippttttqttttpipijouoi.',
31:'.iuujivipqtqqqqqqtqpivijuui.',
}
for y,text in back_rows.items():
    # These rows are centred by their actual width.
    rear[y]=['.']*28
    setrow(rear,y,(28-len(text))//2,text)
# Shape the back bodice to preserve the original tailored waist.
for y in [30,31]:
    for x in range(12,16): rear[y][x]='t' if y==30 else 'q'
for y in range(32,37):
    for x in range(11,17): rear[y][x]='q'
    rear[y][13]='t'
    if y<35:
        rear[y][11]='s'
        rear[y][12]='s'
for y in range(38,49):
    rear[y][13]='s'
    if y<43: rear[y][14]='q'
# Crown silhouette and rich brown palette are retained from the source.
for y in range(10): rear[y]=source[y][:]
# Continue the crown strands down the back of the head; there is no front
# part or face opening on this side.
for y,text in {
    6:'efedddcddddd',
    7:'bddccddccddd',
    8:'cdddeeeeddcc',
    9:'deffddddffed',
}.items(): setrow(rear,y,8,text)
# Swept back hair converging on the left nape.
hair_rows={
10:'.acfacafccfddccdfccfacafca.',
11:'..adfaadabcddddccbadaafda..',
12:'..abdcabccccddccccbaacdba..',
13:'...acdadccddddcccdaddaca...',
14:'...acfeecddccddceefccaca...',
15:'...abdeffedccddeffeddcba...',
16:'....acddfeedddffedddcba....',
17:'....abcddfffffedddccba.....',
18:'.....abcdddeedddccbaa.....',
19:'......abccdddddccbaa......',
20:'.......aabcccccbbaa.......',
21:'........aabbcbbaa.........',
22:'..........aaiaa...........',
}
for y,text in hair_rows.items():
    rear[y]=['.']*28
    setrow(rear,y,(28-len(text))//2,text)
# Gathered curls sit on the character's left, screen-left from behind.
back_hair=blank()
for y in range(19,31):
    for x in range(16,28):
        if source[y][x] in 'abcdef': back_hair[y+1][27-x]=source[y][x]
stamp(rear,back_hair)

f1=output(make_grid('left_grid',q1),'frame_1_left_45')
f2=output(make_grid('right_grid',q2),'frame_2_right_45')
f3=output(make_grid('rear_grid',rear),'frame_3_rear')
# Confirm all final pixels are from the original palette, then export.
allowed=set(pal)
for i,c in enumerate([f1,f2,f3],1):
    assert c.stats()['size']==[66,119] or tuple(c.stats()['size'])==(66,119)
    assert all(c.get(x,y) in allowed for y in range(119) for x in range(66))
    save('turn_frame_'+str(i),c)
    view(c,scale=4,margin=0)
finish([f1,f2,f3])
