output = input_canvas.copy(name='output')
snow='#e6ebf2'
shadow='#b3c8d8'
highlight='#f6f8f5'
# Follow the existing sprays, preserving dark needles beneath the snow.
for y in range(120):
    for x in range(82):
        p=input_canvas.get(x,y)
        if p==2:
            output.set(x,y,snow)
        elif p==1:
            near_snow=any(input_canvas.get(xx,yy)==2 for yy in range(max(0,y-2),min(120,y+2)) for xx in range(max(0,x-1),min(82,x+2)))
            if near_snow:
                output.set(x,y,shadow)
# Thicken the upper surfaces into small connected pillows of fresh snow.
for y in range(1,119):
    for x in range(1,81):
        if input_canvas.get(x,y)==2 and input_canvas.get(x,y-1)!=2:
            adjacent=sum(input_canvas.get(xx,y)==2 for xx in (x-1,x+1))
            if adjacent:
                output.set(x,y-1,snow)
                if x<46:
                    output.set(x,y-1,highlight)
# A tiny cap on the leader.
output.set(41,0,snow)
view(output,scale=5,margin=0)
finish(output)
