c = input_canvas
print("REGION sword streak (0,40)-(30,56):")
print(c.matrix_text(region=(0, 40, 30, 56), indices=True))
print()
print("REGION hand/grip (30,36)-(56,48):")
print(c.matrix_text(region=(30, 36, 55, 48), indices=True))
