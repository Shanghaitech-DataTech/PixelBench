# Preserve the complete original on a shared, padded animation canvas.
f1 = new_canvas(36, 48, name='frame_1_original')
f1.blit(input_canvas, 2, 2)
f2 = f1.copy(name='frame_2_left_jab')
# Coordinates below are relative to the original sprite.
def pixel(x,y,col):
    f2.set(x+2,y+2,col)
def row(x,y,values):
    for i,v in enumerate(values):
        pixel(x+i,y,None if v=='.' else int(v))
# Remove the bent forearm and fist, leaving the head and torso in place.
for y in range(7,16):
    for x in range(13,22):
        pixel(x,y,None)
# Reestablish the jaw, neck, and shoulder beneath the former guard.
row(12,7,'31')
row(12,8,'1')
row(12,9,'1')
# A compact fist at the end of a nearly level arm.
row(26,9,'1111')
row(12,10,'11111')
row(25,10,'133331')
row(12,11,'5133311111111135331')
row(12,12,'3553333333333533531')
row(12,13,'3355555555555555611')
row(12,14,'33366666666666111')
row(12,15,'55556111111111')
# Keep the original lower edge of the shoulder and torso.
view(f1, scale=8)
view(f2, scale=8)
finish([f1,f2])
