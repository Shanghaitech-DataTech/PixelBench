import random, math
random.seed(19)
result = input_canvas.copy(name='output')
pal={p['index']:p['rgba'] for p in input_canvas.palette()}
# Transform the original pixel clusters, retaining cloud and stone detail.
stops=[(0,(8,6,15)),(30,(20,12,27)),(48,(34,17,37)),(70,(57,23,46)),(100,(85,32,52)),(135,(117,43,59)),(170,(154,55,65)),(205,(187,73,77)),(255,(223,105,94))]
def gradient(v):
    for (a,ca),(b,cb) in zip(stops,stops[1:]):
        if v<=b:
            t=(v-a)/(b-a)
            return tuple(round(ca[k]+(cb[k]-ca[k])*t) for k in range(3))
    return stops[-1][1]
stone={26:'#715062',30:'#4b384d',33:'#352d42',39:'#947080',73:'#886171',18:'#211b2b',57:'#644250',58:'#332b3b',60:'#533745',61:'#262132',63:'#44303e'}
for y in range(128):
    for x in range(256):
        idx=input_canvas.get(x,y); r,g,b,a=pal[idx]
        if idx in stone:
            col=stone[idx]
        else:
            v=.22*r+.58*g+.20*b
            col=gradient(v)
        result.set(x,y,col)
# Blood moon: a heavy dark aureole and uneven, cratered red surface.
cx,cy=128,21
result.circle(cx,cy,20,'#452039')
result.circle(cx,cy,18,'#7e283e')
result.circle(cx,cy,17,'#c34650')
result.circle(cx,cy,16,'#e76b60')
for y in range(cy-16,cy+17):
    for x in range(cx-16,cx+17):
        dx,dy=x-cx,y-cy
        if dx*dx+dy*dy<=16*16:
            v=math.sin(x*.36+math.sin(y*.7))*math.cos(y*.34)+.35*math.sin(x*.9+y*.7)
            if dx>8 or dy>11: col='#a93649' if v<.25 else '#c84c53'
            elif v<-.55: col='#c84c53'
            elif v<-.1: col='#e05a56'
            else: col='#f17c69'
            result.set(x,y,col)
result.path('M 117 12 L 119 9 L 124 8 M 115 16 L 115 19', '#ff9c7e',fill=False)
result.poly([(133,9),(139,12),(141,16),(137,15),(135,12)],'#c84c53')
result.poly([(119,25),(121,23),(125,24),(126,27),(123,29),(120,28)],'#c84c53')
result.rect(131,30,4,2,'#a93649')
# Restore the original needle silhouette where it cuts across the moon.
result.line(128,27,128,38,'#191321')
result.line(129,34,129,41,'#3b293e')
# New horned defensive towers, shaded in the same stone palette.
def tower(x,y,w,h):
    result.rect(x,y,w,h,'#181421')
    result.rect(x+1,y+1,2,h-1,'#523448')
    result.rect(x+w-2,y+1,2,h-1,'#100f1b')
    result.line(x,y+h-1,x+w-1,y+h-1,'#39283d')
    result.line(x,y+3,x+w-1,y+3,'#6b3c50')
    for yy in range(y+7,y+h-2,6):
        result.set(x+3,yy,'#634052')
    for yy in range(y+7,y+h-2,8):
        result.rect(x+w//2,yy,1,3,'#e85b4c')
        result.set(x+w//2,yy,'#ffac6a')
    # Outward hooks frame the tower like a demonic crown.
    result.poly([(x-1,y+2),(x-4,y-3),(x-4,y-11),(x-2,y-6),(x+2,y-3),(x+w//2,y-8),(x+w-2,y-3),(x+w+2,y-6),(x+w+4,y-11),(x+w+4,y-3),(x+w,y+2)],'#17121f')
    result.line(x-4,y-10,x-3,y-4,'#805064')
    result.line(x-3,y-4,x,y-1,'#543448')
    result.line(x+w//2,y-8,x+w//2-2,y-3,'#6b3c50')
tower(98,79,8,21)
tower(149,78,9,30)
# Two swept horns on the central keep, preserving its original tall needle.
result.poly([(124,65),(120,61),(118,54),(119,47),(120,54),(124,58),(126,59)],'#191421')
result.line(119,49,120,55,'#8c4b5d')
result.line(120,55,124,59,'#684053')
result.poly([(132,64),(138,59),(139,52),(137,46),(137,53),(134,57),(131,59)],'#191421')
result.line(137,47,138,53,'#754052')
# Fiery lancet windows inset into original buildings.
for x,y,h in [(126,48,4),(127,58,4),(130,70,5),(119,78,3),(123,85,4),(136,83,4),(143,89,3),(110,94,3),(117,91,3),(154,97,3)]:
    result.rect(x-1,y,3,h+2,'#1b1423')
    result.rect(x,y+1,1,h,'#e85144')
    result.set(x,y+1,'#ffa66a')
# Ragged royal banners.
for x,y in [(114,81),(140,77)]:
    result.line(x-1,y-2,x+6,y-2,'#755063')
    result.poly([(x,y-1),(x+5,y-1),(x+5,y+11),(x+3,y+8),(x+1,y+13),(x,y+8)],'#771e39')
    result.line(x+1,y,x+1,y+8,'#c43e4b')
    result.set(x+3,y+3,'#ed7b66')
    result.set(x+2,y+4,'#ed7b66')
    result.set(x+3,y+5,'#ed7b66')
# Portcullis and glowing gate on the front curtain wall.
result.path('M 137 111 L 137 102 Q 141 95 145 102 L 145 111 Z','#100e19')
result.path('M 139 110 L 139 103 Q 141 99 143 103 L 143 110 Z','#c53d3c')
result.rect(140,104,3,6,'#f77c50')
for x in [140,142]: result.line(x,102,x,110,'#422033')
result.line(138,105,144,105,'#422033')
# Red hot fissures follow the original road down the mountain.
result.path('M 142 112 L 145 114 L 144 116 L 147 119 L 147 122 L 144 127','#bd3c43',fill=False)
result.path('M 142 113 L 143 115 L 142 117 L 145 120 L 145 123 L 142 127','#ff8758',fill=False)
result.path('M 136 118 L 132 116 L 129 117 L 124 115 L 119 115','#aa3744',fill=False)
# Dark bats wheel beneath the storm's opening.
for x,y,s in [(88,34,2),(165,35,2),(177,48,1),(78,50,1),(153,15,1)]:
    result.poly([(x-3*s,y+s),(x-3*s,y-s),(x-s,y),(x,y-s),(x+s,y),(x+3*s,y-s),(x+3*s,y+s),(x+s,y+s),(x,y+2*s),(x-s,y+s)],'#120f1e')
# Small sparks rise around the walls.
for x,y in [(89,91),(96,103),(164,91),(167,105),(155,69),(108,70),(134,92),(173,115)]:
    result.set(x,y,'#da5756')
view(result,scale=3,margin=0)
finish(result)
