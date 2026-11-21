result = new_canvas(16,16)
colors = {
'O':'#122640','D':'#23516b','B':'#367e9a','C':'#53c9d8','L':'#a0f5ed','W':'#e0fff8','S':'#648ece','P':'#8abcf0'
}
rows = [
'................',
'......OOOO......',
'....OOBLLBOO....',
'...OBLWWLLCBO...',
'..OBLWLCCCCSBO..',
'..OLWLCCBBCCSO..',
'..OLLCBBSSBCSO..',
'..OCCBSPPSBBSO..',
'.ODCCCLLLLCCCDO.',
'..OOCLCCCCLCOO..',
'....OCOOOOCO....',
'...OLO.CC.ODO...',
'...OC.OLO..OCO..',
'....O.OC...OO...',
'.......O........',
'................',
]
for y,row in enumerate(rows):
    for x,ch in enumerate(row):
        if ch != '.': result.set(x,y,colors[ch])
view(result)
finish(result)
