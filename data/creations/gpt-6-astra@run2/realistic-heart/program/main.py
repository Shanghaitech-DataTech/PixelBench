from pixelbench_api import *

# 64x64 transparent pixel-art study of a realistic human heart
c = new_canvas(64, 64, background=None, name="realistic_heart")

# Palette: kept deliberately small for strong pixel-art grouping.
ink      = "#24101a"
blackred = "#35121d"
shadow   = "#4b1724"
plum     = "#5f1d2c"
maroon   = "#742337"
red0     = "#8f2b3d"
red1     = "#a93645"
red2     = "#bd4650"
red3     = "#ce5b5d"
coral    = "#dc7470"
rose     = "#e79586"
light    = "#f2b09b"
cream    = "#ffd0ae"

# Cool lowlights distinguish folds and vessels from muscle.
blueink  = "#24182b"
blue0    = "#39213a"
blue1    = "#51304b"
blue2    = "#71435a"
blue3    = "#92536a"

# A subtle cast shadow gives the floating transparent sprite a grounded edge.
c.ellipse(32, 57, 19, 3, "#24101a", fill=True)
c.ellipse(34, 56, 14, 2, "#4b1724", fill=True)

# Rear vessel mass, tucked behind the muscle.
c.path("M 27 25 C 24 20 24 15 26 11 C 28 7 34 7 37 10 L 40 16 L 45 12 C 48 10 52 12 53 15 C 54 18 51 22 48 25 L 44 30 Z", blackred, fill=True)
c.path("M 29 23 C 27 18 27 13 29 11 C 31 9 34 10 35 12 L 37 19 L 42 16 C 45 13 49 13 50 15 C 50 17 48 20 45 23 L 41 28 Z", maroon, fill=True)
c.path("M 31 20 C 30 16 30 12 32 11 C 34 11 35 13 35 16 L 36 22 Z", red2, fill=True)
c.path("M 43 19 C 46 15 48 14 49 15 C 49 17 47 19 44 22 Z", red1, fill=True)

# Great vessels: aorta's thick arch and the cut ends at the top.
c.path("M 28 25 C 27 20 27 13 29 8 C 31 4 36 4 39 7 C 41 10 40 15 38 19 L 35 26 Z", ink, fill=True)
c.path("M 30 24 C 29 18 29 12 31 8 C 32 6 35 6 37 8 C 39 11 38 15 36 20 L 34 25 Z", red1, fill=True)
c.path("M 32 21 C 31 16 31 10 33 8 C 34 7 36 8 36 10 C 37 13 35 18 34 22 Z", red3, fill=True)
c.line(32, 8, 35, 7, rose)
c.line(34, 7, 36, 9, light)
# vessel opening
c.ellipse(33, 5, 3, 2, ink, fill=True)
c.ellipse(33, 5, 2, 1, red2, fill=True)
c.set(32, 5, red3)

# Pulmonary artery crossing in front of the aorta.
c.path("M 31 25 C 30 20 33 16 37 15 C 42 14 46 16 48 20 L 46 27 L 39 29 Z", ink, fill=True)
c.path("M 33 25 C 33 21 35 18 38 17 C 42 16 45 18 46 21 L 44 25 L 39 27 Z", plum, fill=True)
c.path("M 35 23 C 36 20 38 18 41 18 C 43 18 45 19 45 21 L 43 23 Z", red2, fill=True)
c.line(38, 18, 42, 17, red3)
c.ellipse(45, 17, 3, 2, ink, fill=True)
c.ellipse(45, 17, 2, 1, red1, fill=True)

# Main outer anatomical silhouette, with the notch and pointed apex.
c.path("M 29 23 C 25 21 20 23 17 27 C 14 29 11 34 12 39 C 13 45 18 48 22 51 C 25 54 28 58 34 61 C 37 59 40 56 43 53 C 48 49 52 44 54 38 C 56 32 53 27 49 25 C 45 23 42 24 39 27 C 37 24 34 22 29 23 Z", ink, fill=True)

# Deep maroon underpainting preserves a near-black contour.
c.path("M 29 25 C 25 23 21 25 18 28 C 15 31 14 35 15 39 C 16 44 20 47 24 50 C 27 53 30 57 34 59 C 37 56 40 54 43 51 C 47 47 50 43 52 37 C 54 32 51 28 48 27 C 44 25 41 27 38 30 C 36 26 33 24 29 25 Z", maroon, fill=True)

# Viewer-left chamber: cooler, folded side of the heart.
c.path("M 28 25 C 24 24 20 26 18 29 C 15 32 15 37 17 41 C 19 44 23 46 27 48 L 33 55 L 35 43 L 32 32 Z", shadow, fill=True)
c.path("M 26 27 C 22 26 19 29 18 32 C 17 36 18 40 21 42 C 23 44 27 44 30 47 L 33 52 L 33 38 L 29 30 Z", red0, fill=True)
c.path("M 22 29 C 19 31 18 35 19 38 C 20 41 23 42 26 42 L 29 38 L 27 31 Z", red2, fill=True)
c.path("M 20 32 C 20 29 23 28 25 28 L 27 31 L 23 34 Z", red3, fill=True)

