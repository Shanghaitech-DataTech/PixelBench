from pixelbench_api import *

# 64x64 transparent pixel-art anatomical heart
c = new_canvas(64, 64, name="realistic_heart")

# Compact, deliberately limited palette: ink, oxblood shadows, warm muscle, and highlights.
ink = "#180a12"
outline = "#2a0d18"
deep = "#42101c"
shadow = "#5a1723"
maroon = "#741d2c"
red = "#922a38"
mid = "#aa3540"
coral = "#c44c4c"
light = "#df7060"
shine = "#f39b78"
plum = "#351225"
vein = "#50152b"
blue = "#233348"
blue2 = "#34516a"
gold = "#b7654f"

# A few blocky background glints make the isolated form sit in the frame without a backdrop.
c.rect(7, 28, 2, 8, plum)
c.rect(53, 25, 2, 9, plum)
c.rect(9, 40, 2, 4, plum)
c.set(56, 39, plum)

# Main outer silhouette, with the notch, atria, broad ventricles, and pointed apex.
c.path("M 13 25 C 11 21 14 17 18 16 C 21 15 24 17 27 20 C 28 15 31 12 35 13 C 38 13 40 16 41 19 C 44 16 48 16 51 19 C 55 23 54 29 52 34 C 50 40 46 45 43 50 C 40 55 36 60 32 63 C 30 65 27 61 24 58 C 19 53 15 47 12 41 C 9 35 8 29 13 25 Z", ink)
# inner muscle base, leaving a thick pixel outline
c.path("M 15 26 C 14 22 17 19 20 19 C 24 19 27 23 29 26 C 29 20 31 16 35 16 C 39 16 41 20 41 24 C 44 19 48 19 50 22 C 53 26 50 34 47 40 C 44 48 38 57 31 61 C 25 56 19 50 16 43 C 12 35 11 29 15 26 Z", maroon)

# Right atrium: darker, cupped shadow plane.
c.path("M 39 23 C 42 19 48 19 50 22 C 52 26 50 33 46 37 C 43 39 40 37 38 33 Z", shadow)
c.path("M 43 23 C 46 21 49 23 49 26 C 49 30 47 33 44 35 C 43 31 42 27 43 23 Z", red)
c.rect(48, 24, 2, 5, coral)
c.set(46, 23, light)
# Right ventricle wall and groove.
c.path("M 37 32 C 41 34 45 37 46 41 C 44 47 39 54 33 59 C 34 52 33 44 30 38 C 32 34 34 32 37 32 Z", red)
c.path("M 39 36 C 42 38 43 41 42 44 C 40 49 36 53 33 56 C 35 48 34 41 32 37 Z", coral)
c.line(41, 39, 36, 53, shadow)
c.line(42, 40, 37, 50, light)

# Left ventricle: large mass with a deep interventricular groove.
c.path("M 16 29 C 20 25 27 26 30 31 C 34 38 34 49 31 59 C 28 58 24 53 20 48 C 16 42 13 35 16 29 Z", red)
c.path("M 18 31 C 22 28 26 29 28 33 C 31 40 30 49 29 54 C 25 51 20 45 18 40 C 16 36 16 33 18 31 Z", mid)
# left ventricle warm ridge and fine muscle striations
c.path("M 20 31 C 23 30 26 32 27 36 C 29 42 28 48 28 51 C 25 47 22 42 20 37 Z", coral)
c.line(20, 34, 25, 46, light)
c.line(23, 33, 27, 43, red)
c.line(18, 37, 24, 49, shadow)
c.line(27, 36, 29, 49, shine)

# Central interventricular sulcus, descending toward the apex.
c.path("M 28 26 C 30 29 32 33 33 38 C 35 46 33 55 31 61 L 28 58 C 30 50 30 42 28 35 C 27 31 26 29 28 26 Z", deep)
c.line(30, 31, 32, 48, shadow)
c.line(31, 39, 31, 54, coral)
c.set(31, 56, light)

# Left atrium behind the great vessels.
c.path("M 15 24 C 16 19 21 18 25 21 C 27 23 28 27 27 30 C 23 28 19 28 15 30 C 13 28 13 26 15 24 Z", shadow)
c.path("M 17 23 C 19 20 22 21 24 23 C 25 24 25 26 24 27 C 21 25 19 25 16 26 Z", coral)
c.set(19, 22, light)
c.rect(14, 27, 3, 3, deep)

