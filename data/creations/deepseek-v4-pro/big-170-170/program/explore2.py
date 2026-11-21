from pixelbench_api import *

c = input_canvas
# print indices for regions, compressed to 2 char per pixel? use hex index base62 maybe
# Just print matrix with indices=True for region (0,50)-(130,115) might be wide.
print(c.matrix_text(region=(0,50,130,115), indices=True))
