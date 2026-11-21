# 16 x 16 hand-pixelled, periodically wrapped cracked stone.
result = new_canvas(16, 16, background='#80847f', name='cracked_stone')
P = ['#4b4e50', '#606467', '#74787b', '#85898b', '#979b9c', '#a9adae']
# Broad mineral patches keep the tile legible at game scale.
stone = [
'3333443332222333',
'3334443332223333',
'2344433322233344',
'2344333332334444',
'2333323333344443',
'3333222333344333',
'4332222333333334',
'4432223332233344',
'4433333442223344',
'3333334443222333',
'3223344443333333',
'2223344433333222',
'2233333334433222',
'2333333344443332',
'3332233344433333',
'3332233333332333',
]
for y,row in enumerate(stone):
    for x,v in enumerate(row):
        result.set(x,y,P[int(v)])
# Fissures are explicitly periodic across all four edges.
main = [(8,0),(8,1),(8,2),(9,3),(10,4),(10,5),(10,6),(9,7),(9,8),(9,9),(8,10),(7,11),(7,12),(7,13),(8,14),(8,15)]
branch = [(11,6),(12,6),(13,6),(14,7),(15,8),(0,8),(1,8),(2,9),(3,9),(4,10)]
twig = [(7,2),(6,3),(5,3),(4,3),(3,4)]
cracks = main + branch + twig
# A recessed lip and an intermittent upper-left bevel.
for x,y in cracks:
    result.set((x+1)%16,y,P[2])
for x,y in [(8,0),(8,1),(9,3),(10,4),(10,5),(9,8),(9,9),(7,11),(7,12),(7,13),(8,15)]:
    result.set((x-1)%16,y,P[4])
for x,y in [(11,6),(12,6),(13,6),(15,8),(0,8),(1,8),(3,9),(5,3)]:
    result.set(x,(y-1)%16,P[4])
for i,(x,y) in enumerate(cracks):
    result.set(x,y,P[0 if i < len(main) or i in [18,19,23,27,28] else 1])
# Small, quiet mineral faces, never isolated high-contrast noise.
for x,y in [(2,2),(3,2),(12,3),(13,3),(3,7),(3,8),(11,13),(12,13),(0,15)]:
    result.set(x,y,P[4])
for x,y in [(2,1),(3,1),(12,2),(13,2),(11,12),(12,12)]:
    result.set(x,y,P[4])
view(result, scale=24, margin=0)
# The repeat is for inspection only, not an output.
repeat = new_canvas(48,48,name='seam_check')
for y in range(3):
    for x in range(3):
        repeat.blit(result,16*x,16*y)
view(repeat, scale=8, margin=0)
save('cracked_stone',result)
finish(result)
