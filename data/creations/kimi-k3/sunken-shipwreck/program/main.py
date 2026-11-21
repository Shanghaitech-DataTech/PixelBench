import math

# ---------- palette ----------
WATER = ['#2f88c4', '#2a7cb8', '#256faa', '#20629c',
         '#1b558e', '#164880', '#123c72', '#103368']
RAY1 = '#5aa3d6'
RAY2 = '#6fb3df'
SPARK = '#8fc6e8'
BUB = '#bfe2f2'
BUB2 = '#e8f6ff'

SAND = '#cba96b'
SAND_L = '#e0c488'
SAND_D = '#a3854d'
SAND_SH = '#8a6c3e'
ROCK = '#7a7a72'
ROCK_D = '#5a5a54'

HULL_D = '#3a2415'
HULL_M = '#6b4426'
HULL_L = '#8f6136'
HULL_RIM = '#b0824a'
CORR = '#4f7a5a'
CORR2 = '#6a9a6f'
SAIL = '#8b9078'
SAIL_D = '#5f6b58'
RIG = '#241609'
PORT = '#16232c'
GLOW = '#e6c25c'

FISH = '#f2a03d'
FISH_D = '#cf7d27'
SILV = '#dfe4d8'
SILV_D = '#b8bfae'
EYE = '#ffffff'

COR_P = '#e06a8a'
COR_PL = '#f091ab'
COR_PD = '#b04a68'
COR_O = '#e07840'
COR_OL = '#f09a5c'
COR_OD = '#a5501f'
WEED = '#2e8a5a'
WEED_L = '#46b273'
WEED_D = '#1d6a42'

c = new_canvas(64, 64, name='sunken-shipwreck')

