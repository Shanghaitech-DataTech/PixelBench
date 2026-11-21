W, H = 110, 119
src = input_canvas

def blank(name):
    return new_canvas(W, H, background=None, name=name)

def shear(c, k):
    # shift each row horizontally: rows near top shift one way, bottom anchored
    for y in range(H):
        dx = int(round(k * (H - 1 - y)))
        for x in range(66):
            idx = src.get(x, y)
            if idx is not None and idx != 0:
                nx = x + dx + 22
                if 0 <= nx < W:
                    c.set(nx, y, idx)
    return c

def mirror(c):
    for y in range(H):
        for x in range(66):
            idx = src.get(x, y)
            if idx is not None and idx != 0:
                c.set(66 - 1 - x + 22, y, idx)
    return c

f1 = blank('f1'); shear(f1, -0.22)
f2 = blank('f2'); shear(f2, 0.22)
f3 = blank('f3'); mirror(f3)

print(f1.stats_text()); print(f2.stats_text()); print(f3.stats_text())
finish([f1, f2, f3])
