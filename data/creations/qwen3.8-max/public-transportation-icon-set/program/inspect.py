src = open("main.py").read()
ns = dict(globals())
exec(compile(src, "main.py", "exec"), ns)
c = ns["c"]
print("SUBWAY TILE")
print(c.matrix_text(region=(32, 0, 63, 31)))
print("BICYCLE TILE")
print(c.matrix_text(region=(0, 32, 31, 63)))
