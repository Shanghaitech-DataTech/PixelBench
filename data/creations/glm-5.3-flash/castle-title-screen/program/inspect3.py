import pixelbench_api as api

src = open("main.py").read().replace("finish(c)", "pass")
ns = {n: getattr(api, n) for n in ("new_canvas", "canvas", "canvases", "flatten",
      "load", "save", "view", "export", "finish", "redraw")}
ns["input_canvas"] = api.input_canvas
exec(compile(src, "main.py", "exec"), ns)
c = ns["c"]

print("== TOP SKY + TITLE (x0-64, y0-30) ==")
print(c.matrix_text(region=(0, 0, 64, 30)))
print()
print("== SEA LEFT (x0-40, y64-112) ==")
print(c.matrix_text(region=(0, 64, 40, 112)))
