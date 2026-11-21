src = open("main.py").read()
g = globals()
exec(compile(src, "main.py", "exec"), g)
cv = g["cv"]

W = H = 64
w_, h_, buf = cv.to_rgba()
chars = " .:-=+*#%@"
print("coarse luminance map (32x32):")
for by in range(0, H, 2):
    row = ""
    for bx in range(0, W, 2):
        tot = 0; cnt = 0
        for dy in range(2):
            for dx in range(2):
                o = ((by+dy)*W + (bx+dx))*4
                if buf[o+3] > 0:
                    lum = 0.3*buf[o] + 0.59*buf[o+1] + 0.11*buf[o+2]
                    tot += lum; cnt += 1
        row += " " if cnt == 0 else chars[min(9, int((tot/cnt)/255.0*10))]
    print(row)
