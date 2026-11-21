W, H = 72, 68
OX, OY = 12, 3

# Preserve the supplied artwork exactly, only centering it on a roomier stage.
f1 = new_canvas(W, H, name="frame_1")
f1.blit(input_canvas, OX, OY)

# Work on an independent body copy for the attack pose.
body = f1.copy(name="attack_body")
trail = new_canvas(W, H, name="motion_trail")
weapon = new_canvas(W, H, name="attack_weapon")

INK = "#101010"
DEEP = "#2c2623"
DARK = "#332d32"
STEEL = "#858086"
STEEL_HI = "#dccaca"
WHITE = "#ffffff"
GOLD = "#c67b02"
GOLD_HI = "#ffcc43"
GOLD_PALE = "#ffe38c"
WOOD = "#804018"
WOOD_DARK = "#422110"
MAGENTA = "#9e005d"
MAGENTA_HI = "#ef5ba1"

# A broad, broken crescent behind the descending weapon. The stepped edges
# and small gaps keep the effect consistent with the source sprite.
# Three tapering streamers describe the hammer's fast descending arc.
trail.path("M 55 11 C 64 16 69 24 69 33 L 66 33 C 65 25 61 19 52 15 Z", WHITE, fill=True)
trail.path("M 68 36 C 68 43 65 49 61 54 L 58 51 C 62 46 64 41 64 36 Z", WHITE, fill=True)
trail.path("M 59 16 C 64 21 66 26 66 30 L 63 29 C 62 24 60 21 56 18 Z", "#a9a5ab", fill=True)
trail.rect(67, 22, 3, 3, WHITE)
trail.rect(66, 39, 3, 3, WHITE)
trail.rect(62, 48, 3, 3, WHITE)
trail.rect(57, 11, 2, 2, WHITE)

# Remove the old raised haft and its tip without disturbing the helmet/body.
for x, y, w, h in [
    (38, 10, 4, 3), (40, 12, 5, 3), (43, 14, 5, 3),
    (46, 16, 5, 3), (49, 18, 5, 3), (52, 20, 4, 4),
    (53, 21, 3, 4)
]:
    body.clear(x, y, w, h)

# Erase the forward leg and foot, then rebuild it as a low, weight-bearing step.
body.clear(39, 47, 14, 18)
# Upper leg emerging from the skirt, compressed under the forward lean.
body.poly([(38,43),(45,43),(49,48),(48,53),(43,54),(39,49)], INK)
body.rect(40, 44, 5, 3, GOLD)
body.poly([(42,46),(46,46),(47,50),(45,52),(41,49)], STEEL)
body.rect(43, 46, 3, 2, STEEL_HI)
body.rect(45, 50, 3, 2, "#5a565a")
# Segmented greave angles toward a planted, foreshortened boot.
body.poly([(44,51),(49,50),(54,56),(53,61),(49,63),(45,57)], INK)
body.poly([(46,52),(49,52),(52,55),(51,58),(48,58),(46,55)], STEEL)
body.rect(48, 53, 3, 2, STEEL_HI)
body.poly([(48,57),(53,57),(56,61),(54,64),(50,63),(47,60)], INK)
body.rect(50, 58, 3, 4, "#5a565a")
body.rect(51, 58, 3, 2, STEEL_HI)
body.poly([(52,61),(57,60),(63,62),(63,65),(54,66),(50,64)], INK)
body.rect(55, 62, 7, 3, STEEL)
body.rect(58, 62, 4, 2, STEEL_HI)
body.rect(54, 65, 9, 2, "#17003599")

# Shift the weapon arm forward/down over the original shoulder and gauntlet.
body.poly([(39,27),(45,28),(48,33),(45,37),(39,35),(36,31)], INK)
body.poly([(40,28),(44,29),(46,32),(44,35),(40,34),(38,31)], STEEL)
body.rect(42, 29, 3, 3, STEEL_HI)
body.rect(45, 33, 4, 4, GOLD)
body.rect(46, 34, 3, 2, GOLD_HI)

# Descending two-handed warhammer: dark outline, wooden core, metal head.
def thick_line(c, x0, y0, x1, y1, colour, radius=1):
    for d in range(-radius, radius + 1):
        c.line(x0 + d, y0, x1 + d, y1, colour)
        c.line(x0, y0 + d, x1, y1 + d, colour)

thick_line(weapon, 43, 32, 59, 55, INK, 2)
thick_line(weapon, 43, 32, 59, 55, WOOD_DARK, 1)
weapon.line(44, 32, 60, 55, WOOD)
weapon.rect(42, 31, 5, 5, INK)
weapon.rect(43, 32, 3, 3, GOLD_PALE)
weapon.rect(45, 34, 3, 3, GOLD)

# Compact heavy hammer head at the end of the arc.
weapon.poly([(56,52),(61,50),(65,53),(65,57),(60,60),(55,56)], INK)
weapon.poly([(58,52),(61,52),(63,54),(63,56),(60,58),(57,56)], STEEL)
weapon.rect(60, 52, 3, 2, STEEL_HI)
weapon.rect(63, 53, 3, 4, WHITE)
weapon.rect(57, 56, 3, 2, DARK)
weapon.rect(54, 53, 3, 4, GOLD)
weapon.set(55, 54, GOLD_HI)

# Speed chips tie the weapon head into the trailing streaks.
weapon.rect(66, 48, 3, 2, WHITE)
weapon.rect(68, 43, 2, 3, WHITE)
weapon.rect(64, 58, 2, 2, "#a9a5ab")

f2 = flatten([trail, body, weapon], name="frame_2")
view(f1, scale=7, margin=1, edges="all")
view(f2, scale=7, margin=1, edges="all")
finish([f1, f2])
