result = new_canvas(16, 16, name='female_lab_researcher')
p = {
'.':None,
'O':'#191923',
'H':'#272632',
'G':'#41404e',
'S':'#d89876',
'F':'#f4c5a0',
'L':'#ffe0b6',
'E':'#633a27',
'A':'#a66a37',
'R':'#db8e82',
'W':'#fffdf1',
'C':'#dbe5ed',
'D':'#8d9eaf',
'T':'#427d8b',
'B':'#284857',
'Q':'#75d8d0',
'V':'#d0fff1',
}
rows = [
'.....OOOOOO.....',
'....OHGGHHHO....',
'...OHGGHHHHHO...',
'...OHHHHLFHHO...',
'...OHHLFLFLHO...',
'...OHFEFFEFHO...',
'...OHFAFFAFHO...',
'...OHSRFSRFHO...',
'...OHHSSSSHO....',
'...OHWCTCWHO....',
'...OCWWTWWCO.O..',
'...OWWCTCWWSSVO.',
'...OSWCBBWDC OQO.'.replace(' ', ''),
'.....WWDBWW..O..',
'......B..B......',
'.....OO..OO.....',
]
for y,row in enumerate(rows):
    assert len(row)==16, (y,len(row))
    for x,key in enumerate(row):
        result.set(x,y,p[key])
view(result, scale=24)
finish(result)
