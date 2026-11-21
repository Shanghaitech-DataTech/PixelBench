from pixelbench_api import input_canvas

print("input size:", input_canvas.stats()["size"])
print(input_canvas.stats_text())
print("palette:")
for e in input_canvas.palette():
    print(e)
print("matrix:")
print(input_canvas.matrix_text())
