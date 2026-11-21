from pixelbench_api import load
import glob
p = glob.glob("**/exports/tavern-interior.pixelart.json", recursive=True)
print(p)
c = load(p[0], add=False)
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 33)))
