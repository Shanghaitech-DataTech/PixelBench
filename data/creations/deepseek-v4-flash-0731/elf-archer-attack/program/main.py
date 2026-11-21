from pixelbench_api import *

# Canvas: both frames 70x48 (shared).
# Frame 1 = original input content.
f1 = new_canvas(70, 48)
f1.blit(input_canvas, 17, 0)

# ---- palette refs (indices from the input palette, shared) ----
K  = 10   # dark magenta
I  = 8    # magenta
L  = 11   # pink
D  = 3    # skin
N  = 13   # skin shade
M  = 12   # skin light
g  = 32   # tunic green
h  = 33   # tunic light
c  = 28   # dark green
n  = 39   # pants
k  = 35   # boots (83,67,56)
l  = 36   # boot accent (116,52,28)
q  = 42   # purple cape
p  = 41   # cape light
Z  = 25   # dark
H  = 7    # gold
J  = 9    # wood
A  = 1    # dark brown
U  = 20   # ink
E  = 4    # white
b  = 27   # wood dark

f2 = new_canvas(70, 48)

# Build the figure on a 46-wide virtual grid, then blit/draw.
# We draw directly on f2 with an x-offset 12 (grid col 0 -> canvas x 12).
OX = 12

rows = {}

def fill(y, c0, c1, ch):
    for x in range(c0, c1 + 1):
        rows.setdefault(y, {})[x] = ch

# ---- cape (behind body) ----
cape_r = {
 12:[11,12], 13:[10,12], 14:[9,12], 15:[8,11], 16:[8,11], 17:[7,11],
 18:[7,10], 19:[6,10], 20:[6,9], 21:[5,9], 22:[5,9], 23:[5,8], 24:[5,8],
 25:[4,8], 26:[4,7], 27:[4,7], 28:[4,7], 29:[3,6], 30:[3,6], 31:[3,6],
 32:[3,6], 33:[3,5], 34:[3,5], 35:[3,5], 36:[3,4], 37:[3,4], 38:[3,4],
 39:[3,4], 40:[3,4], 41:[3,4], 42:[3,5], 43:[3,5], 44:[4,5], 45:[4,6],
 46:[4,6],
}
for y, xs in cape_r.items():
    for x in xs:
        rows.setdefault(y, {})[x] = q
# cape highlights / folds
hl = [(11,12),(10,13),(9,14),(8,15),(7,16),(7,17),(6,18),(5,20),(5,22),(4,25),(4,28),(3,32),(3,36),(3,40),(4,44),(5,44),(4,30),(5,34),(4,38)]
for (x, y) in hl:
    rows.setdefault(y, {})[x] = p
sh = [(12,13),(11,14),(10,15),(9,16),(8,17),(7,18),(6,20),(5,22),(5,24),(4,27),(4,30),(3,35),(3,39),(4,43),(5,45)]
for (x, y) in sh:
    rows.setdefault(y, {})[x] = Z

# ---- head ----
fill(0, 10, 15, K)
fill(1, 9, 16, K)
fill(2, 9, 16, I)
fill(3, 8, 16, I)
fill(4, 8, 11, I); fill(4, 12, 12, L); fill(4, 13, 15, D); fill(4, 16, 16, I)
fill(5, 7, 7, K); fill(5, 8, 10, I); fill(5, 11, 11, L); fill(5, 12, 16, D)
fill(6, 7, 7, I); fill(6, 8, 10, I); fill(6, 11, 11, L); fill(6, 12, 16, D)
fill(7, 8, 9, I); fill(7, 10, 11, L); fill(7, 12, 15, D); fill(7, 16, 16, U)
fill(8, 9, 10, L); fill(8, 11, 12, D); fill(8, 13, 13, U); fill(8, 15, 16, U)
fill(9, 10, 11, L); fill(9, 12, 15, D); fill(9, 16, 16, N)
fill(10, 11, 11, L); fill(10, 12, 15, D); fill(10, 16, 16, N)
fill(11, 12, 12, L); fill(11, 13, 15, D)
# ear tip
rows.setdefault(6, {})[6] = I; rows.setdefault(7, {})[7] = L

