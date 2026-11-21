from pixelbench_api import *

# Create canvas
c = new_canvas(256, 256, name="east_hero")

# Define color palette
# Background - misty mountains
bg_light = c.color("#e8ecf0", "bg_light")
bg_mid = c.color("#c5ccd4", "bg_mid")
bg_dark = c.color("#9aa3ad", "bg_dark")
mist1 = c.color("#d8dde4", "mist1")
mist2 = c.color("#b0b8c0", "mist2")

# Mountains
mount_far = c.color("#6b7580", "mount_far")
mount_mid = c.color("#4a525c", "mount_mid")
mount_near = c.color("#2d343c", "mount_near")

# Bamboo hat (douli)
hat_light = c.color("#d4b896", "hat_light")
hat_mid = c.color("#b89968", "hat_mid")
hat_dark = c.color("#8b6f47", "hat_dark")
hat_shadow = c.color("#5c4a2f", "hat_shadow")
hat_highlight = c.color("#e8d4b8", "hat_highlight")

# Hair
hair_dark = c.color("#1a1510", "hair_dark")
hair_mid = c.color("#3d2f22", "hair_mid")
hair_highlight = c.color("#5c4a38", "hair_highlight")

# Skin
skin_light = c.color("#f5d5b8", "skin_light")
skin_mid = c.color("#d4a882", "skin_mid")
skin_shadow = c.color("#a67c52", "skin_shadow")
skin_dark = c.color("#7d5a3a", "skin_dark")

# Robe (dark flowing)
robe_dark = c.color("#1c1a24", "robe_dark")
robe_mid = c.color("#2d2a38", "robe_mid")
robe_light = c.color("#4a4558", "robe_light")
robe_highlight = c.color("#6b6378", "robe_highlight")
robe_fold = c.color("#0f0d14", "robe_fold")

# Sash
sash_dark = c.color("#8b2f2f", "sash_dark")
sash_mid = c.color("#b84545", "sash_mid")
sash_light = c.color("#d46060", "sash_light")
sash_highlight = c.color("#e88080", "sash_highlight")

# Sword (jian)
sword_steel = c.color("#c0c8d0", "sword_steel")
sword_light = c.color("#e0e8f0", "sword_light")
sword_dark = c.color("#808890", "sword_dark")
sword_shadow = c.color("#505860", "sword_shadow")
sword_guard = c.color("#b89968", "sword_guard")

# Outline
outline = c.color("#0a0810", "outline")

# ============ BACKGROUND: Misty Mountains ============

# Fill background with gradient
for y in range(256):
    if y < 80:
        col = bg_light
    elif y < 140:
        col = bg_mid
    else:
        col = bg_dark
    c.rect(0, y, 256, 1, col)

# Far mountains (back layer)
c.poly([(0, 120), (40, 90), (80, 110), (120, 70), (180, 100), (220, 80), (255, 95), (255, 160), (0, 160)], mount_far, fill=True)

# Mid mountains
c.poly([(0, 150), (50, 120), (100, 140), (150, 100), (200, 130), (255, 110), (255, 180), (0, 180)], mount_mid, fill=True)

# Near mountains
c.poly([(0, 180), (30, 160), (80, 170), (130, 150), (180, 165), (230, 155), (255, 170), (255, 220), (0, 220)], mount_near, fill=True)

# Mist layers
c.poly([(0, 140), (60, 130), (120, 145), (180, 135), (255, 150), (255, 155), (0, 155)], mist1, fill=True)
c.poly([(0, 165), (50, 155), (100, 170), (150, 160), (200, 175), (255, 165), (255, 172), (0, 172)], mist2, fill=True)

# ============ CHARACTER: Position and Stance ============
# Character centered, three-quarter view, heroic stance
# Body center around x=128, y=140 (standing on ground)

# ============ ROBE (drawn first, base layer) ============

# Main robe body - flowing dark fabric
# Left side of robe (character's right)
robe_left_path = [(95, 140), (85, 160), (80, 190), (75, 230), (80, 255), (110, 255), (115, 220), (110, 180), (105, 150)]
c.poly(robe_left_path, robe_dark, fill=True)

