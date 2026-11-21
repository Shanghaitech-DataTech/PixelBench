from pixelbench_api import *

INK      = (24, 16, 12)     # near-black outline
DARK     = (62, 34, 18)     # leather shadow / spine
LEA      = (96, 54, 26)     # leather mid
HI       = (134, 80, 40)    # leather highlight
BRASS    = (196, 150, 40)   # metal plates
BRASS_HI = (236, 202, 84)   # metal shine
BRASS_DK = (122, 90, 20)    # metal shading
PAGE     = (216, 188, 138)  # page edges

c = new_canvas(32, 32, name="spellbook")

# --- silhouette: dark outline, leather cover, page block on the right ---
c.rect(3, 4, 26, 22, INK, fill=False)   # x3..28, y4..25
c.rect(4, 5, 21, 20, LEA)               # cover x4..24, y5..24
c.rect(25, 6, 3, 18, PAGE)              # page edges x25..27, y6..23
c.rect(25, 5, 3, 1, HI)                 # leather top edge above pages
c.rect(25, 24, 3, 1, DARK)              # leather bottom edge below pages

# --- leather shading ---
c.line(4, 5, 24, 5, HI)                 # top highlight
c.line(4, 24, 24, 24, DARK)             # bottom shadow
c.line(24, 6, 24, 23, DARK)             # fore-edge shadow
c.rect(4, 5, 4, 20, DARK)               # spine strip x4..7
c.line(8, 6, 8, 23, HI)                 # hinge crease highlight

# --- chamfered metal corner plates ---
def plate(cx, cy, sx, sy):
    for i in range(5):
        for j in range(5):
            if i + j <= 4:
                col = BRASS_DK if i + j == 4 else (BRASS_HI if (i == 0 or j == 0) else BRASS)
                c.set(cx + sx * i, cy + sy * j, col)

plate(4, 5,  1,  1)    # top-left
plate(24, 5, -1,  1)   # top-right
plate(4, 24,  1, -1)   # bottom-left
plate(24, 24, -1, -1)  # bottom-right

# --- blind-tooled border with brass corner studs ---
c.rect(11, 9, 12, 12, DARK, fill=False)  # x11..22, y9..20
for s in [(11, 9), (22, 9), (11, 20), (22, 20)]:
    c.set(*s, BRASS)

# --- brass rune diamond emblem ---
c.poly([(16, 11), (20, 15), (16, 19), (12, 15)], BRASS)
c.poly([(16, 12), (19, 15), (16, 18), (13, 15)], BRASS_HI)

print(c.stats_text())
for p in c.palette():
    print(p)
for y in range(4, 26):
    print(y, [c.get(x, y) for x in range(3, 29)])
print("plate TL rows 5-9 at cols 4-8:", [[c.get(x, y) for x in range(4, 9)] for y in range(5, 10)])

finish(c)
