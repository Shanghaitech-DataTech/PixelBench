from pixelbench_api import *

src = input_canvas
rot = src.select(0, 0, 93, 128).rotate(-56, algorithm="nearest").preview()
knife = rot.select(2, 61, 154, 32).preview("knife")

W, H = 300, 100
out = new_canvas(W, H, name="output")
pal = {e['index']: e['rgba'] for e in knife.palette()}

def stamp(sprite, dx, dy, alpha):
    w, h = sprite.stats()['size']
    for y in range(h):
        for x in range(w):
            idx = sprite.get(x, y)
            r, g, b, a = pal[idx]
            if a == 0:
                continue
            col = out.color((r, g, b, alpha)) if alpha is not None else idx
            out.set(dx + x, dy + y, col)

p1 = out.color((255, 255, 255, 50))
p2 = out.color((255, 255, 255, 80))
p3 = out.color((255, 255, 255, 110))
out.line(60, 28, 268, 28, p1)
out.line(120, 31, 268, 31, p2)
out.line(180, 25, 230, 25, p2)
out.line(60, 68, 265, 68, p2)
out.line(100, 72, 250, 72, p1)

for dx, al in ((6, 42), (34, 78), (62, 116), (90, 158)):
    stamp(knife, dx, 34, al)

out.blit(knife, 118, 34)

white = out.color((255, 255, 255, 255))
soft = out.color((255, 255, 255, 150))
out.path("M 262 46 Q 282 46 290 58 Q 283 76 262 74", soft, fill=False)
out.path("M 266 51 Q 280 51 286 58 Q 281 72 266 70", white, fill=False)
out.line(292, 55, 299, 53, white)
out.line(288, 63, 295, 65, white)

print(out.matrix_text(region=(250, 30, 299, 83)))
finish(out)
