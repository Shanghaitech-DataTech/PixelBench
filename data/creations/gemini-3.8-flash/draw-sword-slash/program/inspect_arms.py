colors = {
    0: ' ', # transparent
    1: 'X', # c0 black
    2: 'B', # c1 dark purple-black
    4: 'D', # c3 blue-gray gi
    5: 'E', # c4 dark gi
    6: 'F', # c5 gi shade
    7: 'G', # c6 hakama light
    8: 'H', # c7 hakama mid
    9: 'I', # c8 hakama dark / hilt
    10: 'J', # c9 hilt dark
    11: 'S', # c10 skin
    12: 'W', # c11 white
    13: 'M', # c12 gray
    14: 'N', # c13 silver
    15: 'L', # c14 blue
}

print("Y 20-50, X 25-62:")
for y in range(20, 52):
    line = f"{y:2d}: "
    for x in range(25, 62):
        c = input_canvas.get(x, y)
        line += colors.get(c, '?')
    print(line)
