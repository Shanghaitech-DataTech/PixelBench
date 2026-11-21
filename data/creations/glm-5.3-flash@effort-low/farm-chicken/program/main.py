from pixelbench_api import *

c = new_canvas(32, 32, name="chicken")

CREAM  = "#f0e2c0"   # body
LIGHT  = "#faf1dd"   # highlight
SHADE  = "#d8c298"   # body shadow
WING   = "#c9a877"   # wing
WINGD  = "#a98a5e"   # wing edge
COMB   = "#c4554a"   # comb / wattle
COMBD  = "#a03c34"
BEAK   = "#e0913a"
BEAKD  = "#b56f26"
EYE    = "#3a2a20"
LEG    = "#d98f3a"
TAIL   = "#e8d9b8"

# --- body: plump rounded shape (side view facing left) ---
# main mass
c.ellipse(17, 18, 9, 7, CREAM)
c.ellipse(13, 16, 6, 5, CREAM)

# --- head ---
c.circle(11, 9, 4, CREAM)

# neck shadow under head
for x in range(10, 15):
    c.set(x, 12, SHADE)

# comb (three bumps on top of head)
c.set(9, 4, COMB); c.set(10, 4, COMB)
c.set(11, 3, COMB); c.set(12, 3, COMB); c.set(12, 4, COMB)
c.set(13, 4, COMB); c.set(14, 5, COMB)
c.set(11, 4, COMBD); c.set(13, 5, COMBD)
c.set(10, 5, COMB); c.set(11, 5, COMB)

# beak (pointing left)
c.set(6, 9, BEAK); c.set(7, 9, BEAK); c.set(5, 9, BEAKD)
c.set(7, 10, BEAKD)

# wattle
c.set(8, 12, COMB); c.set(8, 13, COMBD); c.set(9, 13, COMB)

# eye
c.set(10, 8, EYE); c.set(9, 8, EYE)

# --- neck blend ---
c.rect(10, 12, 5, 4, CREAM)

# --- wing: rounded leaf shape on body ---
c.ellipse(18, 18, 5, 4, WING)
c.ellipse(19, 18, 3, 2, WINGD)
# wing feather tips
for x, y in [(14,17),(13,18),(13,19),(14,20),(15,21)]:
    c.set(x, y, WINGD)

# --- body shading (lower belly) ---
for x in range(10, 26):
    for y in range(22, 26):
        if c.get(x, y) and c.get(x, y) != 0:
            pass
# simpler: shade a band
c.ellipse(16, 23, 8, 3, SHADE)
# re-cover wing area
c.ellipse(18, 18, 5, 4, WING)
c.ellipse(19, 18, 3, 2, WINGD)
for x, y in [(14,17),(13,18),(13,19),(14,20),(15,21)]:
    c.set(x, y, WINGD)

# highlight on upper back (drawn after shading so it stays bright)
c.ellipse(16, 13, 5, 2, LIGHT)
# cheek highlight on head
c.set(9, 7, LIGHT); c.set(10, 7, LIGHT)

# --- tail: soft feathers pointing up-right ---
c.poly([(24,15),(29,8),(30,9),(26,16)], TAIL)
c.poly([(25,17),(30,11),(30,12),(27,18)], TAIL)
c.poly([(25,19),(30,14),(30,15),(27,20)], TAIL)
c.set(29,8,SHADE); c.set(30,11,SHADE); c.set(30,14,SHADE)

# --- legs ---
c.set(14, 25, LEG); c.set(14, 26, LEG)
c.set(13, 27, LEG); c.set(14, 27, LEG); c.set(15, 27, LEG)
c.set(19, 25, LEG); c.set(19, 26, LEG)
c.set(18, 27, LEG); c.set(19, 27, LEG); c.set(20, 27, LEG)

# tidy: remove stray transparent-edge artifacts from ellipses at bottom
# legs (with tiny feet)
c.set(14, 25, LEG); c.set(14, 26, LEG)
c.set(13, 27, LEG); c.set(14, 27, LEG); c.set(15, 27, LEG)
c.set(19, 25, LEG); c.set(19, 26, LEG)
c.set(18, 27, LEG); c.set(19, 27, LEG); c.set(20, 27, LEG)
c.set(16, 25, SHADE); c.set(17, 25, SHADE)

print(c.stats_text())
print(c.matrix_text())

result = c
save("farm-chicken", c)
finish(result)