# ---------- 1. water gradient ----------
for y in range(64):
    c.rect(0, y, 64, 1, WATER[min(y // 8, 7)])

# surface sparkles
for x, y in [(5, 0), (20, 1), (35, 0), (50, 1), (60, 0), (12, 1), (44, 0)]:
    c.set(x, y, SPARK)

# ---------- 2. light rays ----------
c.poly([(9, 0), (17, 0), (33, 40), (27, 42)], RAY1)
c.poly([(30, 0), (35, 0), (49, 36), (44, 38)], RAY2)
c.poly([(52, 0), (56, 0), (63, 22), (60, 24)], RAY1)

# ---------- 3. sand dunes (back dark, front light) ----------
for x in range(64):
    t = 48 + round(1.5 * math.sin(x / 5.0 + 2))
    c.rect(x, t, 1, 64 - t, SAND_D)
for x in range(64):
    t = 51 + round(1.5 * math.sin(x / 6.0))
    c.rect(x, t, 1, 64 - t, SAND)

# ---------- 4. ship hull ----------
hull_pts = [(11, 45), (13, 42), (20, 40), (34, 37), (46, 34), (52, 34),
            (55, 38), (55, 46), (52, 52), (40, 55), (22, 55), (14, 52), (11, 48)]
c.poly(hull_pts, HULL_M)

# shading pass over the hull silhouette
hm = c.color(HULL_M); hd = c.color(HULL_D); hl = c.color(HULL_L); hr = c.color(HULL_RIM)
hullish = (hm, hd, hl, hr)
for y in range(33, 57):
    for x in range(10, 57):
        if c.get(x, y) != hm:
            continue
        above = c.get(x, y - 1)
        below = c.get(x, y + 1) if y < 63 else hm
        r = (x * 13 + y * 29) % 37
        if above not in hullish:
            c.set(x, y, HULL_RIM)          # sun-lit deck rim
        elif below not in hullish:
            c.set(x, y, HULL_D)            # keel shadow edge
        elif y >= 51:
            c.set(x, y, HULL_D)            # buried lower strakes
        elif y in (41, 45, 49):
            c.set(x, y, HULL_D)            # plank seams
        elif r == 0:
            c.set(x, y, CORR2)             # corrosion patches
        elif r <= 2:
            c.set(x, y, CORR)

# stern castle
c.rect(47, 29, 8, 7, HULL_M)
for x in range(47, 55):
    c.set(x, 29, HULL_L)
for x in (47, 49, 51, 53):
    c.set(x, 28, HULL_M)
c.rect(49, 31, 3, 3, PORT)
c.set(50, 32, GLOW)

# ---------- 5. masts, yards, sails, rigging ----------
for y in range(14, 39):                    # main mast (leans left)
    mx = 30 - (38 - y) // 9
    c.set(mx, y, HULL_D); c.set(mx + 1, y, HULL_M)
c.set(28, 13, HULL_D); c.set(28, 12, HULL_D); c.set(29, 13, HULL_M)

for y in range(30, 41):                    # fore mast stump
    fx = 16 - (40 - y) // 10
    c.set(fx, y, HULL_D); c.set(fx + 1, y, HULL_M)
c.set(15, 29, HULL_D)

for y in range(20, 35):                    # mizzen mast
    mz = 49 - (34 - y) // 12
    c.set(mz, y, HULL_D); c.set(mz + 1, y, HULL_M)
c.set(48, 19, HULL_D)

c.line(18, 22, 40, 18, HULL_D)             # yards
c.line(10, 33, 21, 31, HULL_D)
c.line(42, 25, 54, 23, HULL_D)

# tattered sails (two torn patches + rags)
p1 = [(21, 22), (30, 21), (28, 28), (23, 29)]
c.poly(p1, SAIL); c.poly(p1, SAIL_D, fill=False)
p2 = [(32, 20), (38, 19), (36, 27), (33, 26)]
c.poly(p2, SAIL); c.poly(p2, SAIL_D, fill=False)
c.poly([(11, 33), (19, 32), (17, 37), (13, 36)], SAIL_D)
p4 = [(44, 25), (52, 24), (50, 30), (46, 29)]
c.poly(p4, SAIL); c.poly(p4, SAIL_D, fill=False)

# rigging + bowsprit
c.line(28, 13, 12, 44, RIG)
c.line(28, 13, 50, 28, RIG)
c.line(15, 30, 11, 45, RIG)
c.line(48, 20, 55, 38, RIG)
c.line(12, 43, 5, 38, HULL_D)
c.set(4, 37, HULL_D)

# ---------- 6. hull details ----------
for x in (20, 27, 34, 41):                 # portholes
    c.rect(x, 46, 2, 2, PORT)
c.set(34, 46, GLOW)                        # one still glowing
for x, y in [(24, 49), (25, 49), (26, 49), (24, 50), (25, 50), (26, 50), (27, 50)]:
    c.set(x, y, PORT)                      # damage hole
for x, y in [(18, 44), (43, 41), (31, 43), (50, 39), (37, 45)]:
    c.set(x, y, SAND_L)                    # barnacles

# ---------- 7. front sand mound (buries the keel) ----------
c.poly([(4, 63), (4, 56), (10, 53), (18, 55), (26, 52), (34, 55),
        (42, 52), (50, 55), (58, 53), (63, 56), (63, 63)], SAND)

sand_i = c.color(SAND)
for x in range(64):                        # sun-lit sand crests
    for y in range(40, 64):
        if c.get(x, y) == sand_i and c.get(x, y - 1) != sand_i:
            c.set(x, y, SAND_L)
            break
for y in range(48, 64):                    # speckles
    for x in range(64):
        if c.get(x, y) == sand_i and (x * 11 + y * 7) % 31 == 0:
            c.set(x, y, SAND_D)
for x in range(16, 51):                    # shadow under the hull
    for y in (55, 56):
        if c.get(x, y) in (sand_i, c.color(SAND_L)):
            c.set(x, y, SAND_SH)

# ---------- 8. seaweed ----------
def weed(x, y0, h, c1, c2):
    pat = [0, 0, 1, 1, 0, 0, -1, -1]
    for i in range(h):
        c.set(x + pat[i % 8], y0 - i, c1 if i % 3 else c2)

weed(6, 54, 7, WEED, WEED_L)
weed(8, 55, 9, WEED_D, WEED)
weed(11, 54, 6, WEED, WEED_L)
weed(61, 54, 8, WEED_D, WEED)
weed(62, 53, 6, WEED, WEED_L)
weed(25, 48, 4, WEED_D, WEED)              # growing from the damage hole
weed(33, 37, 5, WEED_D, WEED_L)            # encrusted on the deck

# ---------- 9. corals, rocks, starfish ----------
coral = [
    "....L.",
    "...Lp.",
    "d.pL..",
    ".p..pL",
    "dp..p.",
    ".pL.p.",
    "..pp..",
    "..pd..",
    "..p...",
]
cmap = {'p': COR_P, 'L': COR_PL, 'd': COR_PD}
for j, row in enumerate(coral):
    for i, ch in enumerate(row):
        if ch in cmap:
            c.set(54 + i, 45 + j, cmap[ch])
c.set(57, 54, COR_P)

c.rect(5, 50, 3, 5, COR_O)                 # tube corals
c.set(5, 50, COR_OL); c.set(7, 50, COR_OL); c.set(6, 50, COR_OD)
c.rect(9, 51, 2, 4, COR_O); c.set(9, 51, COR_OL)
c.rect(3, 52, 2, 3, COR_O); c.set(3, 52, COR_OL)

for x, y, col in [(43, 53, ROCK), (44, 52, ROCK), (45, 53, ROCK),
                  (44, 53, ROCK_D), (20, 55, ROCK), (21, 55, ROCK_D)]:
    c.set(x, y, col)

for x, y in [(36, 58), (35, 58), (37, 58), (36, 57), (36, 59)]:
    c.set(x, y, COR_O)                     # starfish
c.set(36, 58, COR_OL)

# ---------- 10. fish ----------
SMALL = [".bb.t.", "ebbbtt", ".bb.t."]
MED = ["..bbb...", ".bbbbbtt", "ebbbbbt.", ".bbbbbtt", "..bbb..."]

def sprite(x, y, rows, cmap):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch in cmap:
                c.set(x + i, y + j, cmap[ch])

fs = {'b': FISH, 't': FISH_D, 'e': EYE}
sv = {'b': SILV, 't': SILV_D, 'e': EYE}
for x, y in [(6, 8), (14, 13), (22, 7), (30, 12), (10, 19), (18, 17),
             (38, 9), (52, 6), (58, 10)]:
    sprite(x, y, SMALL, fs)
sprite(46, 13, MED, fs)
sprite(4, 34, MED, sv)

# ---------- 11. bubbles ----------
c.circle(36, 38, 1, BUB, fill=False)
c.circle(39, 30, 1, BUB, fill=False)
c.circle(36, 23, 2, BUB, fill=False)
c.set(38, 17, BUB)
c.set(40, 13, BUB2)
c.set(35, 34, BUB2)

print(c.stats_text())
view(c)
finish(c)
