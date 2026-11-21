from pixelbench_api import *
c = load('exports/main-canvas.pixelart.json') if False else None

# Rebuild check via code
exec(open('main.py').read().split("print(c.stats_text())")[0])
for p in [(13,20),(14,20),(15,20),(17,18),(13,12),(8,24),(14,24)]:
    print(p, c.get(*p), c.color_name(c.get(*p)))
