# Three-frame hit animation for the supplied demon cyclops.
W, H = 48, 42

# Frame 1: exact original artwork, recentered with room for motion.
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, 5, 7)

# Build recoil by rotating the intact sprite clockwise: the upper body moves
# back to image-right and the image-left (monster-right) foot lifts.
recoil_patch = input_canvas.select(0, 0, 37, 33).rotate(9, algorithm="rotsprite").preview()
f2 = new_canvas(W, H, name="frame_2_recoil")
f2.blit(recoil_patch, 5, 2)

# Face edits are intentionally chunky to match the source pixel language.
outline = "#10191a"
eye_white = "#f5d9c4"
eye_shadow = "#c58c68"
mouth_dark = "#250f16"
tooth = "#ffe3a0"

# Replace the rotated face with an upward-rolled eye and open mouth.
# Eye socket / upper gaze.
f2.rect(22, 16, 12, 8, eye_shadow)
f2.rect(20, 17, 16, 6, eye_white)
f2.rect(25, 16, 6, 6, outline)
f2.rect(26, 16, 4, 3, "#070b0c")
f2.rect(21, 22, 14, 2, eye_shadow)
# Open, startled mouth below the eye.
f2.rect(23, 25, 11, 5, outline)
f2.rect(24, 26, 9, 3, mouth_dark)
f2.set(25, 26, tooth).set(31, 26, tooth)
f2.rect(27, 28, 4, 1, "#d85b55")

# Add a small motion accent near the lifted foot.
f2.line(6, 32, 3, 29, "#f6dda0")
f2.line(7, 34, 3, 34, "#f6dda0")

# Frame 3: same recoil at contact, with impact burst and a red filter applied
# only to visible monster pixels.
f3_base = f2.copy(name="frame_3_base")
f3_base.line(4, 16, 0, 13, "#fff0b8")
f3_base.line(4, 18, 0, 18, "#fff0b8")
f3_base.line(5, 20, 1, 23, "#fff0b8")
f3_base.rect(1, 16, 4, 4, "#ffcf43")
f3_base.set(0, 15, "#ffffff").set(0, 20, "#ffffff")

red_filter = new_canvas(W, H, name="red_impact_filter")
pal = f2.palette()
for y in range(H):
    for x in range(W):
        idx = f2.get(x, y)
        if idx is not None and pal[idx]["rgba"][3] > 0:
            red_filter.set(x, y, "#ef2438a8")

f3 = flatten([f3_base, red_filter], name="frame_3_impact")

finish([f1, f2, f3])
view(f1, scale=10, margin=0)
view(f2, scale=10, margin=0)
view(f3, scale=10, margin=0)
