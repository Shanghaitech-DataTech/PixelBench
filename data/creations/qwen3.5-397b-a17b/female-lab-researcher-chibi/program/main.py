from pixelbench_api import new_canvas, finish

# Create a 16x16 canvas for the chibi lab researcher
c = new_canvas(16, 16, name="female_lab_researcher")

# Define colors
black = c.color((0, 0, 0), "black")           # hair
brown = c.color((139, 69, 19), "brown")       # eyes
skin = c.color((255, 220, 180), "skin")       # skin tone
white = c.color((255, 255, 255), "white")     # lab coat
light_gray = c.color((200, 200, 200), "light_gray")  # coat shadow
dark_gray = c.color((100, 100, 100), "dark_gray")    # coat detail
pink = c.color((255, 180, 180), "pink")       # blush

# Draw hair (black) - top and sides of head
# Top of hair
c.rect(4, 0, 8, 2, black)
c.rect(3, 1, 10, 1, black)
c.rect(2, 2, 12, 1, black)
# Side hair framing face
c.set(2, 3, black)
c.set(2, 4, black)
c.set(2, 5, black)
c.set(13, 3, black)
c.set(13, 4, black)
c.set(13, 5, black)
# Hair bottom/back
c.rect(3, 6, 10, 2, black)

# Draw face (skin tone)
c.rect(4, 3, 8, 5, skin)
c.set(3, 4, skin)
c.set(3, 5, skin)
c.set(12, 4, skin)
c.set(12, 5, skin)

# Draw eyes (brown) - chibi style, large and expressive
c.set(5, 5, brown)
c.set(6, 5, brown)
c.set(9, 5, brown)
c.set(10, 5, brown)
# Eye highlights (white)
c.set(6, 5, white)
c.set(10, 5, white)

# Draw mouth (small smile)
c.set(7, 7, pink)
c.set(8, 7, pink)

# Draw blush
c.set(4, 6, pink)
c.set(11, 6, pink)

# Draw lab coat (white) - body area
# Shoulders
c.rect(3, 8, 10, 2, white)
# Main body
c.rect(4, 10, 8, 5, white)
# Bottom of coat
c.rect(5, 14, 6, 2, white)

# Lab coat details - shadow/fold lines
c.set(4, 9, light_gray)
c.set(11, 9, light_gray)
c.set(5, 11, light_gray)
c.set(10, 11, light_gray)

# Lab coat buttons
c.set(7, 10, dark_gray)
c.set(7, 12, dark_gray)
c.set(7, 14, dark_gray)

# Draw arms/sleeves
c.rect(2, 9, 2, 4, white)
c.rect(12, 9, 2, 4, white)

# Hands (skin tone peeking out)
c.set(2, 13, skin)
c.set(3, 13, skin)
c.set(12, 13, skin)
c.set(13, 13, skin)

# Check stats
print(c.stats_text())
print(c.matrix_text())

# Submit the result
finish(c)
