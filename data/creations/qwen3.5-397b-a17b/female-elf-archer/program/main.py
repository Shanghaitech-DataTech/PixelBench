from pixelbench_api import new_canvas, finish

# Create 64x64 canvas for the elf archer portrait
c = new_canvas(64, 64, name="elf_archer")

# Define color palette
# Skin tones
skin_light = c.color((255, 224, 200), "skin_light")
skin_mid = c.color((235, 195, 165), "skin_mid")
skin_shadow = c.color((210, 165, 140), "skin_shadow")
skin_blush = c.color((245, 180, 170), "skin_blush")

# Hair colors (green)
hair_dark = c.color((30, 80, 40), "hair_dark")
hair_mid = c.color((50, 120, 60), "hair_mid")
hair_light = c.color((80, 160, 90), "hair_light")
hair_highlight = c.color((120, 200, 130), "hair_highlight")

# Outfit colors (light green)
outfit_dark = c.color((60, 100, 70), "outfit_dark")
outfit_mid = c.color((100, 150, 100), "outfit_mid")
outfit_light = c.color((140, 190, 130), "outfit_light")
outfit_highlight = c.color((170, 220, 160), "outfit_highlight")

# Bow and arrows
bow_wood = c.color((120, 80, 50), "bow_wood")
bow_dark = c.color((80, 50, 30), "bow_dark")
arrow_shaft = c.color((180, 150, 100), "arrow_shaft")
arrow_fletching = c.color((200, 80, 80), "arrow_fletching")
arrow_tip = c.color((180, 180, 200), "arrow_tip")

# Eyes
eye_white = c.color((255, 255, 255), "eye_white")
eye_green = c.color((60, 140, 80), "eye_green")
eye_dark = c.color((30, 60, 40), "eye_dark")

# Lips
lip_color = c.color((200, 120, 110), "lip_color")

# Leather straps/details
leather = c.color((100, 70, 40), "leather")
leather_dark = c.color((70, 45, 25), "leather_dark")

# Metal accents
metal_light = c.color((200, 200, 210), "metal_light")
metal_dark = c.color((120, 120, 130), "metal_dark")

# Outline/shadow
outline = c.color((40, 30, 25), "outline")

# Background (slight gradient for depth)
bg_dark = c.color((30, 40, 35), "bg_dark")
bg_mid = c.color((45, 55, 50), "bg_mid")

# Draw background gradient
for y in range(64):
    for x in range(64):
        if y < 32:
            c.set(x, y, bg_dark)
        else:
            c.set(x, y, bg_mid)

# Character positioning: centered, three-quarter view facing slightly right
# Head center around x=32, y=20

# ============ HAIR (back layer, long flowing green hair) ============
# Draw the long hair first (behind everything)

# Main hair mass - flowing down the back
c.poly([
    (20, 12), (44, 12), (48, 20), (50, 35), (48, 50), (46, 58),
    (42, 60), (22, 60), (18, 58), (16, 50), (14, 35), (16, 20)
], hair_dark, fill=True)

# Hair mid tones
c.poly([
    (22, 14), (42, 14), (45, 22), (46, 35), (44, 48), (42, 56),
    (22, 56), (20, 48), (18, 35), (19, 22)
], hair_mid, fill=True)

# Hair highlights/strands
c.poly([
    (24, 16), (40, 16), (42, 24), (42, 35), (40, 45), (40, 52),
    (24, 52), (24, 45), (22, 35), (22, 24)
], hair_light, fill=True)

# Hair shine
for i in range(5):
    c.line(26 + i*2, 18, 26 + i*2, 28 + i, hair_highlight)

# Flowing hair strands on sides
c.line(18, 25, 14, 45, hair_mid)
c.line(46, 25, 50, 45, hair_mid)
c.line(17, 30, 12, 52, hair_dark)
c.line(47, 30, 52, 52, hair_dark)

# ============ POINTED EARS ============
# Left ear (visible, pointed elf ear)
c.poly([(18, 22), (20, 18), (24, 20), (22, 26), (20, 28), (17, 25)], skin_mid, fill=True)
c.poly([(19, 22), (20, 19), (22, 20), (21, 25), (20, 26), (18, 24)], skin_light, fill=True)

# Right ear (partially hidden by hair)
c.poly([(42, 22), (44, 18), (46, 20), (46, 25), (44, 27), (41, 24)], skin_mid, fill=True)

# ============ FACE ============
# Face shape - three-quarter view
c.poly([
    (20, 18), (44, 18), (46, 24), (46, 32), (44, 40), (40, 46),
    (32, 48), (24, 46), (20, 40), (18, 32), (18, 24)
], skin_mid, fill=True)

# Face highlight (center)
c.poly([
    (24, 20), (40, 20), (42, 26), (42, 34), (40, 40), (32, 42),
    (24, 40), (22, 34), (22, 26)
], skin_light, fill=True)

# Cheek blush
c.set(24, 34, skin_blush)
c.set(25, 35, skin_blush)
c.set(40, 34, skin_blush)
c.set(39, 35, skin_blush)

# Jaw shadow
c.poly([(20, 38), (22, 42), (26, 45), (32, 46), (38, 45), (42, 42), (44, 38), (42, 40), (32, 42), (22, 40)], skin_shadow, fill=True)

