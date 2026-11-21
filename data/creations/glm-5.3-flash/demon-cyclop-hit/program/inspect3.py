c = input_canvas
t = c.copy(name="t2")
t.set(27, 32, (255, 0, 255))   # marker at right foot toe
t.set(7, 32, (0, 255, 255))    # marker at left foot toe
s = t.select(0, 0, 37, 33)
r = s.rotate(12, algorithm="rotsprite")
pv = r.preview()
w, h, data = pv.to_rgba()
print("preview size:", w, h)
def find(pred):
    out = []
    for y in range(h):
        for x in range(w):
            i = (y * w + x) * 4
            if data[i + 3] > 0 and pred(data[i], data[i+1], data[i+2]):
                out.append((x, y))
    return out
print("magenta marker:", find(lambda r_,g,b: r_>200 and b>200 and g<100))
print("cyan marker:", find(lambda r_,g,b: g>200 and b>200 and r_<100))
# bbox of all visible pixels
xs = [x for y in range(h) for x in range(w) if data[(y*w+x)*4+3] > 0]
ys = [y for y in range(h) for x in range(w) if data[(y*w+x)*4+3] > 0]
print("visible bbox:", min(xs), min(ys), max(xs), max(ys))
