# Four matching 30-pixel cheerleader turnarounds on a transparent sheet.
P={
'O':'#242437','H':'#633b4a','h':'#9e5360','j':'#cc7b76',
'S':'#e89c86','s':'#ffd1a6','L':'#ffe3ba',
'T':'#279eb4','t':'#62d7d4','D':'#246078',
'W':'#fff2df','w':'#b9d7d2','N':'#343b59',
'R':'#ef6179','r':'#ff9a9b',
'G':'#f6b841','g':'#ffe47d','B':'#b66a3c'}

def rect(c,x,y,w,h,k): c.rect(x,y,w,h,P[k])
def line(c,x,y,a,b,k): c.line(x,y,a,b,P[k])
def poly(c,pts,k): c.poly(pts,P[k])
def pix(c,x,y,k): c.set(x,y,P[k])
def rows(c,x,y,pattern):
    for yy,row in enumerate(pattern):
        for xx,k in enumerate(row):
            if k!='.':pix(c,x+xx,y+yy,k)

def pom(c,x,y):
    rows(c,x,y,[
    '..O.O..',
    '.OgOgO.',
    'OgGgGgO',
    '.GBgBG.',
    'OgGgGgO',
    '.OgGgO.',
    '..O.O..'])

def pigtails(c):
    poly(c,[(8,5),(11,4),(13,7),(11,11),(11,14),(7,13),(6,10)],'O')
    poly(c,[(8,6),(10,6),(11,8),(9,10),(10,12),(8,12),(7,10)],'H')
    line(c,8,7,8,10,'h');pix(c,9,6,'j')
    poly(c,[(21,5),(24,5),(26,9),(25,13),(21,14),(21,10),(19,7)],'O')
    poly(c,[(22,6),(24,7),(25,10),(24,12),(22,12),(23,10),(21,8)],'H')
    line(c,23,7,24,10,'h')
    # Matching coral ribbons.
    rows(c,8,3,['OO.OO','OrORO','.ORO.'])
    rows(c,20,3,['OO.OO','OROrO','.ORO.'])

def feet(c,back=False):
    # Separated legs, white ankle socks and matching trainers.
    for x in [12,18]:
        rect(c,x,22,4,7,'O');rect(c,x+1,23,2,4,'s')
        line(c,x+2,23,x+2,25,'S')
        rect(c,x+1,26,2,2,'W')
    rows(c,11,28,['.OOOO..OOOO.','OWwWO..OWwWO','OOOOO..OOOOO'])
    if back:
        pix(c,13,29,'T');pix(c,20,29,'T')
    else:
        pix(c,12,29,'T');pix(c,19,29,'T')

def uniform(c,back=False):
    # Hands and arms set behind the two gold pom-poms.
    poly(c,[(11,12),(8,14),(7,18),(9,20),(12,17),(13,14)],'O')
    poly(c,[(10,14),(9,15),(8,18),(9,18),(12,15)],'s')
    poly(c,[(20,12),(23,14),(24,18),(22,20),(19,17),(18,14)],'O')
    poly(c,[(21,14),(22,15),(23,18),(22,18),(19,15)],'S')
    # Sleeveless cheer shell.
    poly(c,[(12,11),(19,11),(22,14),(20,16),(20,19),(11,19),(11,16),(9,14)],'O')
    poly(c,[(12,12),(19,12),(20,14),(19,16),(19,18),(12,18),(12,16),(11,14)],'T')
    line(c,12,13,12,16,'t');line(c,19,14,19,17,'D')
    if not back:
        line(c,12,12,15,15,'W');line(c,15,15,19,12,'W')
        pix(c,15,14,'w')
        # Tiny chest star/chevron.
        pix(c,15,16,'g');line(c,14,17,16,17,'g')
    else:
        line(c,12,12,19,12,'W');line(c,13,13,18,13,'w')
    # White belt, dark hem and alternating box pleats.
    rect(c,11,18,10,2,'O');rect(c,12,18,8,1,'W')
    poly(c,[(11,19),(20,19),(23,23),(8,23)],'O')
    poly(c,[(12,19),(19,19),(21,22),(10,22)],'T')
    line(c,12,20,11,22,'t');line(c,15,20,15,22,'D')
    line(c,18,20,19,22,'D');line(c,17,20,17,22,'t')
    line(c,10,22,21,22,'W')
    pom(c,3,15);pom(c,22,15)

