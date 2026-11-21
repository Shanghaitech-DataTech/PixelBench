# 128x64 pixel-art bar chart: fruit data with mini fruit icons instead of text labels
# Data: apple 10, banana 5, orange 7, lemon 14, grape 2

BG    = '#f7f5ef'
AXIS  = '#3a3a44'
GRID  = '#dcdce4'
STEM  = '#7a4a21'
LEAF  = '#4da94a'

chart = new_canvas(128, 64, background=BG, name='fruit_chart')

# ---------------- mini fruit icons (10x10) ----------------
apple_icon = [
".....S....",
"...GGS....",
"..GGGS....",
"...rRRr...",
"..rRRRRr..",
".rRhRRRRr.",
".rRRRRRRr.",
".rRRRRRRr.",
"..rRRRRr..",
"...rrrr...",
]

banana_icon = [
"........BB",
".......YYy",
"......YYy.",
".....YYy..",
".....Yy...",
"....Yy....",
"....Yy....",
"...YYy....",
"..YYy.....",
".BBy......",
]

orange_icon = [
"....S.....",
"...GGS....",
"..GGGS....",
"..oOOOo...",
".oOhOOOo..",
".oOOOOOOo.",
".oOOOOOOo.",
".oOOOOOOo.",
".oOOOOOo..",
"..ooooo...",
]

lemon_icon = [
".......SG.",
"......GGG.",
"......G...",
"..lLLLl...",
".lLhLLLl..",
"lLLLLLLLLl",
"lLLLLLLLLl",
".lLLLLLl..",
"..lLLLl...",
"...lll....",
]

grape_icon = [
"....S.....",
"...GGS....",
"..GG......",
".pPPp.....",
"pPhPPp....",
"pPPpPPp...",
"pPPPPPp...",
".pPPPPp...",
"..pPPp....",
"...pp.....",
]

apple_map  = {'R':'#e23c41','r':'#9e2028','h':'#f57a70','S':STEM,'G':LEAF}
banana_map = {'Y':'#ffd23e','y':'#c9920f','B':'#6e4a1e'}
orange_map = {'O':'#ff8f1f','o':'#c96a0a','h':'#ffb35e','S':STEM,'G':LEAF}
lemon_map  = {'L':'#f9e44d','l':'#c4ad1d','h':'#fff59e','S':STEM,'G':LEAF}
grape_map  = {'P':'#9350c8','p':'#5f2f8e','h':'#b47ee6','S':STEM,'G':LEAF}

def draw_icon(c, x, y, rows, cmap):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch != '.':
                c.set(x + i, y + j, cmap[ch])

# fruit, value, icon, icon colors, bar main, bar edge, bar highlight
fruits = [
    ('apple',  10, apple_icon,  apple_map,  '#e23c41', '#9e2028', '#f57a70'),
    ('banana',  5, banana_icon, banana_map, '#ffd23e', '#c9920f', '#ffe58a'),
    ('orange',  7, orange_icon, orange_map, '#ff8f1f', '#c96a0a', '#ffbd66'),
    ('lemon',  14, lemon_icon,  lemon_map,  '#f9e44d', '#c4ad1d', '#fff7a0'),
    ('grape',   2, grape_icon,  grape_map,  '#9350c8', '#5f2f8e', '#c49ae8'),
]

SCALE = 7   # px per unit; lemon(14) -> 98px
BAR_X = 17

# gridlines every 2 units (drawn first, bars paint over them)
for k in range(1, 8):
    gx = BAR_X + 14 * k
    chart.line(gx, 2, gx, 61, GRID)

# value axis
chart.line(15, 2, 15, 61, AXIS)

# bars + icons
for i, (name, val, icon, cmap, bmain, bedge, blight) in enumerate(fruits):
    y0 = 2 + 12 * i
    L = val * SCALE
    chart.rect(BAR_X, y0 + 1, L, 8, bedge)
    chart.rect(BAR_X + 1, y0 + 2, L - 2, 6, bmain)
    chart.rect(BAR_X + 1, y0 + 2, L - 2, 2, blight)
    draw_icon(chart, 2, y0, icon, cmap)

view(chart)
finish(chart)
