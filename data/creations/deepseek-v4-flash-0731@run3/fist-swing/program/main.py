from pixelbench_api import *

src = input_canvas
W, H = 48, 44

a = "#222034"    # outline (c0)
skin = "#eec39a"  # skin (c2)
br = "#8f563b"    # brown (c5)

f1 = new_canvas(W, H)
f1.blit(src, 0, 0)

# ---- frame 2: light punch with the left fist, arm extends horizontally right ----
f2 = f1.copy(name="f2")

# 1) remove the old raised left fist (rows 16..20, x 1..6)
f2.clear(1, 16, 6, 5)

# 2) left arm extended horizontally to the right from the left shoulder (x6),
#    ending in a fist at the far right (x36-43)
f2.rect(6, 21, 31, 4, a)      # arm outline x6-36, y21-24
f2.rect(7, 22, 29, 2, skin)   # arm fill x7-35, y22-23
f2.rect(36, 20, 8, 5, a)      # fist outline x36-43, y20-24
f2.rect(37, 21, 6, 3, skin)   # fist fill x37-42, y21-23
f2.set(38, 22, br).set(40, 22, br)  # knuckle creases

print(f2.matrix_text(region=(0, 13, 47, 26)))
print("f1:", f1.stats()['size'], "f2:", f2.stats()['size'])
print(f2.stats_text())

finish([f1, f2])
