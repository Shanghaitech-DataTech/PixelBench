from pixelbench_api import *

# ---------- Palette code mapping (reusing input palette by hex so frame 2 stays on-style) ----
# We simply reuse input_canvas palette via input copy; we draw using hex values directly.
PAL = {
 'a': '#422110',  # dark brown outline
 'b': '#7b4231',  # brown
 'c': '#c5956a',  # skin
 'd': '#ffffffff',# white
 'e': '#949473',
 'f': '#f3f4b6',
 'g': '#ffe75a',  # gold
 'h': '#c30074',  # pink hair
 'i': '#df9859',
 'j': '#55002a',  # dark pink hair
 'k': '#ef5ba1',  # pink hair
 'u': '#9e005d',
 'w': '#f6adcd',
 'v': '#529439',  # green leaf
 'x': '#304915',
 'z': '#9cde5a',
 'D': '#4f7229',
 'B': '#252a23',  # outfit dark green
 't': '#121311',  # black outline
 'y': '#14110e',
 'K': '#74341c',  # bow wood
 'A': '#bc6c0c',
 'L': '#48382f',
 'M': '#313b31',
 'E': '#3c3c3c',
 'F': '#687862',  # gray-green
 'G': '#a4b496',
 'N': '#5d422f',
 'O': '#d1b6a2',
 'P': '#170035',   # shadow/translucent
}
# map to actual registered colors from input palette
CM = {ch: input_canvas.color(hexv) for ch, hexv in PAL.items()}

# Frame 1: exact original content (35x47)
f1 = input_canvas.copy(name='f1')

# ---------- FRAME 2: full draw ----------
# Design: elf (pink hair), RIGHT-facing, bow held forward, string pulled fully back to the cheek.
# Grid is 44 wide x 47 tall. Elf stands left, bow in L-hand (arm extended RIGHT), R-hand at cheek,
# bow limbs curved "C" fully open, braced stance.
W, H = 44, 47
f2 = new_canvas(W, H)
g = {}
ROWS = []
def R(s):
    r = list(s)
    if len(r) < W: r += '.' * (W - len(r))
    assert len(r) == W, (len(r), s)
    ROWS.append(r)
h_rows = [
"....hhhhhhhhhhh................................",
"...hhhhhhhhhhh............................",
]
