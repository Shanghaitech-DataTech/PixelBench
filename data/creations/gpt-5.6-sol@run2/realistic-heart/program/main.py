from pixelbench_api import *

result = new_canvas(64, 64, background=None, name="realistic-heart")

# Restrained anatomical palette.
outline = "#2a1018"
deep = "#43131c"
shadow = "#641a25"
shadow2 = "#7d2029"
mid = "#9e2830"
red = "#b93438"
light = "#d4514c"
high = "#ef7866"
glint = "#ff9a7b"
maroon = "#551827"
vein_dark = "#182332"
vein = "#263c50"
vein_light = "#42657a"
aorta_dark = "#521622"
aorta = "#8e2530"
aorta_light = "#c44743"
flesh_dark = "#73302f"
flesh = "#a94a43"

# Rear great vessels: vena cava and pulmonary branches.
result.path("M18 25 C15 21 14 15 16 8 L22 8 C21 15 22 20 25 25 Z", vein_dark)
result.path("M17 23 C16 18 17 12 18 8 L21 8 C20 15 21 20 23 24 Z", vein)
result.rect(18, 9, 2, 9, vein_light)
result.rect(17, 10, 1, 5, "#58788a")
result.path("M21 22 C15 20 10 21 7 25 L9 30 C14 27 19 27 25 29 Z", vein_dark)
result.path("M22 24 C16 23 12 24 9 26 L10 28 C16 26 20 27 25 30 Z", vein)

# Aortic arch and descending trunk.
result.path("M33 23 C34 16 32 10 36 6 C41 1 50 3 53 9 C55 13 53 18 51 22 L44 22 C47 17 49 14 47 10 C45 7 41 7 40 10 C38 14 40 20 40 24 Z", outline)
result.path("M35 23 C36 16 34 11 38 7 C41 4 47 5 50 9 C53 13 50 18 48 22 L43 22 C46 16 48 13 46 10 C44 8 41 8 39 11 C37 15 40 21 39 24 Z", aorta)
result.path("M39 8 C42 5 47 7 49 10 L47 12 C45 9 42 8 39 11 Z", aorta_light)
result.rect(48, 11, 3, 7, aorta_dark)
result.rect(49, 12, 1, 5, aorta_light)
# Aortic branch stubs.
result.path("M38 8 L36 3 L40 2 L42 7 Z", outline)
result.path("M38 7 L37 3 L39 3 L41 7 Z", aorta_light)
result.path("M44 6 L44 2 L48 2 L48 7 Z", outline)
result.rect(45, 3, 2, 4, aorta)
result.path("M49 8 L52 4 L55 6 L52 11 Z", outline)
result.path("M50 8 L52 5 L54 6 L52 10 Z", aorta)

# Pulmonary artery crossing the upper heart.
result.path("M27 17 C31 13 37 13 42 16 C46 18 50 18 55 16 L57 21 C50 25 43 23 38 21 C34 20 31 22 28 25 Z", outline)
result.path("M29 18 C33 15 37 15 41 17 C46 21 51 20 55 18 L55 20 C50 23 44 21 39 19 C35 18 32 21 29 23 Z", vein)
result.line(43, 19, 52, 20, vein_light)

# Main muscular silhouette, deliberately asymmetric and tapered.
result.path("M30 16 C24 13 17 15 13 21 C9 27 10 36 14 42 C18 48 24 51 28 56 C31 60 34 62 36 60 C39 56 41 53 46 49 C52 44 55 36 54 29 C53 22 48 18 42 18 C38 18 35 20 33 23 C33 20 32 18 30 16 Z", outline)
result.path("M29 18 C23 16 18 18 15 23 C12 29 13 36 16 41 C20 47 25 49 30 55 C32 57 34 60 35 58 C38 53 41 51 45 47 C50 42 53 35 51 28 C50 22 46 20 42 20 C37 20 35 24 33 28 C32 23 32 20 29 18 Z", shadow2)

