from pixelbench_api import *

s = input_canvas.select(0, 0, 93, 128)
r = s.rotate(125, algorithm="rotsprite")
rot = r.preview()
b = rot.stats()['bbox']
crop_w = b[2] - b[0] + 1
crop_h = b[3] - b[1] + 1
s2 = rot.select(b[0], b[1], crop_w, crop_h)
knife = s2.preview()

def make_ghost(src, alpha_factor):
    w, h = src.stats()['size']
    g = new_canvas(w, h)
    pal = {p['index']: p['rgba'] for p in src.palette()}
    for y in range(h):
        for x in range(w):
            idx = src.get(x, y)
            if idx is None:
                continue
            r_, g_, b_, a = pal[idx]
            if a <= 0:
                continue
            na = int(round(a * alpha_factor))
            if na <= 0:
                continue
            g.set(x, y, (r_, g_, b_, na))
    return g

W, H = 240, 120
out = new_canvas(W, H, name="result")
main_x = 70
main_y = 40
ghosts = [(main_x-22, main_y, 0.40), (main_x-44, main_y, 0.20), (main_x-66, main_y, 0.09)]
for gx, gy, fac in ghosts:
    out.blit(make_ghost(knife, fac), gx, gy)

slash_outer = [(24, 73), (70, 65), (170, 63), (214, 73), (170, 80), (70, 79)]
slash_inner = [(40, 73), (76, 68), (164, 67), (204, 73), (164, 77), (76, 77)]
out.poly(slash_outer, (255, 255, 255, 70), fill=True)
out.poly(slash_inner, (255, 255, 255, 200), fill=True)
out.line(45, 73, 198, 73, (255, 255, 255, 255))
out.blit(knife, main_x, main_y)

print(out.matrix_text(region=(0, 55, 239, 90), indices=False))
