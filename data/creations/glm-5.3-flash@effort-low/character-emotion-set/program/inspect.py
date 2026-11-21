from pixelbench_api import *
c = load('exports/emotions.pixelart.json', add=False)
print(c.matrix_text(region=(0,0,31,31)))
