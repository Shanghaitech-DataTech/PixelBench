result = new_canvas(16, 16, name='female_lab_researcher')
palette = {
'.': None,
'H': '#191c2a', 'h': '#2b3042', 's': '#464b62',
'f': '#efba91', 'F': '#ffdab1', 'r': '#d88c7c',
'e': '#513421', 'b': '#985c32',
'O': '#576477', 'W': '#fffaf0', 'w': '#dce7e9', 'g': '#a4bbc8',
'T': '#3f8c94', 't': '#27606f', 'P': '#344054',
'C': '#8be0d2'
}
rows = [
'.....HHHHHH.....',
'....HhhhhhhH....',
'...HhssshhhhH...',
'...HhhHhHFFFH...',
'...HhFFeFFeFH...',
'...HhFFbFFbFH...',
'...HHFrFFFrrH...',
'....HHFffFHH....',
'....OWWffWWO....',
'...OWWgTgWWWO...',
'...OWWWtWWWgO...',
'...OfWgWgWWfO...',
'....OWWgWWWO....',
'.....OwwwwO.....',
'.....HPPPPH.....',
'.....HH..HH.....',
]
for y,row in enumerate(rows):
    assert len(row)==16, (y,len(row))
    for x,k in enumerate(row):
        if k != '.': result.set(x,y,palette[k])
# Pen and pocket in the coat.
result.set(10,10,palette['T'])
result.set(11,10,palette['g'])
result.line(10,11,11,11,palette['g'])
view(result, scale=24)
finish(result)
