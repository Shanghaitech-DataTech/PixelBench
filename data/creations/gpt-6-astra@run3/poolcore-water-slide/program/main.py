import math
import random

result = new_canvas(128, 128, '#e4efed', name='Stillwater')
c = result
P = {
    'ceil':'#deebe9', 'beam':'#bccfd3', 'beamlight':'#f0f5ee',
    'white':'#f3f8ef', 'light':'#fcfff7', 'tile':'#dcebea',
    'tileblue':'#c9e1e4', 'tilecool':'#d0e3e4', 'grout':'#b7d1d7',
    'wallshadow':'#aacbd2', 'side':'#9ebfc9', 'deep':'#6c99a8',
    'alcove':'#88b2bc', 'alcove2':'#779eaa', 'floor':'#d9e9e7',
    'floorgrid':'#aecbd0', 'coping':'#f0f5e9', 'edge':'#7aafb9',
    'water0':'#9ed8de', 'water1':'#a1dce1', 'water2':'#a5dfe3',
    'water3':'#ace2e5', 'water4':'#b1e6e6', 'watergrid':'#9bd1d8',
    'watergridlight':'#b9e8e8', 'ripple':'#c9efeb', 'ripplewhite':'#dcf7ed',
    'rippledark':'#8ccbd2', 'reflection':'#c5e9e5',
    'slideedge':'#8eb3c0', 'slideshadow':'#afcdd5', 'slide':'#e4f0ec',
    'slidewhite':'#f8fcf1', 'trough':'#c4dfe2', 'troughdeep':'#a9cbd5',
    'yellowshadow':'#c9a63c', 'yellow':'#f0cb46', 'yellowlight':'#ffe875',
    'skinshadow':'#bd8d75', 'skin':'#e2b798', 'skinlight':'#f2c8a5',
    'hair':'#493e3d', 'hairlight':'#6b5146', 'hairshine':'#8b6953',
    'suit':'#668e95', 'suitlight':'#91b1b1', 'reflectgold':'#bacf9b'
}

def poly(points, col):
    c.poly(points, P.get(col,col))

def lerp(a,b,t):
    return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)

def quad_point(q,u,v):
    a=lerp(q[0],q[1],u)
    b=lerp(q[3],q[2],u)
    p=lerp(a,b,v)
    return (round(p[0]), round(p[1]))

rng=random.Random(27)
def tiled(q, cols, rows, colors, grout, xcuts=None):
    us=xcuts or [i/cols for i in range(cols+1)]
    for j in range(rows):
        for i in range(cols):
            col=colors[rng.randrange(len(colors))]
            c.poly([quad_point(q,us[i],j/rows),quad_point(q,us[i+1],j/rows),quad_point(q,us[i+1],(j+1)/rows),quad_point(q,us[i],(j+1)/rows)],P[col])
    for u in us:
        a=quad_point(q,u,0); b=quad_point(q,u,1)
        c.line(*a,*b,P[grout])
    for j in range(rows+1):
        a=quad_point(q,0,j/rows); b=quad_point(q,1,j/rows)
        c.line(*a,*b,P[grout])

# High, evenly lit ceiling.
c.rect(0,0,128,35,P['ceil'])
for x in [-55,1,56,117,177]:
    c.line(max(0,min(127,x)),0,63+round((x-63)*0.24),29,P['beam'])
for y,x0,x1 in [(7,0,127),(19,13,124),(27,27,116)]:
    c.line(x0,y,x1,y,P['beam'])
    c.line(x0,y+1,x1,y+1,P['beamlight'])
poly([(13,0),(23,0),(45,23),(39,23)], 'beam')
poly([(15,0),(21,0),(43,21),(40,21)], 'light')
poly([(61,2),(69,2),(70,24),(65,24)], 'beam')
poly([(63,3),(67,3),(68,22),(66,22)], 'light')
poly([(108,1),(117,1),(100,24),(95,24)], 'beam')
poly([(109,2),(114,2),(99,22),(97,22)], 'light')

# Mosaic walls converge into the far end of the hall.
tiled([(0,11),(30,29),(30,64),(0,101)],8,11,
      ['white','tile','tile','tileblue','tilecool'],'grout',
      [0,.20,.38,.53,.66,.77,.86,.94,1])
