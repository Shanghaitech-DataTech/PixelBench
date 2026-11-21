c = input_canvas
t = c.copy(name="t4")
marks = {(2,2): (250,10,250), (33,2): (10,250,250), (2,29): (250,250,10),
         (33,29): (10,10,250), (18,16): (250,10,10), (26,30): (10,250,10), (9,30): (250,130,10)}
for (x,y),col in marks.items():
    for dx in range(3):
        for dy in range(3):
            t.set(x+dx, y+dy, col)
s = t.select(0,0,37,33)
r = s.rotate(12, algorithm="rotsprite")
pv = r.preview()
w,h,data = pv.to_rgba()
print("preview size:", w, h)
for (x,y),col in marks.items():
    hits = []
    for yy in range(h):
        for xx in range(w):
            i = (yy*w+xx)*4
            if data[i+3] > 0 and data[i]==col[0] and data[i+1]==col[1] and data[i+2]==col[2]:
                hits.append((xx,yy))
    if hits:
        cx = sum(p[0] for p in hits)/len(hits)
        cy = sum(p[1] for p in hits)/len(hits)
        print(f"  block@({x},{y}) -> centre ({cx:.1f},{cy:.1f})  n={len(hits)}")
    else:
        print(f"  block@({x},{y}) -> LOST")
