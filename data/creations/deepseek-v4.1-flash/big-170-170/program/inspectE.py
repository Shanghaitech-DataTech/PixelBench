import colorsys
c = input_canvas
pal = {p['index']: p['rgba'] for p in c.palette()}
B = 10
print("block averages, 10x10 -> hue/lum")
print("     " + "".join("%-2d" % (bx*B) for bx in range(17)))
for by in range(17):
    hue_row = "    "
    lum_row = "    "
    for bx in range(17):
        rs = gs = bs = 0; n = 0
        for y in range(by*B, by*B+B):
            for x in range(bx*B, bx*B+B):
                r, g, b, a = pal[c.get(x, y)]
                rs += r; gs += g; bs += b; n += 1
        r, g, b = rs/n/255, gs/n/255, bs/n/255
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        hue = h*360
        if s < 0.15:
            ch = 'n'
        elif hue < 20 or hue >= 340: ch = 'R'
        elif hue < 45: ch = 'O'
        elif hue < 70: ch = 'Y'
        elif hue < 160: ch = 'G'
        elif hue < 200: ch = 'C'
        elif hue < 260: ch = 'B'
        elif hue < 320: ch = 'M'
        else: ch = 'P'
        hue_row += ch + ("^" if s > 0.4 else " ") if True else ""
        lum_row += ".:-=+#@"[min(6, int(l*7))] + " "
    print("%3d " % (by*B) + hue_row)
    print("    " + lum_row)
