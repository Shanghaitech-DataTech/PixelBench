src = input_canvas
W, H = 40, 30

DARK = src.color((58, 55, 55))
G1 = src.color((183, 179, 178))
G2 = src.color((130, 124, 124))
WHT = src.color((239, 233, 231))
SK1 = src.color((214, 179, 157))
SK2 = src.color((188, 139, 109))
GLD = src.color((205, 174, 103))

# ---------------- frame 1 : original picture ----------------
f1 = new_canvas(W, H, None, name="frame1")
f1.blit(src, 1, 1)

# ---------------- frame 2 : mid-leap ----------------
HEAD = {6: (25, 31), 7: (24, 32), 8: (23, 32), 9: (23, 32), 10: (23, 32),
        11: (23, 33), 12: (23, 33), 13: (24, 32), 14: (25, 31), 15: (26, 30)}
EAR_A = {0: (19, 23), 1: (19, 23), 2: (20, 24), 3: (20, 25), 4: (22, 26),
         5: (24, 27)}
EAR_B = {0: (27, 31), 1: (27, 31), 2: (28, 32), 3: (28, 32), 4: (29, 32),
         5: (29, 32)}
BODY = {10: (12, 23), 11: (9, 24), 12: (7, 24), 13: (5, 24), 14: (4, 24),
        15: (4, 23), 16: (5, 23), 17: (7, 21), 18: (10, 19), 19: (14, 17)}
FRONT = {15: (24, 27), 16: (25, 29), 17: (26, 31), 18: (27, 32),
         19: (28, 32), 20: (29, 31)}
HIND = {15: (2, 7), 16: (1, 7), 17: (1, 6), 18: (2, 6), 19: (3, 6)}

f2 = new_canvas(W, H, None, name="frame2")
OX, OY = 3, 2

def paint(part, col=WHT):
    for y, (x0, x1) in part.items():
        f2.rect(OX + x0, OY + y, x1 - x0 + 1, 1, col)

for part in (BODY, HIND, FRONT, HEAD, EAR_A, EAR_B):
    paint(part)

# two-tone shade along lower edges (light grey band, mid grey core)
colh = [sum(1 for y in range(H) if f2.get(x, y) == WHT) for x in range(W)]
light, deep = [], []
for x in range(W):
    for y in range(H):
        if f2.get(x, y) != WHT or f2.get(x, y + 1) in (0, None):
            continue
        if f2.get(x, y + 2) in (0, None):
            light.append((x, y))
        elif colh[x] >= 6 and f2.get(x, y + 3) in (0, None):
            deep.append((x, y))
for x, y in deep:
    f2.set(x, y, G2)
for x, y in light:
    f2.set(x, y, G1)

def put(x, y, col):
    if f2.get(x, y) == WHT:
        f2.set(x, y, col)

# inner ear skin (near ear, upper-left of head)
for x, y in [(20, 3), (21, 3), (21, 4), (22, 4), (22, 5), (21, 5)]:
    put(OX + x, OY + y, SK1)
put(OX + 22, OY + 5, SK2)
put(OX + 23, OY + 5, SK2)
# far ear: soft inner tint
for x, y in [(28, 3), (29, 3), (29, 4)]:
    put(OX + x, OY + y, SK1)

# eye (dark 2x2 with a bright catch-light)
for x, y in [(28, 10), (29, 10), (28, 11), (29, 11)]:
    put(OX + x, OY + y, DARK)
put(OX + 28, OY + 10, WHT)
# nose tip and muzzle shading
put(OX + 32, OY + 11, GLD)
put(OX + 31, OY + 11, GLD)
put(OX + 32, OY + 10, SK1)
put(OX + 31, OY + 12, SK1)
# cheek
put(OX + 29, OY + 13, SK1)
put(OX + 30, OY + 13, SK1)

f2.outline(DARK)

ch = {0: '.', 1: '#', 2: 'o', 3: 'x', 4: '@', 5: 's', 6: 'S', 7: 'g'}
for y in range(H):
    row = ''
    for x in range(W):
        row += ch[f2.get(x, y)]
    print('%2d |%s|' % (y, row))
print('    ' + ''.join(str(x % 10) for x in range(W)))
