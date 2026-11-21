# skeleton-grunt - 32x32 RPG enemy sprite
# Hunched skeleton warrior: short sword raised beside the skull,
# small round wooden shield held forward, dark joint shading at the
# neck, elbows, spine gaps, hips and knees. Transparent background.

W = H = 32
grid = [['.'] * W for _ in range(H)]


def px(x, y, ch):
    grid[y][x] = ch


def hline(x0, x1, y, ch):
    for x in range(x0, x1 + 1):
        px(x, y, ch)


def vline(x, y0, y1, ch):
    for y in range(y0, y1 + 1):
        px(x, y, ch)


# ============ 1. SHORT SWORD, raised beside the skull ============
px(6, 1, 'S')                                    # tip
for y in range(2, 13):                           # blade, 3 px wide
    px(5, y, 'S')                                # lit edge
    px(6, y, 'm')                                # core
    px(7, y, 's')                                # shaded edge
px(5, 9, 's')                                    # nick in the edge
hline(3, 9, 13, 's')                             # crossguard
px(3, 13, 'S'); px(9, 13, 'S')                   # guard tips catch light
vline(6, 14, 15, 'G')                            # leather grip above the fist
hline(5, 7, 18, 's')                             # pommel below the fist

# ============ 2. LEGS ============
# back leg
vline(11, 23, 25, 'b'); vline(12, 23, 25, 'd')   # thigh
hline(11, 12, 26, 'J')                           # dark knee
vline(11, 27, 28, 'b'); vline(12, 27, 28, 'd')   # shin
hline(10, 13, 29, 'b'); hline(10, 13, 30, 'd')   # foot + sole
# front leg, knee pushed forward
vline(15, 23, 24, 'b'); vline(16, 23, 24, 'd')   # thigh
hline(16, 17, 25, 'b')                           # knee bends ahead
hline(16, 17, 26, 'J')                           # dark knee
vline(16, 27, 28, 'b'); vline(17, 27, 28, 'd')   # shin
hline(16, 19, 29, 'b'); hline(16, 19, 30, 'd')   # foot + sole

# ============ 3. PELVIS ============
hline(12, 15, 19, 'b')                           # waist
hline(11, 16, 20, 'b'); px(11, 20, 'd'); px(16, 20, 'd')
hline(11, 16, 21, 'b'); px(11, 21, 'd'); px(16, 21, 'd')
hline(11, 12, 22, 'J')                           # hip sockets
hline(13, 14, 22, 'd')
hline(15, 16, 22, 'J')

# ============ 4. RIBCAGE (dark gap row between two bright ribs) ============
hline(10, 16, 14, 'b'); px(10, 14, 'd'); px(12, 14, 'B'); px(16, 14, 'd')   # clavicle
hline(11, 16, 15, 'B'); px(11, 15, 'd'); px(15, 15, 'd'); px(16, 15, 'b')   # rib 1
px(10, 16, 'd'); px(11, 16, 'J'); px(12, 16, 'd'); px(13, 16, 'b')
px(14, 16, 'b'); px(15, 16, 'd'); px(16, 16, 'd')                # rib gap, dark inside
hline(11, 16, 17, 'B'); px(11, 17, 'd'); px(15, 17, 'd'); px(16, 17, 'b')   # rib 2
hline(12, 15, 18, 'd'); px(14, 18, 'J')                                     # belly shadow

# ============ 5. HUNCHED NECK + SPINE HUMP ============
px(12, 12, 'd'); px(13, 12, 'J'); px(14, 12, 'b')                # neck under jaw
px(10, 13, 'd'); px(11, 13, 'J'); px(12, 13, 'b')                # humped back
px(13, 13, 'd'); px(14, 13, 'b')                                 # shoulder line

