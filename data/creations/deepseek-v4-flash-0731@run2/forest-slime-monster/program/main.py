from pixelbench_api import *

OUTLINE = "#17351f"
BODY = "#55a04f"
BODY_LIGHT = "#79c46c"
BODY_DARK = "#3d7f43"
MOSS = "#a8d971"
MOSS_DARK = "#7fae52"
GLOW = "#eaff6d"
PUPIL = "#1d3a24"
EYE_HI = "#ffffff"
BONE = "#e9d6a8"
CAP = "#e23b30"
CAP_DK = "#a8231e"
SPOT = "#ffecd8"
STEM = "#f2dcac"
MOUTH = "#3b1f22"
TONGUE = "#e05a68"
CHEEK = (255, 124, 148, 170)

c = new_canvas(32, 32, name="slime")

# --- tiny antlers (bases get covered by body) ---
c.line(8, 12, 8, 6, BONE)
c.line(8, 8, 6, 5, BONE)
c.line(8, 8, 10, 5, BONE)
c.line(24, 12, 24, 6, BONE)
c.line(24, 8, 26, 5, BONE)
c.line(24, 8, 22, 5, BONE)

# --- body silhouette ---
c.ellipse(16, 18, 10, 9, BODY)
c.ellipse(16, 26, 8, 3, BODY)
c.ellipse(13, 29, 1, 1, BODY)
c.ellipse(19, 29, 1, 1, BODY)

# --- shading ---
c.ellipse(16, 26, 6, 3, BODY_DARK)
c.ellipse(12, 13, 3, 1, BODY_LIGHT)

# --- small red mushroom growing on its back (upper right) ---
c.rect(18, 11, 3, 2, STEM)
c.circle(19, 11, 2, CAP)
c.line(18, 12, 20, 12, CAP_DK)
c.set(19, 13, CAP_DK)
c.set(17, 10, SPOT)
c.set(20, 10, SPOT)

# --- glowing eyes ---
c.ellipse(11, 17, 2, 2, GLOW)
c.ellipse(11, 17, 1, 1, PUPIL)
c.set(10, 16, EYE_HI)
c.ellipse(21, 17, 2, 2, GLOW)
c.ellipse(21, 17, 1, 1, PUPIL)
c.set(20, 16, EYE_HI)

# --- mouth ---
c.ellipse(16, 23, 2, 1, MOUTH)
c.set(16, 23, TONGUE)

# --- blush cheeks ---
c.ellipse(9, 20, 1, 1, CHEEK)
c.ellipse(23, 20, 1, 1, CHEEK)

# --- moss patches ---
c.ellipse(10, 24, 2, 1, MOSS)
c.set(10, 24, MOSS_DARK)
c.ellipse(22, 22, 1, 1, MOSS)
c.set(21, 21, MOSS_DARK)

# --- unified dark outline ---
c.outline(OUTLINE)

# --- redraw thin details on top so they keep their colours ---
c.line(8, 12, 8, 6, BONE)
c.line(8, 8, 6, 5, BONE)
c.line(8, 8, 10, 5, BONE)
c.line(24, 12, 24, 6, BONE)
c.line(24, 8, 26, 5, BONE)
c.line(24, 8, 22, 5, BONE)
c.rect(18, 11, 3, 2, STEM)
c.circle(19, 11, 2, CAP)
c.line(18, 12, 20, 12, CAP_DK)
c.set(19, 13, CAP_DK)
c.set(17, 10, SPOT)
c.set(20, 10, SPOT)
c.ellipse(10, 24, 2, 1, MOSS)
c.set(10, 24, MOSS_DARK)
c.ellipse(22, 22, 1, 1, MOSS)
c.set(21, 21, MOSS_DARK)

# --- inspect ---
print(c.stats_text())

finish(c)
