from pixelbench_api import new_canvas, finish

# Create 64x64 canvas for the mad cyborg scientist portrait
c = new_canvas(64, 64, background=None, name="cyborg_scientist")

# Define color palette - carefully planned for ~86 colors max
# Background (dark gradient)
bg_dark = c.color("#0a0a12", "bg_dark")
bg_mid = c.color("#151525", "bg_mid")

# Skin tones (left human side)
skin_base = c.color("#d4a574", "skin_base")
skin_shadow = c.color("#a67c52", "skin_shadow")
skin_dark = c.color("#7a5738", "skin_dark")
skin_highlight = c.color("#e8c49a", "skin_highlight")
skin_blush = c.color("#c9896a", "skin_blush")

# Metal/robotic colors (right side)
metal_base = c.color("#6b7280", "metal_base")
metal_dark = c.color("#374151", "metal_dark")
metal_light = c.color("#9ca3af", "metal_light")
metal_highlight = c.color("#d1d5db", "metal_highlight")
metal_rust = c.color("#8b5a3c", "metal_rust")
metal_blue = c.color("#4a6fa5", "metal_blue")

# Glowing cybernetic eye
glow_core = c.color("#ffffff", "glow_core")
glow_inner = c.color("#00ffff", "glow_inner")
glow_outer = c.color("#0088aa", "glow_outer")
glow_halo = c.color("#004455", "glow_halo")

# Normal human eye
eye_white = c.color("#f0f0f0", "eye_white")
eye_iris = c.color("#4a6fa5", "eye_iris")
eye_pupil = c.color("#1a1a1a", "eye_pupil")

# Messy white hair
hair_white = c.color("#f5f5f5", "hair_white")
hair_gray = c.color("#c0c0c0", "hair_gray")
hair_shadow = c.color("#888888", "hair_shadow")
hair_dark = c.color("#555555", "hair_dark")

# Maniacal grin
teeth = c.color("#fafafa", "teeth")
teeth_shadow = c.color("#d0d0d0", "teeth_shadow")
gums = c.color("#c96a6a", "gums")
mouth_dark = c.color("#2a1a1a", "mouth_dark")

# Dirty lab coat
coat_white = c.color("#e8e8e0", "coat_white")
coat_gray = c.color("#b8b8b0", "coat_gray")
coat_shadow = c.color("#888880", "coat_shadow")
coat_stain = c.color("#9a8b6a", "coat_stain")

# Leather apron
leather_dark = c.color("#4a3525", "leather_dark")
leather_mid = c.color("#6b4a35", "leather_mid")
leather_light = c.color("#8b6545", "leather_light")
leather_highlight = c.color("#ab8565", "leather_highlight")

# Tool belt
belt_dark = c.color("#3a2a1a", "belt_dark")
belt_mid = c.color("#5a4030", "belt_mid")
tool_metal = c.color("#7a8a9a", "tool_metal")

# Cables and wires
cable_red = c.color("#aa3333", "cable_red")
cable_blue = c.color("#3355aa", "cable_blue")
cable_yellow = c.color("#aaaa33", "cable_yellow")
cable_black = c.color("#2a2a2a", "cable_black")

# Electrode plugs
plug_metal = c.color("#aaaaaa", "plug_metal")
plug_gold = c.color("#ccaa44", "plug_gold")
plug_wire = c.color("#666666", "plug_wire")

# Neck shadow
neck_shadow = c.color("#8a6a5a", "neck_shadow")

# Shoulder/clothing shadows
shoulder_shadow = c.color("#2a2a3a", "shoulder_shadow")

# ===== DRAWING THE PORTRAIT =====

# Background gradient (dark vignette)
c.rect(0, 0, 64, 64, bg_dark)
# Darker corners
for i in range(8):
    alpha_val = int(200 - i * 20)
    c.rect(i, i, 64-i*2, 64-i*2, bg_mid)

# ===== NECK AND SHOULDERS =====
# Neck area (bottom center of head area)
c.rect(24, 42, 16, 12, neck_shadow)

# Left shoulder (human side - lab coat)
c.poly([(10, 50), (30, 52), (28, 63), (5, 63), (5, 52)], coat_shadow, fill=True)
c.poly([(12, 50), (28, 52), (26, 63), (8, 63), (8, 52)], coat_gray, fill=True)

# Right shoulder (robotic arm side - exposed metal)
c.poly([(34, 50), (54, 50), (59, 63), (36, 63)], metal_dark, fill=True)
c.poly([(36, 50), (52, 50), (56, 63), (38, 63)], metal_base, fill=True)

