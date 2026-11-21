# Three-frame demon cyclops hit animation.
W, H = 47, 43
outline = "c0"
horn = "c1"
body_hi = "c2"
body_shadow = "c3"
lid = "c4"
eye = "c5"

# Frame 1: exact original content, centered on a slightly larger stage.
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, 5, 6)

# Frame 2: rotate the entire mass into a backward recoil.
pose = input_canvas.select(0, 0, 37, 33).rotate(10, algorithm="rotsprite").preview()
f2 = new_canvas(W, H, name="frame_2_recoil")
f2.blit(pose, 3, 1)

# Remove the planted image-left foot and rebuild it kicked upward.
f2.clear(11, 34, 11, 9)
# Bent leg outline, then inset shadow/body planes.
f2.poly([(18,29),(21,32),(18,35),(16,35),(14,38),(10,38),(9,36),(12,33),(14,31)], outline)
f2.poly([(18,30),(20,32),(17,34),(15,34),(13,37),(10,37),(11,35),(14,32)], body_shadow)
f2.rect(9, 35, 4, 3, outline)
f2.rect(9, 34, 4, 2, horn)
f2.set(13, 35, body_shadow)

# Replace the neutral face with one eye rolled upward and an open mouth.
f2.rect(20, 18, 15, 13, body_hi)
f2.rect(22, 18, 11, 1, lid)
f2.rect(20, 20, 2, 4, lid)
f2.rect(33, 20, 2, 4, lid)
f2.rect(22, 19, 11, 6, eye)
f2.rect(23, 18, 9, 1, eye)
f2.rect(23, 25, 9, 1, lid)
# Pupil pressed against the upper lid.
f2.rect(25, 18, 5, 4, outline)
f2.rect(26, 22, 4, 1, outline)
# Open shocked mouth with pale lower teeth.
f2.rect(23, 27, 9, 1, lid)
f2.rect(22, 28, 11, 3, outline)
f2.rect(23, 31, 9, 1, lid)
f2.rect(24, 28, 2, 1, eye)
f2.rect(29, 28, 2, 1, eye)
f2.rect(25, 30, 5, 1, "#7d2638")

# Frame 3: the same contact pose, remapped through a strong red impact filter.
f3 = new_canvas(W, H, name="frame_3_impact")
red_dark = f3.color("#451722", name="impact_dark")
red_shadow = f3.color("#9b2637", name="impact_shadow")
red_mid = f3.color("#dc3545", name="impact_red")
red_light = f3.color("#ff6970", name="impact_light")
red_flash = f3.color("#ffd0bd", name="impact_flash")
source_palette = {p["index"]: p["rgba"] for p in f2.palette()}
for y in range(H):
    for x in range(W):
        idx = f2.get(x, y)
        rgba = source_palette[idx]
        if rgba[3] == 0:
            continue
        lum = (rgba[0] * 299 + rgba[1] * 587 + rgba[2] * 114) // 1000
        if lum < 45:
            col = red_dark
        elif lum < 130:
            col = red_shadow
        elif lum < 195:
            col = red_mid
        elif lum < 235:
            col = red_light
        else:
            col = red_flash
        f3.set(x, y, col)

# Contact spark and directional speed marks on the struck side.
spark = "#fff1a8"
f3.poly([(8,18),(11,21),(16,22),(12,24),(13,28),(9,25),(5,27),(7,23),(3,21),(8,21)], spark)
f3.set(8, 22, "#ffffff")
f3.line(0, 16, 7, 19, red_light)
f3.line(0, 29, 7, 25, red_light)
f3.line(1, 22, 5, 22, red_flash)

view(f2, scale=10, margin=1, edges="all")
view(f3, scale=10, margin=1, edges="all")
finish([f1, f2, f3])
