inp = input_canvas
W, H = 58, 57
SPLIT = 44


def band(src, y0, y1):
    t = src.copy()
    if y0 > 0:
        t.clear(0, 0, W, y0)
    if y1 < H - 1:
        t.clear(0, y1 + 1, W, H - (y1 + 1))
    return t


upper = band(inp, 0, 43)
lower = band(inp, 44, 56)
row43 = band(inp, 43, 43)

f1 = new_canvas(58, 58, name='f1')
f1.blit(inp, 0, 1)

f2 = new_canvas(58, 58, name='f2')
f2.blit(upper, 0, 0)
f2.blit(row43, 0, 1)
f2.blit(lower, 0, 1)

f3 = new_canvas(58, 58, name='f3')
f3.blit(upper, 0, 2)
f3.blit(lower, 0, 1)

print('f2 head rows 0-13:')
print(f2.matrix_text(region=(0, 0, 57, 13)))
print('f3 head rows 2-15:')
print(f3.matrix_text(region=(0, 2, 57, 15)))
print('f1 bottom rows 55-57:')
print(f1.matrix_text(region=(0, 55, 57, 57)))
