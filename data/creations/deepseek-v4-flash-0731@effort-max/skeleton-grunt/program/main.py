# Skeleton Grunt - 32x32 RPG enemy (transparent background)
G = [['.'] * 32 for _ in range(32)]

def put(y, x, ch):
    if 0 <= x < 32 and 0 <= y < 32:
        G[y][x] = ch

def putr(y, x0, x1, ch):
    for x in range(x0, x1 + 1):
        put(y, x, ch)

C = {
    'a': (232, 216, 186),   # bone base
    's': (166, 146, 112),   # bone shadow
    'j': (106, 88, 62),     # dark joint shading
    'k': (70, 56, 42),      # dark teeth gaps
    'o': (26, 21, 16),      # dark outline
    'u': (20, 14, 12),      # eye sockets
    'r': (232, 64, 42),     # eye glow
    'b': (240, 246, 254),   # blade highlight
    'c': (150, 162, 178),   # blade steel
    'd': (92, 100, 118),    # blade edge
    'h': (104, 70, 38),     # grip
    'n': (52, 40, 30),      # guard / pommel
    'm': (100, 106, 118),   # shield rim
    'W': (136, 92, 52),     # wood base
    'w': (196, 150, 96),    # wood light
    'M': (208, 216, 228),   # shield boss light
}

# ---------------- SKULL (facing left, leaning forward) ----------------
putr(3, 14, 16, 'a')
putr(4, 13, 17, 'a')
putr(5, 12, 18, 'a')
putr(6, 12, 18, 'a')
put(6, 12, 'o'); put(6, 18, 'o')
put(7, 12, 'o'); put(7, 13, 'u'); put(7, 14, 'u'); put(7, 15, 'a'); put(7, 16, 'u'); put(7, 17, 'u'); put(7, 18, 'o')
put(8, 12, 'o'); put(8, 13, 'u'); put(8, 14, 'u'); put(8, 15, 'k'); put(8, 16, 'a'); put(8, 17, 'a'); put(8, 18, 'o')
put(9, 12, 'o'); put(9, 13, 'a'); put(9, 14, 'a'); put(9, 15, 'a'); put(9, 16, 'a'); put(9, 17, 'a'); put(9, 18, 'o')
put(10, 12, 'o'); put(10, 13, 'a'); put(10, 14, 'k'); put(10, 15, 'a'); put(10, 16, 'k'); put(10, 17, 'a'); put(10, 18, 'o')
put(11, 12, 'o'); put(11, 13, 'a'); put(11, 14, 'a'); put(11, 15, 'a'); put(11, 16, 'a'); put(11, 17, 'a'); put(11, 18, 'o')
put(8, 14, 'r')   # glowing eye

# ---------------- NECK ----------------
put(12, 14, 'a'); put(12, 15, 'a'); put(12, 16, 'a')
put(12, 13, 'o'); put(12, 17, 'o')

# ---------------- TORSO (hunched ribcage) ----------------
putr(13, 13, 18, 'a'); put(13, 19, 'o')
put(14, 12, 'o'); putr(14, 13, 18, 'a'); put(14, 19, 'o')
put(15, 12, 'o'); put(15, 13, 'a'); put(15, 14, 's'); put(15, 15, 'j'); put(15, 16, 's'); put(15, 17, 'a'); put(15, 18, 'o')
put(16, 12, 'o'); put(16, 13, 'a'); put(16, 14, 'j'); put(16, 15, 'a'); put(16, 16, 'j'); put(16, 17, 'a'); put(16, 18, 'o')
put(17, 13, 'o'); put(17, 14, 's'); put(17, 15, 'j'); put(17, 16, 's'); put(17, 17, 'a'); put(17, 18, 'o')
put(18, 14, 'o'); put(18, 15, 'a'); put(18, 16, 'j'); put(18, 17, 'a'); put(18, 18, 'o')
put(19, 14, 'o'); put(19, 15, 's'); put(19, 16, 'j'); put(19, 17, 'o')
put(20, 15, 'o'); put(20, 16, 'a'); put(20, 17, 'o')

