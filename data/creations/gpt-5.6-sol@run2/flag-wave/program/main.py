f1 = input_canvas.copy(name='frame1')
def wave(name, offsets):
    c = input_canvas.copy(name=name)
    c.clear(20, 0, 28, 56)
    for x in range(20, 48):
        dy = offsets[(x-20)//4]
        for y in range(56-dy):
            col = input_canvas.get(x,y)
            if col != 0:
                c.set(x,y+dy,col)
    return c
f2 = wave('frame2', [0,0,4,4,8,8,8])
f3 = wave('frame3', [0,4,8,12,16,20,20])
view(f2)
view(f3)
finish([f1,f2,f3])
