from pixelbench_api import *

OUTLINE = "#1a1a1a"
SKIN = "#ffcdb2"
SKIN_SHADOW = "#e5989b"
HAIR = "#ffb703"
HAIR_SHADOW = "#fb8500"
RED = "#d90429"
DARK_RED = "#9b2226"
WHITE = "#edf2f4"
GRAY = "#8d99ae"
BLUE = "#0077b6"
LIGHT_BLUE = "#00b4d8"

def draw_front_half():
    c = new_canvas(32, 32)
    c.rect(13, 8, 3, 6, SKIN)
    c.set(12, 10, SKIN)
    c.set(12, 11, SKIN)
    c.set(14, 10, OUTLINE)
    c.set(15, 12, DARK_RED)
    
    c.rect(12, 4, 4, 4, HAIR)
    c.rect(13, 3, 3, 1, HAIR)
    c.rect(12, 8, 1, 2, HAIR)
    c.rect(6, 6, 5, 8, HAIR)
    c.rect(7, 5, 3, 1, HAIR)
    c.rect(7, 14, 3, 1, HAIR)
    c.rect(11, 6, 2, 2, RED)
    
    c.rect(15, 14, 1, 1, SKIN)
    c.rect(13, 15, 3, 5, RED)
    c.rect(13, 17, 3, 2, WHITE)
    c.set(15, 15, SKIN)
    
    c.rect(12, 20, 4, 4, RED)
    c.rect(12, 22, 4, 1, WHITE)
    
    c.rect(10, 15, 2, 5, SKIN)
    c.rect(9, 19, 2, 2, SKIN)
    
    c.rect(13, 24, 2, 5, SKIN)
    c.rect(13, 27, 2, 2, WHITE)
    c.rect(12, 29, 3, 2, WHITE)
    c.rect(12, 30, 3, 1, GRAY)
    
    c.circle(7, 20, 3, BLUE)
    c.set(7, 20, LIGHT_BLUE)
    c.set(5, 19, LIGHT_BLUE)
    c.set(8, 18, LIGHT_BLUE)
    c.set(6, 22, LIGHT_BLUE)
    c.set(9, 21, LIGHT_BLUE)
    
    c.set(15, 14, SKIN_SHADOW)
    c.rect(11, 15, 1, 4, SKIN_SHADOW)
    c.rect(14, 24, 1, 2, SKIN_SHADOW)
    c.rect(12, 8, 1, 2, HAIR_SHADOW)
    c.rect(6, 13, 5, 1, HAIR_SHADOW)
    c.rect(13, 19, 3, 1, DARK_RED)
    c.rect(12, 20, 4, 1, DARK_RED)
    
    return c

def draw_back_half():
    c = new_canvas(32, 32)
    c.rect(13, 8, 3, 6, HAIR)
    c.set(12, 10, SKIN)
    c.set(12, 11, SKIN)
    
    c.rect(12, 4, 4, 4, HAIR)
    c.rect(13, 3, 3, 1, HAIR)
    c.rect(12, 8, 1, 2, HAIR)
    c.rect(6, 6, 5, 8, HAIR)
    c.rect(7, 5, 3, 1, HAIR)
    c.rect(7, 14, 3, 1, HAIR)
    c.rect(11, 6, 2, 2, RED)
    
    c.rect(14, 8, 2, 7, HAIR)
    c.rect(13, 8, 1, 7, OUTLINE)
    
    c.rect(13, 15, 3, 5, RED)
    c.rect(13, 17, 3, 2, WHITE)
    
    c.rect(12, 20, 4, 4, RED)
    c.rect(12, 22, 4, 1, WHITE)
    
    c.rect(10, 15, 2, 5, SKIN)
    c.rect(9, 19, 2, 2, SKIN)
    
    c.rect(13, 24, 2, 5, SKIN)
    c.rect(13, 27, 2, 2, WHITE)
    c.rect(12, 29, 3, 2, WHITE)
    c.rect(12, 30, 3, 1, GRAY)
    
    c.circle(7, 20, 3, BLUE)
    c.set(7, 20, LIGHT_BLUE)
    c.set(5, 19, LIGHT_BLUE)
    c.set(8, 18, LIGHT_BLUE)
    c.set(6, 22, LIGHT_BLUE)
    c.set(9, 21, LIGHT_BLUE)
    
    c.rect(11, 15, 1, 4, SKIN_SHADOW)
    c.rect(14, 24, 1, 2, SKIN_SHADOW)
    c.rect(12, 8, 1, 2, HAIR_SHADOW)
    c.rect(6, 13, 5, 1, HAIR_SHADOW)
    c.rect(14, 13, 2, 2, HAIR_SHADOW)
    c.rect(13, 19, 3, 1, DARK_RED)
    c.rect(12, 20, 4, 1, DARK_RED)
    
    return c

