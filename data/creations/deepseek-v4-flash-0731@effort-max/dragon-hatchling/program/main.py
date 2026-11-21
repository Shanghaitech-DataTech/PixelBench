from pixelbench_api import new_canvas, finish

OUT    = "#101a12"   # outline
BODY   = "#3b6b2c"   # main body green
BODY_D = "#27491e"   # shadow green
BODY_L = "#558c3c"   # highlight green
MEM    = "#c04a2a"   # wing membrane
MEM_D  = "#93331c"   # membrane shading / ribs
BONE   = "#e8d9a8"   # horns, claws
BELLY  = "#f4e6b8"   # pale belly
BELLY_D= "#dcc086"   # belly shading
EYE    = "#ffd23e"
PUPIL  = "#1a1208"
MOUTH  = "#6b1620"
TONGUE = "#e2688e"
TOOTH  = "#f7f2df"

c = new_canvas(64, 64)

# ---------- wings (behind the body, half-spread, scalloped edges) ----------
c.poly([(25,28),(13,8),(9,12),(12,16),(16,20),(20,24),(24,26),(26,28)], MEM)
c.poly([(37,28),(39,26),(44,23),(50,18),(53,12),(50,7),(38,27)], MEM)
c.line(25,28,13,8, MEM_D); c.line(25,28,9,12, MEM_D)
c.line(25,28,12,16, MEM_D); c.line(25,28,16,20, MEM_D); c.line(25,28,20,24, MEM_D)
c.line(37,28,50,7, MEM_D); c.line(37,28,53,12, MEM_D)
c.line(37,28,50,18, MEM_D); c.line(37,28,44,23, MEM_D)

# ---------- spiked tail (chain of strongly overlapping ellipses = one blob) ----------
c.ellipse(43, 47, 7, 5, BODY)
c.ellipse(52, 47, 6, 5, BODY)
c.ellipse(59, 47, 4, 4, BODY)

# ---------- body core ----------
c.ellipse(30, 42, 13, 11, BODY)          # torso
c.rect(21, 26, 17, 8, BODY)              # neck
c.ellipse(28, 20, 7, 6, BODY)            # skull
c.rect(33, 19, 13, 9, BODY)              # upper snout
c.circle(46, 22, 1, BODY)                 # nose
c.rect(34, 28, 11, 9, BODY)              # lower jaw

# ---------- open growing mouth / teeth / tongue (all interior) ----------
c.rect(35, 27, 10, 5, MOUTH)             # mouth cavity
c.poly([(36,26),(38,26),(37,29)], TOOTH)
c.poly([(40,26),(42,26),(41,29)], TOOTH)
c.poly([(44,26),(45,26),(44,29)], TOOTH)
c.poly([(37,31),(39,31),(38,28)], TOOTH)
c.poly([(41,31),(43,31),(42,28)], TOOTH)
c.poly([(38,29),(42,29),(41,32),(39,32)], TONGUE)

# ---------- legs + claws ----------
c.poly([(31,47),(41,46),(40,55),(33,55)], BODY)   # front leg
c.poly([(18,49),(25,47),(25,55),(18,55)], BODY)   # hind leg
c.poly([(33,55),(35,55),(34,59)], BONE)
c.poly([(36,55),(38,55),(37,59)], BONE)
c.poly([(38,55),(40,55),(39,59)], BONE)
c.poly([(20,55),(22,55),(21,59)], BONE)
c.poly([(22,55),(24,55),(23,59)], BONE)

# ---------- horns (small) ----------
c.poly([(22,16),(24,8),(27,15)], BONE)
c.poly([(28,16),(30,9),(33,15)], BONE)

# ---------- back / neck / tail spikes ----------
c.poly([(22,24),(19,20),(25,25)], BODY_D)
c.poly([(24,28),(21,25),(27,29)], BODY_D)
c.poly([(20,33),(17,29),(24,34)], BODY_D)
c.poly([(45,44),(47,37),(50,43)], BODY_D)
c.poly([(52,44),(55,37),(58,43)], BODY_D)
c.poly([(59,44),(61,43),(60,50)], BONE)    # tail tip spike

# ---------- pale belly ----------
c.poly([(21,40),(34,38),(39,43),(39,52),(33,55),(24,55),(20,49)], BELLY)
c.line(24, 51, 34, 50, BELLY_D)

# ---------- strong silhouette outline ----------
c.outline(OUT)

# ---------- face details (after outline so they survive) ----------
c.circle(28, 19, 2, EYE)                   # eye
c.circle(28, 19, 1, PUPIL)
c.line(23, 14, 27, 17, OUT)                # angry brow
c.set(46, 22, OUT); c.set(47, 21, OUT)      # nostril

# ---------- scale highlights ----------
c.set(29, 33, BODY_L); c.set(35, 42, BODY_L)
c.set(25, 47, BODY_L); c.set(33, 50, BODY_L); c.set(21, 44, BODY_L)

print(c.stats_text())
print(c.matrix_text(region=(4, 5, 50, 40)))
print(c.matrix_text(region=(16, 40, 63, 61)))

finish(c)
