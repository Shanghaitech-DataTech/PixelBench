result = new_canvas(16, 16, background='#85878a', name='cracked_stone')
# Interlocking, low-contrast mineral patches wrap around the tile boundaries.
patches = [
('#909295',[(0,0),(4,0),(4,1),(3,1),(3,3),(0,3)]),
('#787b80',[(5,0),(9,0),(9,2),(8,2),(8,3),(5,3)]),
('#96989a',[(11,0),(15,0),(15,3),(13,3),(13,2),(11,2)]),
('#777a7e',[(0,5),(3,5),(3,7),(5,7),(5,9),(2,9),(2,8),(0,8)]),
('#919396',[(5,4),(8,4),(8,5),(10,5),(10,7),(7,7),(7,6),(5,6)]),
('#7b7e82',[(12,4),(15,4),(15,7),(13,7),(13,6),(12,6)]),
('#96989a',[(0,10),(3,10),(3,12),(2,12),(2,14),(0,14)]),
('#777a7e',[(5,10),(8,10),(8,12),(7,12),(7,14),(4,14),(4,12),(5,12)]),
('#919396',[(10,9),(13,9),(13,11),(15,11),(15,13),(11,13),(11,12),(9,12),(9,10)]),
('#787b80',[(9,14),(13,14),(13,16),(9,16)]),
('#909295',[(0,15),(4,15),(4,16),(0,16)]),
]
for color, points in patches:
    result.poly(points,color)
# Small squared mineral facets, rather than independent noise pixels.
result.rect(3,3,2,1,'#a0a2a4')
result.rect(8,8,2,1,'#777a7e')
result.rect(14,8,2,1,'#919396')
result.rect(7,15,2,1,'#96989a')
result.rect(2,11,2,1,'#919396')
# Continuous fracture: steps are deliberate and edge coordinates are periodic.
crack=[(0,4),(1,4),(2,4),(3,5),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9),(9,9),(10,8),(11,8),(12,7),(12,6),(13,5),(14,5),(15,4)]
branch=[(7,8),(7,7),(8,6),(8,5),(9,4),(9,3),(10,2)]
branch2=[(9,9),(9,10),(8,11),(8,12),(9,13)]
# Subtle light catches on the lower lip of each break.
for pts in [crack,branch,branch2]:
    for x,y in pts:
        result.set(x,(y+1)%16,'#a0a2a4')
for pts in [crack,branch,branch2]:
    for x,y in pts:
        result.set(x,y,'#585c62')
for x,y in [(5,6),(5,7),(7,8),(8,9),(9,9),(12,6),(12,7)]:
    result.set(x,y,'#484d53')
view(result,scale=24,margin=0)
# A repeat preview verifies the horizontal and vertical joins.
repeat = new_canvas(48,48,name='repeat_preview')
for y in range(3):
    for x in range(3):
        repeat.blit(result,x*16,y*16)
view(repeat,scale=8,margin=0)
finish(result)
