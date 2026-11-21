result = new_canvas(64,64,name='explosion_2_frames')
# Two 32 x 64 animation cells, with consistent centres and a clear gutter.
red='#a92c32'
scarlet='#e34426'
orange='#f87924'
gold='#ffb72d'
yellow='#ffe35a'
light='#fff6ab'
white='#fffce2'
def shape(cx,cy,pts,col):
    result.poly([(cx+x,cy+y) for x,y in pts],col)
def pix(cx,cy,pts,col):
    for x,y in pts: result.set(cx+x,cy+y,col)
# FRAME 1: a tight, hot ball, with stepped flame tongues.
x,y=16,32
shape(x,y,[(-3,-14),(0,-11),(2,-12),(4,-8),(7,-10),(7,-6),(10,-6),(9,-2),(12,1),(10,4),(11,7),(7,7),(6,11),(3,10),(0,13),(-3,10),(-7,11),(-7,7),(-10,6),(-9,3),(-12,1),(-9,-2),(-10,-6),(-7,-6),(-6,-10),(-3,-8)],scarlet)
shape(x,y,[(-3,-11),(0,-8),(2,-10),(4,-6),(6,-7),(6,-4),(9,-4),(8,-1),(10,2),(8,4),(9,6),(5,6),(5,9),(2,8),(0,11),(-2,8),(-6,9),(-6,5),(-9,4),(-8,1),(-10,0),(-7,-3),(-8,-5),(-5,-5),(-5,-8),(-3,-6)],orange)
shape(x,y,[(-3,-8),(-1,-9),(1,-6),(3,-7),(5,-4),(7,-3),(6,0),(8,2),(6,4),(5,7),(2,7),(0,9),(-2,6),(-5,7),(-5,4),(-7,3),(-6,0),(-8,-1),(-5,-3),(-5,-5),(-3,-5)],yellow)
shape(x,y,[(-2,-7),(0,-5),(3,-5),(3,-3),(5,-2),(4,1),(6,2),(4,4),(2,4),(1,7),(-1,5),(-3,5),(-3,2),(-5,2),(-4,-1),(-5,-3),(-2,-3)],light)
shape(x,y,[(-1,-4),(2,-3),(2,-1),(3,1),(1,3),(-1,3),(-2,1),(-3,0),(-2,-2)],white)
pix(x,y,[(-8,-3),(6,5),(-3,7),(3,8)],gold)
result.line(9,18,10,20,gold)
result.set(22,18,orange)
result.line(25,23,26,22,yellow)
result.set(4,29,orange)
result.set(26,44,gold)
result.set(10,47,orange)
# FRAME 2: a larger, irregular red blast with separated tongues and hot lobes.
x,y=48,32
shape(x,y,[(-2,-15),(1,-11),(4,-12),(5,-9),(9,-12),(8,-7),(12,-7),(10,-3),(14,-1),(11,2),(13,6),(9,6),(10,10),(6,9),(5,13),(2,11),(-1,15),(-3,11),(-7,12),(-7,8),(-12,9),(-10,5),(-14,3),(-11,0),(-13,-4),(-9,-4),(-10,-9),(-6,-8),(-5,-12),(-3,-10)],red)
shape(x,y,[(-2,-13),(0,-9),(3,-10),(4,-7),(7,-9),(6,-5),(10,-6),(8,-2),(12,-1),(9,2),(11,5),(7,5),(8,8),(4,7),(4,11),(1,9),(-1,12),(-3,9),(-5,10),(-5,6),(-10,7),(-8,3),(-12,3),(-9,0),(-10,-3),(-7,-2),(-8,-7),(-5,-6),(-4,-9),(-2,-7)],scarlet)
# Orange flame mantle is broken into asymmetric masses.
shape(x,y,[(-2,-10),(0,-7),(3,-8),(3,-5),(6,-7),(5,-3),(8,-4),(7,-1),(10,0),(7,2),(8,4),(4,4),(5,7),(2,6),(1,9),(-1,7),(-3,8),(-4,5),(-7,5),(-6,2),(-9,1),(-7,-1),(-8,-3),(-5,-3),(-5,-6),(-2,-5)],orange)
shape(x,y,[(-3,-7),(-1,-5),(2,-6),(2,-3),(5,-4),(4,-1),(7,0),(4,2),(5,4),(2,3),(0,6),(-2,4),(-5,4),(-4,1),(-6,0),(-4,-2),(-5,-4),(-3,-3)],gold)
# The formerly solid centre begins to cool and tear open.
shape(x,y,[(-1,-3),(2,-3),(2,-1),(4,0),(2,2),(1,4),(-1,2),(-3,2),(-2,0),(-3,-1)],orange)
shape(x,y,[(0,-1),(2,0),(1,2),(-1,1)],scarlet)
# Small bright flame edges keep a coherent clockwise energy.
shape(x,y,[(-5,-5),(-3,-5),(-3,-2),(-5,0),(-6,-1)],yellow)
shape(x,y,[(1,-7),(3,-6),(2,-4),(0,-4)],yellow)
shape(x,y,[(4,1),(6,1),(5,3),(3,3)],yellow)
result.line(44,36,46,38,yellow)
pix(x,y,[(-8,-6),(7,-5),(-8,5),(4,9),(-1,10)],gold)
# Escaping embers, angled outward, with darker tails and hot tips.
for ax,ay,bx,by in [(37,18,39,21),(56,18,54,21),(60,24,58,26),(35,41,38,39),(58,44,56,41),(43,49,44,46),(50,14,50,17),(60,36,58,35)]:
    result.line(ax,ay,bx,by,scarlet)
    result.set(ax,ay,gold)
result.rect(37,14,1,2,orange)
result.set(59,48,orange)
result.set(51,51,gold)
result.set(34,25,gold)
result.set(61,19,orange)
view(result,scale=8,margin=0)
save('explosion-effect',result)
finish(result)