# Right side of robe (character's left) - more visible in 3/4 view
robe_right_path = [(155, 140), (175, 160), (190, 200), (200, 240), (195, 255), (145, 255), (140, 220), (145, 180), (150, 150)]
c.poly(robe_right_path, robe_dark, fill=True)

# Center robe panel
c.poly([(110, 140), (115, 180), (120, 220), (125, 255), (135, 255), (140, 220), (145, 180), (150, 145)], robe_mid, fill=True)

# Robe folds and details (left)
c.poly([(85, 160), (90, 190), (88, 220), (82, 240)], robe_fold, fill=True)
c.poly([(95, 170), (100, 200), (98, 230)], robe_light, fill=True)

# Robe folds and details (right)
c.poly([(175, 160), (185, 190), (192, 220), (198, 245)], robe_fold, fill=True)
c.poly([(165, 170), (175, 200), (182, 230)], robe_light, fill=True)

# Flowing fabric edges
c.poly([(75, 230), (80, 250), (78, 255), (72, 240)], robe_mid, fill=True)
c.poly([(200, 240), (205, 250), (202, 255), (196, 245)], robe_mid, fill=True)

# ============ SASH/BELT ============

# Main sash around waist
c.poly([(95, 138), (110, 135), (128, 133), (146, 135), (160, 138), (160, 150), (145, 148), (128, 146), (110, 148), (95, 150)], sash_dark, fill=True)

# Sash knot/bow on left side
c.poly([(85, 135), (95, 130), (100, 138), (92, 145), (82, 142)], sash_mid, fill=True)
c.poly([(80, 138), (88, 135), (92, 142), (85, 148)], sash_light, fill=True)

# Sash flowing ends
c.poly([(85, 145), (80, 160), (75, 180), (78, 185), (85, 170), (88, 150)], sash_mid, fill=True)
c.poly([(78, 165), (73, 175), (76, 182), (82, 172)], sash_highlight, fill=True)

# ============ BODY/TORSO ============

# Upper torso under robe
c.poly([(105, 110), (115, 115), (128, 118), (141, 115), (151, 110), (151, 138), (145, 140), (128, 142), (111, 140), (105, 138)], robe_dark, fill=True)

# Chest highlight
c.poly([(115, 115), (128, 120), (141, 115), (140, 125), (128, 130), (116, 125)], robe_light, fill=True)

# ============ SHOULDERS ============

# Left shoulder
c.poly([(95, 105), (110, 100), (115, 110), (105, 115), (92, 112)], robe_mid, fill=True)

# Right shoulder
c.poly([(145, 100), (161, 105), (164, 112), (151, 115), (141, 110)], robe_mid, fill=True)

# ============ NECK ============

c.rect(120, 95, 16, 18, skin_mid)
c.rect(122, 95, 12, 18, skin_light)

# ============ HEAD ============

# Face shape (three-quarter view, lower half visible)
face_path = [(112, 85), (120, 80), (136, 80), (144, 85), (146, 95), (144, 108), (138, 118), (128, 122), (118, 118), (112, 108), (110, 95)]
c.poly(face_path, skin_light, fill=True)

# Face shadow (right side in 3/4 view)
c.poly([(136, 80), (144, 85), (146, 95), (144, 108), (140, 105), (138, 95), (136, 88)], skin_shadow, fill=True)

# Jaw line shadow
c.poly([(118, 118), (128, 122), (135, 118), (132, 110), (122, 112)], skin_dark, fill=True)

# Nose (side view)
c.poly([(142, 92), (148, 95), (146, 100), (142, 98)], skin_shadow, fill=True)

# Mouth
c.line(138, 108, 144, 107, skin_dark)

# Chin
c.poly([(125, 118), (132, 122), (138, 118)], skin_dark, fill=True)

# ============ HAIR ============

# Main hair mass (loose, flowing)
# Back of head
c.poly([(108, 75), (115, 65), (128, 60), (141, 65), (148, 75), (150, 90), (148, 105), (144, 95), (142, 80), (136, 72), (128, 70), (120, 72), (114, 80), (112, 95), (108, 90)], hair_dark, fill=True)

