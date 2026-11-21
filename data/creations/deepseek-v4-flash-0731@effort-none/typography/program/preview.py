from pixelbench_api import *
import main  # reuse? Actually main calls finish. Let me just re-inspect via reading the exported file.

# view the canvas
c = canvas(-1)
print(c.matrix_text(region=(8, 10, 56, 25), indices=False))
print("----")
print(c.matrix_text(region=(8, 30, 56, 48), indices=False))
