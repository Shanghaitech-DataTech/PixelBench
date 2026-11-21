from pixelbench_api import new_canvas, view, finish

# 64x64 anatomical heart study, transparent background.
c = new_canvas(64, 64, background=None, name="realistic-heart")

# Compact hand-picked palette.
outline = "#2a0d16"
deep = "#48101d"
shadow = "#681526"
dark_red = "#851b2b"
red = "#aa2534"
bright = "#ce3c48"
light = "#e76668"
pink = "#f28b86"
pale = "#ffc0ad"
maroon = "#5b1524"
vein = "#38445a"
vein_hi = "#66758c"
artery_dark = "#722031"
artery = "#b73743"
artery_hi = "#e26767"
fat_dark = "#a85e40"
fat = "#d88a58"
fat_hi = "#f2b879"

# Rear vessels: pulmonary artery and vena cava.
c.path("M20 21 C15 17 14 11 17 7 C19 4 23 5 24 8 L24 22 Z", outline)
c.path("M18 20 C16 15 16 10 18 7 C20 6 21 7 21 10 L22 24 Z", vein)
c.rect(18, 9, 2, 8, vein_hi)
c.set(20, 8, "#8c98a7")

c.path("M39 22 C43 16 48 14 55 16 L57 20 C49 20 46 23 43 27 Z", outline)
c.path("M40 23 C44 18 49 17 55 18 L55 20 C49 20 46 23 43 27 Z", vein)
c.line(46, 20, 53, 19, vein_hi)

# Aorta rising behind the heart and arching right.
c.path("M31 23 C29 17 29 10 33 6 C37 2 44 3 48 6 C51 9 51 13 49 17 L43 16 C45 12 44 9 41 8 C37 6 35 9 36 14 L38 23 Z", outline)
c.path("M33 23 C32 17 31 11 34 8 C37 4 42 5 46 7 C49 9 49 12 47 16 L44 15 C46 11 44 8 41 7 C36 6 33 10 34 15 L36 23 Z", artery)
c.path("M35 14 C34 10 36 7 40 7 C43 7 46 9 47 11", artery_hi, fill=False)
c.line(34, 9, 35, 16, light)

# Aortic branches.
for d in ["M35 8 L34 2 C34 1 36 1 37 2 L38 7 Z", "M41 7 L42 1 C42 0 44 0 45 1 L44 8 Z", "M46 9 L50 4 C51 3 53 4 53 6 L49 12 Z"]:
    c.path(d, outline)
for d in ["M36 7 L36 2 L37 2 L38 7 Z", "M42 7 L43 1 L44 1 L44 8 Z", "M47 9 L51 5 L52 6 L49 11 Z"]:
    c.path(d, artery)

# Main heart silhouette.
c.path("M30 18 C24 15 18 16 14 21 C10 26 10 34 14 40 C18 47 23 51 29 59 C31 62 34 63 36 59 C41 53 48 48 52 41 C57 31 53 22 47 19 C42 16 36 18 33 21 Z", outline)
# Base volume.
c.path("M29 19 C23 17 18 18 15 23 C12 28 13 35 16 40 C20 46 25 51 30 58 C32 61 34 61 36 57 C41 52 47 47 50 40 C54 32 51 24 46 21 C41 18 36 20 33 24 C32 22 31 20 29 19 Z", dark_red)

# Right anatomical ventricle, broad lit mass on viewer left.
c.path("M27 23 C20 20 15 25 15 32 C15 39 21 45 28 50 C31 52 33 55 34 58 C31 52 30 43 32 35 C34 28 32 25 27 23 Z", red)
c.path("M24 23 C18 23 16 27 16 33 C17 39 21 43 27 47 C29 48 30 47 29 44 C27 37 31 30 28 26 C27 24 26 24 24 23 Z", bright)
c.path("M19 26 C17 29 17 34 19 38 C21 41 24 43 27 44", light, fill=False)
c.path("M20 25 C18 29 19 32 20 34", pink, fill=False)

