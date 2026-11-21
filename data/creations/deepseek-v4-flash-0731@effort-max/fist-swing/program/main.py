from pixelbench_api import *

c = input_canvas
DARK = "#222034"   # c0 outline
SKIN = "#eec39a"   # c2 skin

# ---------------- Frame 1: original picture content ----------------
f1 = c.copy("f1")

# ---------------- Frame 2: light punch with the left fist
# (character's left arm = the arm on the right side of the image).
f2 = c.copy("f2")
f2.clear(15, 10, 14, 7)
f2.rect(14, 13, 7, 4, DARK, fill=False)
f2.rect(15, 14, 5, 2, SKIN)
f2.rect(20, 12, 6, 5, DARK, fill=False)
f2.rect(21, 13, 4, 3, SKIN)

print("submit frames:", f1.stats()["size"], f2.stats()["size"])
finish([f1, f2])
