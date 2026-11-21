from pixelbench_api import *

c = input_canvas
print("canvas name:", c.name if hasattr(c, 'name') else None)
print("stats_text:", c.stats_text())
print("size:", c.stats()['size'])
print("bbox:", c.stats()['bbox'])
print("colors_used:", c.stats()['colors_used'])
print("top_colors:", c.stats()['top_colors'])
print("palette:")
for p in c.palette():
    print(p)
