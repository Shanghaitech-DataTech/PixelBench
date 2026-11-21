from pixelbench_api import load
c = load('exports/ancient-treant-boss.pixelart.json', add=False)
print(c.stats_text())
print(c.matrix_text(region=(96, 96, 164, 164)))
