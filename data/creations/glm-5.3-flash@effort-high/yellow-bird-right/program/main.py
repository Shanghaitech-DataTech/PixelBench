result = input_canvas.copy(name='output')

# palette indices of the colours we remap (right parrot only, x >= 32)
BLUE   = result.color('#0097e0')   # main body blue   (c2)
LBLUE  = result.color('#2ecdf5')   # light blue       (c7)
BEAK   = result.color('#ffcf1a')   # yellow beak      (c3)

BODY_Y  = result.color('#ffd21f')   # main yellow
LIGHT_Y = result.color('#ffe98a')   # pale yellow highlight
ORANGE  = result.color('#f57f17')   # orange beak

w, h = 64, 64
for y in range(h):
    for x in range(32, w):
        i = result.get(x, y)
        if i == BLUE:
            result.set(x, y, BODY_Y)
        elif i == LBLUE:
            result.set(x, y, LIGHT_Y)
        elif i == BEAK:
            result.set(x, y, ORANGE)

print(result.stats_text())
finish(result)
