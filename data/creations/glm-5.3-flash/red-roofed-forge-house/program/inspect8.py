from pixelbench_api import new_canvas  # noqa
src = open("main.py").read()
head = src.split("print(c.stats_text())")[0]
exec(head, globals())
print("== barrels / yard (88,72)-(124,102) ==")
print(c.matrix_text(region=(88, 72, 124, 102)))
