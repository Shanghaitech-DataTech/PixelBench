try:
    from pixelbench_api import *
except Exception:
    pass

import math

W = H = 64
c = new_canvas(W, H, background=None, name="mad-cyborg-scientist")

# ---------------------------------------------------------------- palette
PAL = {
    'H': "#f2f6fa", 'h': "#c8d2de", 'n': "#93a0b0", 'N': "#5f6b7a",   # hair
    'S': "#f4c9a0", 's': "#e2ab80", 't': "#c2855c", 'T': "#9c6440", 'u': "#6e4530",  # skin
    'M': "#c9d4e2", 'm': "#9aa7b6", 'e': "#6d7987", 'E': "#434c59", 'D': "#272e38",  # metal
    'R': "#ff6a3c", 'r': "#e03418", 'o': "#8a1a0c", 'O': "#451009", 'Y': "#b85426",  # eye glow
    'W': "#f6f3e6", 'w': "#d0cab4", 'K': "#2b1310",                  # teeth / mouth
    'P': "#cf9142", 'p': "#83551f", 'C': "#2b323d", 'c': "#4d5867",  # plugs / cables
    'A': "#8f6a45", 'a': "#6d4c30", 'z': "#47301d",                  # leather apron
    'L': "#e9eef4", 'l': "#c2cad4", 'x': "#939dab", 'X': "#5f6875",  # lab coat
    'G': "#7d6b4a", 'B': "#4c3726", 'b': "#6f5236", 'V': "#aab4c1",  # grime / belt
    'J': "#97a2b0",
}
IDX = {}
for k, v in PAL.items():
    IDX[k] = c.color(v)

# ---------------------------------------------------------------- background
BG_RAMP = ["#05070c", "#0d1420", "#16202f", "#212e44"]
bg = [c.color(h) for h in BG_RAMP]
WARM = c.color("#2a1013")


def bayer(x, y):
    return ((x % 2) * 2 + (y % 2)) / 4.0


for y in range(H):
    for x in range(W):
        d = math.hypot(x - 32.0, (y - 22.0) * 1.25)
        v = 1.0 - d / 36.0
        v = 0.0 if v < 0 else (0.999 if v > 0.999 else v)
        i = int(v * 3.0 + bayer(x, y) * 0.85)
        c.set(x, y, bg[min(i, 3)])

# warm ambient bleed behind the robotic half of the head
for y in range(H):
    for x in range(W):
        d = math.hypot(x - 40.0, (y - 19.0) * 1.1)
        if d < 13.0:
            v = 1.0 - d / 13.0
            if v * 1.3 + bayer(x, y) * 0.6 > 0.85:
                c.set(x, y, WARM)

