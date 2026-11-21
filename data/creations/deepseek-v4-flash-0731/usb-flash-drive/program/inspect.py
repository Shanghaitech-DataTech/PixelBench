from pixelbench_api import new_canvas, finish, canvas

# Rebuild by importing logic from main source is not needed; use runtime canvas
c = canvas(-1)
print(c.matrix_text(region=(8, 2, 24, 30), indices=False))
finish(c)
