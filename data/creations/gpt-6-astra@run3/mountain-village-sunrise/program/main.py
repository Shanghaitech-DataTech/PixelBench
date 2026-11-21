import random
random.seed(12)
result = new_canvas(128,128, background='#edac88', name='mountain-village-sunrise')
c=result
# A limited, shared palette: cool mountains against the warm village.
sky=['#88839e','#a28aa5','#bb92a5','#d49ba0','#e9ac91','#f2bd91','#f8cf9c']
for i,col in enumerate(sky): c.rect(0,i*7,128,7,col)
c.rect(0,49,128,25,sky[-1])
# Thin banks of dawn cloud.
c.rect(7,14,25,2,'#c8a2af'); c.rect(13,12,15,2,'#c8a2af')
c.rect(91,9,28,2,'#b79aaf'); c.rect(98,7,13,2,'#b79aaf')
c.rect(87,23,30,2,'#e9b4a6'); c.rect(96,21,16,2,'#e9b4a6')
c.rect(0,31,27,2,'#f8cf9c')
c.circle(64,35,12,'#f8dba4'); c.circle(64,35,9,'#ffe9b4')
# Far peaks and sunlit snow planes.
c.poly([(0,57),(0,43),(12,34),(23,42),(40,21),(60,46),(73,35),(89,18),(110,42),(120,34),(127,41),(127,68)],'#938ba4')
c.poly([(21,43),(40,21),(51,35),(43,31),(39,33),(36,30),(30,41)],'#efd0bc')
c.poly([(40,23),(43,32),(51,36),(59,46),(44,40)],'#b3a4b7')
c.poly([(73,35),(89,18),(104,35),(94,30),(89,25),(84,31),(80,30)],'#f5d9bd')
c.poly([(89,21),(94,30),(103,34),(111,43),(98,38)],'#b7a7b8')
c.poly([(0,49),(12,35),(18,41),(11,40),(7,45)],'#c4b2c0')
# Overlapping mountain ridges.
c.poly([(0,60),(13,50),(25,54),(43,40),(61,55),(76,44),(98,55),(116,44),(127,48),(127,79),(0,79)],'#777e95')
c.poly([(0,63),(20,59),(38,65),(59,55),(77,62),(100,53),(127,64),(127,84),(0,84)],'#64798a')
c.poly([(0,71),(23,66),(46,72),(66,66),(91,72),(111,64),(127,67),(127,88),(0,88)],'#536e78')
# Tiny trees on the far slopes.
for x in range(0,128,4):
    y=72+int(3*__import__('math').sin(x*.12))
    h=random.randrange(4,10)
    c.poly([(x,y-h),(x-3,y),(x+3,y)],'#4b6870')
# Meadow terraces, with a warm rim on each crest.
c.poly([(0,86),(17,78),(37,81),(62,77),(84,79),(104,74),(127,80),(127,128),(0,128)],'#789075')
c.poly([(0,87),(17,79),(37,82),(62,78),(83,80),(104,75),(127,81),(127,84),(105,79),(85,84),(61,82),(36,86),(17,83),(0,91)],'#a2aa79')
c.poly([(0,106),(25,96),(47,102),(73,96),(102,96),(127,88),(127,128),(0,128)],'#526e59')
c.poly([(0,108),(25,98),(47,104),(73,98),(102,98),(127,90),(127,94),(102,102),(74,102),(47,108),(25,102),(0,112)],'#829164')
# Path curves from the central doorstep into the foreground.
c.poly([(62,90),(70,90),(70,98),(62,107),(64,114),(80,128),(40,128),(46,116),(49,108),(59,98)],'#595f59')
c.poly([(63,92),(69,92),(67,99),(58,108),(59,116),(74,128),(45,128),(50,116),(52,108),(61,99)],'#a5a28a')
# Short branches serve the other two houses.
c.poly([(26,95),(30,93),(47,99),(59,99),(57,103),(44,103)],'#a5a28a')
c.poly([(99,90),(103,91),(87,98),(68,101),(68,98),(85,95)],'#a5a28a')
# Individual irregular paving stones, kept distinct from the mortar.
stonecols=['#d2c6a5','#bcb69b','#879085','#e2d0a9']
for x,y,w,h in [(63,94,4,2),(61,98,5,2),(58,102,5,2),(54,106,5,3),(57,110,4,3),(51,112,4,3),(51,117,6,3),(58,117,5,3),(48,122,7,4),(57,122,7,3),(66,125,6,3),(45,127,8,1),(59,127,6,1),(33,98,4,2),(40,100,5,2),(47,100,5,2),(76,98,5,2),(85,96,4,2),(93,93,4,2)]:
    c.poly([(x+1,y),(x+w-1,y),(x+w,y+1),(x+w-1,y+h),(x,y+h),(x,y+1)],random.choice(stonecols))
# Grass clusters on the banks.
for i in range(170):
    x=random.randrange(128); y=random.randrange(83,128)
    if c.color_name(c.get(x,y)) in ['#526e59','#789075','#829164']:
        col=random.choice(['#98a271','#647e60','#b2ad76'])
        c.line(x,y,x+random.choice([1,2,3]),y,col)
        if i%4==0: c.set(x+1,y-1,col)
