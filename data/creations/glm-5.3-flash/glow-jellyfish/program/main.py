# glow-jellyfish — 16x16 RPG enemy sprite
#
# A small jellyfish glowing in deep water:
#   * dark navy outline (reads against any dungeon background)
#   * white-hot core -> pale aqua -> saturated cyan glow
#   * translucent teal bell skirt where the light thins out
#   * dim halo bleeding into the water above and beside the bell
#   * short curling tentacles, glowing oral arms, frilled underside

from pixelbench_api import *

c = new_canvas(16, 16, background=None, name="glow-jellyfish")

INK    = c.color("#101c3a", name="ink")        # dark outline, deep water
HALO   = c.color("#14586e", name="halo")       # dim glow bleeding into the water
DEEP   = c.color("#1f8fae", name="bell_flesh") # translucent teal bell skirt
GLOW   = c.color("#3ce6d9", name="glow")       # saturated cyan glow
BRIGHT = c.color("#a5ffee", name="bright")     # pale aqua inner glow
CORE   = c.color("#f2fffc", name="core")       # white-hot centre

CHAR = {"O": INK, "G": HALO, "D": DEEP, "C": GLOW, "B": BRIGHT, "W": CORE}

# legend: O outline, G halo, D translucent flesh, C glow, B bright, W hot core
MAP = [
    "................",  # y=0
    "................",  # y=1
    ".......GG.......",  # y=2  halo rising off the dome
    "......OOOO......",  # y=3  dome top
    ".....OCBBCO.....",  # y=4
    "....OCBWWBCO....",  # y=5  white-hot core
    "..GOCBBWWBBCOG..",  # y=6  widest row, halo at the flanks
    "..GODCCCCCCDOG..",  # y=7  translucent skirt appears
    "...ODDCCCCDDO...",  # y=8  skirt narrows
    "....OOOOOOOO....",  # y=9  dark underside rim
    "....ODCBBCDO....",  # y=10 frilled skirt + oral arms
    "...O..CCCC..O...",  # y=11 tentacles drift outward
    "...O...CC...O...",  # y=12
    "....O..CC..O....",  # y=13 tentacle tips curl back in
    "................",  # y=14
    "................",  # y=15
]

# --- sanity checks -----------------------------------------------------------
assert all(len(row) == 16 for row in MAP), "every row must be 16 wide"
for row in MAP:                                   # left/right symmetry
    assert row == row[::-1], f"asymmetric row: {row!r}"

visible = sum(ch in CHAR for row in MAP for ch in row)
assert visible <= 86, f"too many visible pixels: {visible}"

for y, row in enumerate(MAP):
    for x, ch in enumerate(row):
        if ch in CHAR:
            c.set(x, y, CHAR[ch])

print(c.stats_text())
print(c.matrix_text())
print("visible pixels:", visible, "| distinct colours:", len({ch for r in MAP for ch in r if ch in CHAR}))

save("glow-jellyfish", c)
finish(c)
