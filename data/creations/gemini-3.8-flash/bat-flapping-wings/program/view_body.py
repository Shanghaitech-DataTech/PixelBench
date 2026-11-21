body = new_canvas(27, 22, name="body")
for y in range(22):
    for x in range(27):
        is_body = False
        if y == 0 and x in (10, 16):
            is_body = True
        elif y in (1, 2, 3) and 9 <= x <= 17:
            is_body = True
        elif y in (4, 5) and 9 <= x <= 17:
            is_body = True
        elif y in (6, 7) and 10 <= x <= 16:
            is_body = True
        elif y in (8, 9, 10) and 9 <= x <= 17:
            is_body = True
        elif y in (11, 12, 13, 14) and 10 <= x <= 16:
            is_body = True
        elif y == 15 and x in (11, 15):
            is_body = True
        if is_body:
            body.set(x, y, input_canvas.get(x, y))

view(body)
