from pixelbench_api import *

sel = input_canvas.select(0, 0, 93, 128)
base = sel.rotate(90).preview()   # 128x93, blade tip points right, cutting edge down

out = new_canvas(190, 96)

# white slash streak (behind the knife), along the horizontal thrust path at tip height
tip_y = 5
for dy in range(-4, 5):
    a = max(16, 120 - abs(dy) * 22)
    out.line(10, tip_y + dy, 176, tip_y + dy, (255, 255, 255, a))
out.line(10, tip_y, 176, tip_y, (255, 255, 255, 235))

def afterimage(offx, mult):
    w, h, data = base.to_rgba()
    c = new_canvas(w, h)
    for y in range(h):
        for x in range(w):
            i = (y * w + x) * 4
            r, g, b, a = data[i], data[i + 1], data[i + 2], data[i + 3]
            if a > 0:
                c.set(x, y, (r, g, b, int(a * mult)))
    return c

base_dx = 56
base_dy = 2
for off, mult in [(72, 0.16), (48, 0.32), (24, 0.55)]:
    out.blit(afterimage(off, mult), base_dx - off, base_dy)

out.blit(base, base_dx, base_dy)

print(out.stats_text())
finish(out)
