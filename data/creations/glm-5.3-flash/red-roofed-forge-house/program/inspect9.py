from pixelbench_api import new_canvas  # noqa
src = open("main.py").read()
head = src.split("print(c.stats_text())")[0]
exec(head, globals())
print("== left dressing: pine, rocks, bushes, path (0,55)-(70,124) ==")
print(c.matrix_text(region=(0, 55, 70, 124)))
