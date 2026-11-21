result = new_canvas(16, 16, background='#4f7937', name='grass')
# Irregular, wrapping clusters keep the texture continuous at every edge.
def pixels(coords, color):
    for x,y in coords:
        result.set(x % 16, y % 16, color)
pixels([(0,0),(1,0),(8,0),(9,0),(14,1),(4,1),(5,2),(10,2),(11,2),(0,3),(1,4),(7,4),(8,4),(13,4),(3,5),(4,5),(10,6),(11,6),(15,6),(0,7),(6,7),(7,8),(13,8),(14,9),(2,9),(3,10),(9,10),(10,11),(0,12),(1,12),(5,12),(6,13),(12,13),(13,14),(3,14),(8,15),(9,15),(15,15)], '#618b3c')
pixels([(2,0),(6,0),(11,0),(15,2),(3,3),(6,3),(12,3),(9,5),(14,5),(2,7),(5,8),(10,8),(15,10),(6,10),(8,12),(11,14),(0,15),(4,15)], '#426b31')
# Short forked grass blades; shaded feet and lighter tips.
for x,y in [(2,4),(11,5),(6,12),(14,15)]:
    pixels([(x-1,y-1),(x,y),(x+1,y-2),(x+1,y-1),(x,y+1)], '#355a2b')
    pixels([(x-1,y-2),(x+2,y-1)], '#729544')
# Two small exposed earth pockets, tucked beneath the turf.
pixels([(7,2),(8,2),(7,3),(8,3),(9,3)], '#6d6038')
pixels([(7,2),(8,3)], '#93804b')
pixels([(2,12),(3,12),(2,13)], '#6d6038')
pixels([(2,12)], '#93804b')
# Sparse light-catching blades.
pixels([(0,1),(5,3),(14,3),(7,6),(15,7),(3,8),(10,10),(1,11),(8,14),(4,0)], '#7d9f49')
# Tiny yellow wildflowers, each anchored by a green stem.
pixels([(4,7),(12,12)], '#355a2b')
pixels([(4,6),(12,11)], '#d4b744')
pixels([(5,6),(12,10)], '#f1d66b')
view(result, scale=24, margin=0)
# A repeat preview makes edge continuity easy to inspect.
repeat = new_canvas(48,48, name='repeat_preview')
for y in range(3):
    for x in range(3):
        repeat.blit(result,x*16,y*16)
view(repeat, scale=8, margin=0)
finish(result)
