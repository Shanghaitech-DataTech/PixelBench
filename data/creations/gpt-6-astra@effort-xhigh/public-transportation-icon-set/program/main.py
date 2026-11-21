# Four transport glyphs, designed directly on the final pixel grid.
result = new_canvas(64, 64, background='#0c1c2b', name='public_transportation')
BG = '#0c1c2b'
EDGE = '#35505e'
PANEL = '#183342'
INK = '#f4ebd3'
TEAL = '#70c7bd'
AMBER = '#f2b568'

# Matching stepped, round-corner frames.
def panel(x, y):
    for row in range(28):
        inset = max(0, 3-min(row,27-row))
        result.rect(x+inset,y+row,28-2*inset,1,EDGE)
        if 0 < row < 27:
            inside = max(1,4-min(row,27-row))
            result.rect(x+inside,y+row,28-2*inside,1,PANEL)

for py in (3,33):
    for px in (3,33):
        panel(px,py)

# BUS: wide split windscreen, mirrors, destination bar and rubber wheels.
result.rect(10,24,4,3,INK)
result.rect(20,24,4,3,INK)
result.rect(6,12,3,5,INK)
result.rect(25,12,3,5,INK)
result.poly([(11,7),(22,7),(25,10),(25,23),(23,25),(10,25),(8,23),(8,10)], INK)
result.rect(12,8,10,2,PANEL)
result.rect(14,8,6,2,AMBER)
result.rect(10,11,14,7,PANEL)
result.rect(10,11,6,5,TEAL)
result.rect(18,11,6,5,TEAL)
result.rect(10,19,14,4,PANEL)
result.rect(10,20,3,2,AMBER)
result.rect(21,20,3,2,AMBER)
result.rect(15,20,4,2,INK)

# SUBWAY: a train within an arched tunnel, ending in a pair of rails.
result.poly([(36,26),(36,13),(38,9),(42,6),(51,6),(55,9),(57,13),(57,26)],TEAL)
result.poly([(38,26),(38,14),(40,11),(43,8),(50,8),(53,11),(55,14),(55,26)],PANEL)
result.poly([(43,23),(45,24),(42,28),(39,28)],INK)
result.poly([(49,24),(51,23),(55,28),(52,28)],INK)
result.poly([(43,10),(51,10),(54,13),(54,22),(51,25),(43,25),(40,22),(40,13)],INK)
result.rect(43,11,8,2,PANEL)
result.rect(45,11,4,2,AMBER)
result.rect(42,14,10,5,TEAL)
result.rect(46,14,2,5,PANEL)
result.rect(42,21,3,2,AMBER)
result.rect(49,21,3,2,AMBER)
result.rect(46,21,2,2,PANEL)

# A square-ended two-pixel stroke keeps small diagonals clear.
def stroke(x0,y0,x1,y1,colour):
    result.line(x0,y0,x1,y1,colour)
    if abs(y1-y0) > abs(x1-x0):
        result.line(x0+1,y0,x1+1,y1,colour)
    else:
        result.line(x0,y0+1,x1,y1+1,colour)

# BICYCLE: equal wheels, two frame triangles, raised handlebars.
for wx in (10,23):
    result.circle(wx,51,5,INK)
    result.circle(wx,51,3,PANEL)
stroke(10,51,13,43,TEAL)
stroke(13,43,17,51,TEAL)
stroke(10,51,17,51,TEAL)
stroke(13,43,21,43,TEAL)
stroke(21,43,17,51,TEAL)
stroke(20,40,23,51,TEAL)
result.rect(20,38,5,2,INK)
result.rect(20,39,2,2,INK)
result.rect(12,41,2,2,INK)
result.rect(10,39,6,2,INK)
result.rect(16,50,2,2,AMBER)
result.rect(18,52,3,2,INK)

# PEDESTRIAN: a right-facing head and an open walking stride.
result.circle(48,39,3,INK)
result.rect(48,38,4,3,INK)
stroke(45,45,42,48,INK)
stroke(40,48,42,48,INK)
stroke(49,45,51,48,INK)
stroke(51,48,55,48,INK)
result.poly([(46,43),(49,44),(48,49),(46,52),(43,50)],TEAL)
stroke(45,51,42,57,INK)
result.rect(40,57,4,2,INK)
stroke(46,51,50,54,INK)
stroke(50,54,52,57,INK)
result.rect(52,57,4,2,INK)
result.rect(46,45,2,2,AMBER)

view(result, scale=8, margin=0)
save('public-transportation-icon-set', result)
finish(result)
