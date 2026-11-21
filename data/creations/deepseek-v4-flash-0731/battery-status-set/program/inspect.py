from pixelbench_api import finish, new_canvas, load

# Rebuild the same drawing, then print the region matrix for inspection.
exec(open('main.py').read().split("print(c.stats_text())")[0])
print(c.matrix_text(region=(0, 18, 63, 44), indices=True))
