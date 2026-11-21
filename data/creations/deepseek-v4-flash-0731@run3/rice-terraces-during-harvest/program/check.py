from draw_terraces import build
from pixelbench_api import canvas

c = build()
print("=== top plateau village (0,0)-(30,14) ===")
print(c.matrix_text(region=(0, 0, 30, 14)))
print("=== mid plateau (30,0)-(63,12) ===")
print(c.matrix_text(region=(30, 0, 63, 12)))
