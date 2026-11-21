from pixelbench_api import *

# Reuse the drawing source without its finish side effects by running in its own namespace.
# Simpler: re-execute main.py, then print the lower region.
exec(open('main.py').read())
print(result.matrix_text(region=(0, 32, 63, 63)))
