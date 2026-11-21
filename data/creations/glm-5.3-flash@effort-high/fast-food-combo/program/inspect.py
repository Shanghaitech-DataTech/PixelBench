import pixelbench_api as api

src = open("main.py").read().replace("finish(c)", "")
ns = {"new_canvas": api.new_canvas, "finish": lambda *a: None}
exec(src, ns)
c = ns["c"]

p = api.view(c, scale=8, margin=0)
print("preview:", p)
