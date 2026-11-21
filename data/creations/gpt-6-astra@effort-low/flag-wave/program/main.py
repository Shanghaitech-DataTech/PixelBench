f1 = input_canvas.copy(name='frame_1')
def wave(name, offsets):
    c = new_canvas(48,56,name=name)
    for y in range(56):
        for x in range(48):
            colour = input_canvas.get(x,y)
            dy = 0 if x < 20 else offsets[x//4-5]*4
            if y+dy < 56:
                c.set(x,y+dy,colour)
    return c
f2 = wave('frame_2', [0,0,1,2,3,3,3])
f3 = wave('frame_3', [0,0,1,3,5,7,7])
view(f1)
view(f2)
view(f3)
finish([f1,f2,f3])
