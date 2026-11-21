from pixelbench_api import new_canvas, finish, input_canvas, view

W = H = 64
c = new_canvas(W, H)

# ---------- water background gradient ----------
bands = [
    (0, 7, '#2b5b87'),
    (8, 16, '#1e4266'),
    (17, 25, '#173652'),
    (26, 37, '#102e49'),
    (38, 49, '#0b2740'),
    (50, 63, '#092237'),
]
for y0, y1, col in bands:
    c.rect(0, y0, W, y1 - y0 + 1, col)

# light rays
ray = '#3a6f96'
sky = [(16, 0, 40, 26), (30, 2, 36, 34), (44, 0, 48, 24), (54, 1, 50, 20), (8, 0, 30, 22)]
for rx, ry, lx, ly in sky:
    c.line(rx, ry, lx, ly, ray)

# ---------- school of fish (behind hull) ----------
def fish(x, y, col, col2):
    c.ellipse(x, y, 3, 2, col)
    c.poly([(x - 3, y), (x - 6, y - 2), (x - 6, y + 2)], col)
    c.set(x + 2, y - 1, col2)
    c.set(x - 1, y - 1, col2)

school = [
    (48, 14, '#e08a3c'), (55, 11, '#d97f33'), (42, 18, '#e08a3c'),
    (58, 17, '#df8436'), (52, 21, '#edd9a8'), (46, 24, '#e08a3c'),
    (38, 13, '#edd9a8'), (60, 14, '#e08a3c'), (56, 8, '#e08a3c'),
    (49, 27, '#edd9a8'), (60, 20, '#d97f33'), (54, 25, '#e08a3c'),
]
for x, y, col in school:
    fish(x, y, col, '#f4efe0')
school_f = [
    (36, 22, '#e08a3c'), (34, 16, '#edd9a8'), (30, 12, '#e08a3c'),
]
for x, y, col in school_f:
    fish(x, y, col, '#f4efe0')

# ---------- shipwreck hull ----------
wood_dark = '#2b1a0d'
wood_main = '#452a12'
wood_lit = '#6a4420'
wood_br = '#7d5528'
dark_gap = '#150c05'

# hull body
c.path("M 47 19 L 24 24 C 18 25, 14 29, 12 35 C 10 43, 15 50, 26 52 "
       "C 38 54, 49 50, 52 43 L 51 25 Z", wood_main)

# plank lines (curved)
for d in '#6a4420':
    pass
c.path("M 16 30 C 24 27, 40 27, 50 30", wood_lit, fill=False)
c.path("M 14 36 C 23 33, 41 33, 50 36", wood_lit, fill=False)
c.path("M 15 42 C 23 40, 41 40, 50 42", wood_lit, fill=False)
c.path("M 18 47 C 26 49, 40 49, 49 46", wood_lit, fill=False)
c.path("M 13 33 C 16 39, 16 45, 20 50", wood_lit, fill=False)
c.path("M 24 25 C 24 33, 24 40, 27 51", wood_dark, fill=False)
c.path("M 36 25 C 36 33, 36 40, 39 52", wood_dark, fill=False)

# deck interior gap
c.poly([(48, 19), (25, 24), (25, 27), (48, 23)], dark_gap)
c.poly([(14, 34), (12, 35), (13, 39), (16, 37)], dark_gap)

# broken jagged planks sticking up
c.poly([(42, 14), (45, 13), (45, 22), (42, 21)], wood_main)
c.line(43, 13, 43, 19, wood_br)
c.line(37, 12, 38, 20, wood_lit)
c.poly([(37, 15), (39, 12), (40, 20), (38, 20)], wood_main)

# corrosion: rust + gray metal plates
rust = '#7a4623'
rust2 = '#9c5a2c'
gray = '#565760'
gray2 = '#767681'
c.rect(28, 30, 5, 3, gray)
c.rect(33, 28, 4, 4, gray)
c.rect(30, 34, 5, 3, gray2)
c.rect(42, 31, 4, 3, gray)
c.rect(20, 37, 4, 4, gray)
c.line(28, 30, 33, 30, gray2)
c.line(33, 28, 37, 28, gray2)
# rust streaks/stains
c.rect(28, 36, 6, 2, rust)
c.line(30, 38, 33, 42, rust)
c.line(44, 34, 47, 40, rust)
c.rect(21, 42, 5, 2, rust)
c.rect(26, 46, 6, 2, rust2)
c.line(23, 30, 26, 35, rust)
c.rect(48, 27, 3, 4, gray2)

