from pixelbench_api import *

W, H = 31, 26
OX, OY = 2, 4

# Frame 1 preserves every source pixel, adding transparent room for the motion.
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, OX, OY)

# Frame 2 uses the same stage and palette.
f2 = new_canvas(W, H, name="frame_2_wings_up")
dark = "c0"
body_mid = "c1"
membrane = "c3"
membrane_hi = "c2"
membrane_shade = "c7"

# Raised left wing, from the shoulder toward a high pointed tip.
left_outer = [
    (12, 13), (10, 10), (8, 7), (5, 4), (1, 0), (0, 1),
    (1, 5), (3, 9), (5, 8), (6, 12), (8, 10),
    (9, 14), (11, 13)
]
f2.poly(left_outer, dark)
left_inner = [
    (11, 12), (9, 9), (7, 7), (5, 5), (2, 2), (2, 5),
    (4, 8), (5, 7), (6, 10), (7, 9), (9, 13), (10, 12)
]
f2.poly(left_inner, membrane)

# Wing fingers divide the membrane into readable facets.
f2.line(11, 12, 8, 7, dark)
f2.line(8, 7, 1, 0, dark)
f2.line(8, 7, 3, 9, dark)
f2.line(8, 7, 6, 12, dark)
f2.line(11, 12, 9, 14, dark)
f2.poly([(7, 7), (5, 5), (2, 2), (2, 5), (4, 8)], membrane_hi)
f2.poly([(8, 8), (7, 9), (9, 13), (10, 12), (9, 9)], membrane_shade)
f2.set(1, 2, membrane_hi)
f2.set(2, 3, membrane_hi)

# Mirror the full wing around the bat's centerline.
right_wing = f2.select(0, 0, 13, 15).flip("h").preview()
f2.blit(right_wing, 18, 0)

# Keep the supplied head and torso pixels intact in the animated pose.
core = input_canvas.select(9, 0, 9, 16).preview()
f2.blit(core, 11, 4)

# Shoulder joints sit in front of the membranes.
f2.line(11, 11, 13, 13, dark)
f2.line(19, 11, 17, 13, dark)
f2.set(11, 12, membrane)
f2.set(19, 12, membrane)

# Add equal transparent breathing room around both poses.
out1 = new_canvas(35, 30, name="frame_1_original_final")
out2 = new_canvas(35, 30, name="frame_2_wings_up_final")
out1.blit(f1, 2, 2)
out2.blit(f2, 2, 2)

print(out1.stats_text())
print(out2.stats_text())
view(out1, scale=14, margin=0)
view(out2, scale=14, margin=0)
finish([out1, out2])
