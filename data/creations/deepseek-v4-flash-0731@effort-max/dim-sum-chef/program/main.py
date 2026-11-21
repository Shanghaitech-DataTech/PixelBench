from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="chef")

O=(42,30,26); W=(255,250,240); G=(216,210,200)
SK=(248,204,156); E=(46,34,30); BZ=(236,150,130)
BA=(198,152,92); BA2=(162,112,60); BA3=(110,74,42)
BU=(255,252,242); JA=(252,252,252); JS=(214,214,216)
AP=(236,240,246); RD=(188,66,58)
PN=(86,86,96); SH=(58,48,44)

def H(x0,y0,x1,y1,o):
    c.rect(x0,y0,x1-x0+1,y1-y0+1,o)
def S(x,y,o):
    c.set(x,y,o)

# ---- legs & shoes ----
H(11,28,14,29,O); H(12,28,13,29,PN)
H(17,28,20,29,O); H(18,28,19,29,PN)
H(10,30,14,31,O); H(11,30,13,31,SH)
H(17,30,21,31,O); H(18,30,20,31,SH)

# ---- torso (chef jacket) ----
c.ellipse(16,19,8,2,O); c.ellipse(16,19,7,1,JA)
H(8,17,23,28,O); H(9,18,22,27,JA)

# ---- apron ----
H(10,17,21,26,O); H(11,18,20,25,AP)

# ---- apron waist ties ----
H(6,18,9,19,O); H(7,18,8,19,RD)
H(22,18,25,19,O); H(23,18,24,19,RD)

# ---- arms ----
H(5,19,10,25,O); H(6,20,9,23,JA)
H(21,19,26,25,O); H(22,20,25,23,JA)
H(6,23,9,24,SK); H(23,23,26,24,SK)

# ---- bamboo steamer ----
c.ellipse(16,23,4,3,O); c.ellipse(16,23,3,2,BA)
c.ellipse(16,21,3,1,BA3)

# ---- buns: three 3x3 blocks sitting in the steamer ----
H(12,18,14,20,BU); H(15,17,17,19,BU); H(18,18,20,20,BU)

# ---- fingers gripping steamer ----
H(8,22,12,23,SK); H(20,22,24,23,SK)

# ---- head ----
c.circle(9,11,2,O); c.circle(9,11,1,SK)
c.circle(23,11,2,O); c.circle(23,11,1,SK)
c.ellipse(16,11,6,5,O); c.ellipse(16,11,5,4,SK)

# ---- face ----
S(13,11,E); S(19,11,E)
S(12,12,BZ); S(20,12,BZ)
S(15,13,E); S(16,13,E); S(17,13,E)

# ---- chef hat: puffy block with band ----
c.rect(9,0,15,7,O); c.rect(10,1,13,4,W)
c.rect(9,5,15,2,O)
S(12,3,G); S(16,3,G); S(20,3,G)

# ---- collar folds ----
S(12,17,JS); S(13,18,JS); S(19,17,JS); S(18,18,JS)

# ---- steamer slats ----
for x in (13,16,19):
    S(x,22,BA2); S(x,23,BA2)

# ---- pink bun tops ----
S(16,17,BZ); S(12,18,BZ); S(18,18,BZ)
S(13,20,BZ); S(17,20,BZ); S(20,20,BZ)

# ---- flour dust on apron ----
for (x,y) in [(10,19),(11,20),(11,21),(10,22),(11,23),(11,25),
             (20,19),(21,20),(21,21),(19,22),(20,23),(20,25)]:
    S(x,y,W)

print(c.stats_text())
finish([c])
