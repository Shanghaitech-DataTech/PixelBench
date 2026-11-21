c = new_canvas(32, 32, background=None, name="skeleton-grunt")

BONE = "#e8e4d0"
SHADE = "#a8a288"
DARK = "#6b6552"
SWORD = "#b8c4cc"
SWD_D = "#7a8890"
HILT = "#8a6a3a"
WOOD = "#8a5c30"
WOOD_D = "#5e3d1e"
EYE = "#3a2f4a"

# --- legs (hunched stance) ---
c.set(12, 29, BONE); c.set(13, 28, BONE); c.set(13, 29, SHADE)
c.set(19, 29, BONE); c.set(18, 28, BONE); c.set(18, 29, SHADE)
# pelvis
c.rect(13, 26, 6, 2, BONE)
c.set(15, 27, SHADE)

# --- spine (hunched curve) ---
c.set(15, 25, SHADE); c.set(16, 24, BONE); c.set(16, 23, BONE)
c.set(16, 22, SHADE); c.set(16, 21, BONE)

# --- ribcage ---
c.rect(14, 20, 5, 2, BONE)
c.set(16, 20, SHADE)
c.rect(14, 18, 5, 2, BONE)
c.set(16, 19, SHADE)

# --- head, tilted forward (hunch) ---
c.rect(17, 13, 5, 5, BONE)
c.set(21, 14, SHADE)
c.set(20, 15, EYE); c.set(18, 15, EYE)
c.set(19, 17, DARK)  # jaw notch
c.set(19, 16, SHADE)
c.set(17, 12, BONE); c.set(21, 12, SHADE)  # cranium top

# --- sword arm (right side, raised) ---
c.set(22, 18, BONE); c.set(23, 17, BONE)  # upper arm
c.set(24, 16, BONE)  # hand
# sword blade diagonal up-right
c.line(25, 15, 30, 8, SWORD)
c.set(30, 8, SWORD); c.set(29, 7, SWORD)
c.set(29, 9, SWD_D)
c.set(28, 10, SWD_D)
# guard
c.set(24, 15, HILT); c.set(25, 16, HILT)
# grip
c.set(24, 16, HILT)

# --- shield arm (left side, forward) ---
c.set(13, 19, BONE); c.set(12, 20, BONE)  # arm
c.set(11, 20, BONE)
# small round wooden shield
c.circle(9, 21, 3, WOOD)
c.set(9, 21, WOOD_D)  # boss
c.set(8, 20, WOOD_D); c.set(10, 22, WOOD_D)
c.circle(9, 21, 3, WOOD, fill=False)
c.set(6, 21, WOOD_D); c.set(12, 21, WOOD_D)
c.set(9, 18, WOOD_D); c.set(9, 24, WOOD_D)

# --- joint shading (dark elbows/knees) ---
c.set(13, 28, DARK)
c.set(18, 28, DARK)
c.set(22, 18, SHADE)
c.set(12, 20, SHADE)

print(c.stats_text())
finish(c)
