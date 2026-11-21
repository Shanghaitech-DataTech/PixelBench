from pixelbench_api import *

W = H = 256
CX, CY = 128, 112
core = new_canvas(W, H, name="coretest")
core.circle(CX, CY, 9, (255, 244, 212))
core.circle(CX, CY, 7, (255, 232, 168))
core.circle(CX, CY, 5, (255, 250, 236))
core.circle(CX, CY, 3, (255, 255, 255))
core.circle(CX, CY, 2, (255, 255, 255), fill=False)
core.circle(CX, CY, 17, (170, 220, 255, 90), fill=False)
core.circle(CX, CY, 18, (120, 200, 250, 60), fill=False)

print(core.matrix_text(region=(104, 96, 152, 130), indices=False))
print(core.stats())
