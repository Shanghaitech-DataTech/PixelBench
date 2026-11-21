src = open("main.py").read()
exec(compile(src, "main.py", "exec"), globals())
c = canvas(-1)
print(c.matrix_text())
