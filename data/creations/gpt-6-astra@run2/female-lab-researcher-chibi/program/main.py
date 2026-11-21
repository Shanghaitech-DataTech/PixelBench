result = new_canvas(16,16, name='female_lab_researcher')
palette = {
'.':None,
'O':'#20202f',
'H':'#30303d',
'h':'#4c4757',
'S':'#f5c6a0',
's':'#d9967c',
'B':'#774627',
'b':'#bd8247',
'W':'#fff9ee',
'C':'#dce6ed',
'c':'#9daebf',
'T':'#418e9a',
't':'#285469',
'P':'#52536e',
'G':'#80e1d4',
}
rows = [
'.....OOOOO......',
'....OHHhhHO.....',
'...OHHHHHHHO....',
'...OHHHSHHHO....',
'...OHSSSSSHO....',
'...OSBSSBSHO....',
'...OSbSSbSHO....',
'....OSSSSOHO....',
'....OcSTcOO.....',
'...OCWTWWCO.....',
'...OWWttWWOS....',
'...OSWCWWWSOG...',
'....OWCWWWOOG...',
'....OCCWCCO.....',
'.....OPPOO......',
'.....OO.OO......',
]
for y,row in enumerate(rows):
    for x,ch in enumerate(row):
        if ch != '.': result.set(x,y,palette[ch])
# A breast pocket and a small glass sample tube identify her lab role.
result.set(9,11,palette['c'])
result.set(10,11,palette['C'])
result.set(13,9,palette['c'])
result.set(13,10,palette['W'])
result.set(14,10,palette['O'])
result.set(14,11,palette['O'])
result.set(14,12,palette['O'])
result.set(13,13,palette['O'])
result.set(7,14,None)
result.set(6,14,palette['t'])
result.set(8,14,palette['t'])
view(result, scale=24)
finish(result)
