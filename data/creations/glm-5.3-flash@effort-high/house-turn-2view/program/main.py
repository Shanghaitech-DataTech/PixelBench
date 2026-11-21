from pixelbench_api import *

W, H = 200, 200
work = new_canvas(W, H, name='work')
ix, iy = (W - 112) // 2, (H - 157) // 2
work.blit(input_canvas, ix, iy)

s = work.select(ix, iy, 112, 157)
r45 = s.rotate(45, algorithm="rotsprite")
r90 = s.rotate(90, algorithm="nearest")

f1 = new_canvas(W, H, name='house_45')
p45 = r45.preview()
b45 = p45.stats()['bbox']
w45 = b45[2] - b45[0] + 1
h45 = b45[3] - b45[1] + 1
f1.blit(p45, (W - w45) // 2 - b45[0], (H - h45) // 2 - b45[1])

f2 = new_canvas(W, H, name='house_90')
p90 = r90.preview()
b90 = p90.stats()['bbox']
w90 = b90[2] - b90[0] + 1
h90 = b90[3] - b90[1] + 1
f2.blit(p90, (W - w90) // 2 - b90[0], (H - h90) // 2 - b90[1])

# Sanity: central band of f1 should show coherent rotated house structure.
print("f1 center rows:")
print(f1.matrix_text(region=(60, 60, 140, 100)))
print("f1 stats:", f1.stats_text())
print("f2 stats:", f2.stats_text())

finish([f1, f2])
