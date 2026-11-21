print(input_canvas.matrix_text(region=(15,24,34,43)))
for y in range(24,44):
 print(y, ' '.join(f'{x}:{input_canvas.color_name(input_canvas.get(x,y))}' for x in range(15,35) if input_canvas.get(x,y)))
