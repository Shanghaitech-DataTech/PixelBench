from pixelbench_api import canvas

# Let's inspect the actual pixels of c from main.py
import main

c = main.c
# Let's print out the text matrix of rows 19 to 30
print("--- ROWS 19 to 30 ---")
for y in range(19, 31):
    row_str = "".join([f"{c.get(x, y):2d} " for x in range(32)])
    print(f"y={y:2d}: {row_str}")
