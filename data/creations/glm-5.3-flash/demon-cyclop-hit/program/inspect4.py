c = input_canvas
t = c.copy(name="t3")
marks = {(0,0): (255,0,255), (36,0): (0,255,255), (0,32): (255,255,0),
         (36,32): (0,0,255), (18,16): (255,0,0), (27,32): (0,255,0), (7,32): (255,128,0)}
for (x,y),col in marks.items():
    t.set(x,y,col)
s = t.select(0,0,37,33)
r = s.rotate(12, algorithm="rotsprite")
pv = r.preview()
w,h,data = pv.to_rgba()
print("preview size:", w, h)
for (x,y),col in marks.items():
    best = None
    bestd = 1e9
    for yy in range(h):
        for xx in range(w):
            i = (yy*w+xx)*4
            if data[i+3] > 0:
                d = (data[i]-col[0])**2 + (data[i+1]-col[1])**2 + (data[i+2]-col[2])**2
                if d < bestd:
                    bestd = d; best = (xx,yy)
    print(f"  {col} at ({x},{y}) -> {best} (dist {bestd})")
