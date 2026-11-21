from pixelbench_api import *

c = new_canvas(32, 32, name="result")

body = c.color((205, 214, 224), name="body")
mid = c.color((158, 172, 188), name="mid")
dark = c.color((104, 120, 138), name="dark")
outline_c = c.color((28, 34, 42), name="outline")
lens = c.color((46, 66, 90), name="lens")
blue = c.color((120, 180, 215), name="blue")
glass = c.color((200, 226, 240), name="glass")
hi = c.color((238, 244, 250), name="hi")

# ---- base ----
c.rect(5, 25, 22, 2, mid)     # upper base
c.rect(6, 25, 20, 1, hi)      # top highlight
c.rect(4, 27, 24, 3, dark)    # lower foot

# ---- stage ----
c.rect(5, 18, 18, 3, body)
c.rect(5, 18, 18, 1, hi)
c.rect(6, 19, 6, 1, glass)    # glass slide hint

# ---- objective ----
c.rect(11, 15, 5, 3, mid)
c.rect(11, 17, 5, 1, lens)

# ---- turret ----
c.rect(8, 11, 11, 4, dark)

# ---- body tube ----
c.rect(10, 5, 7, 6, mid)
c.rect(11, 5, 2, 6, hi)

# ---- eyepiece ----
c.rect(11, 1, 5, 4, body)
c.rect(12, 1, 3, 1, lens)
c.rect(11, 2, 1, 3, hi)

# ---- arm (separate curved pillar on the right) ----
c.rect(16, 4, 10, 3, dark)    # top band
c.rect(22, 7, 4, 15, dark)    # right pillar
c.rect(16, 22, 10, 4, dark)   # bottom band
c.rect(24, 7, 1, 15, hi)      # pillar highlight

c.outline(outline_c)

# small glass reflection on the objective lens
c.set(13, 17, blue)
# touch of highlight on the eyepiece rim
c.set(13, 2, hi)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))

finish(c)
