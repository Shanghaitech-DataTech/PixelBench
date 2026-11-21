print("Palette:")
for i, c in enumerate(input_canvas.palette()):
    print(i, c)

print("\nRegion around hands (x=35..62, y=35..50):")
print(input_canvas.matrix_text((35, 35, 61, 50)))
