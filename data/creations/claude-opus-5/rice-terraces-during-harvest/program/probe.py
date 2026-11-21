import runpy, sys
sys.argv = ["main"]
g = runpy.run_path("main.py", init_globals=globals())
c = g["c"]
print(c.matrix_text(region=(0, 4, 63, 16)))
