from pixelbench_api import *

c = new_canvas(16, 16)

# Palette - Detective game magnifying glass
# Warm lighting from top-left, rich brass rim, convex glass with specular glare,
# polished mahogany wood handle, and brass ferrule & pommel.
C = {
    # Brass Rim
    'g0': '#FFFDE6', # brilliant gleam (pale warm gold)
    'g1': '#FFDE59', # bright gold
    'g2': '#D69415', # rich gold
    'g3': '#8F5808', # dark gold
    'g4': '#4D2C03', # deep rim shadow

    # Glass Lens (concentric spherical glass shading)
    'w':  '#FFFFFF', # bright specular highlight
    'l0': '#DEF7FA', # white-cyan glare
    'l1': '#9DE2EF', # soft glare
    'l2': '#54B3D6', # bright crystal cyan
    'l3': '#2B80A3', # rich sapphire blue
    'l4': '#18506E', # deep lens blue
    'l5': '#0F3144', # rim shadow inside lens

    # Ferrule & Pommel (Brass)
    'f0': '#FFE885', # ferrule highlight
    'f1': '#E09E19', # ferrule mid-gold
    'f2': '#9E650B', # ferrule shadow gold
    'f3': '#5E3804', # ferrule deep shadow

    # Mahogany Wood Handle
    'h0': '#BA5D2F', # wood highlight
    'h1': '#853916', # wood body
    'h2': '#4F1E08', # wood shadow
}

grid = {}

# Glass interior (10x10 circular lens):
glass = {
    # Row 1:
    (3,1): 'w',  (4,1): 'w',  (5,1): 'l0', (6,1): 'l1',
    # Row 2:
    (2,2): 'w',  (3,2): 'w',  (4,2): 'l0', (5,2): 'l1', (6,2): 'l2', (7,2): 'l3',
    # Row 3:
    (1,3): 'w',  (2,3): 'w',  (3,3): 'l0', (4,3): 'l1', (5,3): 'l2', (6,3): 'l3', (7,3): 'l4', (8,3): 'l4',
    # Row 4:
    (1,4): 'w',  (2,4): 'l0', (3,4): 'l1', (4,4): 'l2', (5,4): 'l3', (6,4): 'l3', (7,4): 'l4', (8,4): 'l5',
    # Row 5:
    (1,5): 'l0', (2,5): 'l1', (3,5): 'l2', (4,5): 'l3', (5,5): 'l3', (6,5): 'l4', (7,5): 'l4', (8,5): 'l5',
    # Row 6:
    (1,6): 'l1', (2,6): 'l2', (3,6): 'l3', (4,6): 'l3', (5,6): 'l4', (6,6): 'l4', (7,6): 'l5', (8,6): 'l5',
    # Row 7:
    (2,7): 'l2', (3,7): 'l3', (4,7): 'l4', (5,7): 'l4', (6,7): 'l5', (7,7): 'l5',
    # Row 8:
    (3,8): 'l3', (4,8): 'l4', (5,8): 'l4', (6,8): 'l5',
}
grid.update(glass)

# Rim:
rim = {
    (3,0): 'g1', (4,0): 'g0', (5,0): 'g0', (6,0): 'g1',
    (2,1): 'g0', (7,1): 'g2',
    (1,2): 'g0', (8,2): 'g2',
    (0,3): 'g0', (9,3): 'g3',
    (0,4): 'g1', (9,4): 'g3',
    (0,5): 'g1', (9,5): 'g3',
    (0,6): 'g2', (9,6): 'g4',
    (1,7): 'g2', (8,7): 'g3',
    (2,8): 'g3', (7,8): 'g3',
    (3,9): 'g3', (4,9): 'g4', (5,9): 'g4', (6,9): 'g4',
}
grid.update(rim)

# Neck & Brass Collar (d=8):
grid[(9,8)] = 'f0' # bright top edge of collar
grid[(8,8)] = 'f1' # mid gold body of collar
grid[(8,9)] = 'f3' # underside shadow of collar

# Mahogany Handle (5 diagonal steps: d=9 to d=13):
# d=9:
grid[(10,9)] = 'h0'
grid[(9,9)]  = 'h1'
grid[(9,10)] = 'h2'

# d=10:
grid[(11,10)] = 'h0'
grid[(10,10)] = 'h1'
grid[(10,11)] = 'h2'

# d=11:
grid[(12,11)] = 'h0'
grid[(11,11)] = 'h1'
grid[(11,12)] = 'h2'

# d=12:
grid[(13,12)] = 'h0'
grid[(12,12)] = 'h1'
grid[(12,13)] = 'h2'

# d=13:
grid[(14,13)] = 'h0'
grid[(13,13)] = 'h1'
grid[(13,14)] = 'h2'

# Brass Pommel Cap (d=14, 15):
# d=14:
grid[(15,14)] = 'f0'
grid[(14,14)] = 'f1'
grid[(14,15)] = 'f3'

# d=15:
grid[(15,15)] = 'f2'

# Apply to canvas
for (x, y), key in grid.items():
    if 0 <= x < 16 and 0 <= y < 16:
        c.set(x, y, C[key])

print(c.stats())
view(c)
finish(c)
