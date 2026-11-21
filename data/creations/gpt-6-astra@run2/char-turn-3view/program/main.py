# Work at the character's original 28 x 50 pixel grid.
src=input_canvas.select(0,0,66,119).resize(28,50).preview()
S=[[src.get(x,y) for x in range(28)] for y in range(50)]
def patch(c,x,y,rows):
    chars='.123456789ABCDEFGHIJKLMNOP'
    for j,row in enumerate(rows):
        for i,v in enumerate(row):
            if v!=' ': c.set(x+i,y+j,chars.index(v))
# Remove the front braid to recover the symmetrical dress underneath.
body=src.copy()
for y in range(21,31):
    for x in range(14,28):
        body.set(x,y,S[y][27-x])
# Turning toward screen right, the character's left.
def turn_body():
    c=new_canvas(28,50)
    for y in range(21,50):
        # asymmetrical projection: broad near side, narrow far side
        for x in range(4,27):
            if x<=16: sx=round(13.5+(x-16)*13.5/12)
            else: sx=round(13.5+(x-16)*13.5/10)
            sx=max(0,min(27,sx))
            c.set(x,y,body.get(sx,y))
    return c
f1s=turn_body()
f2s=f1s.copy().mirror()
# Draw the hair cap as two curved surfaces; the original curl clusters persist.
def head(c, flip=False):
    h=new_canvas(28,50)
    for y in range(14):
        for x in range(2,27):
            sx=round((x-2)*13/15) if x<=17 else round(13+(x-17)*14/9)
            if 0<=sx<28: h.set(x,y,S[y][sx])
    # Near side hair and ear; the cheek and features sit on the rotated front plane.
    patch(h,3,13,[
        '134113431',
        '911346321',
        '977134121',
        '.97811318',
        '.98A13187',
        '..99A1887',
        '....98877',
        '.....9AF8',
        '......9AA',
    ])
    # Forehead, eyes and cheeks; near eye remains broad, far eye foreshortens.
    patch(h,11,13,[
        '1337777331181',
        '8878777787831',
        '811A87778A118',
        '1B99B8778B9B1',
        '8C9DC7777CDC8',
        '77EEC77777EC7',
        '8777777777778',
        'AF877777778F9',
        '.AAF87778FA9.',
        '...AAAAAAA...',
    ])
    # Outer face contour and small nose step.
    h.set(24,16,8).set(24,17,7).set(25,18,7).set(24,18,7)
    h.set(24,19,8).set(24,20,9)
    if flip: h.mirror()
    c.blit(h,0,0)
head(f1s)
head(f2s,True)
# Braid: retain the original interlocking dark brown strands, with projection.
braid=new_canvas(11,13)
for y in range(19,32):
    for x in range(16,27):
        v=S[y][x]
        if v in (1,2,3,4,5,6): braid.set(x-16,y-19,v)
# Far shoulder, narrower and behind the front of the dress.
braid.select(0,0,11,13).resize(6,13).copy_to(21,19,f1s,mode='over')
# Near shoulder on opposite turn: original braid is broad and fully visible.
braid.select(0,0,11,13).resize(10,13).copy_to(16,19,f2s,mode='over')
# Back: retain the silhouette, sleeves, hands and skirt fabric, redraw back bodice.
f3s=body.copy()
f3s.clear(0,0,28,23)
# Rounded rear hair volume, original silhouette and curls.
for y in range(14):
    for x in range(28): f3s.set(x,y,S[y][x])
# Fill central forehead opening with swept hair texture.
patch(f3s,10,7,[
 '43122344',
 '51233215',
 '54144315',
 '63155416',
 '43144313',
 '21233112',
 '13322331',
])
patch(f3s,3,14,[
 '1134541233214543211111',
 '7136532344323653211879',
 '.81334234554324311889.',
 '.91123445665432118A9..',
 '..1133454433453219...',
 '...12344322344311....',
 '....112332233211.....',
 '......11111111.......',
])
# Closed high back collar, same silver fabric.
patch(f3s,8,21,[
 'GGG88FF88GGG',
 'HHGGA AAGGHH'.replace(' ', 'A'),
 'JJHHGGGGHHJJ',
 'JJJHHHHHHJJJ',
 'HHJJJHHJJJHH',
 'KHHJJHHJJHHK',
 'GKHHJHHJHHKG',
 'GGKHHHHHHKGG',
 'GGGKH H HGGG'.replace(' ', 'H'),
 'GGGKKHHKKGGG',
 'GGKHJJJJHKGG',
 'GKHJJJJJJHKG',
 'GKHHJJJJHHKG',
 'GKKHHHHHHKKG',
 'GGKKHHHHKKGG',
 'HGGKKKKKKGGH',
])
# The braid stays on the anatomical left (screen left from behind).
braid.select(0,0,11,13).flip().copy_to(2,19,f3s,mode='over')
# Export at exactly the same dimensions as the supplied character.
def full(c,name):
    out=new_canvas(66,119,name=name)
    c.select(0,0,28,50).resize(66,119).copy_to(0,0,out)
    return out
f1=full(f1s,'left_45')
f2=full(f2s,'right_45')
f3=full(f3s,'rear')
view(f1,scale=4)
view(f2,scale=4)
view(f3,scale=4)
finish([f1,f2,f3])
