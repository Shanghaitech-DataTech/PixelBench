# A hand-pixelled, periodic 16 x 16 RPG timber texture.
result = new_canvas(16, 16, background='#533524', name='wooden_planks')
palette = {
    'S':'#533524', # recessed joins
    'K':'#603d28', # dark knot hearts
    'D':'#70462b', # end grain
    'B':'#875531', # deep warm grain
    'R':'#986437', # shaded timber
    'M':'#ac773f', # honey brown
    'H':'#be8b4d', # golden face
    'L':'#d1a05e', # raised edges
    'P':'#dfb575', # small fresh-cut glints
}
# Three unequal boards; end joints are staggered between columns.
rows = [
    'SLHRHRS HMRRS LMRR',
    'SLHRHRS HBRRS LMRR',
    'SLHMRRS DKBRS LMRR',
    'SLHMHRS HBRRS LMMR',
    'SDDDDBS HMRRS LHMR',
    'SPLLHRS HMRRS LHMR',
    'SLHMHRS HHMRS DDDD',
    'SLHMHRS HMMRS PLLH',
    'SLMBHRS HMMRS LHMR',
    'SHBKMRS HMMRS LHMR',
    'SLRBHRS DDDDS LHBR',
    'SLHMHRS LHHMS LRKR',
    'SLHHMRS HMRRS LHBR',
    'SLHHMRS HMRRS LHMR',
    'SLHMHRS HMRRS LHMR',
    'SLHRHRS HMRRS LMMR',
]
for y, row in enumerate(rows):
    row = row.replace(' ', '')
    assert len(row) == 16, (y, len(row))
    for x, symbol in enumerate(row):
        result.set(x, y, palette[symbol])
view(result, scale=24, margin=0)
repeat = new_canvas(64, 64, name='repeat_check')
for ty in range(4):
    for tx in range(4):
        repeat.blit(result, tx*16, ty*16)
view(repeat, scale=6, margin=0)
finish(result)