# ============ EYES ============
# Left eye (more visible in three-quarter view)
c.poly([(24, 26), (30, 26), (29, 28), (27, 30), (25, 30), (23, 28)], eye_white, fill=True)
c.poly([(26, 27), (29, 27), (28, 29), (27, 29)], eye_green, fill=True)
c.set(28, 27, eye_dark)  # pupil
c.set(27, 26, eye_white)  # highlight

# Right eye (slightly smaller due to perspective)
c.poly([(34, 26), (40, 26), (39, 28), (37, 30), (35, 30), (33, 28)], eye_white, fill=True)
c.poly([(36, 27), (39, 27), (38, 29), (37, 29)], eye_green, fill=True)
c.set(38, 27, eye_dark)  # pupil
c.set(37, 26, eye_white)  # highlight

# Eyebrows
c.poly([(23, 24), (30, 23), (30, 24), (23, 25)], hair_dark, fill=True)
c.poly([(34, 23), (41, 23), (41, 24), (34, 25)], hair_dark, fill=True)

# ============ NOSE ============
c.set(32, 30, skin_shadow)
c.set(32, 31, skin_shadow)
c.set(31, 32, skin_light)

# ============ MOUTH ============
c.poly([(28, 38), (36, 38), (35, 40), (32, 41), (29, 40)], lip_color, fill=True)
c.set(32, 39, skin_light)  # mouth highlight

# ============ NECK ============
c.poly([(26, 46), (38, 46), (38, 52), (26, 52)], skin_mid, fill=True)
c.poly([(28, 46), (36, 46), (36, 50), (28, 50)], skin_light, fill=True)

# ============ OUTFIT (light green, archer style) ============
# Main tunic/body
c.poly([
    (22, 52), (42, 52), (46, 58), (48, 63), (16, 63), (18, 58)
], outfit_mid, fill=True)

# Chest area
c.poly([
    (24, 52), (40, 52), (42, 58), (38, 62), (26, 62), (22, 58)
], outfit_light, fill=True)

# Shoulder pads/armor
c.poly([(18, 52), (26, 52), (24, 58), (16, 56)], outfit_dark, fill=True)
c.poly([(38, 52), (46, 52), (48, 56), (40, 58)], outfit_dark, fill=True)

# Outfit details - trim
c.line(22, 52, 22, 63, leather)
c.line(42, 52, 42, 63, leather)

# Collar
c.poly([(26, 50), (38, 50), (38, 54), (26, 54)], leather, fill=True)
c.poly([(28, 50), (36, 50), (36, 52), (28, 52)], outfit_highlight, fill=True)

# ============ BOW (on back, visible over shoulder) ============
# Bow curve
c.path("M 12 45 Q 8 52 12 60 Q 16 52 12 45", bow_wood, fill=False)
c.path("M 14 46 Q 11 52 14 59", bow_dark, fill=False)

# Bow grip
c.poly([(12, 50), (16, 50), (16, 54), (12, 54)], leather, fill=True)
c.poly([(13, 51), (15, 51), (15, 53), (13, 53)], leather_dark, fill=True)

# ============ ARROWS (in quiver on back) ============
# Arrow shafts visible
c.line(50, 48, 50, 63, arrow_shaft)
c.line(52, 48, 52, 63, arrow_shaft)
c.line(54, 48, 54, 63, arrow_shaft)

# Arrow tips
c.set(50, 47, arrow_tip)
c.set(52, 47, arrow_tip)
c.set(54, 47, arrow_tip)

# Fletching (feathers)
c.poly([(48, 60), (50, 58), (50, 62)], arrow_fletching, fill=True)
c.poly([(52, 60), (54, 58), (54, 62)], arrow_fletching, fill=True)
c.poly([(54, 60), (56, 58), (56, 62)], arrow_fletching, fill=True)

# Quiver strap
c.poly([(44, 54), (52, 54), (52, 63), (44, 63)], leather, fill=True)
c.poly([(46, 54), (50, 54), (50, 63), (46, 63)], leather_dark, fill=True)

# ============ HAIR (front layer - bangs and framing) ============
# Bangs across forehead
c.poly([
    (22, 16), (42, 16), (40, 22), (36, 20), (32, 22), (28, 20), (24, 22)
], hair_mid, fill=True)

# Side hair framing face
c.poly([(18, 18), (24, 18), (22, 35), (18, 32)], hair_dark, fill=True)
c.poly([(40, 18), (46, 18), (46, 32), (42, 35)], hair_dark, fill=True)

# Hair highlights on bangs
c.line(26, 17, 26, 20, hair_highlight)
c.line(32, 17, 32, 20, hair_highlight)
c.line(38, 17, 38, 20, hair_highlight)

# ============ FINAL DETAILS ============
# Outline key features
c.set(18, 18, outline)
c.set(46, 18, outline)
c.set(20, 46, outline)
c.set(44, 46, outline)

# Metal buckle on strap
c.set(46, 56, metal_light)
c.set(47, 56, metal_light)
c.set(46, 57, metal_dark)

# Add some depth to outfit
c.set(24, 60, outfit_dark)
c.set(40, 60, outfit_dark)

# Print stats to verify color count
print(c.stats_text())

# Submit the canvas
finish(c)
