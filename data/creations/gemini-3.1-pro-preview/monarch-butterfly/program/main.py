import sys
from pixelbench_api import *

def draw():
    ORANGE = '#ff7f00'
    DARK_ORANGE = '#d95f00'
    LIGHT_ORANGE = '#ffa500'
    BLACK = '#1a1a1a'
    WHITE = '#ffffff'
    BODY = '#2b2b2b'

    c = new_canvas(32, 32)
    
    # Forewing Black Base
    c.poly([(16, 6), (20, 3), (25, 2), (29, 4), (31, 8), (30, 13), (26, 17), (21, 18), (16, 16)], BLACK)

    # Hindwing Black Base
    c.poly([(16, 16), (21, 18), (25, 20), (28, 23), (28, 27), (24, 30), (19, 31), (16, 29)], BLACK)

    # Forewing Orange
    c.poly([(17, 7), (20, 5), (24, 4), (27, 5), (29, 8), (28, 12), (24, 15), (20, 16), (17, 15)], ORANGE)

    # Hindwing Orange
    c.poly([(17, 18), (21, 19), (24, 21), (26, 23), (26, 26), (23, 28), (19, 29), (17, 28)], DARK_ORANGE)

    # Forewing Veins
    c.line(17, 11, 21, 10, BLACK)
    c.line(17, 13, 21, 10, BLACK)
    c.line(21, 10, 26, 5, BLACK)
    c.line(21, 10, 28, 8, BLACK)
    c.line(21, 10, 27, 12, BLACK)
    c.line(21, 10, 23, 15, BLACK)
    c.line(19, 14, 19, 16, BLACK)
    
    # Apical orange spots
    c.set(26, 3, LIGHT_ORANGE)
    c.set(27, 4, LIGHT_ORANGE)
    c.set(28, 5, LIGHT_ORANGE)
    c.set(29, 7, LIGHT_ORANGE)

    # Hindwing Veins
    c.line(17, 20, 21, 22, BLACK)
    c.line(17, 25, 21, 22, BLACK)
    c.line(21, 22, 25, 21, BLACK)
    c.line(21, 22, 26, 24, BLACK)
    c.line(21, 22, 25, 27, BLACK)
    c.line(21, 22, 22, 28, BLACK)
    c.line(19, 24, 19, 29, BLACK)

    # Forewing White Dots
    c.set(27, 3, WHITE)
    c.set(29, 5, WHITE)
    c.set(30, 8, WHITE)
    c.set(29, 11, WHITE)
    c.set(28, 14, WHITE)
    c.set(25, 16, WHITE)
    c.set(22, 17, WHITE)
    
    # Hindwing White Dots
    c.set(26, 20, WHITE)
    c.set(27, 23, WHITE)
    c.set(27, 26, WHITE)
    c.set(25, 28, WHITE)
    c.set(22, 29, WHITE)
    c.set(19, 30, WHITE)

    # Mirror right wing to left
    left = c.copy().mirror("h")
    
    # Draw body on a separate layer
    body_layer = new_canvas(32, 32)
    body_layer.rect(15, 6, 2, 20, BODY) # Thorax and abdomen
    body_layer.rect(15, 4, 2, 2, BODY) # Head
    
    # Antenna
    body_layer.line(15, 3, 12, 1, BLACK)
    body_layer.set(11, 1, BLACK)
    body_layer.line(16, 3, 19, 1, BLACK)
    body_layer.set(20, 1, BLACK)

    # Flatten
    final = flatten([left, c, body_layer])
    
    finish(final)

draw()
