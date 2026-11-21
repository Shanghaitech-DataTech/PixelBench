from pixelbench_api import canvas, view

for name in ('frame1', 'frame2'):
    c = canvas(name)
    print(name, c.stats_text())
    print(view(c, scale=8))
