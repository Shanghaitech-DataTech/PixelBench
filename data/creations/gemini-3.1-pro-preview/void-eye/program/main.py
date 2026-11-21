import os
from pixelbench_api import new_canvas, flatten, finish, view

# Create canvases
c_shadow = new_canvas(64, 64, name="shadow")
c = new_canvas(64, 64, name="monster")

# Palette
b_out = c.color("#0a0812")
b_dark = c.color("#1a1525")
b_mid = c.color("#2d243d")
b_light = c.color("#46395e")
b_high = c.color("#695787")

s_dark = c.color("#5c5366")
s_mid = c.color("#9286a1")
s_light = c.color("#d1c9db")
s_white = c.color("#f2eff5")

i_dark = c.color("#260542")
i_mid = c.color("#480a7d")
i_light = c.color("#7211c4")

p_glow1 = c.color("#a933ff")
p_glow2 = c.color("#d899ff")
p_core = c.color("#ffffff")

# Shadow on ground
shadow_col = c.color((0, 0, 0, 100), "shadow")
shadow_core = c.color((0, 0, 0, 150), "shadow_core")
c_shadow.ellipse(32, 58, 20, 4, shadow_col)
c_shadow.ellipse(32, 58, 12, 2, shadow_core)

# Extra small tentacles (Back)
c.path("M 16 34 Q 4 40 6 48 Q 8 48 10 42 Q 12 38 18 36 Z", b_dark)
c.path("M 48 34 Q 60 40 58 48 Q 56 48 54 42 Q 52 38 46 36 Z", b_dark)

# Tentacles (Back layer)
# Left back
c.path("M 22 38 Q 6 45 8 55 Q 12 58 14 50 Q 18 45 26 40 Z", b_dark)
c.path("M 23 39 Q 8 46 9 54 Q 11 56 13 49 Q 17 44 25 39 Z", b_mid)
# Right back
c.path("M 42 38 Q 58 45 56 55 Q 52 58 50 50 Q 46 45 38 40 Z", b_dark)
c.path("M 41 39 Q 56 46 55 54 Q 53 56 51 49 Q 47 44 39 39 Z", b_mid)

# Mid tentacles
# Left mid
c.path("M 26 42 Q 12 52 16 62 Q 20 62 20 55 Q 22 48 30 44 Z", b_mid)
c.path("M 27 43 Q 14 52 17 61 Q 19 61 19 54 Q 21 47 29 43 Z", b_light)
# Right mid
c.path("M 38 42 Q 52 52 48 62 Q 44 62 44 55 Q 42 48 34 44 Z", b_mid)
c.path("M 37 43 Q 50 52 47 61 Q 45 61 45 54 Q 43 47 35 43 Z", b_light)

# Horns (Bone colored)
c.path("M 20 14 Q 14 6 10 4 Q 18 8 26 12 Z", s_dark)
c.path("M 21 14 Q 15 7 11 5 Q 18 9 25 12 Z", s_mid)
c.path("M 44 14 Q 50 6 54 4 Q 46 8 38 12 Z", s_dark)
c.path("M 43 14 Q 49 7 53 5 Q 46 9 39 12 Z", s_mid)
c.path("M 30 10 Q 28 2 32 0 Q 36 2 34 10 Z", s_dark)
c.path("M 31 10 Q 29 3 32 1 Q 35 3 33 10 Z", s_mid)

# Body Base
c.circle(32, 28, 21, b_dark)
c.circle(32, 27, 20, b_mid)
c.circle(32, 25, 18, b_light)
c.circle(32, 23, 15, b_high)

# Sclera
c.circle(32, 28, 14, s_dark)
c.circle(32, 28, 13, s_mid)
c.circle(32, 28, 12, s_light)
c.circle(32, 28, 10, s_white)

# Iris
c.circle(32, 28, 7, i_dark)
c.circle(32, 28, 6, i_mid)
c.circle(32, 28, 5, i_light)

# Pupil & Glow
c.circle(32, 28, 4, p_glow1)
c.circle(32, 28, 2, p_glow2)
c.ellipse(32, 28, 0, 3, p_core)

# Eye Reflection
c.circle(35, 25, 1, p_core)
c.set(36, 24, p_core)

# Angry Brow Eyelid
c.path("M 15 24 Q 24 16 32 20 Q 40 16 49 24 Q 49 10 32 10 Q 15 10 15 24 Z", b_dark)
c.path("M 16 23 Q 24 17 32 21 Q 40 17 48 23 Q 48 12 32 12 Q 16 12 16 23 Z", b_mid)
c.path("M 17 22 Q 24 18 32 22 Q 40 18 47 22 Q 47 14 32 14 Q 17 14 17 22 Z", b_light)

# Bottom Eyelid
c.path("M 16 34 Q 32 40 48 34 Q 48 48 32 48 Q 16 48 16 34 Z", b_dark)
c.path("M 17 35 Q 32 39 47 35 Q 47 46 32 46 Q 17 46 17 35 Z", b_mid)

# Veins or texture on the body
c.path("M 16 28 Q 12 24 18 20", b_high, fill=False)
c.path("M 48 28 Q 52 24 46 20", b_high, fill=False)
c.path("M 22 40 Q 28 44 32 42", b_high, fill=False)
c.path("M 42 40 Q 36 44 32 42", b_high, fill=False)

# Warts
c.circle(20, 32, 1, b_high)
c.set(20, 33, b_light)
c.circle(44, 32, 1, b_high)
c.set(44, 33, b_light)
c.circle(24, 20, 1, b_high)
c.circle(40, 20, 1, b_high)

# Front tentacles
# Left front
c.path("M 26 42 Q 20 54 24 62 Q 28 62 28 54 Q 27 49 28 42 Z", b_mid)
c.path("M 27 43 Q 22 54 25 61 Q 27 61 27 54 Q 26 49 27 43 Z", b_light)

# Right front
c.path("M 38 42 Q 44 54 40 62 Q 36 62 36 54 Q 37 49 36 42 Z", b_mid)
c.path("M 37 43 Q 42 54 39 61 Q 37 61 37 54 Q 38 49 37 43 Z", b_light)

# Outline the monster
c.outline(b_out)

# Flatten
final = flatten([c_shadow, c])
view(final)
finish(final)
