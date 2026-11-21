import numpy as np

c = input_canvas
OUT_W, OUT_H = 200, 150

# ---- 1. rotate the knife: mirror so cutting edge goes to the down-right side,
#         then rotate clockwise so the tip points right and the edge faces down
s = c.select(0, 0, 93, 128)
recipe = s.flip(axis="h").rotate(54.4, algorithm="rotsprite")
knife = recipe.preview()          # 159x151, content bbox (3,63)-(156,92)
print("knife preview:", knife.stats_text())

out = new_canvas(OUT_W, OUT_H, name="output")

# ---- 2. semi-transparent afterimages trailing behind (thrust to the right)
def ghost(src, scale):
    w, h, raw = src.to_rgba()
    arr = np.frombuffer(raw, np.uint8).reshape(h, w, 4).copy()
    arr[:, :, 3] = (arr[:, :, 3].astype(np.uint16) * scale // 255).astype(np.uint8)
    g = new_canvas(w, h)
    ys, xs = np.nonzero(arr[:, :, 3])
    for y, x in zip(ys, xs):
        r, gg, b, al = arr[y, x]
        g.set(int(x), int(y), (int(r), int(gg), int(b), int(al)))
    return g

g1 = ghost(knife, 110)   # closer echo
g2 = ghost(knife, 55)    # fainter echo
out.blit(g1, 34 - 34, -2 + 7)    # ~34px behind, drifting up-left
out.blit(g2, 34 - 68, -2 + 14)

# ---- 3. white slash effect sweeping along the thrust line
glow = (255, 255, 255, 55)
mid  = (255, 255, 255, 140)
core = (255, 255, 255, 225)
out.path("M 6 32 C 70 44, 140 58, 198 100 C 140 70, 70 56, 6 38 Z", glow, fill=True)
out.path("M 7 35 C 70 47, 140 61, 196 99 C 140 68, 70 54, 7 37 Z", mid, fill=True)
out.path("M 8 36 C 70 48, 140 62, 194 98", core, fill=False)

# ---- 4. main knife on top: tip at ~(190, 75), edge facing downward
knife.copy_to(34, -2, out, mode="over")

# ---- 5. impact sparkle at the tip + small speed ticks behind the thrust
tx, ty = 191, 75
out.set(tx, ty, core)
out.set(tx + 1, ty, mid); out.set(tx - 1, ty, mid)
out.set(tx, ty - 1, mid); out.set(tx, ty + 1, mid)
out.set(tx + 3, ty - 1, glow); out.set(tx + 3, ty + 2, glow)
out.line(16, 56, 30, 56, mid)
out.line(10, 70, 22, 70, glow)

print(out.stats_text())
save("knife_thrust", out)
finish(out)
