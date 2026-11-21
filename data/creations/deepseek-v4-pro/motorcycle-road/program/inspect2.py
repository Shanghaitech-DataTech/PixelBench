from pixelbench_api import *

# rebuild the same result quickly by importing? Re-run drawing inline is tedious;
# just load the saved state from previous run? Not saved. We'll re-run main drawing code.
exec(open('main.py').read())
print(result.matrix_text(region=(0, 32, 63, 63)))
