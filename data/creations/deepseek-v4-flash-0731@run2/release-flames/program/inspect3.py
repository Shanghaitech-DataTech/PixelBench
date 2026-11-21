from pixelbench_api import input_canvas

print("ARMS/HANDS region (14,8)-(40,30):")
print(input_canvas.matrix_text(region=(14, 8, 40, 30)))
print()
print("LOWER BODY region (0,40)-(46,62):")
print(input_canvas.matrix_text(region=(0, 40, 46, 62)))
