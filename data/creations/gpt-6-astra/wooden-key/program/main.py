result = new_canvas(16, 16, name='wooden_key')
D='#38251f'
S='#75452b'
W='#ae713e'
L='#daa05a'
H='#f0c783'
# Stepped silhouette: pierced bow, diagonal stem and two cut teeth.
rows = [
'................',
'...DDDD.........',
'..DHLLLD........',
'.DHLSSWLD.......',
'.DLS..SWD.......',
'.DLS..SWD.......',
'.DWWSSWLD.......',
'..DSWWWLWD..D...',
'...DDDSWLWDDLD..',
'......DSWLWLWD..',
'.......DSWLWD...',
'........DSWLWDD.',
'.........DSWLWLD',
'..........DSWLD.',
'...........DDD..',
'................',
]
palette={'D':D,'S':S,'W':W,'L':L,'H':H}
for y,row in enumerate(rows):
    for x,k in enumerate(row):
        if k!='.': result.set(x,y,palette[k])
view(result, scale=24)
save('wooden_key', result)
finish(result)
