# Keep the original sprite intact, with room for recoil around its planted foot.
f1 = new_canvas(49, 43, name='01-original')
f1.blit(input_canvas, 4, 8)
pose = input_canvas.copy(name='recoil-source')
ink = '#141b1b'
skin = '#adbc3a'
shade = '#74a334'
white = '#fce2ca'
rim = '#c8966b'
# Roll the pupil to the upper edge of the single eye.
for y in range(16,19):
    for x in range(16,20):
        pose.set(x,y,white)
pose.rect(18,15,3,3,ink)
pose.set(18,15,white)
# Replace the closed mouth with an open, shaded gasp.
pose.rect(14,22,9,4,skin)
pose.poly([(16,22),(20,22),(22,24),(22,26),(20,28),(16,28),(14,26),(14,24)],ink)
pose.line(16,23,20,23,'#4f3028')
pose.rect(16,24,5,3,'#4f3028')
pose.line(17,26,20,26,rim)
pose.line(17,27,19,27,rim)
pose.set(16,23,white)
pose.set(20,23,white)
# A clockwise recoil keeps the right-side toe planted and lifts the left toe.
rotated = pose.select(0,0,37,33).rotate(12, algorithm='rotsprite').preview()
print('Rotated size', rotated.stats_text())
f2 = new_canvas(49,43,name='02-recoil')
f2.blit(rotated,3,2)
# Impact flash recolours every opaque monster pixel, keeping transparency and contrast.
f3 = new_canvas(49,43,name='03-red-impact')
tints = {
    '#141b1b':'#481b29',
    '#ffe18d':'#ffb48a',
    '#adbc3a':'#ef554e',
    '#74a334':'#bd3547',
    '#c8966b':'#f77a75',
    '#fce2ca':'#ffd0bb',
    '#4f3028':'#792b3a',
}
for y in range(43):
    for x in range(49):
        idx = f2.get(x,y)
        rgba = f2.palette()[idx]['rgba']
        if rgba[3]:
            key = '#%02x%02x%02x' % tuple(rgba[:3])
            f3.set(x,y,tints[key])
print(f1.stats_text())
print(f2.stats_text())
print(f2.matrix_text())
print(f3.stats_text())
finish([f1,f2,f3])
