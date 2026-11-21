from pixelbench_api import *

c = canvas('dining')
# Print the full center region around table and fruit bowl
print(c.matrix_text(region=(10, 10, 53, 53), indices=False))