# Right atrium (viewer's left), darker and rounder.
result.path("M28 19 C23 17 18 20 15 25 C13 30 14 38 18 42 C21 45 25 46 29 44 C32 41 31 34 30 29 C30 25 30 21 28 19 Z", mid)
result.path("M22 20 C18 22 16 26 16 32 C16 36 18 40 21 42 C18 37 19 29 22 24 C24 21 27 20 28 20 C26 19 24 19 22 20 Z", light)
result.path("M17 25 C16 29 16 33 17 35 L19 34 C18 30 19 26 21 23 Z", high)
result.rect(18, 25, 1, 5, glint)

# Left ventricle, dominant muscular chamber.
result.path("M35 27 C39 21 46 21 49 26 C53 32 50 40 46 45 C42 50 38 53 35 58 C32 53 28 49 27 44 C26 38 29 32 35 27 Z", red)
result.path("M42 23 C47 23 50 27 50 33 C50 39 46 45 41 49 C38 52 36 56 35 58 C35 51 37 45 40 40 C43 35 44 29 42 23 Z", shadow)
result.path("M35 29 C38 25 40 24 42 24 C43 31 40 38 37 43 C34 47 33 51 34 55 C30 50 28 45 29 40 C29 36 31 32 35 29 Z", light)
result.path("M33 31 C35 28 37 26 39 25 C39 30 36 35 34 39 C31 44 31 48 33 52 C29 47 29 42 30 38 C30 35 31 33 33 31 Z", high)
result.rect(31, 34, 1, 7, glint)
result.rect(32, 31, 1, 3, glint)
result.set(33, 29, glint)

# Septal groove gives the organ its anatomical division.
result.path("M33 25 C31 31 31 37 29 42 C28 46 30 52 34 57", deep, fill=False)
result.path("M34 26 C33 32 33 37 31 43 C30 48 32 53 35 57", maroon, fill=False)
result.set(31, 45, aorta_light)
result.set(32, 49, aorta_light)
result.set(33, 53, aorta_light)

# Upper atrial folds and auricles.
result.path("M15 23 C14 19 16 16 20 16 C23 16 25 19 24 22 C21 21 18 22 15 23 Z", deep)
result.path("M16 21 C17 18 20 17 22 19 L23 21 C20 20 18 21 16 22 Z", flesh)
result.path("M43 20 C45 16 50 17 52 21 C54 24 53 27 51 29 C49 24 47 22 43 20 Z", deep)
result.path("M45 20 C48 18 51 20 51 24 L50 26 C49 23 47 21 45 20 Z", flesh)
result.set(47, 20, light)

# Coronary vessels over the myocardium.
result.path("M36 25 C38 29 39 33 38 37 C37 42 37 47 35 52", aorta_dark, fill=False)
result.path("M37 25 C39 29 40 33 39 38 C38 43 38 48 36 53", aorta_light, fill=False)
result.line(39, 34, 45, 30, aorta_dark)
result.line(40, 34, 45, 31, aorta_light)
result.line(38, 40, 44, 42, aorta_dark)
result.line(38, 41, 43, 43, aorta_light)
result.line(36, 47, 40, 50, aorta_dark)
result.line(36, 48, 39, 51, aorta_light)
result.path("M29 29 C25 30 22 33 20 37 C19 40 21 43 24 45", vein_dark, fill=False)
result.path("M29 30 C25 31 23 34 21 38 C21 41 22 43 25 44", vein_light, fill=False)
result.line(23, 34, 18, 33, vein_dark)
result.line(23, 35, 19, 34, vein_light)

# Pixel-scale texture: highlights, pores and edge accents.
for x, y in [(22,24),(24,23),(20,38),(23,42),(26,47),(28,50),(42,27),(46,28),(47,35),(44,40),(41,45)]:
    result.set(x, y, light)
for x, y in [(19,27),(20,30),(18,37),(22,40),(24,46),(27,49),(43,25),(47,31),(48,37),(43,44),(39,49)]:
    result.set(x, y, high)
for x, y in [(16,31),(17,40),(25,20),(26,53),(30,56),(45,23),(50,29),(49,40),(45,46),(38,54)]:
    result.set(x, y, deep)

# Reassert a few dark silhouette pixels around the pointed apex.
result.set(34, 59, outline)
result.set(35, 59, deep)
result.set(35, 58, shadow)

view(result, scale=8, margin=0)
finish(result)
