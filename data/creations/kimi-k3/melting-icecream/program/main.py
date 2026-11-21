# Melting ice cream: chocolate melts and drips down the cone.
output = input_canvas.copy(name='output')

E = '#5e363eff'  # chocolate scoop base brown
R = '#95524cff'  # chocolate reddish highlight
B = '#613942ff'  # darker outline brown
W = '#fef4f5ff'  # specular white (matches the scoop's existing shine)
G = '#c58d83ff'  # soft gloss for small drips

rects = [
    # --- melted cap: scoop sags over the cone rim with a wavy contour ---
    (20,32,23,1,E),
    (20,33,22,1,E),
    (21,34,5,1,E),
    (28,34,6,1,E),
    (35,34,7,1,E),
    (22,35,3,1,E),
    (30,35,2,1,E),
    (35,35,2,1,E),
    (40,35,2,1,E),
    (23,36,2,1,E),
    (30,36,2,1,E),
    (35,36,2,1,E),
    (40,36,2,1,E),
    # --- small drip over the left edge of the cone ---
    (18,32,2,3,E),
    (17,35,4,1,E),
    (18,36,2,1,E),
    # --- drip A (left, over the peach part of the cone) ---
    (23,37,2,8,E),
    (22,45,4,1,E),
    (22,46,4,1,E),
    (23,47,2,1,E),
    # --- drip B (middle, over the waffle divider) ---
    (30,37,2,4,E),
    (29,41,4,1,E),
    (30,42,2,1,E),
    # --- drip C (right, over the cream part, longest) ---
    (35,37,2,9,E),
    (34,46,4,1,E),
    (34,47,4,1,E),
    (35,48,2,1,E),
    # --- drip D (far right, over the cone's right edge) ---
    (40,37,2,1,E),
    (39,38,4,1,E),
    (40,39,2,1,E),
    # --- detached falling drop below drip A (open background there) ---
    (24,50,1,1,E),
    (23,51,2,3,E),
    (24,54,1,1,E),
    # --- puddle below the cone tip ---
    (26,59,9,1,E),
    (24,60,13,1,E),
    (26,61,9,1,B),
]
for x,y,w,h,col in rects:
    output.rect(x,y,w,h,col)

highlights = [
    # highlight oozing down from the scoop's lit area
    (32,32,3,1,R),(33,33,2,1,R),
    # drip highlights (light from the right)
    (24,37,1,2,R),
    (31,37,1,2,R),
    (36,38,1,2,R),
    (41,36,1,1,R),
    (24,46,1,1,R),
    (31,41,1,1,R),
    (36,47,1,1,R),
    (23,51,1,2,R),
    # puddle highlight
    (31,59,3,1,R),(34,60,1,1,R),
]
for x,y,w,h,col in highlights:
    output.rect(x,y,w,h,col)

# glossy sparkles (wet melted chocolate)
for x,y in [(35,46),(24,52),(30,60)]:
    output.set(x,y,W)
for x,y in [(23,45),(31,42)]:
    output.set(x,y,G)

finish(output)
