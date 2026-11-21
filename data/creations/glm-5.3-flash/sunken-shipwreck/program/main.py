from pixelbench_api import *

W = H = 64

# ============================================================ water
bg = new_canvas(W, H, name="water")
for y0, y1, col in [
    (0, 6, "#3f9fdc"), (6, 13, "#3590cf"), (13, 21, "#2c80bf"),
    (21, 30, "#2470ae"), (30, 39, "#1d609c"), (39, 48, "#17518a"),
    (48, 56, "#114376"), (56, 64, "#0d3866"),
]:
    bg.rect(0, y0, W, y1 - y0, col)
bg.rect(0, 0, W, 2, "#5cb4e6")          # surface shimmer

RAY = ["#6cc0ea", "#57b2e2", "#459fd4", "#3a8fc6"]
def ray(x0, drift, n):
    x = x0
    for i in range(n):
        if not (i >= 6 and i % 2):
            bg.rect(x, i * 4, 2 if i < 3 else 1, 3, RAY[min(i // 2, 3)])
        x += drift

for a, b, n in [(9, -1, 9), (21, -1, 8), (33, -1, 10), (45, -1, 8), (56, -1, 7)]:
    ray(a, b, n)

for x, y in [(6,18),(14,26),(24,34),(40,30),(52,24),(58,34),(10,44),(30,44),
             (46,40),(20,8),(36,12),(50,6),(60,14),(4,34),(16,38),(56,44),
             (28,22),(44,26),(12,32),(60,50)]:
    bg.set(x, y, "#a9d4e8")              # marine snow

# ============================================================ wreck
wk = new_canvas(W, H, name="wreck")
WOOD_D, WOOD_M, WOOD_L, WOOD_HL, WOOD_DK = "#5f442a", "#7a5a36", "#93714a", "#a8905f", "#3a2a19"
hull_idx = wk.color(WOOD_D)

# stern block, broken open toward the bow, base buried
wk.poly([(2,46),(3,39),(5,35),(9,32),(15,31),(20,33),(23,37),(25,41),
         (24,45),(26,50),(25,56),(2,56)], WOOD_D)

def row_span(cnv, y, idx):
    xs = [x for x in range(W) if cnv.get(x, y) == idx]
    return (min(xs), max(xs)) if xs else None

def col_span(cnv, x, idx):
    ys = [y for y in range(H) if cnv.get(x, y) == idx]
    return (min(ys), max(ys)) if ys else None

# planking
for y in (36, 39, 42, 45, 48, 51):
    s = row_span(wk, y, hull_idx)
    if s:
        wk.line(s[0], y, s[1], y, WOOD_M)
# exposed frames low on the hull
for x in (6, 11, 16, 21):
    s = col_span(wk, x, hull_idx)
    if s:
        wk.line(x, max(s[0], 44), x, s[1], WOOD_DK)

# sheer / deck edge highlight, and a dark broken edge on the right
for x in range(W):
    for y in range(H):
        if wk.get(x, y) == hull_idx:
            wk.set(x, y, WOOD_HL)
            break
for y in range(H):
    s = row_span(wk, y, hull_idx)
    if s and y > 34:
        wk.set(s[1], y, WOOD_DK)

# portholes, corroded copper rims
for px, py in [(8, 39), (15, 43)]:
    wk.circle(px, py, 1, "#122b3a")
    wk.circle(px, py, 1, "#4f8a7a", fill=False)

# corrosion / algae patches
for x, y, w, h, col in [(4, 47, 4, 2, "#4f6b4a"), (18, 36, 3, 2, "#6b8a55"),
                        (10, 50, 5, 2, "#4f6b4a"), (21, 47, 3, 2, "#6b8a55")]:
    wk.rect(x, y, w, h, col)

# rust weeping from the portholes
RUST = "#96522e"
wood_idx = {wk.color(c) for c in (WOOD_D, WOOD_M, WOOD_L, WOOD_HL)}
for rx, ry0, ry1 in [(8, 41, 45), (15, 45, 47), (19, 38, 40)]:
    for ry in range(ry0, ry1 + 1):
        if wk.get(rx, ry) in wood_idx:
            wk.set(rx, ry, RUST)

# broken mast
wk.line(13, 36, 19, 15, WOOD_M)
wk.line(14, 36, 20, 15, WOOD_DK)
wk.set(19, 14, WOOD_M); wk.set(20, 14, WOOD_DK)
wk.set(18, 13, WOOD_DK); wk.set(21, 15, WOOD_DK)      # splinters
# broken yard
wk.line(12, 25, 17, 23, WOOD_DK)
wk.line(20, 22, 23, 21, WOOD_DK)
# tattered sail scrap
wk.poly([(14,25),(19,23),(20,27),(17,29),(14,27)], "#8a7a5f")
wk.clear(17, 25, 1, 1); wk.clear(15, 27, 1, 1)

# exposed ribs of the lost hull, shortening toward the bow
for d in ["M 24 56 Q 26.5 16 29 56", "M 30 56 Q 33 22 36 56",
          "M 37 56 Q 40 28 43 56", "M 44 56 Q 46.5 36 49 56"]:
    wk.path(d, WOOD_DK, fill=False)
# broken deck planks between the ribs
wk.line(25, 40, 34, 40, WOOD_M)
wk.line(31, 44, 42, 44, WOOD_M)
wk.line(38, 47, 46, 47, WOOD_M)

# ============================================================ sand
sd = new_canvas(W, H, name="sand")
SAND_M, SAND_L, SAND_D, SAND_DD = "#c9a96e", "#e0c48c", "#a8895a", "#8a6f47"
sand_idx = sd.color(SAND_M)
sd.poly([(0,56),(5,55),(10,55),(14,53),(18,51),(22,50),(26,49),(30,49),
         (34,50),(38,50),(42,51),(46,52),(50,53),(54,54),(58,54),(63,55),
         (63,63),(0,63)], SAND_M)
for x in range(0, W, 2):                 # lit crest
    for y in range(H):
        if sd.get(x, y) == sand_idx:
            sd.set(x, y, SAND_L)
            break
for x, y in [(8,58),(15,57),(22,56),(31,55),(38,56),(45,57),(52,58),(59,58),
             (12,61),(27,60),(43,61),(56,61),(4,60),(35,62),(20,59),(49,60)]:
    sd.set(x, y, SAND_D)
for x, y in [(10,59),(24,62),(41,59),(54,62),(62,59),(17,62)]:
    sd.set(x, y, SAND_DD)

# rocks
sd.ellipse(44, 54, 2, 1, "#6b7280"); sd.set(43, 53, "#8b95a0")
sd.ellipse(48, 55, 1, 1, "#5c666e")

# ---------------------------------------------------------- coral
# pink branching coral, right of the wreck
sd.path("M 54 56 L 54 49 M 54 52 L 50 47 M 54 51 L 58 46 M 50 47 L 49 44 M 58 46 L 60 43",
        "#e2788e", fill=False)
for x, y in [(54,48),(49,43),(60,42),(50,46),(58,45)]:
    sd.set(x, y, "#f5a8b8")
# orange brain coral, left foreground
sd.ellipse(5, 54, 4, 3, "#d97a3f")
for x, y in [(3,52),(6,51),(8,53),(4,55),(7,55)]:
    sd.set(x, y, "#f2b070")
sd.ellipse(5, 57, 4, 1, "#a85a2a")

# starfish on the open sand
sd.path("M 32 56 L 33 58 L 35 58 L 33.5 59.5 L 34 61 L 32 60 L 30 61 "
        "L 30.5 59.5 L 29 58 L 31 58 Z", "#d9604a")
sd.set(32, 59, "#b04a38"); sd.set(31, 58, "#b04a38")

# shell and pebbles in the open sand
sd.set(55, 59, "#e8d5b0"); sd.set(54, 60, "#e8d5b0"); sd.set(56, 60, "#e8d5b0")
sd.set(55, 60, "#c9b28a")
for x, y, col in [(50, 60, "#8a6f47"), (52, 61, "#a8895a"), (60, 60, "#8a6f47"),
                  (25, 62, "#8a6f47"), (38, 61, "#a8895a")]:
    sd.set(x, y, col)

# ---------------------------------------------------------- seaweed
for d, col in [("M 3 58 C 1 52 5 48 3 42", "#2f7d4f"),
               ("M 7 57 C 9 51 5 47 8 40", "#47a367"),
               ("M 12 56 C 10 52 14 49 12 44", "#2f7d4f"),
               ("M 20 57 C 18 53 22 50 20 46", "#2f7d4f"),
               ("M 50 57 C 48 52 52 48 50 43", "#47a367"),
               ("M 61 57 C 63 52 59 47 62 41", "#2f7d4f"),
               ("M 57 56 C 55 53 59 50 57 46", "#7cc983")]:
    sd.path(d, col, fill=False)

# ============================================================ fish + bubbles
fs = new_canvas(W, H, name="fish")

def fish(cnv, x, y, body, shade, eye, facing=-1):
    def mx(dx):
        return (5 - dx) if facing > 0 else dx
    for dx, dy in [(1,0),(2,0),(0,1),(1,1),(2,1),(3,1),(1,2),(2,2)]:
        cnv.set(x + mx(dx), y + dy, shade if dy == 0 else body)
    for dx, dy in [(4,0),(5,1),(4,2)]:
        cnv.set(x + mx(dx), y + dy, shade)
    cnv.set(x + mx(1), y + 1, eye)

SIL, SIL_S, YEL, YEL_S, EYE = "#cfe3ee", "#8fb4cc", "#f0b544", "#c98f2a", "#16283a"
school = [(34,6,SIL,SIL_S),(42,8,SIL,SIL_S),(28,9,YEL,YEL_S),(48,11,SIL,SIL_S),
          (24,12,SIL,SIL_S),(38,13,SIL,SIL_S),(44,16,YEL,YEL_S),(31,17,SIL,SIL_S),
          (14,8,SIL,SIL_S),(20,11,SIL,SIL_S),(36,20,YEL,YEL_S),(52,15,SIL,SIL_S)]
for x, y, b, s in school:
    fish(fs, x, y, b, s, EYE, -1)

# a big grouper cruising past the wreck
BF, BF_B, BF_F, BF_S = "#6e8296", "#9fb2c0", "#4e5f70", "#55687a"
fs.line(51, 28, 54, 28, BF)
fs.line(49, 29, 56, 29, BF)
fs.line(48, 30, 57, 30, BF)
fs.line(48, 31, 57, 31, BF)
fs.line(49, 32, 56, 32, BF)
fs.line(51, 33, 54, 33, BF)
fs.rect(50, 31, 7, 2, BF_B)
fs.poly([(58, 28), (61, 31), (58, 34)], BF_F)   # tail
fs.poly([(51, 28), (54, 26), (55, 28)], BF_F)   # dorsal
fs.poly([(52, 32), (55, 34), (52, 34)], BF_F)   # pectoral
fs.line(51, 29, 51, 31, BF_S)
fs.line(54, 29, 54, 31, BF_S)
fs.set(49, 30, EYE)
fs.set(47, 31, BF_F)

# tiny distant fish, upper left
DIST = "#4a7ea8"
for dx, dy in [(0, 0), (1, 0), (2, 0), (3, 0), (2, 1)]:
    fs.set(5 + dx, 6 + dy, DIST)
    fs.set(12 + dx, 10 + dy, DIST)
for dx, dy in [(0, 0), (1, 0), (2, 0), (3, 0), (2, 1)]:
    fs.set(17 + dx, 4 + dy, DIST)

# a small crab on the sand
CRAB, CRAB_D = "#c94f3f", "#a03a2e"
fs.set(39, 57, EYE); fs.set(41, 57, EYE)
fs.rect(39, 58, 3, 1, CRAB)
fs.set(38, 58, CRAB); fs.set(42, 58, CRAB)
fs.set(38, 59, CRAB_D); fs.set(40, 59, CRAB_D); fs.set(42, 59, CRAB_D)

for x, y in [(25,31),(27,27),(24,23),(26,19),(41,4),(43,1),(53,9),(54,6),
             (13,21),(14,17),(58,12),(35,25),(9,30),
             (11,33),(10,30),(12,27),(46,29),(45,26),(43,23)]:
    fs.set(x, y, "#d8f0fa")
for x, y in [(30,14),(48,7),(20,26)]:
    fs.circle(x, y, 1, "#a8d8ee", fill=False)

# ============================================================ composite
scene = flatten([bg, wk, sd, fs], name="shipwreck")
print(scene.stats_text())
print(scene.matrix_text(region=(0, 0, 63, 63)))
finish(scene)
