inp = input_canvas
f1 = inp.copy(name='frame1')
f2 = inp.copy(name='frame2')

K = '#222034'
S = '#eec39a'
O = '#df7126'
B = '#8f563b'

# Erase the original arm area (cols 16-28, rows 8-14)
f2.clear(x=16, y=8, w=13, h=7)

# Restore torso outline at col 16
f2.set(16, 8, K)
f2.set(16, 14, K)

# Draw the punch arm (horizontal, extended)
for x in range(16, 27):
    f2.set(x, 9, K)
for y in range(10, 13):
    for x in range(16, 23):
        f2.set(x, y, O)
    for x in range(23, 26):
        f2.set(x, y, S)
    f2.set(26, y, K)
for x in range(16, 27):
    f2.set(x, 13, K)

f2.set(16, 12, B)
f2.set(17, 12, B)

print(f1.stats_text())
print(f2.stats_text())
finish([f1, f2])
