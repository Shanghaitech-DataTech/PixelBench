from pixelbench_api import *
exec(open("main.py").read().split("view(f1)")[0])
print(f2.stats_text())
view(f2, scale=10, margin=0)
view(f2, size=(512, 512), margin=0)
