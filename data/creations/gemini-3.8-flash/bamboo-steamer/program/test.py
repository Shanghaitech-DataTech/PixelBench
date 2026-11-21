import math
from pixelbench_api import *

def test_arrangements():
    # Let's create two canvases to compare
    c1 = new_canvas(32, 32, name="slid_ajar")
    c2 = new_canvas(32, 32, name="tilted_propped")
    
    view(c1)

test_arrangements()
