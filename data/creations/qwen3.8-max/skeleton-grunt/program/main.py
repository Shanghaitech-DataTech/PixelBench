from pixelbench_api import new_canvas, view, save, finish

PAL = {
    'K': '#151021',  # outline / darkest
    'D': '#5f5346',  # bone shadow, joint shading
    'M': '#a2947c',  # bone mid
    'L': '#d8ccb0',  # bone light
    'W': '#f7f0da',  # bone highlight
    'E': '#e04a26',  # eye glow
    'B': '#3d4759',  # steel dark
    'S': '#7d8aa3',  # steel mid
    'T': '#c3d2e4',  # steel light
    'G': '#3a2a1c',  # leather dark
    'H': '#6b4526',  # leather light
    'P': '#c08a45',  # wood light
    'O': '#8f5c2a',  # wood mid
    'Q': '#5b3a1d',  # wood dark
}

SW = SH = 32
g = [['.'] * SW for _ in range(SH)]


def put(r, c, s):
    assert 0 <= r < SH, ("row", r)
    for i, ch in enumerate(s):
        assert 0 <= c + i < SW, ("col", r, c + i)
        assert ch in PAL or ch == '.', ("bad char", ch, r, c + i)
        g[r][c + i] = ch


# ================= SKULL (sunk low between hunched shoulders) =================
put(3, 13, "KLLLLK")
put(4, 12, "KLWWLLDK")
put(5, 11, "KMWLLLLMDK")
put(6, 11, "KMKKLLKKMK")
put(7, 11, "KMEEKKEEDK")
put(8, 11, "KMLLKKLMDK")
put(9, 12, "KLKLLKLK")          # teeth
put(9, 8, "KDML")                # raised shoulder cap, left
put(9, 20, "LMDK")               # raised shoulder cap, right
put(10, 12, "KDMMMMDK")          # jaw
put(10, 8, "KDML")
put(10, 20, "LMDK")

# ================= SHOULDERS / CHEST =================
put(11, 8, "KDMLLDDDDDDLLMDK")
put(12, 8, "KDMDMLLLLLLMDMDK")

# ================= RIBCAGE / BELT / PELVIS =================
put(13, 11, "KDMLLLLMDK")
put(14, 11, "KDMKMMKMDK")
put(15, 11, "KDMLLLLMDK")
put(16, 11, "KDMKMMKMDK")
put(17, 11, "KDMLLLLMDK")
put(18, 11, "KDKMMMMKDK")
put(19, 11, "KGHGSTGHGK")        # leather belt + iron buckle
put(20, 11, "KMLDGGDLMK")        # pelvis + loincloth
put(21, 12, "KMLGGLMDK")

# ================= RIGHT ARM (sword arm, elbow out) =================
put(13, 21, "MDK")
put(14, 21, "MDK")
put(15, 21, "MDK")
put(16, 21, "DDK")               # elbow joint shading
put(17, 22, "DMD")               # forearm to the fist
put(18, 23, "D")

# ================= LEGS (slightly bowed, crouched) =================
put(22, 12, "KLMDKLMDK")
put(23, 12, "KLMDKLMDK")
put(24, 12, "KDMDKDMDK")         # knee joint shading
put(25, 12, "KDMDKDMDK")
put(26, 11, "KLMDK.KLMDK")       # shins angle out
put(27, 11, "KLMDK.KLMDK")
put(28, 11, "KDDDK.KDDDK")       # ankle joint shading
put(29, 10, "KLLMDK")            # left foot
put(29, 17, "KMLLDK")            # right foot
put(30, 10, "KDDDDK")
put(30, 17, "KDDDDK")

# ================= SWORD (short sword, blade up) =================
put(5, 26, "KTK")                        # point
for r in range(6, 15):
    put(r, 25, "KTSBK")                  # blade: light edge / mid / dark edge
put(15, 24, "KSTTTSK")                   # crossguard top
put(16, 24, "KBSSSBK")                   # crossguard bottom
put(17, 25, "KGHGK")                     # grip
put(22, 25, "KSTK")                      # pommel
put(23, 25, "KBSK")

# ================= FIST (over the grip) =================
put(18, 24, "KMLLMK")
put(19, 24, "DLWWMD")
put(20, 24, "DMKKMD")
put(21, 24, "KDMMDK")

# ================= SHIELD (small round wooden buckler, in front) =================
EXT = {12: (6, 8), 13: (5, 10), 14: (4, 10), 15: (3, 11), 16: (3, 11),
       17: (3, 11), 18: (4, 10), 19: (5, 9), 20: (6, 8)}
inside = set()
for r, (x0, x1) in EXT.items():
    for x in range(x0, x1 + 1):
        inside.add((x, r))
for (x, r) in sorted(inside, key=lambda p: (p[1], p[0])):
    if any((x + dx, r + dy) not in inside for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
        g[r][x] = 'K'                    # dark rim
    else:
        d = (x - 7) + (r - 16)
        g[r][x] = 'P' if d <= -2 else ('Q' if d >= 3 else 'O')
BOSS = {(6, 15): 'T', (7, 15): 'T', (8, 15): 'S',
        (6, 16): 'T', (7, 16): 'S', (8, 16): 'B',
        (6, 17): 'S', (7, 17): 'B', (8, 17): 'B'}
for (x, r), ch in BOSS.items():
    g[r][x] = ch

# ================= render =================
c = new_canvas(SW, SH, name="skeleton_grunt")
for r in range(SH):
    for x in range(SW):
        ch = g[r][x]
        if ch != '.':
            c.set(x, r, PAL[ch])

print("grid:")
for r in range(SH):
    print("%2d|%s|" % (r, "".join(g[r])))
print(c.stats_text())
print(view(c, scale=12))
save("skeleton_grunt", c, indexed=True)
finish(c)
