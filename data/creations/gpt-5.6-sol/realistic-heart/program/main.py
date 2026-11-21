from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="realistic_heart")

# Compact anatomical palette.
outline = "#34151b"
deep = "#5a1720"
shadow = "#7b1d25"
red = "#a82a30"
mid = "#c33a3d"
light = "#df5750"
hi = "#f17a68"
bright = "#ff9a7e"
vein_dark = "#562231"
vein = "#84405a"
blue_dark = "#26394e"
blue = "#3f6278"
blue_hi = "#7191a0"
artery_dark = "#6d2226"
artery = "#b9433e"
artery_hi = "#e87562"

# Rear vessels: vena cava on left, pulmonary branches, and aortic arch.
c.path("M18 6 C15 8 15 15 16 23 L24 25 L28 18 C26 13 25 8 22 6 Z", outline)
c.path("M19 7 C17 10 17 17 18 22 L23 23 L26 18 C24 13 24 9 22 7 Z", blue_dark)
c.path("M20 8 C19 12 19 18 20 21 L22 21 C23 16 22 11 22 8 Z", blue)
c.rect(20, 9, 1, 10, blue_hi)

# Horizontal pulmonary vessels.
c.path("M12 19 C17 16 24 16 31 19 C38 15 47 14 54 17 L55 23 C47 23 41 23 36 26 L19 26 C16 24 13 23 10 23 Z", outline)
c.path("M13 20 C19 18 25 18 31 21 C39 17 47 16 53 18 L53 21 C45 20 39 23 35 25 L19 24 C17 22 15 22 12 22 Z", artery_dark)
c.path("M16 20 C22 19 26 20 31 22 C39 19 45 18 51 19", artery_hi, fill=False)

# Aorta rising and curling to the right.
c.path("M31 24 C29 17 28 10 31 5 C35 1 43 2 46 6 C49 9 49 14 52 16 L57 17 L56 24 L48 23 C42 21 40 16 40 12 C40 9 37 8 36 11 C35 15 38 20 39 25 Z", outline)
c.path("M33 23 C31 16 31 10 33 7 C36 4 42 4 44 7 C47 10 45 15 50 18 L55 19 L54 22 L49 21 C43 20 42 16 42 12 C42 7 36 6 34 10 C33 14 36 20 37 24 Z", artery)
c.path("M34 8 C37 5 42 6 43 9 C44 12 43 16 48 19", artery_hi, fill=False)
c.set(35, 7, bright)
c.set(55, 20, shadow)

# Main heart silhouette, with asymmetric atria and long ventricular apex.
c.path("M27 19 C22 17 16 19 13 24 C9 30 12 38 17 43 C21 48 24 53 29 59 C31 62 35 63 38 59 C42 54 45 48 49 42 C53 36 55 29 51 24 C48 20 43 19 39 22 C36 18 31 17 27 19 Z", outline)
# Base mass.
c.path("M27 21 C22 19 17 21 15 25 C12 30 14 36 18 41 C23 47 25 54 31 59 C33 61 35 61 37 58 C41 52 44 46 48 40 C52 34 52 28 49 25 C46 22 42 22 38 25 C35 21 31 20 27 21 Z", deep)

# Left ventricular muscle (viewer right), dominant bright chamber.
c.path("M37 25 C43 21 49 25 50 30 C52 36 47 42 44 47 C41 52 38 57 35 60 C33 57 32 52 32 46 C32 38 33 30 37 25 Z", red)
c.path("M39 27 C44 24 48 27 48 32 C49 37 45 42 42 47 C40 51 38 55 35 58 C35 50 35 42 36 35 C36 31 37 28 39 27 Z", mid)
c.path("M42 28 C45 27 47 29 47 33 C47 38 44 41 42 45 C40 49 39 52 37 54 C38 45 37 37 39 31 C40 29 41 28 42 28 Z", light)
c.path("M43 29 C45 29 46 31 45 34 C45 37 43 40 42 42", hi, fill=False)
c.set(44, 30, bright)
c.set(43, 31, bright)
c.set(42, 33, hi)