# ===== ROBOTIC ARM (right side, exposed) =====
# Upper arm
c.poly([(38, 52), (52, 52), (54, 60), (36, 60)], metal_base, fill=True)
c.line(40, 52, 40, 60, metal_dark)
c.line(50, 52, 50, 60, metal_light)

# Forearm with cables
c.rect(36, 58, 20, 6, metal_dark)
c.rect(38, 58, 16, 6, metal_base)

# Cables coming from arm
c.line(42, 60, 42, 63, cable_red)
c.line(46, 60, 46, 63, cable_blue)
c.line(50, 60, 50, 63, cable_yellow)

# Prosthetic hand (partial view)
c.poly([(38, 62), (48, 62), (46, 63), (40, 63)], metal_light, fill=True)

# ===== LAB COAT (left side) =====
c.poly([(8, 50), (32, 50), (32, 63), (8, 63)], coat_white, fill=True)
# Coat folds
c.line(15, 50, 15, 63, coat_gray)
c.line(25, 50, 24, 63, coat_shadow)
# Stains on coat
c.set(12, 55, coat_stain)
c.set(13, 56, coat_stain)
c.set(11, 58, coat_stain)
c.set(20, 53, coat_stain)
c.set(19, 57, coat_stain)

# ===== LEATHER APRON =====
c.poly([(18, 50), (46, 50), (44, 63), (20, 63)], leather_dark, fill=True)
c.poly([(20, 50), (44, 50), (42, 63), (22, 63)], leather_mid, fill=True)
# Apron straps
c.rect(22, 50, 4, 13, leather_dark)
c.rect(38, 50, 4, 13, leather_dark)
# Apron highlight
c.line(25, 52, 25, 62, leather_light)
c.line(40, 52, 40, 62, leather_highlight)

# ===== TOOL BELT =====
c.rect(16, 58, 32, 5, belt_dark)
c.rect(18, 58, 28, 3, belt_mid)
# Tools on belt
c.rect(22, 59, 3, 4, tool_metal)
c.rect(30, 59, 3, 4, tool_metal)
c.rect(38, 59, 3, 4, tool_metal)

# ===== HEAD SHAPE =====
# Basic head oval - split down the middle at x=32
# Left side (human) - organic curve
c.poly([(20, 12), (32, 10), (32, 48), (20, 46), (16, 42), (14, 32), (14, 22), (16, 14)], skin_base, fill=True)
# Right side (robotic) - angular mechanical
c.poly([(32, 10), (44, 12), (48, 16), (50, 24), (50, 36), (48, 44), (44, 48), (32, 48)], metal_base, fill=True)

# ===== HAIR (messy white, flowing) =====
# Top of head hair
c.poly([(14, 14), (20, 8), (32, 6), (44, 8), (50, 14), (48, 18), (44, 14), (32, 12), (20, 14), (16, 18)], hair_white, fill=True)
# Messy strands left side
c.poly([(12, 16), (16, 12), (18, 16), (14, 20)], hair_gray, fill=True)
c.poly([(10, 20), (14, 18), (15, 24), (11, 24)], hair_shadow, fill=True)
# Messy strands right side (over robot head)
c.poly([(48, 14), (52, 16), (54, 22), (50, 24), (48, 20)], hair_gray, fill=True)
c.poly([(50, 12), (54, 14), (56, 20), (52, 22), (50, 18)], hair_white, fill=True)
# Strands hanging down
c.line(14, 20, 12, 28, hair_shadow)
c.line(18, 18, 16, 30, hair_gray)
c.line(48, 18, 50, 26, hair_shadow)

# ===== HUMAN FACE (left side) =====
# Skin shading
c.poly([(18, 16), (30, 16), (30, 44), (22, 44), (18, 36), (16, 26), (16, 20)], skin_base, fill=True)
# Shadow under cheekbone
c.poly([(18, 28), (26, 28), (26, 34), (20, 34)], skin_shadow, fill=True)
# Highlight on forehead
c.poly([(20, 16), (28, 16), (28, 20), (22, 20)], skin_highlight, fill=True)
# Nose (human side)
c.poly([(26, 24), (30, 26), (28, 30), (26, 28)], skin_shadow, fill=True)
c.set(28, 28, skin_highlight)

# ===== NORMAL HUMAN EYE (left) =====
# Eye white
c.poly([(20, 22), (26, 22), (26, 26), (20, 26)], eye_white, fill=True)
# Iris
c.circle(23, 24, 2, eye_iris, fill=True)
# Pupil
c.set(23, 24, eye_pupil)
# Eye highlight
c.set(22, 23, glow_core)
# Eyebrow (furrowed, mad expression)
c.poly([(19, 20), (26, 19), (26, 21), (19, 22)], hair_shadow, fill=True)

