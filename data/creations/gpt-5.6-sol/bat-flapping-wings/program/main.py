from pixelbench_api import *

# Shared framing gives the raised wings room while retaining the original sprite.
W, H = 31, 26
f1 = new_canvas(W, H, background=None, name="frame_1_original")
f1.blit(input_canvas, 2, 3)

f2 = new_canvas(W, H, background=None, name="frame_2_wings_raised")

dark = "c0"
slate = "c1"
bright = "c2"
deep = "c3"
mid = "c4"
accent = "c7"

left_outline = [
    (11, 11), (10, 8), (8, 6), (6, 4), (3, 1), (0, 1),
    (1, 5), (0, 7), (3, 8), (2, 11), (5, 10), (5, 14),
    (8, 12), (9, 15), (11, 13),
]
left_membrane = [
    (10, 10), (9, 8), (7, 6), (5, 4), (2, 2), (2, 5),
    (1, 6), (4, 7), (3, 10), (6, 9), (6, 12), (8, 10),
    (9, 13), (10, 12),
]
left_upper = [(2, 2), (5, 4), (7, 6), (4, 7), (2, 5)]
left_mid = [(4, 7), (7, 6), (9, 8), (6, 9), (3, 10)]
left_inner = [(6, 9), (9, 8), (10, 10), (10, 12), (9, 13), (8, 10)]

mirror = lambda pts: [(W - 1 - x, y) for x, y in pts]

# Dark outer edge, colored membrane panels, then crisp structural ribs.
f2.poly(left_outline, dark)
f2.poly(mirror(left_outline), dark)
f2.poly(left_membrane, deep)
f2.poly(mirror(left_membrane), deep)
f2.poly(left_upper, bright)
f2.poly(mirror(left_upper), bright)
f2.poly(left_mid, accent)
f2.poly(mirror(left_mid), accent)
f2.poly(left_inner, mid)
f2.poly(mirror(left_inner), mid)

for a, b in [((2, 2), (10, 10)), ((4, 7), (10, 10)), ((3, 10), (10, 11)), ((6, 12), (10, 11))]:
    f2.line(*a, *b, dark)
    ma, mb = mirror([a, b])
    f2.line(*ma, *mb, dark)

# Small highlights echo the segmented shading of the original hanging wings.
for x, y, color in [(3, 3, slate), (5, 5, bright), (2, 6, mid), (5, 8, accent), (7, 10, mid)]:
    f2.set(x, y, color)
    f2.set(W - 1 - x, y, color)

# Preserve the original head and torso exactly; transparent source pixels skip.
body = input_canvas.select(9, 0, 9, 22)
body.copy_to(11, 3, f2, mode="over")

save("bat_flap_frame_1", f1, indexed=True)
save("bat_flap_frame_2", f2, indexed=True)
view(f1, scale=16, margin=1, edges="all")
view(f2, scale=16, margin=1, edges="all")
finish([f1, f2])
