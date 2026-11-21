from pixelbench_api import *

out = input_canvas.copy(name='output')

K = '#2e1f12'          # existing dark outline
WHITE = '#ffffff'      # background
WL = '#d89b6a'         # wood light
WM = '#96613a'         # wood mid
WD = '#6b4423'         # wood dark
GOLD_L = '#e8d071'
GOLD_M = '#c9a227'
GOLD_D = '#8a6c14'
GEM_L = '#bff2ff'
GEM_M = '#4fbfe8'
GEM_D = '#1d6f9c'

# ---------------- 1. erase the sword ----------------
# gold cross-guard and its outlines (rows 39-40, x40..x46)
for y in (39, 40):
    for x in range(40, 47):
        out.set(x, y, WHITE)
# blade (rows 41-54, x41..x45)
for y in range(41, 55):
    for x in range(41, 46):
        out.set(x, y, WHITE)
# blade tip
out.set(43, 55, WHITE)
# the little grip sliver peeking under the fist
out.set(43, 38, K)


# ---------------- 2. draw the staff ----------------
def shaft(y):
    out.set(42, y, K)
    out.set(43, y, WL)
    out.set(44, y, WM)
    out.set(45, y, WD)


# wooden shaft: above the fist (rows 25-34) and below it (rows 39-55)
for y in range(25, 35):
    shaft(y)
for y in range(39, 56):
    shaft(y)
# right edge of the shaft stays visible beside the fist
for y in range(35, 39):
    out.set(45, y, WD)

# gold bands
for y in (23, 24, 53, 54):
    out.set(42, y, K)
    out.set(43, y, GOLD_L)
    out.set(44, y, GOLD_M)
    out.set(45, y, GOLD_D)

# dark foot of the staff
out.set(42, 55, K)
out.set(43, 55, WD)
out.set(44, 55, WD)
out.set(45, 55, K)

# crystal head (ellipse, 7 rows tall)
gem = {
    16: [(43, K), (44, K)],
    17: [(42, K), (43, GEM_L), (44, GEM_M), (45, K)],
    18: [(41, K), (42, GEM_L), (43, GEM_L), (44, GEM_M), (45, GEM_M), (46, K)],
    19: [(41, K), (42, GEM_L), (43, GEM_M), (44, GEM_M), (45, GEM_D), (46, K)],
    20: [(41, K), (42, GEM_M), (43, GEM_M), (44, GEM_D), (45, GEM_D), (46, K)],
    21: [(42, K), (43, GEM_M), (44, GEM_D), (45, K)],
    22: [(43, K), (44, K)],
}
for y, px in gem.items():
    for x, col in px:
        out.set(x, y, col)
# specular sparkle on the crystal
out.set(42, 18, WHITE)

print(out.stats_text())

name = {0:'.',1:'W',2:'K',3:'D',4:'R',5:'F',6:'G',7:'H',8:'I',9:'S',10:'J',11:'L',12:'M',
        13:'N',14:'O',15:'P',16:'Q',17:'R',18:'$',19:'t',20:'u',21:'v',22:'a',23:'b',
        24:'c',25:'d',26:'e',27:'f',28:'*',29:'%',30:'g',31:'C',32:'B'}
for y in range(0, 64):
    print(f"{y:2d} " + "".join(name[out.get(x, y)] for x in range(0, 64)))

finish(out)
