from pixelbench_api import *

# Palette
CHARS = {
    'H': '#f2ead2',  # bone highlight
    'B': '#d8cfb2',  # bone
    'b': '#a89f86',  # bone shadow
    'J': '#4c463a',  # dark joint shading
    'D': '#26221a',  # deep dark (sockets/outline)
    'E': '#d8402a',  # eye glow
    'S': '#c4cad2',  # steel
    's': '#7a808a',  # steel shadow
    'h': '#6a4a28',  # hilt / grip
    'W': '#9a6a38',  # wood
    'w': '#5e3f22',  # wood dark
    'R': '#8a8f98',  # shield rim
}

GRID = [
    "................................",  # 0
    "................................",  # 1
    ".........................S......",  # 2  sword tip
    "........HHBB............sS......",  # 3  skull top (juts left = hunch)
    ".......HBBBBb..........sS.......",  # 4
    ".......BBBBBBb........sS........",  # 5
    ".......BDEBDEb.......sS.........",  # 6  glowing eye sockets
    ".......BBBDBBb......sS..........",  # 7  nose hole
    ".......bBDBDBb....hhhhhh........",  # 8  teeth + crossguard
    "........bBBBbJ.....BBB..........",  # 9  jaw, neck joint, fist
    ".........bBBJJBBbBBbhh..........",  # 10 clavicle, shoulder, forearm, pommel
    ".....RRRBbBBJJBBbBJ.............",  # 11 shield top, left arm, ribs, shoulder J
    "....RWWWRb..JJ..bb..............",  # 12 rib gap, spine, back curve
    "...RWwWwWRBBJJBBbb..............",  # 13 rib bar 2
    "...RWWDWWRb.JJ..bb..............",  # 14 shield boss
    "...RWwWwWRBBJJBBbb..............",  # 15 rib bar 3
    "....RWWWR..bJJb.................",  # 16 lower ribs
    ".....RRR..bBJJBBb...............",  # 17 shield bottom, pelvis
    "..........bJB.BJb...............",  # 18 hips (joints)
    "...........BB.BB................",  # 19 thighs
    "...........Bb.Bb................",  # 20
    "...........BB.BB................",  # 21
    "...........Bb.Bb................",  # 22
    "...........JJ.JJ................",  # 23 knees
    "...........Bb.Bb................",  # 24 shins
    "...........BB.BB................",  # 25
    "...........Bb.Bb................",  # 26
    "...........J...J................",  # 27 ankles
    ".........BBBb.bBBB..............",  # 28 feet
    ".........bbbb.bbbb..............",  # 29 foot shadow
    "................................",  # 30
    "................................",  # 31
]

c = new_canvas(32, 32, background=None, name="skeleton_grunt")
for y, row in enumerate(GRID):
    assert len(row) == 32, (y, len(row))
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, CHARS[ch])

print(c.stats_text())
view(c)
finish(c)
