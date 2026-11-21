result = new_canvas(16, 16, background='#858788', name='cracked_stone')
# Hand-clustered midtones: broad stone grain without isolated noise.
colours = ['#707475', '#7c8081', '#898c8c', '#969998', '#a3a5a2', '#515757', '#62696a']
rows = [
'2222112223332222',
'2332111223333222',
'2332211222233211',
'2222222332222211',
'1122333332212222',
'1122343322112332',
'2222332211112332',
'3322222112222223',
'3332111222332223',
'2322111223332212',
'2222222223322112',
'1122332222221111',
'1223333211222221',
'2223322111223322',
'2232221112233332',
'2222112222333222',
]
for y, row in enumerate(rows):
    for x, value in enumerate(row):
        result.set(x, y, colours[int(value)])
# Fracture lips catch a little light on one side.
for x,y in [(11,0),(10,1),(10,2),(8,3),(8,4),(6,6),(7,7),(7,8),(10,9),(11,10),(11,11),(11,12),(12,14),(11,15),(11,5),(13,6),(14,7),(15,8),(0,8),(2,9)]:
    result.set(x,y,colours[3])
# Continuous broken seam wraps vertically; its branch wraps horizontally.
for x,y in [(10,0),(9,1),(9,2),(8,2),(7,3),(7,4),(7,5),(6,5),(5,6),(6,7),(6,8),(7,8),(8,9),(9,9),(10,10),(10,11),(10,12),(10,13),(11,14),(10,15)]:
    result.set(x,y,colours[6])
for x,y in [(9,1),(7,3),(7,4),(5,6),(6,7),(8,9),(10,11),(10,12),(11,14)]:
    result.set(x,y,colours[5])
for x,y in [(8,5),(9,5),(10,5),(11,6),(12,6),(12,7),(13,7),(14,7),(15,7),(0,7),(1,8),(2,8)]:
    result.set(x,y,colours[6])
# A few shallow pits and short mineral edges.
result.line(1,3,3,3,colours[1])
result.line(2,2,3,2,colours[3])
result.line(4,11,5,11,colours[1])
result.set(4,10,colours[3])
result.line(13,11,14,11,colours[0])
result.line(13,10,14,10,colours[3])
view(result, scale=24, margin=0)
finish(result)
