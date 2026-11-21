from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, name="female-elf-archer")

COL = {
    'O': (15, 36, 21),   # outline dark green
    'H': (28, 90, 48),   # hair dark
    'h': (47, 143, 68),  # hair mid
    'L': (77, 191, 94),  # hair light
    'l': (122, 232, 138) # hair lightest
}

COL.update({
    'S': (248, 201, 163),  # skin
    's': (224, 168, 120),  # skin shade
    'R': (240, 160, 136),  # blush
    'E': (46, 110, 168),   # iris
    'e': (22, 40, 63),     # pupil
    'M': (180, 90, 90),    # mouth
    'G': (210, 245, 192),  # outfit light green
    'g': (159, 224, 138),  # outfit mid
    'D': (108, 190, 102),  # outfit shade
    'W': (61, 122, 66),    # outfit line
    'K': (124, 74, 38),    # belt
    'Y': (232, 192, 96),   # buckle
    'q': (110, 76, 44),    # quiver leather
    'Q': (78, 53, 32),     # quiver dark
    'P': (154, 96, 50),    # bow wood
    'p': (122, 74, 36),    # bow dark
    'F': (216, 80, 52),    # fletching
    'A': (196, 158, 96),   # arrow shaft
    'V': (74, 56, 38),    # boots
    'v': (106, 84, 56),   # boots light
    'N': (79, 168, 216),  # gem
    'B': (230, 236, 222), # bow string
})

# ---------------------------------------------------------------- helpers
def px(y, x, s):
    for i, ch in enumerate(s):
        col = COL.get(ch)
        if col is not None:
            c.set(x + i, y, col)

# ---------------------------------------------------------------- background
top = (60, 92, 54)
bot = (22, 40, 26)
steps = 24
cmap = []
for i in range(steps):
    t = i / (steps - 1)
    cmap.append(tuple(round(top[k] + (bot[k] - top[k]) * t) for k in range(3)))
for y in range(H):
    idx = min(steps - 1, int(y * (steps - 1) / (H - 1)))
    c.rect(0, y, W, 1, cmap[idx])

# soft aura behind the figure
c.ellipse(33, 26, 21, 25, (70, 102, 64))
c.ellipse(33, 30, 15, 18, (80, 116, 72))
# ground
c.ellipse(33, 59, 16, 4, (20, 34, 24))
c.ellipse(33, 60, 11, 3, (17, 29, 21))

# ---------------------------------------------------------------- quiver + arrows (left side, behind)
# quiver body
for y in range(23, 41):
    c.set(19, y, COL['Q'])
for y in range(23, 40):
    c.set(20, y, COL['q'])
for y in range(23, 38):
    c.set(21, y, COL['q'])
# arrow shafts
for y in range(19, 23):
    for x in range(19, 22):
        c.set(x, y, COL['A'])
# fletching feathers
for y in range(14, 19):
    for x in range(19, 22):
        c.set(x, y, COL['F'])
# fletching nocks at top
c.set(19, 13, COL['F']); c.set(20, 13, COL['F']); c.set(21, 13, COL['F'])
# quiver tips
c.set(18, 12, COL['Q'])
# quiver bottom cap
for x in range(18, 22):
    c.set(x, 41, COL['Q'])
# ear tips stand out
c.set(21, 13, COL['s']); c.set(21, 14, COL['s'])
c.set(41, 13, COL['s']); c.set(41, 14, COL['s'])

# bow (right side, longbow on the back)
# bow string first (behind the wood)
c.line(44, 18, 34, 38, COL['B'])
bow = [(43, 19), (42, 20), (42, 21), (41, 22), (41, 23), (40, 24), (40, 25),
       (39, 26), (39, 27), (39, 28), (38, 29), (38, 30), (38, 31), (38, 32),
       (38, 33), (38, 34), (37, 35), (37, 36), (37, 37), (37, 38)]
for (x, y) in bow:
    c.set(x, y, COL['P'])
bowin = [(40, 20), (39, 21), (39, 22), (38, 23), (38, 24), (37, 25), (37, 26),
        (37, 27), (36, 28), (36, 29)]
for (x, y) in bowin:
    c.set(x, y, COL['p'])

# ---------------------------------------------------------------- long hair back streams (behind body)
for x in range(22, 26):
    for y in range(21, 33):
        col = COL['H'] if x in (22, 25) else COL['h']
        c.set(x, y, col)

# ---------------------------------------------------------------- legs + boots
# legs (light-green outfit leggings -> boots)
for y in range(37, 50):
    for x in range(29, 33):
        c.set(x, y, COL['G'])
for y in range(37, 50):
    for x in range(34, 38):
        c.set(x, y, COL['G'])
for y in range(37, 50):
    c.set(29, y, COL['D']); c.set(32, y, COL['g'])
    c.set(34, y, COL['g']); c.set(37, y, COL['D'])
# boots
for y in range(50, 53):
    for x in range(29, 33):
        c.set(x, y, COL['V'])
for y in range(50, 53):
    for x in range(34, 38):
        c.set(x, y, COL['V'])
for y in range(53, 55):
    for x in range(29, 32):
        c.set(x, y, COL['V'])
for y in range(53, 55):
    for x in range(34, 37):
        c.set(x, y, COL['V'])
for y in range(55, 57):
    c.set(29, y, COL['V']); c.set(34, y, COL['V'])
# boot highlights
for x in range(29, 32):
    c.set(x, 51, COL['v'])
for x in range(34, 37):
    c.set(x, 51, COL['v'])

# ---------------------------------------------------------------- torso (light green outfit)
# skirt
c.set(26, 34, COL['D'])
for y in range(34, 37):
    for x in range(27, 36):
        c.set(x, y, COL['G'])
