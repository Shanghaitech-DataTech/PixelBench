from pixelbench_api import new_canvas  # noqa
src = open("main.py").read()
head = src.split("print(c.stats_text())")[0]
exec(head, globals())
print("== chimney / ridge region (44,18)-(92,56) ==")
print(c.matrix_text(region=(44, 18, 92, 56)))
