# Public transportation icon set, 64x64 pixel art
result = new_canvas(64, 64, background="#0b1720", name="public-transportation-icon-set")

BG = "#0b1720"
PANEL = "#132a38"
FRAME = "#315166"
EDGE = "#4f7182"
INK = "#f1ead7"
SHADE = "#a9c1c4"
CYAN = "#27c2b8"
YELLOW = "#f2bd4b"
CORAL = "#ef6b5a"

# Consistent 29x29 framed cells.
def tile(x, y, accent):
    result.rect(x, y, 29, 29, FRAME)
    result.rect(x + 2, y + 2, 25, 25, PANEL)
    # Pixel-cut corners and repeated route marker.
    result.set(x, y, BG); result.set(x + 28, y, BG)
    result.set(x, y + 28, BG); result.set(x + 28, y + 28, BG)
    result.rect(x + 4, y + 4, 5, 2, accent)
    result.rect(x + 21, y + 23, 4, 2, EDGE)

# BUS, upper left
tile(2, 2, CYAN)
# body and destination cap
result.rect(8, 8, 17, 16, INK)
result.rect(10, 6, 13, 2, INK)
result.rect(6, 12, 2, 7, SHADE)
result.rect(25, 12, 2, 7, SHADE)
# windows
result.rect(10, 10, 5, 6, PANEL)
result.rect(17, 10, 6, 6, PANEL)
result.rect(10, 18, 13, 2, CYAN)
# bumper, lamps, wheels
result.rect(10, 22, 13, 2, SHADE)
result.set(9, 20, YELLOW); result.set(23, 20, YELLOW)
result.rect(10, 24, 4, 3, BG); result.rect(20, 24, 4, 3, BG)
result.rect(11, 24, 2, 2, EDGE); result.rect(21, 24, 2, 2, EDGE)

# SUBWAY, upper right
tile(33, 2, YELLOW)
# train face with stepped roof
result.rect(41, 7, 15, 2, INK)
result.rect(39, 9, 19, 15, INK)
result.rect(41, 24, 15, 2, SHADE)
# windscreen and center divider
result.rect(42, 11, 5, 7, PANEL)
result.rect(50, 11, 5, 7, PANEL)
result.rect(42, 20, 13, 2, CYAN)
result.set(41, 20, YELLOW); result.set(56, 20, YELLOW)
# undercarriage / rails
result.rect(42, 26, 4, 2, BG); result.rect(52, 26, 4, 2, BG)
result.line(40, 28, 43, 25, EDGE); result.line(57, 28, 54, 25, EDGE)
result.rect(40, 28, 18, 1, EDGE)

# BICYCLE, lower left
tile(2, 33, CORAL)
# two 2px-ring wheels
for cx in (10, 24):
    result.circle(cx, 53, 6, INK)
    result.circle(cx, 53, 4, PANEL)
    result.set(cx, 53, SHADE)
# frame joints and geometry
result.line(10, 53, 15, 44, CYAN)
result.line(15, 44, 20, 53, CYAN)
result.line(20, 53, 10, 53, CYAN)
result.line(15, 44, 24, 53, CYAN)
# duplicate key diagonals for 2px visual weight
result.line(11, 53, 16, 44, CYAN)
result.line(16, 45, 21, 53, CYAN)
# crank, seat, handlebar
result.rect(18, 51, 4, 4, YELLOW)
result.rect(13, 42, 6, 2, INK)
result.line(20, 45, 23, 43, INK)
result.line(23, 43, 26, 44, INK)
result.line(20, 45, 24, 53, INK)

# PEDESTRIAN, lower right
tile(33, 33, CYAN)
# head
result.rect(47, 39, 5, 2, INK)
result.rect(46, 41, 7, 5, INK)
result.rect(47, 46, 5, 2, SHADE)
# torso as a bold walking silhouette
result.poly([(46,47),(52,47),(54,52),(58,54),(57,57),(52,54),(51,51),(50,56),(55,60),(52,62),(47,57),(44,62),(40,62),(46,54),(43,52),(40,56),(38,54),(43,47)], INK)
# clothing/accent pixels
result.rect(47, 48, 4, 5, CORAL)
result.rect(45, 53, 6, 2, CORAL)
# restore separated limbs/gaps for readable pose
result.set(44, 57, PANEL)
result.set(45, 58, PANEL)
result.set(51, 57, PANEL)

view(result, scale=8, margin=0)
finish(result)
