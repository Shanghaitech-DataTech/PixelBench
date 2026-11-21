from pixelbench_api import *

W, H = 40, 47
f2 = new_canvas(W, H, name="f2")
body = input_canvas.select(0, 0, 23, 47).preview()
f2.blit(body, 2, 0)
bow = input_canvas.select(23, 0, 12, 40).preview()
f2.blit(bow, 27, 0)
bridge = {(25, 19): 31, (26, 19): 32,
          (25, 20): 20, (26, 20): 2,
          (25, 21): 32, (26, 21): 14,
          (25, 22): 32, (26, 22): 14,
          (25, 23): 20, (26, 23): 20}
for (x, y), ci in bridge.items():
    f2.set(x, y, ci)
for y in range(7, 19):
    for x in range(29, 34):
        if f2.get(x, y) in (12, 3, 4):
            f2.set(x, y, None)
for y in range(24, 36):
    for x in range(27, 31):
        if f2.get(x, y) in (12, 3, 4):
            f2.set(x, y, None)
print(f2.matrix_text(region=(24, 4, 39, 22), indices=True))
print(f2.matrix_text(region=(24, 22, 39, 40), indices=True))
