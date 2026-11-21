from pixelbench_api import new_canvas, finish
import random

c = new_canvas(128, 128, name="cyberpunk-alley")

# ---------------- sky ----------------
SKY = ['#04050d', '#070a18', '#0c1022', '#131834', '#1a2044', '#232a5a']
for y in range(84):
    c.rect(0, y, 128, 1, SKY[min(5, y // 15)])

# ---------------- distant buildings ----------------
c.rect(26, 42, 30, 42, '#0a0d1e')
c.rect(72, 38, 30, 46, '#0b0e20')
c.rect(52, 48, 26, 36, '#0c0f22')
c.rect(26, 38, 10, 8, '#080a18')
c.rect(44, 34, 8, 12, '#080a18')
c.rect(82, 30, 10, 8, '#090b1a')

# ---------------- far alley building ----------------
c.rect(28, 50, 72, 34, '#121732')
for wx in range(32, 98, 6):
    for wy in range(55, 82, 6):
        p = (wx * 7 + wy * 13) % 9
        if p < 2:
            c.rect(wx, wy, 2, 3, '#ffd97a')
        elif p == 2:
            c.rect(wx, wy, 2, 3, '#59d8ff')
        elif p == 3:
            c.rect(wx, wy, 2, 2, '#2a3566')
        elif p == 4:
            c.rect(wx, wy, 2, 3, '#1c2450')

# CYBER neon sign on far building
c.rect(36, 48, 46, 17, '#3a1240')
c.rect(38, 50, 42, 13, '#180a2c')
c.text(41, 52, 'CYBER', '#b3246e')
c.text(42, 53, 'CYBER', '#ff3ea5')

# ---------------- side walls ----------------
c.rect(0, 0, 25, 128, '#070811')
c.rect(103, 0, 25, 128, '#070811')
c.rect(21, 0, 4, 128, '#0a0d1c')
c.rect(103, 0, 4, 128, '#0a0d1c')
for y in (16, 28, 40, 52, 62, 72, 84, 96, 108, 118):
    c.rect(0, y, 25, 1, '#0a0d1c')
    c.rect(103, y, 25, 1, '#0a0d1c')

# right wall circle sign
c.circle(116, 40, 9, '#4a1038', fill=False)
c.circle(116, 40, 7, '#7a1a4d', fill=False)
c.circle(116, 40, 6, '#ff2a6d', fill=False)
c.circle(116, 40, 5, '#ff6a9a', fill=False)
c.rect(116, 31, 1, 4, '#ff9ac8')
c.line(116, 40, 116, 40, '#ff9ac8')

# right BAR panel
c.rect(104, 60, 21, 15, '#170f2a')
c.text(105, 61, 'BAR', '#b3246e')
c.text(106, 62, 'BAR', '#ff9ac8')
c.rect(104, 59, 21, 1, '#7a1a4d')
c.line(113, 60, 113, 52, '#4a1038')

# left vertical cyan sign
c.rect(5, 20, 16, 56, '#0e1226')
c.rect(7, 22, 12, 52, '#0f5a7a')
c.rect(10, 23, 4, 50, '#26d9ff')
c.rect(11, 24, 1, 48, '#8ff0ff')
for sx in (8, 5, 12, 7):
    c.set(sx, 30, '#a8f0ff')
    c.set(sx + 5, 44, '#a8f0ff')

# left 24H sign
c.rect(5, 5, 18, 10, '#0a1410')
c.text(5, 5, '24H', '#2fae5a')
c.text(6, 6, '24H', '#39ff88')

# ---------------- street ----------------
c.rect(0, 84, 128, 44, '#090b15')
c.rect(25, 84, 78, 44, '#0c0f1d')
c.rect(25, 84, 78, 6, '#161c3a')
c.rect(0, 116, 128, 12, '#070a13')
c.line(25, 84, 25, 127, '#0a0d1c')
c.line(102, 84, 102, 127, '#0a0d1c')

# ---------------- puddles ----------------
c.ellipse(64, 116, 33, 6, '#151a38')
c.ellipse(92, 114, 13, 5, '#151a38')
c.ellipse(34, 113, 10, 5, '#151a38')

# ---------------- reflections ----------------
for x in (44, 49, 55, 61, 67, 73, 79):
    c.line(x, 112, x, 121, '#7a1a4d')
for x in (47, 58, 70):
    c.line(x, 113, x, 118, '#b3246e')
for x in (36, 38):
    c.line(x, 107, x, 116, '#0f5a7a')
    c.line(x + 2, 108, x + 2, 114, '#26d9ff')
for x in (99, 103, 107, 111):
    c.line(x, 110, x, 118, '#5a1440')
    c.line(x, 112, x, 116, '#b3246e')

# ---------------- vending machines ----------------
# left (red)
c.rect(7, 80, 18, 32, '#b32445')
c.rect(7, 80, 18, 18, '#d93155')
c.rect(9, 82, 14, 12, '#1a0a12')
c.rect(10, 83, 12, 6, '#ff8aa8')
c.rect(10, 90, 12, 2, '#7a1830')
c.rect(7, 104, 18, 2, '#7a1830')
c.set(17, 92, '#ffd97a')
c.set(16, 97, '#8f1a45')
c.ellipse(17, 116, 10, 4, '#3a0f22')
c.ellipse(17, 115, 7, 3, '#5a1230')
for x in (10, 14, 18, 22):
    c.line(x, 114, x, 119, '#8f1a45')
# right (blue)
c.rect(106, 80, 18, 32, '#145aa8')
c.rect(106, 80, 18, 6, '#2a86d8')
c.rect(108, 82, 14, 14, '#0a1628')
c.rect(109, 83, 12, 6, '#a8e6ff')
c.rect(109, 90, 12, 2, '#d8f4ff')
c.rect(108, 93, 14, 2, '#2a86d8')
c.rect(106, 100, 18, 4, '#0a1628')
c.ellipse(111, 114, 12, 5, '#0f2a4a')
c.ellipse(111, 113, 8, 3, '#145aa8')
for x in (104, 110, 116):
    c.line(x, 112, x, 118, '#2a86d8')

# ---------------- lamp ----------------
c.rect(98, 86, 12, 2, '#04060f')
c.circle(97, 86, 7, '#4a3417')
c.circle(97, 86, 5, '#8a5a1f')
c.circle(97, 86, 3, '#ffd97a')
c.ellipse(97, 119, 9, 4, '#2a2412')
c.ellipse(97, 118, 6, 3, '#4a3a1a')

# ---------------- cables ----------------
def wire(pts, colr):
    for p, q in zip(pts, pts[1:]):
        c.line(p[0], p[1], q[0], q[1], colr)

wire([(0, 3), (30, 14), (58, 7), (92, 18), (127, 9)], '#020308')
wire([(0, 10), (36, 19), (62, 12), (96, 24), (124, 17)], '#04060f')
wire([(0, 18), (28, 28), (52, 15), (80, 25), (102, 18), (127, 22)], '#020308')
wire([(25, 5), (44, 20), (64, 12), (86, 24), (102, 16)], '#04060f')
wire([(30, 44), (56, 60), (94, 46)], '#04060f')

# ---------------- person (transparent umbrella) ----------------
c.poly([(50, 88), (55, 77), (61, 70), (67, 77), (72, 88)], '#a8e8ff', fill=False)
c.line(61, 70, 61, 92, '#2a7db3')
for tx in (50, 55, 67, 72):
    c.line(61, 71, tx, 88, '#2a7db3')
c.line(50, 88, 72, 88, '#2a7db3')
c.set(61, 78, '#d8f4ff')
c.set(55, 82, '#d8f4ff')
c.line(66, 81, 66, 83, '#d8f4ff')
c.circle(61, 100, 3, '#04050c')
c.line(63, 98, 63, 103, '#7a1a4d')
c.rect(55, 103, 13, 14, '#04050c')
c.line(67, 104, 67, 116, '#1a5a8f')
c.rect(57, 117, 9, 7, '#04050c')
c.line(64, 105, 64, 116, '#0e2a4a')
c.rect(57, 119, 9, 7, '#0a0e1a')
c.line(59, 120, 59, 124, '#1a5a8f')
c.line(63, 118, 63, 124, '#2a5a8f')
c.line(52, 112, 52, 120, '#7a1a4d')

# ---------------- surroundings ----------------
c.ellipse(28, 118, 6, 4, '#0d0e18')
c.ellipse(32, 120, 5, 3, '#0a0b14')
c.rect(124, 44, 3, 34, '#0a0d1c')
c.rect(0, 0, 128, 2, '#020308')
c.rect(0, 126, 128, 2, '#020308')
c.rect(0, 0, 3, 128, '#03040c')
c.rect(125, 0, 3, 128, '#03040c')

# ---------------- rain ----------------
random.seed(11)
for _ in range(150):
    x = random.randint(2, 120)
    y = random.randint(0, 118)
    ln = random.randint(3, 5)
    dx = random.randint(0, 1)
    dy = random.randint(2, 4)
    if y + dy * ln > 124:
        y = 124 - dy * ln
    r = random.random()
    colr = '#9fd8ff' if r < 0.18 else ('#5f7fa8' if r < 0.5 else '#3a4a66')
    c.line(x, y, x + dx * ln, y + dy * ln, colr)

# ---------------- report ----------------
print(c.stats_text())
print("---- umbrella region ----")
print(c.matrix_text(region=(44, 66, 82, 92)))
print("---- neon region ----")
print(c.matrix_text(region=(34, 44, 86, 72)))
print("---- street region ----")
print(c.matrix_text(region=(0, 84, 127, 127)))

result = c
finish(result)
