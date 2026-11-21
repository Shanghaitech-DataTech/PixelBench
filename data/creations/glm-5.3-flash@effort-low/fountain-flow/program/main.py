c = input_canvas.copy(name='output')
for y in range(3, 21):
    c.set(31, y, 7)
    if y % 2 == 0:
        c.set(30, y, 6)
        c.set(32, y, 6)
c.set(30, 2, 7); c.set(31, 1, 7); c.set(32, 2, 7)
c.set(29, 3, 6); c.set(33, 3, 6)
for x in range(20, 31):
    y = 3 + (30 - x) ** 2 // 22
    c.set(x, y, 7)
    if x % 2 == 0:
        c.set(x, y + 1, 6)
for x in range(32, 43):
    y = 3 + (x - 32) ** 2 // 22
    c.set(x, y, 7)
    if x % 2 == 0:
        c.set(x, y + 1, 6)
for (x, y) in [(24, 22), (22, 24), (27, 24), (38, 22), (40, 24), (35, 24),
               (26, 23), (36, 23), (21, 26), (41, 26), (31, 23), (31, 25)]:
    c.set(x, y, 7)
for (x, y) in [(23, 23), (39, 23), (29, 24), (33, 24)]:
    c.set(x, y, 6)
for x0 in (17, 27, 37):
    for dx in range(11):
        x = x0 + dx
        y = 26 + abs(dx - 5)
        if c.get(x, y) in (6, 7):
            c.set(x, y, 4 if dx % 2 else 5)
print(c.matrix_text(region=(18, 0, 46, 30)))
finish(c)