# Right ventricle and right atrium (viewer left), darker and rounder.
c.path("M27 22 C21 20 16 24 15 29 C14 35 18 40 22 44 C26 48 28 54 33 59 C32 52 34 44 32 36 C31 30 31 25 27 22 Z", shadow)
c.path("M21 23 C17 25 16 29 17 34 C18 39 22 41 25 45 C28 49 29 53 32 56 C30 48 32 41 30 34 C29 28 26 23 21 23 Z", red)
c.path("M19 26 C17 31 19 36 22 39 C24 41 26 43 27 46 C26 39 29 34 27 29 C25 25 22 24 19 26 Z", mid)
c.path("M19 27 C18 31 20 35 23 37", light, fill=False)
c.set(19, 29, hi)
c.set(20, 27, hi)

# Central interventricular groove.
c.path("M36 24 C33 29 33 36 33 42 C33 49 34 55 34 59", vein_dark, fill=False)
c.path("M35 27 C34 34 34 42 35 49 C35 53 35 56 34 59", vein, fill=False)
c.set(34, 33, "#a85a65")
c.set(34, 39, "#a85a65")
c.set(35, 48, "#a85a65")

# Coronary branch wrapping across the surface.
c.path("M38 26 C34 29 30 30 25 29 C22 28 20 27 17 29", vein_dark, fill=False)
c.path("M36 28 C31 31 27 31 23 30", vein, fill=False)
c.path("M34 36 C38 37 41 39 43 42", vein_dark, fill=False)
c.path("M34 37 C38 38 40 40 42 42", vein, fill=False)
c.path("M29 39 C26 42 25 46 27 50", vein_dark, fill=False)

# Small blue pulmonary vessel opening and upper folds.
c.path("M27 18 C27 14 29 11 33 11 C36 12 37 16 36 22 L31 25 Z", outline)
c.path("M29 19 C29 15 30 13 33 13 C35 14 35 17 34 21 L31 23 Z", blue_dark)
c.rect(30, 15, 2, 5, blue)
c.set(30, 15, blue_hi)

# Atrial lobes restored in front of vessel roots.
c.path("M17 22 C19 18 25 17 29 20 C31 22 30 27 27 30 C23 31 18 29 16 26 Z", outline)
c.path("M18 23 C21 19 25 19 28 21 C30 23 28 27 26 28 C22 29 18 27 18 23 Z", red)
c.path("M20 22 C22 21 25 21 27 22", light, fill=False)
c.set(19, 24, hi)

c.path("M39 22 C43 18 49 20 51 24 C53 27 51 31 48 33 C44 33 40 30 38 27 Z", outline)
c.path("M40 23 C43 20 47 21 49 24 C51 27 49 30 47 31 C43 31 41 29 40 26 Z", deep)
c.path("M42 23 C45 22 48 24 48 27", mid, fill=False)

# Block-level edge accents and tiny surface texture.
for x, y, col in [
    (15,31,light),(16,36,light),(18,40,mid),(21,44,light),(23,48,mid),
    (26,53,mid),(29,57,light),(32,59,hi),(38,55,light),(41,50,hi),
    (45,44,light),(48,38,mid),(50,32,shadow),(22,34,hi),(24,35,light),
    (39,34,hi),(40,35,hi),(40,46,hi),(37,51,light)
]:
    c.set(x, y, col)

# Deep edge pixels sharpen the silhouette and apex.
c.line(18, 43, 21, 46, deep)
c.line(47, 41, 44, 46, deep)
c.set(30, 60, outline)
c.set(31, 61, outline)
c.set(35, 60, outline)
c.set(36, 59, outline)

view(c, scale=8, margin=1, edges="all")
finish(c)
