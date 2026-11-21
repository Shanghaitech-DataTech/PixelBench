f1 = input_canvas.copy(name='frame_1')
def wave(name, shifts):
    c = input_canvas.copy(name=name)
    c.clear(20,0,28,56)
    for x in range(20,48):
        dy=shifts[x//4-5]*4
        for y in range(56-dy):
            idx=input_canvas.get(x,y)
            c.set(x,y+dy,idx)
    return c
f2=wave('frame_2',[0,0,1,2,3,3,3])
f3=wave('frame_3',[0,1,3,4,5,5,5])
view(f1)
view(f2)
view(f3)
finish([f1,f2,f3])
