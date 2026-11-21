output = input_canvas.copy(name='output')
surface = '#8540ad'
body = '#b577d5'
shade = '#9b58bf'
light = '#e9bfff'
deep = '#512466'
# Preserve the glass, stopper and original stepped silhouette.
for y in range(64):
    for x in range(64):
        original = input_canvas.get(x,y)
        if original == 5:
            output.set(x,y,surface)
        elif original in (6,7,8,10):
            output.set(x,y,shade if x >= 38 and y >= 44 else body)
        elif original == 9:
            output.set(x,y,deep)
# All new details follow the original two-pixel grid.
def block(x,y,w,h,col):
    output.rect(x*2,y*2,w*2,h*2,col)
def bubble(x,y,size,inside):
    # Stepped ring, with the light gathering at its upper left.
    block(x+1,y,size-2,1,light)
    block(x,y+1,1,size-2,light)
    block(x+size-1,y+1,1,size-2,shade)
    block(x+1,y+size-1,size-2,1,shade)
    block(x+1,y+1,size-2,size-2,inside)
    if size>=4:
        block(x+1,y+1,1,1,'#fff1ff')
# Bubbles rising through and above the liquid.
bubble(9,15,5,surface)
bubble(17,14,4,surface)
bubble(15,9,4,'#ffffff')
bubble(21,11,3,'#ffffff')
bubble(12,7,3,'#ffffff')
# Submerged bubbles and a little reflected light on the flask.
bubble(8,23,3,body)
bubble(15,25,4,body)
block(5,22,1,3,light)
block(6,25,1,1,light)
# A small magical glint suspended in the neck.
block(21,7,1,3,shade)
block(20,8,3,1,shade)
block(21,8,1,1,light)
view(output, scale=8)
finish(output)
