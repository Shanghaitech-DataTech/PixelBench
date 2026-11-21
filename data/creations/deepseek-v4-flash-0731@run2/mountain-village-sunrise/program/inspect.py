from pixelbench_api import *
import main as m

c = canvas("mountain-village-sunrise")
print(c.stats_text())
print("sun+ridge+smoke check")
print(c.matrix_text(region=(30, 14, 110, 58), indices=False))