# ===== MANIACAL GRIN =====
# Mouth opening
c.poly([(20, 36), (30, 36), (32, 40), (28, 42), (22, 42), (18, 40)], mouth_dark, fill=True)
# Upper teeth
c.rect(21, 36, 2, 3, teeth)
c.rect(23, 36, 2, 3, teeth)
c.rect(25, 36, 2, 3, teeth)
c.rect(27, 36, 2, 3, teeth)
# Tooth shadows
c.set(21, 38, teeth_shadow)
c.set(23, 38, teeth_shadow)
c.set(25, 38, teeth_shadow)
c.set(27, 38, teeth_shadow)
# Lower teeth (partial)
c.rect(22, 40, 2, 2, teeth)
c.rect(25, 40, 2, 2, teeth)
# Gums
c.line(21, 36, 29, 36, gums)

# ===== ROBOTIC HEAD (right side) =====
# Metal plating
c.poly([(34, 14), (46, 16), (48, 44), (34, 44)], metal_base, fill=True)
# Panel lines
c.line(36, 16, 36, 44, metal_dark)
c.line(42, 16, 42, 44, metal_dark)
c.line(34, 24, 48, 24, metal_dark)
c.line(34, 36, 48, 36, metal_dark)

# Metal highlights
c.line(38, 16, 38, 24, metal_light)
c.line(44, 16, 44, 24, metal_light)
c.line(46, 30, 46, 44, metal_highlight)

# Rust spots
c.set(40, 30, metal_rust)
c.set(41, 31, metal_rust)
c.set(45, 38, metal_rust)
c.set(38, 40, metal_rust)

# ===== GLOWING CYBERNETIC EYE (right) =====
# Eye socket (dark)
c.poly([(36, 22), (46, 22), (46, 28), (36, 28)], metal_dark, fill=True)
# Glow halo
c.ellipse(41, 25, 6, 4, glow_halo, fill=True)
# Outer glow
c.ellipse(41, 25, 5, 3, glow_outer, fill=True)
# Inner glow (cyan)
c.ellipse(41, 25, 3, 2, glow_inner, fill=True)
# Core (bright white)
c.set(41, 25, glow_core)
c.set(40, 25, glow_inner)
c.set(42, 25, glow_inner)
# Scan line effect
c.line(37, 25, 45, 25, glow_outer)

# ===== BRAIN ELECTRODE PLUGS =====
# Plugs on left side of head (human side, going into brain)
# Plug 1
c.set(16, 14, plug_metal)
c.set(15, 14, plug_gold)
c.line(12, 14, 15, 14, plug_wire)
# Plug 2
c.set(17, 18, plug_metal)
c.set(16, 18, plug_gold)
c.line(13, 18, 16, 18, plug_wire)
# Plug 3 (top)
c.set(22, 10, plug_metal)
c.set(21, 10, plug_gold)
c.line(21, 10, 21, 6, plug_wire)
# Plug 4 (back)
c.set(14, 24, plug_metal)
c.set(13, 24, plug_gold)
c.line(10, 24, 13, 24, plug_wire)

# Wires from plugs
c.line(12, 14, 10, 10, cable_black)
c.line(13, 18, 10, 16, cable_black)
c.line(21, 6, 22, 4, cable_black)
c.line(10, 24, 8, 26, cable_black)

# ===== ROBOTIC HEAD DETAILS =====
# Antenna/sensor on top right
c.line(46, 10, 46, 6, metal_dark)
c.set(46, 6, plug_metal)
c.set(46, 5, glow_outer)
# Small blinking light
c.set(46, 5, glow_inner)

# Vent grilles on robot side
for i in range(4):
    c.line(38 + i*2, 32, 38 + i*2, 34, metal_dark)

# Exposed wiring at neck junction
c.line(32, 44, 34, 46, cable_red)
c.line(33, 44, 35, 47, cable_blue)
c.line(32, 46, 33, 48, cable_yellow)

# ===== FINAL DETAILS =====
# Strong lighting - add highlights on left side (light source from left)
c.set(18, 24, skin_highlight)
c.set(20, 20, skin_highlight)
c.set(28, 22, skin_highlight)

# Shadow on right side of face (robot side in shadow)
c.poly([(32, 20), (38, 20), (38, 30), (32, 30)], metal_dark, fill=True)

# Sweat/dirt on human face (mad scientist look)
c.set(24, 32, skin_shadow)
c.set(26, 30, skin_shadow)

# More cable details on robotic arm
c.line(44, 54, 48, 56, cable_red)
c.line(45, 56, 49, 58, cable_blue)

# Check stats
print(c.stats_text())

# Submit the canvas
finish(c)
