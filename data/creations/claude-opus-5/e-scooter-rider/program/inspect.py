import runpy
mod = runpy.run_path("main.py")
c = mod["c"]
print(c.matrix_text(region=(0, 18, 14, 29)))
print(c.stats_text())
