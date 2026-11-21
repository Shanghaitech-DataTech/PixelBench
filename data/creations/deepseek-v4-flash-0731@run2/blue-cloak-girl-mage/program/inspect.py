from pixelbench_api import *

src = open("main.py").read()
src = src.replace("finish(c)", "pass")
ns = {"__name__": "__main__"}
exec(compile(src, "main.py", "exec"), ns)
c = ns["c"]
c = ns["c"]
for y in range(37, 45):
    print(y, [c.get(x, y) for x in range(41, 49)])
print(c.matrix_text(region=(12, 0, 40, 25)))
