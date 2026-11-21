from pixelbench_api import *

c = new_canvas(32, 32)

W = c.color("#ffffff")
M = c.color("#f4f0ec")
S = c.color("#e3d8cd")
D = c.color("#c8b8a8")

F = c.color("#fadcd1")
H = c.color("#eebcae")

E = c.color("#ffc4c4")
R = c.color("#f29b9b")
r_color = c.color("#d97878")

L = c.color("#d59c8b")
V = c.color("#6b5a55")
l_color = c.color("#b87d6c")
v_color = c.color("#4a3b37")

Y = c.color("#382b27")

# Back legs
c.rect(12, 19, 2, 6, l_color)
c.rect(12, 25, 2, 2, v_color)
c.rect(20, 19, 2, 6, l_color)
c.rect(20, 25, 2, 2, v_color)

# Front legs
c.rect(15, 20, 2, 6, L)
c.rect(15, 26, 2, 2, V)
c.rect(23, 20, 2, 6, L)
c.rect(23, 26, 2, 2, V)

# Head
c.rect(4, 13, 5, 4, H)
c.circle(5, 14, 2, H)
c.circle(8, 13, 3, H)

c.rect(4, 12, 5, 4, F)
c.circle(5, 13, 2, F)
c.circle(8, 12, 3, F)

# Eye
c.set(6, 12, Y)
# Nose
c.set(3, 14, Y)

# Puffs
def draw_puff(cx, cy, rx, ry=None):
    if ry is None: ry = rx
    c.ellipse(cx, cy+1, rx, ry, D)
    c.ellipse(cx, cy, rx, ry, S)
    c.ellipse(cx-1, cy-1, rx, ry, M)
    if rx > 1 and ry > 1:
        c.ellipse(cx-1, cy-2, rx-1, ry-1, W)
    else:
        c.ellipse(cx-1, cy-2, rx, ry, W)

puffs = [
    # Back layers
    (23, 9, 4),
    (19, 7, 4, 3),
    (14, 8, 4, 3),
    (27, 11, 3),
    (26, 14, 4),
    (28, 16, 2), # tail
    (24, 18, 3),
    (20, 19, 4, 3),
    (15, 18, 4, 3),
    (11, 17, 2),
    # Front layers
    (11, 14, 3),
    (16, 13, 5, 4),
    (22, 14, 4),
]

for p in puffs:
    draw_puff(*p)

# Forehead puff
draw_puff(9, 9, 2)
draw_puff(11, 9, 2)

# Ear
# shadow
c.rect(10, 14, 3, 2, r_color)
c.rect(11, 15, 3, 2, r_color)
c.rect(12, 16, 2, 2, r_color)
c.set(9, 14, r_color)

# main
c.rect(10, 13, 3, 2, R)
c.rect(11, 14, 3, 2, R)
c.rect(12, 15, 2, 2, R)
c.set(9, 13, R)

# highlight
c.rect(10, 13, 2, 1, E)
c.set(11, 14, E)

view(c)
finish(c)
