from pixelbench_api import *

def check():
    c = new_canvas(64, 64)
    print("New canvas get(0,0):", c.get(0,0))
    print("New canvas stats:", c.stats())

check()
