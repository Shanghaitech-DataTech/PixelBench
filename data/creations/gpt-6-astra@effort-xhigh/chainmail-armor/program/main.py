# A compact, cool-steel mail hauberk. All edges are on the native pixel grid.
result = new_canvas(32, 32, name="chainmail_armor")
ink = '#161c2a'
deep = '#2b3648'
shade = '#44556a'
steel = '#697f90'
light = '#9eb1bb'
high = '#cbd8d9'
glint = '#edf1e5'

silhouette = [(10,3),(12,3),(12,5),(14,7),(17,7),(19,5),(19,3),(21,3),(22,4),(25,5),(27,8),(29,12),(29,15),(26,17),(24,16),(24,27),(23,29),(17,29),(16,28),(15,29),(8,29),(7,27),(7,16),(5,17),(2,15),(2,12),(4,8),(6,5),(9,4)]
result.poly(silhouette, ink)
result.poly(silhouette, ink, fill=False)
# The separate field provides an exact stencil for the small interwoven links.
field = new_canvas(32, 32, name='metal_stencil')
inside = [(10,4),(11,4),(11,6),(14,9),(17,9),(20,6),(20,4),(21,4),(22,5),(24,6),(26,9),(28,13),(28,14),(26,16),(23,14),(23,27),(22,28),(17,28),(16,27),(15,28),(9,28),(8,26),(8,14),(5,16),(3,14),(3,13),(5,9),(7,6)]
field.poly(inside, steel)
field.poly(inside, steel, fill=False)
mask_pixels = {(x,y) for y in range(32) for x in range(32) if field.get(x,y) != field.get(0,0)}

def tone(x,y):
    # Light comes from above and to the left; the lower right turns away.
    if x >= 22 or y >= 25: return 0
    if x >= 17 or y >= 21: return 1
    return 2

ramps = [ (deep,shade,steel,light), (shade,steel,light,high), (steel,light,high,glint) ]
for x,y in mask_pixels:
    result.set(x,y, (deep,shade,shade)[tone(x,y)])

# Offset oval links pass through the next row: one-pixel open centres remain legible.
for row,y in enumerate(range(5,28,3)):
    for x in range(-2+(row%2)*2,31,4):
        ring = [(1,0,2),(0,1,2),(1,1,-1),(2,1,1),(0,2,1),(1,2,-1),(2,2,0),(1,3,1)]
        for dx,dy,v in ring:
            px,py=x+dx,y+dy
            if (px,py) in mask_pixels:
                r=ramps[tone(px,py)]
                result.set(px,py,deep if v == -1 else r[v])

# Shoulder seams and dark underarms describe the garment's construction.
result.line(8,11,8,14, shade)
result.line(23,11,23,15, deep)
result.set(7,15,ink)
result.set(24,15,ink)
# Small rolled metal cuffs, with glancing light along the outer rims.
result.line(3,14,5,16, deep)
result.line(4,14,6,15,light)
result.set(3,13,high)
result.line(26,16,28,14,deep)
result.line(25,14,27,13,steel)
result.set(28,13,light)
# The open collar has a bright outer rim and a shadowed inner edge.
result.path('M 10 4 L 10 6 L 13 9 L 18 9 L 21 6 L 21 4', shade, fill=False)
result.path('M 11 4 L 11 6 L 14 8 L 17 8 L 20 6 L 20 4', light, fill=False)
result.line(11,4,11,5,high)
result.line(12,7,14,8,high)
result.line(15,8,17,8,steel)
result.set(20,4,high)
# The subtly split hem carries a final line of dangling rings.
result.line(9,28,14,28,shade)
result.line(17,28,22,28,deep)
result.set(9,27,light)
result.set(13,27,light)
result.set(18,27,steel)
result.set(22,27,steel)
view(result, scale=12, margin=0)
save('chainmail_armor', result)
finish(result)
