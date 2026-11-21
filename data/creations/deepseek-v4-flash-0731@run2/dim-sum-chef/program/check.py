from pixelbench_api import load, canvas
c = canvas("dimsum_chef")
print(c.matrix_text(region=(0, 0, 31, 31), indices=False))