# ---------------------------------------------------------------- pixel map
MAP = [
    # y=0..2
    "." * 64,
    "." * 64,
    "." * 64,
    # y=3  cable bundle arcing away to the right
    "." * 32 + "C" * 19 + "." * 13,
    # y=4
    "." * 24 + "h" + "C" * 14 + "." * 12 + "C" * 6 + "." * 7,
    # y=5
    "." * 25 + "C" + "hh" + "HHH" + "PP" + "hhh" + "CCC" + "." * 16 + "C" * 6 + "." * 3,
    # y=6
    "." * 22 + "hhh" + "CC" + "hhhh" + "PP" + "hhhh" + "CC" + "h" + "." * 18 + "C" * 6,
    # y=7
    "." * 20 + "hhhhh" + "PP" + "hhhh" + "pp" + "hhhh" + "PP" + "hhhhhh" + "." * 8 + "CCCCCC" + "." * 5,
    # y=8
    "." * 19 + "hhhhhh" + "pp" + "hhhhhhhhhh" + "pp" + "hhhhhhh" + "." * 18,
    # y=9
    "." * 18 + "nnnn" + "hhhhhhhhh" + "NN" + "hhhhhhhh" + "nnnnn" + "." * 18,
    # y=10
    "." * 18 + "nnn" + "hhhhh" + "HHHH" + "hhhh" + "HHHHH" + "hhhhh" + "nn" + "." * 18,
    # y=11  hairline / forehead
    "." * 18 + "nn" + "hhh" + "SSS" + "sssss" + "NN" + "mmmmmmmm" + "eee" + "nn" + "." * 18,
    # y=12
    "." * 20 + "nn" + "hh" + "SSSS" + "ssss" + "EE" + "mmmmmmmmmm" + "nn" + "." * 18,
    # y=13
    "." * 20 + "nn" + "h" + "SS" + "T" + "ssssss" + "EE" + "mmmmmmmmmm" + "nn" + "." * 18,
    # y=14  brow ridge + glow above the lens
    "." * 20 + "nn" + "h" + "s" + "TTTTTT" + "ss" + "EE" + "m" + "OOOOOO" + "m" + "e" + "E" + "nn" + "." * 18,
    # y=15
    "." * 20 + "nn" + "h" + "s" + "TTTTTT" + "ss" + "EEEEEEEEEE" + "e" + "E" + "nn" + "." * 18,
    # y=16  eye housings
    "." * 20 + "nn" + "h" + "s" + "uuuuuu" + "ss" + "EE" + "oooooooo" + "EE" + "nn" + "." * 18,
    # y=17
    "." * 20 + "nn" + "h" + "s" + "WW" + "KK" + "W" + "u" + "ss" + "EE" + "o" + "rrrrr" + "o" + "EEE" + "nn" + "." * 18,
    # y=18
    "." * 20 + "nn" + "h" + "s" + "ww" + "KK" + "w" + "t" + "ss" + "EE" + "o" + "r" + "RRR" + "r" + "o" + "EEE" + "nn" + "." * 18,
    # y=19
    "." * 20 + "nn" + "h" + "s" + "tttttt" + "ss" + "EE" + "oooooooo" + "EE" + "nn" + "." * 18,
    # y=20  glow spilling under the lens
    "." * 20 + "nn" + "h" + "ssssss" + "t" + "ss" + "EE" + "OOOOOOOO" + "EE" + "nn" + "." * 18,
    # y=21  cheek plates + rivets
    "." * 20 + "nn" + "h" + "sssssss" + "tt" + "E" + "mmVmmmVmm" + "e" + "E" + "nn" + "." * 18,
    # y=22
    "." * 20 + "nn" + "h" + "ssssss" + "t" + "tt" + "E" + "mmYmmmYmm" + "e" + "E" + "nn" + "." * 18,
    # y=23  nose / panel seam
    "." * 20 + "nn" + "h" + "ss" + "T" + "ssss" + "tt" + "E" + "mmmm" + "e" + "mmmm" + "e" + "E" + "nn" + "." * 18,
    # y=24
    "." * 20 + "nn" + "h" + "ss" + "T" + "ssss" + "tt" + "E" + "mmmm" + "e" + "mmmm" + "e" + "E" + "nn" + "." * 18,
    # y=25
    "." * 20 + "nn" + "h" + "ssssss" + "t" + "TT" + "E" + "mmmm" + "e" + "mmmm" + "e" + "E" + "nn" + "." * 18,
    # y=26  nostril
    "." * 20 + "nn" + "h" + "sssss" + "t" + "T" + "K" + "T" + "E" + "mmmm" + "e" + "mmmm" + "e" + "E" + "nn" + "." * 18,
    # y=27
    "." * 20 + "nn" + "h" + "ssssss" + "t" + "ss" + "E" + "mmmm" + "e" + "mmmm" + "e" + "E" + "nn" + "." * 18,
    # y=28  upper lip / metal lip plate
    "." * 20 + "nn" + "h" + "ss" + "TTTTTTT" + "E" + "EEEEEE" + "e" + "mmm" + "E" + "nn" + "." * 18,
    # y=29  the grin
    "." * 20 + "nn" + "h" + "ss" + "K" + "WWWWWWWWWWWWW" + "K" + "mmm" + "E" + "nn" + "." * 18,
    # y=30
    "." * 20 + "nn" + "h" + "ss" + "K" + "KK" + "wwwwwwwww" + "KKK" + "mmm" + "E" + "nn" + "." * 18,
    # y=31  lower lip
    "." * 20 + "nn" + "h" + "ss" + "ttttttt" + "E" + "eeeeee" + "E" + "mmm" + "E" + "nn" + "." * 18,
    # y=32  chin / metal jaw
    "." * 20 + "nn" + "h" + "sssssssss" + "E" + "mmmmmm" + "e" + "mmm" + "E" + "nn" + "." * 18,
    # y=33
    "." * 21 + "nn" + "ttt" + "sssss" + "t" + "E" + "mmmmmm" + "e" + "mm" + "E" + "n" + "." * 20,
    # y=34
    "." * 22 + "nn" + "ttt" + "ssss" + "t" + "E" + "mmmmm" + "e" + "EE" + "nn" + "." * 21,
    # y=35  jaw underside
    "." * 24 + "nn" + "tttt" + "T" + "E" + "EEEEE" + "D" + "nn" + "." * 24,
    # y=36  neck
    "." * 26 + "nn" + "ttt" + "T" + "E" + "eee" + "E" + "n" + "." * 26,
    # y=37
    "." * 26 + "nn" + "ttt" + "T" + "E" + "ee" + "E" + "D" + "n" + "." * 26,
    # y=38  collar bolt
    "." * 26 + "nn" + "TTTT" + "E" + "V" + "ee" + "E" + "n" + "." * 26,
    # y=39
    "." * 25 + "nn" + "TTTTT" + "E" + "EEE" + "D" + "nn" + "." * 25,
    # y=40  collar rises
    "." * 22 + "xxx" + "nn" + "TTTTT" + "E" + "EEEE" + "D" + "xxx" + "XX" + "." * 21,
    # y=41
    "." * 18 + "xxxx" + "LLLLL" + "TTTTT" + "E" + "EEEE" + "D" + "LLLLL" + "llll" + "xx" + "." * 15,
    # y=42
    "." * 14 + "xxxx" + "LLLLLLLL" + "l" + "TTTTT" + "E" + "EEEE" + "D" + "LLLLLLLL" + "lllll" + "xx" + "." * 11,
    # y=43
    "." * 12 + "xx" + "LLLLLLLLLL" + "lll" + "TTTTT" + "E" + "EEEE" + "D" + "LLLL" + "llllll" + "xxxxx" + "." * 11,
    # y=44  shoulders, metal shoulder cap appears right
    "." * 10 + "xx" + "L" * 11 + "lll" + "XXXX" + "D" * 6 + "XXX" + "LLLLL" + "lll" + "MMM" + "mmmmm" + "ee" + "." * 7,
    # y=45
    "." * 9 + "xx" + "L" * 11 + "lll" + "XXXX" + "D" * 9 + "LLLLL" + "l" + "MM" + "mmmmm" + "ee" + "E" + "." * 10,
    # y=46
    "." * 8 + "xx" + "L" * 11 + "lll" + "XXXX" + "D" * 9 + "LLLLL" + "ll" + "MMMM" + "mmmmmm" + "ee" + "E" + "." * 7,
    # y=47
    "." * 8 + "xx" + "L" * 10 + "lll" + "XXXX" + "D" * 9 + "LLLLL" + "ll" + "MMMM" + "mmmmmmm" + "eee" + "EE" + "." * 5,
    # y=48  apron bib top
    "." * 8 + "xx" + "L" * 9 + "lll" + "XX" + "A" * 16 + "XX" + "l" + "MMMM" + "mmmmmmm" + "ee" + "EE" + "." * 6,
    # y=49
    "." * 8 + "xx" + "L" * 9 + "lll" + "XX" + "aaaa" + "GG" + "aaaa" + "G" + "aaaaa" + "XX" + "l" + "MMMMM" + "mmmmmm" + "ee" + "EE" + "." * 6,
    # y=50
    "." * 7 + "xx" + "L" * 9 + "lll" + "XX" + "aaaaa" + "GG" + "aaaaaa" + "G" + "aaaa" + "XX" + "l" + "MMMMM" + "mmmmmm" + "ee" + "E" + "." * 6,
    # y=51
    "." * 7 + "xx" + "L" * 9 + "lll" + "XX" + "aaaaa" + "GG" + "aaaaaa" + "G" + "aaaa" + "XX" + "l" + "MMMMM" + "mm" + "c" + "mmm" + "ee" + "E" + "." * 6,
    # y=52  apron pocket
    "." * 7 + "xx" + "L" * 9 + "lll" + "XX" + "aaaa" + "zzzzzzzzzz" + "aaaa" + "XX" + "l" + "MMMMM" + "mm" + "c" + "mmm" + "ee" + "E" + "." * 6,
    # y=53  tools in the pocket
    "." * 7 + "xx" + "L" * 9 + "lll" + "XX" + "aaaa" + "z" + "aaa" + "J" + "aa" + "J" + "a" + "z" + "aaaa" + "XX" + "l" + "MMMMM" + "mm" + "c" + "mmm" + "ee" + "E" + "." * 6,
    # y=54  pocket bottom
    "." * 6 + "xx" + "L" * 9 + "lll" + "XX" + "aaaa" + "z" * 12 + "aaaa" + "XX" + "MMMMM" + "mmmmmm" + "ee" + "EE" + "." * 5,
    # y=55  tool belt
    "." * 6 + "xx" + "BBBB" + "bbbbbbbb" + "B" * 10 + "VVVVV" + "B" * 9 + "MMMMM" + "mmmmmm" + "ee" + "EE" + "." * 5,
    # y=56
    "." * 6 + "xx" + "BBBB" + "bbbbbbbb" + "B" * 10 + "VVVVV" + "B" * 9 + "MMMMM" + "mmmmmm" + "ee" + "EE" + "." * 5,
    # y=57
    "." * 6 + "xx" + "BBBB" + "bbbbbbbb" + "B" * 10 + "VVVVV" + "B" * 9 + "MMMMM" + "mmmmmm" + "ee" + "EE" + "." * 5,
    # y=58  apron skirt / forearm
    "." * 6 + "xx" + "l" * 14 + "aaaaaa" + "z" + "aaaaaaaa" + "z" + "aaaa" + "xxx" + "MMMM" + "mmmmmmm" + "ee" + "E" + "." * 5,
    # y=59
    "." * 6 + "xx" + "l" * 14 + "aaaaaa" + "z" + "aaaaaaaa" + "z" + "aaaa" + "xxx" + "MMMM" + "mmmmmmm" + "ee" + "E" + "." * 5,
    # y=60  wrist cable
    "." * 6 + "xx" + "l" * 14 + "aaaaaa" + "z" + "aaaaaaaa" + "z" + "aaaa" + "xxx" + "MMM" + "mm" + "C" + "mmmmmm" + "ee" + "EE" + "." * 3,
    # y=61  prosthetic fingers
    "." * 6 + "xx" + "l" * 14 + "aaaaaa" + "z" + "aaaaaaaa" + "z" + "aaaa" + "xxx" + "MM" + "mmm" + "C" + "m" + "E" + "m" + "E" + "m" + "E" + "m" + "e" + "E" + "." * 4,
    # y=62
    "." * 6 + "xx" + "l" * 14 + "aaaaaa" + "z" + "aaaaaaaa" + "z" + "aaaa" + "xxx" + "MM" + "mmm" + "C" + "m" + "E" + "m" + "E" + "m" + "E" + "m" + "e" + "E" + "." * 4,
    # y=63  bottom edge
    "." * 6 + "XX" + "x" * 14 + "z" * 20 + "XXX" + "EE" + "eee" + "C" + "ee" + "EE" + "ee" + "EE" + "D" + "." * 4,
]

