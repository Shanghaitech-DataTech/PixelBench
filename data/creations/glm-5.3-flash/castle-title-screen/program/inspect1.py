import pixelbench_api as api

src = open("main.py").read().replace("finish(c)", "pass")
ns = {}
for name in ("new_canvas", "canvas", "canvases", "flatten", "load", "save",
             "view", "export", "finish", "redraw", "input_canvas"):
    ns[name] = getattr(api, name, None)
exec(compile(src, "main.py", "exec"), ns)
c = ns["c"]

print("== CASTLE + TOWERS (x85-128, y6-58) ==")
print(c.matrix_text(region=(85, 6, 128, 58), indices=False))
