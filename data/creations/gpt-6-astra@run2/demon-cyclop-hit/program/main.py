# Original art is retained pixel-for-pixel in the first frame.
f1 = new_canvas(47, 40, name='01_original')
f1.blit(input_canvas, 4, 4)
pose = input_canvas.copy(name='recoil_parts')
ink = '#141b1b'
skin = '#adbc3a'
shade = '#74a334'
horn = '#ffe18d'
white = '#fce2ca'
rim = '#c8966b'
# Roll the eye upward, exposing more of the pale lower eye.
pose.rect(17,16,3,3,white)
pose.rect(17,15,3,2,ink)
pose.set(20,15,white)
# Open the small mouth beneath the eye, with teeth and a visible tongue.
pose.rect(15,22,7,4,skin)
pose.poly([(16,22),(21,22),(23,24),(22,27),(16,27),(14,25)], shade)
pose.poly([(16,22),(21,22),(22,23),(22,25),(21,27),(16,27),(15,25),(15,23)], ink)
pose.rect(17,22,4,1,white)
pose.rect(17,25,4,1,'#9b3f45')
pose.rect(18,26,3,1,'#e06a65')
# Remove the planted right foot (on the image's left).
pose.clear(6,26,9,7)
# The bent knee and lifted foot project to the left.
pose.poly([(10,25),(13,26),(14,28),(11,30),(7,30),(4,29),(3,27),(5,25),(8,24)],ink)
pose.poly([(9,25),(12,26),(12,28),(10,29),(7,29),(5,28),(5,26),(8,25)],shade)
pose.line(8,25,11,26,skin)
pose.set(5,28,horn)
pose.set(7,29,horn)
# A row-wise tilt keeps every colour and the hand-built pixel edges crisp.
f2 = new_canvas(47,40,name='02_recoil')
pal = {p['index']:p['rgba'] for p in pose.palette()}
for y in range(33):
    lean = round((29-y)*0.18)
    for x in range(37):
        idx = pose.get(x,y)
        if pal[idx][3]:
            f2.set(x+4+lean,y+4,idx)
# A full-sprite red flash, including horns, eye, mouth, and dark contours.
f3 = new_canvas(47,40,name='03_impact')
flash = {
    '#141b1b':'#421b29', '#ffe18d':'#ffb299',
    '#adbc3a':'#ed5b59', '#74a334':'#bc3946',
    '#c8966b':'#e57778', '#fce2ca':'#ffd2c2',
    '#9b3f45':'#b12d4d', '#e06a65':'#ff7277',
}
pal = {p['index']:p['rgba'] for p in f2.palette()}
for y in range(40):
    for x in range(47):
        idx = f2.get(x,y)
        r,g,b,a = pal[idx]
        if a:
            key = '#%02x%02x%02x' % (r,g,b)
            f3.set(x,y,flash[key])
view(f1,scale=9)
view(f2,scale=9)
view(f3,scale=9)
finish([f1,f2,f3])
