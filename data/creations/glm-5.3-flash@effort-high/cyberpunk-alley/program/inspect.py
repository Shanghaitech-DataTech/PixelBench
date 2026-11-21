import pixelbench_api as api
src = open("main.py").read().replace("finish(c)", "")
ns = {"new_canvas": api.new_canvas}
exec(src, ns)
c = ns["c"]
print("---- BOTTOM-RIGHT: puddle + reflections ----")
print(c.matrix_text(region=(80, 100, 127, 127)))
