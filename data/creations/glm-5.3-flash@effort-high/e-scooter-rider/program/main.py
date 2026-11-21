# e-scooter-rider: 32x32 pixel art, side view riding right

W, H = 32, 32

COLORS = {
    "H": "#e04848",  # helmet
    "h": "#f28c8c",  # helmet highlight
    "S": "#f2c79a",  # skin
    "E": "#2b2b2b",  # eye
    "B": "#3d7dd8",  # shirt
    "b": "#2c5ca8",  # shirt shade
    "P": "#3a4668",  # pants
    "K": "#23252b",  # shoes
    "G": "#37b3a8",  # deck teal
    "D": "#2a8a82",  # deck underside
    "T": "#8a919c",  # stem / fork
    "W": "#26282e",  # wheel tyre
    "w": "#6e7683",  # wheel hub
    "g": "#1e1f24",  # handlebar grip
    "L": "#b9c2cc",  # motion lines
    "R": "#8a93a0",  # ground dashes
}

MAP = [
    "................................",  # 0
    "................................",  # 1
    "................................",  # 2
    "................................",  # 3
    "................................",  # 4
    "....................HHH.........",  # 5  helmet dome
    "...................HhHHH........",  # 6
    "...................HHHSS........",  # 7  face front
    "...................HHSES........",  # 8  eye
    ".....................SS.........",  # 9  chin
    "....................BB..........",  # 10 shoulders
    "....................BbBB........",  # 11 torso + upper arm
    "...................BB.BSgg......",  # 12 arm -> hand -> grip on stem
    "...................BB....T......",  # 13
    "...LLL............BB.....T......",  # 14 motion line
    ".................PP......T......",  # 15 hips
    "................P.P......T......",  # 16 legs
    "....LL..........P.P......T......",  # 17
    "...............P..P......T......",  # 18
    "...............P..P......T......",  # 19
    "...............P..P......T......",  # 20
    "..............P...P......T......",  # 21
    "..............KK..KK.....T......",  # 22 feet on deck
    "..........GGGGGGGGGGGGGGGT......",  # 23 deck top + fork
    ".........DDDDDDDDDDDDDDD.T......",  # 24 deck underside / fender
    ".........WWW.............TWW....",  # 25 wheel tops + fork crown
    "........WWWWW...........WWWWW...",  # 26
    "........WWwWW...........WWwWW...",  # 27 hubs
    "........WWWWW...........WWWWW...",  # 28
    ".........WWW.............WWW....",  # 29
    "....R.R.R.R.R.R.R.R.R.R.R.R.....",  # 30 ground dashes
    "................................",  # 31
]

c = new_canvas(W, H, background=None, name="e-scooter-rider")

for y, row in enumerate(MAP):
    assert len(row) == W, f"row {y} has {len(row)} chars"
    for x, ch in enumerate(row):
        if ch != ".":
            c.set(x, y, c.color(COLORS[ch], name=ch))

print(c.stats_text())
print(c.matrix_text())
finish(c)
