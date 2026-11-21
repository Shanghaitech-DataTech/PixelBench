IN = input_canvas

# ---------- Frame 1: original content, preserved, on a larger canvas ----------
f1 = new_canvas(64, 64, name='frame1')
f1.blit(IN, 0, 0)

# ---------- Frame 2: heavy downward smash ----------
f2 = f1.copy(name='frame2')

# 1) erase the raised weapon + raised arm (keep pauldron rows 19-22 x29-36)
f2.rect(27, 8, 37, 2, None)    # x27-63, y8-9
f2.rect(26, 10, 38, 9, None)   # x26-63, y10-18
f2.rect(37, 19, 7, 3, None)    # x37-43, y19-21 (old blade tip)
f2.set(26, 8, None)            # stray grip pixel next to the helm
f2.set(26, 9, None)

# 2) white motion trail: crescent from the old blade position sweeping down
f2.path('M 33 8 C 52 9 61 24 58 45 L 50 46 C 53 29 47 15 30 12 Z', '#ffffff55')
f2.path('M 35 10 C 50 11 57 25 55 42 L 51 42 C 53 29 47 16 32 13 Z', '#ffffff')
f2.path('M 36 12 C 48 14 54 27 52 39', '#ffffd5', fill=False)
for (sx, sy) in [(60, 16), (62, 23), (63, 30), (63, 37), (62, 44), (60, 50), (57, 12), (61, 46)]:
    f2.set(sx, sy, '#ffffff')

# 3) weapon: the same golden sword, now swung down-forward, tip reaching the ground
Tw = new_canvas(22, 34, name='wpn')
J = '#af7a18'; Z = '#d1b563'; G = '#512a13'
Tw.poly([(0, 3), (2, 0), (11, 11), (9, 14)], J)           # grip / shaft
Tw.line(2, 1, 10, 12, Z)                                   # shaft highlight
Tw.line(0, 5, 9, 14, G)                                    # shaft dark edge
Tw.poly([(8, 11), (12, 14), (10, 18), (6, 15)], J)         # crossguard
Tw.line(8, 12, 11, 15, Z)
Tw.poly([(11, 14), (14, 12), (20, 28), (17, 32)], J)       # blade
Tw.line(13, 14, 18, 26, Z)                                 # blade highlight
Tw.line(11, 17, 16, 28, G)                                 # blade dark edge
Tw.outline('#101010')
f2.blit(Tw, 40, 22)

# 4) arm extended down-forward + gauntlet hand gripping the shaft
U = '#332d32'; E = '#a9a5ab'; GG = '#512a13'; K = '#101010'
f2.set(36, 18, K); f2.set(37, 18, K)
f2.set(36, 19, E); f2.set(37, 19, U); f2.set(38, 19, K)
f2.set(36, 20, U); f2.set(37, 20, U); f2.set(38, 20, U); f2.set(39, 20, K)
f2.set(36, 21, U); f2.set(37, 21, U); f2.set(38, 21, U); f2.set(39, 21, K)
f2.set(36, 22, U); f2.set(37, 22, U); f2.set(38, 22, U); f2.set(39, 22, U); f2.set(40, 22, K)
f2.set(36, 23, K); f2.set(37, 23, K); f2.set(38, 23, U); f2.set(39, 23, U); f2.set(40, 23, U); f2.set(41, 23, K)
f2.set(37, 24, K); f2.set(38, 24, GG); f2.set(39, 24, GG); f2.set(40, 24, GG); f2.set(41, 24, GG); f2.set(42, 24, K)
f2.set(37, 25, K); f2.set(38, 25, GG); f2.set(39, 25, GG); f2.set(40, 25, Z); f2.set(41, 25, GG); f2.set(42, 25, K)
f2.set(38, 26, K); f2.set(39, 26, GG); f2.set(40, 26, GG); f2.set(41, 26, GG); f2.set(42, 26, K)
f2.set(39, 27, K); f2.set(40, 27, GG); f2.set(41, 27, GG); f2.set(42, 27, K)
f2.set(40, 28, K); f2.set(41, 28, K)

# 5) left (rear) foot steps forward to put weight behind the blow
s = f2.select(2, 50, 17, 10)
s.move_to(7, 50, f2)
S = '#17003599'
f2.rect(4, 58, 5, 1, S)     # shadow taper behind old stance
f2.rect(23, 58, 6, 1, S)    # shadow bridging to front foot
f2.rect(5, 59, 5, 1, S)
f2.rect(21, 59, 4, 1, S)
f2.rect(11, 60, 6, 1, S)

print('--- frame2 head/neck check ---')
print(f2.matrix_text(region=(14, 0, 40, 14)))
print('--- frame2 weapon + trail ---')
print(f2.matrix_text(region=(36, 20, 63, 50)))
print(f1.stats_text())
print(f2.stats_text())
finish([f1, f2])
