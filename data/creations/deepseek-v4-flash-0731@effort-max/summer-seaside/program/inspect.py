src = open("main.py").read()
src = src.replace("from pixelbench_api import new_canvas, finish",
                  "from pixelbench_api import new_canvas\n_captured = {}\ndef finish(c):\n    _captured['c'] = c")
src = src.replace("print(c.stats_text())\nfinish(c)", "")
ns = {}
exec(src, ns)
c = ns["c"]
for p in c.palette():
    print(p)
print("---- umbrella region with legend ----")
print(c.matrix_text(region=(74, 96, 120, 127)))
