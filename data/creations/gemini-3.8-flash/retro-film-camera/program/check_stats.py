import sys
import math
from pixelbench_api import new_canvas, view, finish, save

def check():
    import main
    c = main.make_camera()
    stats = c.stats()
    print("Colors used:", stats['colors_used'])
    print("Stats:", stats)

check()
