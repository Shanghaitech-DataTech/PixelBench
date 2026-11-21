import random
random.seed(8)
c = new_canvas(128,128,background='#edbb92',name='mountain-village-sunrise')
# restrained dawn palette
sky=['#b896ae','#c6a0ae','#d8aaa9','#e9b69e','#f3c89d','#f8d8a5']
for y in range(62):
    c.line(0,y,127,y,sky[min(5,y//11)])
# pale broken clouds
for x,y,w in [(4,15,23),(14,17,23),(87,12,25),(101,14,19),(70,27,24)]:
    c.rect(x,y,w,1,'#ecc0b5')
# rising sun, nestled behind mountain pass
c.circle(67,40,13,'#f9dba7')
c.circle(67,40,10,'#ffe9b5')
# distant peaks
c.poly([(0,49),(11,37),(18,44),(34,23),(46,38),(54,45),(65,37),(77,47),(94,25),(110,42),(119,34),(127,42),(127,77),(0,77)],'#9690aa')
c.poly([(19,43),(34,23),(45,38),(36,34),(32,37),(30,33)],'#d0b7be')
c.poly([(79,43),(94,25),(108,40),(98,35),(94,37),(91,33),(87,40)],'#cbb4bc')
c.poly([(0,57),(15,48),(23,54),(41,40),(56,57),(68,49),(79,56),(105,39),(119,52),(127,49),(127,85),(0,85)],'#777e99')
c.poly([(41,40),(56,57),(45,52),(40,47),(32,49)],'#a6a0b3')
c.poly([(105,39),(119,52),(107,47),(102,49),(99,45)],'#a5a1b2')
c.poly([(0,68),(16,57),(30,63),(47,56),(62,63),(76,58),(94,66),(115,54),(127,59),(127,88),(0,88)],'#627989')
# foothill silhouettes
c.poly([(0,77),(20,70),(38,74),(57,68),(80,74),(101,64),(127,72),(127,102),(0,102)],'#526f75')
def pine(x,y,h,dark,light):
    c.rect(x,y-h,1,h,dark)
    for top,width,base in [(y-h, max(2,h//5),y-h//2),(y-h*3//4,max(3,h//4),y-h//4),(y-h//2,max(4,h//3),y-2)]:
        c.poly([(x,top),(x-width,base),(x+width,base)],dark)
        c.poly([(x,top),(x-width,base),(x-1,base-1)],light)
    c.rect(x,y-3,2,4,'#424e51')
for x,y,h in [(3,76,12),(12,76,16),(22,74,10),(31,77,14),(42,73,9),(84,73,11),(94,74,16),(102,71,10),(114,75,16),(123,77,11)]:
    pine(x,y,h,'#506b76','#69818a')
# ground slopes
c.poly([(0,88),(18,79),(41,84),(62,78),(82,83),(106,78),(127,85),(127,128),(0,128)],'#788777')
c.poly([(0,101),(30,90),(61,91),(80,85),(107,91),(127,89),(127,128),(0,128)],'#8f967b')
c.poly([(0,116),(23,104),(48,104),(74,102),(98,105),(127,96),(127,128),(0,128)],'#a7a283')
# path warm ground and darker edging
c.poly([(64,86),(71,86),(77,96),(71,103),(58,111),(62,119),(77,128),(49,128),(44,118),(47,108),(61,99),(67,95)],'#6e776f')
c.poly([(65,86),(70,86),(74,96),(67,103),(54,111),(55,119),(71,128),(52,128),(47,118),(50,109),(64,99),(69,95)],'#c0b397')
# irregular stone pavers follow path
for x,y,w,h in [(66,90,3,2),(69,93,3,2),(67,97,4,2),(62,100,4,2),(65,103,4,2),(57,105,5,2),(52,109,5,3),(58,110,5,3),(50,114,5,3),(56,115,5,3),(50,120,6,3),(58,121,6,3),(56,126,7,2),(65,125,6,3)]:
    c.poly([(x+1,y),(x+w-1,y),(x+w,y+h-1),(x+1,y+h),(x,y+1)],'#8a8d80')
    c.line(x+1,y,x+w-1,y,'#e0c9a2')
# grasses and stones, kept off the path
for i in range(165):
    x=random.randrange(128); y=random.randrange(86,128)
    if abs(x-(65 if y<102 else 54 if y<121 else 60))<13: continue
    col=random.choice(['#7e8c72','#b8ad86','#8f967b','#c5b58a'])
    c.line(x,y,min(x+random.randrange(1,4),127),y,col)
# soft smoke rises in stepped translucent-looking warm grays
c.path('M 69 58 C 65 53 72 50 69 46 C 65 43 68 40 71 37 C 68 42 73 43 74 47 C 75 52 69 54 73 58 Z','#d0bcb0')
c.path('M 24 70 C 20 65 26 63 23 59 C 20 56 23 53 26 52 C 23 57 28 60 27 63 C 25 66 26 68 27 70 Z','#b6b1af')
c.path('M 103 67 C 100 63 105 60 104 57 C 103 54 105 52 108 50 C 106 54 108 58 107 60 C 104 64 106 65 106 67 Z','#c4bab0')
# homes, front gable and receding right roof
# coordinates: front x/y of eave, width, roof peak, wall height, side depth
def house(x,y,w,peak,h,depth,central=False):
    outline='#423d48'; wood='#9b644f'; warm='#c1855b'; shade='#754e48'
    # foundation shadow
    c.ellipse(x+w//2+depth//2,y+h+3,w//2+depth//2+3,3,'#67776b')
    c.poly([(x+w,y),(x+w+depth,y-4),(x+w+depth,y+h-4),(x+w,y+h)],shade)
    c.rect(x,y,w+1,h,warm)
    for yy in range(y+3,y+h,4):
        c.line(x,yy,x+w,yy,'#a46e50')
        c.line(x+w+1,yy,x+w+depth,yy-3,'#63494a')
        c.line(x+2,yy-1,x+w-2,yy-1,'#d39663')
    c.poly([(x-2,y),(x+w//2,peak),(x+w+2,y)],warm)
    for yy in range(peak+7,y,3):
        half=int((yy-peak)/(y-peak)*w/2)-2
        if half>0: c.line(x+w//2-half,yy,x+w//2+half,yy,'#a46e50')
    # roof mass and right shingle plane
    c.poly([(x+w//2,peak-2),(x+w//2+depth,peak-5),(x+w+depth+4,y-5),(x+w+3,y+1)],outline)
    c.poly([(x+w//2+2,peak-1),(x+w//2+depth,peak-3),(x+w+depth+1,y-5),(x+w+2,y-1)],'#755260')
    for yy in range(peak+2,y-3,3):
        frac=(yy-peak)/(y-peak)
        xx=int(x+w//2+frac*w/2)+2
        c.line(xx,yy,xx+depth-1,yy-3,'#9c6c70')
        c.set(xx+depth//2,yy-1,'#574653')
    # outline of front roof, highlighted edge
    c.line(x-3,y,x+w//2,peak-2,outline)
    c.line(x-3,y+1,x+w//2,peak-1,outline)
    c.line(x+w//2,peak-2,x+w+3,y,outline)
    c.line(x-2,y-1,x+w//2,peak-3,'#e1a875')
    c.line(x+w//2+1,peak-2,x+w+3,y-1,'#b77c62')
    # timber frame
    for xx in [x,x+w]: c.rect(xx,y,2,h,'#684747')
    c.line(x,y+h,x+w,y+h,outline)
    # foundation blocks
    c.rect(x,y+h+1,w+2,3,'#72756e')
    for xx in range(x+1,x+w,5):
        c.line(xx,y+h+1,xx+3,y+h+1,'#b8ac94')
        c.set(xx+3,y+h+3,'#4e5c5c')
    # door
    dx=x+w//2-2
    c.rect(dx,y+h-10,6,11,outline)
    c.rect(dx+1,y+h-9,4,9,'#6e4c42')
    c.line(dx+2,y+h-8,dx+2,y+h-2,'#a16b4b')
    c.set(dx+4,y+h-5,'#efbd74')
    c.rect(dx-2,y+h+3,10,2,'#cbb99a')
    # windows
    for wx in [x+4,x+w-7]:
        c.rect(wx-1,y+3,6,7,outline)
        c.rect(wx,y+4,4,4,'#f5ba67')
        c.rect(wx,y+4,2,2,'#ffe0a0')
        c.line(wx+2,y+4,wx+2,y+7,'#9b654b')
        c.rect(wx-1,y+10,6,1,'#e2a773')
    # attic diamond
    ax=x+w//2
    c.poly([(ax,peak+6),(ax-3,peak+9),(ax,peak+12),(ax+3,peak+9)],outline)
    c.set(ax,peak+8,'#ffdb8e'); c.line(ax-1,peak+9,ax+1,peak+9,'#f4ba68');c.set(ax,peak+10,'#f4ba68')
    # chimney
    chx=x+w//2+depth-2
    c.rect(chx,peak-8,4,8,'#715b60')
    c.rect(chx,peak-8,1,7,'#b5907c')
    c.rect(chx-1,peak-9,6,2,'#484550')
    c.set(chx+2,peak-4,'#ae8070')
# rear side cottages
house(10,77,23,65,17,5)
house(91,74,22,62,18,5)
# focal central cabin
house(46,71,29,55,22,9,True)
# small split rail fence on right of path
for x,y in [(82,101),(93,104),(105,107),(118,110)]:
    c.rect(x,y-7,2,10,'#64564b');c.set(x,y-8,'#e1bb86')
for x,y,nx,ny in [(82,101,93,104),(93,104,105,107),(105,107,118,110)]:
    c.line(x,y-5,nx,ny-5,'#c29767');c.line(x,y-2,nx,ny-2,'#81684f')
# foreground framing trees
pine(6,111,44,'#304e54','#45685f')
pine(122,104,42,'#304e54','#4d6f63')
pine(22,117,29,'#36574f','#5c7c62')
# warm light picking out needles
for x,y in [(5,75),(4,84),(2,94),(120,70),(117,85),(20,99),(17,109)]:
    c.line(x,y,x+2,y,'#859877')
# foreground rocks and tiny flowers
for x,y in [(8,122),(33,119),(91,121),(115,118),(37,101)]:
    c.poly([(x,y),(x+2,y-3),(x+6,y-2),(x+8,y+1)],'#68796d')
    c.line(x+2,y-3,x+5,y-3,'#bdba95')
for x,y in [(31,110),(36,113),(83,114),(87,118),(99,112),(28,125)]:
    c.line(x,y,x,y+2,'#6b805f');c.set(x,y-1,'#edc78b')
result=c
assert result.stats()['size'] == (128,128) or list(result.stats()['size']) == [128,128]
assert result.stats()['colors_used'] <= 86
print(result.stats_text())
view(result)
save('mountain-village-sunrise',result)
finish(result)
