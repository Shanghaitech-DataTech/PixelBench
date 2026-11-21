import colorsys
from pixelbench_api import *

output = input_canvas.copy(name='output')
palette = output.palette()

new_colors = {}

for p in palette:
    if p['name'] == 'transparent':
        continue
    r, g, b, a = p['rgba']
    idx = p['index']
    name = p['name']
    
    h, l, s = colorsys.rgb_to_hls(r/255.0, g/255.0, b/255.0)
    
    # 1. Moon core (c11)
    if name == 'c11':
        new_colors[idx] = (255, 210, 210)
        
    # 2. Yellow lights (c18, c30) -> Fiery orange/red
    elif name in ['c18', 'c30']:
        new_colors[idx] = (255, 60, 0)
        
    # 3. Magic rings / Cyans -> Bright red/crimson
    elif name in ['c10', 'c14', 'c15', 'c27', 'c39', 'c46', 'c50', 'c6', 'c7', 'c8', 'c13', 'c40', 'c41', 'c42']:
        # Map to glowing reds depending on original lightness
        new_h = 355 / 360.0
        new_s = 0.9
        new_l = l
        nr, ng, nb = colorsys.hls_to_rgb(new_h, new_l, new_s)
        new_colors[idx] = (int(nr*255), int(ng*255), int(nb*255))
        
    # 4. Pink stars
    elif name == 'c43':
        new_colors[idx] = (255, 0, 40)
        
    # 5. Castle walls (browns and greys) -> Obsidian / Dark purple-grey
    elif name in ['c17', 'c25', 'c29', 'c38', 'c72', 'c9', 'c32']:
        new_h = 270 / 360.0 # purple
        new_s = 0.15 # low saturation
        new_l = l * 0.7 # slightly darker
        nr, ng, nb = colorsys.hls_to_rgb(new_h, new_l, new_s)
        new_colors[idx] = (int(nr*255), int(ng*255), int(nb*255))
        
    # 6. Mountains and ground (greens/olives) -> Dark ash / black-red
    elif name in ['c56', 'c57', 'c59', 'c60', 'c62']:
        new_h = 0.0 # red
        new_s = 0.2
        new_l = l * 0.6
        nr, ng, nb = colorsys.hls_to_rgb(new_h, new_l, new_s)
        new_colors[idx] = (int(nr*255), int(ng*255), int(nb*255))
        
    # 7. Sky and Clouds (Blues)
    else:
        # Blood moon sky
        new_h = 355 / 360.0
        if l < 0.2:
            new_l = l * 0.4
            new_s = 0.5
        elif l < 0.5:
            new_l = l * 0.5
            new_s = 0.6
        elif l < 0.7:
            new_l = l * 0.6
            new_s = 0.7
        else:
            new_l = l * 0.7
            new_s = 0.8
            
        nr, ng, nb = colorsys.hls_to_rgb(new_h, new_l, new_s)
        new_colors[idx] = (int(nr*255), int(ng*255), int(nb*255))

for y in range(128):
    for x in range(256):
        c_idx = output.get(x, y)
        if c_idx != 0:
            nr, ng, nb = new_colors[c_idx]
            output.set(x, y, (nr, ng, nb, 255))

finish(output)