# Viewer-right ventricle: broad warm plane tapering into the apex.
c.path("M 37 29 C 41 26 46 26 49 29 C 52 33 51 38 49 42 C 47 47 42 50 38 54 L 34 59 C 33 54 32 48 32 42 C 32 36 33 32 37 29 Z", red0, fill=True)
c.path("M 39 30 C 43 28 47 29 49 32 C 50 36 48 41 45 45 C 42 49 38 51 35 56 L 34 43 C 34 37 35 33 39 30 Z", red2, fill=True)
c.path("M 42 30 C 45 29 48 31 48 34 C 48 38 45 42 42 45 C 40 47 37 48 35 52 L 35 40 C 36 35 38 32 42 30 Z", red3, fill=True)
c.path("M 44 31 C 47 31 48 33 47 36 C 46 39 43 42 40 44 L 37 45 C 39 39 40 34 44 31 Z", coral, fill=True)

# Central interventricular groove, a dark organic seam.
c.path("M 35 29 C 34 35 33 41 34 47 C 35 52 35 56 34 59 L 32 55 C 31 49 30 44 30 39 C 30 34 31 29 33 26 Z", blueink, fill=True)
c.path("M 34 31 C 33 37 32 43 33 49 L 34 54 L 35 48 C 34 41 36 34 36 30 Z", plum, fill=True)

# Left atrium and auricle, sitting over the upper heart mass.
c.path("M 19 26 C 20 22 24 20 29 22 C 32 23 34 26 34 30 L 29 34 C 26 31 22 32 19 30 Z", blackred, fill=True)
c.path("M 21 26 C 22 23 25 22 28 23 C 31 24 32 26 32 29 L 29 31 C 26 29 23 30 21 29 Z", red1, fill=True)
c.path("M 22 25 C 24 23 27 23 29 25 L 30 28 L 26 27 L 23 28 Z", red3, fill=True)
# right auricular flap
c.path("M 43 24 C 47 22 51 24 53 27 C 54 30 52 33 49 34 L 45 31 L 40 29 Z", blackred, fill=True)
c.path("M 44 25 C 47 24 50 25 51 27 C 52 29 50 31 49 32 L 46 30 L 42 28 Z", red1, fill=True)
c.line(46, 26, 50, 28, red3)

# Large branching vessels and natural surface vessels.
c.path("M 28 27 C 25 29 23 33 22 37 C 21 40 19 42 17 43", blueink, fill=False)
c.path("M 29 28 C 27 31 26 34 25 37 C 24 40 22 42 19 44", blue3, fill=False)
c.line(26, 33, 22, 31, blue3)
c.line(24, 37, 20, 36, blue2)
c.line(22, 40, 18, 40, blue2)

c.path("M 39 27 C 42 32 43 35 43 39 C 43 44 41 48 38 52", blueink, fill=False)
c.path("M 40 28 C 42 33 41 37 42 40 C 42 45 40 48 37 52", blue3, fill=False)
c.line(42, 35, 47, 33, blue2)
c.line(42, 39, 47, 39, blue3)
c.line(41, 44, 45, 46, blue2)

# Fine coronary branches and capillary-like pixel marks.
c.line(30, 31, 27, 34, rose)
c.line(28, 34, 25, 35, red3)
c.line(27, 35, 26, 38, rose)
c.line(38, 31, 40, 35, cream)
c.line(40, 35, 40, 39, rose)
c.line(39, 40, 37, 44, coral)
c.line(36, 46, 34, 51, red1)
c.line(44, 33, 47, 31, rose)

# Muscle striations: short, stepped highlights and red planes.
c.line(20, 37, 24, 38, red3)
c.line(21, 39, 26, 40, red1)
c.line(23, 42, 28, 43, red3)
c.line(26, 45, 30, 47, red1)
c.line(37, 34, 40, 33, light)
c.line(36, 37, 41, 36, rose)
c.line(36, 40, 40, 39, red3)
c.line(36, 43, 39, 42, rose)
c.line(37, 47, 40, 45, red1)

# Specular glints along the wet upper muscle and vessel rim.
c.set(24, 25, light)
c.set(25, 24, rose)
c.set(28, 26, cream)
c.set(46, 26, rose)
c.set(47, 27, light)
c.set(18, 34, rose)
c.set(19, 33, light)
c.set(45, 30, cream)
c.set(46, 31, rose)
c.set(38, 29, rose)

# A few pixel clusters restore a crisp, hand-placed edge after the curves.
c.line(14, 34, 14, 39, shadow)
c.set(15, 42, shadow)
c.set(18, 46, shadow)
c.set(22, 49, shadow)
c.set(27, 54, shadow)
c.line(48, 44, 50, 40, blackred)
c.set(46, 48, blackred)
c.set(42, 53, blackred)
c.set(37, 57, blackred)

# Tiny contact shadow at the pointed tip.
c.set(34, 59, ink)
c.set(35, 58, shadow)

view(c)
finish(c)
