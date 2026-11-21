from pixelbench_api import *

c = input_canvas
print("   2345678901234")
for y in range(47):
    row = ''.join('.' if c.get(x,y)==0 else '?' for x in range(35))
    # print letters for x24..34
    lines = c.matrix_text(region=(24,0,34,46)).splitlines()
    # simpler: get char mapping from matrix_text legend via letters
print()
# Use a helper to map index to matrix_text char: replicate by printing matrix_text region
print(c.matrix_text(region=(24,0,34,46)))