# Left ventricle, darker powerful lobe at viewer right.
c.path("M36 24 C41 20 48 23 50 29 C53 37 48 44 43 49 C39 53 37 57 34 60 C35 52 31 44 32 36 C32 30 33 26 36 24 Z", shadow)
c.path("M40 24 C46 23 49 27 49 33 C50 39 46 44 42 48 C38 52 36 56 34 59 C37 49 34 43 35 35 C35 29 37 26 40 24 Z", dark_red)
c.path("M44 26 C48 29 48 35 46 40 C44 44 41 46 39 49", red, fill=False)
c.line(47, 29, 48, 35, bright)
c.set(46, 28, light)

# Atria and auricles.
c.path("M14 23 C10 20 8 23 9 28 C10 31 12 33 15 34 L19 27 C18 25 16 24 14 23 Z", outline)
c.path("M14 24 C11 22 10 24 11 28 C11 30 13 31 15 32 L18 27 C17 25 16 25 14 24 Z", shadow)
c.set(12, 25, light)
c.set(13, 26, bright)

c.path("M45 20 C49 17 54 20 54 25 C54 29 52 31 49 32 L44 27 Z", outline)
c.path("M46 21 C49 19 52 21 52 25 C52 28 51 29 49 30 L45 27 Z", dark_red)
c.line(48, 21, 51, 24, light)

# Central interventricular groove, with fatty tissue.
c.path("M32 24 C31 30 30 36 31 42 C32 49 35 53 34 59", maroon, fill=False)
c.path("M34 25 C33 31 32 36 33 42 C34 48 36 52 35 57", fat_dark, fill=False)
c.path("M33 27 C32 34 33 40 34 44", fat, fill=False)
c.set(34, 30, fat_hi); c.set(34, 35, fat_hi); c.set(35, 45, fat_hi); c.set(36, 51, fat)

# Coronary artery branches.
c.path("M34 27 C38 29 40 33 43 37 C45 40 47 40 49 40", artery_hi, fill=False)
c.path("M34 30 C29 31 26 34 23 37 C21 39 19 39 17 39", artery, fill=False)
c.path("M35 42 C39 42 41 44 43 47", artery_hi, fill=False)
c.path("M32 38 C28 39 26 41 25 44", artery_hi, fill=False)
# Dark vessel edges and small blue coronary veins.
c.path("M35 26 C38 28 41 33 44 36 C46 38 48 38 50 38", deep, fill=False)
c.path("M28 25 C26 29 24 31 20 32", vein, fill=False)
c.path("M41 31 C40 35 40 39 42 42", vein, fill=False)
c.path("M27 46 C29 48 30 51 31 54", vein_hi, fill=False)

# Muscle bands and secondary vessels break up the deep ventricular plane.
c.path("M36 33 C39 32 42 33 44 35", bright, fill=False)
c.path("M36 38 C39 37 42 38 44 40", red, fill=False)
c.path("M37 43 C39 42 41 43 42 45", light, fill=False)
c.path("M38 27 C39 30 38 33 37 35", maroon, fill=False)
c.line(42, 29, 44, 30, light)
c.line(39, 36, 41, 36, artery_hi)
c.line(40, 41, 42, 42, bright)
c.set(37, 31, pink); c.set(43, 33, pale); c.set(38, 40, bright)
c.set(41, 46, pink); c.set(38, 48, red)

# Specular pixels and myocardial texture.
for x,y,col in [
 (22,22,pale),(24,22,pink),(17,29,pink),(18,35,light),(20,39,pink),
 (23,42,light),(26,46,bright),(29,49,light),(30,55,bright),
 (40,23,light),(43,24,bright),(47,31,light),(46,36,bright),(43,43,bright),
 (39,48,light),(37,53,bright),(16,36,bright),(21,27,pale),
 (25,25,light),(27,29,pink),(25,34,light),(22,36,bright)
]: c.set(x,y,col)
# Tiny shadow pores/fibres.
for x,y in [(15,33),(18,42),(21,45),(24,48),(28,52),(31,57),(39,26),(44,28),(48,34),(45,41),(40,46),(37,50),(29,33),(27,38),(30,43)]:
    c.set(x,y,deep)
# Short muscle fibres.
c.line(19,31,21,30,light); c.line(21,40,23,41,pink); c.line(24,28,26,28,pale)
c.line(39,29,41,28,bright); c.line(44,34,46,35,light); c.line(38,45,40,44,bright)

view(c, scale=8, margin=1, edges="all")
finish(c)
