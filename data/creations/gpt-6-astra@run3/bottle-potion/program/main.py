output = input_canvas.copy(name='output')
recolors = {'#2f7598':'#7540a4','#74b8cf':'#ae70d5','#77b7ce':'#ae70d5','#76b7d1':'#ae70d5','#31121d':'#512665','#7bb5cb':'#ae70d5'}
ids={input_canvas.color(k):v for k,v in recolors.items()}
for y in range(64):
    for x in range(64):
        p=input_canvas.get(x,y)
        if p in ids: output.set(x,y,ids[p])
def block(x,y,w,h,col):
    output.rect(x*2,y*2,w*2,h*2,col)
# A darker right-hand edge gives the potion depth, keeping the original outline.
body=input_canvas.color('#74b8cf')
for y in range(44,62,2):
    xs=[x for x in range(0,64,2) if input_canvas.get(x,y)==body]
    if xs:
        for x in xs[-3:]: output.rect(x,y,2,2,'#8c4db6')
# Reflections in the lower liquid.
block(5,23,1,3,'#dda4ee')
block(6,26,1,1,'#dda4ee')
block(7,27,1,1,'#dda4ee')
block(10,29,3,1,'#c78ae2')
# Pixel bubbles with a bright upper-left glint, in the same 2px grid as the bottle.
def bubble(x,y,r=2,air=False):
    dark='#9653bb' if air else '#512665'
    light='#e9b8fa'
    fill='#d19be8' if air else '#a96cce'
    if r==2:
        block(x+1,y,2,1,dark)
        block(x,y+1,1,2,dark)
        block(x+3,y+1,1,2,dark)
        block(x+1,y+3,2,1,dark)
        block(x+1,y+1,2,2,fill)
        block(x+1,y,1,1,light)
        block(x,y+1,1,1,light)
    else:
        block(x+1,y,1,1,light)
        block(x,y+1,1,1,light)
        block(x+1,y+1,1,1,fill)
        block(x+2,y+1,1,1,dark)
        block(x+1,y+2,1,1,dark)
# Bubbles suspended above and breaking through the surface.
bubble(13,8,2,True)
bubble(19,10,1,True)
bubble(8,11,1,True)
bubble(11,14,2)
bubble(19,15,2)
bubble(6,16,1)
bubble(15,18,1)
# Small pink foam flecks and magical glints.
block(16,14,1,1,'#e9b8fa')
block(10,19,1,1,'#d19be8')
block(23,17,1,1,'#e9b8fa')
block(18,25,1,3,'#efd0ff')
block(17,26,3,1,'#efd0ff')
block(12,24,1,1,'#d9a3ee')
view(output)
finish(output)