# Flowing hair left side
c.poly([(108, 75), (100, 85), (95, 100), (92, 120), (95, 140), (100, 155), (105, 145), (102, 120), (105, 100), (108, 85)], hair_mid, fill=True)

# Flowing hair right side
c.poly([(148, 75), (156, 85), (162, 100), (168, 120), (172, 145), (175, 170), (170, 165), (165, 140), (160, 115), (155, 95), (150, 80)], hair_mid, fill=True)

# Hair highlights
c.poly([(115, 70), (128, 65), (141, 70), (138, 75), (128, 73), (118, 75)], hair_highlight, fill=True)
c.poly([(100, 95), (105, 110), (102, 125)], hair_highlight, fill=True)
c.poly([(156, 95), (162, 110), (168, 130)], hair_highlight, fill=True)

# Stray hair strands
c.line(95, 140, 90, 160, hair_dark)
c.line(172, 145, 178, 165, hair_dark)
c.line(92, 120, 85, 135, hair_mid)
c.line(168, 120, 175, 135, hair_mid)

# ============ BAMBOO HAT (DOULI) ============

# Hat brim - wide conical shape, tilted down
# Main brim (ellipse-like shape in perspective)
hat_brim_path = [(80, 78), (95, 72), (115, 68), (128, 66), (141, 68), (161, 72), (176, 78), (178, 85), (165, 82), (145, 78), (128, 76), (111, 78), (91, 82), (78, 85)]
c.poly(hat_brim_path, hat_mid, fill=True)

# Hat brim highlight (top edge)
c.poly([(80, 78), (95, 72), (115, 68), (128, 66), (141, 68), (161, 72), (176, 78), (174, 82), (160, 78), (141, 74), (128, 72), (115, 74), (96, 78), (82, 82)], hat_light, fill=True)

# Hat brim shadow (underside)
c.poly([(82, 85), (95, 82), (115, 78), (128, 76), (141, 78), (161, 82), (174, 85), (176, 90), (162, 88), (142, 84), (128, 82), (114, 84), (94, 88), (80, 90)], hat_shadow, fill=True)

# Hat crown (conical top)
c.poly([(115, 68), (128, 50), (141, 68), (138, 72), (128, 60), (118, 72)], hat_light, fill=True)

# Hat crown shadow
c.poly([(128, 50), (141, 68), (138, 72), (130, 58)], hat_dark, fill=True)

# Hat band/decoration
c.poly([(95, 75), (115, 71), (128, 69), (141, 71), (161, 75), (161, 78), (141, 74), (128, 72), (115, 74), (95, 78)], hat_dark, fill=True)

# Hat shadow on face (covers upper half)
c.poly([(108, 82), (120, 78), (136, 78), (144, 82), (142, 88), (136, 85), (128, 84), (120, 85), (114, 88)], hat_shadow, fill=True)

# ============ ARMS ============

# Right arm (character's right, on viewer's left) - resting on sword
c.poly([(95, 112), (105, 115), (108, 135), (105, 155), (98, 160), (92, 145), (90, 125)], skin_mid, fill=True)
c.poly([(98, 135), (105, 140), (102, 155), (95, 150)], skin_light, fill=True)

# Left arm (character's left, on viewer's right) - at side
c.poly([(151, 115), (165, 118), (170, 135), (168, 155), (162, 160), (155, 145), (152, 125)], skin_mid, fill=True)
c.poly([(155, 135), (165, 140), (162, 155), (155, 150)], skin_light, fill=True)

# Sleeves (flowing from robe)
# Right sleeve
c.poly([(92, 112), (100, 110), (105, 125), (102, 145), (95, 155), (88, 140), (85, 120)], robe_mid, fill=True)
# Left sleeve
c.poly([(151, 115), (160, 113), (168, 128), (170, 150), (165, 162), (158, 148), (153, 128)], robe_mid, fill=True)

# ============ HANDS ============

