from pixelbench_api import new_canvas, view, save, flatten, finish

# Palette
outline = "#1a1c23"
body_dark = "#7a2026"
body_base = "#b3323b"
body_light = "#d95763"
belly_dark = "#d1a67d"
belly_base = "#f2d4a7"
belly_light = "#fff1cc"
wing_dark = "#3d2330"
wing_base = "#663b4a"
wing_light = "#8f5765"
horn_base = "#c4bba9"
horn_light = "#f0ebdf"
mouth_dark = "#4a1823"
mouth_base = "#8a2c3a"
eye_color = "#ffcc00"
teeth_color = "#ffffff"

c_far_wing = new_canvas(64, 64)
c_far_limbs = new_canvas(64, 64)
c_tail = new_canvas(64, 64)
c_body = new_canvas(64, 64)
c_head = new_canvas(64, 64)
c_near_limbs = new_canvas(64, 64)
c_near_wing = new_canvas(64, 64)

# --- Far Wing ---
c_far_wing.path("M 40 30 L 44 10 Q 54 10 58 14 Q 56 18 62 22 Q 54 26 52 32 Q 46 30 40 30 Z", wing_dark)
c_far_wing.line(40, 30, 44, 10, body_dark)
c_far_wing.line(44, 10, 58, 14, body_dark)
c_far_wing.line(44, 10, 62, 22, body_dark)
c_far_wing.line(44, 10, 52, 32, body_dark)
c_far_wing.outline(outline)

# --- Far Limbs ---
# hind leg
c_far_limbs.poly([(38, 42), (44, 40), (46, 48), (40, 50)], body_dark)
c_far_limbs.poly([(40, 50), (46, 48), (48, 54), (42, 56)], body_dark)
c_far_limbs.rect(42, 56, 2, 2, horn_base)
c_far_limbs.rect(46, 55, 2, 2, horn_base)
# front leg
c_far_limbs.poly([(26, 38), (30, 36), (32, 42), (28, 44)], body_dark)
c_far_limbs.poly([(28, 44), (32, 42), (32, 48), (28, 50)], body_dark)
c_far_limbs.rect(28, 50, 2, 2, horn_base)
c_far_limbs.rect(31, 49, 2, 2, horn_base)
c_far_limbs.outline(outline)

# --- Tail ---
c_tail.path("M 36 44 C 48 44 56 48 62 46 C 58 52 48 56 36 54 Z", body_base)
c_tail.path("M 36 48 C 48 48 56 52 62 48 C 58 52 48 56 36 54 Z", body_dark)
# Tail spikes
c_tail.poly([(46, 45), (48, 38), (50, 46)], horn_base)
c_tail.poly([(54, 47), (58, 40), (58, 48)], horn_base)
c_tail.outline(outline)

# --- Body ---
c_body.poly([(22, 24), (30, 24), (38, 34), (42, 44), (36, 54), (24, 54), (20, 44), (20, 32)], body_base)
c_body.poly([(28, 24), (30, 24), (38, 34), (42, 44), (36, 54), (30, 54), (36, 44), (32, 34)], body_dark)

# Belly
c_body.poly([(22, 24), (26, 24), (32, 34), (34, 44), (28, 54), (24, 54), (20, 44), (20, 32)], belly_base)
c_body.poly([(23, 24), (26, 24), (31, 34), (33, 44), (28, 52), (25, 52), (21, 44), (21, 32)], belly_light)

# Belly lines
c_body.line(21, 30, 29, 30, belly_dark)
c_body.line(21, 36, 32, 36, belly_dark)
c_body.line(22, 42, 33, 42, belly_dark)
c_body.line(23, 48, 31, 48, belly_dark)

# Back spikes
c_body.poly([(34, 30), (38, 24), (38, 32)], horn_base)
c_body.poly([(38, 36), (44, 32), (42, 40)], horn_base)
c_body.poly([(40, 46), (48, 42), (42, 48)], horn_base)
c_body.outline(outline)

# --- Head ---
c_head.poly([(12, 16), (22, 14), (28, 16), (32, 22), (30, 30), (22, 32), (12, 30), (8, 24), (8, 20)], body_base)
c_head.poly([(14, 30), (22, 32), (30, 30), (32, 22), (28, 24), (22, 28), (14, 28)], body_dark)
c_head.poly([(12, 16), (22, 14), (28, 16), (32, 22), (28, 22), (22, 18), (14, 18)], body_light)

# Mouth (Open, growling)
c_head.poly([(8, 24), (20, 24), (22, 26), (18, 28), (10, 28)], mouth_dark)
c_head.poly([(12, 26), (18, 26), (16, 28), (12, 28)], mouth_base) # tongue
# Teeth
c_head.rect(9, 24, 1, 2, teeth_color)
c_head.rect(13, 24, 1, 2, teeth_color)
c_head.rect(17, 24, 1, 2, teeth_color)
c_head.rect(11, 27, 1, 2, teeth_color)
c_head.rect(15, 27, 1, 2, teeth_color)

# Eye
c_head.rect(14, 17, 3, 4, eye_color)
c_head.rect(15, 18, 2, 2, outline) # pupil
c_head.set(14, 17, teeth_color) # highlight

# Angry brow
c_head.line(12, 16, 18, 18, body_dark)
c_head.line(12, 15, 18, 17, body_dark)

# Horns
c_head.poly([(22, 14), (24, 6), (26, 14)], horn_base)
c_head.poly([(26, 15), (32, 8), (30, 16)], horn_base)
c_head.line(23, 13, 24, 7, horn_light)
c_head.line(27, 14, 31, 9, horn_light)
c_head.outline(outline)

# --- Near Limbs ---
# Front leg
c_near_limbs.poly([(22, 40), (28, 38), (32, 46), (26, 48)], body_base)
c_near_limbs.poly([(26, 48), (32, 46), (30, 52), (24, 54)], body_dark)
c_near_limbs.rect(24, 54, 2, 2, horn_base)
c_near_limbs.rect(27, 53, 2, 2, horn_base)
c_near_limbs.rect(30, 51, 2, 2, horn_base)

# Hind leg
c_near_limbs.poly([(26, 44), (36, 42), (40, 52), (30, 54)], body_base)
c_near_limbs.poly([(30, 54), (40, 52), (42, 58), (32, 60)], body_dark)
c_near_limbs.rect(32, 60, 2, 2, horn_base)
c_near_limbs.rect(36, 59, 2, 2, horn_base)
c_near_limbs.rect(40, 58, 2, 2, horn_base)
c_near_limbs.outline(outline)

# --- Near Wing ---
c_near_wing.path("M 32,32 L 36,6 Q 48,6 52,10 Q 50,16 58,20 Q 50,24 48,32 Q 40,30 32,32 Z", wing_base)
c_near_wing.line(32, 32, 36, 6, body_base)
c_near_wing.line(36, 6, 52, 10, body_base)
c_near_wing.line(36, 6, 58, 20, body_base)
c_near_wing.line(36, 6, 48, 32, body_base)

c_near_wing.line(31, 32, 35, 6, body_light)
c_near_wing.line(35, 6, 51, 10, body_light)
c_near_wing.line(35, 6, 57, 20, body_light)
c_near_wing.line(35, 6, 47, 32, body_light)
c_near_wing.outline(outline)

final = flatten([c_far_wing, c_far_limbs, c_tail, c_body, c_head, c_near_limbs, c_near_wing])
finish(final)
