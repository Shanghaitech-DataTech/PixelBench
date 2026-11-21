# Pose: knife thrusting to the right, cutting edge facing down,
# with semi-transparent afterimages trailing behind and a white slash effect.
ANGLE = 53.0

# --- build the posed knife: mirror h (puts cutting edge downward after rotation), rotate cw ---
work = input_canvas.copy(name="work")
work.mirror("h")
rec = work.select(0, 0, 93, 128).rotate(ANGLE, algorithm="rotsprite")
preview = rec.preview()
bx0, by0, bx1, by1 = preview.stats()["bbox"]
bw, bh = bx1 - bx0 + 1, by1 - by0 + 1
knife = new_canvas(bw, bh, background=None, name="knife")
preview.select(bx0, by0, bw, bh).copy_to(0, 0, knife)
print("posed knife:", bw, bh)

W, H = 288, 96
result = new_canvas(W, H, background=None, name="output")

def ghost(src, factor, name):
    """Copy of src with every pixel's alpha scaled by factor (semi-transparent)."""
    g = src.copy(name=name)
    g.clear()
    mapping = {}
    for e in src.palette():
        r, gr, b, a = e["rgba"]
        if a == 0:
            continue
        na = max(1, int(round(a * factor)))
        mapping[e["index"]] = g.color((r, gr, b, na))
    w, h = src.stats()["size"]
    for y in range(h):
        for x in range(w):
            i = src.get(x, y)
            if i in mapping:
                g.set(x, y, mapping[i])
    return g

k1 = ghost(knife, 0.45, "ghost1")  # nearer afterimage
k2 = ghost(knife, 0.22, "ghost2")  # farther afterimage

tx = W - bw - 6
ty = (H - bh) // 2
print("main knife at", tx, ty)

WHITE = "#ffffff"
GLOW = "#a4add9"
# --- white slash / speed streaks on their own layer ---
slash = new_canvas(W, H, background=None, name="slash")
slash.poly([(30, 39), (212, 37), (212, 42), (34, 43)], WHITE)
slash.poly([(12, 47), (232, 45), (232, 51), (16, 52)], WHITE)
slash.poly([(40, 57), (192, 56), (192, 61), (44, 61)], WHITE)
# swooshing slash arcs sweeping under the blade (3px thick)
for dy in (0, 1, 2):
    slash.path("M 118 %d Q 200 %d 282 %d" % (70 + dy, 79 + dy, 60 + dy), WHITE, fill=False)
    slash.path("M 140 %d Q 210 %d 274 %d" % (76 + dy, 82 + dy, 69 + dy), WHITE, fill=False)
# short speed dashes above the blade
slash.rect(196, 25, 14, 3, WHITE)
slash.rect(228, 20, 10, 3, WHITE)

# tinted glow copy so the white slash reads on any background
glow = slash.copy(name="slash_glow")
glow.clear()
gi = glow.color(GLOW)
opaque = {e["index"] for e in slash.palette() if e["rgba"][3] > 0}
sw, sh = slash.stats()["size"]
for y in range(sh):
    for x in range(sw):
        if slash.get(x, y) in opaque:
            glow.set(x, y, gi)

# --- slash glow rim, then white slash (behind everything else) ---
for ddx, ddy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
    result.blit(glow, ddx, ddy)
result.blit(slash, 0, 0)
# --- afterimages trailing to the left, blending over the slash ---
result.blit(k2, tx - 88, ty)
result.blit(k1, tx - 44, ty)
# --- the posed knife on top ---
result.blit(knife, tx, ty)

view(result)
print(result.stats_text())
save("knife_thrust", result)
finish(result)
