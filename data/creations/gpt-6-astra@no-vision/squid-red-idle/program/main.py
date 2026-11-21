# A one-pixel breath in either direction.  The lower tentacles are anchors;
# the soft mantle absorbs the displacement along a shallow curved seam.
W, H = 58, 57
PAD = 2
f1 = new_canvas(W+PAD*2, H+PAD*2, name='idle_01_original')
f1.blit(input_canvas, PAD, PAD)
source = [[input_canvas.get(x,y) for x in range(W)] for y in range(H)]

def breath(name, direction):
    out = new_canvas(W+PAD*2, H+PAD*2, name=name)
    for x in range(W):
        edge_distance = min(x, W-1-x)
        seam = min(40, 29 + (edge_distance*3)//5)
        for y in range(-1, H):
            # Repeat a row for inhalation, omit one for exhalation.  Both
            # transitions happen below the face, in the shaded soft body.
            if direction < 0:
                sy = y+1 if y < seam else y
            else:
                sy = y-1 if y <= seam else y
            if 0 <= sy < H:
                out.set(x+PAD, y+PAD, source[sy][x])
    return out

f2 = breath('idle_02_inhale', -1)
f3 = breath('idle_03_exhale', 1)
print(f1.stats_text())
print(f2.stats_text())
print(f3.stats_text())
print('INHALE: lower mantle and roots')
print(f2.matrix_text(region=(2,30,59,47)))
print('EXHALE: lower mantle and roots')
print(f3.matrix_text(region=(2,30,59,47)))
finish([f1, f2, f3])
