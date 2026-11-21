import numpy as np

c = input_canvas
W, H, rgba = c.to_rgba()
arr = np.frombuffer(rgba, dtype=np.uint8).reshape(H, W, 4)

print('    ' + ''.join(str(x % 10) for x in range(W)))
for y in range(7, 22):
    row = ''
    for x in range(W):
        t = tuple(arr[y, x])
        if t[3] == 0:
            row += '.'
        elif t == (34, 32, 52, 255):
            row += 'K'
        elif t == (238, 195, 154, 255):
            row += 'S'
        elif t == (223, 113, 38, 255):
            row += 'O'
        elif t == (143, 86, 59, 255):
            row += 'B'
        elif t == (132, 126, 135, 255):
            row += 'G'
        else:
            row += '?'
    print('%2d  %s' % (y, row))