def draw_side_left():
    c = new_canvas(32, 32)
    c.rect(16, 6, 4, 8, HAIR_SHADOW)
    c.rect(17, 5, 2, 1, HAIR_SHADOW)
    c.rect(17, 14, 2, 1, HAIR_SHADOW)
    
    c.circle(16, 19, 3, BLUE)
    c.set(16, 19, LIGHT_BLUE)
    
    c.rect(15, 23, 2, 5, SKIN_SHADOW)
    c.rect(15, 27, 2, 2, GRAY)
    c.rect(14, 29, 3, 2, GRAY)
    c.set(14, 30, OUTLINE)
    
    c.rect(12, 8, 5, 6, SKIN)
    c.rect(11, 9, 1, 4, SKIN)
    c.set(10, 11, SKIN)
    c.set(12, 10, OUTLINE)
    c.set(11, 12, DARK_RED)
    c.set(14, 11, SKIN)
    
    c.rect(12, 4, 6, 4, HAIR)
    c.rect(13, 3, 4, 1, HAIR)
    c.rect(15, 8, 3, 6, HAIR)
    c.rect(13, 8, 1, 3, HAIR)
    
    c.rect(14, 6, 4, 8, HAIR)
    c.rect(15, 5, 2, 1, HAIR)
    c.rect(15, 14, 2, 1, HAIR)
    c.rect(14, 6, 2, 2, RED)
    
    c.rect(13, 14, 2, 1, SKIN)
    c.rect(12, 15, 4, 5, RED)
    c.rect(12, 17, 4, 2, WHITE)
    
    c.rect(11, 20, 6, 4, RED)
    c.rect(11, 22, 6, 1, WHITE)
    
    c.rect(13, 15, 3, 5, SKIN)
    c.rect(13, 19, 3, 2, SKIN)
    
    c.rect(13, 24, 2, 5, SKIN)
    c.rect(13, 27, 2, 2, WHITE)
    c.rect(11, 29, 4, 2, WHITE)
    c.rect(11, 30, 4, 1, GRAY)
    
    c.circle(12, 21, 3, BLUE)
    c.set(12, 21, LIGHT_BLUE)
    c.set(10, 20, LIGHT_BLUE)
    c.set(13, 19, LIGHT_BLUE)
    c.set(11, 23, LIGHT_BLUE)
    c.set(14, 22, LIGHT_BLUE)
    
    c.set(14, 14, SKIN_SHADOW)
    c.rect(14, 24, 1, 2, SKIN_SHADOW)
    c.rect(16, 8, 2, 6, HAIR_SHADOW)
    c.rect(14, 13, 4, 1, HAIR_SHADOW)
    c.rect(12, 19, 4, 1, DARK_RED)
    c.rect(11, 20, 6, 1, DARK_RED)
    
    c.rect(15, 15, 1, 5, OUTLINE)
    c.rect(17, 6, 1, 8, OUTLINE)
    
    c.outline(OUTLINE)
    return c

out = new_canvas(64, 64)

fh = draw_front_half()
fr = fh.copy()
fr.mirror("h")
front = flatten([fh, fr])
front.outline(OUTLINE)
out.blit(front, 0, 0)

bh = draw_back_half()
br = bh.copy()
br.mirror("h")
back = flatten([bh, br])
back.outline(OUTLINE)
out.blit(back, 32, 0)

sl = draw_side_left()
out.blit(sl, 0, 32)

sr = sl.copy()
sr.mirror("h")
out.blit(sr, 32, 32)

finish(out)
