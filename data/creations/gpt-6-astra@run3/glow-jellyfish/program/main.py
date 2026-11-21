result = new_canvas(16, 16, name='glow_jellyfish')
p = {
'O':'#102a49',
'S':'#245577',
'B':'#238da8e8',
'C':'#43c9d4dc',
'L':'#89f2ee',
'W':'#d4fff5',
'V':'#577caf',
'T':'#57c6d4',
}
rows = [
'................',
'......OOOO......',
'....OOLLCCOO....',
'...OLWWLCCBBO...',
'..OLWLCCCBBSBO..',
'..OLLCCTTCBSBO..',
'.OLLCCTLLTCBSBO.',
'.OLCCTLLLLTCBBO.',
'.OCCCLWLLWLCBBO.',
'..OLLLCCCCLLLO..',
'...OOTOOTOOTO...',
'....OTOOTOOTO...',
'...OTO..OTOOTO..',
'...OLO..OLOLO...',
'....O....O.O....',
'................',
]
for y,row in enumerate(rows):
    for x,ch in enumerate(row):
        if ch != '.': result.set(x,y,p[ch])
view(result, scale=24)
finish(result)
