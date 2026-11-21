from pixelbench_api import *
c = load("exports/magic-forest-cottage.pixelart.json", add=False)
print(c.matrix_text(region=(0, 0, 127, 30)))
