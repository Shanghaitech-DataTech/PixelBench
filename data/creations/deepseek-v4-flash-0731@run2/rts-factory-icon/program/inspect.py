from pixelbench_api import *
# Rebuild the same drawing by executing main.py logic? Instead, load the saved preview:
import subprocess, os
# Just print matrix of the constructed canvas by re-running the drawing inline:
exec(open("main.py").read().replace("finish(result)", "pass"))
print(result.matrix_text())