# barnacles along hull bottom
for bx, by in [(18, 50), (22, 51), (27, 52), (33, 53), (40, 52), (46, 49), (13, 48), (16, 47), (25, 36), (21, 40)]:
    c.set(bx, by, '#7a7a80')

# ---------- seabed sand (buries hull bottom) ----------
sand1 = '#d6c584'
sand2 = '#c2ad68'
sand3 = '#a89154'
sand_d = '#7f6c3e'
c.rect(0, 51, W, H - 51, sand1)
c.path("M 0 50 C 12 46, 22 52, 34 50 C 46 48, 54 54, 63 49 L 63 53 C 54 57, 46 52, 34 54 C 22 56, 12 50, 0 54 Z", sand2)
c.path("M 40 52 C 50 49, 58 52, 63 51 L 63 56 C 58 57, 50 54, 42 56 Z", sand3)
c.path("M 4 54 C 14 52, 20 55, 28 53 L 28 58 C 20 59, 12 56, 4 58 Z", sand3)
# sand ripples
c.line(6, 55, 20, 54, sand_d)
c.line(30, 57, 46, 56, sand_d)
c.line(48, 59, 60, 58, sand_d)
c.line(10, 60, 24, 59, sand_d)
c.set(35, 57, sand_d)

# wrecked metal fragments sticking out of sand
c.rect(16, 45, 2, 6, gray2)
c.rect(50, 47, 3, 4, gray)
c.line(52, 46, 55, 50, rust)
c.rect(6, 49, 2, 3, gray2)

# ---------- seaweed ----------
def seaweed(x, top_y, base_y, stem, leaf):
    c.line(x, base_y, x + 1, top_y, stem)
    xs = range(base_y - 3, top_y, -3)
    k = 0
    for i, yy in enumerate(xs):
        lx = x + (2 if i % 2 == 0 else -2)
        c.ellipse(lx, yy, 2, 1, leaf)
    c.ellipse(x - 1, top_y, 2, 2, leaf)

# foreground plants
seaweed(8, 34, 56, '#1e5a2b', '#3c9a4c')
seaweed(5, 40, 57, '#1e5a2b', '#2f7f38')
seaweed(58, 30, 55, '#1e5a2b', '#45a858')
seaweed(61, 38, 56, '#1e5a2b', '#3c9a4c')
seaweed(54, 44, 58, '#174d24', '#2f7f38')
seaweed(11, 47, 60, '#174d24', '#2f7f38')
# tall seaweed behind hull front
seaweed(30, 28, 54, '#1d4f26', '#2f7f38')
seaweed(59, 24, 52, '#1d4f26', '#3c9a4c')

# coral clusters
def coral(x, y, base, light):
    c.ellipse(x, y, 3, 2, base)
    c.ellipse(x + 3, y + 1, 2, 2, base)
    c.ellipse(x - 3, y + 1, 2, 2, base)
    c.ellipse(x + 2, y - 1, 2, 1, light)
    c.ellipse(x - 2, y - 1, 2, 1, light)
    c.ellipse(x, y, 1, 1, light)

coral(4, 52, '#cf3f3f', '#ec7a70')
coral(60, 53, '#cf3f3f', '#ec7a70')
coral(15, 54, '#b53434', '#d65a5a')
coral(50, 56, '#b53434', '#d65a5a')
# small fan coral
c.poly([(63, 40), (63, 47), (60, 47), (60, 40)], '#e06868')
c.line(61, 41, 61, 46, '#e06868')

# ---------- small fish in front ----------
fish(12, 30, '#e08a3c', '#f4efe0')
fish(55, 28, '#d9cfc0', '#f4efe0')
fish(30, 20, '#d9cfc0', '#f4efe0')

# ---------- bubbles ----------
bub = '#b9dcec'
for bx, by in [(20, 26), (24, 20), (36, 16), (46, 27), (9, 24), (52, 22), (28, 11), (40, 9)]:
    c.circle(bx, by, 1, bub, fill=False)
c.set(20, 26, bub)
c.set(24, 20, bub)
c.set(36, 16, bub)
c.set(46, 27, bub)
c.set(28, 11, bub)

# sparkle highlights on water
for x in range(0, 64, 4):
    c.set(x + (6 if x % 8 else 2), (x * 7) % 8, bub)

print(c.stats_text())
finish([c])