# ---------------- SWORD ARM (right arm from shoulder down to grip) ----------------
put(16, 17, 'a')          # shoulder on torso
put(17, 18, 'a')          # upper arm
put(18, 19, 'a')          # upper arm
put(18, 20, 'j')          # elbow (dark joint)
put(19, 21, 'a')          # forearm
put(19, 22, 'a')
put(19, 23, 'j')          # wrist (dark joint)
put(18, 23, 'a')          # hand gripping

# ---------------- SWORD (short sword, raised, pointing up) ----------------
put(3, 24, 'b')           # tip
for y in range(4, 16):
    put(y, 23, 'd'); put(y, 24, 'b'); put(y, 25, 'd')
put(17, 23, 'n'); put(17, 24, 'n'); put(17, 25, 'n')   # crossguard
put(18, 24, 'h')           # grip
put(19, 24, 'h')
put(20, 24, 'n')           # pommel

# ---------------- LEFT ARM (shield arm forward; hand at shield edge) ----------------
put(14, 13, 'a')          # shoulder

# ---------------- PELVIS ----------------
put(21, 15, 'o'); put(21, 16, 'a'); put(21, 17, 'a'); put(21, 18, 'a'); put(21, 19, 'a'); put(21, 20, 'o')
put(22, 15, 'o'); put(22, 16, 'a'); put(22, 17, 'j'); put(22, 18, 'a'); put(22, 19, 'o')

# ---------------- LEGS (bent, dark joints) ----------------
# front leg (viewer left)
put(23, 15, 'o'); put(23, 16, 'a'); put(23, 17, 'a')
put(24, 16, 's'); put(24, 17, 'j'); put(24, 18, 'a')
put(25, 16, 'a'); put(25, 17, 'a'); put(25, 18, 'a')
put(26, 16, 'j'); put(26, 17, 's'); put(26, 18, 'j')
put(27, 15, 'a'); put(27, 16, 'a'); put(27, 17, 'a'); put(27, 18, 'a')
put(28, 15, 'a'); put(28, 16, 'a'); put(28, 17, 'a'); put(28, 18, 'a')
# back leg (viewer right, slightly back, shaded to separate from front leg)
put(23, 18, 'a'); put(23, 19, 's')
put(24, 19, 'j'); put(24, 20, 's')
put(25, 19, 'a'); put(25, 20, 's')
put(26, 19, 'j'); put(26, 20, 's'); put(26, 21, 's')
put(27, 18, 'a'); put(27, 19, 's'); put(27, 20, 's'); put(27, 21, 's')
put(28, 18, 'a'); put(28, 19, 's'); put(28, 20, 's'); put(28, 21, 's')

# ---------------- SHIELD (small round wooden buckler in front, left) ----------------
import math
cx, cy, r = 8, 19, 4
for y in range(cy - r, cy + r + 1):
    for x in range(cx - r, cx + r + 1):
        if round(math.sqrt((x - cx) ** 2 + (y - cy) ** 2)) <= r:
            put(y, x, 'm')          # metal rim
for y in range(cy - 3, cy + 4):
    for x in range(cx - 3, cx + 4):
        put(y, x, 'W')              # wood
for y in range(cy - 1, cy + 2):
    for x in range(cx - 1, cx + 2):
        put(y, x, 'M')              # boss
put(cy, cx, 'n')
put(17, 7, 'w'); put(17, 8, 'w'); put(16, 8, 'w')
put(16, 9, 'a')           # left hand bone at shield edge

# ---------------- build canvas ----------------
c = new_canvas(32, 32)
for y in range(32):
    for x in range(32):
        ch = G[y][x]
        if ch != '.':
            c.set(x, y, C[ch])

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
finish(c)
