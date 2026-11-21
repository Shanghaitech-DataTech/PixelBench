# Rebuild the drawing (without finishing) and dump text matrices.
src = open("main.py").read().replace("finish(c)", "pass")
ns = dict(globals())
exec(src, ns)
c = ns["c"]
print(c.matrix_text(region=(0, 0, 63, 30)))
print()
print(c.matrix_text(region=(0, 30, 63, 63)))
