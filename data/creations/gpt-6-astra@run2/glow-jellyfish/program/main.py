result = new_canvas(16, 16, name='glow_jellyfish')
# Hand-placed silhouette and luminous, translucent bell.
palette = {
'O':'#15243f', 'S':'#244c68', 'B':'#277995',
'C':'#3db9cd', 'L':'#7eece5', 'H':'#d3fff2',
'T':'#4296b9', 'V':'#6766ad', 'G':'#a1fff0',
'A':'#43bed0b8', 'D':'#296b93cf'
}
rows = [
'................',
'......OOOO......',
'....OOLLCCOO....',
'...OLHHLLCCBO...',
'..OLHLLLCCCBBO..',
'..OHLCCCLCCBBO..',
'.OLLCACCLACBBBO.',
'.OCCACCCACABBBO.',
'.OBBSCBSCBSCBBO.',
'..OOLGLGLGLOOO..',
'...OTOVOVOTO....',
'...OLOVOVOCO....',
'....OLOVOVOLO...',
'....OGO..OGO....',
'.....O....O.....',
'................',
]
for y,row in enumerate(rows):
    for x,ch in enumerate(row):
        if ch != '.': result.set(x,y,palette[ch])
view(result, scale=24, margin=0)
finish(result)
