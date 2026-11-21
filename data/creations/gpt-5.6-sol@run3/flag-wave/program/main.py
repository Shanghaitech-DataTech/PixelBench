f1 = input_canvas.copy(name='frame1')
def wave(name, shifts):
    f = input_canvas.copy(name=name)
    f.clear(20, 0, 28, 56)
    for i, dy in enumerate(shifts):
        x = 20 + i * 4
        input_canvas.select(x, 0, 4, 56 - dy).copy_to(x, dy, f, mode='over')
    return f
f2 = wave('frame2', [0, 0, 4, 4, 8, 8, 8])
f3 = wave('frame3', [0, 4, 8, 12, 16, 20, 20])
view(f2)
view(f3)
finish([f1, f2, f3])
