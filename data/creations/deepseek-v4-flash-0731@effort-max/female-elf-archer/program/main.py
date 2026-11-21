from pixelbench_api import *
import math

W, H = 64, 64
c = new_canvas(W, H)

P = {
    '.': None,
    'd': (0x1e, 0x52, 0x30),
    'g': (0x2c, 0x74, 0x40),
    'H': (0x3f, 0x9c, 0x58),
    'h': (0x63, 0xc4, 0x7e),
    'S': (0xf2, 0xd5, 0xb0),
    's': (0xd9, 0xa8, 0x84),
    'E': (0xf8, 0xf8, 0xf4),
    'e': (0x2a, 0x6a, 0x3a),
    'p': (0x14, 0x14, 0x14),
    'b': (0x2c, 0x6a, 0x3c),
    'M': (0xc2, 0x60, 0x60),
    'P': (0xec, 0xab, 0x8d),
    'O': (0xd8, 0xf2, 0xcc),
    'o': (0xa8, 0xe0, 0xa0),
    'Q': (0x7c, 0xc0, 0x7a),
    'G': (0xe8, 0xc0, 0x60),
    'L': (0x8a, 0x5a, 0x2c),
    'l': (0x5e, 0x38, 0x1a),
    'W': (0x7a, 0x4a, 0x22),
    'w': (0x4e, 0x2e, 0x14),
    'A': (0xc8, 0xa8, 0x64),
    'F': (0xd8, 0x50, 0x50),
    'f': (0xef, 0xe8, 0xd8),
    'T': (0xb0, 0xbc, 0xd0),
    'B': (0x54, 0x30, 0x1a),
    'bb': (0x36, 0x1e, 0x0e),
    'X': (0x2f, 0x2a, 0x22),
}

def put(y, x0, x1, ch):
    for x in range(x0, x1 + 1):
        c.set(x, y, P[ch])

def putp(x, y, ch):
    c.set(x, y, P[ch])

# ---------------- shadow ----------------
put(61, 26, 45, 'X'); put(62, 27, 44, 'X'); put(63, 28, 43, 'X')

# ---------------- arrows + quiver (on back, far left figure side) ----------------
arrows = [((15, 3), (21, 13)), ((17, 4), (22, 13)), ((19, 5), (23, 13))]
for (sx, sy), (ex, ey) in arrows:
    c.line(sx, sy, ex, ey, P['A'])
# fletching
for (cx, cy) in [(15, 3), (17, 4), (19, 5)]:
    putp(cx, cy, 'F'); putp(cx - 1, cy, 'f'); putp(cx + 1, cy, 'f'); putp(cx, cy - 1, 'f')
# quiver tube
for y in range(14, 39):
    put(y, 21, 23, 'L')
    putp(22, y, 'l')
put(13, 21, 23, 'l')
putp(21, 14, 'l')

# ---------------- bow (on back, right figure side) ----------------
for y in range(7, 21):
    x = 45 + round(3.0 * math.sin(math.pi * (y - 7) / 13.0))
    putp(x, y, 'W'); putp(x - 1, y, 'w')
putp(45, 6, 'W')
for y in range(24, 43):
    x = 45 + round(3.0 * math.sin(math.pi * (y - 24) / 18.0))
    putp(x, y, 'W'); putp(x - 1, y, 'w')
putp(45, 43, 'W')

# ---------------- hair (back layer) ----------------
for y in range(6, 16):
    put(y, 22, 24, 'g'); put(y, 43, 45, 'g')
for y in range(16, 21):
    put(y, 22, 26, 'g'); put(y, 41, 45, 'g')
for y in range(21, 39):
    put(y, 22, 26, 'g'); put(y, 41, 45, 'g')
    putp(23, y, 'H'); putp(23 + 18, y, 'H')
for y in range(39, 42):
    put(y, 23, 25, 'g'); put(y, 42, 44, 'g')
for y in range(42, 44):
    put(y, 43, 44, 'g')

# ---------------- head / face ----------------
put(4, 30, 37, 'g'); put(4, 32, 35, 'h')
put(5, 29, 38, 'g'); put(5, 31, 36, 'H')
put(6, 31, 36, 'S'); put(6, 30, 30, 'H')
put(7, 29, 40, 'S')
put(8, 25, 42, 'S')
put(9, 24, 43, 'S'); put(10, 24, 43, 'S')
put(11, 24, 43, 'S')
put(12, 24, 43, 'S')
put(13, 24, 43, 'S')
put(14, 24, 43, 'S'); putp(34, 14, 's')
put(15, 24, 43, 'S'); putp(33, 15, 's')
put(16, 25, 42, 'S')
put(17, 26, 41, 'S')
put(18, 27, 40, 'S')
put(19, 28, 39, 'S')
put(20, 30, 37, 'S')
put(21, 30, 37, 'S')
put(22, 31, 36, 'S')

