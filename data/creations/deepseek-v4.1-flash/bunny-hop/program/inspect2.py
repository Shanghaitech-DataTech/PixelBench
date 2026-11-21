c = input_canvas
ch = {0: '.', 1: '#', 2: 'o', 3: 'x', 4: ' ', 5: 's', 6: 'S', 7: 'g'}
for y in range(28):
    row = ''
    for x in range(26):
        row += ch[c.get(x, y)]
    print('%2d |%s|' % (y, row))
print('    ' + ''.join(str(x % 10) for x in range(26)))
