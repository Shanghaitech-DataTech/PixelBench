from pixelbench_api import *

c = new_canvas(64, 64, name="eye")

# palette
aura = c.color((95, 50, 150, 70), name="aura")
shadow1 = c.color((18, 10, 35, 120), name="shadow1")
shadow2 = c.color((10, 5, 25, 150), name="shadow2")
body = c.color("#241536", name="body")
body_light = c.color("#3a2350", name="body_light")
body_dark = c.color("#160b24", name="body_dark")
tip = c.color("#4a2c66", name="tip")
sclera = c.color("#e9e2f5", name="sclera")
sclera_shade = c.color("#b3a6cf", name="sclera_shade")
iris = c.color("#5a2390", name="iris")
iris_light = c.color("#7a3fc0", name="iris_light")
iris_dark = c.color("#2d0f4d", name="iris_dark")
pupil = c.color("#0b0614", name="pupil")
pupil_glow = c.color("#b98ae8", name="pupil_glow")
glow_soft = c.color((210, 170, 255, 90), name="glow_soft")
glow_inner = c.color((220, 190, 255, 150), name="glow_inner")
white = c.color("#ffffff", name="white")

# ambient aura behind the monster
c.ellipse(32, 26, 25, 20, aura)

# soft ground shadow
c.ellipse(32, 58, 19, 4, shadow1)
c.ellipse(32, 59, 12, 2, shadow2)

# short tentacles (drawn before body so their bases are hidden)
def tentacle(x, y0, tx, ty, w=2):
    d = (f"M {x-w} {y0} "
         f"C {x-w-1} {(y0+ty)//2} {tx-1} {ty-2} {tx} {ty} "
         f"C {tx+1} {ty-2} {x+w+1} {(y0+ty)//2} {x+w} {y0} Z")
    c.path(d, body)
    c.set(tx, ty, tip)

tentacles = [
    (16, 40, 14, 48, 2),
    (23, 41, 22, 51, 2),
    (31, 42, 32, 52, 2),
    (39, 41, 41, 51, 2),
    (46, 40, 48, 48, 2),
    (52, 39, 55, 44, 2),
]
for x, y0, tx, ty, w in tentacles:
    tentacle(x, y0, tx, ty, w)

# main body blob
body_path = (
    "M 22 8 "
    "C 30 3 42 3 46 10 "
    "C 52 14 55 22 53 31 "
    "C 51 38 47 42 41 43 "
    "C 38 44 34 43 32 43 "
    "C 30 43 26 44 23 43 "
    "C 17 42 13 38 11 31 "
    "C 9 22 12 14 18 10 "
    "C 20 8 21 8 22 8 Z"
)
c.path(body_path, body)

# rim light along the top-left of the body
c.path("M 22 8 C 30 3 42 3 46 10", body_light, fill=False)

# sclera (eye opening base)
sclera_path = (
    "M 16 23 "
    "C 19 14 28 10 32 10 "
    "C 36 10 45 14 48 23 "
    "C 45 32 36 36 32 36 "
    "C 28 36 19 32 16 23 Z"
)
c.path(sclera_path, sclera)

# veins
c.line(19, 21, 24, 25, sclera_shade)
c.line(45, 21, 40, 25, sclera_shade)
c.line(19, 26, 23, 27, sclera_shade)
c.line(45, 26, 41, 27, sclera_shade)

# iris
c.ellipse(32, 22, 10, 9, iris)

# radial iris streaks
import math
for ang in range(0, 360, 45):
    x = 32 + int(round(math.cos(math.radians(ang)) * 8))
    y = 22 + int(round(math.sin(math.radians(ang)) * 7))
    c.line(32, 22, x, y, iris_light)

# dark limbal ring around the iris
c.ellipse(32, 22, 10, 9, iris_dark, fill=False)

# pupil (small enough that the deep purple iris stays readable)
c.ellipse(32, 22, 2, 3, pupil)
# faintly glowing core inside the pupil
c.set(32, 22, pupil_glow)
c.set(31, 22, pupil_glow)

# small specular highlights (glassy, faintly glowing feel)
c.set(31, 19, white)
c.set(30, 20, white)

# eyelids overlap the top and bottom of the eye for a menacing squint
upper_lid = (
    "M 16 23 "
    "C 19 14 28 10 32 10 "
    "C 36 10 45 14 48 23 "
    "C 44 19 36 17 32 17 "
    "C 28 17 20 19 16 23 Z"
)
lower_lid = (
    "M 16 23 "
    "C 19 32 28 36 32 36 "
    "C 36 36 45 32 48 23 "
    "C 44 31 36 33 32 33 "
    "C 28 33 20 31 16 23 Z"
)
c.path(upper_lid, body)
c.path(lower_lid, body)

# thin lid rim highlights
c.path("M 16 23 C 20 19 28 17 32 17 C 36 17 44 19 48 23", body_light, fill=False)
c.path("M 16 23 C 20 31 28 33 32 33 C 36 33 44 31 48 23", body_light, fill=False)

# faint pupil glow as a separate layer, composited source-over
g = new_canvas(64, 64, name="glow")
g.clear()
g.ellipse(32, 22, 7, 6, glow_soft)
g.ellipse(32, 22, 3, 3, None)  # cut the centre out -> outer ring
g.ellipse(32, 22, 4, 4, glow_inner)
g.ellipse(32, 22, 2, 2, None)  # cut the centre out -> brighter inner ring

result = flatten([c, g], name="result")

# crisp specular dots on top of the glow, so the eye reads as glossy
result.set(31, 19, white)
result.set(30, 20, white)

print(result.stats_text())
print(result.matrix_text(region=(6, 0, 58, 63)))

save("void_eye", result)
finish(result)
