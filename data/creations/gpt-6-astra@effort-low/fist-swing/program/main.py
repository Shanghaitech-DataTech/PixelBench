f1 = new_canvas(38,46,name='original')
f1.blit(input_canvas,2,1)
f2 = f1.copy(name='light_punch')
# Replace only the raised left arm; retain the head, torso and stance.
f2.clear(16,9,19,7)
pal = {'a':'#222034','c':'#eec39a','e':'#df7126','f':'#8f563b'}
rows = [
'............aaaa',
'aaa........acccca',
'ceaaaaaaa aacccca',
'ccceccccca cceeea',
'fccceeeeeeeeeefa',
'fffaffffffffaaa',
'fffa aaaaaaa',
]
# Continuous skin and shadow bands from the shoulder to the knuckles.
rows[2]='ceaaaaaaaaaccccca'
rows[3]='ccceccccccccceeea'
for yy,row in enumerate(rows):
    for xx,ch in enumerate(row):
        if ch in pal: f2.set(16+xx,9+yy,pal[ch])
view(f1,scale=8)
view(f2,scale=8)
finish([f1,f2])
