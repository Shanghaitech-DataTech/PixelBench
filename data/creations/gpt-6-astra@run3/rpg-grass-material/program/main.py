result = new_canvas(16, 16, background='#4e813b', name='rpg_grass')
# Deliberately staggered clusters; wrapping coordinates keep the texture periodic.
def pixels(coords, col):
    for x,y in coords:
        result.set(x%16,y%16,col)
pixels([(0,0),(1,0),(6,0),(10,0),(11,0),(14,1),(3,2),(4,2),(8,2),(0,3),(6,3),(11,3),(12,3),(15,4),(3,5),(7,5),(8,5),(13,6),(0,7),(4,7),(9,7),(10,7),(15,8),(6,9),(11,9),(12,9),(2,10),(3,10),(8,11),(14,11),(0,12),(5,12),(10,13),(11,13),(3,14),(7,14),(14,14),(15,15),(5,15)], '#608f42')
pixels([(2,0),(8,0),(13,0),(4,1),(9,1),(15,2),(1,4),(5,4),(10,4),(13,4),(4,6),(10,6),(15,6),(2,8),(7,8),(12,8),(0,10),(5,10),(10,10),(15,10),(3,12),(7,12),(12,12),(1,14),(8,14),(12,15)], '#3f7036')
# Sparse exposed earth, with grass breaking up its outlines.
pixels([(4,4),(5,4),(3,5),(4,5),(5,5)], '#76633a')
pixels([(4,4),(5,5)], '#97804a')
pixels([(12,12),(13,12),(13,13)], '#76633a')
pixels([(13,12)], '#97804a')
pixels([(3,4),(6,5),(12,13)], '#365d32')
# Forked grass blades.
for x,y in [(1,5),(8,2),(6,11),(14,8),(0,14)]:
    pixels([(x,y),(x+2,y-1),(x+1,y+1),(x+2,y)], '#315d32')
    pixels([(x,y-1),(x+1,y)], '#76a34b')
# Small light-catching grass tips.
pixels([(2,1),(11,1),(5,2),(14,4),(8,6),(3,8),(10,9),(4,11),(9,12),(5,14),(11,15)], '#79a34c')
# Tiny golden blooms, each supported by a darker stem.
for x,y in [(3,10),(12,5),(10,14)]:
    pixels([(x,y+1)], '#315d32')
    pixels([(x,y)], '#ead269')
    pixels([(x+1,y)], '#c3a047')
view(result, scale=24)
finish(result)
