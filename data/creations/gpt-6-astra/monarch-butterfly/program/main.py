result = new_canvas(32, 32, name='monarch')
ink='#20202a'
edge='#37303a'
orange='#ef862b'
light='#ffb347'
red='#c95122'
cream='#fff1ce'
# Paired open wings, hand-placed on the pixel grid.
for flip in (False, True):
    def pt(x,y): return (31-x,y) if flip else (x,y)
    def poly(coords,col): result.poly([pt(x,y) for x,y in coords],col)
    def line(x,y,a,b,col): result.line(*pt(x,y),*pt(a,b),col)
    def dot(x,y,col): result.set(*pt(x,y),col)
    # Broad forewing and rounded, scalloped hindwing.
    poly([(14,14),(11,9),(6,4),(2,3),(1,5),(1,11),(3,16),(7,20),(13,21),(15,18)],ink)
    poly([(14,17),(8,17),(3,20),(3,24),(5,27),(8,29),(11,28),(14,25),(15,20)],ink)
    # Forewing interior split by continuous black veins.
    poly([(3,6),(5,6),(9,10),(12,14),(6,11),(3,9)],light)
    poly([(3,11),(6,12),(12,15),(6,15),(4,14)],orange)
    poly([(5,16),(11,16),(13,17),(10,18),(7,18)],orange)
    poly([(7,8),(10,10),(13,14),(12,13)],orange)
    line(4,7,6,8,'#ffd06a')
    line(4,12,5,13,'#ffac3d')
    dot(11,14,red)
    # Hindwing panels radiate from the body.
    poly([(12,19),(9,19),(5,21),(5,23),(7,23)],orange)
    poly([(13,20),(9,23),(8,26),(10,27),(12,25)],light)
    poly([(7,24),(6,24),(6,25),(7,27)],orange)
    poly([(13,22),(13,25),(11,27)],red)
    line(6,21,8,20,'#ffae42')
    dot(9,25,orange)
    # Ivory marginal dots in the black wing borders.
    for x,y in [(2,5),(4,4),(2,8),(2,11),(3,14),(5,17),(7,19),(4,21),(4,24),(6,27),(9,28),(12,26)]:
        dot(x,y,cream)
    dot(9,7,'#ffddb1')
# Narrow thorax and tapered abdomen.
result.rect(15,12,2,10,ink)
result.rect(15,22,2,3,edge)
result.set(15,25,ink)
result.set(15,13,'#756252')
result.set(15,17,'#b88b55')
result.set(15,20,'#79634f')
result.rect(15,10,2,2,ink)
# Antennae with a subtle outward curl.
result.line(15,10,13,7,ink)
result.line(16,10,18,7,ink)
result.set(12,7,edge)
result.set(19,7,edge)
view(result)
finish(result)