# Right hand (on sword hilt)
c.poly([(102, 155), (110, 152), (115, 158), (112, 165), (105, 168), (100, 162)], skin_light, fill=True)
# Fingers on sword
c.poly([(110, 158), (118, 156), (120, 162), (115, 165), (112, 162)], skin_mid, fill=True)

# Left hand (at side, partially visible)
c.poly([(162, 160), (170, 158), (173, 165), (168, 170), (162, 168)], skin_light, fill=True)

# ============ JIAN SWORD ============

# Sword blade (straight, vertical, tip down)
# Main blade
c.poly([(118, 165), (122, 165), (125, 220), (122, 250), (118, 250), (115, 220)], sword_steel, fill=True)

# Blade highlight
c.poly([(120, 165), (122, 165), (124, 200), (122, 240), (120, 240), (118, 200)], sword_light, fill=True)

# Blade edge shadow
c.poly([(115, 220), (118, 220), (120, 250), (118, 250)], sword_shadow, fill=True)

# Sword guard (crossguard)
c.poly([(110, 162), (118, 160), (126, 160), (134, 162), (134, 168), (126, 170), (118, 170), (110, 168)], sword_guard, fill=True)

# Sword hilt (where hand rests)
c.poly([(115, 155), (120, 153), (125, 153), (130, 155), (130, 162), (125, 164), (120, 164), (115, 162)], sword_dark, fill=True)

# Sword pommel
c.poly([(118, 150), (122, 148), (126, 148), (130, 150), (128, 155), (122, 155)], sword_guard, fill=True)

# ============ DARK OUTLINE ============

# Outline around character (selective, not everywhere)

# Hat outline
c.line(80, 78, 95, 72, outline)
c.line(95, 72, 115, 68, outline)
c.line(115, 68, 128, 66, outline)
c.line(128, 66, 141, 68, outline)
c.line(141, 68, 161, 72, outline)
c.line(161, 72, 176, 78, outline)
c.line(176, 78, 178, 85, outline)

# Hair outline (flowing strands)
c.line(108, 75, 100, 85, outline)
c.line(100, 85, 95, 100, outline)
c.line(95, 100, 92, 120, outline)
c.line(148, 75, 156, 85, outline)
c.line(156, 85, 162, 100, outline)
c.line(162, 100, 168, 120, outline)

# Face outline (visible lower half)
c.line(144, 85, 146, 95, outline)
c.line(146, 95, 144, 108, outline)
c.line(144, 108, 138, 118, outline)
c.line(138, 118, 128, 122, outline)
c.line(128, 122, 118, 118, outline)
c.line(118, 118, 112, 108, outline)
c.line(112, 108, 110, 95, outline)

# Robe outline
c.line(95, 140, 85, 160, outline)
c.line(85, 160, 80, 190, outline)
c.line(80, 190, 75, 230, outline)
c.line(75, 230, 80, 255, outline)
c.line(155, 140, 175, 160, outline)
c.line(175, 160, 190, 200, outline)
c.line(190, 200, 200, 240, outline)
c.line(200, 240, 195, 255, outline)

# Sword outline
c.line(118, 165, 122, 165, outline)
c.line(122, 165, 125, 220, outline)
c.line(125, 220, 122, 250, outline)
c.line(118, 250, 115, 220, outline)
c.line(115, 220, 118, 165, outline)

# ============ ADDITIONAL DETAILS ============

# Robe fold lines
c.line(100, 170, 102, 220, robe_fold)
c.line(115, 175, 118, 230, robe_fold)
c.line(170, 175, 175, 225, robe_fold)
c.line(185, 180, 188, 235, robe_fold)

# Sash details
c.line(95, 140, 100, 145, sash_highlight)
c.line(150, 140, 155, 145, sash_highlight)

# More mist in foreground
c.poly([(0, 200), (50, 195), (100, 205), (150, 198), (200, 208), (255, 200), (255, 210), (0, 210)], mist1, fill=True)

# Ground hint
c.poly([(0, 245), (50, 240), (100, 245), (150, 242), (200, 248), (255, 245), (255, 255), (0, 255)], mount_near, fill=True)

print(c.stats_text())
print(c.matrix_text(region=(100, 50, 160, 130)))

finish(c)