# Pines have stepped boughs and warm edge lights.
def pine(x,y,h,near=False):
    dark='#253f46' if near else '#36575a'
    mid='#365c57' if near else '#426b64'
    lit='#577b62' if near else '#648574'
    c.rect(x-1,y-h//2,3,h//2+2,'#5b5145')
    for k in range(4):
        top=y-h+k*h//6
        width=max(3,int(h*(.14+.045*k)))
        bot=top+int(h*.38)
        c.poly([(x,top),(x-width,bot),(x+width,bot)],dark)
        c.poly([(x,top),(x-width+1,bot-1),(x-1,bot-3)],mid)
        c.line(x-1,top+3,x-width+2,bot-3,lit)
    c.set(x,y-h,'#a8aa77')
pine(7,84,26); pine(43,83,22); pine(117,77,30); pine(83,77,19)
# Wood cabins; the front-facing gable of the central house is the focal point.
def house(x,y,w,h):
    # y = wall top, eave; h = wall height
    ridge=y-w//3
    c.ellipse(x+w//2,y+h+2,w//2+4,3,'#40574e')
    c.rect(x,y,w,h,'#614a40')
    c.rect(x+2,y,w-5,h-2,'#b78251')
    c.rect(x+w-6,y,6,h,'#78553e')
    for yy in range(y+3,y+h-2,4):
        c.line(x+2,yy,x+w-7,yy,'#8b603f')
        c.line(x+3,yy+1,x+w-8,yy+1,'#d0995d')
        c.line(x+w-5,yy,x+w-1,yy,'#4e4140')
    # stone footings
    c.rect(x,y+h-2,w,3,'#485051')
    for xx in range(x+1,x+w-1,5): c.rect(xx,y+h-2,4,2,'#9d9a82')
    # timber gable
    c.poly([(x,y),(x+w//2,ridge+2),(x+w,y)],'#d09a5f')
    for yy in range(ridge+5,y,3):
        span=int((yy-ridge)*1.4)
        c.line(max(x+2,x+w//2-span//2),yy,min(x+w-2,x+w//2+span//2),yy,'#a27348')
    # chimney sits behind roof
    cx=x+w-8
    c.rect(cx,ridge-2,4,10,'#665653'); c.rect(cx,ridge-2,2,9,'#a48a74')
    c.rect(cx-1,ridge-3,6,2,'#51494b')
    # roof silhouette, warm lit left slope and cool far eave
    c.poly([(x-4,y+1),(x+w//2-1,ridge-3),(x+w//2+3,ridge-3),(x+w+4,y+1),(x+w+4,y+4),(x+w//2+1,ridge+2),(x-4,y+4)],'#403d43')
    c.poly([(x-3,y),(x+w//2,ridge-2),(x+w//2+1,ridge),(x-2,y+2)],'#e3ad6d')
    c.poly([(x+w//2+2,ridge-1),(x+w+3,y+1),(x+w+1,y+2),(x+w//2+2,ridge+2)],'#9a6651')
    for xx in range(x+1,x+w//2,4):
        yy=y-int((xx-x)*2/3)
        c.set(xx,yy,'#a77352')
    # front structural timbers
    c.rect(x+1,y+2,2,h-4,'#62483b'); c.rect(x+w-8,y+2,2,h-4,'#62483b')
    # doorway to right of center
    dx=x+w//2
    c.rect(dx-1,y+h-12,8,11,'#694c3b'); c.rect(dx,y+h-11,5,10,'#403d3b')
    c.line(dx+1,y+h-10,dx+1,y+h-3,'#80573b'); c.set(dx+4,y+h-6,'#efbd72')
    c.rect(dx-2,y+h,10,2,'#c4b18b')
    # luminous divided window
    c.rect(x+5,y+4,7,8,'#4c4140'); c.rect(x+6,y+5,5,5,'#ffe3a0')
    c.line(x+8,y+5,x+8,y+9,'#ae794b'); c.line(x+6,y+7,x+10,y+7,'#ae794b')
    c.rect(x+4,y+11,9,2,'#d7a366')
    # attic glint
    c.rect(x+w//2-1,y-5,3,4,'#584441'); c.rect(x+w//2,y-4,1,2,'#ffda8a')
    return cx+1,ridge-4
sm1=house(14,79,25,18)
sm2=house(91,74,24,18)
sm3=house(48,71,33,24)
# Soft segmented chimney smoke; pixel clusters drift into the dawn.
def smoke(x,y,central=False):
    c.poly([(x,y),(x-1,y-4),(x+1,y-7),(x,y-10),(x-4,y-13),(x-4,y-16),(x-1,y-18),(x+3,y-18),(x,y-15),(x+1,y-12),(x+4,y-9),(x+4,y-6),(x+1,y-3),(x+2,y)],'#c2b5b2')
    c.line(x,y-2,x+1,y-6,'#e0c7b9')
    c.rect(x-4,y-17,4,2,'#d5c0b9')
    c.rect(x-2,y-21,5,2,'#cfb7b4')
smoke(*sm1); smoke(*sm2); smoke(*sm3,True)
# Fence fragments, deliberately opening onto the path.
for x,y in [(17,105),(26,102),(35,104),(91,104),(101,102),(111,99)]:
    c.rect(x,y-7,2,10,'#514c3e'); c.set(x,y-8,'#dac08b')
for a,b in [((18,100),(35,99)),((18,103),(35,102)),((92,99),(112,94)),((92,102),(112,97))]:
    c.line(*a,*b,'#b39a68')
# Foreground framing and stones.
pine(5,117,47,True); pine(122,114,49,True)
pine(17,125,30,True)
for x,y in [(30,116),(86,119),(99,110),(39,111),(83,106)]:
    c.poly([(x,y),(x+2,y-3),(x+6,y-3),(x+8,y),(x+7,y+2),(x+1,y+2)],'#394f4a')
    c.poly([(x+1,y-1),(x+3,y-3),(x+6,y-3),(x+6,y)],'#8c9782')
for x,y in [(35,119),(90,115),(85,124),(29,110),(104,119),(37,125)]:
    c.line(x,y,x-1,y-4,'#a4a271'); c.line(x,y,x+2,y-3,'#a4a271')
    c.set(x-1,y-4,'#e6bc79')
view(result)
finish(result)
