from pixelbench_api import *

# 32x32 Stardew-style fluffy sheep, side view, transparent background
c = new_canvas(32, 32, background=None, name="sheep")

# palette
WOOL      = c.color("#F4F0E6", "wool")         # warm white
WOOL_HI   = c.color("#FBF8F0", "wool_light")   # gentle top light
WOOL_SH   = c.color("#DCD3C2", "wool_shadow")  # muted shadow
FACE      = c.color("#EAE2D3", "face")         # warm cream face
FACE_SH   = c.color("#D6CCBA", "face_shadow")
NOSE      = c.color("#C98F8C", "nose")
PINK      = c.color("#EBB9B4", "pale_pink")    # pale pink ear
PINK_SH   = c.color("#D89C99", "pink_shadow")
EYE       = c.color("#2B2320", "eye")
LEG       = c.color("#4C3E35", "leg")
LEG_FAR   = c.color("#3A2E27", "leg_far")
HOOF      = c.color("#2B2320", "hoof")

FAR_LEGS = [(11, 22), (20, 22)]   # darker, behind
NEAR_LEGS = [(8, 22), (17, 22)]   # in front

# ---- wool shadow rim first, so legs sit in front of it ----
puffs = [(7,15,3),(11,13,3),(15,12,3),(19,14,3),(20,18,3),
         (17,21,3),(12,22,3),(8,20,3),(5,17,3),(13,17,4)]
for (x, y, r) in puffs:
    c.circle(x, y + 2, r, WOOL_SH)

# ---- far legs (drawn first, partly hidden by body) ----
for (x, y) in FAR_LEGS:
    c.rect(x, y, 2, 6, LEG_FAR)
    c.rect(x, y + 5, 2, 1, HOOF)

# ---- near legs ----
for (x, y) in NEAR_LEGS:
    c.rect(x, y, 2, 7, LEG)
    c.rect(x, y + 6, 2, 1, HOOF)

# ---- tail: little wool puff ----
c.circle(4, 14, 2, WOOL_SH)
c.circle(4, 13, 2, WOOL)
# shadow notch so the tail reads apart from the body
c.set(7, 13, WOOL_SH)
c.set(7, 14, WOOL_SH)

# ---- white fluff on top ----
for (x, y, r) in puffs:
    c.circle(x, y, r, WOOL)

# ---- gentle top light on the upper bumps ----
for (x, y) in [(6,13),(7,12),(10,11),(11,10),(12,10),(14,9),(15,9),
               (16,10),(19,12),(20,13),(9,18),(5,16)]:
    c.set(x, y, WOOL_HI)

# ---- head ----
c.ellipse(24, 12, 4, 4, FACE)
# soft shading: lower face + chin
c.rect(21, 14, 7, 1, FACE_SH)
c.rect(22, 15, 6, 1, FACE_SH)
c.rect(23, 16, 4, 1, FACE_SH)
# wool tuft over the forehead so head melts into the fluff
c.circle(23, 9, 2, WOOL)
c.set(21, 10, WOOL)
c.set(22, 9, WOOL)
# tiny pink nose
c.set(27, 13, NOSE)

# ---- ear: pale pink, up and back ----
c.ellipse(20, 9, 2, 2, PINK)
c.ellipse(20, 9, 1, 1, PINK_SH)

# ---- eye (drawn last so nothing covers it) ----
c.set(26, 11, EYE)
c.set(26, 12, EYE)

print(c.stats_text())
print(c.matrix_text())
view(c, scale=12)
print("saved preview")
finish(c)
