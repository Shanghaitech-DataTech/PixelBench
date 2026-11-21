# The input is drawn on a 4-pixel grid. Preserve that grid in every pose.
S = 4
W, H = 56, 64
OX, OY = 4, 4
base = [[input_canvas.get(x*S, y*S) for x in range(12)] for y in range(14)]
ink = input_canvas.get(36, 0)
red = input_canvas.get(36, 4)
light = input_canvas.get(28, 12)

# Original pixels, only translated to give all poses breathing room.
f1 = new_canvas(W, H, name='frame_1_high')
f1.blit(input_canvas, OX, OY)

# The shaft and both ties are fixed for the entire cycle.
def pole_frame(name):
    result = new_canvas(W, H, name=name)
    input_canvas.select(0, 0, 20, 56).copy_to(OX, OY, result)
    return result

def block(c, x, y, color):
    c.rect(OX+x*S, OY+y*S, S, S, color)

# Mid-stroke: a loose fold travels outward, making the flag belly sag
# while the free edge passes the height of the upper tie.
f2 = pole_frame('frame_2_middle')
tops =    [3, 3, 3, 4, 4, 3, 3]
bottoms = [8, 8, 9,10,10, 9, 9]
for x, top, bottom in zip(range(5,12), tops, bottoms):
    for y in range(top,bottom+1):
        col = ink if y in (top,bottom) or x == 11 else red
        block(f2,x,y,col)
for x,y in [(6,4),(6,5),(7,4),(7,5),(7,6),(8,5),(8,6)]:
    block(f2,x,y,light)

# Low extreme: invert the fabric's curvature about its fixed attachment.
# Only the cloth beyond the shaft changes; its original pixel clusters
# and thickness are retained as the fly end drops.
f3 = pole_frame('frame_3_low')
for y in range(12):
    for x in range(5,12):
        block(f3,x,y,base[11-y][x])

# Inspect each output and a temporary strip; the strip is not submitted.
view(f1,scale=6)
view(f2,scale=6)
view(f3,scale=6)
strip = new_canvas(W*3,H,name='pose_comparison')
strip.blit(f1,0,0).blit(f2,W,0).blit(f3,W*2,0)
view(strip,scale=4)
# Verify exact preservation and stationary attachment before export.
for y in range(56):
    for x in range(48):
        assert f1.get(x+OX,y+OY) == input_canvas.get(x,y)
for frame in (f2,f3):
    for y in range(56):
        for x in range(20):
            assert frame.get(x+OX,y+OY) == f1.get(x+OX,y+OY)
save('flag_wave_1',f1)
save('flag_wave_2',f2)
save('flag_wave_3',f3)
finish([f1,f2,f3])