c.set(36, 27, COL['D']); c.set(36, 34, COL['D'])
# torso upper
for y in range(24, 30):
    for x in range(26, 37):
        c.set(x, y, COL['G'])
for y in range(30, 33):
    for x in range(27, 36):
        c.set(x, y, COL['g'])
c.set(26, 24, COL['D'])
for y in range(24, 30):
    c.set(26, y, COL['D']); c.set(36, y, COL['D'])
for y in range(30, 33):
    c.set(27, y, COL['D']); c.set(35, y, COL['D'])
# torso side shading
for y in range(25, 30):
    c.set(27, y, COL['g']); c.set(35, y, COL['g'])
c.set(31, 28, COL['g']); c.set(32, 28, COL['g'])
# waist belt
for y in range(33, 34):
    for x in range(27, 36):
        c.set(x, y, COL['K'])
c.set(31, 33, COL['Y']); c.set(32, 33, COL['Y'])
# collar / neck
c.set(30, 23, COL['S'])
c.set(31, 22, COL['S']); c.set(32, 22, COL['S']); c.set(33, 22, COL['S'])

# ---------------------------------------------------------------- hair over shoulders (front)
# left side: frames the face and falls over the shoulder
for y in range(19, 22):
    for x in range(23, 29):
        c.set(x, y, COL['H'] if x in (23, 28) else COL['h'])
for y in range(22, 33):
    for x in range(23, 28):
        c.set(x, y, COL['H'] if x in (23, 27) else COL['h'])
# right side: frames the neck, keeps the bow visible
for y in range(19, 22):
    for x in range(34, 38):
        c.set(x, y, COL['H'] if x in (34, 37) else COL['h'])
for y in range(22, 24):
    for x in range(35, 38):
        c.set(x, y, COL['H'] if x in (35, 37) else COL['h'])
for y in range(24, 32):
    for x in range(36, 37):
        c.set(x, y, COL['h'])

# ---------------------------------------------------------------- head
# hair mass
for y in range(5, 9):
    for x in range(24, 37):
        c.set(x, y, COL['H'])
for y in range(9, 12):
    c.set(23, y, COL['H'])
c.set(22, 10, COL['H'])
# face
for y in range(9, 13):
    for x in range(26, 37):
        c.set(x, y, COL['S'])
for y in range(13, 15):
    for x in range(26, 37):
        c.set(x, y, COL['S'])
# ears
for x in range(22, 26):
    for y in range(13, 16):
        c.set(x, y, COL['S'])
for x in range(37, 41):
    for y in range(13, 16):
        c.set(x, y, COL['S'])
# face lower
for y in range(15, 16):
    for x in range(26, 36):
        c.set(x, y, COL['S'])
for y in range(16, 17):
    for x in range(27, 35):
        c.set(x, y, COL['S'])
for y in range(17, 18):
    for x in range(28, 35):
        c.set(x, y, COL['S'])
for y in range(18, 19):
    for x in range(28, 34):
        c.set(x, y, COL['S'])
for y in range(19, 20):
    for x in range(29, 34):
        c.set(x, y, COL['S'])
for y in range(20, 22):
    for x in range(29, 33):
        c.set(x, y, COL['S'])
# face details
# left eye
c.set(28, 13, COL['O']); c.set(29, 13, COL['E']); c.set(30, 13, COL['E']); c.set(31, 13, COL['O'])
c.set(28, 14, COL['O']); c.set(29, 14, COL['e']); c.set(30, 14, COL['e']); c.set(31, 14, COL['O'])
# right eye
c.set(33, 13, COL['O']); c.set(34, 13, COL['E']); c.set(35, 13, COL['E']); c.set(36, 13, COL['O'])
c.set(33, 14, COL['O']); c.set(34, 14, COL['e']); c.set(35, 14, COL['e']); c.set(36, 14, COL['O'])
# brows
c.set(28, 12, COL['O']); c.set(29, 12, COL['O']); c.set(33, 12, COL['O']); c.set(34, 12, COL['O'])
# cheek blush
c.set(29, 15, COL['R']); c.set(30, 15, COL['R'])
c.set(33, 15, COL['R']); c.set(34, 15, COL['R'])
# nose + mouth
c.set(31, 16, COL['s'])
c.set(30, 17, COL['M']); c.set(31, 17, COL['M']); c.set(32, 17, COL['M'])
# necklace gem
c.set(31, 23, COL['N']); c.set(32, 23, COL['N'])
c.set(31, 24, COL['N'])

# ---------------------------------------------------------------- arrows top peeking over shoulder
c.set(20, 12, COL['A']); c.set(21, 13, COL['A'])
c.set(21, 14, COL['A']); c.set(21, 20, COL['A'])
c.set(22, 14, COL['A']); c.set(22, 21, COL['A'])

# ---------------------------------------------------------------- final hair hilights on top
c.set(27, 6, COL['l']); c.set(28, 6, COL['l']); c.set(29, 6, COL['l'])
c.set(30, 6, COL['l'])
c.set(27, 7, COL['l']); c.set(31, 7, COL['l'])
c.set(26, 9, COL['h']); c.set(35, 9, COL['h'])
# stray front strands
c.set(24, 23, COL['l']); c.set(25, 24, COL['l'])
c.set(36, 21, COL['l'])

# ---------------------------------------------------------------- chest strap (bow/quiver strap across)
for x in range(28, 36):
    c.set(x, 30, COL['W'])

# ---------------------------------------------------------------- final chain
# floor shadow under feet
c.ellipse(33, 58, 14, 3, (17, 29, 21))

print(c.matrix_text(region=(18, 4, 44, 32)))
print(c.stats_text())
print("canvas 64x64 num colors:", c.stats()['colors_used'])

finish(c)
