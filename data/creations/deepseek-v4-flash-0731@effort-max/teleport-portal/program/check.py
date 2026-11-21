import math
from pixelbench_api import *

exec(open("main.py").read().split("print(c.stats_text())")[0])
print(c.matrix_text(region=(16, 16, 32, 32)))
print(c.matrix_text(region=(0, 0, 10, 10)))
