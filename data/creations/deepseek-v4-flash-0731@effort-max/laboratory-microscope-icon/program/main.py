from pixelbench_api import *

c = new_canvas(32, 32, name="microscope")

k = c.color("#262b3d")   # ink outline
d = c.color("#454c66")  # dark metal
m = c.color("#8d95ab")  # mid metal
l = c.color("#c9d0e0")  # light metal
b = c.color("#1c2444")  # lens glass
g = c.color("#7fa6ff")  # glint
r = c.color("#e85d78")  # slide
gr = c.color("#2fbf71")  # specimen
a = c.color("#e6a93c")  # gold accent

# ---------- base ----------
c.rect(4, 26, 24, 5, k)       # base block outline
c.rect(5, 27, 22, 3, m)       # base body
c.rect(5, 27, 22, 1, l)       # base top highlight
c.rect(13, 28, 8, 1, a)       # gold nameplate

# ---------- arm (back, right side) ----------
c.rect(20, 15, 4, 12, k)      # arm outline  x20..23, y15..26
c.rect(21, 16, 2, 10, m)      # arm body
c.rect(21, 16, 1, 10, l)      # arm highlight

# ---------- head (joint block + focus knob) ----------
c.rect(20, 12, 5, 4, k)       # head outline
c.rect(21, 13, 3, 2, a)       # gold head band
c.rect(22, 13, 3, 3, k)       # knob rim
c.rect(23, 13, 1, 3, a)       # knob face
c.set(23, 13, b)               # knob notch

# ---------- stage ----------
c.rect(9, 21, 16, 4, k)       # stage outline   x9..24, y21..24
c.rect(10, 21, 14, 1, l)      # stage top face
c.rect(10, 22, 14, 1, m)      # stage front
c.rect(10, 23, 14, 1, d)      # stage front shade

# ---------- slide + specimen ----------
c.rect(13, 20, 8, 2, k)       # slide outline
c.rect(14, 20, 6, 2, r)       # slide
c.set(17, 20, gr)              # specimen dot

# ---------- objective ----------
c.rect(14, 14, 7, 5, k)       # objective body outline  x14..20, y14..18
c.rect(15, 15, 5, 3, m)       # objective body
c.rect(15, 15, 1, 3, l)       # body highlight
c.rect(13, 18, 9, 2, k)       # lens cap outline  x13..21, y18..19
c.rect(14, 18, 7, 1, d)       # cap ring
c.rect(14, 19, 7, 1, b)       # lens
c.set(15, 19, g)
c.set(18, 19, g)

# ---------- body tube (leaning head) ----------
c.poly([(20, 8), (25, 7), (19, 15), (14, 16)], k)
c.poly([(21, 9), (24, 8), (18, 14), (15, 15)], m)
c.poly([(21, 9), (22, 9), (16, 14), (15, 15)], l)

# ---------- eyepiece ----------
c.poly([(21, 3), (26, 2), (25, 8), (20, 9)], k)
c.poly([(22, 4), (25, 3), (24, 7), (21, 8)], b)
c.set(23, 4, g)
c.set(23, 5, g)

print(c.stats_text())
finish(c)
