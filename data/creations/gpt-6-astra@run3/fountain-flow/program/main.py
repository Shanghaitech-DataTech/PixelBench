result = new_canvas(64, 88, name='running_fountain')
result.blit(input_canvas, 0, 12)
water = new_canvas(64,88,name='flow')
dark='#1d8baa'
blue='#2ec7dc'
light='#8ae9ee'
white='#dffff6'
def line(x,y,xx,yy,c): water.line(x,y+12,xx,yy+12,c)
def rect(x,y,w,h,c): water.rect(x,y+12,w,h,c)
def pix(x,y,c): water.set(x,y+12,c)
def path(s,c):
    # paths are drawn on a temporary canvas in shifted coordinates below
    pass
# Central jet, narrowing into a sparkling crown.
rect(30,-5,3,8,blue)
rect(31,-7,1,8,light)
rect(30,-6,1,3,white)
pix(32,-8,light)
# Two outward-curving spray arms, with separated droplets.
for points in [[(30,-3),(28,-5),(26,-5),(24,-3),(23,0),(22,5),(22,9)],[(32,-3),(34,-5),(36,-4),(38,-1),(39,3),(40,9)]]:
    for (x,y),(xx,yy) in zip(points,points[1:]):
        line(x,y,xx,yy,blue)
for x,y in [(28,-5),(26,-5),(24,-3),(23,1),(22,5),(34,-5),(36,-4),(38,0),(39,4)]:
    pix(x,y,light)
rect(21,10,2,2,light)
rect(39,10,2,2,light)
pix(21,7,white)
pix(41,6,blue)
pix(26,-8,blue)
pix(37,-7,light)
# Impact rings in the upper pool.
line(21,12,25,12,light)
pix(20,11,blue)
line(37,12,41,12,light)
pix(42,11,blue)
# Water spilling over the upper two rims, in narrow irregular ribbons.
for x,y,end,slant in [(25,14,21,-1),(37,14,21,1),(19,23,29,-1),(44,23,29,1)]:
    line(x,y,x+slant,end,blue)
    line(x+1,y,x+slant+1,end-1,dark)
    line(x,y,x+slant,end-2,light)
    pix(x,y,white)
    pix(x+slant,end,white)
    line(x+slant-2,end+1,x+slant+2,end+1,blue)
    pix(x+slant-2,end,light)
# Two main waterfalls, streaming from the wide bowl into the reservoir.
for x,dx in [(17,-2),(47,2)]:
    line(x+1,32,x+dx+1,50,dark)
    line(x,32,x+dx,51,blue)
    line(x-1,32,x+dx-1,49,blue)
    line(x-1,33,x+dx-1,40,light)
    line(x,41,x+dx,46,light)
    pix(x-1,32,white)
    pix(x+dx-1,48,white)
    pix(x+dx,51,white)
    # small spread of spray at the foot and a broken oval ripple
    line(x+dx-3,52,x+dx+3,52,light)
    line(x+dx-4,53,x+dx-2,54,blue)
    line(x+dx+2,54,x+dx+5,52,blue)
    line(x+dx-1,55,x+dx+2,55,light)
    line(x+dx-2,50,x+dx-3,48,light)
    pix(x+dx+3,49,light)
    pix(x+dx+4,47,blue)
# Bright broken surface ripples, keeping the original basin texture.
line(24,57,28,57,light)
line(34,58,39,58,blue)
line(40,55,43,55,light)
line(23,28,25,28,light)
line(33,30,36,30,light)
result = flatten([result,water],name='output')
view(result,scale=6,margin=0)
finish(result)
