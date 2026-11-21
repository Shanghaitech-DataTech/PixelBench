# Sky pirate girl - 64x64 anime portrait, 3/4 view facing left
c = new_canvas(64, 64, background=None, name="sky-pirate-girl")

# ---------- palette ----------
OUT     = "#33202b"   # dark plum outline
SKIN    = "#f3c39c"
SKIN_SH = "#d9966a"
BLUSH   = "#ef9d8d"
HAIR    = "#8a4b2d"
HAIR_D  = "#5f3220"
HAIR_L  = "#c47b42"
HAIR_SH = "#e9a55e"
NAVY    = "#2f3a5e"
NAVY_D  = "#1d2742"
NAVY_L  = "#47587f"
RED     = "#c8332b"
RED_D   = "#8e1f1f"
RED_L   = "#e86048"
BRASS   = "#c8912f"
BRASS_L = "#f0c060"
BRASS_D = "#7a5416"
GLASS   = "#a8dcea"
GLASS_D = "#6fb3c9"
STRAP   = "#4a3226"
EYE     = "#2f8f5f"
EYE_D   = "#1c5c3c"
EYE_L   = "#63c189"
WHITE   = "#ffffff"
MOUTH   = "#9c3f36"

# ---------- silhouette shapes (outline pass applies to these) ----------
# back hair mass + wind-swept spikes blowing right
c.ellipse(29, 17, 12, 10, HAIR)
c.poly([(37,8),(48,2),(45,8),(56,5),(44,12)], HAIR)          # top spike
c.poly([(39,13),(53,9),(48,14),(59,13),(44,18)], HAIR)        # mid spike
c.poly([(38,18),(49,23),(55,30),(48,32),(40,24)], HAIR)       # lower lock
c.poly([(19,11),(12,16),(15,22),(20,17)], HAIR)               # left wisp
c.poly([(37,21),(43,30),(42,39),(36,32)], HAIR)               # back hair right
c.poly([(19,20),(17,30),(20,36),(23,28)], HAIR)               # back hair left
# goggle strap end flapping in the wind
c.line(35,10,44,8,STRAP)
c.set(44,9,STRAP)
c.line(19,10,21,10,STRAP)
# neck, face, ear
c.rect(25,34,7,9,SKIN)
c.poly([(21,16),(36,16),(38,22),(37,28),(33,34),(28,37),(24,34),(20,27),(20,21)], SKIN)
c.rect(38,24,2,4,SKIN)
# navy coat
c.poly([(12,63),(12,53),(15,47),(21,42),(25,40),(34,40),(40,43),(44,48),(46,55),(46,63)], NAVY)
# standing collar flaps
c.poly([(20,41),(23,35),(27,41),(25,45)], NAVY)
c.poly([(34,41),(37,35),(40,42),(36,46)], NAVY)
# red scarf: wrap + knot + wind-blown tail
c.poly([(20,39),(27,36),(35,36),(39,39),(37,46),(24,46),(20,44)], RED)
c.poly([(34,40),(39,42),(37,47),(32,45)], RED)
c.poly([(36,41),(46,36),(58,34),(61,38),(52,44),(43,47),(36,46)], RED)
# one silhouette outline for the whole character
c.outline(OUT)

# ---------- details ----------
# jagged bangs over forehead
c.poly([(19,11),(20,17),(22,13),(23,19),(25,14),(27,19),(29,14),(31,18),(33,13),(35,17),(37,13),(38,15),(38,11)], HAIR)
# side strands framing the face
c.poly([(18,12),(20,20),(19,27),(21,31),(23,26),(22,13)], HAIR)
c.poly([(39,13),(40,20),(39,28),(41,30),(42,20),(41,12)], HAIR)
# ear over the strand
c.rect(38,24,2,4,SKIN)
c.set(38,25,SKIN_SH)
c.set(39,24,OUT); c.set(39,27,OUT)
c.set(38,28,BRASS_L)   # tiny earring
# goggles resting on the forehead
c.circle(23,10,3,BRASS); c.circle(23,10,2,GLASS)
c.circle(31,10,3,BRASS); c.circle(31,10,2,GLASS)
c.set(27,9,BRASS_D); c.set(27,10,BRASS_D)
c.line(21,13,24,13,BRASS_D); c.line(29,13,32,13,BRASS_D)
c.set(22,7,BRASS_L); c.set(30,7,BRASS_L)
c.set(21,9,WHITE); c.set(22,8,WHITE)
c.set(29,9,WHITE); c.set(30,8,WHITE)
c.line(22,12,24,12,GLASS_D); c.line(30,12,32,12,GLASS_D)
# eyes - far (left) one narrower for the 3/4 turn
c.line(21,25,25,25,OUT); c.set(20,26,OUT)
c.rect(22,26,3,3,EYE)
c.line(22,26,24,26,EYE_D)
c.set(22,27,WHITE)
c.line(22,29,24,29,SKIN_SH)
c.line(29,25,34,25,OUT); c.set(35,26,OUT)
c.rect(30,26,4,3,EYE)
c.line(30,26,33,26,EYE_D)
c.set(34,27,OUT)
c.set(31,27,WHITE); c.set(33,28,WHITE)
c.set(31,28,EYE_L); c.set(32,28,EYE_L)
c.line(30,29,33,29,SKIN_SH)
# brows, nose, confident smirk, blush
c.line(21,23,25,22,HAIR_D)
c.line(30,22,34,23,HAIR_D)
c.set(27,30,SKIN_SH)
c.line(25,33,29,33,MOUTH); c.set(29,32,MOUTH)
c.set(23,30,BLUSH); c.set(22,31,BLUSH); c.set(23,31,BLUSH)
c.set(34,30,BLUSH); c.set(35,31,BLUSH); c.set(34,31,BLUSH)
# (neck fully covered by the raised scarf - no chin line needed)
# hair shine + shadow
c.line(22,9,25,7,HAIR_L)
c.line(26,7,30,8,HAIR_L)
c.set(23,8,HAIR_SH); c.set(24,8,HAIR_SH)
c.line(41,8,47,4,HAIR_L)
c.line(43,17,51,14,HAIR_D)
c.line(20,21,19,27,HAIR_D)
c.line(38,26,41,33,HAIR_D)
# coat details
c.line(28,47,27,63,NAVY_D)                 # placket
c.set(25,50,BRASS); c.set(25,56,BRASS); c.set(25,62,BRASS)
# leather crossbody strap with brass buckle
c.line(16,51,43,61,STRAP)
c.set(29,55,BRASS_L); c.set(30,56,BRASS); c.set(29,56,BRASS)
c.line(13,50,18,46,NAVY_L)
c.line(44,52,45,60,NAVY_D)
c.line(22,47,36,47,NAVY_D)
c.set(22,37,NAVY_L); c.set(21,38,NAVY_L)
c.set(37,37,NAVY_D); c.set(38,38,NAVY_D)
# scarf folds
c.line(23,42,26,43,RED_D)
c.line(29,44,32,45,RED_D)
c.line(22,40,27,39,RED_L)
c.line(40,43,48,39,RED_D)
c.line(46,44,53,41,RED_D)
c.line(39,41,47,37,RED_L)
c.set(35,42,RED_D); c.set(36,43,RED_D)
# scarf knot where the tail springs out
c.poly([(33,41),(37,40),(39,43),(37,47),(33,46),(32,43)], RED)
c.line(34,41,36,41,RED_L)
c.line(33,45,36,46,RED_D)
c.set(38,42,RED_D)
c.line(45,40,54,37,RED_L)

print(c.stats_text())
print(c.matrix_text(region=(14,36,46,48)))
view(c)
finish(c)
