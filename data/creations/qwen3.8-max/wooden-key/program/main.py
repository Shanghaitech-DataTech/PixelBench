from pixelbench_api import *

c = new_canvas(16, 16, name="wooden_key")

# --- palette (max 6 visible colours) ---
O = c.color('#241409', 'outline')      # near-black brown outline
D = c.color('#5d3a1c', 'wood_dark')    # shadow wood
M = c.color('#8c5a2c', 'wood_mid')     # base wood
L = c.color('#b9834a', 'wood_light')   # lit wood
H = c.color('#e2b87c', 'wood_hilite')  # highlight / grain glint

# ============ BOW (the round head, left side) ============
c.circle(4, 8, 4, O, fill=True)     # dark silhouette
c.circle(4, 8, 3, M, fill=True)     # wood body
# light on the upper-left of the ring
for (x, y) in [(2,5),(3,5),(4,5),(5,5),(1,6),(2,6),(3,6),(1,7),(2,7),(1,8),(1,9),(2,10),(3,11),(4,11)]:
    c.set(x, y, L)
# brightest glints on the ring crown
for (x, y) in [(3,5),(2,6),(1,7)]:
    c.set(x, y, H)
# shadow on the lower-right of the ring
for (x, y) in [(6,10),(7,9),(7,8),(5,11),(6,6),(7,7)]:
    c.set(x, y, D)
# the hole
c.rect(3, 7, 3, 3, O, fill=True)
c.rect(4, 7, 2, 2, None, fill=True)

# ============ SHAFT ============
# top outline
c.rect(7, 6, 8, 1, O)
# wood rows
c.rect(7, 7, 8, 1, L)
c.rect(7, 8, 8, 1, M)
c.rect(7, 9, 8, 1, D)
# bottom outline
c.rect(7, 10, 8, 1, O)
# rounded tip
c.set(15, 7, O); c.set(15, 8, O); c.set(15, 9, O)
c.set(14, 7, L); c.set(14, 8, M); c.set(14, 9, D)
# grain flecks on the shaft
c.set(9, 7, H); c.set(12, 7, H)
c.set(10, 8, D); c.set(13, 8, D)

# ============ TEETH ============
# tooth 1 (longer)
c.rect(9, 10, 3, 3, O)
c.rect(10, 10, 1, 2, M)
# tooth 2
c.rect(12, 10, 3, 2, O)
c.rect(13, 10, 1, 1, M)
# tooth shading: darker bottoms
c.set(10, 11, D)
# carved collar groove where shaft meets bow
c.set(8, 7, D); c.set(8, 8, D); c.set(8, 9, D)

print(c.matrix_text(indices=False))
print(c.stats_text())
p = view(c, scale=16)
print(p)
save('wooden_key', c, indexed=True)
finish(c)
