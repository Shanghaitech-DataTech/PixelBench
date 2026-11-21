import pixelbench_api as api

src = open("main.py").read().replace("finish(c)", "pass")
ns = {n: getattr(api, n) for n in ("new_canvas", "canvas", "canvases", "flatten",
      "load", "save", "view", "export", "finish", "redraw")}
ns["input_canvas"] = api.input_canvas
exec(compile(src, "main.py", "exec"), ns)
c = ns["c"]

print("== LEFT TOWER TOP (x84-104, y2-20) ==")
print(c.matrix_text(region=(84, 2, 104, 20)))
print()
print("== RIGHT TOWER TOP (x108-128, y10-28) ==")
print(c.matrix_text(region=(108, 10, 128, 28)))
