# ============================================================
# Sky pirate girl - 64x64 anime portrait
# young sky pirate, goggles pushed up, short navy coat, red scarf,
# three-quarter view, confident smirk, wind-swept blonde hair
# ============================================================
c = new_canvas(64, 64, None, "result")

SKIN     = c.color('#f2c8a4', 'skin')
SKIN_SH  = c.color('#d29a76', 'skin_sh')
SKIN_HI  = c.color('#ffe6cc', 'skin_hi')
BLUSH    = c.color('#e79280', 'blush')
OUT      = c.color('#241a20', 'outline')

HAIR     = c.color('#d9a24e', 'hair')
HAIR_SH  = c.color('#a2702e', 'hair_sh')
HAIR_HI  = c.color('#f7d492', 'hair_hi')
HAIR_DK  = c.color('#6d4718', 'hair_dk')

WHITE    = c.color('#f6f4ef', 'eye_white')
IRIS     = c.color('#2f9fa6', 'iris')
IRIS_DK  = c.color('#1c5f68', 'iris_dk')
PUPIL    = c.color('#10222a', 'pupil')
LASH     = c.color('#2a1a22', 'lash')
MOUTH    = c.color('#a04a48', 'mouth')

BRASS    = c.color('#e0b34c', 'brass')
BRASS_SH = c.color('#a87c26', 'brass_sh')
LENS     = c.color('#8fd0d8', 'lens')
LENS_DK  = c.color('#3f8090', 'lens_dk')
LENS_HI  = c.color('#e2f7fa', 'lens_hi')
STRAP    = c.color('#3b2a2c', 'strap')

RED      = c.color('#cf3b33', 'red')
RED_SH   = c.color('#8e2622', 'red_sh')
RED_HI   = c.color('#ef6a58', 'red_hi')

NAVY     = c.color('#2e4166', 'navy')
NAVY_DK  = c.color('#27354f', 'navy_dk')
NAVY_HI  = c.color('#446a9c', 'navy_hi')
NAVY_LT  = c.color('#3a5580', 'navy_lt')

# ================================================== back hair mass
c.poly([(33,2),(37,4),(41,4),(45,8),(48,14),(49,21),(48,28),(48,34),(50,42),
        (43,44),(34,43),(28,40),(23,36),(20,31),(19,24),(20,17),(23,9),(26,5),(30,3)],
       HAIR_SH)
# wind-blown locks streaming to the viewer's right (tapered wedges)
for (a, b, d) in [((44,3),(48,11),(59,7)),
                  ((46,11),(49,20),(62,15)),
                  ((45,20),(48,29),(61,26)),
                  ((46,33),(52,36),(49,41))]:
    c.poly([a, b, d], HAIR)
c.line(46,5,57,8,HAIR_HI)
c.line(48,13,60,15,HAIR_HI)
c.line(47,22,58,26,HAIR_HI)
c.line(47,34,50,39,HAIR_HI)
c.line(45,9,54,8,HAIR_DK)
c.line(47,18,58,16,HAIR_DK)
c.line(46,27,56,27,HAIR_DK)

# ================================================== short navy coat
c.poly([(29,44),(39,44),(46,47),(51,50),(55,54),(58,58),(59,63),
        (5,63),(6,58),(9,54),(13,50),(19,47)], NAVY)
c.poly([(19,47),(26,44),(24,52),(20,58),(19,63),(5,63),(6,58),(9,54),(13,50)], NAVY_DK)
c.poly([(45,46),(51,49),(55,53),(58,58),(59,63),(46,63),(44,54),(42,48)], NAVY_LT)
c.line(46,47,51,50,NAVY_HI)
c.line(51,50,55,54,NAVY_HI)
c.line(55,54,58,58,NAVY_HI)
c.line(21,49,26,63,NAVY_DK)
c.line(48,51,52,63,NAVY_DK)
c.line(33,52,32,63,NAVY_DK)
c.line(36,52,35,63,NAVY_HI)
c.set(39,55,BRASS); c.set(39,60,BRASS)
c.set(40,55,BRASS_SH); c.set(40,60,BRASS_SH)

# ================================================== neck
c.rect(32, 34, 6, 11, SKIN_SH)
c.rect(35, 36, 3, 9, SKIN)

# ================================================== red scarf
c.poly([(25,45),(30,43),(38,43),(44,46),(44,49),(39,51),(31,51),(25,49)], RED)
c.line(26,45,30,44,RED_HI)
c.line(31,44,38,44,RED_HI)
c.line(38,44,42,46,RED_HI)
c.line(26,48,31,50,RED_SH)
c.line(31,50,39,50,RED_SH)
c.line(39,50,42,48,RED_SH)
c.line(29,46,29,48,RED_SH)
c.line(34,46,34,48,RED_SH)
c.circle(41, 47, 2, RED)
c.set(40, 46, RED_HI)
c.set(41, 49, RED_SH)
# hanging end
c.poly([(26,49),(31,49),(32,56),(30,60),(27,58),(25,52)], RED)
c.line(30,50,31,56,RED_SH)
c.line(30,56,29,59,RED_SH)
c.line(26,50,27,54,RED_HI)

