src = open("main.py").read().replace("finish(c)", "pass")
exec(src, globals())

print("=== SIGN (x 58..96, y 12..30) ===")
print(c.matrix_text(region=(58, 12, 96, 30)))
