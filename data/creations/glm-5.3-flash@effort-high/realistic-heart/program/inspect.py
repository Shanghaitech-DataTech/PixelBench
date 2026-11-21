from pixelbench_api import load

c = load("exports/heart.pixelart.json", add=False)
print(c.matrix_text())
