from pixelbench_api import *

def draw_mushroom():
    c = new_canvas(16, 16)
    
    C_OUT = "#2b2b26"
    C_RED = "#d93838"
    C_WHI = "#ffffff"
    C_BEI = "#d1a67e"
    
    # y=1
    for x in range(5, 11): c.set(x, 1, C_OUT)
    
    # y=2
    c.set(4, 2, C_OUT); c.set(11, 2, C_OUT)
    for x in [5,6, 9,10]: c.set(x, 2, C_RED)
    for x in [7,8]: c.set(x, 2, C_WHI)
    
    # y=3
    c.set(3, 3, C_OUT); c.set(12, 3, C_OUT)
    for x in [4,5, 10,11]: c.set(x, 3, C_RED)
    for x in range(6, 10): c.set(x, 3, C_WHI)
    
    # y=4
    c.set(3, 4, C_OUT); c.set(12, 4, C_OUT)
    for x in [4,5, 10,11]: c.set(x, 4, C_RED)
    for x in range(6, 10): c.set(x, 4, C_WHI)
    
    # y=5
    c.set(2, 5, C_OUT); c.set(13, 5, C_OUT)
    for x in [3, 5,6, 9,10, 12]: c.set(x, 5, C_RED)
    for x in [4, 7,8, 11]: c.set(x, 5, C_WHI)
    
    # y=6
    c.set(2, 6, C_OUT); c.set(13, 6, C_OUT)
    for x in [3,4,5, 10,11,12]: c.set(x, 6, C_WHI)
    for x in range(6, 10): c.set(x, 6, C_RED)
    
    # y=7
    c.set(1, 7, C_OUT); c.set(14, 7, C_OUT)
    for x in [2,3, 12,13]: c.set(x, 7, C_RED)
    for x in [4,5, 10,11]: c.set(x, 7, C_WHI)
    for x in range(6, 10): c.set(x, 7, C_RED)
    
    # y=8
    c.set(1, 8, C_OUT); c.set(14, 8, C_OUT)
    for x in [2,3, 12,13]: c.set(x, 8, C_RED)
    for x in range(4, 12): c.set(x, 8, C_OUT)
    
    # y=9
    for x in [2,3,4, 11,12,13]: c.set(x, 9, C_OUT)
    for x in range(5, 11): c.set(x, 9, C_BEI)
    
    # y=10
    c.set(3, 10, C_OUT); c.set(12, 10, C_OUT)
    for x in [4, 7,8, 11]: c.set(x, 10, C_BEI)
    for x in [5,6, 9,10]: c.set(x, 10, C_WHI)
    
    # y=11
    c.set(3, 11, C_OUT); c.set(12, 11, C_OUT)
    for x in [4, 7,8, 11]: c.set(x, 11, C_BEI)
    for x in [5, 10]: c.set(x, 11, C_WHI)
    for x in [6, 9]: c.set(x, 11, C_OUT)
    
    # y=12
    for x in [3,4, 11,12]: c.set(x, 12, C_OUT)
    for x in range(5, 11): c.set(x, 12, C_BEI)
    
    # y=13
    for x in [4, 7,8, 11]: c.set(x, 13, C_OUT)
    for x in [5,6, 9,10]: c.set(x, 13, C_BEI)
    
    # y=14
    for x in [4,5,6, 9,10,11]: c.set(x, 14, C_OUT)
    
    return c

c = draw_mushroom()
finish(c)
