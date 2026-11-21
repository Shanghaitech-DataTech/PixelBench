W, H = 63, 63
OX = 8

# Frame 1: original picture, placed on a larger canvas so the flame can fly forward
f1 = new_canvas(W, H, name='f1')
f1.blit(input_canvas, OX, 0)

# Frame 2: copy, then pose + fire edits
f2 = f1.copy(name='f2')

# --- pose: lean in. Shift head+torso (rows 0..31) right by 2 px ---
torso = f2.select(OX + 10, 0, 24, 32)
torso.move_to(OX + 12, 0, f2, mode='replace')

# --- left (rear) foot steps forward: shift foot block right by 4 px ---
foot = f2.select(OX + 0, 53, 15, 10)
foot.move_to(OX + 4, 53, f2, mode='replace')

# erase ember residue left behind by the torso shift (streak start overlaps old pose)
for x in range(10, 26):
    for y in range(14, 26):
        idx = f2.get(x, y)
        if idx in (f2.color('#f27219ff'), f2.color('#f4a30cff'), f2.color('#fed32cff')):
            f2.set(x, y, None)

# --- fire spell flying forward with trail ---
M = '#f27219ff'  # orange
N = '#f4a30cff'  # amber
O = '#fed32cff'  # yellow

# trail: tapered streak of embers behind the fireball
trail = [
    (34, 21, M), (35, 20, N), (35, 22, M),
    (36, 21, O), (37, 20, M), (37, 22, N),
    (38, 21, N), (38, 23, M), (39, 20, O),
    (40, 21, M), (40, 22, N), (41, 20, M),
    (41, 23, M), (42, 21, N), (42, 22, O),
    (43, 20, M), (43, 22, M), (44, 21, N),
]
for x, y, col in trail:
    f2.set(x, y, col)

# fireball core
f2.circle(49, 21, 3, M, fill=True)
f2.circle(49, 21, 2, N, fill=True)
f2.set(49, 21, O)
f2.set(48, 20, O)
# flicker tongues on the leading edge
f2.set(53, 21, N)
f2.set(52, 19, M)
f2.set(52, 23, M)
f2.set(54, 20, M)
f2.set(54, 22, M)
print(f1.stats_text())
print(f2.stats_text())
save('frame1', f1)
save('frame2', f2)
finish([f1, f2])
