from pixelbench_api import new_canvas  # noqa
src = open("main.py").read()
head = src.split("print(c.stats_text())")[0]
exec(head, globals())
print("== right wall / furnace (62,58)-(100,104) ==")
print(c.matrix_text(region=(62, 58, 100, 104)))
