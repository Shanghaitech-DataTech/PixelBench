result = new_canvas(16,16,background='#4e7836',name='grass')
# Distributed short, interleaved grass blades; all marks wrap at tile edges.
def mark(x,y,pattern,col):
    for dx,dy in pattern:
        result.set((x+dx)%16,(y+dy)%16,col)
for x,y in [(0,0),(5,1),(10,0),(14,3),(3,5),(8,4),(11,7),(0,8),(5,9),(15,12),(9,12),(3,14),(12,15)]:
    mark(x,y,[(0,0),(1,1),(0,1)],'#608c3e')
for x,y in [(2,2),(7,0),(12,2),(0,5),(5,4),(9,6),(14,8),(3,10),(7,11),(11,10),(1,13),(6,15),(13,13)]:
    mark(x,y,[(0,0),(1,0),(1,1)],'#41672f')
for x,y in [(1,0),(6,2),(10,3),(3,6),(7,7),(0,10),(5,12),(10,14),(14,0),(14,10)]:
    mark(x,y,[(0,0)],'#79a34a')
# Tiny bare earth breaks sheltered by grass.
mark(5,6,[(0,0),(1,0),(0,1)],'#78633b')
mark(5,6,[(1,0)],'#9a8050')
mark(12,11,[(0,0),(1,0),(1,1)],'#78633b')
# Forked dark tufts.
for x,y in [(1,6),(8,9),(13,4),(4,13)]:
    mark(x,y,[(0,0),(2,0),(1,1)],'#31582c')
    mark(x,y,[(0,-1)],'#608c3e')
# Two tiny golden wildflowers with shadowed stems.
for x,y in [(3,3),(11,9)]:
    mark(x,y,[(0,1)],'#31582c')
    mark(x,y,[(0,0),(1,0)],'#dfbb49')
    mark(x,y,[(0,0)],'#f4dc70')
view(result,scale=24)
finish(result)
