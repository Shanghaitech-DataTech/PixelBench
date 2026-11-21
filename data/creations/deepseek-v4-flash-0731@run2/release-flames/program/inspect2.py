from pixelbench_api import input_canvas

print("FIRE region (28,8)-(46,34):")
print(input_canvas.matrix_text(region=(28, 8, 46, 34)))
print()
print("LEGS region (6,28)-(38,62):")
print(input_canvas.matrix_text(region=(6, 28, 38, 62)))
print()
print("HEAD region (10,0)-(36,18):")
print(input_canvas.matrix_text(region=(10, 0, 36, 18)))
