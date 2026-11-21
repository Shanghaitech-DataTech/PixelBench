c = input_canvas
print("=== transition (0,55)-(70,72) ===")
print(c.matrix_text(region=(0, 55, 70, 72)))
print()
print("=== black region check (120,50)-(160,70) ===")
print(c.matrix_text(region=(120, 50, 160, 70)))
