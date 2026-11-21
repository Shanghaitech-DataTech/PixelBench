from pixelbench_api import new_canvas, finish

# Create 64x64 canvas with transparent background
c = new_canvas(64, 64, background=None, name="skill_icons")

# Define colors
dark_outline = c.color("#1a1a1a")
fire_red = c.color("#e63946")
fire_orange = c.color("#f4a261")
fire_yellow = c.color("#f9c74f")
fire_core = c.color("#fff3b0")

ice_dark = c.color("#457b9d")
ice_mid = c.color("#a8dadc")
ice_light = c.color("#e0fbfc")
ice_white = c.color("#ffffff")

heal_dark = c.color("#2d6a4f")
heal_mid = c.color("#52b788")
heal_light = c.color("#95d5b2")
heal_core = c.color("#d8f3dc")

light_dark = c.color("#e9c46a")
light_mid = c.color("#f4e4ba")
light_bright = c.color("#fff9c4")
light_white = c.color("#ffffff")

# ============ FIREBALL (top-left: 0,0 to 31,31) ============
# Outer flame shape
c.circle(16, 16, 14, fire_red, fill=True)
c.circle(14, 14, 12, fire_orange, fill=True)
c.circle(16, 15, 9, fire_yellow, fill=True)
c.circle(17, 14, 6, fire_core, fill=True)

# Flame tongues
c.poly([(16, 2), (14, 8), (18, 8)], fire_orange, fill=True)
c.poly([(2, 16), (8, 14), (8, 18)], fire_orange, fill=True)
c.poly([(30, 16), (24, 14), (24, 18)], fire_orange, fill=True)
c.poly([(16, 30), (14, 24), (18, 24)], fire_orange, fill=True)

# Dark outline around fireball
c.circle(16, 16, 14, dark_outline, fill=False)

# ============ ICE SHIELD (top-right: 32,0 to 63,31) ============
shield_cx, shield_cy = 48, 16

# Shield base shape (hexagon-like)
c.poly([(48, 2), (58, 8), (58, 20), (48, 28), (38, 20), (38, 8)], ice_mid, fill=True)
c.poly([(48, 4), (56, 9), (56, 19), (48, 24), (40, 19), (40, 9)], ice_light, fill=True)
c.poly([(48, 6), (54, 10), (54, 18), (48, 22), (42, 18), (42, 10)], ice_white, fill=True)

# Ice crystal accents
c.poly([(48, 6), (46, 10), (50, 10)], ice_dark, fill=True)
c.poly([(48, 22), (46, 18), (50, 18)], ice_dark, fill=True)

# Dark outline
c.poly([(48, 2), (58, 8), (58, 20), (48, 28), (38, 20), (38, 8)], dark_outline, fill=False)

# ============ HEALING (bottom-left: 0,32 to 31,63) ============
heart_cx, heart_cy = 16, 48

# Heart shape using path
c.path("M 16 38 C 10 32 4 36 4 44 C 4 54 16 62 16 62 C 16 62 28 54 28 44 C 28 36 22 32 16 38", heal_mid, fill=True)
c.path("M 16 40 C 12 36 6 38 6 44 C 6 52 16 60 16 60 C 16 60 26 52 26 44 C 26 38 20 36 16 40", heal_light, fill=True)
c.path("M 16 42 C 13 39 8 40 8 44 C 8 50 16 56 16 56 C 16 56 24 50 24 44 C 24 40 19 39 16 42", heal_core, fill=True)

# Sparkle accents
c.rect(10, 42, 2, 2, heal_core, fill=True)
c.rect(20, 46, 2, 2, heal_core, fill=True)
c.rect(14, 52, 2, 2, heal_core, fill=True)

# Dark outline
c.path("M 16 38 C 10 32 4 36 4 44 C 4 54 16 62 16 62 C 16 62 28 54 28 44 C 28 36 22 32 16 38 Z", dark_outline, fill=False)

# ============ LIGHTNING (bottom-right: 32,32 to 63,63) ============
bolt_cx, bolt_cy = 48, 48

# Lightning bolt shape - classic zigzag
c.poly([(52, 34), (44, 44), (50, 44), (46, 58), (56, 46), (52, 46)], light_mid, fill=True)
c.poly([(52, 36), (46, 44), (50, 44), (47, 55), (54, 47), (52, 47)], light_bright, fill=True)
c.poly([(52, 38), (48, 43), (50, 43), (48, 52), (53, 47), (52, 47)], light_white, fill=True)

# Small spark accents
c.set(52, 34, light_white)
c.set(46, 58, light_white)
c.set(56, 46, light_dark)

# Dark outline
c.poly([(52, 34), (44, 44), (50, 44), (46, 58), (56, 46), (52, 46)], dark_outline, fill=False)

# Print stats for verification
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
print(c.matrix_text(region=(32, 0, 63, 31)))
print(c.matrix_text(region=(0, 32, 31, 63)))
print(c.matrix_text(region=(32, 32, 63, 63)))

# Submit the result
finish(c)
