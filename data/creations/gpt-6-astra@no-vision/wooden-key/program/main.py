result = new_canvas(16, 16, name="wooden_key")
colors = {'D':'#34251f', 'S':'#75452c', 'B':'#ad713d', 'H':'#dca35b', 'L':'#f3cd86'}
rows = [
'................',
'.....DDDDD......',
'....DHLLHHD.....',
'...DHHBBSBHD....',
'...DHB...BSD....',
'...DHB...BSD....',
'...DSHBBHBSD....',
'....DSSSSSD.....',
'......DHSD......',
'......DHSD......',
'......DHSBHHD...',
'......DHSDHSD...',
'......DHSD......',
'......DHBHBHD...',
'......DDDDDDD...',
'................',
]
for y, row in enumerate(rows):
    assert len(row) == 16
    for x, ch in enumerate(row):
        if ch != '.': result.set(x,y,colors[ch])
print(result.stats_text())
print(result.matrix_text())
finish(result)
