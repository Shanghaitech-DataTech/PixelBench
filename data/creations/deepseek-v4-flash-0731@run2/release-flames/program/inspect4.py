from pixelbench_api import input_canvas

print("FULL RIGHT (24,8)-(47,36):")
print(input_canvas.matrix_text(region=(24, 8, 47, 36)))
print()
print("BOTTOM ROWS (0,44)-(47,63):")
print(input_canvas.matrix_text(region=(0, 44, 47, 63)))
