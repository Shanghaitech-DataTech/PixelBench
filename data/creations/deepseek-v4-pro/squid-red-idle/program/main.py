from pixelbench_api import *

W, H = input_canvas.stats()["size"]
print("input size", W, H)

# Use a taller canvas so the 1px up/down idle bob never clips.
OUT_W = W
OUT_H = H + 2
Y_BASE = 1

f1 = new_canvas(OUT_W, OUT_H, name="frame1")
f1.blit(input_canvas, 0, Y_BASE)          # original content, centered vertically

f2 = new_canvas(OUT_W, OUT_H, name="frame2")
f2.blit(input_canvas, 0, Y_BASE - 1)      # bob up (inhale)

f3 = new_canvas(OUT_W, OUT_H, name="frame3")
f3.blit(input_canvas, 0, Y_BASE + 1)      # bob down (exhale)

for f in (f1, f2, f3):
    print(f.name, f.stats_text())

# Check that the three frames differ only by a vertical shift of opaque pixels.
print("f2 minus f1 row offset check:", f2.stats()["bbox"], f1.stats()["bbox"])
print("f3 bbox:", f3.stats()["bbox"])

finish([f1, f2, f3])
