# skeleton-grunt: 32x32 RPG enemy — hunched skeleton, short sword raised,
# small wooden shield on the leading arm, dark joint shading, transparent bg.

ROWS = [
    "................................",  # y0
    "................................",  # y1
    "................................",  # y2
    "................................",  # y3
    "................BBBB............",  # y4  skull top
    "...............BBBBBB...........",  # y5  cranium
    "...............BEBBBEB..........",  # y6  glowing eyes
    "...............BBBBBB..........",  # y7  cranium
    "...............bBJJB...........",  # y8  jaw, dark mouth
    ".................bb............",  # y9  neck
    ".............BBbBbBB...........",  # y10 raised hunched shoulders
    "............BB.Bb..BB..........",  # y11 arms + spine
    "............BbBbB...Jb.........",  # y12 ribs + elbow joint
    "............bbbJb..............",  # y13 spine joint
    "............bbBb...............",  # y14 ribs
    ".......RRRRR..bb...............",  # y15 shield rim + hip
    "......RWWWWWRBb................",  # y16 shield face + hip
    "......RWWWWWRBbB...............",  # y17 shield + pelvis
    "......RWWJWwRBb................",  # y18 shield boss + pelvis
    "......RWWWWWR.Bb...............",  # y19 shield + right thigh
    "......RWWWWwR.bB...............",  # y20 shield shading + leg
    ".......RRRRR..Jb...............",  # y21 shield base + knee joint
    "...........bBBbB...............",  # y22 shins
    "...........bB.bB...............",  # y23 shins
    "...........Jb.Jb...............",  # y24 ankle joints
    "..........BBb.bBB..............",  # y25 feet
    "................................",  # y26
    "................................",  # y27
    "................................",  # y28
    "................................",  # y29
    "................................",  # y30
    "................................",  # y31
]

COLORS = {
    'B': '#e8e2cf',  # bone light
    'b': '#b3a98c',  # bone shade
    'J': '#5f5340',  # dark joint
    'E': '#d8482c',  # eye glow
    'S': '#d3d8e2',  # steel light
    's': '#8a92a2',  # steel shade
    'G': '#6e4a26',  # grip / guard leather
    'R': '#4a3115',  # shield rim
    'W': '#9a6432',  # wood light
    'w': '#6b421e',  # wood dark
}

c = new_canvas(32, 32, name="skeleton-grunt")
for ch, hx in COLORS.items():
    c.color(hx, name=ch)

for y, row in enumerate(ROWS):
    row = row.ljust(32)
    for x, ch in enumerate(row):
        if ch in COLORS:
            c.set(x, y, ch)

# short sword, raised in the skeleton's left hand (viewer's right)
c.line(23, 4, 23, 12, 'S')       # blade
c.line(24, 5, 24, 11, 's')       # blade shading
c.line(22, 13, 25, 13, 'G')      # crossguard
c.line(23, 14, 23, 15, 'G')      # grip
c.set(23, 16, 's')               # pommel
c.set(22, 12, 'b')               # hand knuckle
c.set(24, 12, 'b')               # hand knuckle
c.set(23, 12, 'b')               # hand over grip

print(c.stats_text())
print(c.matrix_text())

finish(c)