def front():
    c=new_canvas(32,32,name='front')
    pigtails(c);feet(c);uniform(c)
    # Main head; fringe is stepped, never antialiased.
    rows(c,10,2,[
    '..OOOOOO....',
    '.OHHhhHHO...',
    'OHhhjjhhHO..',
    'OHhhhHHhhHO.',
    'OHHHssHhhHO.',
    'OHssssssHHO.',
    'OSsOssOssSO.',
    '.OsOssOsSO..',
    '.OsssssssO..',
    '..OSsSssO...',
    '...OOOOO....'])
    pix(c,13,8,'W');pix(c,16,8,'W')
    pix(c,12,10,'R');pix(c,18,10,'R');pix(c,15,11,'H')
    return c

def back():
    c=new_canvas(32,32,name='back')
    pigtails(c);feet(c,True);uniform(c,True)
    rows(c,10,2,[
    '..OOOOOO....',
    '.OHhhhhHO...',
    'OHhhjjhhHO..',
    'OHhjjjhhhHO.',
    'OHhhhhhhhHO.',
    'OHhhHhhHhHO.',
    'OHhhHhhHhHO.',
    '.OHhHhhHHO..',
    '.OHhHhHHHO..',
    '..OHHHHHO...',
    '...OssO.....'])
    return c

def side():
    c=new_canvas(32,32,name='left')
    # Far ponytail, arm and leg are in shadow.
    poly(c,[(19,4),(22,5),(24,8),(24,12),(21,14),(19,12),(20,9),(18,7)],'O')
    poly(c,[(21,6),(22,7),(23,10),(22,12),(21,11),(22,9),(20,7)],'H')
    line(c,21,7,22,9,'h')
    rect(c,17,22,4,7,'O');rect(c,18,23,2,4,'S')
    rect(c,18,26,2,2,'w')
    rows(c,16,28,['.OOOO','OWwWO','OOOOO'])
    # Visible leg and forward-pointing sneaker.
    rect(c,12,22,5,7,'O');rect(c,13,23,3,4,'s')
    line(c,15,23,15,26,'S');rect(c,13,26,3,2,'W')
    rows(c,9,28,['..OOOOOO','.OWWWTwO','.OOOOOOO'])
    # Profile bodice.
    poly(c,[(14,11),(18,11),(20,14),(19,18),(20,20),(12,20),(12,16),(11,14)],'O')
    poly(c,[(14,12),(17,12),(18,14),(17,18),(13,18),(13,15),(12,14)],'T')
    line(c,13,12,12,14,'W');line(c,13,14,13,16,'t')
    line(c,18,14,18,17,'D')
    rect(c,12,18,7,2,'O');rect(c,13,18,5,1,'W')
    poly(c,[(12,19),(19,19),(22,23),(9,23)],'O')
    poly(c,[(13,19),(18,19),(20,22),(11,22)],'T')
    line(c,13,20,12,22,'t');line(c,16,20,16,22,'D');line(c,18,20,19,22,'D')
    line(c,11,22,20,22,'W')
    # Near arm held down and slightly forward, pom clearly in profile.
    poly(c,[(16,13),(18,14),(18,17),(15,20),(12,19),(13,17),(14,15)],'O')
    poly(c,[(16,14),(17,15),(16,17),(14,19),(13,18),(15,16)],'s')
    line(c,16,16,14,18,'S')
    pom(c,7,17)
    # Nose projects to the left; one eye, ear, and a curved hair mass.
    rows(c,9,2,[
    '....OOOOOO..',
    '...OHhhhhHO.',
    '..OHhjjhhhHO',
    '..OHhhhHhhHO',
    '..OHssHHhhHO',
    '..OsOsHHhhHO',
    '.OssOsSHhhHO',
    'OsssssSHhhHO',
    '.OssssSHHHO.',
    '..OSssHHHO..',
    '...OOOOOO...'])
    pix(c,12,8,'W');pix(c,11,10,'R')
    rows(c,18,3,['OO.OO','OrORO','.ORO.'])
    return c

result=new_canvas(64,64,name='cheerleader_turnaround')
f=front();b=back();l=side();r=l.copy(name='right');r.mirror('h')
result.blit(f,0,0);result.blit(b,32,0);result.blit(l,0,32);result.blit(r,32,32)
print(result.stats_text())
print(result.matrix_text(region=(0,32,31,63)))
print(result.matrix_text(region=(32,0,63,31)))
save('cheerleader_turnaround',result)
finish(result)
