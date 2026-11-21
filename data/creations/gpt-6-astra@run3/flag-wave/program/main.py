# Keep the original 4-pixel grid, palette, pole and ties.
f1 = new_canvas(56, 68, name='frame_1_high')
f1.blit(input_canvas, 4, 4)

def wave(name, shifts):
    c = new_canvas(56, 68, name=name)
    # Everything through the attachment stays stationary.
    for y in range(56):
        for x in range(20):
            c.set(x+4, y+4, input_canvas.get(x,y))
    # Vertical column displacement bends the cloth away from its hoist.
    for x in range(20,48):
        dy = shifts[x//4-5]*4
        for y in range(56):
            col = input_canvas.get(x,y)
            if input_canvas.palette()[col]['rgba'][3] != 0:
                c.set(x+4,y+4+dy,col)
    # Close the stepped outline where adjacent cloth columns bend apart.
    rgba = {p['index']: p['rgba'] for p in c.palette()}
    edge_blocks = []
    for y in range(4,64,4):
        for x in range(24,52,4):
            if rgba[c.get(x,y)][3] == 0:
                continue
            if any(rgba[c.get(nx,ny)][3] == 0 for nx,ny in [(x-4,y),(x+4,y),(x,y-4),(x,y+4)]):
                edge_blocks.append((x,y))
    for x,y in edge_blocks:
        c.rect(x,y,4,4,'#141b1b')
    return c

f2 = wave('frame_2_middle', [0,0,1,2,3,4,4])
f3 = wave('frame_3_low', [0,1,3,5,7,8,8])
view(f1, scale=6)
view(f2, scale=6)
view(f3, scale=6)
finish([f1,f2,f3])
