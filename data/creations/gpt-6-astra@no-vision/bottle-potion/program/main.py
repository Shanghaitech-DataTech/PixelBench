# Preserve the original bottle and its two-pixel grid.
result = input_canvas.copy(name='output')
P = {
    'surface':'#8c44bf',
    'body':'#b77de0',
    'shade':'#9156bf',
    'deep':'#63348e',
    'light':'#d5a2f0',
    'rim':'#dba8f5',
    'shine':'#fff0ff',
    'pale':'#ecd4f8',
    'bubble':'#aa64d2',
}
original = [[input_canvas.get(x,y) for x in range(64)] for y in range(64)]
remap = {5:P['surface'], 6:P['body'], 7:P['light'], 8:P['body'], 9:P['deep'], 10:P['shade']}
for y in range(64):
    for x in range(64):
        if original[y][x] in remap:
            result.set(x,y,remap[original[y][x]])

def px(x,y,col):
    result.rect(2*x,2*y,2,2,col)

def stamp(x,y,rows,colors):
    for j,row in enumerate(rows):
        for i,ch in enumerate(row):
            if ch in colors:
                px(x+i,y+j,colors[ch])

# A restrained shadow crescent follows the lower/right wall of the liquid.
light_ids = {6,7,8,10}
for y in range(19,31):
    for x in range(2,27):
        if original[2*y][2*x] not in light_ids:
            continue
        threshold = {19:25,20:25,21:24,22:24,23:23,24:22,25:21,26:20,27:19,28:17,29:15,30:12}[y]
        if x >= threshold:
            px(x,y,P['shade'])
        if y >= 29:
            px(x,y,P['shade'])
# Warm lavender glints in the liquid, respecting the old fill mask.
for x,y in [(3,20),(3,21),(4,22),(4,23),(4,24),(5,25),(6,26),(7,27),(9,28),(10,28)]:
    if original[2*y][2*x] in light_ids:
        px(x,y,P['light'])

# Two suspended bubbles in the clear headspace of the bottle.
stamp(9,7,[
    '.ooo.',
    'ohppo',
    'opppo',
    'opppo',
    '.ooo.',
], {'o':P['bubble'],'p':P['pale'],'h':P['shine']})
stamp(21,8,[
    '.o.',
    'oho',
    '.o.',
], {'o':P['bubble'],'h':P['pale']})

# Foam bubbles floating on the elliptical purple surface.
stamp(6,15,[
    '.hh.',
    'hddr',
    'rddr',
    '.rr.',
], {'h':P['shine'],'r':P['rim'],'d':P['surface']})
stamp(15,13,[
    '.hhh.',
    'hdddr',
    'rdddr',
    'rdddr',
    '.rrr.',
], {'h':P['shine'],'r':P['rim'],'d':P['surface']})
stamp(21,16,[
    '.h.',
    'hdr',
    '.r.',
], {'h':P['shine'],'r':P['rim'],'d':P['surface']})
px(12,17,P['rim'])
px(18,19,P['rim'])

# Small bubbles visible beneath the liquid surface.
stamp(17,23,[
    '.hh.',
    'hddr',
    'rddr',
    '.rr.',
], {'h':P['pale'],'r':P['light'],'d':P['body']})
stamp(10,25,[
    '.h.',
    'hdr',
    '.r.',
], {'h':P['pale'],'r':P['light'],'d':P['body']})
px(14,23,P['light'])

# Tiny magical twinkles, kept inside the bottle's clear upper chamber.
stamp(16,9,['.s.','sss','.s.'], {'s':P['bubble']})

print(result.stats_text())
# Inspect at the artwork's native 2x pixel grid as well as in full resolution.
print(result.select(0,0,64,64).resize(32,32).preview().matrix_text())
save('purple-potion', result)
finish(result)
