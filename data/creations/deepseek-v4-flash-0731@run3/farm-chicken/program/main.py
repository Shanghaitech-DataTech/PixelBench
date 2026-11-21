from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="chicken")

# warm muted palette
cream    = c.color((243, 231, 205), "cream")
cream_hi = c.color((253, 247, 232), "cream_hi")
cream_sh = c.color((223, 197, 157), "cream_sh")
wing     = c.color((233, 212, 170), "wing")
wing_sh  = c.color((202, 169, 112), "wing_sh")
comb     = c.color((196, 80, 62), "comb")
comb_sh  = c.color((160, 60, 48), "comb_sh")
beak     = c.color((237, 169, 78), "beak")
beak_sh  = c.color((209, 135, 45), "beak_sh")
eye      = c.color((52, 38, 30), "eye")
leg      = c.color((217, 153, 65), "leg")
leg_sh   = c.color((186, 124, 46), "leg_sh")
shadow   = c.color((100, 76, 56, 58), "shadow")

# soft ground shadow
c.ellipse(16, 29, 8, 2, shadow)

# tail (behind body)
c.ellipse(7, 13, 3, 4, cream)     # x4..10 y9..17
c.ellipse(5, 16, 2, 2, cream)     # x3..7 y14..18

# body
c.ellipse(16, 18, 9, 9, cream)    # x7..25 y9..27

# head
c.ellipse(24, 12, 4, 4, cream)    # x20..28 y8..16

# comb
c.circle(21, 8, 1, comb)
c.circle(24, 7, 1, comb)
c.circle(27, 8, 1, comb)
c.rect(21, 8, 7, 2, comb)
c.set(20, 9, comb)
c.set(28, 9, comb)

# eye
c.set(23, 11, eye)

# beak
c.poly([(26, 11), (30, 14), (26, 16)], beak)

# wattle
c.set(27, 16, comb_sh)
c.set(28, 16, comb_sh)
c.set(28, 17, comb_sh)

# wing
c.ellipse(15, 19, 4, 3, wing)     # x11..19 y16..22
c.path("M 11 18 Q 15 22 19 18", wing_sh, fill=False)
c.set(13, 21, wing_sh)
c.set(16, 21, wing_sh)

# belly shading
c.path("M 9 25 Q 16 28 23 25", cream_sh, fill=False)

# back/top highlight
c.ellipse(13, 12, 2, 1, cream_hi)

# tail feather tips
c.set(4, 13, cream_sh)
c.set(4, 15, cream_sh)
c.set(3, 16, cream_sh)
c.set(5, 12, cream_sh)
c.set(6, 11, cream_hi)

# legs
c.line(13, 26, 13, 28, leg)
c.line(19, 26, 19, 28, leg)
# feet
c.line(10, 28, 14, 28, leg)
c.line(17, 28, 21, 28, leg)
c.set(15, 29, leg)
c.set(16, 29, leg)
c.set(22, 29, leg)

print(c.stats_text())
print(c.matrix_text())
finish(c)
