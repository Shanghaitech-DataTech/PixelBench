from pixelbench_api import *
c = new_canvas(64, 64)

def S(x, y, col):
    if 0 <= x < 64 and 0 <= y < 64:
        c.set(x, y, col)

def mk(rgb):
    return c.color(rgb)

skin  = mk((247,197,164))
skinS  = mk((229,172,139))
skinD  = mk((199,139,106))
hair  = mk((126,88,54))
hairH  = mk((170,128,86))
hairD  = mk((72,46,24))
navy  = mk((30,56,106))
navyD  = mk((16,33,68))
navyH  = mk((120,156,222))
scarf  = mk((198,52,52))
scarfD = mk((130,32,34))
scarfL = mk((240,116,98))
white = mk((242,245,251))
ink   = mk((46,36,42))
iris  = mk((94,56,38))
irisL = mk((150,96,58))
lens  = mk((122,208,238))
lensD = mk((56,136,182))
gmet  = mk((202,210,216))
gmetD = mk((118,128,146))

# ---------- BACK HAIR ----------
c.ellipse(33,34,15,20, hairD)      # x18-48 y14-54
c.ellipse(33,28,12,16, hairD)
# ---------- COAT SHOULDERS / BACK ----------
c.ellipse(33,58,24,15, navy)       # torso
c.ellipse(34,50,20,10, navy)

# ---------- NECK ----------
c.rect(32,44,6,5, skin)
c.line(31,48,39,48, skinD)
S(32,44,skinS);S(37,44,skinS)

# ---------- FACE ----------
c.ellipse(34,32,9,10, skin)        # x25-43 y22-42
# face shades
c.line(27,27,27,34, skinS)
c.line(27,35,26,37, skinS)
c.line(42,27,42,33, skinS)
S(42,35,skinS);S(41,37,skinD);S(42,38,skinD);S(41,38,skinD)
c.line(36,41,38,41, skinS)

# ---------- CROWN HAIR ----------
c.ellipse(34,20,13,10, hair)       # top mop x21-47 y10-30
c.ellipse(21,14,9,7, hair)         # swept left
c.ellipse(14,10,7,6, hair)
c.ellipse(10,14,5,7, hair)
c.ellipse(9,20,4,6, hair)
c.ellipse(44,15,8,7, hairH)
c.ellipse(49,24,6,7, hairH)
c.ellipse(34,12,9,4, hairH)
# ---------- BANGS ----------
for x in range(27,42): S(x,25, skinS)   # forehead shadow
for x in (27,30,33,36,39,42): S(x,24, hair)
S(28,25,hair);S(31,25,hair);S(34,25,hair);S(37,25,hair);S(40,25,hair)
S(29,26,hair);S(35,26,hair);S(41,26,hair)

# ---------- GOGGLES (forehead) ----------
c.rect(27,27,15,2, gmetD)          # band
c.ellipse(32,28,2,1, gmetD)
c.ellipse(39,28,2,1, gmetD)
c.ellipse(32,28,1,1, lens)
c.ellipse(39,28,1,1, lens)
S(31,27,lensD);S(38,27,lensD)
S(30,27,white);S(37,27,white)      # glints

# ---------- BROWS (confident) ----------
# far brow raised arch
S(27,31,ink);S(28,30,ink);S(29,30,ink);S(30,31,ink);S(31,31,ink)
S(32,30,ink);S(33,30,ink)
# near brow, angled up-right
S(36,30,hair);S(37,29,hair);S(38,29,hair);S(39,30,hair);S(40,31,hair)

# ---------- FAR EYE (viewer left) ----------
S(28,33,ink);S(29,33,ink);S(30,33,ink);S(31,33,ink)
S(28,34,ink);S(31,34,ink)
S(29,34,white);S(30,34,white)
S(29,35,iris);S(30,35,iris)
S(29,36,ink);S(30,36,ink)          # lower

# ---------- NEAR EYE (viewer right) ----------
for x in range(36,42): S(x,33,ink)       # top lid
S(36,34,ink);S(41,34,ink)
S(37,34,white);S(38,34,white);S(39,34,white);S(40,34,white)
S(37,35,iris);S(38,35,iris);S(40,35,white)
S(38,36,ink);S(39,36,ink);S(37,36,ink);S(40,36,ink)   # bottom
S(38,35,white)                     # glint over iris

# ---------- NOSE (right) ----------
S(41,38,skinS);S(42,38,skinD);S(41,39,skinD);S(42,39,skinD)

# ---------- MOUTH (confident smirk) ----------
for x in range(34,40): S(x,41, ink)
S(40,42,ink);S(41,42,ink)
S(35,42,skinD);S(36,42,skinD)

# ---------- SCARF ----------
c.rect(30,49,9,4, scarf)
S(29,50,scarf);S(39,50,scarf)
S(29,51,scarf);S(40,51,scarf)
# tail streaming left
c.poly([(30,51),(17,47),(12,49),(10,52),(15,55),(29,54)], scarfD)
c.poly([(30,53),(19,56),(15,59),(18,61),(25,57),(29,55)], scarfL)
S(13,50,scarf);S(11,53,scarf)

# ---------- COAT FRONT ----------
c.rect(25,52,19,12, navy)
c.rect(23,51,7,6, navyD)           # left lapel
c.rect(39,51,7,6, navyD)           # right lapel
# scarf over chest
c.poly([(29,53),(39,53),(40,59),(28,59)], scarf)
c.line(32,53,32,59, scarfD)
# coat opening
c.line(34,53,34,63, navyD)
S(35,53,navyD);S(35,54,navyD)
# buttons
for by in (56,59,62): S(33,by, gmet)
# shoulder detail
c.line(24,52,18,56, navyH)
c.line(41,52,47,56, navyH)
c.line(16,58,12,62, navyD)
c.line(49,58,53,62, navyD)

print(c.stats_text())

finish(c)
