from pixelbench_api import new_canvas, finish

# Create a 64x64 canvas with transparent background
c = new_canvas(64, 64, background=None, name="emotions")

# Define colors - keeping palette tight
skin = c.color("#f5d0a9")
skin_shadow = c.color("#e0b890")
hair = c.color("#3d2817")
hair_highlight = c.color("#5a3d2b")
eye_white = c.color("#ffffff")
eye_pupil = c.color("#1a1a1a")
eye_blue = c.color("#4a90d9")
mouth_calm = c.color("#c9786a")
mouth_smile = c.color("#d9887a")
mouth_angry = c.color("#b9685a")
cheek = c.color("#f0a8a0")
shirt = c.color("#5a7a9a")
shirt_collar = c.color("#6a8aaa")
outline = c.color("#1a1a1a")

# Each portrait is 32x32, arranged in 2x2 grid
# Top-left (0,0): Calm
# Top-right (32,0): Smiling
# Bottom-left (0,32): Angry
# Bottom-right (32,32): Surprised

def draw_head(base_x, base_y):
    """Draw the common head/face structure."""
    # Hair back
    c.rect(base_x + 6, base_y + 2, 20, 6, hair)
    c.rect(base_x + 4, base_y + 4, 24, 4, hair)
    
    # Hair sides
    c.rect(base_x + 2, base_y + 6, 4, 16, hair)
    c.rect(base_x + 28, base_y + 6, 4, 16, hair)
    
    # Hair top
    c.rect(base_x + 8, base_y + 0, 16, 4, hair)
    c.rect(base_x + 6, base_y + 2, 20, 2, hair)
    
    # Hair highlights
    c.set(base_x + 10, base_y + 2, hair_highlight)
    c.set(base_x + 14, base_y + 2, hair_highlight)
    c.set(base_x + 18, base_y + 2, hair_highlight)
    
    # Face base
    c.rect(base_x + 6, base_y + 8, 20, 18, skin)
    c.rect(base_x + 8, base_y + 6, 16, 2, skin)
    c.rect(base_x + 4, base_y + 10, 2, 14, skin)
    c.rect(base_x + 28, base_y + 10, 2, 14, skin)
    c.rect(base_x + 6, base_y + 26, 20, 4, skin)
    
    # Face shadow
    c.rect(base_x + 8, base_y + 24, 16, 4, skin_shadow)
    
    # Cheeks
    c.set(base_x + 8, base_y + 18, cheek)
    c.set(base_x + 9, base_y + 18, cheek)
    c.set(base_x + 23, base_y + 18, cheek)
    c.set(base_x + 24, base_y + 18, cheek)
    
    # Nose
    c.set(base_x + 15, base_y + 18, skin_shadow)
    c.set(base_x + 15, base_y + 19, skin_shadow)
    
    # Shirt/collar
    c.rect(base_x + 4, base_y + 28, 24, 4, shirt)
    c.rect(base_x + 10, base_y + 28, 12, 3, shirt_collar)
    c.rect(base_x + 12, base_y + 28, 8, 2, skin)

