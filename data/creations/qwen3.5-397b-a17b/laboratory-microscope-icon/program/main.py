from pixelbench_api import *

# Create a 32x32 canvas with transparent background
c = new_canvas(32, 32, background=None, name="microscope")

# Define colors - limited palette for microscope
dark_metal = c.color((35, 35, 42), "dark_metal")
med_metal = c.color((75, 75, 85), "med_metal")
light_metal = c.color((130, 130, 145), "light_metal")
silver = c.color((175, 175, 185), "silver")
highlight = c.color((210, 210, 220), "highlight")
shadow = c.color((50, 50, 58), "shadow")
lens_glass = c.color((100, 140, 180), "lens_glass")
knob_accent = c.color((160, 60, 60), "knob_accent")

# === BASE (bottom part) ===
# Main base platform - trapezoid for 3/4 view
c.poly([
    (5, 28), (27, 28), (28, 26), (28, 24),
    (26, 22), (6, 22), (4, 24), (4, 26)
], dark_metal, fill=True)

# Base top surface (lighter)
c.poly([
    (5, 22), (26, 22), (28, 24), (26, 26),
    (6, 26), (4, 24)
], med_metal, fill=True)

# Base highlight edge
c.line(5, 22, 26, 22, light_metal)
c.line(4, 24, 5, 26, light_metal)

# === ARM/STAND (connects base to body) ===
# Back arm (darker, in shadow)
c.poly([
    (8, 22), (12, 22), (11, 14), (7, 14)
], shadow, fill=True)

# Front arm (lighter)
c.poly([
    (10, 22), (14, 22), (13, 14), (9, 14)
], med_metal, fill=True)

# Arm highlight
c.line(10, 22, 10, 14, light_metal)

# === STAGE (platform for specimens) ===
# Stage platform - flat rectangle in 3/4 view
c.poly([
    (8, 16), (24, 16), (26, 14), (26, 12),
    (24, 10), (8, 10), (6, 12), (6, 14)
], med_metal, fill=True)

# Stage top surface
c.poly([
    (8, 10), (24, 10), (26, 12), (24, 14),
    (8, 14), (6, 12)
], light_metal, fill=True)

# Stage aperture (hole in center)
c.poly([
    (14, 12), (18, 12), (19, 13), (18, 14),
    (14, 14), (13, 13)
], dark_metal, fill=True)

# Stage clips (hold specimen)
c.rect(10, 11, 2, 1, dark_metal)
c.rect(20, 11, 2, 1, dark_metal)

# === OBJECTIVE LENSES (below stage) ===
# Revolving nosepiece
c.poly([
    (12, 15), (20, 15), (21, 17), (19, 19),
    (13, 19), (11, 17)
], dark_metal, fill=True)

# Main objective lens (center, pointing down)
c.poly([
    (15, 19), (17, 19), (17, 22), (15, 22)
], silver, fill=True)
# Lens glass
c.set(16, 21, lens_glass)

# Side objectives (angled, showing 3/4 view)
c.poly([
    (13, 18), (15, 18), (15, 21), (13, 20)
], med_metal, fill=True)
c.set(14, 20, lens_glass)

c.poly([
    (17, 18), (19, 18), (19, 21), (17, 20)
], med_metal, fill=True)
c.set(18, 20, lens_glass)

# === BODY TUBE (main vertical structure) ===
# Main tube body
c.poly([
    (11, 6), (19, 6), (21, 8), (21, 16),
    (19, 18), (11, 18), (9, 16), (9, 8)
], med_metal, fill=True)

# Tube front face (lighter)
c.poly([
    (11, 6), (19, 6), (21, 8), (21, 16),
    (19, 18), (11, 18)
], light_metal, fill=True)

# Tube highlight stripe
c.line(12, 7, 12, 17, highlight)
c.line(13, 7, 13, 17, silver)

# === FOCUS KNOBS (on the side) ===
# Coarse focus knob (larger, lower)
c.ellipse(24, 13, 4, 5, dark_metal, fill=True)
c.ellipse(24, 13, 3, 4, med_metal, fill=True)
c.set(23, 12, highlight)

# Fine focus knob (smaller, upper)
c.ellipse(24, 9, 3, 3, dark_metal, fill=True)
c.ellipse(24, 9, 2, 2, knob_accent, fill=True)
c.set(23, 8, highlight)

# === EYEPIECE (top) ===
# Eyepiece tube
c.poly([
    (13, 2), (17, 2), (18, 3), (18, 7),
    (17, 8), (13, 8), (12, 7), (12, 3)
], dark_metal, fill=True)

# Eyepiece top (where you look)
c.ellipse(15, 2, 3, 2, silver, fill=True)
c.ellipse(15, 2, 2, 1, highlight, fill=True)

# Eyepiece lens (dark circle inside)
c.ellipse(15, 3, 2, 1, dark_metal, fill=True)
c.set(15, 3, lens_glass)

# === FINAL DETAILS ===
# Add some shading to base
c.line(6, 26, 26, 26, shadow)
c.line(5, 25, 5, 27, shadow)

# Condenser below stage (optional detail)
c.poly([
    (14, 15), (18, 15), (18, 17), (16, 18), (14, 17)
], dark_metal, fill=True)

# Print stats to verify color count
print(c.stats_text())

# Submit the canvas
finish(c)
