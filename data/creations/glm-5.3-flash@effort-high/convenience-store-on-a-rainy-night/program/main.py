from pixelbench_api import save, finish
from scene import build

c = build()
save("store", c)
print(c.stats_text())
finish(c)
