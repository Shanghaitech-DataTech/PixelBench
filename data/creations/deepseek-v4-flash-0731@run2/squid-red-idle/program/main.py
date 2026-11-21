from pixelbench_api import *

src = input_canvas
W, H = 58, 60
SH = 57
K = 44  # seam: torso rows 0..44 bob; legs rows 44..56 stay planted

def build(bob, name):
    f = new_canvas(W, H, name=name)
    moving = src.copy(name=name + "_m")
    moving.clear(0, K + 1, W, SH - (K + 1))   # rows 0..K bob
    static = src.copy(name=name + "_s")
    static.clear(0, 0, W, K)                  # rows K..56 planted
    f.blit(static, 0, 2)                      # seams align at canvas row 2+K
    f.blit(moving, 0, 2 + bob)                # torso bobs on top
    return f

f1 = build(0, "f1")
f2 = build(-1, "f2")
f3 = build(1, "f3")

# verify f1 rows 2..58 equal source rows 0..56, pixel for pixel
pal = src.palette()
mismatch = 0
for sy in range(SH):
    for x in range(W):
        a = pal[src.get(x, sy)]["rgba"][3]
        if a > 0:
            b = pal[f1.get(x, sy + 2)]["rgba"][3]
            if b == 0:
                mismatch += 1
print("f1 missing source pixels:", mismatch)

def vis(c):
    pal = c.palette()
    return sum(1 for y in range(60) for x in range(58) if pal[c.get(x, y)]["rgba"][3] > 0)

print("visible:", vis(f1), vis(f2), vis(f3))
for f in (f1, f2, f3):
    print(f.stats_text())

finish([f1, f2, f3])
