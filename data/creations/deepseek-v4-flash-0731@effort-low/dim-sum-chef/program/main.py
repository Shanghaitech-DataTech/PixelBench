from pixelbench_api import *

OUT    = (46, 32, 24)
SKIN   = (246, 198, 160)
SKIN_D = (206, 158, 116)
WHT    = (244, 244, 244)
SHADE  = (188, 190, 196)
APRON  = (253, 250, 242)
DUST   = (228, 220, 206)
BAMBOO = (178, 122, 58)
BAMBOO_D=(138, 92, 40)
INNER  = (88, 56, 28)
BUN    = (252, 250, 240)
BUN_S  = (214, 196, 176)
SHOE   = (54, 38, 26)

c = new_canvas(32, 32)

# ---- feet ----
c.rect(11, 29, 5, 3, SHOE)
c.rect(16, 29, 5, 3, SHOE)
c.rect(13, 27, 2, 3, WHT)
c.rect(17, 27, 2, 3, WHT)

# ---- jacket torso + apron ----
c.rect(10, 16, 12, 7, WHT)          # jacket rows16-22
c.rect(11, 17, 10, 15, APRON)       # apron rows17-31
# collar
c.rect(13, 16, 6, 2, WHT)

# ---- sleeves ----
c.rect(8, 18, 3, 4, WHT)            # left sleeve rows18-21
c.rect(21, 18, 3, 4, WHT)           # right sleeve rows18-21

# ---- steamer body ----
c.rect(10, 21, 12, 5, BAMBOO)       # body rows21-25
for y in (22, 24):
    c.line(11, y, 20, y, BAMBOO_D)
c.rect(10, 25, 12, 3, BAMBOO_D)     # lower band rows25-27

# ---- inner opening (behind buns) ----
c.rect(10, 19, 12, 3, INNER)        # inner rows19-21

# ---- buns in the opening (sit on top rim) ----
c.circle(14, 19, 2, BUN)            # left bun
c.circle(18, 19, 2, BUN)            # right bun
c.circle(12, 18, 1, BUN)
c.circle(16, 18, 1, BUN)            # center bun
c.circle(20, 18, 1, BUN)
c.set(13, 18, BUN_S)
c.set(17, 18, BUN_S)
c.set(16, 17, BUN_S)

# ---- top rim (in front of body, back behind buns) ----
c.rect(10, 20, 12, 2, BAMBOO)       # front rim rows20-21

# ---- hands gripping sides ----
c.rect(8, 22, 3, 5, SKIN)           # left hand rows22-26
c.rect(21, 22, 3, 5, SKIN)          # right hand rows22-26
c.line(11, 22, 13, 22, OUT)         # fingers hint

# ---- apron bottom + feet below steamer ----
c.rect(11, 27, 10, 5, APRON)        # apron rows27-31
c.rect(9, 29, 4, 3, SHOE)           # left foot
c.rect(20, 29, 4, 3, SHOE)          # right foot
c.rect(10, 28, 2, 1, WHT)           # ankle peeks

# ---- neck, face ----
c.rect(14, 15, 4, 2, SKIN)          # neck rows15-16
c.rect(12, 8, 8, 8, SKIN)           # face rows8-15
c.set(12, 12, SKIN); c.set(19, 12, SKIN)
c.set(14, 11, OUT); c.set(17, 11, OUT)
c.set(13, 10, OUT); c.set(18, 10, OUT)
c.set(16, 12, SKIN_D)
c.set(15, 13, OUT); c.set(16, 13, OUT)

# ---- chef hat ----
c.circle(16, 2, 4, WHT)              # puff dome rows-2..6
c.rect(11, 1, 10, 5, WHT)            # solidify puff rows1-5
c.rect(11, 6, 10, 2, WHT)            # band rows6-7
c.rect(11, 7, 10, 1, OUT)            # band bottom edge row7
c.rect(8, 7, 3, 2, WHT)              # left wing rows7-8
c.rect(21, 7, 3, 2, WHT)             # right wing rows7-8
c.rect(8, 7, 3, 1, OUT, fill=False)  # wing top edge
c.rect(21, 7, 3, 1, OUT, fill=False)
c.set(12, 1, SHADE); c.set(20, 1, SHADE)
c.set(16, 0, SHADE); c.set(12, 4, SHADE); c.set(20, 4, SHADE)

# flour dust
for (dx, dy) in [(12,30),(15,30),(18,30),(13,31),(17,31),(14,27),(19,27),(14,24),(17,28)]:
    c.set(dx, dy, DUST)
# fill gaps beside face on band row
c.set(11, 8, WHT); c.set(20, 8, WHT)
# apron fold line
c.line(16, 17, 16, 22, DUST)

print(c.stats_text())
finish(c)
