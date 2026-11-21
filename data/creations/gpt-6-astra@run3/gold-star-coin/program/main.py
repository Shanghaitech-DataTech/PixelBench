result = new_canvas(16, 16, name="gold_star_coin")
palette = {'o':'#75401f','s':'#b96b25','g':'#e9a52b','l':'#ffd65a','h':'#fff1a0','d':'#995321'}
rows = [
'................',
'.....oooooo.....',
'...oohhhhhhoo...',
'..ohhllllllgso..',
'..ohlllllllgso..',
'.ohllllllllggso.',
'.ohlllllllllgso.',
'.ohlllllllllgso.',
'.ohlllllllllgso.',
'.ohlllllllllgso.',
'.ogllllllllggso.',
'..ogllllllggso..',
'..oggggggggsso..',
'...osssssssoo...',
'.....oooooo.....',
'................',
]
for y,row in enumerate(rows):
    assert len(row)==16, (y,len(row))
    for x,p in enumerate(row):
        if p!='.': result.set(x,y,palette[p])
star = ['...d...', '...d...', 'ddddddd', '.ddddd.', '..ddd..', '.dd.dd.', '.d...d.']
# A recessed star, with a fine glint on its upper edge.
for y,row in enumerate(star):
    for x,p in enumerate(row):
        if p == 'd': result.set(x+4,y+5,palette['d'])
result.set(7,4,palette['h'])
result.line(4,6,6,6,palette['h'])
result.line(8,6,10,6,palette['h'])
view(result, scale=24)
finish(result)
