from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, name="dragon")

def reg(name, hexv):
    return c.color(hexv, name=name)

OUTLINE = reg("outline", "#162e10")
BODY   = reg("body", "#3f8f3a")
DK     = reg("body_dark", "#2a5a24")
LT     = reg("body_light", "#66b252")
BELLY  = reg("belly", "#eadeb4")
BSH    = reg("belly_shade", "#c6b47e")
WING   = reg("wing", "#b04a2c")
WINGD  = reg("wing_dark", "#8c3520")
HORN   = reg("horn", "#e8d7a2")
EYE    = reg("eye", "#f2c11d")
PUPIL  = reg("pupil", "#16100a")
MOUTH  = reg("mouth", "#571010")
TONGUE = reg("tongue", "#d24a38")
TOOTH  = reg("tooth", "#f6f2e8")
CLAW   = reg("claw", "#efe0b8")

# ============ tail (behind body) ============
c.poly([(36,42),(55,40),(61,37),(58,42),(49,45),(39,46)], BODY)
# tail spikes
c.poly([(38,42),(41,43),(39,35)], BODY)
c.poly([(44,42),(47,42),(45,34)], BODY)
c.poly([(50,41),(53,40),(51,32)], BODY)
# tail tip
c.poly([(56,40),(61,37),(63,33)], BODY)
c.poly([(58,37),(60,36),(62,32)], DK)

# ============ raised wing (behind body) ============
c.poly([(25,34),(13,8),(5,17),(14,31)], WING)
c.line(24,33, 12,9, BODY)     # wing arm
c.line(13,9, 7,6, BODY)       # finger 1
c.line(12,10, 6,12, BODY)     # finger 2
c.line(11,11, 7,15, BODY)     # finger 3
c.line(11,24, 6,16, WINGD)    # membrane shading

# ============ torso ============
c.ellipse(29,43,11,10, BODY)
# neck filler (bridges head to torso with no gaps)
c.rect(27,27,20,12, BODY)
# dorsal spikes
c.poly([(24,37),(27,38),(26,30)], BODY)
c.poly([(27,35),(30,36),(29,28)], BODY)
c.poly([(30,32),(33,33),(32,26)], BODY)
# legs
c.ellipse(26,53,4,4, BODY)            # rear leg
c.ellipse(35,53,4,5, BODY)            # front leg
# belly
c.ellipse(30,47,6,5, BELLY)
c.line(27,45,27,49, BSH)
c.line(30,44,30,50, BSH)
c.line(33,44,33,49, BSH)
# claws rear foot
c.poly([(22,55),(25,55),(23,59)], CLAW)
c.poly([(26,56),(28,56),(27,59)], CLAW)
c.poly([(29,56),(31,56),(30,59)], CLAW)
# claws front foot
c.poly([(32,57),(34,57),(33,60)], CLAW)
c.poly([(35,57),(37,57),(36,60)], CLAW)
c.poly([(38,57),(40,57),(39,60)], CLAW)
# scale dots on back
for sx, sy in [(34,35),(37,36),(39,42),(41,44),(30,39),(45,44)]:
    c.set(sx, sy, DK)

# ============ head ============
c.circle(38,19,8, BODY)
# upper snout
c.poly([(43,14),(56,19),(57,23),(49,24),(42,22)], BODY)
# horns (two small blades)
c.poly([(37,14),(30,6),(40,9),(40,14)], HORN)
c.poly([(33,11),(27,5),(35,8)], HORN)
# eye + brow
c.line(33,15, 41,17, DK)
c.ellipse(39,18,2,2, EYE)
c.rect(38,17,2,4, PUPIL)
c.set(54,21, PUPIL)          # nostril
# light cheek scale
c.ellipse(35,13,2,1, LT)

# lower jaw
c.poly([(41,32),(56,34),(52,41),(40,40)], BODY)
# mouth interior (open growl)
c.poly([(43,21),(57,24),(54,32),(44,31)], MOUTH)
# tongue
c.poly([(46,26),(52,27),(50,31),(46,30)], TONGUE)
# upper fangs (apex down)
c.poly([(43,21),(45,23),(44,25)], TOOTH)
c.poly([(52,23),(54,24),(53,26)], TOOTH)
# lower fangs (apex up)
c.poly([(45,32),(47,34),(46,29)], TOOTH)
c.poly([(50,33),(52,35),(51,30)], TOOTH)

# ============ silhouette outline ============
c.outline(OUTLINE)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))
finish(c)
