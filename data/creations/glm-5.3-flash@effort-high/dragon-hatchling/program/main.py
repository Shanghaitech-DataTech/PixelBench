c = new_canvas(64, 64, name="hatchling")

OUT     = c.color('#141d17', 'outline')
GRN     = c.color('#4f9e58', 'scale')
GRN_D   = c.color('#33683e', 'scale_shade')
GRN_L   = c.color('#7cc06d', 'scale_light')
WING    = c.color('#5da356', 'wing')
WING_D  = c.color('#3a6b40', 'wing_shade')
BELLY   = c.color('#eadfb2', 'belly')
BELLY_D = c.color('#c3af7f', 'belly_shade')
HORN    = c.color('#e6dfc6', 'horn')
MOUTH   = c.color('#8a2a38', 'mouth')
MOUTH_D = c.color('#5c1a26', 'mouth_deep')
TEETH   = c.color('#f5f2e4', 'teeth')
EYE     = c.color('#ffd23f', 'eye')
BREATH  = c.color('#cfe8d4', 'breath')

# ================= behind layers =================
# far wing: dark sliver peeking top-right of the near wing
c.poly([(39,24),(47,7),(61,4),(56,11),(60,18),(53,20),(51,26),(41,25)], WING_D)

# far legs
c.rect(31,37,4,7, GRN_D)
c.rect(30,44,6,2, GRN_D)
c.rect(46,39,4,6, GRN_D)
c.rect(44,45,8,2, GRN_D)

# tail (drawn before body so it emerges from behind it)
c.poly([(44,34),(52,40),(63,52),(61,54),(51,46),(42,40)], GRN)
c.poly([(44,37),(53,43),(61,51),(61,54),(51,46),(42,40)], GRN_D)

# ================= body =================
c.ellipse(37,33,11,8, GRN)
c.rect(24,32,6,6, GRN)            # chest fill

# belly plates
c.poly([(28,33),(45,33),(45,36),(42,39),(38,41),(34,42),(30,41),(28,38)], BELLY)

# near legs
c.rect(24,37,5,9, GRN)
c.rect(21,46,9,3, GRN)
c.ellipse(41,38,4,4, GRN)
c.rect(40,41,4,6, GRN)
c.rect(37,47,9,3, GRN)

# neck + pale throat
c.poly([(22,16),(29,17),(35,31),(30,37),(24,36)], GRN)
c.poly([(22,17),(27,17),(29,33),(24,35)], BELLY)

# ================= head =================
c.ellipse(19,16,8,6, GRN)         # skull
c.rect(7,14,12,6, GRN)            # snout
c.poly([(7,24),(22,21),(24,23),(17,28),(9,27)], GRN)   # lower jaw

# horns (chunky truncated triangles, before outline so they keep pale cores)
c.poly([(13,12),(14,5),(18,5),(19,12)], HORN)
c.poly([(20,12),(21,5),(25,5),(26,13)], HORN)

# ================= near wing =================
c.poly([(34,29),(42,12),(56,9),(51,16),(55,23),(48,25),(46,31),(36,30)], WING)
c.line(35,28,42,13, GRN_D)
c.line(42,13,55,10, GRN_D)
c.line(42,13,54,22, GRN_D)

# scale dapples
for (x,y) in [(31,28),(35,27),(39,26),(43,28),(30,31),(34,30),(38,30),(14,13),(22,13),(26,15)]:
    c.set(x,y,GRN_L)
for (x,y) in [(33,30),(37,31),(41,30),(44,30),(28,30),(32,26),(36,25),(16,16),(20,18),(47,20),(50,22)]:
    c.set(x,y,GRN_D)
for (x,y) in [(46,20),(49,23),(52,14),(54,18)]:
    c.set(x,y,WING_D)

# belly plate lines
c.line(29,35,44,35, BELLY_D)
c.line(30,37,43,37, BELLY_D)
c.line(32,39,41,39, BELLY_D)

# ================= silhouette =================
c.outline(OUT)

# ================= face / details =================
# open growling mouth (wedge: wide at front, hinged at back)
c.poly([(7,20),(22,20),(22,21),(7,24)], MOUTH)
c.rect(18,20,4,2, MOUTH_D)
# upper teeth + fangs
for x in (9,12,15,18):
    c.set(x,20,TEETH)
c.set(7,20,TEETH); c.set(7,21,TEETH); c.set(7,22,TEETH)
c.set(21,21,TEETH)
# lower teeth
c.set(9,23,TEETH); c.set(12,22,TEETH); c.set(15,22,TEETH); c.set(18,21,TEETH)
# eye + brow + nostril
c.rect(15,12,3,2,EYE)
c.set(16,12,OUT); c.set(16,13,OUT)
c.line(14,11,18,11,GRN_D)
c.set(9,15,OUT)

# claws
c.set(20,47,HORN); c.set(20,48,HORN)
c.set(36,48,HORN); c.set(36,49,HORN)
c.poly([(40,12),(38,6),(44,11)], HORN)
c.line(40,12,38,6,OUT); c.line(38,6,44,11,OUT)

# tail spikes (post-outline, with dark edges)
for pts in ([(46,38),(48,33),(50,39)],[(53,44),(55,39),(57,45)],[(58,50),(60,45),(62,51)]):
    c.poly(pts, HORN)
    c.line(pts[0][0],pts[0][1],pts[1][0],pts[1][1],OUT)
    c.line(pts[1][0],pts[1][1],pts[2][0],pts[2][1],OUT)

# growl breath
c.line(2,18,5,18,BREATH)
c.line(1,20,4,20,BREATH)
c.line(2,22,5,22,BREATH)

print(c.stats_text())
print(c.matrix_text())
finish(c)
