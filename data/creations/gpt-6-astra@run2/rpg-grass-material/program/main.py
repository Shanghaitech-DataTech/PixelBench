result = new_canvas(16, 16, background='#527b32', name='grass')
# Wrapped marks keep the material continuous at each boundary.
def marks(points, color):
    for x,y in points:
        result.set(x%16,y%16,color)
# Interlocking low grass shadows.
marks([(0,1),(1,1),(4,0),(5,0),(8,2),(9,2),(12,0),(13,0),
       (3,3),(4,3),(6,5),(7,5),(11,4),(12,4),(15,4),(0,4),
       (1,7),(2,7),(4,8),(8,8),(9,8),(13,7),(14,7),
       (0,11),(1,11),(5,11),(6,11),(10,10),(11,10),
       (3,14),(4,14),(8,13),(9,13),(12,14),(15,14),(0,14)], '#42692d')
# Short light blades interleaved with darker grass.
marks([(1,0),(2,0),(6,1),(6,2),(10,0),(14,2),(15,2),
       (1,4),(2,4),(4,5),(5,4),(9,4),(10,3),(13,5),
       (0,8),(3,6),(6,7),(7,7),(10,7),(11,6),(15,9),
       (2,10),(3,10),(7,10),(8,10),(12,9),(13,10),
       (1,13),(5,13),(6,14),(10,12),(11,12),(14,13),
       (2,15),(7,15),(13,15)], '#6e9440')
# Sparse earthy gaps, edged with overhanging grass.
marks([(4,9),(5,9),(5,10),(12,2),(13,2),(13,3)], '#675638')
marks([(4,9),(13,2)], '#957342')
marks([(4,10),(12,3)], '#3b602b')
# Small forked tufts.
for x,y in [(2,2),(9,6),(14,11),(6,13)]:
    marks([(x-1,y-1),(x+1,y-2),(x,y),(x+1,y-1)], '#315729')
    marks([(x,y-1)], '#789b44')
# Two tiny golden wildflowers, with shaded stems.
marks([(11,14),(3,7)], '#315729')
marks([(10,13),(2,6)], '#c5a53d')
marks([(11,13),(3,5)], '#efd967')
view(result, scale=24, margin=0)
# Inspect a repeated swatch without adding it to the submission.
swatch = new_canvas(48,48, name='repeat_check')
for y in range(3):
    for x in range(3):
        swatch.blit(result,16*x,16*y)
view(swatch, scale=8, margin=0)
finish(result)
