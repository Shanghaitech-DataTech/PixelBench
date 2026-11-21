result = new_canvas(16,16,background='#85878a',name='cracked_stone')
# Interlocking mineral patches, continued across the tile edges.
patches=[('#919396',[(0,0,4,2),(13,0,3,2),(1,2,5,2),(3,4,3,1),(9,3,4,2),(10,5,4,1),(0,9,3,3),(14,9,2,3),(2,12,4,2),(7,10,4,2),(9,12,3,2),(6,15,5,1)]),('#797c80',[(6,0,4,2),(7,2,2,2),(0,5,3,2),(14,5,2,2),(2,7,4,2),(5,9,2,2),(12,7,3,2),(13,13,3,3),(0,14,2,2),(6,13,2,2)]),('#9c9ea0',[(1,1,2,1),(3,3,2,1),(10,3,2,1),(0,10,2,1),(3,12,2,1),(8,10,2,1)]),('#6e7175',[(7,1,2,1),(1,6,2,1),(3,8,2,1),(13,8,2,1),(14,14,2,1),(6,14,2,1)])]
for color,rs in patches:
 for x,y,w,h in rs: result.rect(x,y,w,h,color)
# Main fracture wraps at both sides and branches to top and bottom.
crack=[(0,4),(1,4),(2,5),(3,5),(4,6),(5,6),(6,7),(7,7),(8,8),(9,8),(10,7),(11,6),(12,6),(13,5),(14,4),(15,4)]
branch=[(6,7),(6,8),(7,9),(7,10),(6,11),(6,12),(5,13),(5,14),(4,15),(4,0),(5,1),(5,2),(6,3),(6,4)]
for x,y in crack+branch:
 result.set((x+1)%16,(y+1)%16,'#a3a4a5')
for x,y in crack+branch:
 result.set(x,y,'#565a60')
for x,y in [(4,6),(6,7),(7,9),(11,6),(5,13)]: result.set(x,y,'#484d53')
view(result,scale=24)
finish(result)
