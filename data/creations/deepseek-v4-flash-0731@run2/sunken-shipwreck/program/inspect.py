from pixelbench_api import load

c = load('exports/wreck.pixelart.json', add=False)
print(c.matrix_text(region=(26, 6, 47, 26)))
print(c.matrix_text(region=(2, 24, 62, 48)))
