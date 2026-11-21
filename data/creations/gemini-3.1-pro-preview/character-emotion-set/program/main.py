from pixelbench_api import *

c = new_canvas(64, 64)

c.color("#ffccaa", "skin")
c.color("#e0a080", "skin_dark")
c.color("#3366cc", "hair")
c.color("#4488ff", "hair_light")
c.color("#dd3333", "shirt")
c.color("#aa2222", "shirt_dark")
c.color("#ffffff", "white")
c.color("#000000", "black")
c.color("#ff6666", "red")
c.color("#881111", "dark_red")
c.color("#111111", "outline")

def draw_base(dx, dy):
    # Neck
    c.rect(dx + 13, dy + 25, 6, 4, "skin_dark")
    
    # Shirt
    c.rect(dx + 8, dy + 28, 16, 3, "shirt")
    c.rect(dx + 6, dy + 29, 20, 2, "shirt")
    c.rect(dx + 8, dy + 28, 16, 1, "shirt_dark")
    c.rect(dx + 13, dy + 28, 6, 1, "shirt") # override neck area
    
    # Head base
    c.rect(dx + 8, dy + 10, 16, 14, "skin")
    c.rect(dx + 10, dy + 24, 12, 2, "skin")
    # Cheeks / shading
    c.rect(dx + 8, dy + 20, 2, 2, "skin_dark")
    c.rect(dx + 22, dy + 20, 2, 2, "skin_dark")
    c.rect(dx + 10, dy + 24, 12, 1, "skin_dark")
    c.rect(dx + 14, dy + 24, 4, 1, "skin")
    
    # Ears
    c.rect(dx + 6, dy + 15, 2, 4, "skin")
    c.rect(dx + 24, dy + 15, 2, 4, "skin")
    c.rect(dx + 7, dy + 16, 1, 2, "skin_dark")
    c.rect(dx + 24, dy + 16, 1, 2, "skin_dark")
    
    # Nose
    c.rect(dx + 15, dy + 19, 2, 1, "skin_dark")
    
    # Hair
    c.rect(dx + 7, dy + 5, 18, 7, "hair")
    c.rect(dx + 9, dy + 3, 14, 2, "hair")
    c.rect(dx + 12, dy + 1, 4, 2, "hair")
    c.rect(dx + 18, dy + 1, 3, 2, "hair")
    c.rect(dx + 6, dy + 12, 2, 5, "hair")
    c.rect(dx + 24, dy + 12, 2, 5, "hair")
    
    # Hair highlight
    c.rect(dx + 9, dy + 6, 4, 2, "hair_light")
    c.rect(dx + 14, dy + 5, 2, 2, "hair_light")
    
    # Bangs
    c.rect(dx + 8, dy + 10, 16, 2, "hair")
    c.rect(dx + 9, dy + 12, 2, 2, "hair")
    c.rect(dx + 15, dy + 12, 3, 2, "hair")
    c.rect(dx + 21, dy + 12, 2, 2, "hair")

def draw_calm(dx, dy):
    draw_base(dx, dy)
    # Whites
    c.rect(dx + 10, dy + 16, 3, 2, "white")
    c.rect(dx + 19, dy + 16, 3, 2, "white")
    # Pupils
    c.rect(dx + 11, dy + 16, 1, 2, "black")
    c.rect(dx + 20, dy + 16, 1, 2, "black")
    # Eyebrows
    c.rect(dx + 10, dy + 14, 3, 1, "hair")
    c.rect(dx + 19, dy + 14, 3, 1, "hair")
    # Mouth
    c.rect(dx + 14, dy + 22, 4, 1, "black")

def draw_smiling(dx, dy):
    draw_base(dx, dy)
    # Happy eyes
    c.set(dx + 10, dy + 17, "black")
    c.set(dx + 11, dy + 16, "black")
    c.set(dx + 12, dy + 17, "black")
    c.set(dx + 19, dy + 17, "black")
    c.set(dx + 20, dy + 16, "black")
    c.set(dx + 21, dy + 17, "black")
    # Eyebrows
    c.rect(dx + 10, dy + 13, 3, 1, "hair")
    c.rect(dx + 19, dy + 13, 3, 1, "hair")
    # Mouth
    c.rect(dx + 13, dy + 21, 6, 1, "black")
    c.rect(dx + 14, dy + 22, 4, 2, "black")
    c.rect(dx + 14, dy + 22, 4, 1, "white")
    c.rect(dx + 15, dy + 23, 2, 1, "red")

def draw_angry(dx, dy):
    draw_base(dx, dy)
    # Whites
    c.rect(dx + 10, dy + 16, 3, 2, "white")
    c.rect(dx + 19, dy + 16, 3, 2, "white")
    # Pupils
    c.rect(dx + 11, dy + 16, 1, 1, "black")
    c.rect(dx + 20, dy + 16, 1, 1, "black")
    # Eyebrows
    c.line(dx + 9, dy + 13, dx + 14, dy + 15, "hair")
    c.line(dx + 9, dy + 14, dx + 14, dy + 16, "hair")
    c.line(dx + 22, dy + 13, dx + 17, dy + 15, "hair")
    c.line(dx + 22, dy + 14, dx + 17, dy + 16, "hair")
    # Mouth
    c.rect(dx + 14, dy + 22, 4, 1, "black")
    c.set(dx + 13, dy + 23, "black")
    c.set(dx + 18, dy + 23, "black")

def draw_surprised(dx, dy):
    draw_base(dx, dy)
    # Whites
    c.rect(dx + 10, dy + 14, 3, 4, "white")
    c.rect(dx + 19, dy + 14, 3, 4, "white")
    # Pupils
    c.rect(dx + 11, dy + 15, 1, 2, "black")
    c.rect(dx + 20, dy + 15, 1, 2, "black")
    # Eyebrows
    c.rect(dx + 10, dy + 11, 3, 1, "hair")
    c.rect(dx + 19, dy + 11, 3, 1, "hair")
    # Mouth
    c.rect(dx + 14, dy + 21, 4, 3, "black")
    c.rect(dx + 15, dy + 22, 2, 1, "dark_red")

draw_calm(0, 0)
draw_smiling(32, 0)
draw_angry(0, 32)
draw_surprised(32, 32)

c.outline("outline")
view(c)
finish(c)
