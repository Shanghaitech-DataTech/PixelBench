from pixelbench_api import *

c = new_canvas(16, 16, name="lab_researcher")

hair  = c.color("#20202a")
shine = c.color("#3d3d4a")
skin  = c.color("#f8cba3")
blush = c.color("#e7a878")
eye   = c.color("#5a3418")
hl    = c.color("#ffffff")
white = c.color("#f6f6f6")
white2 = c.color("#d3d3d8")
pants = c.color("#46536e")
shoe  = c.color("#2a2a33")

# ---- head (rows 0-7: two-heads-tall means head == body) ----
c.rect(3, 0, 10, 1, hair)     # hair top rounded, row 0, cols 3-12
c.rect(2, 1, 12, 2, hair)     # hair, rows 1-2, cols 2-13
c.rect(4, 1, 4, 1, shine)     # hair shine
c.rect(1, 3, 14, 1, hair)     # fringe, row 3, cols 1-14
c.rect(1, 4, 2, 3, hair)      # side hair left, rows 4-6
c.rect(13, 4, 2, 3, hair)     # side hair right, rows 4-6
c.rect(2, 7, 2, 1, hair)      # hair rows 7 left
c.rect(12, 7, 2, 1, hair)     # hair rows 7 right
c.rect(3, 4, 10, 3, skin)     # face, rows 4-6, cols 3-12
c.set(4, 6, blush)
c.set(11, 6, blush)
c.set(5, 5, eye); c.set(6, 5, eye)
c.set(9, 5, eye); c.set(10, 5, eye)
c.set(6, 5, hl);  c.set(10, 5, hl)   # catchlights
c.rect(4, 7, 8, 1, skin)     # chin, row 7, cols 4-11

# ---- body (rows 8-15) ----
c.rect(6, 8, 4, 1, skin)     # neck
c.rect(2, 8, 4, 1, white)    # coat collar left
c.rect(10, 8, 4, 1, white)   # coat collar right
c.rect(1, 9, 14, 5, white)   # lab coat torso, rows 9-13, cols 1-14
c.rect(8, 9, 1, 5, white2)   # coat front seam
c.rect(1, 11, 1, 3, white2)  # left sleeve shading
c.rect(14, 11, 1, 3, white2) # right sleeve shading
c.rect(3, 11, 2, 2, white2)  # pocket
c.rect(5, 14, 2, 1, pants)   # legs
c.rect(9, 14, 2, 1, pants)
c.rect(4, 15, 3, 1, shoe)    # shoes
c.rect(9, 15, 3, 1, shoe)

print(c.stats_text())
print(c.matrix_text())

result = c
finish(result)

