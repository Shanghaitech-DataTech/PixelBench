# Inspect rows 0 to 80
for y in range(0, 80, 2):
    row_chars = []
    for x in range(112):
        idx = input_canvas.get(x, y)
        if idx == 0:
            row_chars.append('.')
        elif idx == 4: # c3 outline
            row_chars.append('#')
        elif idx in (1, 2, 3): # wood
            row_chars.append('W')
        elif idx in (5, 6, 7): # gold / door / tiles
            row_chars.append('D')
        elif idx in (8, 9, 10): # wall / cream
            row_chars.append(' ')
        elif idx == 11:
            row_chars.append('~')
        else:
            row_chars.append('?')
    print(f"{y:3d}: " + "".join(row_chars))
