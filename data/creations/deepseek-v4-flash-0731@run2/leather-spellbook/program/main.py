from pixelbench_api import *

INK = "#16100a"   # dark outline
PAGE = "#d8c49a"  # page edges
LE = "#6b4423"    # leather
LD = "#3a2412"    # dark leather
LL = "#9a6233"    # light leather
MET = "#b8903f"   # metal corners
ML = "#e6c97e"    # metal highlight
GEM = "#c23b3b"   # gem / ribbon

c = new_canvas(32, 32, name="spellbook")

# dark silhouette of the closed book
c.rect(3, 4, 26, 23, INK)            # x3..28, y4..26

# top page edges
c.rect(4, 4, 24, 2, PAGE)            # x4..27, y4..5
for x in (10, 14, 18, 22):
    c.line(x, 4, x, 5, INK)

# leather cover
c.rect(4, 7, 24, 19, LE)              # x4..27, y7..25
c.rect(4, 7, 24, 1, LL)               # top bevel highlight

# spine / hinge strip along the left
c.rect(4, 7, 3, 19, LD)
for by in (10, 14, 18, 22):
    c.rect(4, by, 3, 2, LE)

# subtle right-edge shading
c.rect(26, 7, 2, 19, LD)

# tooled border frame
c.rect(8, 9, 18, 15, LD, fill=False)  # x8..25, y9..23
c.rect(8, 9, 18, 1, LL)

# metal corner brackets
# top-left
c.rect(5, 8, 7, 2, MET)
c.rect(5, 8, 2, 7, MET)
c.rect(5, 8, 7, 1, ML)
c.rect(5, 8, 1, 7, ML)
# top-right
c.rect(21, 8, 7, 2, MET)
c.rect(26, 8, 2, 7, MET)
c.rect(21, 8, 7, 1, ML)
c.rect(26, 8, 1, 7, ML)
# bottom-left
c.rect(5, 24, 7, 2, MET)
c.rect(5, 19, 2, 7, MET)
c.set(10, 24, ML)
# bottom-right
c.rect(21, 24, 7, 2, MET)
c.rect(26, 19, 2, 7, MET)
c.set(22, 24, ML)

# central emblem: gold diamond with a red gem
c.poly([(16, 11), (23, 16), (16, 21), (9, 16)], MET)
c.poly([(16, 13), (21, 16), (16, 19), (11, 16)], GEM)
c.set(15, 14, ML)
c.set(15, 15, ML)

# bookmark ribbon peeking out below
c.poly([(14, 26), (18, 26), (16, 29)], GEM)

# crisp dark outline around the whole book
c.rect(3, 4, 26, 23, INK, fill=False)

print(c.stats_text())
print(c.matrix_text(indices=False))
finish(c)