tiled([(30,29),(114,29),(114,64),(30,64)],28,12,
      ['white','tile','tile','tilecool','tileblue'],'grout')
tiled([(114,29),(127,16),(127,90),(114,64)],4,11,
      ['tile','tilecool','tileblue','wallshadow'],'grout')
c.line(30,29,114,29,P['wallshadow'])
c.line(1,12,29,29,P['white'])

# The unoccupied continuation of the building.
c.rect(48,38,19,26,P['side'])
c.rect(50,39,16,24,P['alcove'])
c.rect(52,41,13,18,P['alcove2'])
for x in [55,59,63]: c.line(x,42,x,58,P['deep'])
for y in [45,49,53,57]: c.line(52,y,65,y,P['side'])
c.rect(57,46,6,13,P['deep'])
c.rect(58,46,4,12,P['alcove2'])
poly([(50,60),(65,59),(66,63),(49,63)],'floor')
c.line(51,40,51,60,P['wallshadow'])
c.line(48,37,67,37,P['white'])

# Tiled promenade around the pool.
poly([(0,101),(30,64),(114,64),(127,90),(127,127),(0,127)],'floor')
for x in range(-120,240,15):
    farx=63+(x-63)*.28
    c.line(round(farx),64,max(0,min(127,x)),127,P['floorgrid'])
for y in [67,72,79,89,102,120]:
    left=max(0,round(30-(y-64)*30/37))
    right=min(127,round(114+(y-64)*13/26))
    c.line(left,y,right,y,P['floorgrid'])
# Shadow seams along the foot of the walls.
c.line(0,101,30,64,P['wallshadow'])
c.line(30,64,114,64,P['wallshadow'])
c.line(114,64,127,90,P['side'])
c.line(0,103,31,66,P['white'])
c.line(31,66,113,66,P['white'])
# Wide white coping and the blue inner edge.
poly([(32,67),(108,67),(127,91),(127,99),(105,73),(35,73),(0,116),(0,107)],'coping')
c.line(33,69,107,69,P['white'])
c.line(1,110,34,70,P['white'])
c.line(35,72,105,72,P['edge'])
c.line(1,114,35,72,P['edge'])
c.line(105,72,127,98,P['edge'])
for x in range(35,108,6): c.line(x,67,x,70,P['floorgrid'])
for i in range(1,8):
    x=round(33*(1-i/8)); y=round(70+40*i/8)
    c.line(x-3,y-1,x+1,y+2,P['floorgrid'])

# Clear water, with the submerged tile grid visible through it.
w=new_canvas(128,128,name='Water work')
w.poly([(35,73),(105,73),(127,99),(127,127),(0,127),(0,115)],P['water0'])
baseidx=c.color(P['water0'])
wet={(x,y) for y in range(128) for x in range(128) if w.get(x,y)==baseidx}
for y,col in [(78,'water1'),(87,'water2'),(101,'water3'),(115,'water4')]:
    w.rect(0,y,128,128-y,P[col])
