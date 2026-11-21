import random
random.seed(12)
c = new_canvas(128,128,background='#d9ebec',name='Stillwater')
# Limited, cool architectural palette.
P={
'ceil':'#d7e7e8','ceam':'#bdd5da','joint':'#a6c5cf','light':'#f7fff7','lightedge':'#dceff0',
'wall':'#c6e1e5','wallhi':'#e4f1ed','grid':'#9fc8d4','gridhi':'#d2e8e9',
'left':'#b0d4dd','leftgrid':'#8bb8c8','shade':'#7daaba','dark':'#416f82','deep':'#315a70',
'deck':'#dbe8df','deckgrid':'#acc9cb','edge':'#edf4e7','edgeblue':'#85bfce',
'water':'#8bd3df','waterlight':'#a2e2e7','ripple':'#b9eced','foam':'#daf5ed',
'watermid':'#79c7d7','waterdark':'#67b6ce','watershadow':'#5caac4',
'white':'#f6f7e8','slide':'#dbeae5','slideshadow':'#a3cbd4','slideblue':'#79adbf',
'hair':'#493b44','hairhi':'#735653','skin':'#e3bfa6','skinhi':'#f2d6ba','skinshade':'#bc9991',
'yellow':'#f5cf58','yellowhi':'#fff29b','yellowshade':'#c69a3f','suit':'#648ca2'}
for k,v in P.items(): c.color(v,k)
# Room envelope and ceiling, with a single consistent distant horizon.
c.poly([(0,0),(127,0),(127,21),(103,31),(33,31),(0,17)],'ceil')
c.line(0,17,33,31,'ceam'); c.line(33,31,103,31,'ceam'); c.line(103,31,127,21,'ceam')
for x in [-85,-30,26,81,136,191]:
    c.line(x,0,72+(x-72)//5,30,'ceam')
for y in [8,20]:
    c.line(0,y,127,y,'ceam')
# Recessed fluorescent strips recede into the hall.
for pts in [[(12,3),(22,3),(46,19),(40,19)],[(62,2),(70,2),(73,20),(68,20)],[(108,2),(119,2),(94,20),(88,20)],[(47,23),(52,23),(59,28),(55,28)],[(83,23),(89,23),(85,28),(81,28)]]:
    c.poly(pts,'joint'); c.poly([(x,y-1) for x,y in pts],'light')
# Back wall and lateral walls.
c.rect(30,32,75,34,'wall')
c.poly([(0,18),(31,32),(31,66),(0,88)],'left')
c.poly([(105,31),(127,21),(127,83),(105,65)],'wallhi')
# Distant mosaic, one pixel joints and soft alternate tiles.
for y in range(35,64,5):
    c.line(31,y,105,y,'grid')
for x in range(33,106,5): c.line(x,32,x,65,'grid')
for x,y in [(39,36),(59,46),(89,36),(74,56),(99,51),(49,56)]: c.rect(x,y,4,4,'gridhi')
# Tile courses on the side walls fan gently into the perspective.
for yl,yr in [(24,36),(33,41),(43,46),(54,51),(66,56),(79,62)]: c.line(0,yl,31,yr,'leftgrid')
for x in [6,14,23]:
    top=18+round(x*14/31); bot=88-round(x*22/31)
    c.line(x,top,x,bot,'leftgrid')
for yl,yr in [(36,28),(42,38),(48,48),(54,58),(60,70)]: c.line(105,yl,127,yr,'grid')
for x in [111,119,126]: c.line(x,31-(x-105)//2,x,65+(x-105)*18//22,'grid')
# An empty, shadowed doorway in the remote hall.
c.rect(76,43,13,22,'shade'); c.rect(78,44,9,20,'deep')
c.rect(79,46,7,17,'dark'); c.rect(79,61,7,3,'shade')
c.line(76,43,88,43,'wallhi'); c.line(76,44,76,64,'wallhi')
# Long cool wall footings.
c.line(31,63,105,63,'shade'); c.line(0,86,31,64,'shade')
# Walkway surrounding the pool.
c.poly([(0,88),(31,64),(105,64),(127,83),(127,127),(0,127)],'deck')
for x in [-130,-80,-30,20,70,120,170,220,270]: c.line(72+(x-72)//9,64,x,127,'deckgrid')
for y in [67,72,79,89,104,124]: c.line(0,y,127,y,'deckgrid')
# Pool coping. The water broadens out of frame.
c.poly([(30,69),(101,69),(127,92),(127,127),(0,127),(0,101)],'edge')
c.poly([(33,73),(99,73),(127,97),(127,127),(0,127),(0,106)],'edgeblue')
c.poly([(34,75),(98,75),(127,100),(127,127),(0,127),(0,108)],'water')
# Distant submerged tile grid, progressively softer and widely spaced.
c.poly([(34,75),(98,75),(111,86),(23,86)],'waterlight')
for y in [78,82,87,94,104,118]:
    xl=max(0,34-(y-75)); xr=min(127,98+(y-75))
    c.line(xl,y,xr,y,'watermid')
for end in [-85,-45,-5,35,75,115,155,195,235]:
    sx=65+(end-65)//5
    c.line(sx,76,end,127,'watermid')
# Architectural reflections form broken vertical light bands.
for pts in [[(24,86),(30,82),(23,104),(17,111),(13,111)],[(102,78),(106,82),(119,111),(116,115)],[(70,77),(74,77),(78,119),(70,119)],[(7,110),(13,105),(10,127),(1,127)]]:
    c.poly(pts,'waterlight')
# Gentle horizontal ripples; each cluster is kept low-contrast.
for i in range(136):
    y=random.randint(77,127)
    xl=max(0,35-(y-75)); xr=min(127,97+(y-75))
    x=random.randint(xl,xr)
    w=random.choice([2,3,4,5,7]) if y<99 else random.choice([3,5,7,9])
    col=random.choice(['waterlight','ripple','watermid','waterlight'])
    c.line(x,y,min(x+w,xr),y,col)
    if i%6==0 and x+3<xr: c.line(x+2,y+1,min(x+w+3,xr),y+1,'waterlight')
# Rippling dark doorway reflection.
for y,x,w in [(77,78,8),(80,79,7),(84,78,10),(88,81,6)]: c.line(x,y,x+w,y,'waterdark')
# Column reflections.
for y,x,w in [(91,12,9),(96,8,10),(103,4,8),(109,0,7),(88,110,8),(94,116,8),(100,121,6)]:
    c.line(x,y,x+w,y,'ripple')
# Tiled columns, broad foreground piers give the room scale.
def column(x,top,w,bottom):
    c.rect(x+2,bottom,w+2,2,'deckgrid')
    c.rect(x,top,w,bottom-top,'wallhi')
    c.rect(x+w-3,top,3,bottom-top,'left')
    c.line(x,top,x,bottom-1,'lightedge')
    for y in range(top+5,bottom,6): c.line(x,y,x+w-1,y,'grid')
    for xx in range(x+4,x+w-3,4): c.line(xx,top,xx,bottom-1,'gridhi')
    c.line(x+w-3,top,x+w-3,bottom-1,'grid')
    c.rect(x,bottom-2,w,2,'slideshadow')
column(27,29,6,68)
column(100,28,7,70)
column(3,11,11,88)
column(117,9,11,88)
# Slide access landing and narrow ladder, behind the flowing chute.
c.rect(14,40,15,3,'slideshadow'); c.line(15,39,28,39,'white')
c.line(17,43,17,75,'slideblue'); c.line(23,43,23,71,'slideblue')
for y in range(48,72,5): c.line(17,y,23,y-2,'slide')
c.line(15,39,15,33,'slideblue'); c.line(15,33,27,33,'slideblue'); c.line(27,33,27,38,'slideblue')
# Curving white waterslide: underside, interior, and raised bright side walls.
c.path('M 13 39 C 26 34 45 34 54 43 C 66 55 51 65 45 71 C 40 76 47 81 59 81 L 64 88 C 49 94 30 84 33 73 C 34 64 51 58 47 50 C 43 43 26 43 13 47 Z','slideblue')
c.path('M 13 38 C 28 33 46 35 54 43 C 63 54 51 64 43 71 C 39 77 47 83 60 82 L 63 86 C 47 89 33 82 35 73 C 36 64 53 57 48 49 C 43 41 27 41 13 45 Z','white')
c.path('M 15 40 C 30 36 46 38 51 45 C 57 54 46 63 41 68 C 35 75 39 81 52 84 L 59 85 C 47 86 36 80 38 73 C 40 65 56 57 51 48 C 46 39 29 39 15 43 Z','slideshadow')
c.path('M 15 40 C 29 36 45 38 51 45 C 57 53 47 62 41 68','slide',fill=False)
c.path('M 14 38 C 29 34 45 36 52 43','light',fill=False)
c.path('M 38 71 C 33 80 46 87 61 85','light',fill=False)
# Support and wet slide outlet with a small clear wake.
c.line(48,85,48,90,'slideshadow'); c.line(49,86,49,90,'slideblue')
c.line(54,88,63,88,'ripple'); c.line(52,91,65,91,'ripple'); c.line(59,93,68,93,'waterlight')
c.set(64,89,'foam'); c.line(45,93,50,93,'ripple')
# A tiny solitary swimmer, facing the far wall. Reflection first.
c.line(79,110,89,110,'waterdark'); c.line(81,112,91,112,'watermid')
c.line(78,115,85,115,'waterlight'); c.line(86,117,92,117,'ripple')
c.ellipse(84,103,13,4,'watermid'); c.line(69,104,73,104,'ripple'); c.line(96,103,101,103,'ripple')
# Yellow inflatable ring, with an open water-filled middle.
c.ellipse(84,101,11,5,'yellowshade')
c.ellipse(84,99,11,5,'yellow')
c.ellipse(84,98,9,3,'yellowhi')
c.ellipse(84,98,6,2,'waterdark')
c.ellipse(84,100,6,2,'water')
c.line(76,102,79,103,'yellowhi'); c.line(90,102,92,101,'yellowshade')
# Shoulders, back, and arms resting on the ring.
c.poly([(81,93),(87,93),(90,97),(88,101),(80,101),(78,97)],'skin')
c.poly([(81,97),(87,97),(88,101),(80,101)],'suit')
c.line(81,96,80,100,'skinhi'); c.line(87,96,88,100,'skinshade')
c.line(80,94,77,98,'skinhi'); c.line(77,98,75,98,'skin')
c.line(88,94,91,98,'skin'); c.set(92,98,'skinhi')
# Rounded head and damp dark hair from behind, no visible face.
c.rect(82,91,5,4,'skinshade')
c.ellipse(84,89,4,5,'hair')
c.rect(81,88,7,6,'hair')
c.line(81,87,82,85,'hairhi'); c.line(83,85,85,85,'hairhi'); c.line(81,88,81,91,'hairhi')
c.set(88,90,'skin'); c.line(83,94,86,94,'hair')
# Close water glints anchor the foreground without breaking the stillness.
for x,y,w in [(17,120,9),(37,111,6),(48,124,14),(102,120,11),(6,116,5),(64,107,5),(112,111,8),(32,99,4)]:
    c.line(x,y,x+w,y,'ripple')
    if w>8: c.line(x+3,y+2,x+w-2,y+2,'waterlight')
print(c.stats_text())
print(c.matrix_text(region=(70,83,99,106)))
save('stillwater_pool',c)
finish(c)
