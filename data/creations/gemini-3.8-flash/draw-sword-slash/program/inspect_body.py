# Let's inspect the entire character layout
for y in range(0, 72, 2):
    row_chars = []
    for x in range(0, 62):
        c = input_canvas.get(x, y)
        if c == 0:
            row_chars.append('.')
        elif c == 11: # skin
            row_chars.append('K')
        elif c in (4, 5, 2, 6): # kimono
            row_chars.append('#')
        elif c in (7, 8, 9): # hakama
            row_chars.append('=')
        elif c in (12, 13, 14): # metal / white
            row_chars.append('@')
        else:
            row_chars.append('+')
    print(f"{y:2d}: " + "".join(row_chars))
