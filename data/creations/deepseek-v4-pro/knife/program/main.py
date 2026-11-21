from pixelbench_api import *

WHITE = (255, 255, 255)

# --- rotate the input knife to thrust right, cutting edge down ---
s = input_canvas.select(0, 0, 93, 128)
r = s.rotate(125, algorithm="rotsprite")
rot = r.preview()
b = rot.stats()['bbox']
crop_w = b[2] - b[0] + 1
crop_h = b[3] - b[1] + 1
s2 = rot.select(b[0], b[1], crop_w, crop_h)
knife = s2.preview()   # 154 x 30, transparent background

# --- helper: semi-transparent ghost copy of a canvas ---
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

# --- compose ---
W, H = 240, 96
out = new_canvas(W, H, name="result")

main_x = 76
main_y = 28

# afterimages trailing to the left, increasingly transparent
ghosts = [
    (main_x - 22, main_y, 0.40),
    (main_x - 44, main_y, 0.20),
    (main_x - 66, main_y, 0.09),
]
for gx, gy, fac in ghosts:
    gh = make_ghost(knife, fac)
    out.blit(gh, gx, gy)

# white slash effect behind the main knife
slash_outer = [(30, 61), (76, 53), (176, 51), (220, 61), (176, 68), (76, 67)]
slash_inner = [(46, 61), (82, 56), (170, 55), (210, 61), (170, 65), (82, 65)]
out.poly(slash_outer, (255, 255, 255, 70), fill=True)
out.poly(slash_inner, (255, 255, 255, 200), fill=True)
# crisp bright core line
out.line(51, 61, 204, 61, (255, 255, 255, 255))

# main knife on top
out.blit(knife, main_x, main_y)

print(out.stats_text())
save("knife_thrust", out)
finish(out)
