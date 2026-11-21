try:
    from pixelbench_api import *  # noqa: F401,F403
except Exception:
    pass

# ----------------------------------------------------------------- palette
OUT     = '#23262b'   # silhouette outline
BRICK   = '#a8492e'
BRICK_L = '#c06540'
BRICK_D = '#8a3826'
MORTAR  = '#77301f'
ROOF_L  = '#9aa3ad'
ROOF_M  = '#6e7681'
ROOF_D  = '#4a5058'
VENT    = '#8a929c'
VENT_L  = '#a9b1ba'
OPEN    = '#2e3238'   # dark openings / window glass base
GLASS   = '#cfe3ee'   # window reflection
DOOR    = '#3c424a'
DOOR_L  = '#5a636e'
DOOR_D  = '#262b31'
SMOKE   = '#cdd3da'
SMOKE_D = '#a9b0ba'

c = new_canvas(32, 32, name='factory')

# ---------------------------------------------------------- flat roof slab
# y=13 is the exposed parapet edge (the silhouette claims it),
# y=14..16 are the visible top surface and its front shadow.
c.rect(3, 13, 26, 1, ROOF_D)
c.rect(3, 14, 26, 1, ROOF_L)
c.rect(3, 15, 26, 1, ROOF_M)
c.rect(3, 16, 26, 1, ROOF_D)

# ------------------------------------------------------------- brick walls
# 4-row courses: three brick rows then a mortar bed joint (y=20, y=24),
# vertical head joints every 5 px, staggered course to course.
for y in range(17, 28):
    band = (y - 17) // 4
    off = 0 if band % 2 == 0 else 2
    for x in range(4, 28):
        if (y - 17) % 4 == 3:
            col = MORTAR                      # bed joint
        elif (x - 4 + off) % 5 == 0:
            col = MORTAR                      # head joint
        elif x >= 26:
            col = BRICK_D                     # shaded right return
        else:
            cx = (x - 4 + off) // 5
            col = BRICK_L if (cx * 7 + band * 11) % 4 == 0 else BRICK
        c.set(x, y, col)

# -------------------------------------------------------------- foundation
c.rect(3, 28, 26, 1, ROOF_M)
c.rect(3, 29, 26, 1, ROOF_D)

# ---------------------------------------------------------------- chimney
# x=5-8, open dark flue at the top, brick shaft down onto the roof.
c.rect(5, 6, 4, 1, BRICK)                 # rim (outline makes the lip)
c.set(5, 7, BRICK_L)
c.set(6, 7, OPEN); c.set(7, 7, OPEN)      # flue opening
c.set(8, 7, BRICK_D)
for y in range(8, 14):
    if y == 10:
        for x in range(5, 9):
            c.set(x, y, MORTAR)           # one course up the shaft
    else:
        c.set(5, y, BRICK_L)
        c.set(6, y, BRICK)
        c.set(7, y, BRICK)
        c.set(8, y, BRICK_D)

# ---------------------------------------------------- tall vent stack (right)
c.rect(21, 9, 6, 1, ROOF_D)               # cap lip, top
c.rect(21, 10, 6, 1, ROOF_D)              # cap lip, underside
c.rect(22, 11, 4, 3, VENT)                # body down onto the roof
for y in (11, 12, 13):
    c.set(23, y, VENT_L)

# ------------------------------------------------------------- roof vents
c.rect(11, 11, 3, 1, OPEN)                # vent A: dark throat
c.rect(11, 12, 3, 2, VENT)
c.set(12, 12, VENT_L)

c.rect(16, 12, 3, 1, OPEN)                # vent B: low profile
c.rect(16, 13, 3, 1, VENT)
c.set(17, 13, VENT_L)

# ----------------------------------------------------------------- windows
for wx in (7, 14, 21):
    c.rect(wx, 19, 4, 3, OPEN)
    c.set(wx, 19, GLASS)
    c.set(wx + 1, 19, GLASS)

# ------------------------------------------------------------ garage door
c.rect(13, 23, 6, 1, DOOR_L)              # lit top slat
c.rect(13, 24, 6, 1, DOOR_D)
c.rect(13, 25, 6, 1, DOOR)
c.rect(13, 26, 6, 1, DOOR_D)
c.rect(13, 27, 6, 1, DOOR)

# ------------------------------------------------- crisp silhouette outline
c.outline(OUT)

# ------------------------------------------------------ smoke (kept soft)
for x, y, col in [
    (6, 5, SMOKE),  (7, 5, SMOKE_D),
    (6, 4, SMOKE),  (7, 4, SMOKE),
    (7, 3, SMOKE),  (8, 3, SMOKE_D),
    (8, 2, SMOKE),  (9, 2, SMOKE),
    (9, 1, SMOKE_D), (10, 1, SMOKE),
]:
    c.set(x, y, col)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 16)))
print(c.matrix_text(region=(0, 17, 31, 31)))

finish(c)
