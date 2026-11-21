from pixelbench_api import input_canvas, canvases

print("Canvas list:", canvases())
print("Stats:", input_canvas.stats_text())
print("Size:", input_canvas.stats()["size"])
print("Palette:")
for entry in input_canvas.palette():
    print(" ", entry)
print("Matrix:")
print(input_canvas.matrix_text())
