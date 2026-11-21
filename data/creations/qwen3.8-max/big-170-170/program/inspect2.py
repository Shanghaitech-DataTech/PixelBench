from pixelbench_api import *

print("=== region A: machine upper / person ===")
print(input_canvas.matrix_text(region=(76,58,140,112), indices=True))
print("=== region B: machine lower / bike / legs ===")
print(input_canvas.matrix_text(region=(76,100,140,160), indices=True))
