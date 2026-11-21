from pixelbench_api import *

c = input_canvas
# Print symbolic (not indices) for vending machine region right side
print("=== vending machine right x90-169 y50-120 ===")
print(c.matrix_text(region=(90,50,169,120)))
