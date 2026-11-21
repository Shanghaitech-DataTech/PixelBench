from pixelbench_api import canvas
import main  # noqa
c = canvas("teleport_portal")
print(c.matrix_text(region=(8, 8, 39, 39), indices=True))