# face features
put(8, 29, 30, 'g'); put(8, 37, 38, 'g')
put(9, 30, 31, 'g'); put(9, 36, 37, 'g')
put(10, 30, 32, 'b'); put(10, 35, 37, 'b')
put(11, 31, 33, 'E'); put(11, 36, 38, 'E')
put(12, 31, 33, 'E'); put(12, 36, 38, 'E')
putp(32, 12, 'e'); putp(33, 12, 'p')
putp(36, 12, 'e'); putp(37, 12, 'p')
put(13, 30, 31, 'P'); put(13, 36, 37, 'P')
put(14, 33, 34, 's')
put(15, 33, 34, 's'); put(14, 30, 31, 'P'); put(14, 36, 37, 'P')
put(16, 33, 36, 'M')
put(17, 34, 35, 'M')

# pointed ear poking from hair (three-quarter view: left ear visible)
putp(20, 8, 'S'); putp(21, 8, 'S'); putp(22, 8, 'S')
putp(20, 9, 'S'); putp(21, 9, 'S'); putp(22, 9, 'S')
putp(20, 10, 'S'); putp(21, 10, 'S')
putp(21, 11, 's'); putp(22, 11, 's')

# ---------------- body ----------------
put(22, 30, 37, 'G')
put(23, 28, 39, 'o'); put(23, 30, 37, 'G')
for y in range(24, 31):
    put(y, 28, 39, 'o')
    put(y, 26, 28, 'O'); put(y, 39, 41, 'o')
    put(y, 29, 31, 'O'); put(y, 32, 35, 'o'); put(y, 36, 38, 'Q')
put(31, 30, 37, 'o'); put(31, 26, 28, 'O'); put(31, 39, 41, 'o')
put(31, 30, 31, 'O'); put(31, 32, 35, 'o'); put(31, 36, 37, 'Q')
put(32, 30, 37, 'G'); put(32, 26, 28, 'o'); put(32, 39, 41, 'o')
# hands
put(33, 31, 36, 'o')
put(33, 31, 36, 'G')
put(34, 30, 37, 'o')
put(35, 30, 38, 'o'); put(35, 26, 28, 'S'); put(35, 39, 41, 'S')
put(36, 30, 39, 'o'); put(36, 26, 28, 'S'); put(36, 39, 41, 'S'); put(37, 37, 39, 'Q')
put(37, 29, 40, 'o'); put(37, 27, 29, 'S'); put(37, 40, 41, 'S'); put(38, 38, 40, 'Q')
put(38, 29, 40, 'o'); put(38, 27, 29, 'S'); put(38, 40, 41, 'S'); put(39, 39, 40, 'Q')
put(39, 28, 41, 'o'); put(40, 40, 41, 'Q')
put(40, 28, 42, 'o'); put(40, 40, 42, 'Q')
put(41, 27, 42, 'o'); put(41, 41, 42, 'Q')
put(42, 27, 43, 'o'); put(42, 41, 43, 'Q')
put(43, 27, 43, 'o'); put(43, 42, 43, 'Q')
put(44, 26, 44, 'o'); put(44, 42, 44, 'Q')
put(45, 26, 44, 'o'); put(45, 42, 44, 'Q')
put(46, 26, 45, 'o'); put(46, 43, 45, 'Q')
put(47, 26, 45, 'o'); put(47, 43, 45, 'Q')
put(48, 25, 46, 'o'); put(48, 43, 46, 'Q')
put(49, 25, 46, 'o'); put(49, 44, 46, 'Q')
put(50, 25, 46, 'o'); put(50, 44, 46, 'Q')
# boots
for y in range(51, 59):
    put(y, 29, 34, 'B'); put(y, 37, 42, 'B')
    putp(33, y, 'bb'); putp(38, y, 'bb')
put(59, 30, 33, 'B'); put(59, 38, 41, 'B'); putp(33, 59, 'bb'); putp(38, 59, 'bb')
put(60, 30, 33, 'bb'); put(60, 38, 41, 'bb')
put(61, 31, 32, 'bb'); put(61, 39, 40, 'bb')

print(c.stats_text())
finish(c)
