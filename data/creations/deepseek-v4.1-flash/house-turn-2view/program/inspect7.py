c = input_canvas
chars = {0: '.', 1: 'a', 2: 'b', 3: 'c', 4: 'D', 5: 'e', 6: 'F', 7: 'g', 8: 'h', 9: 'i', 10: 'K', 11: 'k', 12: 'L', 13: 'M'}
x0, y0, x1, y1 = 20, 0, 95, 80
print('    ' + ''.join(str(x % 10) for x in range(x0, x1 + 1)))
for y in range(y0, y1 + 1):
    print('%3d %s' % (y, ''.join(chars.get(c.get(x, y), '?') for x in range(x0, x1 + 1))))
