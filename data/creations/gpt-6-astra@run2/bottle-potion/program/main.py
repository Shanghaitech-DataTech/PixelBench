output = input_canvas.copy(name='output')
# Preserve the original bottle and its two-pixel grid.
purple = '#ad63d5'
surface = '#713798'
light = '#e4a8f1'
shine = '#fff0ff'
edge = '#49205f'
for y in range(64):
    for x in range(64):
        p = input_canvas.get(x,y)
        if p == 5:
            output.set(x,y,surface)
        elif p in (6,7,8,10):
            output.set(x,y,purple)
        elif p == 9:
            output.set(x,y,edge)
# Each character is one 2-by-2 pixel cluster, matching the source artwork.
def stamp(x,y,rows,colors):
    for j,row in enumerate(rows):
        for i,v in enumerate(row):
            if v in colors:
                output.rect(x+2*i,y+2*j,2,2,colors[v])
# Bubbles rise through the potion and into the empty part of the bottle.
bubble = ['.ooo.','ohhio','oh bio','oiiio','.ooo.']
# Rounded square pixel bubbles with luminous upper-left rims.
def big_bubble(x,y,inside):
    stamp(x,y,['.ooo.','ohhio','ohbio','oiiio','.ooo.'],{'o':edge,'h':shine,'i':light,'b':inside})
big_bubble(18,28,surface)
big_bubble(34,20,'#d68be8')
big_bubble(30,46,purple)
stamp(20,16,['.oo.','ohio','oibo','.oo.'],{'o':surface,'h':shine,'i':light,'b':'#d68be8'})
stamp(38,32,['.oo.','ohio','oibo','.oo.'],{'o':edge,'h':shine,'i':light,'b':surface})
stamp(12,44,['.o.','oho','.o.'],{'o':light,'h':shine})
stamp(24,54,['.o.','oho','.o.'],{'o':light,'h':shine})
output.rect(30,32,2,2,light)
output.rect(26,46,2,2,shine)
output.rect(44,42,2,2,light)
# A pair of little magical glints in the clear glass.
stamp(44,14,['.s.','sss','.s.'],{'s':'#bb72d7'})
# Reflected light on the liquid and glass follows the curved left side.
output.rect(8,40,2,6,light)
output.rect(10,46,2,4,light)
output.rect(12,50,2,2,light)
view(output)
finish(output)
