c = input_canvas
sym = {0: '.', 1: 'A', 2: 'B', 3: 'C', 4: 'N', 5: 'e', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 's', 11: 'T', 12: 'U', 13: 'V'}
w, h = 112, 157
step = 3
print('    ' + ''.join(str((x//step) % 10) for x in range(0, w, step)))
for y in range(0, h, step):
    row = ''
    for x in range(0, w, step):
        row += sym.get(c.get(x, y), '?')
    print('%3d %s' % (y, row))
print()
print('A=c0 darkbrown B=c1 brown C=c2 tan N=c3 navy e=c4 brown F=c5 orange G=c6 yellow H=c8 grey I=c9 pale s=shadowshadow')
