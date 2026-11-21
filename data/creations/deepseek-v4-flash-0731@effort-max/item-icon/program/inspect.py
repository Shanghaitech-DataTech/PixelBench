from pixelbench_api import new_canvas, finish, canvas

c = canvas("c2")
# also rebuild same as main (already built by run)
print(c.matrix_text(region=(0, 0, 31, 31), indices=True))
