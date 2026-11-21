# Three-frame demon cyclops hit animation.
W, H = 45, 41
INK = "#141b1b"
HORN = "#ffe18d"
LIME = "#adbc3a"
GREEN = "#74a334"
BROWN = "#c8966b"
EYE = "#fce2ca"
RED = "#e53935a0"
FLASH = "#fff1b8"

# Frame 1: exact original pixels, centered with room for the motion.
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, 4, 4)

# Build an editable recoil source from the original.
pose = input_canvas.copy(name="recoil_source")

# Eye rolls upward: restore the lower pupil area, then place pupil high.
pose.rect(17, 16, 3, 4, EYE)
pose.rect(17, 15, 3, 3, INK)
pose.set(20, 16, EYE)

# Open mouth below the eye, with a brown lip and deep interior.
pose.poly([(14, 22), (16, 21), (21, 21), (23, 23), (22, 26), (20, 27),
           (16, 27), (14, 25)], BROWN)
pose.poly([(15, 23), (17, 22), (21, 22), (22, 24), (21, 26), (16, 26),
           (15, 25)], INK)
pose.rect(17, 23, 4, 1, HORN)
pose.set(18, 26, "#e5394f")
pose.set(19, 26, "#e5394f")

# Raise the image-left (monster-right) foot into a bent recoil position.
pose.clear(6, 23, 11, 10)
pose.poly([(8, 22), (15, 22), (16, 25), (14, 27), (11, 27), (10, 29),
           (6, 29), (4, 27), (5, 24)], INK)
pose.poly([(9, 23), (14, 23), (15, 25), (13, 26), (10, 26), (9, 28),
           (6, 28), (5, 27), (6, 25)], GREEN)
pose.rect(4, 26, 3, 3, INK)
pose.rect(3, 25, 3, 2, HORN)
pose.set(3, 27, INK)

# Rotate the complete expression and silhouette into a backward lean.
recoil = pose.select(0, 0, 37, 33).rotate(8, algorithm="rotsprite").preview()
f2 = new_canvas(W, H, name="frame_2_recoil")
f2.blit(recoil, 2, 1)

# Frame 3: same landing pose under a red monster-only impact filter.
red_layer = new_canvas(W, H, name="impact_red_filter")
pal = f2.palette()
for y in range(H):
    for x in range(W):
        idx = f2.get(x, y)
        if pal[idx]["rgba"][3] > 0:
            red_layer.set(x, y, RED)
f3 = flatten([f2, red_layer], name="frame_3_impact")

# Contact flash and short force streaks at the left edge of the monster.
f3.poly([(1, 19), (5, 18), (3, 15), (7, 17), (8, 13), (9, 17),
         (13, 15), (10, 19), (13, 21), (9, 21), (8, 25), (6, 21),
         (2, 23), (5, 20)], FLASH)
f3.set(6, 19, "#ffffff")
f3.line(0, 12, 4, 14, "#e5394f")
f3.line(0, 27, 4, 24, "#e5394f")
f3.line(0, 19, 3, 19, "#ffffff")

# Preview the individual deliverables.
view(f1, scale=8, margin=1, edges="all")
view(f2, scale=8, margin=1, edges="all")
view(f3, scale=8, margin=1, edges="all")
finish([f1, f2, f3])