for y, row in enumerate(MAP):
    if len(row) != W:
        raise SystemExit("row %d has length %d (want %d)" % (y, len(row), W))
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, IDX[ch])

# ---------------------------------------------------------------- finishing touches
# hard rim light down the lit left edge of the coat
for y, x in [(46, 8), (47, 8), (48, 8), (49, 8), (50, 7), (51, 7), (52, 7), (53, 7),
             (54, 6), (55, 6), (56, 6), (57, 6), (58, 6), (59, 6), (60, 6), (61, 6), (62, 6)]:
    c.set(x, y, IDX['L'])

# dried stains on the coat
for x, y in [(10, 50), (15, 50), (13, 51), (16, 52), (10, 53), (12, 58), (18, 59),
             (15, 60), (41, 44), (40, 45), (38, 46)]:
    c.set(x, y, IDX['G'])

# floating sparks / motes in the glow
for x, y, col in [(13, 15, 'R'), (11, 22, 'Y'), (15, 29, 'R'), (51, 27, 'R'),
                  (53, 33, 'Y'), (49, 9, 'R'), (9, 36, 'Y'), (54, 20, 'R')]:
    c.set(x, y, IDX[col])
for x, y in [(12, 16), (14, 28), (52, 28), (50, 10)]:
    c.set(x, y, IDX['o'])

# lens glow bleeding onto the hair beside the housing
for x, y in [(44, 16), (44, 17), (45, 17), (44, 18), (45, 18)]:
    c.set(x, y, IDX['O'])

# metal speculars
for x, y in [(35, 12), (36, 12), (34, 13), (34, 32), (35, 32), (46, 45), (48, 46)]:
    c.set(x, y, IDX['M'])

# skin light + core shadow on the human half
for x, y in [(24, 22), (25, 22), (23, 25), (24, 25)]:
    c.set(x, y, IDX['S'] if y == 22 else IDX['t'])

print(c.stats_text())
if c.stats()["colors_used"] > 86:
    raise SystemExit("too many colours: %d" % c.stats()["colors_used"])
finish(c)
