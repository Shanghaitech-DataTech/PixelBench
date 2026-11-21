result = new_canvas(16,16)
p = {
'O':'#15283f', 'D':'#23516b', 'B':'#307e9b', 'C':'#42b8cd',
'L':'#74edeb', 'W':'#cefff6', 'S':'#438ea8', 'T':'#57d3d9',
'G':'#85fff3'
}
rows = [
'................',
'......OOOO......',
'....OOLLCCOO....',
'...OLWWLLCCDO...',
'..OLWWLCCCBBDO..',
'..OWWLCCCBSSDO..',
'.OLLLCCCBSSSDDO.',
'.OLLCOLLCOLSDDO.',
'.OCCCOCCCOCSDDO.',
'..OLLLLLLLLLOO..',
'...OOLOOOLOO....',
'....OTO.OTO.....',
'...OTO..OTO.....',
'...OGO...OGO....',
'....O.....O.....',
'................',
]
for y,row in enumerate(rows):
    for x,key in enumerate(row):
        if key != '.': result.set(x,y,p[key])
view(result, scale=24)
finish(result)
