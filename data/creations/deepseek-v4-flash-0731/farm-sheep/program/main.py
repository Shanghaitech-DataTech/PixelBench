from pixelbench_api import *

c = new_canvas(32, 32)

# warm muted palette
cream_hi = c.color("#FBF6EA")   # soft highlight
cream    = c.color("#F5EFE0")   # main fluff
shade    = c.color("#E9DCC4")   # gentle fluff shade
shadow   = c.color("#DAC9AB")   # deeper shadow
face     = c.color("#F7E8DC")   # pale warm face
ear_p    = c.color("#EFCAD0")   # pale pink ear
ear_in   = c.color("#D99EAA")   # inner ear
nose     = c.color("#C4878E")   # nose
eye      = c.color("#40302C")   # soft dark eye
blush    = c.color("#EFB9B6")   # cheek blush
leg      = c.color("#9C8573")   # legs
leg_d    = c.color("#7A6757")   # hoof

# --- legs (behind the body) ---
for x in (10, 15, 20, 25):
    c.rect(x, 25, 2, 5, leg)
    c.rect(x, 29, 2, 2, leg_d)

# --- fluffy body bumps ---
c.ellipse(18, 20, 9, 6, cream)   # main mass   x9..27  y14..25
c.circle(13, 17, 3, cream)       # shoulder    x10..16
c.circle(19, 16, 3, cream)       # top bump    x16..22
c.circle(25, 18, 3, cream)       # rump        x22..28
c.circle(16, 15, 2, cream)       # mid fluff
c.circle(20, 13, 3, cream)       # top fluff dome
c.circle(27, 14, 2, cream)       # rump fluff

# gentle flat shading on the fluff
c.ellipse(18, 23, 8, 2, shade)     # lower-fluff shade   rows 21..24
c.ellipse(18, 24, 5, 1, shadow)    # soft under-shadow   row 24
c.rect(16, 22, 2, 1, shade)        # dip shadows
c.rect(23, 22, 2, 1, shade)

# top highlights
c.set(17, 13, cream_hi)
c.set(19, 13, cream_hi)
c.set(12, 15, cream_hi)
c.set(24, 16, cream_hi)

# --- head (front left, overlapping the body) ---
c.ellipse(9, 15, 5, 4.5, face)    # x4..14 y10..19
c.ellipse(9, 19, 3, 1, shade)     # tiny chin shadow

# --- ear (on top of the head) ---
c.ellipse(13, 9, 2, 2, ear_p)     # x11..15 y7..11
c.rect(14, 8, 2, 2, ear_in)       # inner ear

# face
c.rect(7, 14, 2, 2, eye)
c.set(5, 18, nose)
c.set(6, 18, nose)
c.set(9, 16, blush)
c.set(10, 17, blush)
c.set(6, 11, cream_hi)
c.set(7, 11, cream_hi)

# centre the sprite horizontally
c.shift(-1, 0, None)

print(c.stats_text())
print(c.matrix_text(region=(0, 7, 31, 26), indices=True))

finish(c)