# Wavering underwater grout, rather than an opaque surface grid.
for yy in [77,83,91,102,117]:
    for x in range(128):
        y=yy+round(math.sin(x*.12+yy)*.55)
        w.set(x,y,P['watergrid'])
        if yy>90 and (x//10)%3!=0: w.set(x,y+1,P['watergridlight'])
for xb in range(-110,255,19):
    pts=[]
    for y in range(73,128):
        x=round(63+(xb-63)*(y-43)/84+math.sin(y*.33+xb)*.7)
        if 0<=x<128: w.set(x,y,P['watergrid'])
# The ceiling strips break into long, pale reflections.
for y in range(76,128):
    if y%9 in [0,1,5]: continue
    x=round(39-(y-76)*.37+math.sin(y*.7)*1.7)
    width=2+(y-76)//20
    w.line(x,y,x+width,y,P['reflection'])
    if y%3==0: w.line(x+width+2,y,x+width+4,y,P['ripple'])
for y in range(78,128):
    if y%11 in [2,3,4,8]: continue
    x=round(79+(y-78)*.34+math.sin(y*.5)*1.5)
    w.line(x,y,x+2+(y-78)//18,y,P['reflection'])
# Small horizontal ripple clusters, with more breathing room at the far end.
wr=random.Random(18)
for i in range(97):
    y=wr.randrange(76,127); x=wr.randrange(0,128)
    length=wr.randrange(2,6) + (2 if y>105 else 0)
    col='ripple' if i%4 else 'ripplewhite'
    w.line(x,y,min(127,x+length),y,P[col])
    if i%3==0 and y<126:
        w.line(min(127,x+length),y+1,min(127,x+length+3),y+1,P['watergridlight'])
# A few broad caustic ribbons in the near, empty water.
for d in [
    'M 4 121 L 11 120 L 16 122 L 24 121 L 28 118 L 34 118',
    'M 33 112 L 40 111 L 46 113 L 53 112',
    'M 77 121 L 85 119 L 92 120 L 97 118 L 107 119',
    'M 98 107 L 105 105 L 111 106 L 116 104 L 125 105',
    'M 13 99 L 19 98 L 24 99 L 30 97',
    'M 49 124 L 54 122 L 61 123 L 68 121'
]: w.path(d,P['ripple'],fill=False)
# Architectural reflections, softly fragmented.
for y in range(76,93):
    if y%4==0: continue
    x=round(44-(y-73)*.32)
    w.line(x,y,x+3,y,P['watergrid'])
for y in range(128):
    for x in range(128):
        if (x,y) not in wet: w.set(x,y,None)
c.blit(w,0,0)
# Narrow submerged blue wall just beneath the coping.
c.line(35,73,104,73,P['watergrid'])
c.line(1,116,34,75,P['watergrid'])

# Columns repeat into the depth of the room.
poly([(39,65),(47,65),(49,69),(38,69)],'wallshadow')
poly([(77,63),(85,63),(89,68),(78,68)],'wallshadow')
def column(front, side, rows):
    tiled(side,2,rows,['tileblue','wallshadow','tilecool'],'grout')
    tiled(front,2,rows,['white','tile','white','tilecool'],'grout')
    c.line(*front[0],*front[3],P['white'])
column([(39,25),(44,25),(44,67),(39,67)],[(44,25),(47,28),(47,65),(44,67)],11)
c.rect(38,25,8,2,P['white'])
c.rect(38,66,7,2,P['tileblue'])
column([(77,27),(82,27),(82,64),(77,64)],[(82,27),(85,29),(85,63),(82,64)],11)
c.rect(76,27,8,2,P['white'])
c.line(77,64,82,64,P['white'])
# A close column is cut by the edge of the view.
poly([(7,88),(17,83),(23,87),(12,94)],'wallshadow')
column([(8,0),(15,0),(15,88),(8,90)],[(15,0),(21,5),(21,82),(15,88)],14)
c.line(8,89,15,87,P['white'])
c.line(15,87,20,82,P['side'])
column([(119,11),(125,8),(125,89),(119,83)],[(125,8),(127,7),(127,91),(125,89)],14)

# Slender ladder, landing rails, and supports for the water slide.
c.line(111,33,117,64,P['slideedge'])
c.line(115,32,122,65,P['slideedge'])
c.line(112,33,118,63,P['white'])
c.line(116,33,123,64,P['white'])
for y in range(39,63,4):
    xx=112+round((y-33)*.20)
    c.line(xx,y,xx+5,y,P['slideshadow'])
c.line(102,32,115,32,P['slideedge'])
c.line(103,31,115,31,P['white'])
c.line(104,30,104,24,P['side'])
c.line(114,29,114,23,P['side'])
c.line(104,23,114,23,P['side'])
c.line(105,24,113,24,P['white'])
c.line(109,59,109,76,P['slideedge'])
c.line(110,60,110,75,P['white'])
c.line(100,48,100,68,P['slideedge'])
c.line(101,49,101,67,P['slide'])
c.line(106,77,113,77,P['floorgrid'])

# A white open flume winds down in an S and empties into the pool.
slide = 'M 103 29 L 112 29 C 113 38 100 39 100 45 C 100 49 117 50 117 59 C 118 70 104 79 91 83 L 84 80 L 84 76 C 98 73 107 67 107 61 C 107 57 90 56 90 47 C 89 39 102 35 103 29 Z'
c.path(slide,P['slideedge'])
c.path('M 103 28 L 111 28 C 112 37 99 38 99 44 C 99 49 116 49 116 58 C 116 68 103 77 90 81 L 84 79 L 84 75 C 98 72 107 66 107 60 C 107 56 90 55 90 46 C 90 39 102 34 103 28 Z',P['slide'])
c.path('M 106 29 L 109 29 C 109 37 95 39 95 45 C 95 53 111 52 112 59 C 113 67 101 75 87 78 L 85 76 C 100 72 108 66 109 60 C 109 54 92 54 92 46 C 92 38 105 34 106 29 Z',P['trough'])
c.path('M 103 28 L 104 30 C 102 36 92 38 92 45 C 92 53 108 54 109 59',P['slidewhite'],fill=False)
c.path('M 111 29 C 112 37 99 39 99 44 C 99 49 116 49 116 58 C 116 68 103 77 90 80',P['slidewhite'],fill=False)
c.path('M 94 46 C 94 52 110 53 111 59 C 112 66 102 73 88 77',P['troughdeep'],fill=False)
c.path('M 99 46 C 101 50 114 51 115 57 M 116 61 C 114 70 103 77 92 80',P['slideshadow'],fill=False)
c.path('M 104 29 C 104 36 93 39 93 44 M 93 49 C 97 54 108 54 109 59',P['white'],fill=False)
# Rounded lip at the mouth, with a trickle and two soft ripples.
c.line(84,76,85,79,P['slidewhite'])
c.line(85,80,90,81,P['slideshadow'])
c.line(86,78,90,79,P['white'])
c.line(87,81,85,83,P['ripplewhite'])
c.line(82,84,91,84,P['ripple'])
c.line(79,85,82,85,P['ripple'])
c.line(92,83,96,82,P['ripple'])
c.line(84,87,91,87,P['ripple'])

# The only person, facing away into the quiet room.
# Reflections and concentric ripples sit below the floating ring.
for x0,y,x1 in [(48,100,52),(45,102,51),(72,100,77),(73,103,80),(50,106,58),(63,107,72),(56,111,66)]:
    c.line(x0,y,x1,y,P['ripple'])
c.line(57,102,65,102,P['reflectgold'])
c.line(55,104,60,104,P['reflectgold'])
c.line(63,105,67,105,P['reflectgold'])
c.line(59,108,63,108,P['watergrid'])
c.line(59,110,62,110,P['watergrid'])
# Ring body and its open centre.
c.ellipse(61,97,12,5,P['yellowshadow'])
c.ellipse(61,95,12,5,P['yellow'])
c.ellipse(61,94,11,4,P['yellowlight'])
c.ellipse(61,94,7,2,P['watergrid'])
c.line(56,93,66,93,P['water2'])
# Head, hair and back, deliberately without facial features.
c.rect(59,87,5,5,P['skinshadow'])
c.poly([(57,89),(59,88),(64,88),(66,89),(66,94),(57,94)],P['skin'])
c.line(57,89,54,92,P['skinlight'])
c.line(54,92,53,95,P['skin'])
c.line(66,89,68,92,P['skinlight'])
c.line(68,92,69,94,P['skin'])
c.line(59,92,59,95,P['suit'])
c.line(64,92,64,95,P['suit'])
c.rect(59,94,6,2,P['suit'])
c.line(60,94,63,94,P['suitlight'])
c.poly([(58,81),(60,79),(63,79),(65,81),(66,84),(65,89),(63,91),(58,89),(57,85)],P['hair'])
c.poly([(59,81),(62,80),(64,82),(64,87),(62,89),(59,87)],P['hairlight'])
c.line(59,82,59,85,P['hairshine'])
c.line(58,85,58,88,P['hair'])
c.line(64,84,64,89,P['hair'])
# The forward rim overlaps her swimsuit and arms.
c.path('M 50 95 Q 51 100 61 100 Q 71 100 72 95 L 68 96 Q 61 100 54 96 Z',P['yellow'])
c.line(55,97,59,98,P['yellowlight'])
c.line(60,98,65,98,P['yellowlight'])
c.set(52,94,P['skinlight'])
c.set(69,94,P['skinlight'])
c.line(52,99,56,100,P['yellowshadow'])

assert tuple(result.stats()['size']) == (128, 128)
assert result.stats()['colors_used'] <= 86
save('stillwater', result)
view(result,scale=4,margin=0)
finish(result)
