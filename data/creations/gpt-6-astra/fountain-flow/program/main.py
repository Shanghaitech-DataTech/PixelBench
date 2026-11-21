result = new_canvas(64,84,name='flowing_fountain')
result.blit(input_canvas,0,8)
D='#1d8baa'; B='#2ec7dc'; L='#8de7ed'; W='#dffff5'
def line(x,y,x2,y2,c): result.line(x,y+8,x2,y2+8,c)
def rect(x,y,w,h,c): result.rect(x,y+8,w,h,c)
def dot(x,y,c): result.set(x,y+8,c)
def poly(points,c): result.poly([(x,y+8) for x,y in points],c)
# Fresh water jets rise from the finial and arc out into the first bowl.
line(31,1,31,-4,B); line(32,1,32,-5,L)
line(31,-5,31,-6,W); dot(32,-6,L)
for pts in [[(31,0),(28,-4),(25,-4),(23,-2),(22,2),(22,6)],[(32,0),(35,-4),(38,-4),(40,-2),(41,2),(41,6)]]:
    for (x,y),(xx,yy) in zip(pts,pts[1:]): line(x,y,xx,yy,B)
for a in [(25,-4,27,-4),(23,-2,23,0),(36,-4,38,-4),(40,-1,40,1)]: line(*a,L)
line(29,0,27,-1,L); line(27,-1,26,1,L); line(26,1,25,4,B)
line(34,0,36,-1,L); line(36,-1,37,2,B); dot(37,4,L)
for x,y in [(20,1),(43,0),(20,4),(44,4),(28,-6),(36,-7)]: dot(x,y,L)
# Small impact ripples in the top bowl.
for x,y in [(22,8),(39,8)]:
    line(x-1,y,x+2,y,L); dot(x-2,y-1,B); dot(x+3,y-1,B)
# Water pouring over upper and middle stone lips.
for x,y,end in [(26,14,20),(36,14,20),(21,24,30),(41,24,30)]:
    rect(x,y,3,end-y+1,D)
    rect(x,y,2,end-y,B)
    line(x,y,x+1,y,L)
    line(x,y+1,x,y+3,L)
    dot(x+1,end-1,L)
    line(x-2,end+1,x+3,end+1,B)
    line(x-1,end+1,x+1,end+1,L)
    dot(x-2,end-1,L); dot(x+3,end-2,B)
# Two long side falls leave the broad lower bowl and land in the gold basin.
for x in [17,45]:
    poly([(x-1,32),(x+3,32),(x+2,36),(x+2,45),(x+3,50),(x,52),(x-1,48),(x,39)],D)
    poly([(x-1,32),(x+2,32),(x+1,37),(x+1,46),(x+2,50),(x,51),(x,43),(x-1,37)],B)
    line(x-1,32,x+1,32,W)
    line(x,33,x,38,L)
    line(x,40,x,43,L)
    line(x+1,46,x+1,49,L)
    dot(x+1,39,W)
    # Foamy rings and airborne splash pixels at each impact.
    line(x-3,52,x+4,52,B)
    line(x-2,53,x+3,53,L)
    line(x-4,51,x-3,50,B)
    line(x+4,50,x+5,51,B)
    line(x-1,50,x+1,51,W)
    dot(x-2,48,L); dot(x+4,48,L)
    dot(x+3,46,B)
# Fine reflected ripple glints between the moving streams.
for x,y,w in [(29,11,4),(29,21,3),(33,29,4),(24,55,4),(36,54,3),(12,48,2),(51,48,2)]:
    line(x,y,x+w-1,y,L)
view(result,scale=7,margin=0)
finish(result)
