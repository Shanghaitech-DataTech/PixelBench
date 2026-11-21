c = input_canvas
chars = {0: '.', 1: 'a', 2: 'b', 3: 'c', 4: 'D', 5: 'e', 6: 'F', 7: 'g', 8: 'h', 9: 'i', 10: 'K', 11: 'k', 12: 'L', 13: 'M'}

w, h = 112, 157
step = 2
print('    ' + ''.join(str((x//step) % 10) for x in range(0, w, step)))
for y in range(0, h, step):
    row = ''
    for x in range(0, w, step):
        row += chars.get(c.get(x, y), '?')
    print('%3d %s' % (y, row))