# ---- torso ----
fill(12, 13, 14, D); fill(12, 15, 15, g); fill(12, 16, 18, h); fill(12, 19, 19, g)
fill(13, 13, 15, g); fill(13, 16, 18, h); fill(13, 19, 20, g)
fill(14, 14, 15, g); fill(14, 16, 17, h); fill(14, 18, 20, g)
fill(15, 14, 15, g); fill(15, 16, 17, h); fill(15, 18, 21, g)
fill(16, 15, 16, g); fill(16, 17, 18, h); fill(16, 19, 21, g)
fill(17, 15, 16, g); fill(17, 17, 18, h); fill(17, 19, 22, g)
fill(18, 16, 17, g); fill(18, 18, 19, h); fill(18, 20, 22, g)
fill(19, 16, 17, g); fill(19, 18, 19, h); fill(19, 20, 23, g)
fill(20, 16, 17, g); fill(20, 18, 19, h); fill(20, 20, 23, g)
fill(21, 17, 18, g); fill(21, 19, 19, h); fill(21, 20, 23, g)
fill(22, 17, 23, Z)
fill(23, 18, 23, Z)
fill(24, 18, 23, n)

# ---- legs ----
fill(25, 17, 18, n); fill(25, 20, 21, n)
fill(26, 16, 17, n); fill(26, 20, 21, n)
fill(27, 15, 16, n); fill(27, 21, 22, n)
fill(28, 14, 15, n); fill(28, 21, 22, n)
fill(29, 13, 14, n); fill(29, 21, 23, n)
fill(30, 12, 13, n); fill(30, 22, 23, n)
fill(31, 12, 13, n); fill(31, 22, 23, n)
fill(32, 11, 12, n); fill(32, 23, 24, n)
fill(33, 10, 11, n); fill(33, 23, 24, n)
fill(34, 10, 11, n); fill(34, 23, 24, n)
fill(35, 9, 10, n); fill(35, 24, 25, k)
fill(36, 9, 10, k); fill(36, 24, 25, k)
fill(37, 8, 9, k); fill(37, 24, 26, k)
fill(38, 8, 9, k); fill(38, 25, 26, k)
fill(39, 7, 8, k); fill(39, 25, 27, k)
fill(40, 7, 8, k); fill(40, 26, 27, k)
fill(41, 6, 7, k); fill(41, 27, 28, k)
fill(42, 6, 7, k); fill(42, 27, 28, k)
fill(43, 5, 6, k); fill(43, 28, 29, k)
fill(44, 4, 5, k); fill(44, 29, 30, k)
fill(45, 3, 4, k); fill(45, 30, 31, k)
fill(46, 4, 4, k)
# boot accents
rows.setdefault(38, {})[7] = l
rows.setdefault(42, {})[6] = l
rows.setdefault(44, {})[29] = l
rows.setdefault(45, {})[30] = l
rows.setdefault(43, {})[28] = l

# ---- draw hand at jaw ----
rows.setdefault(11, {})[17] = D; rows.setdefault(11, {})[18] = D
rows.setdefault(12, {})[17] = D; rows.setdefault(12, {})[18] = N

# ---- bow arm (tunic) ----
arm = [(19,13),(21,14),(23,15),(25,15),(27,16),(29,16),(31,17),(33,17),(35,18),(37,18),(38,18)]
for (x, y) in arm:
    rows.setdefault(y, {})[x] = g
armh = [(20,13),(22,14),(24,15),(26,15),(28,16),(30,17),(32,17),(34,18),(36,18)]
for (x, y) in armh:
    rows.setdefault(y, {})[x] = h

# ---- paint grid onto f2 ----
for y, d in rows.items():
    for x, ch in d.items():
        f2.set(OX + x, y, ch)

# ---- string ----
f2.line(OX + 38, 2, OX + 18, 11, U)
f2.line(OX + 18, 11, OX + 38, 30, U)

# ---- bow (deep crescent) ----
f2.path(f'M{OX+37} 2 Q{OX+44} 16 {OX+37} 30', A, fill=False)
f2.path(f'M{OX+38} 2 Q{OX+45} 16 {OX+38} 30', H, fill=False)
f2.path(f'M{OX+39} 2 Q{OX+46} 16 {OX+39} 30', A, fill=False)

# ---- grip hand over bow ----
f2.rect(OX + 38, 15, 4, 3, D)
f2.rect(OX + 39, 16, 3, 1, N)

# ---- thicken the extended bow arm (drawn under the string) ----
f2.line(OX + 19, 14, OX + 38, 19, g)
f2.line(OX + 20, 15, OX + 38, 20, c)

# re-draw the string on top so it stays continuous in front of the arm
f2.line(OX + 38, 2, OX + 18, 11, U)
f2.line(OX + 18, 11, OX + 38, 30, U)

# ---- subtle ground shadow under the feet ----
shadow = {44:[3,4,5], 45:[2,3,4,5], 46:[3,4,32,33]}
for y, xs in shadow.items():
    for x in xs:
        f2.set(OX + x, y, q)

print("F1:", f1.stats_text())
print("F2:", f2.stats_text())

finish([f1, f2])
