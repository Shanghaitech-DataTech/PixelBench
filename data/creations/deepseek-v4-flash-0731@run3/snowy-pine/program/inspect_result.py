from pixelbench_api import input_canvas
from main import out

print("=== top 0-30 ===")
print(out.matrix_text(region=(16, 0, 65, 30), indices=True))
print("=== mid 55-80 ===")
print(out.matrix_text(region=(10, 55, 75, 80), indices=True))
print("=== lower 100-118 ===")
print(out.matrix_text(region=(0, 100, 81, 118), indices=True))
