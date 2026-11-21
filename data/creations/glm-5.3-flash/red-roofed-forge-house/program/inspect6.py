from pixelbench_api import new_canvas  # noqa
src = open("main.py").read()
head = src.split("print(c.stats_text())")[0]
exec(head, globals())
print("== upper house: roof, ridge, chimney (30,10)-(100,50) ==")
print(c.matrix_text(region=(30, 10, 100, 50)))