# ================================================== face
FACE_ROWS = [
    (9,29,37),(10,27,39),(11,26,40),(12,25,41),(13,24,42),(14,24,42),(15,23,43),
    (16,23,43),(17,23,44),(18,23,44),(19,23,44),(20,23,44),(21,23,44),(22,23,44),
    (23,23,44),(24,23,44),(25,23,44),(26,24,43),(27,24,43),(28,25,42),(29,26,42),
    (30,27,41),(31,28,41),(32,29,40),(33,30,40),(34,30,39),(35,31,39),(36,32,38),
    (37,33,37),
]
for (y, x0, x1) in FACE_ROWS:
    c.line(x0, y, x1, y, SKIN)
for (y, x0, x1) in FACE_ROWS:
    if y <= 32 and x1 - x0 >= 2:
        c.line(x0, y, x0 + 1, y, SKIN_SH)
    elif y > 32:
        c.set(x0, y, SKIN_SH)
c.line(32, 38, 37, 38, SKIN_SH)        # jaw shadow on neck

# ================================================== front hair
c.poly([(18,13),(22,10),(23,19),(23,30),(31,41),(26,45),(19,39),(17,22)], HAIR)   # left lock
c.poly([(45,10),(48,13),(50,21),(49,30),(46,35),(44,28),(43,17)], HAIR)           # right lock
c.poly([(19,17),(20,9),(25,5),(28,4),(33,4),(38,5),(45,8),(48,14),(48,19),
        (45,20),(42,15),(38,20),(35,14),(31,20),(28,15),(24,20),(21,15)], HAIR)   # bangs
c.line(21,15,22,8,HAIR_DK)
c.line(28,15,28,7,HAIR_DK)
c.line(35,14,35,5,HAIR_DK)
c.line(42,15,42,7,HAIR_DK)
c.line(25,7,23,12,HAIR_HI)
c.line(31,5,30,9,HAIR_HI)
c.line(38,6,37,10,HAIR_HI)
c.line(46,9,45,13,HAIR_HI)
c.line(45,8,52,6,HAIR_HI)
c.line(47,15,55,16,HAIR_HI)

# ================================================== eyes (anime, 3/4 view)
# near eye - viewer's right
c.line(36,22,41,22,LASH)
c.line(35,23,42,23,LASH)
c.set(35,24,LASH); c.set(36,24,WHITE); c.line(37,24,40,24,IRIS_DK); c.set(41,24,WHITE); c.set(42,24,LASH)
c.set(35,25,LASH); c.set(36,25,WHITE); c.line(37,25,40,25,IRIS);      c.set(41,25,WHITE); c.set(42,25,LASH)
c.set(35,26,LASH); c.set(36,26,WHITE); c.set(37,26,IRIS); c.line(38,26,39,26,PUPIL); c.set(40,26,IRIS); c.set(41,26,WHITE); c.set(42,26,LASH)
c.set(36,27,WHITE); c.set(37,27,IRIS); c.line(38,27,39,27,PUPIL); c.set(40,27,IRIS); c.set(41,27,WHITE)
c.line(36,28,41,28,WHITE)
c.line(37,29,40,29,LASH)
c.set(38,25,LENS_HI)
# far eye - viewer's left, foreshortened
c.line(26,23,31,23,LASH)
c.line(25,24,31,24,LASH)
c.set(25,25,LASH); c.set(26,25,WHITE); c.line(27,25,29,25,IRIS_DK); c.set(30,25,WHITE); c.set(31,25,LASH)
c.set(25,26,LASH); c.set(26,26,WHITE); c.line(27,26,29,26,IRIS);      c.set(30,26,WHITE); c.set(31,26,LASH)
c.set(25,27,LASH); c.set(26,27,WHITE); c.set(27,27,IRIS); c.set(28,27,PUPIL); c.set(29,27,IRIS); c.set(30,27,WHITE); c.set(31,27,LASH)
c.line(26,28,30,28,WHITE)
c.line(27,29,29,29,LASH)
# determined brows
for (bx, by) in [(25,20),(26,20),(27,20),(28,20),(29,21),(30,21),(31,21)]:
    c.set(bx, by, LASH)
for (bx, by) in [(35,21),(36,21),(37,21),(38,20),(39,20),(40,20),(41,20),(42,20)]:
    c.set(bx, by, LASH)
# nose, confident smirk, blush
c.set(37,31,SKIN_SH); c.set(38,31,SKIN_SH); c.set(37,30,SKIN_HI)
c.line(34,34,37,34,MOUTH); c.line(38,33,39,33,MOUTH)
c.set(31,32,BLUSH); c.set(38,32,BLUSH)

# ================================================== goggles pushed up on the head
c.rect(22, 9, 6, 3, STRAP)
c.rect(44, 11, 6, 3, STRAP)
c.rect(31, 10, 5, 2, BRASS)
c.rect(31, 12, 5, 1, BRASS_SH)
c.circle(27, 11, 3, BRASS)
c.circle(27, 11, 2, LENS_DK)
c.set(26, 10, LENS_HI); c.set(26, 11, LENS); c.set(28, 12, LENS)
c.circle(39, 11, 4, BRASS)
c.circle(39, 11, 3, LENS_DK)
c.circle(39, 11, 2, LENS)
c.set(38, 9, LENS_HI); c.set(39, 9, LENS_HI); c.set(37, 10, LENS_HI)
c.set(41, 13, BRASS_SH)

# ================================================== finishing
bottom = [(x, c.get(x, 62)) for x in range(4, 61)]
for x, col in bottom:
    c.set(x, 63, col)
c.outline(OUT)
for x, col in bottom:
    c.set(x, 63, col)

print(c.stats_text())
save('sky_pirate_girl', c)
finish(c)
