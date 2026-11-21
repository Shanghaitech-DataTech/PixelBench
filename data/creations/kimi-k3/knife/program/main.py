# ---- Pose the knife: rotate 123 deg clockwise so the blade axis is
# horizontal with the tip to the right, then mirror vertically so the
# curved cutting edge faces downward.
sel = input_canvas.select(0, 0, 93, 128).rotate(123, algorithm="rotsprite")
posed = sel.preview("posed")
posed.mirror("v")

bb = posed.stats()["bbox"]
x0, y0, x1, y1 = bb
kw, kh = x1 - x0 + 1, y1 - y0 + 1

knife = new_canvas(kw, kh, name="knife")
knife.blit(posed, -x0, -y0)

palm = {p["index"]: p["rgba"] for p in knife.palette()}

def make_ghost(src, frac, name):
    g = new_canvas(kw, kh, name=name)
    for y in range(kh):
        for x in range(kw):
            r, gg, b, a = palm[src.get(x, y)]
            if a == 0:
                continue
            g.set(x, y, (r, gg, b, max(1, int(round(a * frac)))))
    return g

ghost1 = make_ghost(knife, 0.35, "ghost1")
ghost2 = make_ghost(knife, 0.16, "ghost2")

best = -1
tip_pts = []
for y in range(kh):
    for x in range(kw):
        if palm[knife.get(x, y)][3] > 0:
            if x > best:
                best = x
                tip_pts = [(x, y)]
            elif x == best:
                tip_pts.append((x, y))
tipx = best
tipy = sum(p[1] for p in tip_pts) // len(tip_pts)
print("tip:", tipx, tipy)

PAD_L, PAD_R, PAD_T, PAD_B = 32, 34, 14, 14
W, H = kw + PAD_L + PAD_R, kh + PAD_T + PAD_B
out = new_canvas(W, H, name="output")

KX, KY = PAD_L, PAD_T
TX, TY = KX + tipx, KY + tipy

white = out.color("#ffffff")
white_soft = out.color((255, 255, 255, 130))

# speed lines behind the handle
for (lx0, ly0, lx1, ly1) in [
    (3, KY + kh // 2 - 9, 26, KY + kh // 2 - 10),
    (8, KY + kh // 2 + 1, 36, KY + kh // 2),
    (2, KY + kh // 2 + 11, 22, KY + kh // 2 + 10),
]:
    out.line(lx0, ly0, lx1, ly1, white_soft)

# semi-transparent afterimages trailing the thrust (faintest first)
out.blit(ghost2, KX - 24, KY + 2)
out.blit(ghost1, KX - 12, KY + 1)
out.blit(knife, KX, KY)

# white slash crescent at the tip on its own layer
slash = new_canvas(W, H, name="slash")
cx, cy = TX - 3, TY
slash.circle(cx, cy, 14, white)
slash.circle(cx - 6, cy, 12, None)   # carve inner -> crescent opening left
slash.line(TX - 4, TY, TX + 7, TY, white)   # sparkle at the tip
slash.line(TX + 1, TY - 5, TX + 1, TY + 5, white)

out.blit(slash, 0, 0)

print(out.stats_text())
view(out)
save("knife_thrust", out)
finish(out)
