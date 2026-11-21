from pixelbench_api import new_canvas, finish, load

c = load("exports/laundromat.pixelart.json", add=False)
print("--- machines region ---")
print(c.matrix_text(region=(0,16,63,46)))
print("--- clock + top ---")
print(c.matrix_text(region=(6,9,53,18)))
print("--- table region ---")
print(c.matrix_text(region=(36,43,63,60)))
