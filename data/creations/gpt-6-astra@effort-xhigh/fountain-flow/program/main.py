# Keep the original fountain intact beneath the running water.
result = new_canvas(64, 88, name='output')
result.blit(input_canvas, 0, 12)
Y = 12
shadow = '#246b89'
blue = '#1d8baa'
cyan = '#2ec7dc'
light = '#83e8ef'
foam = '#e0ffff'

def dot(x,y,col):
    result.set(x,y+Y,col)
def line(x1,y1,x2,y2,col):
    result.line(x1,y1+Y,x2,y2+Y,col)
def poly(points,col):
    result.poly([(x,y+Y) for x,y in points],col)
def path(d,col):
    # Coordinates are supplied in original-image space.
    import re
    tokens = re.findall(r'[MLQZ]|-?\d+',d)
    out=[]
    parity=0
    for t in tokens:
        if t in ('M','L','Q','Z'):
            out.append(t)
            parity=0
        else:
            out.append(str(int(t)+(Y if parity%2 else 0)))
            parity += 1
    result.path(' '.join(out),col,fill=False)

# Small ripples and reflected light sit on the existing water surfaces.
for x,y,w,col in [
    (23,10,5,light),(25,11,3,cyan),(36,10,5,light),
    (23,20,5,light),(26,21,3,cyan),(37,20,5,light),
    (16,29,6,light),(19,30,4,cyan),(41,29,6,light),
    (24,29,3,cyan),(34,31,4,light),
    (12,49,6,light),(15,51,5,light),(10,50,3,cyan),
    (45,49,7,light),(44,51,5,light),(49,50,4,cyan),
    (22,54,5,light),(36,55,6,light),(28,56,3,cyan)]:
    line(x,y,x+w-1,y,col)

# Top jet: a bright central pulse with two falling arcs.
path('M 32 0 L 32 -5 L 31 -8',shadow)
path('M 31 0 L 31 -6 L 30 -8',cyan)
line(31,-5,31,-1,light)
dot(30,-7,foam)
dot(31,-8,light)
# The arcs have broken highlights, with cyan defining the falling edges.
path('M 31 -3 Q 27 -8 24 -4 Q 21 -1 22 5 L 23 8',cyan)
path('M 30 -4 Q 27 -7 25 -4 Q 22 -1 23 4',light)
line(23,5,24,8,foam)
dot(25,-4,foam)
dot(24,-3,foam)
path('M 32 -3 Q 36 -7 39 -3 Q 42 1 40 8',cyan)
path('M 33 -4 Q 36 -6 38 -3 Q 40 0 40 3',light)
line(40,5,40,7,foam)
# A few individual spray drops preserve the open space above the sprite.
for x,y,col in [(28,-9,light),(35,-8,cyan),(36,-7,foam),(21,-3,cyan),(20,0,light),(43,1,cyan),(43,2,light),(27,3,light),(36,4,light)]:
    dot(x,y,col)
# Landing splashes in the top bowl.
for x,y,col in [(22,8,light),(24,9,foam),(25,8,light),(26,9,foam),(38,8,light),(39,9,foam),(41,8,light)]:
    dot(x,y,col)

# Short, curving overflows from the small bowl to the middle bowl.
poly([(24,12),(27,13),(27,16),(25,20),(23,20),(24,16)],blue)
path('M 25 12 L 25 15 L 24 18 L 24 19',light)
path('M 26 14 L 26 17 L 25 19',cyan)
line(25,13,25,15,foam)
dot(24,18,foam)
poly([(37,13),(39,12),(40,16),(41,20),(38,20),(38,16)],blue)
path('M 38 13 L 39 16 L 39 19',light)
path('M 39 14 L 40 17 L 40 19',cyan)
dot(38,14,foam)
dot(39,18,foam)
for x,y,col in [(22,18,light),(23,19,foam),(25,20,foam),(27,19,light),(38,20,foam),(41,19,foam),(42,18,light)]:
    dot(x,y,col)

# Middle tier overflows, following the bowl's curved front rim.
poly([(19,22),(22,23),(22,26),(21,29),(19,30),(18,28),(19,25)],blue)
path('M 20 22 L 20 25 L 19 27 L 20 29',light)
path('M 21 24 L 21 27 L 20 28',cyan)
line(20,23,20,25,foam)
dot(19,27,foam)
poly([(42,23),(44,22),(45,25),(45,29),(43,30),(42,28)],blue)
path('M 43 23 L 43 25 L 44 27 L 44 29',light)
path('M 44 24 L 44 25 L 45 27',cyan)
dot(43,24,foam)
dot(44,28,foam)
for x,y,col in [(17,27,cyan),(18,28,foam),(20,29,foam),(22,28,light),(42,28,light),(44,29,foam),(46,28,foam),(47,26,cyan)]:
    dot(x,y,col)

# Two longer ribbons fall from the large bowl into the lower reservoir.
poly([(15,30),(18,31),(18,35),(17,39),(18,43),(18,47),(16,50),(13,49),(14,45),(14,40),(15,35)],shadow)
poly([(15,31),(17,31),(17,37),(16,40),(17,44),(17,48),(15,49),(14,48),(15,43)],cyan)
path('M 15 31 L 16 33 L 16 37 L 15 40 L 15 43',light)
line(16,32,16,35,foam)
line(15,39,15,41,foam)
path('M 16 44 L 15 47 L 15 48',light)
dot(15,46,foam)
dot(17,42,light)
poly([(46,31),(48,30),(49,35),(49,40),(48,43),(49,47),(50,49),(47,50),(45,48),(46,43),(46,37)],shadow)
poly([(46,32),(48,31),(48,37),(47,40),(47,44),(48,47),(49,49),(46,49),(46,45)],cyan)
path('M 46 32 L 47 34 L 47 37 L 46 41 L 46 43',light)
line(47,33,47,35,foam)
line(46,40,46,42,foam)
path('M 47 45 L 47 47 L 48 48',light)
dot(47,46,foam)
# Splash crowns and droplets at the feet of the falling ribbons.
for pts,col in [
    ([(12,46),(14,48),(17,48),(19,46)],light),
    ([(13,49),(15,50),(18,49)],foam),
    ([(44,47),(46,49),(49,49),(51,47)],light),
    ([(46,50),(49,50)],foam)]:
    for p,q in zip(pts,pts[1:]): line(*p,*q,col)
for x,y,col in [(11,44,cyan),(12,45,foam),(19,44,light),(20,47,foam),(13,47,foam),(18,47,foam),(43,45,light),(44,46,foam),(51,45,cyan),(52,46,light),(49,48,foam),(17,52,cyan),(47,53,cyan)]:
    dot(x,y,col)

# A glint in the lower basin's existing front outlet.
line(31,57,32,57,light)
line(31,58,31,59,light)
dot(31,60,cyan)

save('fountain-flow', result)
view(result, scale=6)
finish(result)
