import colorsys

w, h, rgba = input_canvas.to_rgba()

def px(x, y):
    i = (y*w + x)*4
    return (rgba[i], rgba[i+1], rgba[i+2], rgba[i+3])

def char_for(c):
    r, g, b, a = c
    hh, ll, ss = colorsys.rgb_to_hls(r/255, g/255, b/255)
    if ll > 0.90: return "W"
    if ll > 0.72: return "w"
    if ll < 0.15: return "#"
    if ll < 0.30: return "%"
    deg = hh*360
    if ss < 0.15: return "0"
    if deg < 20 or deg >= 340: return "R"
    if deg < 45: return "O"
    if deg < 70: return "Y"
    if deg < 160: return "G"
    if deg < 200: return "C"
    if deg < 260: return "B"
    if deg < 300: return "P"
    return "M"

# Fine map of sky region y 0..70, x 0..250 -> 125 cols x 35 rows (2px blocks)
print("SKY region x0-250 y0-70 (2x2 blocks)")
for by in range(0, 70, 2):
    line = ""
    for bx in range(0, 250, 2):
        rs=gs=bs=n=0
        for y in range(by, by+2):
            for x in range(bx, bx+2):
                r,g,b,a = px(x,y); rs+=r; gs+=g; bs+=b; n+=1
        line += char_for((rs//n, gs//n, bs//n, 255))
    print(f"{by:3d} {line}")
