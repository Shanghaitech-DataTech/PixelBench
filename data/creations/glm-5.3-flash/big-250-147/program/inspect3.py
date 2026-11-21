w, h, rgba = input_canvas.to_rgba()

def px(x, y):
    i = (y*w + x)*4
    return (rgba[i], rgba[i+1], rgba[i+2], rgba[i+3])

# average colour per row (ignoring the sun area x 100-150)
print("row-averaged sky colours (excluding x100-150):")
for y in range(0, 147, 3):
    rs = gs = bs = n = 0
    for x in range(0, w):
        if 100 <= x <= 150:
            continue
        r, g, b, a = px(x, y)
        rs += r; gs += g; bs += b; n += 1
    print(y, (rs//n, gs//n, bs//n))
