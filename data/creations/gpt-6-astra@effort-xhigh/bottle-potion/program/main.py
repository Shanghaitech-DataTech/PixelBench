output = input_canvas.copy(name='output')
# Preserve the source silhouette and work on its existing two-pixel grid.
P = {
    'surface':'#7137a5', 'body':'#a26bce', 'shade':'#8750b5',
    'deep':'#683b97', 'rim':'#42204e', 'light':'#c78deb',
    'foam':'#eed0fa', 'white':'#fff0ff', 'bubble':'#a95ed4',
    'outline':'#552477', 'pink':'#d99cf2'
}
for y in range(64):
    for x in range(64):
        old = input_canvas.get(x,y)
        if old == 5:
            output.set(x,y,P['surface'])
        elif old in (6,7,8,10):
            qx,qy=x//2,y//2
            col=P['body']
            if qy >= 28 or (qx >= 23 and qy >= 22): col=P['shade']
            if qy >= 30 or (qx >= 24 and qy >= 24): col=P['deep']
            output.set(x,y,col)
        elif old == 9:
            output.set(x,y,P['rim'])

def block(x,y,w,h,c):
    output.rect(x*2,y*2,w*2,h*2,P.get(c,c))

def pixels(points,col):
    for x,y in points: block(x,y,1,1,col)

# The upper meniscus catches a lilac glow beneath the bubbling surface.
block(9,13,7,1,'light')
block(7,14,3,1,'light')
block(5,15,2,1,'pink')
block(21,15,2,1,'bubble')
block(23,16,1,2,'bubble')
block(20,19,2,1,'bubble')
block(11,20,6,1,'bubble')
# A simple broken glass reflection keeps the liquid feeling transparent.
block(3,21,1,3,'light')
block(4,24,1,2,'light')
block(5,26,2,1,'light')
block(9,28,3,1,'light')

# Stepped bubble outlines, with highlights all lit from the upper left.
def bubble(x,y,large=True):
    rows = ['.rrr.','rwpbo','rpbbo','obboo','.ooo.'] if large else ['.rr.','rwbo','obbo','.oo.']
    colors={'o':'outline','r':'light','w':'white','p':'pink','b':'bubble'}
    for yy,row in enumerate(rows):
        for xx,k in enumerate(row):
            if k!='.': block(x+xx,y+yy,1,1,colors[k])

bubble(9,9)
bubble(17,7,False)
bubble(19,13)
# Small bubbles rise toward the neck.
pixels([(23,6),(22,7),(24,7),(23,8)],'bubble')
block(23,7,1,1,'foam')
block(15,8,1,1,'bubble')
# Little surface foam beads.
block(7,17,2,1,'pink')
block(8,18,1,1,'light')
block(16,13,1,1,'foam')
block(15,18,2,1,'light')
# Bubbles suspended in the lower, translucent potion.
bubble(16,24,False)
pixels([(10,23),(9,24),(11,24),(10,25)],'shade')
block(10,24,1,1,'foam')
block(14,28,1,1,'pink')
# A four-point magical glint in the liquid.
pixels([(6,20),(5,21),(6,21),(7,21),(6,22)],'white')
block(21,22,1,1,'foam')
view(output, scale=8, margin=0)
finish(output)
