from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, name="title")

# ---------- palette ----------
bg0    = c.color("#100d26")   # deep night sky (top)
bg1    = c.color("#171240")   # mid sky
bg2    = c.color("#1f1950")   # lower sky
outline= c.color("#15061e")   # letter outlines
shadow = c.color("#05030e")   # drop shadows
gold   = c.color("#f0b51c")   # PIXEL fill
gold_l = c.color("#ffe06a")   # PIXEL highlight
cyan   = c.color("#38c8ec")   # QUEST fill
cyan_l = c.color("#b8f0ff")   # QUEST highlight
cyan_d = c.color("#0d7fa3")   # divider dashes
stars_w= c.color("#ffffff")
stars_d= c.color("#6f7fc0")
moon   = c.color("#f4e9a6")
moon_d = c.color("#bfae72")
ground = c.color("#0a0720")
ground2= c.color("#3a3480")
ge     = c.color("#31296b")

# ---------- background ----------
c.rect(0, 0, W, 14, bg0)
c.rect(0, 14, W, 16, bg1)      # rows 14..29
c.rect(0, 30, W, 22, bg2)      # rows 30..51
c.rect(0, 52, W, 12, ground)   # ground 52..63
c.rect(0, 52, W, 1, ge)        # horizon edge

# far-ground pebbles / grass tufts
tufts = [(8,51,9,50),(24,51,25,50),(40,51,41,50),(56,51,57,50)]
for a, b, a2, b2 in tufts:
    c.set(a, b, ge).set(a2, b2, ge)
for x, y in [(14,58),(28,61),(43,57),(53,62),(60,59),(21,56),(36,60),(49,55)]:
    c.set(x, y, ground2)

# ---------- stars ----------
dots = [(5,3),(13,8),(24,5),(33,2),(42,6),(57,3),(26,11),(45,10),(59,9),
        (6,15),(58,18),(4,26),(59,28),(8,33),(57,34),(6,44),(58,42),(5,47),
        (59,45),(60,24),(3,38),(61,39),(18,2),(49,4)]
for x, y in dots:
    c.set(x, y, stars_d)
for x, y in [(13,8),(33,2),(57,3),(26,11),(45,10),(59,9),(60,24),(6,44)]:
    c.set(x, y, stars_w)

# ---------- moon (top-right) ----------
c.circle(54, 7, 4, moon)
c.set(51, 5, moon_d).set(56, 8, moon_d).set(53, 10, moon_d).set(56, 11, moon_d)

# ---------- letter drawing helpers ----------
def draw_shadow(cv, x, y, glyph, dx, dy, col):
    for r in range(len(glyph)):
        for col_i in range(len(glyph[0])):
            if glyph[r][col_i] == '#':
                cv.set(x + col_i + dx, y + r + dy, col)

def draw_letter(cv, x, y, glyph, fill, light, outl):
    for r in range(len(glyph)):
        for col_i in range(len(glyph[0])):
            if glyph[r][col_i] == '#':
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        cv.set(x + col_i + dc, y + r + dr, outl)
    for r in range(len(glyph)):
        for col_i in range(len(glyph[0])):
            if glyph[r][col_i] == '#':
                cv.set(x + col_i, y + r, light if r < 2 else fill)

# ---------- glyphs ----------
P = ["#######", "#.....#", "#.....#", "#.....#", "#######",
    "#......", "#......", "#......", "#......"]
I = ["#######", "...#...", "...#...", "...#...", "...#...",
    "...#...", "...#...", "...#...", "#######"]
X = ["#.....#", "#.....#", ".#...#.", "..#.#..", "...#...",
    "..#.#..", ".#...#.", "#.....#", "#.....#"]
E = ["#######", "#......", "#......", "#......", "#####..",
    "#......", "#......", "#......", "#######"]
L = ["#......", "#......", "#......", "#......", "#......",
    "#......", "#......", "#......", "#######"]

Q = [".###.", "#...#", "#...#", "#...#", "#...#", ".####", "...#."]
U = ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."]
S = [".###.", "#...#", "#....", ".###.", "....#", "#...#", ".###."]
T = ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."]

# ---------- title: PIXEL ----------
PIX = [P, I, X, E, L]
x0, y0 = 10, 14
for i, g in enumerate(PIX):
    draw_shadow(c, x0 + i * 9, y0, g, 1, 2, shadow)
for i, g in enumerate(PIX):
    draw_letter(c, x0 + i * 9, y0, g, gold, gold_l, outline)

# ---------- divider ----------
c.rect(14, 30, 15, 1, cyan_d)   # x14..28
c.rect(35, 30, 15, 1, cyan_d)   # x35..49
c.poly([(32, 26), (36, 30), (32, 34), (28, 30)], cyan_l)

# ---------- subtitle: QUEST ----------
QST = [Q, U, E, S, T]
xq, yq = 15, 38
for i, g in enumerate(QST):
    draw_shadow(c, xq + i * 7, yq, g, 1, 2, shadow)
for i, g in enumerate(QST):
    draw_letter(c, xq + i * 7, yq, g, cyan, cyan_l, outline)

# ---------- sparkles ----------
def sparkle(cv, x, y, col):
    for sx, sy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        cv.set(x + sx, y + sy, col)

for x, y in [(7, 19), (56, 23), (6, 42), (57, 40), (26, 6), (38, 5)]:
    sparkle(c, x, y, stars_w)
for x, y in [(8, 19), (55, 23), (5, 42), (58, 40)]:
    c.set(x, y, stars_d)
c.set(26, 6, stars_d)

print(c.stats_text())

finish(c)
