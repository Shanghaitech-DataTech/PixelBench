from pixelbench_api import *

result = new_canvas(16, 16, background=None, name="female-lab-researcher-chibi")

# Compact game-sprite palette.
HAIR = "#171821"
HAIR_HI = "#34313d"
OUTLINE = "#252733"
SKIN = "#f2b58f"
SKIN_SH = "#d9866d"
EYE = "#6a3828"
EYE_HI = "#f7dfc4"
WHITE = "#f4f3e8"
COAT_SH = "#b8c7ca"
COAT_DARK = "#7f969b"
TEAL = "#2c8f91"
TEAL_HI = "#58c5ba"
SHOE = "#3d3540"
GLASS = "#91e2da"
LIQUID = "#e15d7b"

# Hair mass and round chibi head.
for y, x0, x1 in [
    (0, 6, 9), (1, 4, 11), (2, 3, 12), (3, 2, 13),
    (4, 2, 13), (5, 2, 13), (6, 2, 13), (7, 3, 12), (8, 3, 12)
]:
    result.line(x0, y, x1, y, HAIR)

# Face, ears, and neck.
result.rect(4, 3, 8, 5, SKIN)
result.set(3, 5, SKIN_SH).set(12, 5, SKIN_SH)
result.rect(7, 7, 2, 3, SKIN_SH)
result.rect(7, 7, 2, 2, SKIN)

# Asymmetric bangs and hair shine.
result.line(4, 2, 10, 2, HAIR)
result.line(3, 3, 7, 3, HAIR)
result.set(4, 4, HAIR).set(7, 3, HAIR).set(10, 3, HAIR)
result.set(5, 1, HAIR_HI).set(6, 1, HAIR_HI)
result.set(4, 2, HAIR_HI).set(3, 3, HAIR_HI)
# Side locks frame the face.
result.line(3, 4, 3, 8, HAIR)
result.line(12, 4, 12, 8, HAIR)
result.set(4, 8, HAIR).set(11, 8, HAIR)

# Brown eyes with tiny pale highlights, brows, nose and smile.
result.set(5, 4, HAIR_HI).set(10, 4, HAIR_HI)
result.set(5, 5, EYE).set(10, 5, EYE)
result.set(5, 6, EYE_HI).set(10, 6, EYE_HI)
result.set(8, 6, SKIN_SH)
result.set(8, 7, EYE)

# Body silhouette: oversized coat, short arms, and little boots.
result.line(5, 9, 10, 9, OUTLINE)
result.line(4, 10, 11, 10, OUTLINE)
result.line(3, 11, 12, 11, OUTLINE)
result.line(3, 12, 12, 12, OUTLINE)
result.line(4, 13, 11, 13, OUTLINE)
result.line(4, 14, 11, 14, OUTLINE)
result.rect(5, 15, 3, 1, SHOE)
result.rect(9, 15, 3, 1, SHOE)

# White lab coat with lapels and cool pixel shadows.
result.rect(5, 9, 6, 1, WHITE)
result.rect(4, 10, 8, 3, WHITE)
result.rect(5, 13, 6, 2, WHITE)
result.set(4, 12, COAT_SH).set(5, 14, COAT_SH)
result.set(11, 11, COAT_SH).set(10, 14, COAT_SH)
result.set(6, 10, COAT_SH).set(9, 10, COAT_SH)
# Teal shirt under open lapels.
result.set(7, 9, TEAL).set(8, 9, TEAL)
result.set(7, 10, TEAL_HI).set(8, 10, TEAL)
result.set(7, 11, TEAL).set(8, 11, TEAL)
# Lapel edges, seam, pocket and badge.
result.set(6, 9, COAT_DARK).set(9, 9, COAT_DARK)
result.set(6, 10, COAT_DARK).set(9, 10, COAT_DARK)
result.line(8, 12, 8, 14, COAT_DARK)
result.set(9, 12, COAT_DARK).set(10, 12, COAT_DARK)
result.set(10, 10, LIQUID)

# Sleeves, hands, and a tiny test tube held at screen right.
result.set(2, 11, COAT_DARK).set(2, 12, WHITE).set(3, 13, SKIN)
result.set(13, 11, COAT_DARK).set(13, 12, WHITE).set(12, 13, SKIN)
result.set(13, 13, GLASS).set(14, 13, GLASS)
result.set(13, 14, GLASS).set(14, 14, OUTLINE)
result.set(13, 15, LIQUID).set(14, 15, LIQUID)

view(result, scale=28, margin=1, edges="all")
finish(result)
