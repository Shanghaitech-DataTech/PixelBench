from pixelbench_api import *
c = load("exports/store.pixelart.json", add=False)
print(c.stats_text())
print(c.matrix_text(region=(0, 8, 63, 30)))