# Great vessels behind the top of the heart, outlined first.
c.path("M 28 21 L 27 12 L 24 9 L 24 5 L 29 3 L 34 4 L 36 8 L 36 15 L 40 13 L 45 13 L 48 16 L 47 22 L 42 24 L 37 22 L 34 25 Z", ink)
# ascending aorta and arch
c.path("M 30 21 L 30 12 L 27 9 L 27 6 L 31 5 L 34 7 L 34 17 L 38 18 L 40 16 L 44 16 L 46 18 L 45 21 L 41 22 L 36 20 L 33 24 Z", red)
c.rect(29, 7, 4, 8, mid)
c.rect(30, 6, 2, 6, coral)
c.rect(38, 17, 7, 3, coral)
c.set(43, 17, light)
# dark opening of aorta
c.rect(27, 4, 5, 2, deep)
c.rect(28, 5, 3, 1, shadow)
# pulmonary trunk crossing in front, with fork
c.path("M 33 25 L 34 16 L 37 12 L 40 12 L 42 15 L 39 18 L 38 26 Z", outline)
c.path("M 35 24 L 36 17 L 38 14 L 40 14 L 38 18 L 37 25 Z", blue2)
c.rect(37, 13, 3, 3, blue)
c.set(39, 14, light)
# superior vena cava at viewer-right
c.path("M 45 5 L 51 5 L 52 8 L 51 20 L 48 23 L 45 20 Z", ink)
c.path("M 47 6 L 50 7 L 50 19 L 48 21 L 47 19 Z", blue2)
c.rect(47, 7, 2, 7, blue)
c.set(48, 8, coral)

# Thin venous channels across the surface.
c.line(45, 27, 48, 30, vein)
c.line(44, 29, 47, 33, deep)
c.line(18, 27, 15, 32, vein)
c.line(20, 28, 16, 35, shadow)
c.line(23, 26, 20, 30, light)

# Surface highlights and pixel clusters for wet, dimensional muscle.
c.rect(17, 30, 2, 3, shine)
c.set(19, 29, light)
c.rect(21, 28, 2, 2, coral)
c.rect(15, 34, 2, 3, coral)
c.set(16, 38, light)
c.rect(24, 51, 2, 2, coral)
c.set(26, 54, shine)
c.rect(35, 29, 2, 3, coral)
c.set(38, 28, light)
c.rect(41, 34, 2, 2, light)
c.set(43, 36, shine)
c.rect(35, 48, 2, 3, mid)
c.set(34, 53, coral)
# restrained deepest creases
c.rect(12, 29, 2, 5, deep)
c.rect(14, 38, 2, 4, deep)
c.rect(18, 45, 2, 3, shadow)
c.rect(42, 43, 2, 4, deep)
c.rect(39, 51, 2, 3, shadow)
c.set(31, 60, ink)

# Delicate coronary vessels: broken, dark-red branching lines laid over the muscle.
c.line(26, 24, 22, 27, vein)
c.line(22, 27, 19, 33, vein)
c.set(18, 34, deep)
c.line(29, 28, 25, 31, shadow)
c.line(25, 31, 23, 36, shadow)
c.line(23, 36, 21, 40, vein)
c.line(37, 27, 40, 30, vein)
c.line(40, 30, 43, 34, vein)
c.line(43, 34, 45, 38, deep)
c.line(36, 31, 38, 36, shadow)
c.line(38, 36, 39, 40, vein)
# Small, offset striations suggest curved fiber direction.
c.line(19, 42, 23, 48, shadow)
c.line(21, 44, 25, 50, coral)
c.line(25, 52, 28, 56, mid)
c.line(35, 42, 37, 47, coral)
c.line(36, 45, 39, 49, shadow)
c.line(33, 52, 35, 55, light)
# Aortic branch tips and soft transition pixels at the root.
c.rect(32, 10, 2, 5, red)
c.set(33, 15, coral)
c.rect(40, 20, 3, 2, mid)
c.set(42, 21, light)
c.set(35, 23, shadow)
c.set(36, 24, coral)

# A few crisp edge pixels to keep the silhouette intentionally pixel-built.
c.set(11, 27, outline); c.set(10, 30, outline); c.set(12, 39, outline)
c.set(15, 45, outline); c.set(21, 53, outline); c.set(26, 59, outline)
c.set(34, 60, outline); c.set(44, 47, outline); c.set(49, 38, outline)
c.set(52, 29, outline); c.set(50, 21, outline)

view(c, size=512, margin=0)
finish(c)
