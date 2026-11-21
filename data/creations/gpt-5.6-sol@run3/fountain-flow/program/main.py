result = new_canvas(64, 84, name='running_fountain')
result.blit(input_canvas, 0, 8)
dark='#197c9e'
blue='#29b9d5'
light='#79e2ec'
shine='#d6ffff'
white='#ffffff'
def line(x,y,xx,yy,col):
    result.line(x,y+8,xx,yy+8,col)
def pixel(x,y,col):
    result.set(x,y+8,col)
def rect(x,y,w,h,col):
    result.rect(x,y+8,w,h,col)
# A rising central jet, with short curved sprays returning to the top bowl.
for pts,col in [([(31,4),(30,0),(30,-4),(31,-6),(33,-6),(34,-4),(34,-1),(33,2)],blue), ([(31,3),(31,-3),(32,-5),(33,-3),(32,1)],shine), ([(30,-2),(27,-4),(25,-3),(24,0),(24,4),(25,7)],light), ([(34,-2),(37,-4),(39,-2),(40,1),(40,5),(39,8)],blue)]:
    for (x,y),(xx,yy) in zip(pts,pts[1:]): line(x,y,xx,yy,col)
line(31,0,31,7,light)
line(32,0,32,6,shine)
line(26,-3,25,-1,shine)
line(38,-2,39,1,shine)
pixel(22,-2,light)
pixel(41,0,light)
pixel(36,-6,light)
# Each cascade has a dark wet edge, a cyan body and broken white highlights.
def fall(x,y,length,drift=0):
    for j in range(length):
        xx=x+round(drift*j/max(1,length-1))
        rect(xx-1,y+j,4,1,dark)
        rect(xx,y+j,2,1,blue)
        pixel(xx,y+j,light)
        if j%6 not in (3,4): pixel(xx+1,y+j,shine)
    xx=x+drift
    line(xx-2,y+length,xx+3,y+length,light)
    line(xx-1,y+length-1,xx+2,y+length-1,shine)
    pixel(xx-3,y+length-2,light)
    pixel(xx+4,y+length-2,light)
    pixel(xx-2,y+length-3,shine)
    pixel(xx+3,y+length-4,light)
fall(25,12,8,-1)
fall(39,12,8,1)
fall(20,22,8,-1)
fall(44,22,8,1)
fall(17,32,18,-1)
fall(46,32,18,1)
# Foamy lips and small reflected ripples reinforce the movement.
for x,y,w in [(24,11,4),(38,11,4),(19,21,4),(43,21,4),(16,31,4),(45,31,4)]:
    line(x,y,x+w-1,y,light)
    line(x+1,y,x+2,y,shine)
for x,y,w in [(28,9,3),(34,10,3),(28,20,5),(33,19,3),(24,29,4),(34,30,5),(13,52,7),(44,52,7),(19,55,5),(37,56,5),(28,54,5)]:
    line(x,y,x+w-1,y,light)
    pixel(x+1,y,shine)
# Tiny detached splash droplets beside the long falls.
for x,y in [(14,37),(20,42),(13,46),(50,39),(44,44),(50,47)]:
    pixel(x,y,light)
    if y%2: pixel(x,y-1,shine)
view(result, scale=7, margin=0)
finish(result)
