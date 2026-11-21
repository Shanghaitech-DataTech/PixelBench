result = new_canvas(16,16,background='#51813b',name='grass')
# Wrapped clusters keep the texture continuous across tile boundaries.
def dots(coords,col):
    for x,y in coords: result.set(x%16,y%16,col)
dots([(0,0),(1,0),(7,0),(11,1),(14,1),(4,2),(5,2),(8,3),(12,3),(0,4),(3,5),(6,5),(10,5),(14,6),(1,7),(5,8),(8,8),(11,9),(15,9),(3,10),(7,11),(13,11),(0,12),(5,13),(9,13),(12,14),(15,15),(3,15)],'#679644')
dots([(2,1),(6,1),(10,2),(15,3),(2,4),(7,4),(11,6),(4,7),(9,7),(13,8),(0,10),(6,10),(10,11),(15,12),(2,13),(7,14),(10,15)],'#436f34')
# Sparse, irregular soil pockets.
dots([(5,3),(6,3),(5,4),(12,12),(13,12),(13,13)],'#685c35')
dots([(6,4),(12,13)],'#8b7445')
# Small forked tufts, shaded at the roots.
for x,y in [(1,6),(8,1),(10,10),(4,14),(15,14)]:
    dots([(x,y),(x-1,y-1),(x+1,y-2)],'#345d30')
    dots([(x,y-1)],'#79a34b')
# Two tiny warm yellow flowers with unobtrusive stems.
for x,y in [(12,4),(3,11)]:
    dots([(x,y+1)],'#345d30')
    dots([(x,y)],'#f2d56a')
    dots([(x+1,y)],'#c8ab43')
view(result)
finish(result)
