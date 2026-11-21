from pixelbench_api import new_canvas, finish

W = H = 32
c = new_canvas(W, H, name="farm-sheep")

# warm muted palette
body   = c.color("#f7f1e2")
light  = c.color("#fbf6ea")
shade  = c.color("#e7d9c0")
shade2 = c.color("#d6c3a1")
pink   = c.color("#f3c8d4")
pink_d = c.color("#e2a9bc")
dark   = c.color("#6e6552")
dark2  = c.color("#51493c")
nose   = c.color("#dd8fa2")
shadow = c.color((194, 180, 156, 90))


def rounded_leg(x, y, w, h, col):
    c.rect(x, y, w, h - 1, col)
    c.circle(x + w // 2, y + h - 1, 1, col)


# soft ground shadow
c.ellipse(15, 29, 9, 2, shadow)

# legs: back pair then front pair
for lx in (9, 13, 17, 21):
    rounded_leg(lx, 20, 3, 7, dark)

# tail fluff
c.circle(7, 17, 2, body)

# main wool body
c.ellipse(15, 18, 9, 7, body)

# fluff bumps along the top / back edge
c.circle(10, 13, 2, body)
c.circle(14, 12, 2, body)
c.circle(18, 13, 2, body)
c.circle(7, 15, 2, body)

# flat wool shading on the underside
c.ellipse(14, 22, 7, 3, shade)
c.ellipse(15, 23, 5, 2, shade2)

# gentle highlight on the wool
c.ellipse(12, 14, 4, 3, light)

# back ear (peeks from behind head)
c.ellipse(17, 10, 1, 1, pink_d)

# head
c.ellipse(22, 14, 6, 5, body)

# head underside shading
c.ellipse(22, 17, 4, 2, shade)

# front ear
c.ellipse(21, 9, 2, 1, pink)

# face
c.set(25, 12, dark2)
c.rect(24, 15, 2, 1, nose)
c.set(25, 16, dark)

print(c.stats_text())
print(c.matrix_text())
finish(c)
