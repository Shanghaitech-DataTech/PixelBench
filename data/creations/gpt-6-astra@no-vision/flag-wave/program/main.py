# The source uses a 12 by 14 grid of 4-pixel blocks.
# Keep the pole and both attachment wraps stationary; deform only the free cloth.
f1 = input_canvas.copy(name='frame_1_high')
f2 = input_canvas.copy(name='frame_2_middle')
f3 = input_canvas.copy(name='frame_3_low')
for frame, offsets in [(f2, [0,0,1,1,2,3,3]), (f3, [0,0,1,2,4,5,5])]:
    frame.clear(20, 0, 28, 56)
    for col, drop in zip(range(5,12), offsets):
        for row in range(14):
            colour = input_canvas.get(col*4,row*4)
            if colour != 0:
                frame.rect(col*4, (row+drop)*4, 4, 4, colour)
for frame in [f1,f2,f3]:
    print(frame.stats_text())
    # Inspect at the artwork's native block scale.
    for y in range(0,56,4):
        print(''.join('.' if frame.get(x,y)==0 else str(frame.get(x,y)) for x in range(0,48,4)))
print(f3.matrix_text(region=(20,16,47,47)))
finish([f1,f2,f3])