def draw_eyes_mouth(base_x, base_y, emotion):
    """Draw expression-specific eyes and mouth."""
    
    if emotion == "calm":
        # Eyes - relaxed horizontal
        c.rect(base_x + 10, base_y + 14, 4, 3, eye_white)
        c.rect(base_x + 20, base_y + 14, 4, 3, eye_white)
        c.set(base_x + 11, base_y + 15, eye_blue)
        c.set(base_x + 12, base_y + 15, eye_blue)
        c.set(base_x + 12, base_y + 15, eye_pupil)
        c.set(base_x + 21, base_y + 15, eye_blue)
        c.set(base_x + 22, base_y + 15, eye_blue)
        c.set(base_x + 22, base_y + 15, eye_pupil)
        # Eyebrows - straight, relaxed
        c.rect(base_x + 9, base_y + 12, 6, 1, hair)
        c.rect(base_x + 19, base_y + 12, 6, 1, hair)
        # Mouth - small calm line
        c.rect(base_x + 13, base_y + 22, 6, 1, mouth_calm)
        
    elif emotion == "smile":
        # Eyes - happy, slightly curved
        c.rect(base_x + 10, base_y + 14, 4, 3, eye_white)
        c.rect(base_x + 20, base_y + 14, 4, 3, eye_white)
        c.set(base_x + 11, base_y + 15, eye_blue)
        c.set(base_x + 12, base_y + 15, eye_blue)
        c.set(base_x + 12, base_y + 15, eye_pupil)
        c.set(base_x + 21, base_y + 15, eye_blue)
        c.set(base_x + 22, base_y + 15, eye_blue)
        c.set(base_x + 22, base_y + 15, eye_pupil)
        # Eyebrows - raised and curved
        c.rect(base_x + 9, base_y + 11, 6, 1, hair)
        c.rect(base_x + 19, base_y + 11, 6, 1, hair)
        c.set(base_x + 10, base_y + 12, hair)
        c.set(base_x + 24, base_y + 12, hair)
        # Mouth - big smile (upward curve)
        c.rect(base_x + 11, base_y + 21, 10, 1, mouth_smile)
        c.rect(base_x + 12, base_y + 22, 8, 2, mouth_smile)
        c.set(base_x + 10, base_y + 22, mouth_smile)
        c.set(base_x + 21, base_y + 22, mouth_smile)
        
    elif emotion == "angry":
        # Eyes - narrowed, intense
        c.rect(base_x + 10, base_y + 15, 4, 2, eye_white)
        c.rect(base_x + 20, base_y + 15, 4, 2, eye_white)
        c.set(base_x + 11, base_y + 15, eye_blue)
        c.set(base_x + 12, base_y + 15, eye_blue)
        c.set(base_x + 12, base_y + 15, eye_pupil)
        c.set(base_x + 21, base_y + 15, eye_blue)
        c.set(base_x + 22, base_y + 15, eye_blue)
        c.set(base_x + 22, base_y + 15, eye_pupil)
        # Eyebrows - angled down toward center (angry V shape)
        c.rect(base_x + 8, base_y + 12, 7, 1, hair)
        c.rect(base_x + 19, base_y + 12, 7, 1, hair)
        c.set(base_x + 14, base_y + 13, hair)
        c.set(base_x + 15, base_y + 13, hair)
        c.set(base_x + 19, base_y + 13, hair)
        c.set(base_x + 20, base_y + 13, hair)
        # Mouth - frown (downward curve)
        c.rect(base_x + 12, base_y + 23, 8, 1, mouth_angry)
        c.set(base_x + 11, base_y + 22, mouth_angry)
        c.set(base_x + 21, base_y + 22, mouth_angry)
        
    elif emotion == "surprised":
        # Eyes - big round circles
        c.rect(base_x + 9, base_y + 13, 5, 5, eye_white)
        c.rect(base_x + 20, base_y + 13, 5, 5, eye_white)
        # Blue iris
        c.rect(base_x + 10, base_y + 14, 3, 3, eye_blue)
        c.rect(base_x + 21, base_y + 14, 3, 3, eye_blue)
        # Pupil in center
        c.set(base_x + 11, base_y + 15, eye_pupil)
        c.set(base_x + 22, base_y + 15, eye_pupil)
        # Eyebrows - high and arched
        c.rect(base_x + 9, base_y + 10, 5, 1, hair)
        c.rect(base_x + 20, base_y + 10, 5, 1, hair)
        c.set(base_x + 10, base_y + 11, hair)
        c.set(base_x + 13, base_y + 11, hair)
        c.set(base_x + 21, base_y + 11, hair)
        c.set(base_x + 24, base_y + 11, hair)
        # Mouth - O shape (surprised)
        c.rect(base_x + 13, base_y + 21, 6, 4, mouth_angry)
        c.set(base_x + 12, base_y + 22, mouth_angry)
        c.set(base_x + 12, base_y + 23, mouth_angry)
        c.set(base_x + 20, base_y + 22, mouth_angry)
        c.set(base_x + 20, base_y + 23, mouth_angry)

def draw_outline(base_x, base_y):
    """Add dark outline around the character."""
    # Top of head outline
    c.set(base_x + 6, base_y + 0, outline)
    c.set(base_x + 25, base_y + 0, outline)
    c.rect(base_x + 7, base_y + 0, 18, 1, outline)
    
    # Hair sides outline
    c.rect(base_x + 2, base_y + 6, 1, 16, outline)
    c.rect(base_x + 31, base_y + 6, 1, 16, outline)
    
    # Face outline sides
    c.set(base_x + 4, base_y + 10, outline)
    c.set(base_x + 4, base_y + 23, outline)
    c.set(base_x + 31, base_y + 10, outline)
    c.set(base_x + 31, base_y + 23, outline)
    
    # Chin outline
    c.rect(base_x + 6, base_y + 29, 20, 1, outline)
    
    # Shirt outline
    c.rect(base_x + 4, base_y + 28, 1, 4, outline)
    c.rect(base_x + 27, base_y + 28, 1, 4, outline)
    c.rect(base_x + 5, base_y + 31, 22, 1, outline)

# Draw all four characters
# Calm (top-left)
draw_head(0, 0)
draw_eyes_mouth(0, 0, "calm")
draw_outline(0, 0)

# Smiling (top-right)
draw_head(32, 0)
draw_eyes_mouth(32, 0, "smile")
draw_outline(32, 0)

# Angry (bottom-left)
draw_head(0, 32)
draw_eyes_mouth(0, 32, "angry")
draw_outline(0, 32)

# Surprised (bottom-right)
draw_head(32, 32)
draw_eyes_mouth(32, 32, "surprised")
draw_outline(32, 32)

print(c.stats_text())
print("=== CALM (top-left) ===")
print(c.matrix_text(region=(0, 0, 31, 31)))
print("=== SMILE (top-right) ===")
print(c.matrix_text(region=(32, 0, 63, 31)))
print("=== ANGRY (bottom-left) ===")
print(c.matrix_text(region=(0, 32, 31, 63)))
print("=== SURPRISED (bottom-right) ===")
print(c.matrix_text(region=(32, 32, 63, 63)))

finish(c)
