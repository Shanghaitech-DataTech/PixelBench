from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
# Print a custom char grid: map id -> char
m = {
    0: '.',
    1: '#',   # dark outline
    2: 'b',   # gray
    3: 'C',   # cream
    4: 'd',   # brown3
    5: 'e',   # gray2
    6: 'f',   # darkred
    7: 'g',   # brown (weapon?)
    8: 'h',   # maroon
    9: 'i',   # magenta
    10: '$',  # gold j
    11: 'k',  # darkred2
    12: 'l',  # pink2
    13: 'm',  # pink3
    14: 'n',  # magenta
    15: 'o',  # gray3
    16: 'p',  # gray4
    17: 'q',  # darkmag
    18: 'r',  # light
    19: 's',  # brown2
    20: 't',  # pale
    21: 'u',  # dark
    22: '$',  # gold v
    23: 'w',  # tan
    24: 'x',  # skin2
    25: '$',  # yellow y
    26: 'z',  # tan2
    27: 'A',  # brown
    28: 'S',  # skin B
    29: 'C',  # dark3
    30: 'D',  # olive
    31: 'W',  # white
    32: '$',  # lightgold F
    33: 'G',  # olive2
    34: 'H',  # red-brown
    35: 'I',  # pink
    36: 'J',  # cream2
    37: 'K',  # dark4
    38: 'L',  # darkmag2
    39: 'M',  # dark
    40: '$',  # gold N
    41: 'O',  # shadow
}
for y in range(h):
    row = ''.join(m.get(c.get(x,y), '?') for x in range(w))
    print(f"{y:02d} {row}")
