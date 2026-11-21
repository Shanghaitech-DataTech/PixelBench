from pixelbench_api import new_canvas  # noqa
src = open("main.py").read()
head = src.split("print(c.stats_text())")[0]
exec(head, globals())
print("== walls, furnace, sign, door (28,55)-(100,105) ==")
print(c.matrix_text(region=(28, 55, 100, 105)))
