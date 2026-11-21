from pixelbench_api import *

c = new_canvas(32, 32)

B = c.color((232, 224, 208))
S = c.color((176, 166, 146))
J = c.color((76, 68, 58))
O = c.color((30, 28, 26))
E = c.color((16, 14, 12))
G = c.color((198, 204, 212))
g = c.color((118, 124, 134))
H = c.color((96, 62, 38))
h = c.color((52, 40, 28))
W = c.color((158, 106, 56))
D = c.color((104, 70, 40))

content = {}

def add(colour, pts):
    for p in pts:
        content[p] = colour

# ---------- SKULL ----------
add(B, [(x, y) for x in range(14,19) for y in (4,)])
add(B, [(x, y) for x in range(13,20) for y in (5,10)])
add(B, [(x, y) for x in range(12,21) for y in (6,7,8)])
add(B, [(x, y) for x in (13,15,17) for y in (9,)])
add(B, [(x, 10) for x in range(14,17)])
add(B, [(x, 11) for x in range(13,18)])
add(E, [(14,9),(16,9),(18,9)])
add(E, [(x,y) for x in (13,14) for y in (6,7)])
add(E, [(x,y) for x in (17,18) for y in (6,7)])
add(E, [(15,8),(16,8)])

# ---------- TORSO (hunched) ----------
add(B, [(x,y) for x in range(12,18) for y in (12,)])
add(B, [(x,y) for x in range(11,17) for y in (13,)])
add(B, [(x,y) for x in range(11,16) for y in (14,)])
add(B, [(x,y) for x in range(10,15) for y in (15,)])
add(B, [(x,y) for x in range(10,14) for y in (16,)])
add(B, [(x,y) for x in range(9,13) for y in (17,)])
add(B, [(x,y) for x in range(9,12) for y in (18,)])
add(B, [(x,y) for x in range(8,11) for y in (19,)])
add(B, [(x,y) for x in range(8,10) for y in (20,)])
add(B, [(8,21),(9,21)])
add(B, [(8,22),(9,22)])

add(S, [(x,14) for x in (11,12,13)])
add(S, [(x,16) for x in (10,11,12)])
add(S, [(x,17) for x in (9,10,11)])
add(S, [(x,18) for x in (9,10)])
add(S, [(x,19) for x in (8,9)])
add(J, [(15,12),(14,11),(13,13)])

# ---------- FRONT (sword) ARM ----------
add(B, [(11,14),(10,15),(9,16),(8,17),(8,18),(7,19),(7,20),(6,21),(6,22)])
add(J, [(9,16),(8,18),(6,22)])
add(h, [(6,22),(6,23),(7,23)])
add(H, [(4,24),(5,24),(6,24),(7,24)])
add(G, [(5,25),(4,25)])
add(G, [(4,26),(3,26)])
add(G, [(3,27),(2,27)])
add(G, [(2,28)])
add(g, [(5,26),(4,27),(3,28)])

# ---------- FRONT LEG ----------
add(B, [(8,23),(9,23)])
add(B, [(8,24),(9,24)])
add(J, [(8,24)])
add(B, [(7,25),(8,25)])
add(B, [(7,26),(8,26)])
add(J, [(7,26)])
add(B, [(6,27),(7,27),(8,27),(9,27)])
add(B, [(5,27),(6,27)])

# ---------- BACK (shield) ARM ----------
add(B, [(18,13),(18,14),(19,14),(20,15),(21,15)])
add(B, [(21,16),(22,16),(23,17)])
add(J, [(21,15),(22,16)])

# ---------- SHIELD ----------
add(W, [(x,y) for x in range(23,28) for y in (15,)])
add(W, [(x,y) for x in range(22,29) for y in (16,)])
add(D, [(x,y) for x in range(22,29) for y in (17,)])
add(W, [(x,y) for x in range(22,29) for y in (18,)])
add(W, [(x,y) for x in range(23,28) for y in (19,)])
add(W, [(x,y) for x in range(24,27) for y in (20,)])
add(D, [(22,15),(28,15),(22,18),(28,18),(23,19),(27,19)])
add(J, [(25,16),(25,18)])

# ---------- BACK LEG ----------
add(B, [(13,22),(14,22),(15,22)])
add(B, [(13,23),(14,23),(15,23)])
add(B, [(14,24),(15,24)])
add(J, [(14,24)])
add(B, [(14,25),(15,25)])
add(B, [(14,26),(15,26)])
add(J, [(14,26)])
add(B, [(14,27),(15,27),(16,27),(17,27)])

# ---------- joints ----------
add(J, [(14,12),(16,13)])
add(J, [(9,22),(10,20)])

# ---------- drop shadow ----------
for x in range(4,18):
    content[(x,28)] = (0,0,0,90)
for x in range(6,17):
    content[(x,29)] = (0,0,0,70)

# ---------- apply ----------
for (x, y), col in content.items():
    c.set(x, y, col)

# ---------- auto outline ----------
SOLID = set(k for k,v in content.items())
for (x, y) in list(SOLID):
    for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if (nx, ny) not in SOLID and 0 <= nx < 32 and 0 <= ny < 32:
            c.set(nx, ny, O)

print(c.stats_text())

finish(c)
