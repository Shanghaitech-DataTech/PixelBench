result = new_canvas(16, 16, name='glow-jellyfish')
# A compact, cool-water palette. Bell shadows retain a little transparency.
ink = '#15243e'
edge = '#243b59'
shade = '#25627cce'
blue = '#298ca2db'
aqua = '#3ac2cbdc'
light = '#77eee9ef'
shine = '#d3fff5'
rim = '#79f8ee'
violet = '#827bd5e8'

# Three short, gently curling tentacles, each with its own dark contour.
strands = [([(4,9),(4,10),(4,11),(5,12)], ['#63dfdf','#60d9df','#42a9c4','#6dcde1']),
           ([(7,9),(7,10),(7,11),(8,12),(8,13)], ['#82e8ee','#83bce7','#887bd4','#9c8ce2','#b8b7f1']),
           ([(11,9),(11,10),(11,11),(10,12)], ['#4dcbd1','#43b3c5','#4991bd','#72c3d9'])]
for points, colours in strands:
    for x,y in points:
        for dx,dy in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
            result.set(x+dx,y+dy,ink)
for points, colours in strands:
    for (x,y), colour in zip(points,colours):
        result.set(x,y,colour)

# Stepped dome silhouette.
for y, left, right in [(1,6,9),(2,4,11),(3,3,12),(4,3,12),(5,2,13),(6,2,13),(7,2,13),(8,2,13),(9,3,12)]:
    result.line(left,y,right,y,ink)
# Translucent bell, with the light concentrated along its upper-left curve.
for y,left,right,col in [(2,6,9,light),(3,4,11,aqua),(4,4,11,aqua),(5,3,12,blue),(6,3,12,blue),(7,3,12,shade),(8,3,12,aqua)]:
    result.line(left,y,right,y,col)
result.line(6,2,8,2,shine)
result.line(4,3,5,3,light)
result.line(6,3,9,3,light)
result.set(4,4,shine)
result.set(5,4,light)
result.set(3,5,light)
result.set(4,5,aqua)
result.set(3,6,aqua)
result.line(10,3,11,3,blue)
result.line(10,4,11,4,blue)
result.line(11,5,12,5,shade)
result.line(12,6,12,7,shade)
# A small bioluminescent organ, seen through the bell.
result.line(6,5,8,5,aqua)
result.set(5,6,aqua)
result.set(9,6,aqua)
result.line(6,6,8,6,violet)
result.set(7,6,'#c4b2eee8')
result.line(6,7,8,7,'#536fafe0')
# Bright scalloped lower lip; it opens onto the dangling tendrils.
result.set(3,7,light)
result.line(4,8,6,8,rim)
result.line(7,8,9,8,light)
result.line(10,8,11,8,aqua)
result.set(12,7,aqua)
for x,col in [(4,light),(7,'#99dded'),(11,aqua)]:
    result.set(x,9,col)
# A reflected blue edge keeps the outline readable while staying dark.
result.set(12,4,edge)
result.line(13,5,13,7,edge)
view(result, scale=24, margin=1)
save('glow-jellyfish', result)
finish(result)
