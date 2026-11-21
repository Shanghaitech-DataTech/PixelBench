from pixelbench_api import *

# Let's run a test script that prints the matrix of Frame 2 blade
import main

for y in range(14, 18):
    row_str = ""
    for x in range(18, 32):
        col_idx = main.c.get(32 + x, y)
        col_name = main.c.color_name(col_idx) if col_idx is not None else ".."
        # match against PALETTE
        short = ".."
        for k, v in main.PALETTE.items():
            if v == col_name:
                short = k
                break
        row_str += f"{short:>5} "
    print(f"y={y}: {row_str}")
