from pixelbench_api import *

c = new_canvas(32, 32, name="farm-chicken")

O = c.color("#6E4A33")   # soft dark warm outline
B = c.color("#EFDAA6")   # body cream
C = c.color("#F8E9C4")   # light cream
S = c.color("#DCB67D")   # soft belly shadow
W = c.color("#D9A967")   # wing/tail tan
D = c.color("#C08B4E")   # wing shade
F = c.color("#A9773C")   # feather line
R = c.color("#C75C4E")   # comb / wattle red
K = c.color("#E9A13C")   # beak
E = c.color("#4A3627")   # eye
L = c.color("#E39A3F")   # legs
l = c.color("#BC7A2F")   # feet
P = c.color("#EBB695")   # blush

# ---- silhouette (soft dark warm brown) ----
c.ellipse(25.5, 5.3, 2.6, 1.7, O)     # comb
c.ellipse(7.0, 16.0, 4.3, 4.6, O)     # fluffy tail
c.ellipse(16.5, 18.5, 9.3, 7.6, O)    # plump body
c.circle(25.5, 9.5, 4.5, O)           # head
c.poly([(28, 9), (31, 10), (31, 12), (28, 12)], O)  # beak

# ---- base fills ----
c.ellipse(25.5, 5.3, 1.8, 1.1, R)     # comb red
c.ellipse(7.0, 16.0, 3.4, 3.8, W)     # tail tan
c.ellipse(16.5, 18.5, 8.4, 6.8, B)    # body
c.circle(25.5, 9.5, 3.6, B)           # head
c.poly([(28.5, 9.8), (30.6, 10.2), (30.6, 11.6), (28.5, 11.3)], K)  # beak
c.set(27, 9, K)

# ---- wing: dark disc + tan fill = layered wing ----
c.ellipse(14.4, 18.6, 4.2, 3.4, D)
c.ellipse(14.4, 18.6, 3.3, 2.6, W)
c.set(5, 15, F)
c.set(5, 17, F)

# ---- face ----
c.set(24, 9, E); c.set(25, 9, E); c.set(24, 10, E); c.set(25, 10, E)
c.set(25, 9, C)                         # eye glint
c.set(26, 10, P); c.set(27, 11, P)      # blush
c.set(26, 12, R); c.set(27, 12, R); c.set(28, 12, R); c.set(26, 13, R)  # wattle

# ---- soft shading ----
c.ellipse(20.4, 21.6, 2.0, 1.9, C)     # light chest bib
c.set(11, 13, C); c.set(12, 13, C)      # back highlight
c.set(12, 24, S); c.set(13, 24, S); c.set(14, 24, S)
c.set(15, 24, S); c.set(16, 24, S)      # belly shadow

# ---- legs & feet ----
c.set(14, 26, L); c.set(14, 27, L)
c.set(17, 26, L); c.set(17, 27, L)
c.set(12, 28, l); c.set(13, 28, l); c.set(14, 28, l)
c.set(15, 28, l); c.set(16, 28, l); c.set(17, 28, l); c.set(18, 28, l); c.set(19, 28, l)

print(c.stats_text())
print(c.matrix_text(region=(19, 6, 31, 15)))
print(c.matrix_text(region=(9, 19, 23, 29)))

finish(c)
