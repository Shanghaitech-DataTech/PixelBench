from pixelbench_api import *

def build_dragon():
    c = new_canvas(64, 64)
    # Just a test canvas to check view() and verify setup
    c.rect(10, 10, 20, 20, '#ff0000')
    view(c)
    return c

c = build_dragon()
