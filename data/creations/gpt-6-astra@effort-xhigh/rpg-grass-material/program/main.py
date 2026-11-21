# A repeatable, hand-placed 16px meadow texture.
result = new_canvas(16, 16, background='#4e8439', name='rpg_grass')
P = {
    'base': '#4e8439',
    'shade': '#417333',
    'deep': '#305a2e',
    'light': '#689943',
    'tip': '#82ac4e',
    'soil': '#7f6139',
    'earth': '#a08049',
    'gold': '#dbb843',
    'petal': '#f4db72',
}
def dot(x, y, color):
    result.set(x % 16, y % 16, P[color])
def stamp(x, y, pixels, color):
    for dx, dy in pixels:
        dot(x + dx, y + dy, color)

# Broken, interleaved clusters, including motifs crossing the repeat boundary.
for x,y,shape in [
    (1,0,[(0,0),(1,0),(1,1)]),
    (7,0,[(0,0),(1,0),(0,1)]),
    (12,2,[(0,0),(1,0),(1,1)]),
    (5,3,[(0,0),(0,1),(1,1)]),
    (15,4,[(0,0),(1,0),(1,1)]),
    (8,6,[(0,0),(1,0),(1,1)]),
    (2,7,[(0,0),(1,0),(0,1)]),
    (13,9,[(0,0),(1,0),(1,1)]),
    (7,10,[(0,0),(1,0),(0,1)]),
    (2,12,[(0,0),(1,0),(1,1)]),
    (11,14,[(0,0),(1,0),(1,1)]),
    (5,15,[(0,0),(1,0),(1,1)]),
]:
    stamp(x,y,shape,'shade')

# Short light strokes give the blades a consistent, gentle upper-left light.
for x,y,shape in [
    (4,1,[(0,0),(1,0)]), (10,0,[(0,0),(0,1)]),
    (14,1,[(0,0),(1,0)]), (1,3,[(0,0),(1,0),(1,1)]),
    (8,3,[(0,0),(1,0)]), (12,4,[(0,0),(1,0)]),
    (6,6,[(0,0),(0,1)]), (0,6,[(0,0)]),
    (10,7,[(0,0),(1,0),(1,1)]), (4,8,[(0,0),(1,0)]),
    (15,8,[(0,0),(1,0)]), (8,9,[(0,0)]),
    (1,10,[(0,0),(0,1)]), (10,11,[(0,0),(1,0)]),
    (5,12,[(0,0),(1,0)]), (15,12,[(0,0),(1,0)]),
    (8,14,[(0,0),(1,0)]), (2,15,[(0,0),(1,0)]),
    (14,15,[(0,0)]),
]:
    stamp(x,y,shape,'light')
for x,y in [(4,1),(1,3),(12,4),(10,7),(5,12),(8,14),(15,12)]:
    dot(x,y,'tip')

# Tiny earth windows, partly interrupted by grass.
stamp(2,9,[(0,0),(1,0),(0,1),(1,1),(2,1)],'soil')
stamp(2,9,[(0,0),(1,0)],'earth')
dot(4,10,'shade')
stamp(13,0,[(0,0),(1,0),(0,-1)],'soil')
dot(13,0,'earth')

# Three small, forked tufts with recessed dark roots.
for x,y in [(0,13),(7,8),(13,5)]:
    stamp(x,y,[(0,0),(2,0),(1,1)],'deep')
    dot(x+1,y+2,'shade')
    dot(x,y-1,'light')

# Two tiny buttercups; warm light pixels above unobtrusive green stems.
for x,y in [(3,5),(11,12)]:
    dot(x,y+1,'deep')
    dot(x+1,y+2,'shade')
    dot(x,y,'petal')
    dot(x+1,y,'gold')
    dot(x,y-1,'gold')

view(result, scale=24, margin=0)
# Inspect the wrap in both axes without adding a submitted canvas.
repeat = new_canvas(48,48, name='repeat_preview')
for ty in range(3):
    for tx in range(3):
        repeat.blit(result,16*tx,16*ty)
view(repeat, scale=8, margin=0)
save('rpg-grass-material', result)
finish(result)
