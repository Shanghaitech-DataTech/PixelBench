W, H, rgba = input_canvas.to_rgba()

def px(x, y):
    i = (y*W + x)*4
    return rgba[i], rgba[i+1], rgba[i+2], rgba[i+3]

def win_mean_r(x, y0, n=6):
    s = 0; c = 0
    for y in range(y0, min(y0+n, H)):
        s += px(x, y)[0]; c += 1
    return s / c

for x in (5, 40, 80, 120, 160, 200, 240):
    prof = []
    for y in range(48, 84, 2):
        prof.append(f"{y}:{win_mean_r(x, y):.0f}")
    print("x=", x, " ".join(prof))
