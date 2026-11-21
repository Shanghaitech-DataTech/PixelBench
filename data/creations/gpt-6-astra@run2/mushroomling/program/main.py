result = new_canvas(16, 16, name='mushroomling')
colors = {'D':'#282333', 'R':'#df424b', 'W':'#fff4df', 'C':'#e6bb83'}
rows = [
'................',
'.....DDDDDD.....',
'...DDRRRRRRDD...',
'..DRRWWRRRRRRD..',
'.DRRWWWRRRWWRRD.',
'.DRRRRRRRRWWRRD.',
'DRRWWRRRRRRRRRRD',
'.DDDDDDDDDDDDDD.',
'....DCCCCCCD....',
'..DDCWDCWDCCDD..',
'.DCCCDDCDDCCCCD.',
'..DDCCCCCCCCDD..',
'....DCCCCCCD....',
'....DCCDDCCD....',
'....DDDDDDDD....',
'................',
]
for y, row in enumerate(rows):
    assert len(row) == 16, (y,len(row))
    for x, char in enumerate(row):
        if char != '.':
            result.set(x,y,colors[char])
view(result, scale=24, margin=0)
finish(result)
