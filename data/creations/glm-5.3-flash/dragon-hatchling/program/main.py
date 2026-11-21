# =============================================================
#  dragon-hatchling - 64x64 RPG enemy sprite
#  young western dragon hatchling / half-spread wings / pale belly
#  small horns / spiked tail / open-mouthed low growl
# =============================================================
c = new_canvas(64, 64, background=None, name='dragon-hatchling')

# ---------------- palette ----------------
OUT    = c.color('#1b1226', 'outline')
BODY   = c.color('#5f9e48', 'scales')
BODYD  = c.color('#3c6e30', 'scales_shade')
BODYL  = c.color('#8cc46a', 'scales_light')
WING   = c.color('#b9cf7e', 'wing_membrane')
WINGD  = c.color('#8db25a', 'wing_shade')
FARW   = c.color('#4a6b45', 'far_wing')
BELLY  = c.color('#eadcb6', 'belly')
BELLYD = c.color('#c2b189', 'belly_lines')
BONE   = c.color('#eee6cd', 'bone')
BONED  = c.color('#b9b092', 'bone_shade')
TOOTH  = c.color('#fbf8ec', 'teeth')
MOUTH  = c.color('#691e2a', 'mouth')
TONGUE = c.color('#c25160', 'tongue')
GLOW   = c.color('#9c3a44', 'throat_glow')
EYE    = c.color('#f6b73c', 'eye')
SHINE  = c.color('#ffeaa8', 'eye_shine')

# ============ 1. FAR WING (dark sail behind neck) ============
c.poly([(26,22),(32,8),(38,4),(42,12),(38,24)], FARW)
c.line(32,8,38,4,BODYD)
c.line(32,8,42,12,BODYD)

# ============ 2. FAR LEGS ============
c.rect(36,44,4,9, BODYD)
c.rect(34,53,7,3, BODYD)
c.rect(50,42,4,10, BODYD)
c.rect(48,52,7,3, BODYD)

# ============ 3. TAIL (tapers right, spikes below) ============
c.poly([(48,40),(54,42),(59,46),(63,50),(63,53),(58,53),(53,49),(48,45)], BODY)
c.poly([(52,46),(54,50),(56,47)], BONE)
c.poly([(56,48),(58,52),(60,49)], BONE)
c.poly([(60,50),(62,54),(63,51)], BONE)
c.line(50,42,56,46,BODYL)
c.line(52,48,58,52,BODYD)

# ============ 4. BODY ============
c.ellipse(40,37,10,11, BODY)
c.line(48,40,50,44,BODYD)

# ============ 5. NECK ============
c.poly([(22,14),(30,14),(36,20),(38,28),(36,36),(30,40),(24,36),(20,28),(20,20)], BODY)

# ============ 6. HEAD ============
c.ellipse(18,17,9,7, BODY)
c.poly([(14,12),(6,14),(2,18),(2,22),(6,24),(14,25)], BODY)
c.poly([(14,26),(6,28),(2,30),(4,33),(10,34),(16,33),(20,31),(20,26)], BODY)

# ============ 7. MOUTH ============
c.poly([(2,22),(13,25),(2,29)], MOUTH)
c.poly([(3,27),(8,27),(7,26),(4,26)], TONGUE)
c.poly([(11,25),(13,25),(13,27),(11,27)], GLOW)
for x,y in [(3,22),(6,23),(9,24),(12,24)]:
    c.rect(x,y,1,2,TOOTH)
for x,y in [(4,28),(7,27),(10,26)]:
    c.rect(x,y,1,2,TOOTH)

# ============ 8. EYE ============
c.rect(14,14,4,3,EYE)
c.rect(16,14,1,3,OUT)
c.set(15,14,SHINE)
c.line(12,13,20,12,BODYD)
c.set(4,18,OUT); c.set(4,19,OUT)

# ============ 9. HORNS ============
c.poly([(14,12),(18,4),(20,12)], BONE)
c.poly([(20,12),(24,6),(26,12)], BONED)

# ============ 10. NEAR WING ============
c.poly([(34,28),(46,6),(52,12),(58,16),(40,32)], WING)
c.line(34,28,46,6,BODYD)
c.line(46,6,52,12,BODYD)
c.line(46,6,58,16,BODYD)
c.line(58,16,40,32,WINGD)

# ============ 11. NEAR LEGS ============
c.poly([(26,42),(32,42),(33,52),(27,52)], BODY)
c.poly([(25,52),(34,52),(35,55),(31,57),(26,55)], BODY)
c.ellipse(44,44,5,6,BODY)
c.poly([(40,48),(48,48),(49,54),(41,54)], BODY)
c.poly([(38,54),(48,54),(50,57),(45,59),(38,56)], BODY)
c.poly([(25,54),(22,56),(26,56)], BONE)
c.poly([(38,56),(35,58),(39,58)], BONE)
c.poly([(45,58),(43,60),(47,59)], BONE)

# ============ 12. BELLY ============
c.poly([(24,28),(26,32),(30,36),(34,40),(38,42),(42,43),(46,43),(48,41),(46,38),(42,38),(38,37),(34,35),(30,32),(28,29),(26,26)], BELLY)
c.line(26,30,28,32,BELLYD)
c.line(30,34,33,36,BELLYD)
c.line(34,38,38,40,BELLYD)
c.line(40,41,45,42,BELLYD)

# ============ 13. NECK SPIKES ============
c.poly([(28,16),(30,11),(32,16)], BONE)
c.poly([(32,19),(34,14),(36,19)], BONE)

# ============ 14. SHADING ============
c.line(30,14,36,20,BODYD)
c.line(36,20,38,28,BODYD)
c.line(2,29,6,30,BODYD)
c.line(6,30,14,32,BODYD)
c.line(14,32,20,31,BODYD)
c.set(12,14,BODYL); c.set(16,13,BODYL); c.set(20,14,BODYL)
c.set(24,16,BODYL); c.set(26,18,BODYL)
c.set(34,30,BODYL); c.set(38,32,BODYL); c.set(42,34,BODYL)
c.set(36,28,BODYD); c.set(40,30,BODYD); c.set(44,32,BODYD)
c.set(46,36,BODYD); c.set(44,40,BODYD)
c.set(34,25,BODYL); c.set(37,27,BODYL); c.set(40,29,BODYL)
c.set(36,24,BODYD); c.set(39,26,BODYD); c.set(42,28,BODYD)

# ============ 15. OUTLINE ============
c.outline(OUT)
c.shift(0,1)

print(c.stats_text())
print(c.matrix_text())
finish(c)
