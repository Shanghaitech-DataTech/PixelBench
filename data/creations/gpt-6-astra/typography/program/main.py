result = new_canvas(64, 64, background='#11162c', name='pixel_quest')
c = result
# A quiet, framed night sky keeps the type in the foreground.
c.rect(1,1,62,62,'#26334b',fill=False)
c.rect(3,3,58,58,'#182239',fill=False)
for x,y,sx,sy in [(1,1,1,1),(62,1,-1,1),(1,62,1,-1),(62,62,-1,-1)]:
    c.line(x,y,x+6*sx,y,'#52647a')
    c.line(x,y,x,y+6*sy,'#52647a')
    c.set(x+2*sx,y+2*sy,'#9ea890')
# Subtle low horizon.
c.poly([(4,51),(11,46),(17,51),(22,48),(30,54),(38,49),(44,51),(52,45),(59,50),(59,60),(4,60)],'#1b2940')
c.line(5,51,58,51,'#283c50')
for x,y in [(8,8),(18,6),(46,7),(55,10),(7,30),(57,29),(5,48),(59,48)]:
    c.set(x,y,'#53657c')
# Jewel and fine rules above the name.
c.line(22,6,27,6,'#506076')
c.line(36,6,41,6,'#506076')
c.poly([(31,3),(34,6),(31,9),(28,6)],'#183b49')
c.poly([(31,3),(34,6),(31,9),(28,6)],'#61cbb2',fill=False)
c.line(31,4,31,7,'#d6f4cf')
c.set(30,5,'#d6f4cf')
letters = {
'P':['11110','10001','10001','11110','10000','10000','10000'],
'I':['11111','00100','00100','00100','00100','00100','11111'],
'X':['10001','10001','01010','00100','01010','10001','10001'],
'E':['11111','10000','10000','11110','10000','10000','11111'],
'L':['10000','10000','10000','10000','10000','10000','11111'],
'Q':['01110','10001','10001','10001','10101','10010','01101'],
'U':['10001','10001','10001','10001','10001','10001','01110'],
'S':['01111','10000','10000','01110','00001','00001','11110'],
'T':['11111','00100','00100','00100','00100','00100','00100']}
def title(word,y,tones,depth):
    pts=set()
    for n,ch in enumerate(word):
        for j,row in enumerate(letters[ch]):
            for i,v in enumerate(row):
                if v=='1':
                    for a in range(2):
                        for b in range(2):
                            pts.add((3+n*12+i*2+a,y+j*2+b))
    # Inky one-pixel keyline and a solid two-pixel bevel below.
    for x,yy in sorted(pts):
        for dx in [-1,0,1]:
            for dy in [-1,0,1,2,3]:
                c.set(x+dx,yy+dy,'#090e20')
    for x,yy in sorted(pts):
        c.set(x,yy+2,depth)
    for x,yy in sorted(pts):
        c.set(x,yy,tones[min((yy-y)//3,len(tones)-1)])
    # Top-facing edges pick up the light.
    for x,yy in sorted(pts):
        if (x,yy-1) not in pts:
            c.set(x,yy,tones[0])
title('PIXEL',13,['#fff1bf','#ffda87','#efb85c','#d58a43','#c27638'],'#754137')
title('QUEST',32,['#d9ffe1','#a8e9c5','#70cbb1','#4ca997','#3a8c89'],'#245360')
# A compact start prompt in a separate, quieter typographic tier.
small={
'P':['110','101','110','100','100'],
'R':['110','101','110','101','101'],
'E':['111','100','110','100','111'],
'S':['111','100','111','001','111'],
'T':['111','010','010','010','010'],
'A':['010','101','111','101','101'],
' ':['000']*5}
text='PRESS START'
for n,ch in enumerate(text):
    for j,row in enumerate(small[ch]):
        for i,v in enumerate(row):
            if v=='1': c.set(11+n*4+i,55+j,'#c1cbbd')
c.poly([(6,56),(8,57),(6,59)],'#e9b969')
c.set(57,57,'#e9b969')
view(result,scale=8,margin=0)
save('pixel_quest',result)
finish(result)
