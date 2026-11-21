result = new_canvas(32, 32, name="monarch")
ink = '#211c29'
edge = '#39303a'
orange = '#ef8427'
light = '#ffb34b'
red = '#cc4e20'
cream = '#fff0ce'
# Draw each wing as mirrored pixel clusters.
def poly(points, color):
    result.poly(points,color)
    result.poly([(31-x,y) for x,y in points],color)
def line(x,y,a,b,color):
    result.line(x,y,a,b,color)
    result.line(31-x,y,31-a,b,color)
def dot(x,y,color):
    result.set(x,y,color); result.set(31-x,y,color)
# Tall forewings, broad scalloped hindwings.
poly([(14,15),(11,9),(6,4),(3,3),(1,5),(1,10),(3,16),(6,20),(13,22),(15,19)],ink)
poly([(13,16),(6,17),(3,20),(3,24),(5,27),(8,29),(11,28),(14,24),(15,20)],ink)
# Hindwing orange membrane, subdivided into tapering cells.
poly([(13,19),(7,19),(5,21),(5,24),(8,27),(11,26),(13,23)],orange)
poly([(12,19),(7,20),(5,22),(6,24),(9,24)],light)
poly([(13,20),(10,24),(9,27),(11,26),(13,23)],red)
line(13,19,5,22,ink)
line(13,19,7,26,ink)
line(13,20,11,26,ink)
# Forewing cells: black structural veins separate the orange panes.
poly([(3,6),(5,6),(9,10),(12,15),(13,18),(8,14),(5,10)],orange)
poly([(3,7),(4,8),(5,11),(3,11)],light)
poly([(4,12),(6,12),(10,16),(6,16)],orange)
poly([(7,17),(11,18),(13,20),(9,19)],red)
poly([(6,7),(9,10),(11,13),(8,11)],light)
line(5,7,7,12,ink)
line(3,11,6,11,ink)
line(7,12,13,18,ink)
line(6,16,11,17,ink)
# Warm highlights along the wing cells.
dot(4,7,light); dot(5,9,light); dot(5,13,light); dot(6,14,light)
dot(8,21,light); dot(6,23,light)
# Monarch's characteristic pale spots inside the dark margins.
for x,y in [(3,4),(2,6),(2,9),(3,13),(4,16),(6,18),(4,21),(4,24),(6,26),(8,28),(11,27),(13,24)]:
    dot(x,y,cream)
dot(3,5,edge); dot(7,27,'#d2bda6')
# Antennae and slim segmented body.
line(15,10,13,6,ink)
line(13,6,12,6,ink)
result.rect(15,10,2,4,ink)
result.rect(14,14,4,6,ink)
result.rect(15,20,2,6,ink)
result.set(15,26,ink)
result.set(15,11,'#b9a595')
result.line(15,14,15,18,'#766054')
result.set(15,20,'#b58a58')
result.set(15,22,'#80654c')
result.set(15,24,'#80654c')
view(result, scale=12)
finish(result)
