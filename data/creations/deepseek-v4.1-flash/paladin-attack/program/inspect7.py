c = input_canvas
for y in range(61):
    s = ''
    for x in range(43):
        i = c.get(x,y)
        if i == 0: s += ' '
        elif i == 41: s += '.'
        else: s += '#'
    print('%2d|%s|' % (y, s))