# ============ 6. SKULL (juts forward, to the right) ============
hline(13, 15, 3, 'B')                            # crown
hline(12, 16, 4, 'B'); px(16, 4, 'b')
px(11, 5, 'B'); hline(12, 15, 5, 'B'); px(16, 5, 'b'); px(17, 5, 'b')
px(11, 6, 'B'); hline(12, 13, 6, 'K'); px(14, 6, 'b'); hline(15, 16, 6, 'K'); px(17, 6, 'b')
px(11, 7, 'B'); px(12, 7, 'K'); px(13, 7, 'E'); px(14, 7, 'b')
px(15, 7, 'E'); px(16, 7, 'K'); px(17, 7, 'b')                   # ember pupils
px(11, 8, 'B'); px(12, 8, 'b'); px(13, 8, 'b'); px(14, 8, 'K')
px(15, 8, 'b'); px(16, 8, 'b'); px(17, 8, 'd')                   # cheeks + nose hole
px(11, 9, 'b'); px(12, 9, 'B'); px(13, 9, 'K'); px(14, 9, 'B')
px(15, 9, 'K'); px(16, 9, 'B'); px(17, 9, 'd')                   # upper teeth
px(11, 10, 'b'); hline(12, 16, 10, 'K'); px(17, 10, 'd')         # gaping mouth
hline(13, 15, 11, 'd')                                           # jaw

# ============ 7. SMALL ROUND WOODEN SHIELD, centre (24,17) ============
hline(23, 25, 13, 'v')
hline(22, 26, 14, 'v'); hline(23, 25, 14, 'W')
hline(21, 27, 15, 'v'); hline(22, 24, 15, 'W'); hline(25, 26, 15, 'w')
hline(20, 28, 16, 'v'); hline(21, 22, 16, 'W'); hline(23, 25, 16, 'n'); hline(26, 27, 16, 'w')
hline(20, 28, 17, 'v'); hline(21, 22, 17, 'w'); hline(23, 25, 17, 'n'); hline(26, 27, 17, 'w')
hline(20, 28, 18, 'v'); hline(21, 22, 18, 'w'); hline(23, 25, 18, 'n'); hline(26, 27, 18, 'v')
hline(21, 27, 19, 'v'); hline(22, 26, 19, 'w')
hline(22, 26, 20, 'v'); hline(23, 25, 20, 'w')
hline(23, 25, 21, 'v')
px(23, 16, 'S')                                  # boss highlight
px(25, 18, 's')                                  # boss shade

# ============ 8. ARMS (drawn last, over grip and rim) ============
# left arm, fist wrapped on the grip
px(10, 15, 'b'); px(9, 15, 'b')                  # upper arm
px(9, 16, 'J')                                   # dark elbow
px(8, 16, 'b')                                   # forearm
hline(5, 7, 16, 'b')                             # fist, top row
hline(5, 7, 17, 'd')                             # fist, shaded bottom
# right arm reaching down to the shield rim
px(17, 14, 'b')                                  # shoulder
px(17, 15, 'b')                                  # upper arm
px(17, 16, 'J')                                  # dark elbow
px(18, 16, 'b'); px(19, 16, 'b')                 # forearm
px(19, 17, 'b')
px(20, 17, 'b'); px(20, 18, 'd')                 # fingers over the rim

# ============ emit ============
COLORS = {
    'B': ('bone_light',  '#EFE9D6'),
    'b': ('bone_mid',    '#CFC7AE'),
    'd': ('bone_shade',  '#9C937A'),
    'J': ('joint_dark',  '#5A5340'),
    'K': ('socket',      '#1A1611'),
    'E': ('eye_glow',    '#C8452C'),
    'S': ('steel_light', '#D6DDE4'),
    'm': ('steel_mid',   '#A9B3BE'),
    's': ('steel_dark',  '#7C8592'),
    'G': ('leather',     '#5C4227'),
    'W': ('wood_light',  '#B27E42'),
    'w': ('wood_mid',    '#7E5326'),
    'v': ('wood_dark',   '#4E3013'),
    'n': ('boss_metal',  '#9AA3AE'),
}

used = sorted({ch for row in grid for ch in row if ch != '.'})
missing = [ch for ch in used if ch not in COLORS]
if missing:
    raise SystemExit('undefined chars: %r' % missing)

result = new_canvas(32, 32, background=None, name='skeleton-grunt')
idx = {ch: result.color(hexv, name=name) for ch, (name, hexv) in COLORS.items()}
for y in range(H):
    for x in range(W):
        ch = grid[y][x]
        if ch != '.':
            result.set(x, y, idx[ch])

for y in range(H):
    print('%2d %s' % (y, ''.join(grid[y])))
print(result.stats_text())
finish(result)
