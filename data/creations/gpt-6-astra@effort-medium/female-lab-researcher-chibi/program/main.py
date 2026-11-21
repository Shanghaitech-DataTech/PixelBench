result = new_canvas(16,16,name='researcher')
palette = {
'.':None,'O':'#202334','H':'#171a25','h':'#343445','g':'#505065',
'S':'#edb58e','s':'#c98570','L':'#ffdab0','E':'#74452f','e':'#bb8046',
'W':'#f7faf5','w':'#cbdce1','v':'#8cabbc','T':'#438d9a','t':'#285b72',
'P':'#45495f','B':'#252a3e','C':'#73d8c7'
}
rows=[
'.....OOOOOO.....',
'....OHHhhHHO....',
'...OHhHHHHHHO...',
'...OHHHHLHHHO...',
'...OHLLLHLHHO...',
'...OHLELLELHO...',
'...OHSLLLssHO...',
'....OHsLLsHO....',
'....OvWTTWvO....',
'...OWWWttWWWO...',
'...OWWWTWWwWO...',
'...OSWwWWvWSO...',
'....OWWWWwWO....',
'....OWwOWwWO....',
'.....OP.OP......',
'....OBB.OBB.....',
]
for y,row in enumerate(rows):
    for x,k in enumerate(row):
        if k!='.': result.set(x,y,palette[k])
# Coat pocket, badge, and tiny pen.
result.set(10,10,palette['v'])
result.set(10,9,palette['T'])
result.set(7,11,palette['v'])
view(result)
finish(result)
