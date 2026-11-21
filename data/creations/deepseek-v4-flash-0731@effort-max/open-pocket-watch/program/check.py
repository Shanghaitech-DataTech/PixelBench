from pixelbench_api import load
c = load("exports/open-pocket-watch.pixelart.json", add=False)
print(c.matrix_text(region=(0, 0, 63, 20)))
print(c.matrix_text(region=(0, 21, 63, 43)))
print(c.matrix_text(region=(0, 44, 63, 63)))
